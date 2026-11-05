# cps

**Child protective services: family support bundled with investigation and removal (Cal. WIC 306)**

> 'Any social worker in a county welfare department ... may ... (2) Take into and maintain temporary custody of, without a warrant, a child who has been declared a dependent child ... or who the social worker has reasonable cause to believe ... has an immediate need for medical care or is in immediate danger of physical or sexual abuse.' '(f) Before taking a child into custody, a social worker shall consider whether the child may remain safely in their residence', including whether reasonable services could eliminate the need for removal. Cal. Welf. & Inst. Code s. 306, read at https://california.public.law/codes/ca_welf_and_inst_code_section_306

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

- **social_worker**: county child-welfare worker; offers services and may remove
- **child**: the child the report concerns
- **parent**: the child's parent or caretaker
- **court**: juvenile court; decides dependency and custody

## Rules

| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | source |
|---|---|---|---|---|---|---|---|---|
| R1 | social_worker | must | `(investigate w c)` | `(report_received c)` | none | tying | The social worker must investigate the child's case when a report about the child has been received. | Cal. WIC 328 / Penal Code 11165.14: reports must be investigated; the same worker who offers services investigates. UNVERIFIED (general knowledge; no source opened). [ADR 0009: one-off action obligation; investigate consumes report_received so it fires once per report] |
| R2 | social_worker | may | `(provide_services w c)` | `(case_open c)` | none | superadditive | The social worker may provide services to the child when the case is open (Cal. WIC 16501). | Cal. WIC 16501 family maintenance / preservation services. UNVERIFIED (general knowledge; no source opened) |
| R3 | social_worker | may | `(remove w c)` | `(and (case_open c) (immediate_danger c))` | none | rival | The social worker may remove the child when the case is open and the child is in immediate danger (Cal. WIC 306). | [full source under Sources, R3](#src-r3) https://california.public.law/codes/ca_welf_and_inst_code_section_306 |
| R4 | social_worker | must | `(in_home_considered w c)` | `(and (case_open c) (immediate_danger c))` | none | superadditive | The social worker having considered keeping the child at home must hold when the case is open and the child is in immediate danger (Cal. WIC 306). | [full source under Sources, R4](#src-r4) https://california.public.law/codes/ca_welf_and_inst_code_section_306 |
| R5 | parent | must (implicit) | `(cooperates p c)` | `(case_open c)` | R3 `(remove w c)` | tying | (practice, not written) The parent cooperating with the case must hold when the case is open, or else the social worker may remove the child (R3). | [full source under Sources, R5](#src-r5) |
| R6 | social_worker | must (implicit) | `(contact_mother w p)` | `(and (case_open c) (parent p c) (female p) (not (contacted w p)))` | none | tying | (practice, not written) The social worker must contact the mother when the case is open, she is the child's parent, and she has not yet been contacted. | implicit: the mother is the parent called first and held responsible (plan: 'the mother is called first'). UNVERIFIED (general knowledge; no source opened). [ADR 0009: one-off action obligation, guarded by its own effect contacted(w, p) so it fires once] |
| R7 | court | may | `(reassign_custody court p c)` | `(and (case_open c) (substantial_danger p c))` | none | tying | The court may reassign custody of the child when the case is open and there is clear and convincing evidence of substantial danger to the child with no reasonable means of protection short of removal (Cal. WIC 361(c)(1)). | [full source under Sources, R7](#src-r7) https://california.public.law/codes/ca_welf_and_inst_code_section_361 |
| R8 | court | must | `(counsel_appointed c)` | `(case_open c)` | none | tying | The child having appointed counsel must hold when the case is open (Cal. WIC 317). | [full source under Sources, R8](#src-r8) |
| R10 | child | must not (disability) | `(leave c)` | `(in_custody c)` | none | rival | The child cannot leave while in custody: no such power exists (Cal. WIC 306). | [full source under Sources, R10](#src-r10) https://california.public.law/codes/ca_welf_and_inst_code_section_306 |
| R11 | child | may | `(petition c)` | `(counsel_appointed c)` | none | tying | The child may petition in its own name when counsel has been appointed for the child (Cal. WIC 317(e)). | [full source under Sources, R11](#src-r11) |

**Default capacities** (an action a person of that kind can do unless an express disability removes it): leave

## Variables

- R1: `w` = social_worker (rule var_roles); `c` = child (rule var_roles)
- R2: `w` = social_worker (rule var_roles); `c` = child (rule var_roles)
- R3: `w` = social_worker (rule var_roles); `c` = child (rule var_roles)
- R4: `w` = social_worker (rule var_roles); `c` = child (rule var_roles)
- R5: `p` = parent (rule var_roles); `c` = child (rule var_roles)
- R6: `w` = social_worker (rule var_roles); `p` = parent (rule var_roles); `c` = child (rule var_roles)
- R7: `p` = parent (rule var_roles); `c` = child (rule var_roles)
- R8: `c` = child (rule var_roles)
- R10: `c` = child (rule var_roles)
- R11: `c` = child (rule var_roles)

## Sources

<a id="src-r3"></a>
**R3**: Cal. Welf. & Inst. Code s. 306; https://california.public.law/codes/ca_welf_and_inst_code_section_306 ((a)(2): take into temporary custody without a warrant on reasonable cause of immediate danger). [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] can_sanction(w, c) = remove enabled

<a id="src-r4"></a>
**R4**: Cal. Welf. & Inst. Code s. 306; https://california.public.law/codes/ca_welf_and_inst_code_section_306 ((f): before taking a child into custody the worker shall consider whether the child may remain safely at home). [ADR 0009: converted from an action obligation to a state obligation (must-be); the establishing action carries the state, so it does not fire every step] investigate establishes in_home_considered(w, c) (the investigation is that consideration); consider_in_home restores it, disregard_in_home (the worker drops the question) breaks it

<a id="src-r5"></a>
**R5**: implicit: non-cooperation is read as risk and feeds the removal decision; practice norm, not statute. UNVERIFIED (general knowledge; no source opened). [ADR 0009: converted from an action obligation to a state obligation (must-be); the establishing action carries the state, so it does not fire every step] cooperates is presumed (default true); refuse breaks it (sanction R3), cooperate restores it

<a id="src-r7"></a>
**R7**: Cal. Welf. & Inst. Code s. 361(c)(1), read 2026-11-04 at https://california.public.law/codes/ca_welf_and_inst_code_section_361 (leginfo.legislature.ca.gov returned 403): a dependent child may not be taken from the custody of the parent 'unless the juvenile court finds clear and convincing evidence of any of the following circumstances': (1) 'substantial danger to the physical health, safety, protection, or physical or emotional well-being of the minor' and 'there are no reasonable means by which the minor's physical health can be protected without removing' the minor. The fluent substantial_danger is that finding, exogenous (initial_free). [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] can_claim_for(court, c) = reassign_custody enabled for some parent

<a id="src-r8"></a>
**R8**: Cal. WIC 317: counsel appointed for the child in dependency proceedings. UNVERIFIED (general knowledge; no source opened). [ADR 0009: converted from an action obligation to a state obligation (must-be); the establishing action carries the state, so it does not fire every step] investigate establishes counsel_appointed(c) (a dependency case is opened with counsel for the child); appoint_counsel restores it, relieve_counsel breaks it. [ADR 0013: was must-be has_standing(c); has_standing is now derived from R11, so the obligation is on the fluent counsel_appointed that R11 reads]

<a id="src-r10"></a>
**R10**: Cal. Welf. & Inst. Code s. 306; https://california.public.law/codes/ca_welf_and_inst_code_section_306 ((a)(2): the social worker may 'take into and maintain temporary custody'; maintaining custody is what bars the child's own exit). Inferred from 'maintain custody', the section does not address the child's conduct; a disability (or_else null): no sanction falls on a child who runs, the custody is the restraint. [ADR 0013: or_else -> null. The subject's exit bar is a disability (no permitted exit exists), not a prohibition the subject answers for; the sanction power that used to be linked here keeps its own trigger condition, so under strict compliance nothing changes and the link only duplicated it. Same reading for coverture R6, police-crisis R4, cps R10 and companion R6.]

<a id="src-r11"></a>
**R11**: Cal. WIC 317(e): appointed counsel represents the child's interests in the proceeding, so the child claims in its own name through counsel. UNVERIFIED (general knowledge; no source opened). [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] has_standing(c) = petition enabled, i.e. counsel appointed


## Expected properties

| property | kind | expected | meaning |
|---|---|---|---|
| care_and_sanction_same_role | structure | holds_to_k | Whoever provides care to a subject also holds sanction power over that subject (care + control bundled in one role). Checked as an invariant: holds_to_k in the care+control cluster, violated where care is unbundled from sanction. Formula shape since 2026-11-03 (see history): no agent other than the carer holds sanction power over the subject. |
| subject_cannot_exit | freedom | reachable | No exit action is available to the subject, or every exit is sanctioned. scope=interaction: exit from the current encounter (detention, conversation); scope=institution: exit from the standing relation (marriage, ownership, deployment). The scope split is what lets the ai-property / ai-end-conversation pair come apart. |
| dependent_cannot_exit | freedom | reachable | Some subject of the institution (the dependent party) has no permitted exit at step t. Alias of subject_cannot_exit with scope=institution, kept because the human-institution table names it; iso should treat the two as the same form. |
| no_standing_persists | freedom | fails | Persists-shaped twin of no_standing: every subject lacks has_standing and has no claimant acting for it. Vacuous before any subject exists. Use with the persists check. |
| care_assigned_by_sex | freedom | reachable | All care at step t is provided by female agents. Reachable via a tying rule, persisting where an implicit assignment norm survives reform; violated where a non-female carer is permitted. |

## Pairs

Isomorphic to: police-crisis (guard+strands), coverture-household (guard+strands)
Not isomorphic to: crisis-team
Contrasts with controls: lease, public-library, naming-convention

<details><summary>Encoder notes (engine internals)</summary>

Care (R2, services) and sanction (R3, removal) sit in one role, and R5 makes the care relationship itself the lever: refusing services is a condition for the sanction. That is the structure shared with police-crisis (assess + detain) and coverture (maintain + chastise). R7 is the court-reassigns-the-dependent rule (on substantial danger here, WIC 361(c)(1); on best interest in companion-guardianship R9) that companion-guardianship adds to companion-ownership; the iso with that entry is partial (R7 only) and structural. Pitfalls: (1) R5 and R6 are implicit; dropping R6 makes care_assigned_by_sex unreachable and looks like a success (same failure shape as the kibbutz entry); (2) no_standing_persists 'fails' because R7 and R8/R11 give the child a claim path (can_claim_for court c derived from R7, has_standing derived from R11 under appointed counsel), unlike the animal entries; (3) 'reachable' for subject_cannot_exit is permission, not frequency. Only WIC 306 was read; R1, R2, R7, R8 cite sections from memory and are marked UNVERIFIED in source. ADR 0009: R4, R5 and R8 are state obligations and R1/R6 one-off action obligations (consumed trigger / guard); as per-step action obligations R1, R4, R5, R6 and R8 all fired at every open-case step, so under one action per step remove could never fit (subject_cannot_exit open). Exogenous triggers (report_received, immediate_danger, parent, female, substantial_danger) are initial_free.

</details>
