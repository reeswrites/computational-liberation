# airline-flight

**Airline flight (permanent negative control, EXPECTED to match the care+control cluster)**

> Reconstruction, not a quotation: a flight's crew must care for passengers aboard, may restrain a disruptive passenger, and a passenger must not leave in flight (may leave on the ground); the passenger may complain. Supplied by the third review (2026-11-03) as a structural negative control for the care+control match.

## Roles

- **crew**: cabin crew; serves and may restrain
- **passenger**: a passenger aboard; the counterparty

## Rules

| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | source |
|---|---|---|---|---|---|---|---|---|
| R1 | crew | may | `(board c p)` | `(not (aboard p))` | none | tying | The crew may board the passenger when the passenger is not aboard. | Reconstruction from the third review's 6-rule sketch (no statute opened): 14 CFR... |
| R2 | crew | must | `(provides_care c p)` | `(aboard p)` | none | superadditive | The crew providing care to the passenger must hold when the passenger is aboard (14 CFR 91.11 / 121.580, unverified). | Reconstruction from the third review's 6-rule sketch (no statute opened): 14 CFR... |
| R3 | crew | may | `(restrain c p)` | `(and (aboard p) (disruptive p))` | none | rival | The crew may restrain the passenger when the passenger is aboard and disruptive (14 CFR 91.11 / 121.580, unverified). | Reconstruction from the third review's 6-rule sketch (no statute opened): 14 CFR... |
| R4 | passenger | must not (disability) | `(leave p)` | `(aboard p)` | none | rival | The passenger cannot leave while aboard: no such power exists (14 CFR 91.11 / 121.580, unverified). | Reconstruction from the third review's 6-rule sketch (no statute opened): 14 CFR... |
| R6 | passenger | may | `(complain p)` | `true` | none | tying | The passenger may complain at any time. | Reconstruction from the third review's 6-rule sketch (no statute opened): 14 CFR... |

**Default capacities** (enabled unless an express disability bars them): leave

## Expected properties

| property | kind | expected | meaning |
|---|---|---|---|
| subject_cannot_exit | freedom | reachable | No exit action is available to the subject, or every exit is sanctioned. scope=interaction: exit from the c... |
| dependent_cannot_exit | freedom | reachable | Some subject of the institution (the dependent party) has no permitted exit at step t. Alias of subject_can... |
| care_and_sanction_same_role | structure | holds_to_k | Whoever provides care to a subject also holds sanction power over that subject (care + control bundled in o... |

## Pairs

No pair relations.

## Notes

EXPECTED-MATCH control (`expected_control_match: true`; third review 2026-11-03). PREREGISTERED before any run: airline-flight matches police-crisis, cps and coverture-household at guard+strands (care R2 superadditive ~ care, R3 rival ~ chastise/detain/remove, R4 exit bar ~ exit bar). The match is structural: in-flight custody has the same care + restraint + exit-bar form, so it is a finding about the form, not a failure of the encoding. Retagging R2 superadditive -> tying removes every match: the strand tags are load-bearing and the tags are human inputs. Why it is not in `not_isomorphic_to_control`: gate (b) fails on any match, and the gate has no expected-match mode (philosophy-engine is not edited here); `rules_gate` still lists it as an ordinary dataset entry. Expectations copied from police-crisis minus no_standing and are unverified until check-all. 6 rules (the review's list), not 10.
