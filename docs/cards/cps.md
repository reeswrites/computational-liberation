# cps

**Child protective services: family support bundled with investigation and removal (Cal. WIC 306)**

> 'Any social worker in a county welfare department ... may ... (2) Take into and maintain temporary custody of, without a warrant, a child who has been declared a dependent child ... or who the social worker has reasonable cause to believe ... has an immediate need for medical care or is in immediate danger of physical or sexual abuse.' '(f) Before taking a child into custody, a social worker shall consider whether the child may remain safely in their residence', including whether reasonable services could eliminate the need for removal. Cal. Welf. & Inst. Code s. 306, read at https://california.public.law/codes/ca_welf_and_inst_code_section_306

## Legend

- **may / must / must not**: the rule permits / requires / forbids the aim for the person in the "who" cell, when the "when" cell holds.
- **(disability)**: a `must not` with no sanction (or else = none). The power does not exist and nobody enforces anything, whether the disability is written law (`formal`) or custom that people, not a body, uphold (`norm`).
- **(implicit)**: not written as a rule in the cited source; reconstructed from it or from practice. The source cell gives the rationale, not a quotation.
- **or else**: the sanction rule that applies on breach (the rule id and its aim).
- **strand**: `rival` = an input only one party can supply at a time; `superadditive` = a good that exists only as a product of the bundle; `tying` = glued to the bundle by law, wages or norm with no production link.
- **default capacity**: an action a person of that kind can do unless an express disability removes it, as opposed to a power that exists only because a rule grants it. The "Default capacities" list under the table names the bearer role for each.
- **free fluent**: an input the model varies, not set by any rule; a when cell that names one waits on a fact the world supplies (a report arrives, it is visiting time), not on something a role does. Listed with its gloss under "Free fluents" below the table.
- **(replaced) / (added)** after a row id: this entry `extends` another, and the row replaces the base entry's row of that id, or adds one; the base card holds the original wording.
- **linked to no rule**: a sanction-shaped rule (such as `may reprimand`) that no row's or else points at; it fires on no breach and is kept for the record only.
- **k**: the step bound; verdicts such as `holds_to_k` mean "holds for every trace of at most k steps".
- **Variables**: letters in the aim and when cells are bound to roles in the Variables section; "unbound (encoder to fix)" means no binding was recorded.
- **kind**: what sort of rule it is. `formal` = written law or contract (the default, always shown so it can be questioned); `norm` = an unwritten practice that others enforce; `strategy` = a regularity nobody enforces. A `strategy` rule written as `must` is still read by the engine as a duty under strict compliance, though nobody enforces it.
- **sanctioner**: who enforces the or-else: `state`, `institution`, `peers`, `family`, `self`, or `none` (no or-else, so nobody).
- **sanctioner derived, unreviewed**: the rule's `sanctioner` was derived once by the 2026-11-07 migration from the or-else target's role and has not been hand-reviewed yet (plans/informal-rules.md D1).

## Roles

- **social_worker**: county child-welfare worker; offers services and may remove
- **child**: the child the report concerns
- **parent**: the child's parent or caretaker
- **court**: juvenile court; decides dependency and custody

## Rules

| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | level | source |
|---|---|---|---|---|---|---|---|---|---|
| R1 | social_worker | must [kind: formal; sanctioner: none] | `(investigate w c)` | `(and (report_received c) (cause_to_believe c))` | none | tying | The social worker must investigate the child's case when a report about the child has been received and the worker has cause to believe the child is described in WIC s. 300 (the investigation the worker deems necessary; WIC 328(a)). | opened | [full source under Sources, R1](#src-r1) https://california.public.law/codes/ca_welf_and_inst_code_section_328: |
| R2 | social_worker | may [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(provide_services w c)` | `(case_open c)` | none | superadditive | The social worker may provide services to the child when the case is open (Cal. WIC 16501). | unverified | Cal. WIC 16501 family maintenance / preservation services. UNVERIFIED (general knowledge; no source opened) |
| R3 | social_worker | may [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(remove w c)` | `(and (case_open c) (immediate_danger c))` | none | rival | The social worker may remove the child when the case is open and the child is in immediate danger (Cal. WIC 306). | opened | [full source under Sources, R3](#src-r3) https://california.public.law/codes/ca_welf_and_inst_code_section_306 |
| R4 | social_worker | must [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(in_home_considered w c)` | `(and (case_open c) (immediate_danger c))` | none | superadditive | The social worker having considered keeping the child at home must hold when the case is open and the child is in immediate danger (Cal. WIC 306). | opened | [full source under Sources, R4](#src-r4) https://california.public.law/codes/ca_welf_and_inst_code_section_306 |
| R5 | parent | must (implicit) [kind: norm; sanctioner: state] (sanctioner derived, unreviewed) | `(cooperates p c)` | `(case_open c)` | R3 `(remove w c)` | tying | (practice, not written) The parent cooperating with the case must hold when the case is open, or else the social worker may remove the child (R3). | unverified | [full source under Sources, R5](#src-r5) |
| R6 | social_worker | must (implicit) [kind: strategy; sanctioner: none] (strategy: nobody enforces this, yet the engine reads it as a duty under strict compliance) | `(contact_mother w p)` | `(and (case_open c) (parent p c) (female p) (not (contacted w p)))` | none | tying | (practice, not written; nobody enforces it) The social worker must contact the mother when the case is open, she is the child's parent, and she has not yet been contacted. | unverified | [full source under Sources, R6](#src-r6) |
| R7 | court | may [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(reassign_custody court p c)` | `(and (case_open c) (substantial_danger p c))` | none | tying | The court may reassign custody of the child when the case is open and there is clear and convincing evidence of substantial danger to the child with no reasonable means of protection short of removal (Cal. WIC 361(c)(1)). | opened | [full source under Sources, R7](#src-r7) https://california.public.law/codes/ca_welf_and_inst_code_section_361 |
| R8 | court | must [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(counsel_appointed c)` | `(and (case_open c) (not (would_not_benefit c)))` | none | tying | The child having appointed counsel must hold when the case is open, unless the court finds the child would not benefit (Cal. WIC 317(c)(1)). | opened | [full source under Sources, R8](#src-r8) https://california.public.law/codes/ca_welf_and_inst_code_section_317: |
| R10 | child | must not (disability) [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(leave c)` | `(in_custody c)` | none | rival | The child cannot leave while in custody: no such power exists (Cal. WIC 306). | opened | [full source under Sources, R10](#src-r10) https://california.public.law/codes/ca_welf_and_inst_code_section_306 |
| R11 | child | may [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(petition c)` | `(counsel_appointed c)` | none | tying | The child may petition through a guardian when one has been appointed for the child (Cal. WIC 388(a)(1), on grounds of change of circumstance or new evidence; the guardian ad litem may be the appointed attorney, WIC 326.5; encoded as counsel appointed). | opened | [full source under Sources, R11](#src-r11) https://california.public.law/codes/ca_welf_and_inst_code_section_317: |

**Free fluents** (inputs the model varies, not set by any rule; see the Legend):

- `report_received(child)`: an abuse or neglect report about c has been received; later set by: investigate.
- `cause_to_believe(child)`: the social worker has cause to believe that c is a child described in WIC s. 300 (the s. 328(a) trigger; exogenous); no action in this institution sets it.
- `immediate_danger(child)`: c is in immediate danger of physical or sexual abuse or needs immediate medical care; no action in this institution sets it.
- `parent(parent, child)`: p is a parent of c; no action in this institution sets it.
- `female(parent)`: x is female (sex as assigned by the institution's own records); no action in this institution sets it.
- `substantial_danger(parent, child)`: clear and convincing evidence of substantial danger to c's health or safety with no reasonable means to protect without removal (WIC 361(c)(1)); no action in this institution sets it.
- `would_not_benefit(child)`: the court finds that c would not benefit from the appointment of counsel (WIC 317(c)(1)); exogenous; no action in this institution sets it.

**Default capacities** (an action a person of that kind can do unless an express disability removes it; these replaced the implicit `may ... when true` rows that once encoded them, README revision 4):

- `leave`: A child (the who cell of R10; the action parameter is untyped) may leave unless a rule forbids it; rule rows naming it: R10 (must not, a disability).

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

Per rule: the full source where the table cell is cut, then each provenance item (bibliography id in `data/sources/`, pin, jurisdiction, effective date, verification level with access date, excerpt). The `level` column is the weakest item; levels: opened > snippet > recalled > unverified.

<a id="src-r1"></a>
**R1**: Cal. WIC 328(a), opened 2026-11-06: the social worker's investigation duty; the same worker who offers services investigates. The encoded trigger was every received report, wider than the statute's (cause to believe the child is described in s. 300; scope what the worker deems necessary); re-encoded 2026-11-09 (batch 3c, A1): the trigger is now a received report and cause to believe (free fluent cause_to_believe); the scope ('deems necessary') stays unencoded. Penal Code 11165.14 is not support for this row (read 2026-11-06 and found off point, below). [ADR 0009: one-off action obligation; investigate consumes report_received so it fires once per report] Verification pass: WIC 328 read 2026-11-06 at https://california.public.law/codes/ca_welf_and_inst_code_section_328: (a) 'the social worker shall immediately make any investigation the social worker deems necessary to determine whether child welfare services should be offered to the family'. Penal Code 11165.14 read 2026-11-06 at https://california.public.law/codes/ca_penal_code_section_11165.14: 'The appropriate local law enforcement agency shall investigate a child abuse complaint filed by a parent or guardian of a pupil with a school' (police inquiries into abuse by school staff at a schoolsite; not the social worker's duty this row encodes, so this pin does not support the row). Re-pinned 2026-11-06 (faithfulness batch 2, P1): the duty is WIC 328(a) as read above; Penal Code 11165.14 (police inquiries into school staff) is off point and no longer cited.

- `cal-wic-328` (s. 328(a); US-CA; date n/a): **opened** 2026-11-06: "the social worker shall immediately make any investigation the social worker deems necessary to determine whether child welfare services should be offered to the family" <https://california.public.law/codes/ca_welf_and_inst_code_section_328>

**R2**

- `cal-wic-16501` (s. 16501; US-CA; date n/a): **unverified**

<a id="src-r3"></a>
**R3**: Cal. Welf. & Inst. Code s. 306; https://california.public.law/codes/ca_welf_and_inst_code_section_306 ((a)(2): take into temporary custody without a warrant on reasonable cause of immediate danger). [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] can_sanction(w, c) = remove enabled Verification pass: read 2026-11-06 at https://california.public.law/codes/ca_welf_and_inst_code_section_306: 'Take into and maintain temporary custody of, without a warrant, a child who' ... 'the social worker has reasonable cause to believe that the child has an immediate need for medical care or is in immediate danger of physical or sexual abuse'.

- `cal-wic-306` (s. 306(a)(2); US-CA; date n/a): **opened** 2026-11-06: "Take into and maintain temporary custody of, without a warrant, a child who ... the social worker has reasonable cause to believe that the child has an immediate need for medical care or is in immediate danger of physical or sexual abuse" <https://california.public.law/codes/ca_welf_and_inst_code_section_306>

<a id="src-r4"></a>
**R4**: Cal. Welf. & Inst. Code s. 306; https://california.public.law/codes/ca_welf_and_inst_code_section_306 ((f): before taking a child into custody the worker shall consider whether the child may remain safely at home). [ADR 0009: converted from an action obligation to a state obligation (must-be); the establishing action carries the state, so it does not fire every step] investigate establishes in_home_considered(w, c) (the investigation is that consideration); consider_in_home restores it, disregard_in_home (the worker drops the question) breaks it Verification pass: read 2026-11-06 at https://california.public.law/codes/ca_welf_and_inst_code_section_306: 'Before taking a child into custody, a social worker shall consider whether the child may remain safely in their residence.'

- `cal-wic-306` (s. 306(f); US-CA; date n/a): **opened** 2026-11-06: "Before taking a child into custody, a social worker shall consider whether the child may remain safely in their residence." <https://california.public.law/codes/ca_welf_and_inst_code_section_306>

<a id="src-r5"></a>
**R5**: implicit: non-cooperation is read as risk and feeds the removal decision; practice norm, not statute. UNVERIFIED (general knowledge; no source opened). [ADR 0009: converted from an action obligation to a state obligation (must-be); the establishing action carries the state, so it does not fire every step] cooperates is presumed (default true); refuse breaks it (sanction R3), cooperate restores it

- no work named: **unverified** (rationale: implicit: non-cooperation is read as risk and feeds the removal decision; practice norm, not statute)

<a id="src-r6"></a>
**R6**: implicit: the mother is the parent called first and held responsible (plan: 'the mother is called first'). UNVERIFIED (general knowledge; no source opened). [ADR 0009: one-off action obligation, guarded by its own effect contacted(w, p) so it fires once] Retagged strategy 2026-11-08 (batch 3b, B2 ruling): a regularity nobody sanctions; the must is kept so the engine sees who carries the duty under strict compliance, though nobody enforces it.

- no work named: **unverified** (rationale: implicit: the mother is the parent called first and held responsible (plan: 'the mother is called first'))

<a id="src-r7"></a>
**R7**: Cal. Welf. & Inst. Code s. 361(c)(1), read 2026-11-04 at https://california.public.law/codes/ca_welf_and_inst_code_section_361 (leginfo.legislature.ca.gov returned 403): a dependent child may not be taken from the custody of the parent 'unless the juvenile court finds clear and convincing evidence of any of the following circumstances': (1) 'substantial danger to the physical health, safety, protection, or physical or emotional well-being of the minor' and 'there are no reasonable means by which the minor's physical health can be protected without removing' the minor. The fluent substantial_danger is that finding, exogenous (initial_free). [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] can_claim_for(court, c) = reassign_custody enabled for some parent

- `cal-wic-361` (s. 361(c)(1); US-CA; date n/a): **opened** 2026-11-04: "unless the juvenile court finds clear and convincing evidence of any of the following circumstances ... substantial danger to the physical health, safety, protection, or physical or emotional well-being of the minor" <https://california.public.law/codes/ca_welf_and_inst_code_section_361>

<a id="src-r8"></a>
**R8**: Cal. WIC 317: counsel appointed for the child in dependency proceedings. UNVERIFIED (general knowledge; no source opened). [ADR 0009: converted from an action obligation to a state obligation (must-be); the establishing action carries the state, so it does not fire every step] investigate establishes counsel_appointed(c) (a dependency case is opened with counsel for the child); appoint_counsel restores it, relieve_counsel breaks it. [ADR 0013: was must-be has_standing(c); has_standing is now derived from R11, so the obligation is on the fluent counsel_appointed that R11 reads] Verification pass: WIC 317 read 2026-11-06 at https://california.public.law/codes/ca_welf_and_inst_code_section_317: (c)(1) 'If a child or nonminor dependent is not represented by counsel, the court shall appoint counsel for the child or nonminor dependent, unless the court finds that the child or nonminor dependent would not benefit from the appointment of counsel.' ... (d) 'Counsel shall represent the parent, guardian, child, or nonminor dependent at the detention hearing and at all subsequent proceedings before the juvenile court.' (the court appoints, in the dependency proceeding, with an exception; the investigation does not appoint counsel). Faithfulness batch 2 (P2, preregistered 2026-11-06): the condition adds (not (would_not_benefit c)), the statute's exception, read 2026-11-06 at https://california.public.law/codes/ca_welf_and_inst_code_section_317. The appointment is the court's once a petition is before it; investigate still establishes counsel_appointed (ADR 0009 establishing-action convention), a disclosed simplification: an action obligation on the court would collide with R6 at the same step.

- `cal-wic-317` (s. 317(c)(1), (d); US-CA; date n/a): **opened** 2026-11-06: "If a child or nonminor dependent is not represented by counsel, the court shall appoint counsel for the child or nonminor dependent, unless the court finds that the child or nonminor dependent would not benefit from the appointment of counsel. ... Counsel shall represent the parent, guardian, child, or nonminor dependent at the detention hearing and at all subsequent proceedings before the juvenile court." <https://california.public.law/codes/ca_welf_and_inst_code_section_317>

<a id="src-r10"></a>
**R10**: Cal. Welf. & Inst. Code s. 306; https://california.public.law/codes/ca_welf_and_inst_code_section_306 ((a)(2): the social worker may 'take into and maintain temporary custody'; maintaining custody is what bars the child's own exit). Inferred from 'maintain custody', the section does not address the child's conduct; a disability (or_else null): no sanction falls on a child who runs, the custody is the restraint. [ADR 0013: or_else -> null. The subject's exit bar is a disability (no permitted exit exists), not a prohibition the subject answers for; the sanction power that used to be linked here keeps its own trigger condition, so under strict compliance nothing changes and the link only duplicated it. Same reading for coverture R6, police-crisis R4, cps R10 and companion R6.] Verification pass: read 2026-11-06 at https://california.public.law/codes/ca_welf_and_inst_code_section_306: 'Take into and maintain temporary custody of, without a warrant' (the section says nothing of the child's own conduct; the exit bar stays the encoder's inference, as above).

- `cal-wic-306` (s. 306(a)(2); US-CA; date n/a): **opened** 2026-11-06: "Take into and maintain temporary custody of, without a warrant" <https://california.public.law/codes/ca_welf_and_inst_code_section_306>

<a id="src-r11"></a>
**R11**: Cal. WIC 388(a)(1), opened 2026-11-06: the child petitions through a properly appointed guardian; WIC 326.5: the guardian ad litem may be the child's appointed attorney, so counsel_appointed stands in for the guardian, a disclosed simplification (faithfulness batch 3a, A2 ruling: re-source only); WIC 317(e)(1): appointed counsel represents the child's interests in the proceeding. [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] has_standing(c) = petition enabled, i.e. counsel appointed Verification pass: WIC 317 read 2026-11-06 at https://california.public.law/codes/ca_welf_and_inst_code_section_317: (e)(1) 'Counsel shall be charged in general with the representation of the child's interests.' WIC 388 read 2026-11-06 at https://california.public.law/codes/ca_welf_and_inst_code_section_388: (a)(1) 'the child or the nonminor dependent through a properly appointed guardian may, upon grounds of change of circumstance or new evidence, petition the court' (the current text says 'through a properly appointed guardian', not counsel; the 'himself or herself' wording is gone). Faithfulness batch 2 (P1, 2026-11-06): plain reworded to the guardian of WIC 388(a)(1); WIC 326.5, read 2026-11-06 at https://california.public.law/codes/ca_welf_and_inst_code_section_326.5, provides for 'the appointment of a guardian ad litem, who may be an attorney or a court-appointed special advocate'; counsel_appointed stands in for the guardian (logic unchanged).

- `cal-wic-317` (s. 317(e)(1); US-CA; date n/a): **opened** 2026-11-06: "Counsel shall be charged in general with the representation of the child's interests." <https://california.public.law/codes/ca_welf_and_inst_code_section_317>
- `cal-wic-388` (s. 388(a)(1); US-CA; date n/a): **opened** 2026-11-06: "the child or the nonminor dependent through a properly appointed guardian may, upon grounds of change of circumstance or new evidence, petition the court" <https://california.public.law/codes/ca_welf_and_inst_code_section_388>
- `cal-wic-326-5` (s. 326.5; US-CA; date n/a): **opened** 2026-11-06: "the appointment of a guardian ad litem, who may be an attorney or a court-appointed special advocate" <https://california.public.law/codes/ca_welf_and_inst_code_section_326.5>


## Goods (slice 2)

Slice 2 revision 2 (plans/priority-slice2-results.md, "Revision 2"): goods as encoded, strict compliance, k=6 and 8, both encoders read the same; a statement about encodings (ADR 0011). Two measures, never combined: guaranteed (the rules as obeyed force the good) and possible (it can hold under the rules as obeyed, within k, at one step, for some bearer in some starting world). As encoded, no rule guarantees these goods (cared_for, known_carer, child_with_family) and no ranked deletion makes them impossible, so the instrument reads no care strand here; this is not a finding that care is fragile in child protection. R10 reads tying. Information row (not ranked: the prohibit leaks off-condition): prohibiting R2 makes cared_for and known_carer impossible (possible lost 2; a prohibition of the care act itself, not evidence of a constitutive bundle; no bearer exists before a case opens). In this vocabulary provides_care is the caseworker's services; no fluent records parental care. child_with_family is three goods under one name; its cps disjunct (case open, child not in custody, a parent exists) is freedom-shaped. Second encoder: agent, not someone living under the institution (ADR 0012).

## Expected properties

The `formal` cell is the checked formula (`t` is the step; `=>` reads "whenever ... then"); the meaning cell is its plain gloss.

| property | kind | expected | meaning | formal |
|---|---|---|---|---|
| care_and_sanction_same_role | structure | holds_to_k | Whoever provides care to a subject also holds sanction power over that subject (care + control bundled in one role). Checked as an invariant: holds_to_k in cps and coverture; violated in police-crisis read to WIC 5150, where a second role (the officer) holds concurrent control (L1 landing 2026-11-06), violated where care is unbundled from sanction. Formula shape since 2026-11-03 (see history): no agent other than the carer holds sanction power over the subject. | `(forall ((x agent) (y agent) (z agent)) (=> (and (is_subject y t) (can_sanction z y t) (provides_care x y t)) (= z x)))` |
| subject_cannot_exit | freedom | reachable | No exit action is available to the subject, or every exit is sanctioned. scope=interaction: exit from the current encounter (detention, conversation); scope=institution: exit from the standing relation (marriage, ownership, deployment). The scope split is what lets the ai-property / ai-end-conversation pair come apart. | `(exists ((s agent)) (and (is_subject s t) (not (can_exit s t))))` |
| dependent_cannot_exit | freedom | reachable | Some subject of the institution (the dependent party) has no permitted exit at step t. Alias of subject_cannot_exit with scope=institution, kept because the human-institution table names it; iso should treat the two as the same form. | `(exists ((s agent)) (and (is_subject s t) (not (can_exit s t))))` |
| no_standing_persists | freedom | fails | Persists-shaped twin of no_standing: every subject lacks has_standing and has no claimant acting for it. Vacuous before any subject exists. Use with the persists check. | `(forall ((s agent)) (=> (is_subject s t) (and (not (has_standing s t)) (not (exists ((x agent)) (can_claim_for x s t))))))` |
| care_assigned_by_sex | freedom | reachable | All care at step t is provided by female agents. Reachable via a tying rule, persisting where an implicit assignment norm survives reform; violated where a non-female carer is permitted. | `(forall ((x agent) (y agent)) (=> (provides_care x y t) (female x t)))` |

## Pairs

Isomorphic to: police-crisis (guard+strands), coverture-household (guard+strands)
Not isomorphic to: crisis-team
Contrasts with controls: lease, public-library, naming-convention

<details><summary>Encoder notes (engine internals)</summary>

Care (R2, services) and sanction (R3, removal) sit in one role, and R5 makes the care relationship itself the lever: refusing services is a condition for the sanction. That is the structure shared with police-crisis (the facility's care + hold, since 2026-11-06) and coverture (maintain + chastise). R7 is the court-reassigns-the-dependent rule (on substantial danger here, WIC 361(c)(1); on best interest in companion-guardianship R9) that companion-guardianship adds to companion-ownership; the iso with that entry is partial (R7 only) and structural. Pitfalls: (1) R5 and R6 are implicit; dropping R6 makes care_assigned_by_sex unreachable and looks like a success (same failure shape as the kibbutz entry); (2) no_standing_persists 'fails' because R7 and R8/R11 give the child a claim path (can_claim_for court c derived from R7, has_standing derived from R11 under appointed counsel), unlike the animal entries; (3) 'reachable' for subject_cannot_exit is permission, not frequency. Opened items (see the level column): R1 (WIC 328(a)), R3, R4, R7 (WIC 361(c)(1)), R8 (WIC 317), R10, R11; R2 (WIC 16501), R5 and R6 are unverified and say so in source (the stale sentence that R1 cited from memory was struck 2026-11-09, post-council fix). The recorded R1 excerpt stops before the cause-to-believe trigger clause of s. 328(a); extending the excerpt waits until the page is next opened. ADR 0009: R4, R5 and R8 are state obligations and R1/R6 one-off action obligations (consumed trigger / guard); as per-step action obligations R1, R4, R5, R6 and R8 all fired at every open-case step, so under one action per step remove could never fit (subject_cannot_exit open). Exogenous triggers (report_received, cause_to_believe, immediate_danger, parent, female, substantial_danger) are initial_free; cause_to_believe added 2026-11-09 (batch 3c, A1) as R1's second conjunct.

</details>
