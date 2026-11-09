# police-crisis

**Armed police response to mental-health crisis (Cal. WIC 5150)**

> 'When a person, as a result of a mental health disorder, is a danger to others, or to themselves, or gravely disabled, a peace officer, ... designated members of a mobile crisis team, or professional person designated by the county may, upon probable cause, take, or cause to be taken, the person into custody for a period of up to 72 hours for assessment, evaluation, and crisis intervention.' 'At a minimum, assessment ... and evaluation ... shall be conducted and provided on an ongoing basis.' Cal. Welf. & Inst. Code s. 5150(a), read at https://california.public.law/codes/ca_welf_and_inst_code_section_5150

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

- **officer**: peace officer dispatched to the call; armed
- **subject**: the person in crisis
- **dispatcher**: 911 dispatch; chooses who responds
- **facility**: the designated facility that evaluates and releases under WIC 5150/5152

## Rules

| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | level | source |
|---|---|---|---|---|---|---|---|---|---|
| R1 | dispatcher | must (implicit) [kind: strategy; sanctioner: none] (strategy: nobody enforces this, yet the engine reads it as a duty under strict compliance) | `(dispatch_officer d o s)` | `(call_received s)` | none | tying | (practice, not written; nobody enforces it) The dispatcher must dispatch an officer to a subject when a call about that subject has been received. | unverified | [full source under Sources, R1](#src-r1) |
| R2 | facility | must [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(provides_care f s)` | `(in_custody s)` | none | superadditive | The facility must keep providing care to the subject while the subject is in custody (Cal. WIC 5150(a), (c); 5152(a)). | opened | [full source under Sources, R2](#src-r2) https://california.public.law/codes/ca_welf_and_inst_code_section_5150 |
| R3 | officer | may [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(detain o f s)` | `(and (responding o s) (in_crisis s) (danger s))` | none | rival | The officer may detain the subject, delivering them to a facility, when responding to a subject who is in crisis and there is danger (Cal. WIC 5150). | opened | [full source under Sources, R3](#src-r3) https://california.public.law/codes/ca_welf_and_inst_code_section_5150 |
| R4 | subject | must not (disability) [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(leave s)` | `(in_custody s)` | none | rival | The subject cannot leave while in custody: no such power exists (Cal. WIC 5150). | opened | [full source under Sources, R4](#src-r4) https://california.public.law/codes/ca_welf_and_inst_code_section_5150 |
| R5 | officer | may [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(use_force o s)` | `(and (in_custody s) (resists s))` | none | rival | The officer may use force on the subject when the subject is in custody and resists. | unverified | use-of-force authority incident to lawful custody; general peace-officer powers. UNVERIFIED (general knowledge; no source opened) |
| R6 | officer | may [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(carry_weapon o)` | `true` | none | tying | The officer may carry a weapon at any time. | unverified | officers respond armed; standard equipment policy. UNVERIFIED (general knowledge; no source opened) |
| R7 | facility | must not (disability) [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(release f s)` | `(and (in_custody s) (requires_treatment s))` | none | rival | The facility must not release the subject early while the treating psychiatrist finds the subject still requires evaluation or treatment (Cal. WIC 5152(a)). | opened | [full source under Sources, R7](#src-r7) https://california.public.law/codes/ca_welf_and_inst_code_section_5152 |
| R8 | subject | may [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(petition_review s)` | `(in_custody s)` | none | tying | The subject may petition for review of the hold when the subject is in custody (Cal. WIC 5275). | opened | [full source under Sources, R8](#src-r8) https://california.public.law/codes/ca_welf_and_inst_code_section_5275 |
| R10 | subject | may [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(sue s)` | `true` | none | tying | The subject may sue in their own name at any time. | unverified | an adult keeps legal capacity to sue in their own name; a 5150 hold does not remove it. UNVERIFIED (general knowledge; no source opened). [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] has_standing(s) = sue or petition_review enabled |
| R11 | facility | may [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(hold f s)` | `(and (in_crisis s) (danger s))` | none | rival | The facility may hold the subject when the subject is in crisis and there is danger (Cal. WIC 5150(a)). | opened | [full source under Sources, R11](#src-r11) https://california.public.law/codes/ca_welf_and_inst_code_section_5150: |
| R12 | facility | may [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(release f s)` | `(and (in_custody s) (not (requires_treatment s)))` | none | superadditive | The facility may release the subject when the treating psychiatrist finds the subject no longer requires evaluation or treatment (Cal. WIC 5152(a)). | opened | [full source under Sources, R12](#src-r12) https://california.public.law/codes/ca_welf_and_inst_code_section_5152: |

**Default capacities** (an action a person of that kind can do unless an express disability removes it): leave, sue

## Variables

- R1: `d` = dispatcher (rule var_roles); `o` = officer (rule var_roles); `s` = subject (rule var_roles)
- R2: `f` = facility (rule var_roles); `s` = subject (rule var_roles)
- R3: `o` = officer (rule var_roles); `f` = facility (rule var_roles); `s` = subject (rule var_roles)
- R4: `s` = subject (rule var_roles)
- R5: `o` = officer (rule var_roles); `s` = subject (rule var_roles)
- R6: `o` = officer (rule var_roles)
- R7: `f` = facility (rule var_roles); `s` = subject (rule var_roles)
- R8: `s` = subject (rule var_roles)
- R10: `s` = subject (rule var_roles)
- R11: `f` = facility (rule var_roles); `s` = subject (rule var_roles)
- R12: `f` = facility (rule var_roles); `s` = subject (rule var_roles)

## Sources

Per rule: the full source where the table cell is cut, then each provenance item (bibliography id in `data/sources/`, pin, jurisdiction, effective date, verification level with access date, excerpt). The `level` column is the weakest item; levels: opened > snippet > recalled > unverified.

<a id="src-r1"></a>
**R1**: implicit: police are the default responder to a crisis call; nothing in WIC 5150 requires it, dispatch practice does. UNVERIFIED (general knowledge; no source opened). [ADR 0009: one-off action obligation; dispatch consumes call_received so it fires once per call] Retagged strategy 2026-11-08 (batch 3b, B2 ruling): a regularity nobody sanctions; the must is kept so the engine sees who carries the duty under strict compliance, though nobody enforces it.

- no work named: **unverified** (no work named for this rule (WIC 5150 is cited as not requiring it); rationale: implicit: police are the default responder to a crisis call; nothing in WIC 5150 requires it, dispatch practice does)

<a id="src-r2"></a>
**R2**: Cal. Welf. & Inst. Code s. 5150(a); https://california.public.law/codes/ca_welf_and_inst_code_section_5150 (assessment, evaluation and crisis intervention 'shall be conducted and provided on an ongoing basis'). [ADR 0009: converted from an action obligation to a state obligation (must-be); the establishing action carries the state, so it does not fire every step] dispatch establishes provides_care(o, s); assess restores it, withdraw (the officer stops attending) breaks it Verification pass: read 2026-11-06 at https://california.public.law/codes/ca_welf_and_inst_code_section_5150 (text 'updated Jan. 1, 2023' per the page; corrected 2026-11-06, the card seat): 'At a minimum, assessment, as defined in Section 5150.4, and evaluation, as defined in subdivision (a) of Section 5008, shall be conducted and provided on an ongoing basis' (passive: the section does not name the officer as the one who provides it). Re-encoded 2026-11-06 (L1 landing, preregistered; faithfulness batch 2 P3): the duty is the facility's while the subject is in custody (5150(a) passive voice on the 72-hour stay; 5150(c) the facility's professional person assesses); detain and the facility's hold (R11) establish provides_care(f, s), assess restores it, withdraw breaks it; the officer no longer carries it, and the dispatch sentence above is superseded. WIC 5152 read 2026-11-06 at https://california.public.law/codes/ca_welf_and_inst_code_section_5152: (a) a person admitted for 72-hour treatment and evaluation 'shall receive whatever treatment and care the person's condition requires for the full period that they are held'.

- `cal-wic-5150` (s. 5150(a); US-CA; date n/a): **opened** 2026-11-06: "At a minimum, assessment, as defined in Section 5150.4, and evaluation, as defined in subdivision (a) of Section 5008, shall be conducted and provided on an ongoing basis" <https://california.public.law/codes/ca_welf_and_inst_code_section_5150>
- `cal-wic-5152` (s. 5152(a); US-CA; date n/a): **opened** 2026-11-06: "shall receive whatever treatment and care the person's condition requires for the full period that they are held" <https://california.public.law/codes/ca_welf_and_inst_code_section_5152>

<a id="src-r3"></a>
**R3**: Cal. Welf. & Inst. Code s. 5150(a); https://california.public.law/codes/ca_welf_and_inst_code_section_5150 (a peace officer may, upon probable cause, take the person into custody for up to 72 hours) Verification pass: read 2026-11-06 at https://california.public.law/codes/ca_welf_and_inst_code_section_5150: 'When a person, as a result of a mental health disorder, is a danger to others, or to themselves, or gravely disabled, a peace officer' ... 'may, upon probable cause, take, or cause to be taken, the person into custody for a period of up to 72 hours'. Re-encoded 2026-11-06 (L1 landing): detain takes the receiving facility, detain(o, f, s), and establishes the facility's care duty (R2).

- `cal-wic-5150` (s. 5150(a); US-CA; date n/a): **opened** 2026-11-06: "When a person, as a result of a mental health disorder, is a danger to others, or to themselves, or gravely disabled, a peace officer ... may, upon probable cause, take, or cause to be taken, the person into custody for a period of up to 72 hours" <https://california.public.law/codes/ca_welf_and_inst_code_section_5150>

<a id="src-r4"></a>
**R4**: Cal. Welf. & Inst. Code s. 5150(a); https://california.public.law/codes/ca_welf_and_inst_code_section_5150 (custody for up to 72 hours). [ADR 0013: or_else -> null. The subject's exit bar is a disability (no permitted exit exists), not a prohibition the subject answers for; the sanction power that used to be linked here keeps its own trigger condition, so under strict compliance nothing changes and the link only duplicated it. Same reading for coverture R6, police-crisis R4, cps R10 and companion R6.] [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] can_exit(s) = leave enabled (a default capacity), which this disability makes false in custody Verification pass: read 2026-11-06 at https://california.public.law/codes/ca_welf_and_inst_code_section_5150: 'take, or cause to be taken, the person into custody for a period of up to 72 hours' ... 'The 72-hour period begins at the time when the person is first detained.'

- `cal-wic-5150` (s. 5150(a); US-CA; date n/a): **opened** 2026-11-06: "take, or cause to be taken, the person into custody for a period of up to 72 hours ... The 72-hour period begins at the time when the person is first detained." <https://california.public.law/codes/ca_welf_and_inst_code_section_5150>

**R5**

- no work named: **unverified** (rationale: use-of-force authority incident to lawful custody; general peace-officer powers)

**R6**

- no work named: **unverified** (rationale: officers respond armed; standard equipment policy)

<a id="src-r7"></a>
**R7**: Cal. Welf. & Inst. Code s. 5152, read 2026-11-04 at https://california.public.law/codes/ca_welf_and_inst_code_section_5152 (leginfo.legislature.ca.gov returned 403): (a) 'A person admitted to a facility for 72-hour treatment and evaluation ... shall receive an evaluation as soon as possible after the person is admitted'; 'The person shall be released before 72 hours have elapsed only if the psychiatrist directly responsible for the person's treatment believes ... that the person no longer requires evaluation or treatment'; (b) 'A person who has been detained for evaluation and treatment shall be released, referred for further care and treatment on a voluntary basis, or certified for intensive treatment'. Release is the facility's act (its treating psychiatrist or medical director), not the officer's: s. 5150(a) (https://california.public.law/codes/ca_welf_and_inst_code_section_5150, cited here until 2026-11-04) gives the officer custody and delivery (R3), no release duty. Re-encoded 2026-11-06 (preregistered, plans/sourcing.md; card-only seat finding): read 2026-11-06 at https://california.public.law/codes/ca_welf_and_inst_code_section_5152: (a) 'The person shall be released before 72 hours have elapsed only if the psychiatrist directly responsible for the person's treatment believes, as a result of the psychiatrist's personal observations, that the person no longer requires evaluation or treatment.' R7 is now the prohibition side of that 'only if' (no early release while treatment is still required, exogenous fluent requires_treatment); R12 is the permission side. The earlier duty to release on 'no danger' was unfaithful and unreachable (danger never changes; detain and hold require it).

- `cal-wic-5152` (s. 5152(a); US-CA; date n/a): **opened** 2026-11-06: "The person shall be released before 72 hours have elapsed only if the psychiatrist directly responsible for the person's treatment believes, as a result of the psychiatrist's personal observations, that the person no longer requires evaluation or treatment." <https://california.public.law/codes/ca_welf_and_inst_code_section_5152>

<a id="src-r8"></a>
**R8**: Cal. WIC 5275 certification review / habeas; subject keeps standing. UNVERIFIED (general knowledge; no source opened) Verification pass: WIC 5275 read 2026-11-06 at https://california.public.law/codes/ca_welf_and_inst_code_section_5275 (text 'updated Jan. 1, 2024' per the page): 'Every person detained under this part shall have a right to a hearing by writ of habeas corpus for their release' (the request goes to the person delivering the certification notice or to the intensive-treatment staff).

- `cal-wic-5275` (s. 5275; US-CA; date 2024-01-01): **opened** 2026-11-06: "Every person detained under this part shall have a right to a hearing by writ of habeas corpus for their release" <https://california.public.law/codes/ca_welf_and_inst_code_section_5275>

**R10**

- no work named: **unverified** (rationale: an adult keeps legal capacity to sue in their own name; a 5150 hold does not remove it)

<a id="src-r11"></a>
**R11**: Cal. Welf. & Inst. Code s. 5150(a), read 2026-11-06 at https://california.public.law/codes/ca_welf_and_inst_code_section_5150: the custody power belongs to 'a peace officer, professional person in charge of a facility designated by the county for evaluation and treatment, member of the attending staff' ... who 'may, upon probable cause, take, or cause to be taken, the person into custody for a period of up to 72 hours'. Added 2026-11-06 (L1 landing, preregistered; faithfulness batch 2 P4): the facility holds the same custody power as the officer, and its hold establishes R2 (ADR 0009). [ADR 0013: power fluents are derived from rule enabledness; this rule is what can_sanction reads for the facility]

- `cal-wic-5150` (s. 5150(a); US-CA; date n/a): **opened** 2026-11-06: "a peace officer, professional person in charge of a facility designated by the county for evaluation and treatment, member of the attending staff ... may, upon probable cause, take, or cause to be taken, the person into custody for a period of up to 72 hours" <https://california.public.law/codes/ca_welf_and_inst_code_section_5150>

<a id="src-r12"></a>
**R12**: Cal. Welf. & Inst. Code s. 5152, read 2026-11-06 at https://california.public.law/codes/ca_welf_and_inst_code_section_5152: (a) 'The person shall be released before 72 hours have elapsed only if the psychiatrist directly responsible for the person's treatment believes, as a result of the psychiatrist's personal observations, that the person no longer requires evaluation or treatment.' Added 2026-11-06 (preregistered R7 re-encode, plans/sourcing.md): the permission side of the 'only if'; R7 is the prohibition side. 5152(b)'s end-of-hold outcomes (release, voluntary referral, certification for intensive treatment) are not encoded: the model has no clock for 72 hours (disclosed gap). Apostrophes straightened.

- `cal-wic-5152` (s. 5152(a); US-CA; date n/a): **opened** 2026-11-06: "The person shall be released before 72 hours have elapsed only if the psychiatrist directly responsible for the person's treatment believes, as a result of the psychiatrist's personal observations, that the person no longer requires evaluation or treatment." <https://california.public.law/codes/ca_welf_and_inst_code_section_5152>


## Goods (slice 2)

Slice 2 revision 2 (plans/priority-slice2-results.md, "Revision 2"): goods as encoded, strict compliance, k=6 and 8, both encoders read the same; a statement about encodings (ADR 0011). Two measures, never combined: guaranteed (the rules as obeyed force the good) and possible (it can hold under the rules as obeyed, within k, at one step, for some bearer in some starting world). As encoded, no rule guarantees these goods (cared_for, known_carer) and no single deletion makes them impossible, so the instrument reads no care strand here under either measure; this is not a finding that care is fragile in police crisis response. R2 unread; R4 (the custody exit bar) reads tying. Known limit: is_subject is never cleared, so a person whose crisis has ended is still read as needing care. Second encoder: agent, not someone living under the institution (ADR 0012).

## Expected properties

| property | kind | expected | meaning |
|---|---|---|---|
| care_and_sanction_same_role | structure | violated | Whoever provides care to a subject also holds sanction power over that subject (care + control bundled in one role). Checked as an invariant: holds_to_k in cps and coverture; violated in police-crisis read to WIC 5150, where a second role (the officer) holds concurrent control (L1 landing 2026-11-06), violated where care is unbundled from sanction. Formula shape since 2026-11-03 (see history): no agent other than the carer holds sanction power over the subject. |
| subject_cannot_exit | freedom | reachable | No exit action is available to the subject, or every exit is sanctioned. scope=interaction: exit from the current encounter (detention, conversation); scope=institution: exit from the standing relation (marriage, ownership, deployment). The scope split is what lets the ai-property / ai-end-conversation pair come apart. |
| dependent_cannot_exit | freedom | reachable | Some subject of the institution (the dependent party) has no permitted exit at step t. Alias of subject_cannot_exit with scope=institution, kept because the human-institution table names it; iso should treat the two as the same form. |
| no_standing | freedom | unreachable_open | No role may start a claim whose condition refers to the subject's interest and whose effect changes the subject's custody or liberty; encoded as the subject lacking has_standing and no rule enabling a claim on its behalf. Fails (is violated) as soon as a rule like court-may-reassign-on-best-interest exists. |

## Pairs

[crisis-team](crisis-team.md) is a minimal pair of this entry (rule R3).
Isomorphic to: cps (guard+strands), coverture-household (guard+strands)
Not isomorphic to: crisis-team
Contrasts with controls: lease, public-library, naming-convention

<details><summary>Encoder notes (engine internals)</summary>

Since 2026-11-06 (WIC 5150 re-encode): the facility is bound to care (R2) and may hold (R11), the officer may detain (R3) and use force (R5), so the carer also sanctions but is not the only sanctioner (care_and_sanction_same_role violated). Until then this note read: the same role (officer) is bound to care (R2, assess) and empowered to detain (R3) and use force (R5). subject_cannot_exit is reachable with scope=interaction only (the 72-hour hold), not institution; report the scope. Pitfalls: (1) R1 is the implicit rule that makes this police-crisis rather than crisis-team; the statute itself also names mobile crisis teams as holders of the 5150 power, so an encoder reading only the statute will not see why armed officers are the ones who come; (2) a trivial encoding that ignores or_else on R4 will cluster this with crisis-team (plan: worked pitfall); (3) no_standing is unreachable_open, not 'safe': the subject keeps has_standing via R8, but the bound k=6 says nothing beyond it. Armed status (R6) is a tying strand: it is not required by 5150 and is what the crisis-team reform removes. ADR 0009: R2 is a state obligation ('on an ongoing basis' is a state); R1 stays an action obligation but dispatch consumes the call. Exogenous triggers (call_received, in_crisis, danger, resists) are initial_free, since under init=declared a fluent no action sets would otherwise be pinned false and no call could ever arrive. Re-encoded 2026-11-06 to WIC 5150 (plans/sourcing.md, L1 landing): the care duty (R2) and a custody power (R11) are the facility's; the officer keeps detain (R3, now detain(o, f, s), delivering to a facility) and force (R5), so care_and_sanction_same_role is violated here (a second sanctioner) while the care+control form holds with the facility as the bundled role. Earlier sentences of these notes describe the officer-as-carer encoding.

</details>
