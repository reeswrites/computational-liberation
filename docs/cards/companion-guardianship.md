# companion-guardianship

**Companion animal guardianship: ownership plus court reassignment on best-interest grounds**

> '(5) if an animal is owned, for the ownership or joint ownership of the animal, taking into consideration the well-being of the animal.' Alaska Stat. s. 25.24.160(a)(5), enacted SLA 2016 ch. 60 s. 19, effective 2017-01-17, read at https://www.animallaw.info/statute/ak-divorce-%C2%A7-2524160-judgment. Alaska was the first state to direct a court to weigh the animal's own well-being when assigning it; the entry generalises that one rule beyond divorce, which Alaska does not.

## Legend

- **may / must / must not**: the rule permits / requires / forbids the aim for the person in the "who" cell, when the "when" cell holds.
- **(disability)**: a `must not` with no sanction (or else = none). The power does not exist and nobody enforces anything, whether the disability is written law (`formal`) or custom that people, not a body, uphold (`norm`).
- **(implicit)**: a practice no text states, tagged by the encoder; the source cell gives its rationale, not a quotation.
- **or else**: the sanction rule that applies on breach (the rule id and its aim).
- **strand**: `rival` = an input only one party can supply at a time; `superadditive` = a good that exists only as a product of the bundle; `tying` = glued to the bundle by law, wages or norm with no production link.
- **default capacity**: an action a person of that kind can do unless an express disability removes it, as opposed to a power that exists only because a rule grants it.
- **k**: the step bound; verdicts such as `holds_to_k` mean "holds for every trace of at most k steps".
- **Variables**: letters in the aim and when cells are bound to roles in the Variables section; "unbound (encoder to fix)" means no binding was recorded.
- **kind**: what sort of rule it is. `formal` = written law or contract (the default, always shown so it can be questioned); `norm` = an unwritten practice that others enforce; `strategy` = a regularity nobody enforces. A `strategy` rule written as `must` is still read by the engine as a duty under strict compliance, though nobody enforces it.
- **sanctioner**: who enforces the or-else: `state`, `institution`, `peers`, `family`, `self`, or `none` (no or-else, so nobody).
- **sanctioner derived, unreviewed**: the rule's `sanctioner` was derived once by the 2026-11-07 migration from the or-else target's role and has not been hand-reviewed yet (plans/informal-rules.md D1).

## Roles

- **owner**: the custodian (role name kept as 'owner' so the pair differs by one rule, not a rename)
- **animal**: the companion animal; the subject
- **state**: animal control / prosecutor
- **court**: court with power to reassign custody in the animal's interest

## Rules

| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | level | source |
|---|---|---|---|---|---|---|---|---|---|
| R1 | owner | may [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(transfer o a o2)` | `(owns o a)` | none | rival | The owner may transfer the animal to another when the owner owns it (Cal. Civ. Code 655, 663). | recalled | [full source under Sources, R1](#src-r1) https://codes.findlaw.com/ca/civil-code/civ-sect-655/ |
| R2 | owner | may [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(euthanize o a)` | `(owns o a)` | none | rival | The owner may have the animal euthanized when the owner owns it. | unverified | owner may have the animal euthanized by a veterinarian. UNVERIFIED (general knowledge; no source opened). [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] can_sanction(o, a) reads transfer and euthanize |
| R3 | owner | must not [kind: formal; sanctioner: state] (sanctioner derived, unreviewed) | `(abandon o a)` | `(owns o a)` | R4 `(prosecute state o)` | rival | The owner must not abandon the animal when the owner owns it, or else the state may prosecute (R4) (Cal. Penal Code 597s). | opened | [full source under Sources, R3](#src-r3) https://law.justia.com/codes/california/2015/code-pen/part-1/title-14/section-597s/ |
| R4 | state | may [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(prosecute state o)` | `(abandoned a)` | none | rival | The state may prosecute the abandoning owner when the animal has been abandoned (Cal. Penal Code 597s). | opened | [full source under Sources, R4](#src-r4) https://law.justia.com/codes/california/2015/code-pen/part-1/title-14/section-597s/ |
| R5 | owner | must [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(provides_care o a)` | `(owns o a)` | none | superadditive | The owner providing care to the animal must hold when the owner owns it (Cal. Penal Code 597(b)). | unverified | [full source under Sources, R5](#src-r5) |
| R6 | animal | must not (disability) (implicit) [kind: norm; sanctioner: none] (sanctioner derived, unreviewed) | `(leave a)` | `(is_subject a)` | none | rival | (practice, not written; written law in substance, text not opened) The animal cannot leave while it is a companion animal: no such power exists. | unverified | [full source under Sources, R6](#src-r6) |
| R7 | state | may [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(impound state a)` | `(at_large a)` | none | rival | The state may impound the animal when it is at large. | unverified | local animal-control impound of animals at large. UNVERIFIED (general knowledge; no source opened) |
| R8 | owner | may [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(breed_or_sterilize o a)` | `(owns o a)` | none | rival | The owner may breed or sterilize the animal when the owner owns it. | unverified | incident of ownership. UNVERIFIED (general knowledge; no source opened). [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] controls_reproduction(o, a) = breed_or_sterilize enabled |
| R9 (replaced) | court | may [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(reassign court o a)` | `(and (owns o a) (not (best_interest o a)))` | none | tying | The court may reassign custody of the animal when the owner owns it and the arrangement is not in the animal's best interest (Alaska Stat. 25.24.160(a)(5)). | unverified | [full source under Sources, R9](#src-r9) https://www.animallaw.info/statute/ak-divorce-%C2%A7-2524160-judgment |
| R10 | owner | may [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(feed o a)` | `(and (owns o a) (not (provides_care o a)))` | none | superadditive | The owner may feed the animal when the owner owns it and is not currently providing it care. | unverified | feeding is the owner's act (incident of ownership) and restores provides_care after neglect; added with ADR 0009 so that feed, now discretionary, is scoped to the owner of the animal rather than always enabled. UNVERIFIED (general knowledge; no source opened) |
| R11 | animal | must not (disability) (implicit) [kind: norm; sanctioner: none] (sanctioner derived, unreviewed) | `(sue a)` | `true` | none | tying | (practice, not written; written law in substance, text not opened) The animal cannot sue in its own name at any time: no such power exists. | unverified | [full source under Sources, R11](#src-r11) |

**Default capacities** (an action a person of that kind can do unless an express disability removes it): leave

## Variables

- R1: `o` = owner (rule var_roles); `a` = animal (rule var_roles); `o2` = owner (action transfer, effects)
- R2: `o` = owner (rule var_roles); `a` = animal (rule var_roles)
- R3: `o` = owner (rule var_roles); `a` = animal (rule var_roles)
- R4: `o` = owner (rule var_roles); `a` = animal (rule var_roles)
- R5: `o` = owner (rule var_roles); `a` = animal (rule var_roles)
- R6: `a` = animal (rule var_roles)
- R7: `a` = animal (rule var_roles)
- R8: `o` = owner (rule var_roles); `a` = animal (rule var_roles)
- R9: `o` = owner (rule var_roles); `a` = animal (rule var_roles)
- R10: `o` = owner (rule var_roles); `a` = animal (rule var_roles)
- R11: `a` = animal (rule var_roles)

## Sources

Per rule: the full source where the table cell is cut, then each provenance item (bibliography id in `data/sources/`, pin, jurisdiction, effective date, verification level with access date, excerpt). The `level` column is the weakest item; levels: opened > snippet > recalled > unverified.

<a id="src-r1"></a>
**R1**: property status of companion animals: Cal. Civ. Code s. 655: 'There may be ownership of all inanimate things which are capable of appropriation or of manual delivery; of all domestic animals'; s. 663: 'Every kind of property that is not real is personal' (s. 658 defines real property as land and what is affixed or incidental to it, so a domestic animal is personal property). Read 2026-11-04 at https://codes.findlaw.com/ca/civil-code/civ-sect-655/ and https://codes.findlaw.com/ca/civil-code/civ-sect-663/ (leginfo.legislature.ca.gov and law.justia.com returned 403). Transfer is an incident of ownership of personal property; Cal. Penal Code 597s (wilful abandonment, cited here until 2026-11-04) says nothing about property status and is cited on R3 only. [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] can_sanction(o, a) reads transfer and euthanize

- `cal-civ-655` (s. 655; US-CA; date n/a): **opened** 2026-11-04: "There may be ownership of all inanimate things which are capable of appropriation or of manual delivery; of all domestic animals" <https://codes.findlaw.com/ca/civil-code/civ-sect-655/>
- `cal-civ-663` (s. 663; US-CA; date n/a): **opened** 2026-11-04: "Every kind of property that is not real is personal" <https://codes.findlaw.com/ca/civil-code/civ-sect-663/>
- `cal-civ-658` (s. 658; US-CA; date n/a): **recalled**

**R2**

- no work named: **unverified** (rationale: owner may have the animal euthanized by a veterinarian)

<a id="src-r3"></a>
**R3**: Cal. Penal Code s. 597s(a); https://law.justia.com/codes/california/2015/code-pen/part-1/title-14/section-597s/ ('Every person who willfully abandons any animal is guilty of a misdemeanor') Verification pass: read 2026-11-06 at https://california.public.law/codes/ca_penal_code_section_597s (text 'updated Jan. 1, 2000' per the page): (a) 'Every person who willfully abandons any animal is guilty of a misdemeanor.'

- `cal-pen-597s` (s. 597s(a); US-CA; date n/a): **opened** 2026-11-06: "Every person who willfully abandons any animal is guilty of a misdemeanor." <https://california.public.law/codes/ca_penal_code_section_597s>

<a id="src-r4"></a>
**R4**: Cal. Penal Code s. 597s(a); https://law.justia.com/codes/california/2015/code-pen/part-1/title-14/section-597s/ Verification pass: read 2026-11-06 at https://california.public.law/codes/ca_penal_code_section_597s (text 'updated Jan. 1, 2000' per the page): (a) 'Every person who willfully abandons any animal is guilty of a misdemeanor.'

- `cal-pen-597s` (s. 597s(a); US-CA; date n/a): **opened** 2026-11-06: "Every person who willfully abandons any animal is guilty of a misdemeanor." <https://california.public.law/codes/ca_penal_code_section_597s>

<a id="src-r5"></a>
**R5**: Cal. Penal Code 597(b) failure to provide food/water/shelter. UNVERIFIED (general knowledge; no source opened). [ADR 0009: converted from an action obligation to a state obligation (must-be); the establishing action carries the state, so it does not fire every step] acquire (and the initial state) establishes provides_care; feed restores it, neglect breaks it

- `cal-pen-597` (s. 597(b); US-CA; date n/a): **unverified**

<a id="src-r6"></a>
**R6**: implicit: confinement / leash norm; the animal has no permitted exit while it is a companion animal, owned or stray (an animal at large is impounded, R7). UNVERIFIED (general knowledge; no source opened). [ADR 0013: or_else R7 -> null and condition owns -> is_subject: a disability on the animal, not a sanctioned prohibition (impound is the state's power over an at-large animal, triggered by at_large, not a penalty the animal answers for), and conditioned on the animal's status rather than on title so that reassign / abandon, which clear owns in the one-owner domain, do not read as giving the animal an exit.] [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] can_exit(a) = leave enabled, which this disability makes false Kind held at norm 2026-11-08 (batch 3b, B1 ruling): written law in substance, text not opened; retag to formal when opened.

- no work named: **unverified** (rationale: implicit: confinement / leash norm; the animal has no permitted exit while it is a companion animal, owned or stray (an animal at large is impounded, R7))

**R7**

- no work named: **unverified** (rationale: local animal-control impound of animals at large)

**R8**

- no work named: **unverified** (rationale: incident of ownership)

<a id="src-r9"></a>
**R9**: Alaska Stat. s. 25.24.160(a)(5) (SLA 2016 ch. 60, eff. 2017-01-17); https://www.animallaw.info/statute/ak-divorce-%C2%A7-2524160-judgment (in a divorce the court decides ownership of an animal 'taking into consideration the well-being of the animal'); generalised here from the divorce context to any custody claim, which no US jurisdiction yet does. UNVERIFIED (general knowledge; no source opened). [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] can_claim_for(court, a) = reassign enabled: this rule, and nothing in the initial state, is what makes no_standing_persists fail Verification pass: read 2026-11-06 at https://www.animallaw.info/statute/ak-divorce-%C2%A7-2524160-judgment (the statute as reproduced there): '(5) if an animal is owned, for the ownership or joint ownership of the animal, taking into consideration the well-being of the animal.'

- `ak-stat-25-24-160` ((a)(5); US-AK; date 2017-01-17): **opened** 2026-11-06: "(5) if an animal is owned, for the ownership or joint ownership of the animal, taking into consideration the well-being of the animal." <https://www.animallaw.info/statute/ak-divorce-%C2%A7-2524160-judgment>
- no work named: **unverified** (the generalisation from divorce to any custody claim: no jurisdiction does this (the entry's construction))

**R10**

- no work named: **unverified** (rationale: feeding is the owner's act (incident of ownership) and restores provides_care after neglect; added with ADR 0009 so that feed, now discretionary, is scoped to the owner of the animal rather than always enabled)

<a id="src-r11"></a>
**R11**: implicit: an animal is property and cannot sue in its own name (a disability, or_else null). UNVERIFIED (general knowledge; no source opened). [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] has_standing(a) = sue enabled, which this disability makes false Kind held at norm 2026-11-08 (batch 3b, B1 ruling): written law in substance, text not opened; retag to formal when opened.

- no work named: **unverified** (rationale: implicit: an animal is property and cannot sue in its own name (a disability, or_else null))


## Expected properties

| property | kind | expected | meaning |
|---|---|---|---|
| no_standing_persists | freedom | fails | Persists-shaped twin of no_standing: every subject lacks has_standing and has no claimant acting for it. Vacuous before any subject exists. Use with the persists check. |
| subject_cannot_exit_persists | freedom | persists | Persists-shaped twin of subject_cannot_exit for entries where no subject exists at t=0 (companion-*): every subject has no permitted exit. Vacuous before any subject exists, so the persists check cannot fail merely because euthanize removes the subject. Use with the persists check. |
| reproduction_controlled_by_owner | freedom | holds_to_k | Any agent permitted to set or prevent pregnant(S) is S's owner. Holds for dairy and companion ownership; holds with the opposite deontic (must_not breed) for a sanctuary. |
| care_and_sanction_same_role | structure | holds_to_k | Whoever provides care to a subject also holds sanction power over that subject (care + control bundled in one role). Checked as an invariant: holds_to_k in cps and coverture; violated in police-crisis read to WIC 5150, where a second role (the officer) holds concurrent control (L1 landing 2026-11-06), violated where care is unbundled from sanction. Formula shape since 2026-11-03 (see history): no agent other than the carer holds sanction power over the subject. |

## Pairs

Extends [companion-ownership](companion-ownership.md); one line per change:
- R9 replaced: was "(practice, not written; written law in substance, text not opened) The court cannot reassign custody of the animal at any time: no such power exists." now "The court may reassign custody of the animal when the owner owns it and the arrangement is not in the animal's best interest (Alaska Stat. 25.24.160(a)(5))."
- changes role owner: gloss becomes the custodian (role name kept as 'owner' so the pair differs by one rule, not a rename)
- changes role court: gloss becomes court with power to reassign custody in the animal's interest
- overrides expected_properties
- overrides minimal_pair_of
- overrides notes
Minimal pair of [companion-ownership](companion-ownership.md), differing in rule R9.
Isomorphic to: cps
Not isomorphic to: companion-ownership, companion-guardian-renamed

<details><summary>Encoder notes (engine internals)</summary>

Differs from companion-ownership by exactly R9: court must_not reassign (implicit disability) becomes court may reassign when not best_interest. That one rule creates a claim whose condition refers to the subject's interest and whose effect changes custody, so no_standing is violated even though has_standing(a) stays false: the property is about claims on the subject's behalf, not the subject's own capacity. Everything else (no exit, owner controls reproduction, care + sanction in one role) is unchanged, which is the point: a best-interest rule is not an exit. Iso with cps is partial, on R9 alone (cps R7, court reassigns a dependent on best-interest grounds); the report must list it as a sub-signature and must not read it as equivalence of children and animals. reassign(court, o, a) takes the same three arguments as cps reassign_custody(court, p, c) so that the one-rule analogue can map; with one agent per role there is no second custodian to name, so the move-to-new-owner effects live on transfer only. Pitfalls: (1) Alaska's rule applies only at divorce and still calls the result 'ownership'; the generalisation is the entry's, flagged UNVERIFIED; (2) an encoder tempted to rename owner->guardian here as well would conflate this with companion-guardian-renamed; keep the role name. ADR 0009: R5 as in companion-ownership. ADR 0013: can_claim_for(court, a) is derived from R9's enabledness (no initial literal), so no_standing_persists fails on the claim path R9 opens and on nothing else; remove R9 and it persists.

</details>
