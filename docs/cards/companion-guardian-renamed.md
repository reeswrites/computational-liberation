# companion-guardian-renamed

**Companion ownership with 'owner' renamed 'guardian' (municipal and state guardian wording ordinances)**

> 'Wherever the word "owner" shall appear in this chapter it shall also mean and may be interchanged with the word "guardian"', R.I. Gen. Laws s. 4-13-41 (P.L. 2001 ch. 72 s. 3), read at https://webserver.rilegislature.gov/Statutes/TITLE4/4-13/4-13-41.htm. Boulder, Colorado made the same owner->guardian wording change in its animal ordinances in July 2000; the assistant city attorney who rewrote the passages said 'I've always viewed [the wording change] as symbolic' (Westword, read at https://www.westword.com/?p=40702255; the ordinance text itself was not opened).

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

- **guardian**: the person holding title to the animal; the ordinance calls them guardian
- **animal**: the companion animal; the subject
- **state**: animal control / prosecutor
- **court**: civil court; here, has no best-interest power

## Rules

| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | source |
|---|---|---|---|---|---|---|---|---|
| R1 | guardian | may | `(transfer g a o2)` | `(owns g a)` | none | rival | The guardian may transfer the animal to another when the guardian owns it (R.I. Gen. Laws 4-13-41). | [full source under Sources, R1](#src-r1) https://webserver.rilegislature.gov/Statutes/TITLE4/4-13/4-13-41.htm. |
| R2 | guardian | may | `(euthanize g a)` | `(owns g a)` | none | rival | The guardian may have the animal euthanized when the guardian owns it. | owner may have the animal euthanized by a veterinarian. UNVERIFIED (general knowledge; no source opened). [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] can_sanction(o, a) reads transfer and euthanize |
| R3 | guardian | must not | `(abandon g a)` | `(owns g a)` | R4 `(prosecute state g)` | rival | The guardian must not abandon the animal when the guardian owns it, or else the state may prosecute (R4) (Cal. Penal Code 597s). | Cal. Penal Code s. 597s(a); https://law.justia.com/codes/california/2015/code-pen/part-1/title-14/section-597s/ ('Every person who willfully abandons any animal is guilty of a misdemeanor') |
| R4 | state | may | `(prosecute state g)` | `(abandoned a)` | none | rival | The state may prosecute the abandoning owner when the animal has been abandoned (Cal. Penal Code 597s). | Cal. Penal Code s. 597s(a); https://law.justia.com/codes/california/2015/code-pen/part-1/title-14/section-597s/ |
| R5 | guardian | must | `(provides_care g a)` | `(owns g a)` | none | superadditive | The guardian providing care to the animal must hold when the guardian owns it (Cal. Penal Code 597(b)). | [full source under Sources, R5](#src-r5) |
| R6 | animal | must not (disability) (implicit) | `(leave a)` | `(is_subject a)` | none | rival | (practice, not written) The animal cannot leave while it is a companion animal: no such power exists. | [full source under Sources, R6](#src-r6) |
| R7 | state | may | `(impound state a)` | `(at_large a)` | none | rival | The state may impound the animal when it is at large. | local animal-control impound of animals at large. UNVERIFIED (general knowledge; no source opened) |
| R8 | guardian | may | `(breed_or_sterilize g a)` | `(owns g a)` | none | rival | The guardian may breed or sterilize the animal when the guardian owns it. | incident of ownership. UNVERIFIED (general knowledge; no source opened). [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] controls_reproduction(o, a) = breed_or_sterilize enabled |
| R9 | court | must not (disability) (implicit) | `(reassign court g a)` | `true` | none | tying | (practice, not written) The court cannot reassign custody of the animal at any time: no such power exists. | [full source under Sources, R9](#src-r9) |
| R10 | guardian | may | `(feed g a)` | `(and (owns g a) (not (provides_care g a)))` | none | superadditive | The guardian may feed the animal when the guardian owns it and is not currently providing it care. | feeding is the owner's act (incident of ownership) and restores provides_care after neglect; added with ADR 0009 so that feed, now discretionary, is scoped to the owner of the animal rather than always enabled. UNVERIFIED (general knowledge; no source opened) |
| R11 | animal | must not (disability) (implicit) | `(sue a)` | `true` | none | tying | (practice, not written) The animal cannot sue in its own name at any time: no such power exists. | [full source under Sources, R11](#src-r11) |

**Default capacities** (an action a person of that kind can do unless an express disability removes it): leave

## Variables

- R1: `g` = guardian (action transfer, effects); `a` = animal (action transfer, effects); `o2` = guardian (action transfer, effects)
- R2: `g` = guardian (fluent owns); `a` = animal (action euthanize, effects)
- R3: `g` = guardian (action abandon, effects); `a` = animal (action abandon, effects)
- R4: `g` = unbound (encoder to fix); `a` = animal (fluent abandoned)
- R5: `g` = guardian (fluent provides_care); `a` = animal (fluent provides_care)
- R6: `a` = animal (action leave, effects)
- R7: `a` = animal (action impound, effects)
- R8: `g` = guardian (fluent owns); `a` = animal (fluent owns)
- R9: `g` = guardian (action reassign, effects); `a` = animal (action reassign, effects)
- R10: `g` = guardian (action feed, effects); `a` = animal (action feed, effects)
- R11: `a` = unbound (encoder to fix)

## Sources

<a id="src-r1"></a>
**R1**: property status of companion animals; R.I. Gen. Laws s. 4-13-41 (P.L. 2001 ch. 72); https://webserver.rilegislature.gov/Statutes/TITLE4/4-13/4-13-41.htm. [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] can_sanction(o, a) reads transfer and euthanize

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

Rule-by-rule against [companion-ownership](companion-ownership.md) under the rename owner->guardian (declared isomorphic); one line per rule that differs:
- R1: attribute `owner` -> `guardian`; aim `(transfer o a o2)` -> `(transfer g a o2)`; conditions `(owns o a)` -> `(owns g a)` (rename only)
- R2: attribute `owner` -> `guardian`; aim `(euthanize o a)` -> `(euthanize g a)`; conditions `(owns o a)` -> `(owns g a)` (rename only)
- R3: attribute `owner` -> `guardian`; aim `(abandon o a)` -> `(abandon g a)`; conditions `(owns o a)` -> `(owns g a)` (rename only)
- R4: aim `(prosecute state o)` -> `(prosecute state g)` (rename only)
- R5: attribute `owner` -> `guardian`; aim `(provides_care o a)` -> `(provides_care g a)`; conditions `(owns o a)` -> `(owns g a)` (rename only)
- R8: attribute `owner` -> `guardian`; aim `(breed_or_sterilize o a)` -> `(breed_or_sterilize g a)`; conditions `(owns o a)` -> `(owns g a)` (rename only)
- R9: aim `(reassign court o a)` -> `(reassign court g a)` (rename only)
- R10: attribute `owner` -> `guardian`; aim `(feed o a)` -> `(feed g a)`; conditions `(and (owns o a) (not (provides_care o a)))` -> `(and (owns g a) (not (provides_care g a)))` (rename only)
- the other 3 rules are identical in attribute, aim and conditions
Isomorphic to: companion-ownership
Not isomorphic to: companion-guardianship

<details><summary>Encoder notes (engine internals)</summary>

Rule-for-rule identical to companion-ownership under the role bijection owner->guardian (and variable o->g). Gate (f): iso must report equivalence here and must report companion-guardianship as one rule apart (R9). Pitfalls: (1) an encoder that reads 'guardian' and infers fiduciary duties (a best-interest rule) silently turns this into companion-guardianship; the Rhode Island text says the words are interchangeable, so the rules are those of ownership; (2) the property reproduction_controlled_by_owner keeps its name under the rename; the bijection, not the property name, carries the mapping; (3) 'symbolic' is the city attorney's word, recorded as a source statement, not as the engine's finding; the engine's finding is the iso.

</details>
