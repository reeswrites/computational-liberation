"""One-off: convert the committed institutions.json / properties.json into src/*.yaml.

Kept in the repo as the record of how the YAML was derived. Not part of the build; running it again overwrites
src/ from the JSON, so do not run it once src/ has been edited by hand.

Each rule gains `plain: ""` (a later pass fills it; nothing is invented here). Entries named in DELTAS become
`extends` of their base when the delta reproduces the committed entry exactly (key order included); otherwise
they are written standalone and reported.
"""
import copy
import json
from pathlib import Path

import build
from build import HERE, SRC, dump_yaml

# entry -> base. Chain order for the MWPA entries follows the prev links of _gen_institutions._mwpa(...).
DELTAS = {
    "mwpa-creditor-exemption": "coverture-household",
    "mwpa-property": "mwpa-creditor-exemption",
    "mwpa-earnings": "mwpa-property",
    "mwpa-sole-trader": "mwpa-earnings",
    "mwpa-suit": "mwpa-sole-trader",
    "mwpa-property-narrowed": "mwpa-property",
    "companion-guardianship": "companion-ownership",
    "companion-guardian-renamed": "companion-ownership",
    "kibbutz-childrens-house-no-implicit": "kibbutz-childrens-house",
    "footbinding-no-pledge": "footbinding",
    "gestational-surrogacy": "ectogenesis",
    "transferable-leave": "paternity-quota",
}
HEAD = ("id", "name", "extends")


def with_plain(rule):
    out = {}
    for k, v in rule.items():
        out[k] = v
        if k == "id":
            out["plain"] = ""
    return out


def named_delta(E, B, kind):
    """(drop, set, add) turning B[kind] into E[kind], or None if it is not expressible (order, removed fields)."""
    bn = {x["name"]: x for x in B}
    en = {x["name"]: x for x in E}
    drop = [n for n in bn if n not in en]
    add = [x for n, x in en.items() if n not in bn]
    sets = {}
    for n, x in en.items():
        if n in bn and x != bn[n]:
            if any(k not in x for k in bn[n]):
                return None
            sets[n] = {k: v for k, v in x.items() if bn[n].get(k, object()) != v or k not in bn[n]}
    return drop, sets, add


def delta(E, B):
    d = {"id": E["id"], "name": E["name"], "extends": B["id"]}
    for l in build.LISTS:
        r = named_delta(E[l], B[l], l)
        if r is None:
            return None
        drop, sets, add = r
        if drop: d[f"{l}_drop"] = drop
        if sets: d[f"{l}_set"] = sets
        if add: d[f"{l}_add"] = add
    br = {r["id"]: r for r in B["rules"]}
    er = {r["id"]: r for r in E["rules"]}
    drop = [i for i in br if i not in er]
    repl = [with_plain(r) for i, r in er.items() if i in br and br[i] != r]
    add = [with_plain(r) for i, r in er.items() if i not in br]
    if drop: d["rules_drop"] = drop
    if repl: d["rules_replace"] = repl
    if add: d["rules_add"] = add
    kd = [k for k in B if k not in E]
    if kd: d["keys_drop"] = kd
    for k, v in E.items():
        if k in build.LISTS or k in ("rules", "id", "name"):
            continue
        if k not in B or B[k] != v:
            d[k] = v
    return d


def main():
    inst = json.loads((HERE / "institutions.json").read_text())
    props = json.loads((HERE / "properties.json").read_text())
    by_id = {e["id"]: e for e in inst}
    SRC.mkdir(exist_ok=True)
    raws, report = {}, []
    for e in inst:
        std = {k: ([with_plain(r) for r in v] if k == "rules" else v) for k, v in e.items()}
        raws[e["id"]] = std
        base = DELTAS.get(e["id"])
        if not base:
            continue
        d = delta(e, by_id[base])
        if d is None:
            report.append((e["id"], base, "standalone: not expressible as a delta"))
            continue
        trial = dict(raws); trial[e["id"]] = d
        got = build.strip(build.resolve(e["id"], trial))
        if json.dumps(got) != json.dumps(e):
            report.append((e["id"], base, "standalone: delta does not reproduce the entry"))
            continue
        nrules = len(e["rules"])
        changed = len(d.get("rules_drop", [])) + len(d.get("rules_replace", [])) + len(d.get("rules_add", []))
        if changed * 2 > nrules + len(by_id[base]["rules"]):  # a rename-style delta restates most rules: not worth it
            report.append((e["id"], base, f"standalone: delta touches {changed} of {nrules} rules"))
            continue
        raws[e["id"]] = d
        report.append((e["id"], base, f"extends: drop {len(d.get('rules_drop', []))}, replace {len(d.get('rules_replace', []))}, add {len(d.get('rules_add', []))}"))
    for i, r in raws.items():
        (SRC / f"{i}.yaml").write_text(dump_yaml(r), encoding="utf-8")
    (SRC / "_order.yaml").write_text(dump_yaml([e["id"] for e in inst]), encoding="utf-8")
    (SRC / "properties.yaml").write_text(dump_yaml(props), encoding="utf-8")
    for r in report:
        print(*r)
    print("wrote", len(raws), "entries + properties.yaml + _order.yaml")


if __name__ == "__main__":
    main()
