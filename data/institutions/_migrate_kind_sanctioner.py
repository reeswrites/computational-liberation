"""One-off: add `kind`, `sanctioner` and `sanctioner_review: derived` to every rule in src/*.yaml (plans/informal-rules.md D1).

Run once from the comp-lib root:  uv run python data/institutions/_migrate_kind_sanctioner.py [--dry]

kind        norm if `implicit: true` else formal (no strategy yet).
sanctioner  `none` when or_else is null; else derived from the *attribute role* of the or_else target rule (resolved
            within the same entry, through `extends`) by the table below (case-insensitive substring of the role name,
            first row hit wins); no hit -> institution, reported as unmatched.
Edits are text insertions after each rule's `implicit:` line, so the rest of the file is untouched.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build  # noqa: E402

TABLE = [
    ("state", "state court judge officer police agency caseworker legislature government clerk immigration"),
    ("institution", "hospital committee employer airline library platform school kibbutz carrier landlord lessor clinic provider"),
    ("family", "husband wife parent mother father daughter son family spouse guardian"),
    ("peers", "suitor member neighbour neighbor peer community villager worker tenant"),
    ("self", "self"),
]


def derive(role: str):
    r = role.lower()
    for val, words in TABLE:
        if any(w in r for w in words.split()):
            return val, True
    return "institution", False


def main(dry: bool) -> None:
    order, raws = build.load_sources()
    report, unmatched, counts = [], {}, {}
    for eid in order:
        resolved = build.resolve(eid, raws)
        by_id = {r["id"]: r for r in resolved["rules"]}
        path = build.SRC / f"{eid}.yaml"
        lines = path.read_text(encoding="utf-8").split("\n")
        out = []
        for i, ln in enumerate(lines):
            out.append(ln)
            m = re.match(r"^(\s+)implicit: (true|false)$", ln)
            if not m:
                continue
            ind, implicit = m.group(1), m.group(2) == "true"
            j = i
            while not re.match(r"^\s*- id: ", lines[j]):
                j -= 1
            rid = lines[j].split("- id:")[1].strip()
            k = j
            oe = None
            while k < len(lines) and (k == j or not re.match(r"^\s*- id: ", lines[k])):
                mm = re.match(rf"^{ind}or_else: (.+)$", lines[k])
                if mm:
                    oe = None if mm.group(1) == "null" else mm.group(1)
                k += 1
            if oe is None:
                san, tgt_attr = "none", None
            else:
                tgt_attr = by_id[oe]["attribute"]
                san, hit = derive(tgt_attr)
                if not hit:
                    unmatched[(eid, rid, tgt_attr)] = san
            counts[san] = counts.get(san, 0) + 1
            if oe is not None:
                report.append((eid, rid, oe, tgt_attr, san))
            out += [f"{ind}kind: {'norm' if implicit else 'formal'}", f"{ind}sanctioner: {san}",
                    f"{ind}sanctioner_review: derived"]
        if not dry:
            path.write_text("\n".join(out), encoding="utf-8")
    for row in report:
        print("\t".join(map(str, row)))
    print("counts", counts)
    print("unmatched", unmatched)


if __name__ == "__main__":
    main("--dry" in sys.argv)
