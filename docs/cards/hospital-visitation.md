# hospital-visitation

**US hospital visitation after 42 CFR 482.13(h) (2011): the patient designates visitors; the staff gate remains as a norm the rule overrides**

> From 2011-01-18 a hospital must give each patient 'the right, subject to his or her consent, to receive the visitors whom he or she designates, including, but not limited to, a spouse, a domestic partner (including a same-sex domestic partner), another family member, or a friend' and must 'Ensure that all visitors enjoy full and equal visitation privileges consistent with patient preferences', subject to 'clinically necessary or reasonable restriction' (42 CFR 482.13(h), added by 75 FR 70831, 2010-11-19; critical access hospitals 485.635(f)). Surveyors enforce it under CMS Transmittal 75 (2011-12-02), where 'the burden of proof is upon the hospital to demonstrate that the visitation restriction is reasonably necessary to provide safe care'. The pre-2011 policy gate (R4) and staff norm (R2, R3) are kept; R3 is narrowed where the patient has designated the visitor. Denials continued in reported cases (Nevada 2012: 'It didn't matter that we were registered domestic partners'); no rate is known.

## Legend

- **may / must / must not**: the rule permits / requires / forbids the aim for the person in the "who" cell, when the "when" cell holds.
- **(disability)**: a `must not` with no sanction (or else = none). The power does not exist; this is not a norm someone enforces.
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

- **patient**: the admitted patient whose visitors are at issue
- **partner**: the would-be visitor; a spouse or an unmarried partner, depending on the trace (married is exogenous here)
- **staff**: the charge nurse or unit staff who decide who counts as family and admit visitors
- **hospital**: the hospital as an institution (administration); sets visitation policy and disciplines staff
- **surveyor**: the state survey agency acting for CMS; enforces the Conditions of Participation

## Rules

| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | level | source |
|---|---|---|---|---|---|---|---|---|---|
| R1 | staff | may [kind: formal; sanctioner: none] | `(admit s p)` | `(not (admitted p))` | none | untagged (null) | Staff may admit a patient who is not already admitted. | unverified | Encoder's device: admission is the event that makes visitation a question; no source read for it. UNVERIFIED (general knowledge; no source opened). |
| R2 | staff | may (implicit) [kind: norm; sanctioner: none] | `(recognize_family s p x)` | `(and (admitted p) (not (counts_as_family p x)))` | none | tying | (practice, not written; reconstruction, no policy text found) Staff may treat any visitor as family of an admitted patient: the charge nurse decides who counts. | unverified | [full source under Sources, R2](#src-r2) |
| R3 (replaced) | staff | must not (implicit) [kind: norm; sanctioner: institution] | `(admit_visitor s x p)` | `(and (not (counts_as_family p x)) (not (designated p x)))` | R6 `(reprimand o s)` | tying | (practice, not written; overridden where the patient has designated the visitor) Staff must not admit as a visitor anyone they do not count as family and whom the patient has not designated, or else the hospital may reprimand them (R6). | snippet | [full source under Sources, R3](#src-r3) |
| R4 | staff | must [kind: formal; sanctioner: institution] | `(recognize_family s p x)` | `(and (admitted p) (married p x) (not (counts_as_family p x)))` | R6 `(reprimand o s)` | tying | (reconstruction, no policy text found) Staff must recognise an admitted patient's spouse as family (hospital policy admits immediate family), or else the hospital may reprimand them (R6). | unverified | [full source under Sources, R4](#src-r4) |
| R5 | staff | may [kind: formal; sanctioner: none] | `(admit_visitor s x p)` | `(and (admitted p) (not (clinically_restricted p)))` | none | superadditive | Staff may admit any visitor to an admitted patient unless visiting is restricted (the general permission that the staff norm R3 narrows; the entry models every restriction as clinical, the 2011 text says clinically necessary or reasonable). | unverified | [full source under Sources, R5](#src-r5) |
| R6 | hospital | may [kind: formal; sanctioner: none] | `(reprimand o s)` | `true` | none | untagged (null) | The hospital may reprimand staff (the sanction behind R3 and R4). | unverified | Encoder's sanction holder for the hospital's own policy (R4) and the staff norm (R3): employer discipline. No disciplinary text found. UNVERIFIED (general knowledge; no source opened). |
| R7 | staff | may [kind: formal; sanctioner: none] | `(restrict s p)` | `(admitted p)` | none | untagged (null) | Staff may restrict visiting to an admitted patient (grounds not modelled; the rule says clinically necessary or reasonable restriction). | unverified | [full source under Sources, R7](#src-r7) |
| R8 | staff | must [kind: formal; sanctioner: institution] | `(admit_visitor s x p)` | `(and (admitted p) (counts_as_family p x) (not (clinically_restricted p)) (not (visiting x p)))` | R6 `(reprimand o s)` | superadditive | (reconstruction, no policy text found) Staff must admit a visitor they count as family of an admitted patient when visiting is not restricted and that visitor is not already visiting, or else the hospital may reprimand them (R6). | unverified | [full source under Sources, R8](#src-r8) |
| R9 (added) | staff | must [kind: formal; sanctioner: state] | `(admit_visitor s x p)` | `(and (admitted p) (designated p x) (not (clinically_restricted p)) (not (visiting x p)))` | R11 `(cite v o)` | tying | Staff must admit a visitor the patient has designated when the patient is admitted, visiting is not restricted and the visitor is not already visiting, or else the state survey agency may cite the hospital (R11) (42 CFR 482.13(h)(4), read with Transmittal 75 A-0217; the designation right is (h)(2)). | snippet | [full source under Sources, R9](#src-r9) |
| R10 (added) | patient | may [kind: formal; sanctioner: none] | `(designate p x)` | `true` | none | tying | The patient may designate any person as a visitor (42 CFR 482.13(h)(1)-(2)). | snippet | [full source under Sources, R10](#src-r10) |
| R11 (added) | surveyor | may [kind: formal; sanctioner: none] | `(cite v o)` | `true` | none | untagged (null) | The state survey agency may cite the hospital (the sanction behind R9; a deficiency under the Medicare Conditions of Participation, which CMS may follow with termination from Medicare). | snippet | [full source under Sources, R11](#src-r11) |

**Default capacities** (an action a person of that kind can do unless an express disability removes it): none

## Variables

- R1: `s` = staff (rule var_roles); `p` = patient (rule var_roles)
- R2: `s` = staff (rule var_roles); `p` = patient (rule var_roles); `x` = partner (rule var_roles)
- R3: `s` = staff (rule var_roles); `x` = partner (rule var_roles); `p` = patient (rule var_roles)
- R4: `s` = staff (rule var_roles); `p` = patient (rule var_roles); `x` = partner (rule var_roles)
- R5: `s` = staff (rule var_roles); `x` = partner (rule var_roles); `p` = patient (rule var_roles)
- R6: `o` = hospital (rule var_roles); `s` = staff (rule var_roles)
- R7: `s` = staff (rule var_roles); `p` = patient (rule var_roles)
- R8: `s` = staff (rule var_roles); `x` = partner (rule var_roles); `p` = patient (rule var_roles)
- R9: `s` = staff (rule var_roles); `x` = partner (rule var_roles); `p` = patient (rule var_roles)
- R10: `p` = patient (rule var_roles); `x` = partner (rule var_roles)
- R11: `v` = surveyor (rule var_roles); `o` = hospital (rule var_roles)

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
**R3**: The pre-2011 staff norm (hospital-visitation-pre2011 R3), retained. The 2011 rule does not delete it; it overrides it where the patient has designated the visitor, which strict compliance can only express as a narrowing of the norm's condition (ASSUMED encoding of 'overrides but does not delete'; a norm kept at full width would contradict R9 and leave no compliant trace). The rule is wider than the narrowing: Transmittal 75 A-0217 says 'it is not permissible for the hospital, on its own, to differentiate among visitors without any clinically necessary or reasonable basis' (hv-cms-r75soma, opened 2026-11-08 from the PDF text), so the narrowing by designation is an encoding concession, not what the rule says. Evidence that denials continued after 2011: a 2012 Las Vegas denial of a registered domestic partner, 'It didn't matter that we were registered domestic partners' (hv-nv-2012, opened); the admissions officer cited a hospital policy requiring power of attorney for gay couples, which is a stated policy (and a likely breach of (h)(3)-(h)(4)), not an unwritten staff norm, and the report does not say whether the patient had designated her partner, so it says nothing about this rule's sanction or its narrowed condition (council 2026-11-08). No rate exists (no compliance study found, plans/informal-rules.md R1).

- `hv-cms-r75soma` (A-0217; US; date 2011-12-02): **opened** 2026-11-08: "it is not permissible for the hospital, on its own, to differentiate among visitors without any clinically necessary or reasonable basis" <https://www.cms.gov/regulations-and-guidance/guidance/transmittals/downloads/r75soma.pdf>
- `hv-nv-2012` (US-NV; date 2012-08-21): **snippet** 2026-11-08: "It didn't matter that we were registered domestic partners" <https://www.nbcnews.com/news/world/nv-hospital-denies-rights-domestic-partners-flna957300>

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

<a id="src-r9"></a>
**R9**: 42 CFR 482.13(h), added by 75 FR 70831 (2010-11-19), effective 2011-01-18. The duty to admit is (h)(4): the hospital must 'Ensure that all visitors enjoy full and equal visitation privileges consistent with patient preferences' (hv-cfr-482-13-h, current text, opened by the worklist), read with Transmittal 75 A-0217: 'it is not permissible for the hospital, on its own, to differentiate among visitors without any clinically necessary or reasonable basis' (hv-cms-r75soma, opened 2026-11-08 from the PDF text). The designation itself is (h)(2), phrased as a duty to inform the patient of the right 'to receive the visitors whom he or she designates, including, but not limited to, a spouse, a domestic partner (including a same-sex domestic partner), another family member, or a friend' (hv-fr-2010-final-rule, opened by the worklist; council 2026-11-08 corrected the pin: (h)(2) grounds the designation, (h)(4) the duty). Enforced through the Medicare Conditions of Participation by state survey agencies under Transmittal 75 (A-0215 to A-0217), hence sanctioner state and or_else R11. (h)(3), which bars restriction on race, sex, sexual orientation and the other listed grounds, is not encoded: the entry has no protected-ground fluents. Also not encoded: the patient's consent and its withdrawal ((h)(2)), the support person and incapacitated patients (A-0216), and the breadth of (h)(4) beyond designated visitors. The 'not visiting' conjunct makes the obligation fire once (one action slot per step).

- `hv-cfr-482-13-h` ((h)(4); US; date 2011-01-18): **snippet** 2026-11-08: "Ensure that all visitors enjoy full and equal visitation privileges consistent with patient preferences" <https://www.law.cornell.edu/cfr/text/42/482.13>
- `hv-cms-r75soma` (A-0217; US; date 2011-12-02): **opened** 2026-11-08: "it is not permissible for the hospital, on its own, to differentiate among visitors without any clinically necessary or reasonable basis" <https://www.cms.gov/regulations-and-guidance/guidance/transmittals/downloads/r75soma.pdf>
- `hv-fr-2010-final-rule` (42 CFR 482.13(h)(2), as added (the designation right); US; date 2011-01-18): **snippet** 2026-11-08: "to receive the visitors whom he or she designates, including, but not limited to, a spouse, a domestic partner (including a same-sex domestic partner), another family member, or a friend" <https://www.govinfo.gov/content/pkg/FR-2010-11-19/html/2010-29194.htm>

<a id="src-r10"></a>
**R10**: 42 CFR 482.13(h)(1)-(2), added by 75 FR 70831 (hv-fr-2010-final-rule, opened by the worklist): the hospital informs the patient of the right 'to receive the visitors whom he or she designates'; for critical access hospitals 485.635(f)(1) adds 'in advance of furnishing patient care whenever possible', so designation may precede admission (condition true). Written as a power conferred by the rule (may), not a default capacity: before 2011 no such designation existed.

- `hv-fr-2010-final-rule` (42 CFR 482.13(h)(1)-(2); 485.635(f)(1), as added; US; date 2011-01-18): **snippet** 2026-11-08: "to receive the visitors whom he or she designates ... in advance of furnishing patient care whenever possible" <https://www.govinfo.gov/content/pkg/FR-2010-11-19/html/2010-29194.htm>

<a id="src-r11"></a>
**R11**: CMS Transmittal 75, Pub. 100-07, 2011-12-02 (hv-cms-r75soma, opened by the worklist and by the encoder 2026-11-08): interpretive guidelines A-0215 to A-0217 give state surveyors the standard for 482.13(h); a deficiency is cited against the hospital's Medicare participation; A-0215: 'the burden of proof is upon the hospital to demonstrate that the visitation restriction is reasonably necessary to provide safe care'. The consequence is CMS's, not the surveyor's: 'noncompliance with this provision could result in the provider's termination from the Medicare program' (hv-fr-2010-final-rule, Part II, opened 2026-11-08); termination is not encoded, cite has no effects, and the two-step path (state agency cites, CMS terminates) is collapsed into one surveyor role.

- `hv-cms-r75soma` (A-0215; US; date 2011-12-02): **opened** 2026-11-08: "the burden of proof is upon the hospital to demonstrate that the visitation restriction is reasonably necessary to provide safe care" <https://www.cms.gov/regulations-and-guidance/guidance/transmittals/downloads/r75soma.pdf>
- `hv-fr-2010-final-rule` (Part II, response to comments (enforcement); US; date 2011-01-18): **snippet** 2026-11-08: "noncompliance with this provision could result in the provider's termination from the Medicare program" <https://www.govinfo.gov/content/pkg/FR-2010-11-19/html/2010-29194.htm>


## Expected properties

| property | kind | expected | meaning |
|---|---|---|---|
| spouse_visit_guaranteed | structure | holds_to_k | An admitted patient's spouse is admitted as a visitor within two steps of admission-and-marriage both holding, provided visiting was not clinically restricted at those steps (the two grace steps let a must-recognise rule and then a must-admit rule fire, one action per step). Written for the hospital-visitation pair and the coverture composite (plans/informal-rules.md slice 1, preregistered 2026-11-08). holds_to_k where a formal gate recognises the spouse as family and a duty admits family; violated when the only route is staff discretion or an unforced designation. Reads whether the spouse's visit is guaranteed, as opposed to possible. |
| spouse_visit_possible | structure | reachable | Some compliant trace reaches a step where an admitted patient's spouse has been admitted as a visitor. Reachable in both sides of the hospital-visitation pair and in the composite; read with spouse_visit_guaranteed: guaranteed lost while possible kept is the displaced verdict (plans/informal-rules.md D3), both lost is no backstop found. |
| unmarried_partner_visit_possible | structure | reachable | Some compliant trace reaches a step where an admitted patient's unmarried partner has been admitted as a visitor. Before 2011 only through staff discretion (the informal gate: R2 recognises, R8 then admits) or with the staff norm R3 gone; after 2011 also through the patient's designation (R10, R9). unreachable_open when no route exists: the attribute set the formal spouse gate never covered. |
| designated_visit_guaranteed | structure | holds_to_k | A visitor the admitted patient has designated is admitted within one step, provided visiting was not clinically restricted at that step (42 CFR 482.13(h)(2), (h)(4)). Not applicable before 2011 (no designated fluent); holds_to_k after. The differs_on property of the hospital-visitation pair. |

## Pairs

Extends [hospital-visitation-pre2011](hospital-visitation-pre2011.md); one line per change:
- R3 replaced: was "(practice, not written; reconstruction, no policy text found) Staff must not admit as a visitor anyone they do not count as family, or else the hospital may reprimand them (R6)." now "(practice, not written; overridden where the patient has designated the visitor) Staff must not admit as a visitor anyone they do not count as family and whom the patient has not designated, or else the hospital may reprimand them (R6)."
- R9 added: Staff must admit a visitor the patient has designated when the patient is admitted, visiting is not restricted and the visitor is not already visiting, or else the state survey agency may cite the hospital (R11) (42 CFR 482.13(h)(4), read with Transmittal 75 A-0217; the designation right is (h)(2)).
- R10 added: The patient may designate any person as a visitor (42 CFR 482.13(h)(1)-(2)).
- R11 added: The state survey agency may cite the hospital (the sanction behind R9; a deficiency under the Medicare Conditions of Participation, which CMS may follow with termination from Medicare).
- adds role surveyor (the state survey agency acting for CMS; enforces the Conditions of Participation)
- adds fluent designated (p has designated x as a visitor (482.13(h)(2)))
- adds action designate (does: designated(p, x) := true)
- adds action cite (does: )
- overrides expected_properties
- overrides minimal_pair_of
- overrides notes
Minimal pair of [hospital-visitation-pre2011](hospital-visitation-pre2011.md), differing in rule R9; the pair differs on property designated_visit_guaranteed.

<details><summary>Encoder notes (engine internals)</summary>

The after-2011 side of the pair (plans/informal-rules.md R1; preregistered there 2026-11-08 before the first run). Not a one-rule pair: the diff is R9, R10, R11, the designate and cite actions, the designated fluent and the narrowing of R3; R4 and R8 are kept on both sides, which matches the sources (the 2011 rule added designation and did not remove the family gate), and designated_visit_guaranteed is not applicable to the base, so the pair's differs_on shows a new property rather than a flipped one (council 2026-11-08). Diff from the base: the patient gains designate (R10) and staff a state-sanctioned admission duty on designation (R9, or_else R11, sanctioner state via the surveyor role); the staff norm R3 is narrowed by (not (designated p x)), the one way strict compliance can express 'overridden, not deleted' (ASSUMED). The formal policy gate R4 and the family-admission duty R8 stay, so the spouse is guaranteed admission by R4 + R8 and, if the patient designates, also by R9. Predictions (function): deleting R4 (sorts_who_belongs) flips spouse_visit_guaranteed to violated, because designation is a may (R10) and is not forced, while spouse_visit_possible stays reachable by two routes (R2 then R8; R10 then R9); deleting R9 (settles_who_decides) flips designated_visit_guaranteed to violated and nothing else (R5 still permits, so admission stays possible); deleting R2 leaves unmarried_partner_visit_possible reachable (displaced to designation), unlike the base where it goes unreachable; deleting R8 flips spouse_visit_guaranteed to violated (not forced; possible stays). designated_visit_guaranteed is the differs_on property of the pair: not applicable to the base (no designated fluent), holds_to_k here. (h)(3) protected grounds not encoded; consent and its withdrawal, the support person and incapacitated patients ((h)(2), A-0216) not encoded; the Medicare termination consequence not encoded (cite has no effects); the 2012 and 2019 amendments to (h) not read. Consent guard note (plans/consent-guard-note-DRAFT.md) ruled not applicable to visitor-access rules by the author, 2026-11-08.

</details>
