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

`--cards` also writes docs/cards/<id>.md (one human-readable card per entry) and docs/cards/README.md, generated
from the same resolved entries. `--check` rebuilds JSON and cards into a temp dir and fails on any difference, on a
rule with an empty `plain` or `source`, and on an `extends` cycle.

Usage (from the comp-lib root):  uv run python data/institutions/build.py [--write] [--cards] | --check
"""
from __future__ import annotations

import argparse
import copy
import difflib
import json
import re
import sys
import tempfile
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
SRC = HERE / "src"
CARDS = HERE.parent.parent / "docs" / "cards"
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


# ---------------------------------------------------------------- cards
def _cell(s) -> str:
    return str(s).replace("|", "\\|").replace("\n", " ").strip()


def _code(s) -> str:
    return f"`{_cell(s)}`"


def _trunc(s, n) -> str:
    s = " ".join(str(s).split())
    return s if len(s) <= n else s[: n - 3].rstrip() + "..."


def short_source(s, n=80) -> str:
    """First ~n chars of a source, with its first URL kept when the cut would drop it."""
    s = " ".join(str(s).split())
    if len(s) <= n + 20:
        return _cell(s)
    m = re.search(r"https?://[^\s)\]]+", s)
    cut = s[:n].rstrip() + "..."
    if m and m.end() > n:
        cut += " " + m.group(0)
    return _cell(cut)


def deontic_cell(r) -> str:
    d = r["deontic"].replace("_", " ")
    if r["deontic"] == "must_not" and r.get("or_else") is None:
        d += " (disability)"
    if r.get("implicit"):
        d += " (implicit)"
    return d


def or_else_cell(r, by_id) -> str:
    oe = r.get("or_else")
    if oe is None:
        return "none"
    t = by_id.get(oe)
    return f"{oe} {_code(t['aim'])}" if t else oe


def _delta_lines(raw, base) -> list:
    base_by = {r["id"]: r for r in base["rules"]}
    out = []
    for rid in raw.get("rules_drop", ()):
        out.append(f"- {rid} dropped: {base_by[rid]['plain']}")
    for r in raw.get("rules_replace", ()):
        out.append(f"- {r['id']} replaced: was \"{base_by[r['id']]['plain']}\" now \"{r['plain']}\"")
    for r in raw.get("rules_add", ()):
        out.append(f"- {r['id']} added: {r['plain']}")
    for l in LISTS:
        for verb, word in (("drop", "dropped"), ("set", "changed"), ("add", "added")):
            v = raw.get(f"{l}_{verb}")
            if v:
                names = [x["name"] for x in v] if verb == "add" else list(v)
                out.append(f"- {l} {word}: {', '.join(names)}")
    for k in raw.get("keys_drop", ()):
        out.append(f"- field {k} dropped")
    over = [k for k in raw if k not in RESERVED and k not in ("id", "name", "notes", "source_text")
            and raw[k] != base.get(k)]
    if over:
        out.append(f"- fields overridden: {', '.join(over)}")
    return out


def pair_lines(e, raws, resolved) -> list:
    """Diff against the base for a delta entry; the entries extending it for a base entry; pair fields in words."""
    raw = raws[e["id"]]
    out = []
    base_id = raw.get("extends")
    if base_id:
        out.append(f"Extends [{base_id}]({base_id}.md); one line per change:")
        out += _delta_lines(raw, resolved[base_id])
    else:
        kids = [i for i, r in raws.items() if r.get("extends") == e["id"]]
        if kids:
            out.append("Extended by: " + ", ".join(f"[{k}]({k}.md)" for k in kids))
    mp = e.get("minimal_pair_of")
    if mp:
        if mp.get("differs_on"):
            diff = f"; the pair differs on property {mp['differs_on']}"
        else:
            diff = "; no layer-1 property separates the pair" if "differs_on" in mp else ""
        out.append(f"Minimal pair of [{mp['id']}]({mp['id']}.md), differing in rule {mp.get('rule', '?')}{diff}.")
    for i, r in resolved.items():
        m = r.get("minimal_pair_of")
        if m and m["id"] == e["id"]:
            out.append(f"[{i}]({i}.md) is a minimal pair of this entry (rule {m.get('rule', '?')}).")
    for key, word in (("isomorphic_to", "Isomorphic to"), ("not_isomorphic_to", "Not isomorphic to"),
                      ("not_isomorphic_to_control", "Contrasts with controls")):
        v = e.get(key) or []
        if v:
            items = [(x["id"] + (f" ({x['level']})" if x.get("level") else "")) if isinstance(x, dict) else x
                     for x in v]
            out.append(f"{word}: {', '.join(items)}")
    return out


def card(e, raws, resolved, props) -> str:
    raw = raws[e["id"]]
    by_id = {r["id"]: r for r in e["rules"]}
    own = {}
    for k, tag in (("rules_add", "added"), ("rules_replace", "replaced")):
        for r in raw.get(k, ()):
            own[r["id"]] = tag
    L = [f"# {e['id']}", "", f"**{e['name']}**", "", "> " + _trunc(e.get("source_text", ""), 400), "", "## Roles", ""]
    L += [f"- **{r['name']}**: {_cell(r.get('gloss', ''))}" for r in e["roles"]]
    L += ["", "## Rules", "",
          "| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | source |",
          "|---|---|---|---|---|---|---|---|---|"]
    for r in e["rules"]:
        rid = r["id"] + (f" ({own[r['id']]})" if r["id"] in own else "")
        L.append("| " + " | ".join([
            rid, r["attribute"], deontic_cell(r), _code(r["aim"]), _code(r["conditions"]), or_else_cell(r, by_id),
            r.get("strand") or "-", _cell(r["plain"]), short_source(r["source"])]) + " |")
    dc = [a["name"] for a in e["actions"] if a.get("default_capacity")]
    L += ["", "**Default capacities** (enabled unless an express disability bars them): "
          + (", ".join(dc) if dc else "none"), "", "## Expected properties", "",
          "| property | kind | expected | meaning |", "|---|---|---|---|"]
    pm = {p["name"]: p for p in props}
    for name, verdict in e.get("expected_properties", {}).items():
        p = pm.get(name, {})
        L.append(f"| {name} | {p.get('kind', '?')} | {verdict} | {_cell(_trunc(p.get('gloss', ''), 110))} |")
    L += ["", "## Pairs", ""]
    L += pair_lines(e, raws, resolved) or ["No pair relations."]
    L += ["", "## Notes", "", e.get("notes", "").rstrip(), ""]
    return "\n".join(L)


def partners(eid, raws, resolved) -> list:
    out = []
    base = raws[eid].get("extends")
    if base:
        out.append(f"{base} (extends)")
    out += [f"{i} (extended by)" for i, r in raws.items() if r.get("extends") == eid]
    seen = {x.split(" ")[0] for x in out}
    mp = resolved[eid].get("minimal_pair_of")
    if mp and mp["id"] not in seen:
        out.append(f"{mp['id']} (minimal pair)")
        seen.add(mp["id"])
    for i, r in resolved.items():
        m = r.get("minimal_pair_of")
        if m and m["id"] == eid and i not in seen:
            out.append(f"{i} (minimal pair)")
            seen.add(i)
    return out


def render_cards(order, raws, resolved_list, props) -> dict:
    resolved = {e["id"]: e for e in resolved_list}
    files = {f"{i}.md": card(resolved[i], raws, resolved, props) for i in order}
    idx = ["# Institution cards", "",
           "Generated by `data/institutions/build.py --cards` from `data/institutions/src/`. Do not edit.", ""]
    for i in order:
        p = partners(i, raws, resolved)
        idx.append(f"- [{i}]({i}.md): {resolved[i]['name']}" + (f" | pairs: {'; '.join(p)}" if p else ""))
    files["README.md"] = "\n".join(idx) + "\n"
    return files


def write_cards(out: Path, files: dict):
    out.mkdir(parents=True, exist_ok=True)
    for f in out.glob("*.md"):
        if f.name not in files:
            f.unlink()
    for name, text in files.items():
        (out / name).write_text(text, encoding="utf-8")


def cards_problems(files: dict, out: Path = CARDS) -> list:
    errs = []
    have = {f.name for f in out.glob("*.md")} if out.exists() else set()
    for name in sorted(set(files) | have):
        if name not in files:
            errs.append(f"docs/cards/{name} is stale (no such entry); run build.py --write --cards")
        elif name not in have:
            errs.append(f"docs/cards/{name} is missing; run build.py --write --cards")
        elif (out / name).read_text(encoding="utf-8") != files[name]:
            errs.append(f"docs/cards/{name} differs from the build of src/; run build.py --write --cards")
    return errs


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


def check():
    order, raws = load_sources()
    resolved, inst, props = build_all()
    errs, _ = problems(resolved, True)
    with tempfile.TemporaryDirectory() as td:
        write(Path(td), inst, props)
        for name in ("institutions.json", "properties.json"):
            new = (Path(td) / name).read_text(encoding="utf-8")
            old = (HERE / name).read_text(encoding="utf-8")
            if new != old:
                d = list(difflib.unified_diff(old.splitlines(), new.splitlines(), f"committed/{name}", f"built/{name}", lineterm="", n=1))
                errs.append(f"{name} differs from the build of src/ ({len(d)} diff lines); run build.py --write\n" + "\n".join(d[:30]))
        # Regenerate the cards into a temp dir and compare the whole set with docs/cards, so a stale or stray card fails.
        write_cards(Path(td) / "cards", render_cards(order, raws, resolved, props))
        fresh = {f.name: f.read_text(encoding="utf-8") for f in (Path(td) / "cards").glob("*.md")}
        errs += cards_problems(fresh)
    for m in errs:
        print("ERROR:", m)
    if not errs:
        print(f"ok: {len(inst)} institutions, {len(props)} properties, JSON and {len(fresh)} cards match src/")
    return 1 if errs else 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true", help="rebuild JSON and cards into a temp dir, diff against the committed files")
    ap.add_argument("--write", action="store_true", help="write institutions.json and properties.json (default)")
    ap.add_argument("--cards", action="store_true", help="write docs/cards/*.md (with --check they are always compared)")
    a = ap.parse_args(argv)
    if a.check:
        return check()
    order, raws = load_sources()
    resolved, inst, props = build_all()
    errs, _ = problems(resolved, False)
    if errs:
        print("\n".join("ERROR: " + m for m in errs))
        return 1
    if a.write or not a.cards:
        write(HERE, inst, props)
        print(f"wrote institutions.json ({len(inst)}) and properties.json ({len(props)})")
    if a.cards:
        files = render_cards(order, raws, resolved, props)
        write_cards(CARDS, files)
        print(f"wrote {len(files)} files to docs/cards/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
