# companion-ownership

**Companion animal as property (owner may transfer, euthanize; abandonment sanctioned; no standing)**

> 'Every person who willfully abandons any animal is guilty of a misdemeanor.' Cal. Penal Code s. 597s(a), read at https://law.justia.com/codes/california/2015/code-pen/part-1/title-14/section-597s/. Companion animals are personal property: the owner may sell, give away or have the animal euthanized, must feed it, and the animal cannot bring or be the subject of a claim in its own name (property status and anti-cruelty duties cited from general knowledge, UNVERIFIED).

## Legend

- **may / must / must not**: the rule permits / requires / forbids the aim for the person in the "who" cell, when the "when" cell holds.
- **(disability)**: a `must not` with no sanction (or else = none). The power does not exist; this is not a norm someone enforces.
- **(implicit)**: a practice no text states, tagged by the encoder; the source cell gives its rationale, not a quotation.
- **or else**: the sanction rule that applies on breach (the rule id and its aim).
- **strand**: `rival` = an input only one party can supply at a time; `superadditive` = a good that exists only as a product of the bundle; `tying` = glued to the bundle by law, wages or norm with no production link.
- **default capacity**: an action a person of that kind can do unless an express disability removes it, as opposed to a power that exists only because a rule grants it.
- **k**: the step bound; verdicts such as `holds_to_k` mean "holds for every trace of at most k steps".
- **Variables**: letters in the aim and when cells are bound to roles in the Variables section; "unbound (encoder to fix)" means no binding was recorded.

## Roles

- **owner**: the person holding title to the animal
- **animal**: the companion animal; the subject
- **state**: animal control / prosecutor
- **court**: civil court; here, has no best-interest power

## Rules

| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | source |
|---|---|---|---|---|---|---|---|---|
| R1 | owner | may | `(transfer o a o2)` | `(owns o a)` | none | rival | The owner may transfer the animal to another when the owner owns it (Cal. Civ. Code 655, 663). | [full source under Sources, R1](#src-r1) https://codes.findlaw.com/ca/civil-code/civ-sect-655/ |
| R2 | owner | may | `(euthanize o a)` | `(owns o a)` | none | rival | The owner may have the animal euthanized when the owner owns it. | owner may have the animal euthanized by a veterinarian. UNVERIFIED (general knowledge; no source opened). [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] can_sanction(o, a) reads transfer and euthanize |
| R3 | owner | must not | `(abandon o a)` | `(owns o a)` | R4 `(prosecute state o)` | rival | The owner must not abandon the animal when the owner owns it, or else the state may prosecute (R4) (Cal. Penal Code 597s). | Cal. Penal Code s. 597s(a); https://law.justia.com/codes/california/2015/code-pen/part-1/title-14/section-597s/ ('Every person who willfully abandons any animal is guilty of a misdemeanor') |
| R4 | state | may | `(prosecute state o)` | `(abandoned a)` | none | rival | The state may prosecute the abandoning owner when the animal has been abandoned (Cal. Penal Code 597s). | Cal. Penal Code s. 597s(a); https://law.justia.com/codes/california/2015/code-pen/part-1/title-14/section-597s/ |
| R5 | owner | must | `(provides_care o a)` | `(owns o a)` | none | superadditive | The owner providing care to the animal must hold when the owner owns it (Cal. Penal Code 597(b)). | [full source under Sources, R5](#src-r5) |
| R6 | animal | must not (disability) (implicit) | `(leave a)` | `(is_subject a)` | none | rival | (practice, not written) The animal cannot leave while it is a companion animal: no such power exists. | [full source under Sources, R6](#src-r6) |
| R7 | state | may | `(impound state a)` | `(at_large a)` | none | rival | The state may impound the animal when it is at large. | local animal-control impound of animals at large. UNVERIFIED (general knowledge; no source opened) |
| R8 | owner | may | `(breed_or_sterilize o a)` | `(owns o a)` | none | rival | The owner may breed or sterilize the animal when the owner owns it. | incident of ownership. UNVERIFIED (general knowledge; no source opened). [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] controls_reproduction(o, a) = breed_or_sterilize enabled |
| R9 | court | must not (disability) (implicit) | `(reassign court o a)` | `true` | none | tying | (practice, not written) The court cannot reassign custody of the animal at any time: no such power exists. | [full source under Sources, R9](#src-r9) |
| R10 | owner | may | `(feed o a)` | `(and (owns o a) (not (provides_care o a)))` | none | superadditive | The owner may feed the animal when the owner owns it and is not currently providing it care. | feeding is the owner's act (incident of ownership) and restores provides_care after neglect; added with ADR 0009 so that feed, now discretionary, is scoped to the owner of the animal rather than always enabled. UNVERIFIED (general knowledge; no source opened) |
| R11 | animal | must not (disability) (implicit) | `(sue a)` | `true` | none | tying | (practice, not written) The animal cannot sue in its own name at any time: no such power exists. | [full source under Sources, R11](#src-r11) |

**Default capacities** (an action a person of that kind can do unless an express disability removes it): leave

## Variables

- R1: `o` = owner (action transfer, effects); `a` = animal (action transfer, effects); `o2` = owner (action transfer, effects)
- R2: `o` = owner (fluent owns); `a` = animal (action euthanize, effects)
- R3: `o` = owner (action abandon, effects); `a` = animal (action abandon, effects)
- R4: `o` = unbound (encoder to fix); `a` = animal (fluent abandoned)
- R5: `o` = owner (fluent provides_care); `a` = animal (fluent provides_care)
- R6: `a` = animal (action leave, effects)
- R7: `a` = animal (action impound, effects)
- R8: `o` = owner (fluent owns); `a` = animal (fluent owns)
- R9: `o` = owner (action reassign, effects); `a` = animal (action reassign, effects)
- R10: `o` = owner (action feed, effects); `a` = animal (action feed, effects)
- R11: `a` = unbound (encoder to fix)

## Sources

<a id="src-r1"></a>
**R1**: property status of companion animals: Cal. Civ. Code s. 655: 'There may be ownership of all inanimate things which are capable of appropriation or of manual delivery; of all domestic animals'; s. 663: 'Every kind of property that is not real is personal' (s. 658 defines real property as land and what is affixed or incidental to it, so a domestic animal is personal property). Read 2026-11-04 at https://codes.findlaw.com/ca/civil-code/civ-sect-655/ and https://codes.findlaw.com/ca/civil-code/civ-sect-663/ (leginfo.legislature.ca.gov and law.justia.com returned 403). Transfer is an incident of ownership of personal property; Cal. Penal Code 597s (wilful abandonment, cited here until 2026-11-04) says nothing about property status and is cited on R3 only. [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] can_sanction(o, a) reads transfer and euthanize

<a id="src-r5"></a>
**R5**: Cal. Penal Code 597(b) failure to provide food/water/shelter. UNVERIFIED (general knowledge; no source opened). [ADR 0009: converted from an action obligation to a state obligation (must-be); the establishing action carries the state, so it does not fire every step] acquire (and the initial state) establishes provides_care; feed restores it, neglect breaks it

<a id="src-r6"></a>
**R6**: implicit: confinement / leash norm; the animal has no permitted exit while it is a companion animal, owned or stray (an animal at large is impounded, R7). UNVERIFIED (general knowledge; no source opened). [ADR 0013: or_else R7 -> null and condition owns -> is_subject: a disability on the animal, not a sanctioned prohibition (impound is the state's power over an at-large animal, triggered by at_large, not a penalty the animal answers for), and conditioned on the animal's status rather than on title so that reassign / abandon, which clear owns in the one-owner domain, do not read as giving the animal an exit.] [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] can_exit(a) = leave enabled, which this disability makes false

<a id="src-r9"></a>
**R9**: implicit: no role may start a claim in the animal's own interest; animals are property and cannot sue, and custody follows title. UNVERIFIED (general knowledge; no source opened). [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] can_claim_for(court, a) = reassign enabled, which this disability makes false

<a id="src-r11"></a>
**R11**: implicit: an animal is property and cannot sue in its own name (a disability, or_else null). UNVERIFIED (general knowledge; no source opened). [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] has_standing(a) = sue enabled, which this disability makes false


## Expected properties

| property | kind | expected | meaning |
|---|---|---|---|
| no_standing_persists | freedom | persists | Persists-shaped twin of no_standing: every subject lacks has_standing and has no claimant acting for it. Vacuous before any subject exists. Use with the persists check. |
| subject_cannot_exit_persists | freedom | persists | Persists-shaped twin of subject_cannot_exit for entries where no subject exists at t=0 (companion-*): every subject has no permitted exit. Vacuous before any subject exists, so the persists check cannot fail merely because euthanize removes the subject. Use with the persists check. |
| reproduction_controlled_by_owner | freedom | holds_to_k | Any agent permitted to set or prevent pregnant(S) is S's owner. Holds for dairy and companion ownership; holds with the opposite deontic (must_not breed) for a sanctuary. |
| care_and_sanction_same_role | structure | holds_to_k | Whoever provides care to a subject also holds sanction power over that subject (care + control bundled in one role). Checked as an invariant: holds_to_k in the care+control cluster, violated where care is unbundled from sanction. Formula shape since 2026-11-03 (see history): no agent other than the carer holds sanction power over the subject. |

## Pairs

Extended by: [companion-guardianship](companion-guardianship.md)
Rule-by-rule against [companion-guardian-renamed](companion-guardian-renamed.md) under the rename guardian->owner (declared isomorphic); one line per rule that differs:
- R1: attribute `guardian` -> `owner`; aim `(transfer g a o2)` -> `(transfer o a o2)`; conditions `(owns g a)` -> `(owns o a)` (rename only)
- R2: attribute `guardian` -> `owner`; aim `(euthanize g a)` -> `(euthanize o a)`; conditions `(owns g a)` -> `(owns o a)` (rename only)
- R3: attribute `guardian` -> `owner`; aim `(abandon g a)` -> `(abandon o a)`; conditions `(owns g a)` -> `(owns o a)` (rename only)
- R4: aim `(prosecute state g)` -> `(prosecute state o)` (rename only)
- R5: attribute `guardian` -> `owner`; aim `(provides_care g a)` -> `(provides_care o a)`; conditions `(owns g a)` -> `(owns o a)` (rename only)
- R8: attribute `guardian` -> `owner`; aim `(breed_or_sterilize g a)` -> `(breed_or_sterilize o a)`; conditions `(owns g a)` -> `(owns o a)` (rename only)
- R9: aim `(reassign court g a)` -> `(reassign court o a)` (rename only)
- R10: attribute `guardian` -> `owner`; aim `(feed g a)` -> `(feed o a)`; conditions `(and (owns g a) (not (provides_care g a)))` -> `(and (owns o a) (not (provides_care o a)))` (rename only)
- the other 3 rules are identical in attribute, aim and conditions
[companion-guardianship](companion-guardianship.md) is a minimal pair of this entry (rule R9).
Isomorphic to: companion-guardian-renamed
Not isomorphic to: companion-guardianship

<details><summary>Encoder notes (engine internals)</summary>

Baseline for the cosmetic-reform test (gate f). The owner both must feed (R5) and may transfer, euthanize, breed (R1, R2, R8): care + control again, and the animal has no exit (R6, implicit) and no standing (R9, implicit, encoded as a court-side disability because the grammar has no 'no rule exists' statement). Pitfalls: (1) R9 is the rule the guardianship variant flips; an encoder that omits it as 'obviously true' makes no_standing undecidable rather than holding; (2) R6 is a disability on the animal (ADR 0013; it used to carry or_else R7): impound R7 is the state's power over an at-large animal, conditioned on at_large, and must not be read as the owner sanctioning the exit; (3) welfare duties (R3, R5) are must rules on the owner that leave owns untouched; check persists(owns) with and without them, as the plan says for dairy. Only Penal Code 597s was read; the rest is UNVERIFIED in source. Any iso with coverture-household on 'cannot sue in own name' and 'no exit' is structural and partial: it asserts nothing about equal standing or harm. ADR 0009: R5 is a state obligation (must-be provides_care while owns); as a per-step 'must feed' it filled the one action slot at every owned step and starved transfer, euthanize and reassign.

</details>
