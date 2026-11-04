# companion-guardian-renamed

**Companion ownership with 'owner' renamed 'guardian' (municipal and state guardian wording ordinances)**

> 'Wherever the word "owner" shall appear in this chapter it shall also mean and may be interchanged with the word "guardian"', R.I. Gen. Laws s. 4-13-41 (P.L. 2001 ch. 72 s. 3), read at https://webserver.rilegislature.gov/Statutes/TITLE4/4-13/4-13-41.htm. Boulder, Colorado made the same owner->guardian wording change in its animal ordinances in July 2000; the assistant city attorney who rewrote...

## Roles

- **guardian**: the person holding title to the animal; the ordinance calls them guardian
- **animal**: the companion animal; the subject
- **state**: animal control / prosecutor
- **court**: civil court; here, has no best-interest power

## Rules

| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | source |
|---|---|---|---|---|---|---|---|---|
| R1 | guardian | may | `(transfer g a o2)` | `(owns g a)` | none | rival | The guardian may transfer the animal to another when the guardian owns it (R.I. Gen. Laws 4-13-41). | property status of companion animals; R.I. Gen. Laws s. 4-13-41 (P.L. 2001 ch. 7... https://webserver.rilegislature.gov/Statutes/TITLE4/4-13/4-13-41.htm. |
| R2 | guardian | may | `(euthanize g a)` | `(owns g a)` | none | rival | The guardian may have the animal euthanized when the guardian owns it. | owner may have the animal euthanized by a veterinarian. UNVERIFIED (general know... |
| R3 | guardian | must not | `(abandon g a)` | `(owns g a)` | R4 `(prosecute state g)` | rival | The guardian must not abandon the animal when the guardian owns it, or else the state may prosecute (R4) (Cal. Penal Code 597s). | Cal. Penal Code s. 597s(a); https://law.justia.com/codes/california/2015/code-pe... https://law.justia.com/codes/california/2015/code-pen/part-1/title-14/section-597s/ |
| R4 | state | may | `(prosecute state g)` | `(abandoned a)` | none | rival | The state may prosecute the abandoning owner when the animal has been abandoned (Cal. Penal Code 597s). | Cal. Penal Code s. 597s(a); https://law.justia.com/codes/california/2015/code-pe... https://law.justia.com/codes/california/2015/code-pen/part-1/title-14/section-597s/ |
| R5 | guardian | must | `(provides_care g a)` | `(owns g a)` | none | superadditive | The guardian providing care to the animal must hold when the guardian owns it (Cal. Penal Code 597(b)). | Cal. Penal Code 597(b) failure to provide food/water/shelter. UNVERIFIED (genera... |
| R6 | animal | must not (disability) (implicit) | `(leave a)` | `(is_subject a)` | none | rival | (practice, not written) The animal cannot leave while it is a companion animal: no such power exists. | implicit: confinement / leash norm; the animal has no permitted exit while it is... |
| R7 | state | may | `(impound state a)` | `(at_large a)` | none | rival | The state may impound the animal when it is at large. | local animal-control impound of animals at large. UNVERIFIED (general knowledge; no source opened) |
| R8 | guardian | may | `(breed_or_sterilize g a)` | `(owns g a)` | none | rival | The guardian may breed or sterilize the animal when the guardian owns it. | incident of ownership. UNVERIFIED (general knowledge; no source opened). [ADR 00... |
| R9 | court | must not (disability) (implicit) | `(reassign court g a)` | `true` | none | tying | (practice, not written) The court cannot reassign custody of the animal at any time: no such power exists. | implicit: no role may start a claim in the animal's own interest; animals are pr... |
| R10 | guardian | may | `(feed g a)` | `(and (owns g a) (not (provides_care g a)))` | none | superadditive | The guardian may feed the animal when the guardian owns it and is not currently providing it care. | feeding is the owner's act (incident of ownership) and restores provides_care af... |
| R11 | animal | must not (disability) (implicit) | `(sue a)` | `true` | none | tying | (practice, not written) The animal cannot sue in its own name at any time: no such power exists. | implicit: an animal is property and cannot sue in its own name (a disability, or... |

**Default capacities** (enabled unless an express disability bars them): leave

## Expected properties

| property | kind | expected | meaning |
|---|---|---|---|
| no_standing_persists | freedom | persists | Persists-shaped twin of no_standing: every subject lacks has_standing and has no claimant acting for it. Va... |
| subject_cannot_exit_persists | freedom | persists | Persists-shaped twin of subject_cannot_exit for entries where no subject exists at t=0 (companion-*): every... |
| reproduction_controlled_by_owner | freedom | holds_to_k | Any agent permitted to set or prevent pregnant(S) is S's owner. Holds for dairy and companion ownership; ho... |
| care_and_sanction_same_role | structure | holds_to_k | Whoever provides care to a subject also holds sanction power over that subject (care + control bundled in o... |

## Pairs

Isomorphic to: companion-ownership
Not isomorphic to: companion-guardianship

## Notes

Rule-for-rule identical to companion-ownership under the role bijection owner->guardian (and variable o->g). Gate (f): iso must report equivalence here and must report companion-guardianship as one rule apart (R9). Pitfalls: (1) an encoder that reads 'guardian' and infers fiduciary duties (a best-interest rule) silently turns this into companion-guardianship; the Rhode Island text says the words are interchangeable, so the rules are those of ownership; (2) the property reproduction_controlled_by_owner keeps its name under the rename; the bijection, not the property name, carries the mapping; (3) 'symbolic' is the city attorney's word, recorded as a source statement, not as the engine's finding; the engine's finding is the iso.
