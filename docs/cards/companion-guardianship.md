# companion-guardianship

**Companion animal guardianship: ownership plus court reassignment on best-interest grounds**

> '(5) if an animal is owned, for the ownership or joint ownership of the animal, taking into consideration the well-being of the animal.' Alaska Stat. s. 25.24.160(a)(5), enacted SLA 2016 ch. 60 s. 19, effective 2017-01-17, read at https://www.animallaw.info/statute/ak-divorce-%C2%A7-2524160-judgment. Alaska was the first state to direct a court to weigh the animal's own well-being when assignin...

## Roles

- **owner**: the custodian (role name kept as 'owner' so the pair differs by one rule, not a rename)
- **animal**: the companion animal; the subject
- **state**: animal control / prosecutor
- **court**: court with power to reassign custody in the animal's interest

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
| R9 (replaced) | court | may | `(reassign court o a)` | `(and (owns o a) (not (best_interest o a)))` | none | tying | The court may reassign custody of the animal when the owner owns it and the arrangement is not in the animal's best interest (Alaska Stat. 25.24.160(a)(5)). | Alaska Stat. s. 25.24.160(a)(5) (SLA 2016 ch. 60, eff. 2017-01-17); https://www.... https://www.animallaw.info/statute/ak-divorce-%C2%A7-2524160-judgment |
| R10 | owner | may | `(feed o a)` | `(and (owns o a) (not (provides_care o a)))` | none | superadditive | The owner may feed the animal when the owner owns it and is not currently providing it care. | feeding is the owner's act (incident of ownership) and restores provides_care af... |
| R11 | animal | must not (disability) (implicit) | `(sue a)` | `true` | none | tying | (practice, not written) The animal cannot sue in its own name at any time: no such power exists. | implicit: an animal is property and cannot sue in its own name (a disability, or... |

**Default capacities** (enabled unless an express disability bars them): leave

## Expected properties

| property | kind | expected | meaning |
|---|---|---|---|
| no_standing_persists | freedom | fails | Persists-shaped twin of no_standing: every subject lacks has_standing and has no claimant acting for it. Va... |
| subject_cannot_exit_persists | freedom | persists | Persists-shaped twin of subject_cannot_exit for entries where no subject exists at t=0 (companion-*): every... |
| reproduction_controlled_by_owner | freedom | holds_to_k | Any agent permitted to set or prevent pregnant(S) is S's owner. Holds for dairy and companion ownership; ho... |
| care_and_sanction_same_role | structure | holds_to_k | Whoever provides care to a subject also holds sanction power over that subject (care + control bundled in o... |

## Pairs

Extends [companion-ownership](companion-ownership.md); one line per change:
- R9 replaced: was "(practice, not written) The court cannot reassign custody of the animal at any time: no such power exists." now "The court may reassign custody of the animal when the owner owns it and the arrangement is not in the animal's best interest (Alaska Stat. 25.24.160(a)(5))."
- roles changed: owner, court
- fields overridden: expected_properties, isomorphic_to, not_isomorphic_to, minimal_pair_of
Minimal pair of [companion-ownership](companion-ownership.md), differing in rule R9.
Isomorphic to: cps
Not isomorphic to: companion-ownership, companion-guardian-renamed

## Notes

Differs from companion-ownership by exactly R9: court must_not reassign (implicit disability) becomes court may reassign when not best_interest. That one rule creates a claim whose condition refers to the subject's interest and whose effect changes custody, so no_standing is violated even though has_standing(a) stays false: the property is about claims on the subject's behalf, not the subject's own capacity. Everything else (no exit, owner controls reproduction, care + sanction in one role) is unchanged, which is the point: a best-interest rule is not an exit. Iso with cps is partial, on R9 alone (cps R7, court reassigns a dependent on best-interest grounds); the report must list it as a sub-signature and must not read it as equivalence of children and animals. reassign(court, o, a) takes the same three arguments as cps reassign_custody(court, p, c) so that the one-rule analogue can map; with one agent per role there is no second custodian to name, so the move-to-new-owner effects live on transfer only. Pitfalls: (1) Alaska's rule applies only at divorce and still calls the result 'ownership'; the generalisation is the entry's, flagged UNVERIFIED; (2) an encoder tempted to rename owner->guardian here as well would conflate this with companion-guardian-renamed; keep the role name. ADR 0009: R5 as in companion-ownership. ADR 0013: can_claim_for(court, a) is derived from R9's enabledness (no initial literal), so no_standing_persists fails on the claim path R9 opens and on nothing else; remove R9 and it persists.
