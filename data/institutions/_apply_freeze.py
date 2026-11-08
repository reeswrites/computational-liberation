"""One-off: write the engine's binding freeze into src/*.yaml (plans/composition.md P3).

Input: the JSON of `uv run phil rules freeze-bindings --json` (path given as argv[1]; `--dry` to only report).
Each row with action `written` becomes a `var_roles` entry on the rule, in the file where that rule is DEFINED
(the nearest of: the entry's own `rules` / `rules_add` / `rules_replace`, else its `extends` ancestor). Inherited rules
show up under every descendant in the JSON, so each (file, rule, variable) is written once; descendants must agree,
else the rule is skipped and reported. Untyped, already_explicit and conflict rows are never touched.
Edits are text insertions (the rest of each file is byte-identical): a new `var_roles` goes before the rule's
`choices:` if it has one, else at the end of the rule block; an existing mapping gets the new lines appended.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build  # noqa: E402


def defining(eid, rid, raws):
    raw = raws[eid]
    for key in ("rules", "rules_add", "rules_replace"):
        if any(r.get("id") == rid for r in raw.get(key, ()) or ()):
            return eid
    if "extends" in raw:
        return defining(raw["extends"], rid, raws)
    raise SystemExit(f"{eid}: rule {rid} defined nowhere")


def main(path, dry):
    _, raws = build.load_sources()
    data = json.load(open(path, encoding="utf-8"))
    want, seen = {}, {}
    for ent in data:
        for row in ent["rows"]:
            if row["action"] != "written":
                continue
            f = defining(ent["entry"], row["rule"], raws)
            k = (f, row["rule"], row["variable"])
            seen.setdefault(k, set()).add(row["role"])
            want.setdefault(k, row["role"])
    skipped = {k for k, v in seen.items() if len(v) > 1}
    for k in sorted(skipped):
        print("SKIP disagreement", k, seen[k])
    skip_rules = {(f, r) for f, r, _ in skipped}
    byfile = {}
    for (f, r, v), role in want.items():
        if (f, r) in skip_rules:
            continue
        byfile.setdefault(f, {}).setdefault(r, []).append((v, role))
    total = 0
    for f, rules in byfile.items():
        p = build.SRC / f"{f}.yaml"
        lines = p.read_text(encoding="utf-8").split("\n")
        # rule blocks: start at `- id: X`, end before the next `- ` / top-level key
        starts = [i for i, ln in enumerate(lines) if re.match(r"^- id: ", ln)]
        todo = dict(rules)
        for i in reversed(starts):
            rid = lines[i].split("- id:")[1].strip()
            if rid not in todo:
                continue
            j = i + 1
            while j < len(lines) and not re.match(r"^(- |[A-Za-z_])", lines[j]):
                j += 1
            while lines[j - 1] == "":  # keep trailing blank lines outside the block
                j -= 1
            new = [f"    {v}: {role}" for v, role in todo.pop(rid)]
            total += len(new)
            vr = next((k for k in range(i, j) if lines[k] == "  var_roles:"), None)
            if vr is not None:
                end = vr + 1
                while end < j and lines[end].startswith("    "):
                    end += 1
                lines[end:end] = new
            else:
                ch = next((k for k in range(i, j) if lines[k].startswith("  choices:")), None)
                at = ch if ch is not None else j
                lines[at:at] = ["  var_roles:"] + new
        assert not todo, (f, todo)
        if not dry:
            p.write_text("\n".join(lines), encoding="utf-8")
    print(f"bindings written: {total}; files: {len(byfile)}; skipped: {len(skipped)}")


if __name__ == "__main__":
    main(sys.argv[1], "--dry" in sys.argv)
