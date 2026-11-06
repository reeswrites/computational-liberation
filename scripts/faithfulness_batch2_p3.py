"""Faithfulness batch 2, P3 (plans/sourcing.md): police-crisis R2 with the care duty on the facility (WIC 5150(a), (c)).

Writes a variant of data/institutions/institutions.json to <out>/institutions.json; the dataset is not changed.
Usage (from the comp-lib root):
  uv run python scripts/faithfulness_batch2_p3.py <out>
  uv run phil rules gate --institutions <out>/institutions.json
  uv run phil rules diff --baseline data/verdicts-baseline.json --institutions <out>/institutions.json --no-cache
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def variant(data):
    pc = next(x for x in data if x["id"] == "police-crisis")
    F = {f["name"]: f for f in pc["fluents"]}
    A = {a["name"]: a for a in pc["actions"]}
    R = {r["id"]: r for r in pc["rules"]}
    F["provides_care"]["arg_roles"] = ["facility", "subject"]
    F["can_sanction"]["derived"] = "(or (exists ((f agent)) (enabled detain o f s)) (enabled use_force o s))"
    for name in ("dispatch_officer", "leave"):
        A[name]["effects"] = [e for e in A[name]["effects"] if e["fluent"] != "provides_care"]
    A["assess"].update(args=["f", "s"], effects=[{"fluent": "provides_care", "args": ["f", "s"], "value": True}])
    A["withdraw"].update(args=["f", "s"], effects=[{"fluent": "provides_care", "args": ["f", "s"], "value": False}])
    A["detain"].update(args=["o", "f", "s"], effects=[{"fluent": "in_custody", "args": ["s"], "value": True},
                                                      {"fluent": "provides_care", "args": ["f", "s"], "value": True}])
    R["R2"].update(attribute="facility", aim="(provides_care f s)", conditions="(in_custody s)")
    R["R3"]["aim"] = "(detain o f s)"
    return data


if __name__ == "__main__":
    out = Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    data = json.loads((ROOT / "data/institutions/institutions.json").read_text(encoding="utf-8"))
    (out / "institutions.json").write_text(json.dumps(variant(data), indent=1), encoding="utf-8")
    print(out / "institutions.json")
