"""Faithfulness batch 2, P4 (plans/sourcing.md): P3 plus the facility's own custody power (WIC 5150(a)).

Writes a variant of data/institutions/institutions.json to <out>/institutions.json; the dataset is not changed.
Usage (from the comp-lib root):  uv run python scripts/faithfulness_batch2_p4.py <out>
then `phil rules gate|diff|iso|ablate --institutions <out>/institutions.json`.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from faithfulness_batch2_p3 import ROOT, variant as p3  # noqa: E402

SOURCE = ("Faithfulness batch 2, P4 (experiment): Cal. Welf. & Inst. Code s. 5150(a), read 2026-11-06 at "
          "https://california.public.law/codes/ca_welf_and_inst_code_section_5150: the custody power belongs to 'a "
          "peace officer, professional person in charge of a facility designated by the county for evaluation and "
          "treatment, member of the attending staff' (and others), who 'may, upon probable cause, take, or cause to be "
          "taken, the person into custody for a period of up to 72 hours'.")


def variant(data):
    data = p3(data)
    pc = next(x for x in data if x["id"] == "police-crisis")
    F = {f["name"]: f for f in pc["fluents"]}
    F["can_sanction"]["derived"] = ("(or (exists ((f agent)) (enabled detain o f s)) (enabled use_force o s) "
                                    "(enabled hold o s))")
    F["can_sanction"]["arg_roles"] = None
    pc["actions"].append({"name": "hold", "args": ["f", "s"],
                          "effects": [{"fluent": "in_custody", "args": ["s"], "value": True},
                                      {"fluent": "provides_care", "args": ["f", "s"], "value": True}]})
    pc["rules"].append({"id": "R11", "attribute": "facility", "deontic": "may", "aim": "(hold f s)",
                        "conditions": "(and (in_crisis s) (danger s))", "or_else": None, "strand": "rival",
                        "implicit": False, "source": SOURCE})
    return data


if __name__ == "__main__":
    out = Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    data = json.loads((ROOT / "data/institutions/institutions.json").read_text(encoding="utf-8"))
    (out / "institutions.json").write_text(json.dumps(variant(data), indent=1), encoding="utf-8")
    print(out / "institutions.json")
