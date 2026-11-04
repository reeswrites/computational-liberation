# companion-ownership

**Companion animal as property (owner may transfer, euthanize; abandonment sanctioned; no standing)**

> 'Every person who willfully abandons any animal is guilty of a misdemeanor.' Cal. Penal Code s. 597s(a), read at https://law.justia.com/codes/california/2015/code-pen/part-1/title-14/section-597s/. Companion animals are personal property: the owner may sell, give away or have the animal euthanized, must feed it, and the animal cannot bring or be the subject of a claim in its own name (property...

## Roles

- **owner**: the person holding title to the animal
- **animal**: the companion animal; the subject
- **state**: animal control / prosecutor
- **court**: civil court; here, has no best-interest power

## Rules

| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | source |
|---|---|---|---|---|---|---|---|---|
| R1 | owner | may | `(transfer o a o2)` | `(owns o a)` | none | rival | The owner may transfer the animal to another when the owner owns it (Cal. Penal Code 597s). | property status of companion animals; Cal. Penal Code s. 597s(a); https://law.ju... https://law.justia.com/codes/california/2015/code-pen/part-1/title-14/section-597s/. |
| R2 | owner | may | `(euthanize o a)` | `(owns o a)` | none | rival | The owner may have the animal euthanized when the owner owns it. | owner may have the animal euthanized by a veterinarian. UNVERIFIED (general know... |
| R3 | owner | must not | `(abandon o a)` | `(owns o a)` | R4 `(prosecute state o)` | rival | The owner must not abandon the animal when the owner owns it, or else the state may prosecute (R4) (Cal. Penal Code 597s). | Cal. Penal Code s. 597s(a); https://law.justia.com/codes/california/2015/code-pe... https://law.justia.com/codes/california/2015/code-pen/part-1/title-14/section-597s/ |
| R4 | state | may | `(prosecute state o)` | `(abandoned a)` | none | rival | The state may prosecute the abandoning owner when the animal has been abandoned (Cal. Penal Code 597s). | Cal. Penal Code s. 597s(a); https://law.justia.com/codes/california/2015/code-pe... https://law.justia.com/codes/california/2015/code-pen/part-1/title-14/section-597s/ |
| R5 | owner | must | `(provides_care o a)` | `(owns o a)` | none | superadditive | The owner providing care to the animal must hold when the owner owns it (Cal. Penal Code 597(b)). | Cal. Penal Code 597(b) failure to provide food/water/shelter. UNVERIFIED (genera... |
| R6 | animal | must not (disability) (implicit) | `(leave a)` | `(is_subject a)` | none | rival | (practice, not written) The animal cannot leave while it is a companion animal: no such power exists. | implicit: confinement / leash norm; the animal has no permitted exit while it is... |
| R7 | state | may | `(impound state a)` | `(at_large a)` | none | rival | The state may impound the animal when it is at large. | local animal-control impound of animals at large. UNVERIFIED (general knowledge; no source opened) |
| R8 | owner | may | `(breed_or_sterilize o a)` | `(owns o a)` | none | rival | The owner may breed or sterilize the animal when the owner owns it. | incident of ownership. UNVERIFIED (general knowledge; no source opened). [ADR 00... |
| R9 | court | must not (disability) (implicit) | `(reassign court o a)` | `true` | none | tying | (practice, not written) The court cannot reassign custody of the animal at any time: no such power exists. | implicit: no role may start a claim in the animal's own interest; animals are pr... |
| R10 | owner | may | `(feed o a)` | `(and (owns o a) (not (provides_care o a)))` | none | superadditive | The owner may feed the animal when the owner owns it and is not currently providing it care. | feeding is the owner's act (incident of ownership) and restores provides_care af... |
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

Extended by: [companion-guardianship](companion-guardianship.md)
[companion-guardianship](companion-guardianship.md) is a minimal pair of this entry (rule R9).
Isomorphic to: companion-guardian-renamed
Not isomorphic to: companion-guardianship

## Notes

Baseline for the cosmetic-reform test (gate f). The owner both must feed (R5) and may transfer, euthanize, breed (R1, R2, R8): care + control again, and the animal has no exit (R6, implicit) and no standing (R9, implicit, encoded as a court-side disability because the grammar has no 'no rule exists' statement). Pitfalls: (1) R9 is the rule the guardianship variant flips; an encoder that omits it as 'obviously true' makes no_standing undecidable rather than holding; (2) R6 is a disability on the animal (ADR 0013; it used to carry or_else R7): impound R7 is the state's power over an at-large animal, conditioned on at_large, and must not be read as the owner sanctioning the exit; (3) welfare duties (R3, R5) are must rules on the owner that leave owns untouched; check persists(owns) with and without them, as the plan says for dairy. Only Penal Code 597s was read; the rest is UNVERIFIED in source. Any iso with coverture-household on 'cannot sue in own name' and 'no exit' is structural and partial: it asserts nothing about equal standing or harm. ADR 0009: R5 is a state obligation (must-be provides_care while owns); as a per-step 'must feed' it filled the one action slot at every owned step and starved transfer, euthanize and reassign.
