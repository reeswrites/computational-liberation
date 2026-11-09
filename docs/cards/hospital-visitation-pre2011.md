# hospital-visitation-pre2011

**US hospital visitation before 2011: policy admits immediate family, staff decide who counts (minimal pair base)**

> Before the 2011 Medicare rule there was no federal visitor-choice standard (North Carolina had amended its Patients' Bill of Rights to let patients designate visitors, as the Presidential Memorandum of 2010-04-15 notes; no other state rule is encoded). The memorandum describes the practice: 'a widow or widower with no children is denied the support and comfort of a good friend', members of religious orders 'unable to choose someone other than an immediate family member to visit them', 'gay and lesbian Americans who are often barred from the bedsides of the partners'; the final rule's comment responses speak of practice that 'denies patients access to their loved ones in times of need' (75 FR 70831). Both are regulators' descriptions; no pre-2011 hospital policy text was opened (plans/sourcing-worklist-marriage.md). Encoded as a reconstructed formal policy gate (R4: the spouse must be recognised as family; R8: family are admitted) over an informal staff gate (R2: staff decide who else counts; R3: staff may not admit anyone they do not count), a general permission to admit visitors (R5) that R3 narrows, and the restriction exception (R7) that the 2011 rule kept.

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

- **patient**: the admitted patient whose visitors are at issue
- **partner**: the would-be visitor; a spouse or an unmarried partner, depending on the trace (married is exogenous here)
- **staff**: the charge nurse or unit staff who decide who counts as family and admit visitors
- **hospital**: the hospital as an institution (administration); sets visitation policy and disciplines staff

## Rules

| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | level | source |
|---|---|---|---|---|---|---|---|---|---|
| R1 | staff | may [kind: formal; sanctioner: none] | `(admit s p)` | `(not (admitted p))` | none | untagged (null) | Staff may admit a patient who is not already admitted. | unverified | Encoder's device: admission is the event that makes visitation a question; no source read for it. UNVERIFIED (general knowledge; no source opened). |
| R2 | staff | may (implicit) [kind: norm; sanctioner: none] | `(recognize_family s p x)` | `(and (admitted p) (not (counts_as_family p x)))` | none | tying | (practice, not written; reconstruction, no policy text found) Staff may treat any visitor as family of an admitted patient: the charge nurse decides who counts. | unverified | [full source under Sources, R2](#src-r2) |
| R3 | staff | must not (implicit) [kind: norm; sanctioner: institution] | `(admit_visitor s x p)` | `(not (counts_as_family p x))` | R6 `(reprimand o s)` | tying | (practice, not written; reconstruction, no policy text found) Staff must not admit as a visitor anyone they do not count as family, or else the hospital may reprimand them (R6). | unverified | [full source under Sources, R3](#src-r3) |
| R4 | staff | must [kind: formal; sanctioner: institution] | `(recognize_family s p x)` | `(and (admitted p) (married p x) (not (counts_as_family p x)))` | R6 `(reprimand o s)` | tying | (reconstruction, no policy text found) Staff must recognise an admitted patient's spouse as family (hospital policy admits immediate family), or else the hospital may reprimand them (R6). | unverified | [full source under Sources, R4](#src-r4) |
| R5 | staff | may [kind: formal; sanctioner: none] | `(admit_visitor s x p)` | `(and (admitted p) (not (clinically_restricted p)))` | none | superadditive | Staff may admit any visitor to an admitted patient unless visiting is restricted (the general permission that the staff norm R3 narrows; the entry models every restriction as clinical, the 2011 text says clinically necessary or reasonable). | unverified | [full source under Sources, R5](#src-r5) |
| R6 | hospital | may [kind: formal; sanctioner: none] | `(reprimand o s)` | `true` | none | untagged (null) | The hospital may reprimand staff (the sanction behind R3 and R4). | unverified | Encoder's sanction holder for the hospital's own policy (R4) and the staff norm (R3): employer discipline. No disciplinary text found. UNVERIFIED (general knowledge; no source opened). |
| R7 | staff | may [kind: formal; sanctioner: none] | `(restrict s p)` | `(admitted p)` | none | untagged (null) | Staff may restrict visiting to an admitted patient (grounds not modelled; the rule says clinically necessary or reasonable restriction). | unverified | [full source under Sources, R7](#src-r7) |
| R8 | staff | must [kind: formal; sanctioner: institution] | `(admit_visitor s x p)` | `(and (admitted p) (counts_as_family p x) (not (clinically_restricted p)) (not (visiting x p)))` | R6 `(reprimand o s)` | superadditive | (reconstruction, no policy text found) Staff must admit a visitor they count as family of an admitted patient when visiting is not restricted and that visitor is not already visiting, or else the hospital may reprimand them (R6). | unverified | [full source under Sources, R8](#src-r8) |

**Free fluents** (inputs the model varies, not set by any rule; see the Legend): none

**Default capacities** (an action a person of that kind can do unless an express disability removes it; these replaced the implicit `may ... when true` rows that once encoded them, README revision 4): none

## Variables

- R1: `s` = staff (rule var_roles); `p` = patient (rule var_roles)
- R2: `s` = staff (rule var_roles); `p` = patient (rule var_roles); `x` = partner (rule var_roles)
- R3: `s` = staff (rule var_roles); `x` = partner (rule var_roles); `p` = patient (rule var_roles)
- R4: `s` = staff (rule var_roles); `p` = patient (rule var_roles); `x` = partner (rule var_roles)
- R5: `s` = staff (rule var_roles); `x` = partner (rule var_roles); `p` = patient (rule var_roles)
- R6: `o` = hospital (rule var_roles); `s` = staff (rule var_roles)
- R7: `s` = staff (rule var_roles); `p` = patient (rule var_roles)
- R8: `s` = staff (rule var_roles); `x` = partner (rule var_roles); `p` = patient (rule var_roles)

## Sources

Per rule: the full source where the table cell is cut, then each provenance item (bibliography id in `data/sources/`, pin, jurisdiction, effective date, verification level with access date, excerpt). The `level` column is the weakest item; levels: opened > snippet > recalled > unverified.

**R1**

- no work named: **unverified** (rationale: admission is the precondition of visitation and is not itself regulated here)

<a id="src-r2"></a>
**R2**: The informal gate. No hospital policy text names the decider. Evidence that non-relatives were excluded while immediate family were admitted is the 2010 Presidential Memorandum's own description of practice: 'a widow or widower with no children is denied the support and comfort of a good friend'; members of religious orders 'unable to choose someone other than an immediate family member to visit them'; 'gay and lesbian Americans who are often barred from the bedsides of the partners' (hv-presmemo-2010, opened); and the final rule's comment response on practice that 'denies patients access to their loved ones in times of need' (hv-fr-2010-final-rule, opened). That the exclusion was exercised as staff discretion rather than written policy is the encoder's reading (ASSUMED); Lambda Legal's 2010 survey (hv-ll-2010-wcnc) could not be opened. The memo's sentence 'no more restrictive than those that immediate family members enjoy' is its target standard for designated visitors, not a description of the baseline (council 2026-11-08). Tag note: a permission carries no sanction of its own; the sanction that bounds the discretion is R3's (sanctioner institution). D1 defines a norm as sanctioned; this `may` half of the practice is tagged norm with sanctioner none knowingly, and whether it should read strategy is an open question for the author (council 2026-11-08).

- `hv-presmemo-2010` (paras. 1-2 (practice described); US; date 2010-04-15): **snippet** 2026-11-08: "a widow or widower with no children is denied the support and comfort of a good friend ... unable to choose someone other than an immediate family member to visit them ... gay and lesbian Americans who are often barred from the bedsides of the partners" <https://obamawhitehouse.archives.gov/the-press-office/presidential-memorandum-hospital-visitation>
- `hv-fr-2010-final-rule` (Part II, response to comments (CAH visitation subsection); US; date 2011-01-18): **snippet** 2026-11-08: "denies patients access to their loved ones in times of need" <https://www.govinfo.gov/content/pkg/FR-2010-11-19/html/2010-29194.htm>
- `hv-ll-2010-wcnc` (US; date n/a): **unverified** <https://legacy.lambdalegal.org/sites/default/files/publications/downloads/whcic_report_when-health-care-isnt-caring.pdf>

<a id="src-r3"></a>
**R3**: The sanctioned side of the informal gate: a visitor staff do not count as family is not admitted. Evidence for the exclusion is the memo's description of practice ('a widow or widower with no children is denied the support and comfort of a good friend'; members of religious orders 'unable to choose someone other than an immediate family member to visit them'; 'gay and lesbian Americans who are often barred from the bedsides of the partners', hv-presmemo-2010, opened) and the final rule's 'denies patients access to their loved ones in times of need' (hv-fr-2010-final-rule, opened). That staff who admitted non-family answered to the hospital is the encoder's inference from the existence of a policy (ASSUMED; no disciplinary text found, unverified item below).

- `hv-presmemo-2010` (paras. 1-2 (practice described); US; date 2010-04-15): **snippet** 2026-11-08: "a widow or widower with no children is denied the support and comfort of a good friend ... unable to choose someone other than an immediate family member to visit them ... gay and lesbian Americans who are often barred from the bedsides of the partners" <https://obamawhitehouse.archives.gov/the-press-office/presidential-memorandum-hospital-visitation>
- `hv-fr-2010-final-rule` (Part II, response to comments (CAH visitation subsection); US; date 2011-01-18): **snippet** 2026-11-08: "denies patients access to their loved ones in times of need" <https://www.govinfo.gov/content/pkg/FR-2010-11-19/html/2010-29194.htm>
- no work named: **unverified** (rationale: the sanction on staff who admit non-family is inferred, not sourced; no pre-2011 hospital policy text or state hospital association model policy was found or opened (plans/sourcing-worklist-marriage.md hv-pre2011-practice), so the rule as a hospital rule is unverified)

<a id="src-r4"></a>
**R4**: The formal gate before 2011: hospital policy, not law. No pre-2011 hospital policy text or state hospital association model policy with 'immediate family' wording was found or opened (unverified item below), so written-ness is ASSUMED and `kind: formal` rests on the ordinary existence of hospital visiting policies. That immediate family were admitted where others were not is the memo's description of practice: members of religious orders were 'unable to choose someone other than an immediate family member to visit them', while 'a widow or widower with no children is denied the support and comfort of a good friend' and 'gay and lesbian Americans who are often barred from the bedsides of the partners' (hv-presmemo-2010, opened). The memo's 'no more restrictive than those that immediate family members enjoy' is its target standard for designees, not the baseline (council 2026-11-08). Immediate family other than the spouse is not encoded (one visitor role). Written as an action obligation (must recognise) because no action can establish counts_as_family for the spouse at admission (ADR 0009 note). That recognition was a DUTY on staff rather than custom is ASSUMED; this rule, with R8, is what makes spouse_visit_guaranteed hold, so the guarantee is an encoding claim about the reconstructed policy (council 2026-11-08).

- `hv-presmemo-2010` (paras. 1-2 (practice described); US; date 2010-04-15): **snippet** 2026-11-08: "a widow or widower with no children is denied the support and comfort of a good friend ... unable to choose someone other than an immediate family member to visit them ... gay and lesbian Americans who are often barred from the bedsides of the partners" <https://obamawhitehouse.archives.gov/the-press-office/presidential-memorandum-hospital-visitation>
- `hv-presmemo-2010` (para. 3 (the target standard); US; date 2010-04-15): **opened** 2026-11-08: "no more restrictive than those that immediate family members enjoy" <https://obamawhitehouse.archives.gov/the-press-office/presidential-memorandum-hospital-visitation>
- no work named: **unverified** (rationale: a hospital policy obliging staff to treat the spouse as family is reconstructed from the memos description, not read; no pre-2011 hospital policy text or state hospital association model policy was found or opened (plans/sourcing-worklist-marriage.md hv-pre2011-practice), so the rule as a hospital rule is unverified)

<a id="src-r5"></a>
**R5**: The general permission the staff norm narrows (R3 bars non-family; R8 obliges family). Post-2011 text cited for a pre-2011 rule: the 2011 rule keeps restriction to a 'clinically necessary or reasonable restriction' (42 CFR 482.13(h) introductory text; hv-fr-2010-final-rule and hv-cfr-482-13-h, opened; Transmittal 75 A-0217 reads it as a bar on the hospital differentiating among visitors 'without any clinically necessary or reasonable basis', hv-cms-r75soma, opened). Before 2011 the permission is the encoder's reconstruction of ordinary practice: UNVERIFIED (item below).

- `hv-fr-2010-final-rule` (42 CFR 482.13(h) introductory text, as added; US; date 2011-01-18): **snippet** 2026-11-08: "clinically necessary or reasonable restriction" <https://www.govinfo.gov/content/pkg/FR-2010-11-19/html/2010-29194.htm>
- no work named: **unverified** (rationale: a general permission to admit visitors before 2011 is reconstructed; no pre-2011 hospital policy text or state hospital association model policy was found or opened (plans/sourcing-worklist-marriage.md hv-pre2011-practice), so the rule as a hospital rule is unverified)

**R6**

- no work named: **unverified** (rationale: a hospital policy is enforced by the hospital on its staff)

<a id="src-r7"></a>
**R7**: The restriction exception, unchanged across the pair. After 2011 it is in 42 CFR 482.13(h): 'clinically necessary or reasonable restriction' (hv-fr-2010-final-rule, opened by the worklist); CMS Transmittal 75 puts 'the burden of proof is upon the hospital to demonstrate that the visitation restriction is reasonably necessary to provide safe care' (hv-cms-r75soma, opened by the worklist and re-opened 2026-11-08 from the PDF text). Before 2011 the same clinical judgment is assumed to have existed without the burden of proof (post-2011 text cited for a pre-2011 rule; unverified item below); the burden is not encoded. Grounds are not modelled: restrict is a free staff act, which over-reads staff power (recorded).

- `hv-fr-2010-final-rule` (42 CFR 482.13(h) introductory text, as added; US; date 2011-01-18): **snippet** 2026-11-08: "clinically necessary or reasonable restriction" <https://www.govinfo.gov/content/pkg/FR-2010-11-19/html/2010-29194.htm>
- `hv-cms-r75soma` (A-0215; US; date 2011-12-02): **opened** 2026-11-08: "the burden of proof is upon the hospital to demonstrate that the visitation restriction is reasonably necessary to provide safe care" <https://www.cms.gov/regulations-and-guidance/guidance/transmittals/downloads/r75soma.pdf>
- no work named: **unverified** (rationale: a pre-2011 clinical-restriction power is reconstructed; no pre-2011 hospital policy text or state hospital association model policy was found or opened (plans/sourcing-worklist-marriage.md hv-pre2011-practice), so the rule as a hospital rule is unverified)

<a id="src-r8"></a>
**R8**: Hospital policy before 2011: immediate family are admitted. No policy text was opened (unverified item below). The memo describes immediate family as the class admitted as of course (members of religious orders 'unable to choose someone other than an immediate family member to visit them', while 'a widow or widower with no children is denied the support and comfort of a good friend' and 'gay and lesbian Americans who are often barred from the bedsides of the partners', hv-presmemo-2010, opened). Written as a duty (must), not a permission, so that the spouse's visit is guaranteed and not merely possible; whether hospitals treated family admission as a duty on themselves is the encoder's reading and the largest over-read in the entry (council 2026-11-08): the source shows custom, not a duty. The 'not visiting' conjunct makes the duty fire once (one action slot per step).

- `hv-presmemo-2010` (paras. 1-2 (practice described); US; date 2010-04-15): **snippet** 2026-11-08: "a widow or widower with no children is denied the support and comfort of a good friend ... unable to choose someone other than an immediate family member to visit them ... gay and lesbian Americans who are often barred from the bedsides of the partners" <https://obamawhitehouse.archives.gov/the-press-office/presidential-memorandum-hospital-visitation>
- no work named: **unverified** (rationale: a duty on staff to admit family is reconstructed from the memos description of custom; no pre-2011 hospital policy text or state hospital association model policy was found or opened (plans/sourcing-worklist-marriage.md hv-pre2011-practice), so the rule as a hospital rule is unverified)


## Expected properties

| property | kind | expected | meaning |
|---|---|---|---|
| spouse_visit_guaranteed | structure | holds_to_k | An admitted patient's spouse is admitted as a visitor within two steps of admission-and-marriage both holding, provided visiting was not clinically restricted at those steps (the two grace steps let a must-recognise rule and then a must-admit rule fire, one action per step). Written for the hospital-visitation pair and the coverture composite (plans/informal-rules.md slice 1, preregistered 2026-11-08). holds_to_k where a formal gate recognises the spouse as family and a duty admits family; violated when the only route is staff discretion or an unforced designation. Reads whether the spouse's visit is guaranteed, as opposed to possible. |
| spouse_visit_possible | structure | reachable | Some compliant trace reaches a step where an admitted patient's spouse has been admitted as a visitor. Reachable in both sides of the hospital-visitation pair and in the composite; read with spouse_visit_guaranteed: guaranteed lost while possible kept is the displaced verdict (plans/informal-rules.md D3), both lost is no backstop found. |
| unmarried_partner_visit_possible | structure | reachable | Some compliant trace reaches a step where an admitted patient's unmarried partner has been admitted as a visitor. Before 2011 only through staff discretion (the informal gate: R2 recognises, R8 then admits) or with the staff norm R3 gone; after 2011 also through the patient's designation (R10, R9). unreachable_open when no route exists: the attribute set the formal spouse gate never covered. |

## Pairs

Extended by: [hospital-visitation](hospital-visitation.md)
[hospital-visitation](hospital-visitation.md) is a minimal pair of this entry (rule R9).

<details><summary>Encoder notes (engine internals)</summary>

Base of the hospital-visitation minimal pair (plans/informal-rules.md R1; preregistered there 2026-11-08 before the first run). Council 2026-11-08 (docs/reviews/2026-11-08-hospital-slice.md): R4 and R8 are duties reconstructed from the memo's description of custom, so spouse_visit_guaranteed is a claim about the reconstruction, and 'no state rule' holds federally only (North Carolina had a designation law); R2 is a may tagged norm with sanctioner none, D1's sanction requirement being carried by R3 (open question for the author: norm or strategy). Vocabulary follows plans/sourcing-worklist-marriage.md section 4 with these changes: the hospital is split into staff (who decide and admit) and hospital (who sanction), so the institution sanction has a holder; the kin role is dropped (one visitor role, married exogenous, so the same role is the spouse in some traces and the unmarried partner in others); deny_visitor is dropped (non-admission is the default); can_visit as a derived power is dropped, because the engine's (enabled ...) ignores a sanctioned must_not (only an or_else-null disability blocks enablement, rules_lower.py), so a power fluent could not see the staff norm; the properties read the admission itself (visiting) on compliant traces, where every must_not binds under strict compliance. married has no setter here, so it is exogenous and free; in the coverture composite marry sets it. Engine facts the encoding leans on: a regulated action (one some may/must names) fires only at a step where some may/must condition on that instance holds, so R5 is what lets any visitor through and R3 is what stops non-family; one action per step (step-mode one), so a must-do that fires takes the step; a trace where two different must-do instances fire at one step is not compliant and is excluded, not counted. spouse_visit_guaranteed therefore has two grace steps (R4 recognises at t0, R8 admits at t1, visiting holds at t2). The formal gate is R4 (function: sorts_who_belongs; prediction: deleting it flips spouse_visit_guaranteed to violated while spouse_visit_possible stays reachable via R2). The informal gate is R2 + R3 (function: sorts_who_belongs; predictions: deleting R2 flips unmarried_partner_visit_possible to unreachable_open, since no other rule lets a non-spouse count; deleting R3 keeps it reachable and makes it reachable without recognition, since R5 permits any visitor). Deleting R8 flips spouse_visit_guaranteed to violated (admission no longer forced) and nothing else; deleting R5 flips nothing (R8 is also a permission). ASSUMED: the split roles, the family-admission duty (R8) and R4 as an action obligation; the card-only seat judges them. Consent guard note (plans/consent-guard-note-DRAFT.md) ruled not applicable to visitor-access rules by the author, 2026-11-08.

</details>
