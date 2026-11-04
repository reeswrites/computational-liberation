"""Build institutions.json and properties.json from src/*.yaml.

src/<id>.yaml is the source of truth for one institution; src/properties.yaml for the named properties;
src/_order.yaml lists the institution ids in output order (the JSON is order-sensitive: entry order and key
order are kept exactly). Never hand-edit the JSON.

An entry is either standalone (every field of the engine schema `InstitutionJSON`, plus per rule a `plain`
sentence and optional `choices` note) or a delta:

    extends: <other id>
    rules_drop:    [R1]            # ids removed from the base
    rules_replace: [{id: R2, ...}] # rule with the same id, replaced in place
    rules_add:     [{id: R13, ...}]# appended after the base's remaining rules
    roles_drop / roles_set / roles_add, fluents_*, actions_*   # same three verbs, keyed by name
    keys_drop: [initial]           # top-level keys the base has and this entry does not
    <any other key>: value         # overrides that key wholesale (name, notes, expected_properties, ...)

Order of application: drops, then replaces/sets, then adds, then overrides. `plain` and `choices` are for
human readers; the engine schema does not carry them, so the build strips them before writing JSON.

Usage (from the comp-lib root):  uv run python data/institutions/build.py [--write | --check [--require-plain]]
"""
from __future__ import annotations

import argparse
import copy
import difflib
import json
import sys
import tempfile
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
SRC = HERE / "src"
STRIP_RULE_KEYS = ("plain", "choices")
LISTS = ("roles", "fluents", "actions")
RESERVED = {"extends", "rules_drop", "rules_replace", "rules_add", "keys_drop"} | {
    f"{l}_{v}" for l in LISTS for v in ("drop", "set", "add")}


# ---------------------------------------------------------------- YAML in and out
class _Dumper(yaml.SafeDumper):
    def ignore_aliases(self, data):  # no anchors or aliases in the sources
        return True


def _str(dumper, s):
    return dumper.represent_scalar("tag:yaml.org,2002:str", s, style="|" if "\n" in s else None)


def _list(dumper, seq):
    flow = all(isinstance(x, (str, int, float, bool)) or x is None for x in seq) and len(repr(seq)) < 72
    return dumper.represent_sequence("tag:yaml.org,2002:seq", seq, flow_style=flow)


_Dumper.add_representer(str, _str)
_Dumper.add_representer(list, _list)


def dump_yaml(obj) -> str:
    return yaml.dump(obj, Dumper=_Dumper, sort_keys=False, allow_unicode=True, width=1_000_000,
                     default_flow_style=False)


def load_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def dump_json(obj) -> str:
    # Same call as the retired generators: json.dump(x, f, indent=1), then a newline. ensure_ascii and key order
    # are the json defaults / the order of the source.
    return json.dumps(obj, indent=1) + "\n"


# ---------------------------------------------------------------- resolution
def load_sources(src: Path = SRC):
    order = load_yaml(src / "_order.yaml")
    raws = {i: load_yaml(src / f"{i}.yaml") for i in order}
    for i, r in raws.items():
        if r.get("id") != i:
            raise SystemExit(f"src/{i}.yaml: id is {r.get('id')!r}, expected {i!r}")
    return order, raws


def _patch_named(items, drop, sets, add, kind, eid):
    names = {x["name"] for x in items}
    for n in list(drop) + list(sets):
        if n not in names:
            raise SystemExit(f"{eid}: {kind}_drop/_set names unknown {n!r}")
    out = []
    for x in items:
        if x["name"] in drop:
            continue
        if x["name"] in sets:
            x = {**x, **sets[x["name"]]}
        out.append(x)
    return out + copy.deepcopy(list(add))


def resolve(eid, raws, stack=()):
    """The entry with `extends` expanded; rules keep `plain` / `choices`."""
    if eid in stack:
        raise SystemExit("extends cycle: " + " -> ".join(stack + (eid,)))
    if eid not in raws:
        raise SystemExit(f"{stack[-1] if stack else '?'}: extends unknown entry {eid!r}")
    raw = raws[eid]
    if "extends" not in raw:
        return copy.deepcopy(raw)
    e = resolve(raw["extends"], raws, stack + (eid,))
    for l in LISTS:
        e[l] = _patch_named(e[l], raw.get(f"{l}_drop", ()), raw.get(f"{l}_set", {}), raw.get(f"{l}_add", ()), l, eid)
    ids = {r["id"] for r in e["rules"]}
    drop = set(raw.get("rules_drop", ()))
    repl = {r["id"]: r for r in raw.get("rules_replace", ())}
    for rid in drop | set(repl):
        if rid not in ids:
            raise SystemExit(f"{eid}: rules_drop/rules_replace names unknown rule {rid!r}")
    e["rules"] = ([copy.deepcopy(repl.get(r["id"], r)) for r in e["rules"] if r["id"] not in drop]
                  + copy.deepcopy(list(raw.get("rules_add", ()))))
    for k in raw.get("keys_drop", ()):
        e.pop(k, None)
    for k, v in raw.items():
        if k not in RESERVED:
            e[k] = copy.deepcopy(v)
    return e


def strip(entry):
    e = dict(entry)
    e["rules"] = [{k: v for k, v in r.items() if k not in STRIP_RULE_KEYS} for r in entry["rules"]]
    return e


def build_all(src: Path = SRC):
    order, raws = load_sources(src)
    resolved = [resolve(i, raws) for i in order]
    return resolved, [strip(e) for e in resolved], load_yaml(src / "properties.yaml")


# ---------------------------------------------------------------- commands
def problems(resolved, require_plain):
    errs, warns = [], []
    for e in resolved:
        for r in e["rules"]:
            where = f"{e['id']} {r['id']}"
            if not r.get("source"):
                errs.append(f"{where}: empty source")
            if not r.get("plain"):
                (errs if require_plain else warns).append(f"{where}: empty plain")
    return errs, warns


def write(out: Path, inst, props):
    (out / "institutions.json").write_text(dump_json(inst), encoding="utf-8")
    (out / "properties.json").write_text(dump_json(props), encoding="utf-8")


def check(require_plain):
    resolved, inst, props = build_all()
    errs, warns = problems(resolved, require_plain)
    with tempfile.TemporaryDirectory() as td:
        write(Path(td), inst, props)
        for name in ("institutions.json", "properties.json"):
            new = (Path(td) / name).read_text(encoding="utf-8")
            old = (HERE / name).read_text(encoding="utf-8")
            if new != old:
                d = list(difflib.unified_diff(old.splitlines(), new.splitlines(), f"committed/{name}", f"built/{name}", lineterm="", n=1))
                errs.append(f"{name} differs from the build of src/ ({len(d)} diff lines); run build.py --write\n" + "\n".join(d[:30]))
    if warns:
        print(f"WARNING: {len(warns)} rules have an empty plain (an error with --require-plain)")
    for m in errs:
        print("ERROR:", m)
    if not errs:
        print(f"ok: {len(inst)} institutions, {len(props)} properties, JSON matches src/")
    return 1 if errs else 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true", help="build into a temp dir, diff against the committed JSON")
    ap.add_argument("--write", action="store_true", help="write institutions.json and properties.json (default)")
    ap.add_argument("--require-plain", action="store_true", help="with --check: an empty plain is an error")
    a = ap.parse_args(argv)
    if a.check:
        return check(a.require_plain)
    resolved, inst, props = build_all()
    errs, _ = problems(resolved, False)
    if errs:
        print("\n".join("ERROR: " + m for m in errs))
        return 1
    write(HERE, inst, props)
    print(f"wrote institutions.json ({len(inst)}) and properties.json ({len(props)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
