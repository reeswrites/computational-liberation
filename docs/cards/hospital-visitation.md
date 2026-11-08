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

## Roles

- **patient**: the admitted patient whose visitors are at issue
- **partner**: the would-be visitor; a spouse or an unmarried partner, depending on the trace (married is exogenous here)
- **staff**: the charge nurse or unit staff who decide who counts as family and admit visitors
- **hospital**: the hospital as an institution (administration); sets visitation policy and disciplines staff
- **surveyor**: the state survey agency acting for CMS; enforces the Conditions of Participation

## Rules

| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | level | source |
|---|---|---|---|---|---|---|---|---|---|
| R1 | staff | may | `(admit s p)` | `(not (admitted p))` | none | untagged (null) | Staff may admit a patient who is not already admitted. | unverified | Encoder's device: admission is the event that makes visitation a question; no source read for it. UNVERIFIED (general knowledge; no source opened). |
| R2 | staff | may (implicit) | `(recognize_family s p x)` | `(and (admitted p) (not (counts_as_family p x)))` | none | tying | (practice, not written) Staff may treat any visitor as family of an admitted patient: the charge nurse decides who counts. | unverified | [full source under Sources, R2](#src-r2) |
| R3 (replaced) | staff | must not (implicit) | `(admit_visitor s x p)` | `(and (not (counts_as_family p x)) (not (designated p x)))` | R6 `(reprimand o s)` | tying | (practice, not written; overridden where the patient has designated the visitor) Staff must not admit as a visitor anyone they do not count as family and whom the patient has not designated, or else the hospital may reprimand them (R6). | opened | [full source under Sources, R3](#src-r3) |
| R4 | staff | must | `(recognize_family s p x)` | `(and (admitted p) (married p x) (not (counts_as_family p x)))` | R6 `(reprimand o s)` | tying | Staff must recognise an admitted patient's spouse as family (hospital policy admits immediate family), or else the hospital may reprimand them (R6). | opened | [full source under Sources, R4](#src-r4) |
| R5 | staff | may | `(admit_visitor s x p)` | `(and (admitted p) (not (clinically_restricted p)))` | none | superadditive | Staff may admit any visitor to an admitted patient when visiting is not clinically restricted (the general permission that the staff norm R3 narrows). | opened | [full source under Sources, R5](#src-r5) |
| R6 | hospital | may | `(reprimand o s)` | `true` | none | untagged (null) | The hospital may reprimand staff (the sanction behind R3 and R4). | unverified | Encoder's sanction holder for the hospital's own policy (R4) and the staff norm (R3): employer discipline. No disciplinary text found. UNVERIFIED (general knowledge; no source opened). |
| R7 | staff | may | `(restrict s p)` | `(admitted p)` | none | untagged (null) | Staff may restrict visiting to an admitted patient on clinical grounds. | opened | [full source under Sources, R7](#src-r7) |
| R8 | staff | must | `(admit_visitor s x p)` | `(and (admitted p) (counts_as_family p x) (not (clinically_restricted p)) (not (visiting x p)))` | R6 `(reprimand o s)` | superadditive | Staff must admit a visitor they count as family of an admitted patient when visiting is not clinically restricted and the visitor is not already admitted, or else the hospital may reprimand them (R6). | opened | [full source under Sources, R8](#src-r8) |
| R9 (added) | staff | must | `(admit_visitor s x p)` | `(and (admitted p) (designated p x) (not (clinically_restricted p)) (not (visiting x p)))` | R11 `(cite v o)` | tying | Staff must admit a visitor the patient has designated when the patient is admitted, visiting is not clinically restricted and the visitor is not already admitted, or else the state survey agency may cite the hospital (R11) (42 CFR 482.13(h)(2), (h)(4)). | snippet | [full source under Sources, R9](#src-r9) |
| R10 (added) | patient | may | `(designate p x)` | `true` | none | tying | The patient may designate any person as a visitor (42 CFR 482.13(h)(1)-(2)). | opened | [full source under Sources, R10](#src-r10) |
| R11 (added) | surveyor | may | `(cite v o)` | `true` | none | untagged (null) | The state survey agency may cite the hospital (the sanction behind R9; CMS Transmittal 75). | opened | [full source under Sources, R11](#src-r11) |

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
**R2**: The informal gate. No hospital policy text was found that names the decider; the rule rests on the regulators' description of practice: the Presidential Memorandum of 2010-04-15 describes the baseline as visitation privileges 'no more restrictive than those that immediate family members enjoy' (hv-presmemo-2010, opened by the worklist), and the 2010 final rule's preamble says 'the current practice in some medical institutions ... denies patients access to their loved ones' (hv-fr-2010-final-rule, opened by the worklist). That staff exercised discretion over who counted as family is the encoder's reading of those descriptions (ASSUMED); Lambda Legal's 2010 survey (hv-ll-2010-wcnc) could not be opened. A permission carries no sanction of its own; the sanction that bounds the discretion is R3's (sanctioner institution), which is why this norm's own sanctioner is none.

- `hv-presmemo-2010` (para. 1; US; date 2010-04-15): **opened** 2026-11-08: "no more restrictive than those that immediate family members enjoy"
- `hv-fr-2010-final-rule` (preamble (Background); US; date 2011-01-18): **opened** 2026-11-08: "the current practice in some medical institutions ... denies patients access to their loved ones"
- `hv-ll-2010-wcnc` (US; date n/a): **unverified**

<a id="src-r3"></a>
**R3**: The pre-2011 staff norm (hospital-visitation-pre2011 R3), retained. The 2011 rule does not delete it; it overrides it where the patient has designated the visitor, which strict compliance can only express as a narrowing of the norm's condition (ASSUMED encoding of 'overrides but does not delete'; a norm kept at full width would contradict R9 and leave no compliant trace). That the norm persisted is anecdotal: a registered domestic partner was denied access at a Las Vegas hospital in 2012, 'It didn't matter that we were registered domestic partners' (hv-nv-2012, opened by the worklist); no rate exists (no compliance study found, plans/informal-rules.md R1). Baseline evidence as before: 'no more restrictive than those that immediate family members enjoy' (hv-presmemo-2010).

- `hv-nv-2012` (US-NV; date 2012-08-21): **opened** 2026-11-08: "It didn't matter that we were registered domestic partners"
- `hv-presmemo-2010` (para. 1; US; date 2010-04-15): **opened** 2026-11-08: "no more restrictive than those that immediate family members enjoy"

<a id="src-r4"></a>
**R4**: The formal gate before 2011: hospital policy, not law. No pre-2011 hospital policy text or state hospital association model policy with 'immediate family' wording was found or opened (plans/sourcing-worklist-marriage.md, hv-pre2011-practice); the rule rests on the Presidential Memorandum's description of the baseline, 'no more restrictive than those that immediate family members enjoy' (hv-presmemo-2010, opened by the worklist). Immediate family other than the spouse (parents, children, siblings) is not encoded: the entry has one visitor role and the composite's question is the spouse. Written as an action obligation (must recognise) rather than a state obligation because no action can establish counts_as_family for the spouse at admission (ADR 0009 note).

- `hv-presmemo-2010` (para. 1; US; date 2010-04-15): **opened** 2026-11-08: "no more restrictive than those that immediate family members enjoy"

<a id="src-r5"></a>
**R5**: The general permission the staff norm narrows (R3 bars non-family; R8 obliges family). Clinical restriction as the standing exception is what the 2011 rule kept (hv-fr-2010-final-rule, opened by the worklist: the rule allows 'clinically necessary or reasonable restriction' in 482.13(h) intro); before 2011 it is the encoder's reconstruction of ordinary practice. UNVERIFIED for the pre-2011 permission itself.

- `hv-fr-2010-final-rule` (42 CFR 482.13(h) introductory text, as added; US; date 2011-01-18): **opened** 2026-11-08: "clinically necessary or reasonable restriction"

**R6**

- no work named: **unverified** (rationale: a hospital policy is enforced by the hospital on its staff)

<a id="src-r7"></a>
**R7**: The clinical-restriction exception, unchanged across the pair. After 2011 it is in 42 CFR 482.13(h): 'clinically necessary or reasonable restriction' (hv-fr-2010-final-rule, opened by the worklist); CMS Transmittal 75 puts 'the burden of proof is upon the hospital to demonstrate that the visitation restriction is reasonably necessary to provide safe care' (hv-cms-r75soma, opened by the worklist). Before 2011 the same clinical judgment existed without the burden of proof; the burden is not encoded (no rule reads it). Clinical grounds are not modelled; restrict is a free staff act, which over-reads staff power (recorded).

- `hv-fr-2010-final-rule` (42 CFR 482.13(h) introductory text, as added; US; date 2011-01-18): **opened** 2026-11-08: "clinically necessary or reasonable restriction"
- `hv-cms-r75soma` (A-0215; US; date 2011-12-02): **opened** 2026-11-08: "the burden of proof is upon the hospital to demonstrate that the visitation restriction is reasonably necessary to provide safe care"

<a id="src-r8"></a>
**R8**: Hospital policy before 2011: immediate family are admitted. No policy text was opened; the duty is read from the Presidential Memorandum's description of the baseline, visitation 'no more restrictive than those that immediate family members enjoy' (hv-presmemo-2010, opened by the worklist), which presupposes that family were admitted as of course. Written as a duty (must), not a permission, so that the spouse's visit is guaranteed and not merely possible; whether hospitals treated family admission as obligatory on themselves is the encoder's reading (ASSUMED). The 'not visiting' conjunct makes the duty fire once (one action slot per step).

- `hv-presmemo-2010` (para. 1; US; date 2010-04-15): **opened** 2026-11-08: "no more restrictive than those that immediate family members enjoy"

<a id="src-r9"></a>
**R9**: 42 CFR 482.13(h), added by 75 FR 70831 (2010-11-19), effective 2011-01-18 (hv-fr-2010-final-rule, opened by the worklist): the patient has 'the right, subject to his or her consent, to receive the visitors whom he or she designates, including, but not limited to, a spouse, a domestic partner (including a same-sex domestic partner), another family member, or a friend' ((h)(2)), and the hospital must 'Ensure that all visitors enjoy full and equal visitation privileges consistent with patient preferences' ((h)(4)) (hv-cfr-482-13-h, current text, opened by the worklist). Enforced through the Medicare Conditions of Participation by state survey agencies under CMS Transmittal 75 (hv-cms-r75soma, A-0215, opened by the worklist), hence sanctioner state and or_else R11. (h)(3), which bars restriction on race, sex, sexual orientation and the other listed grounds, is not encoded: the entry has no protected-ground fluents; the relationship-agnostic effect here comes from (h)(2) and (h)(4). The 'not visiting' conjunct makes the obligation fire once (one action slot per step).

- `hv-fr-2010-final-rule` (42 CFR 482.13(h)(2), (h)(4), as added; US; date 2011-01-18): **opened** 2026-11-08: "to receive the visitors whom he or she designates, including, but not limited to, a spouse, a domestic partner (including a same-sex domestic partner), another family member, or a friend"
- `hv-cfr-482-13-h` ((h)(2)-(4); US; date 2011-01-18): **opened** 2026-11-08: "Ensure that all visitors enjoy full and equal visitation privileges consistent with patient preferences"
- `hv-cms-r75soma` (A-0215; US; date 2011-12-02): **snippet** 2026-11-08

<a id="src-r10"></a>
**R10**: 42 CFR 482.13(h)(1)-(2), added by 75 FR 70831 (hv-fr-2010-final-rule, opened by the worklist): the hospital informs the patient of the right 'to receive the visitors whom he or she designates'; for critical access hospitals 485.635(f)(1) adds 'in advance of furnishing patient care whenever possible', so designation may precede admission (condition true). Written as a power conferred by the rule (may), not a default capacity: before 2011 no such designation existed.

- `hv-fr-2010-final-rule` (42 CFR 482.13(h)(1)-(2); 485.635(f)(1), as added; US; date 2011-01-18): **opened** 2026-11-08: "to receive the visitors whom he or she designates ... in advance of furnishing patient care whenever possible"

<a id="src-r11"></a>
**R11**: CMS Transmittal 75, Pub. 100-07, 2011-12-02 (hv-cms-r75soma, opened by the worklist): interpretive guidelines A-0215 to A-0217 give state surveyors the standard for 482.13(h); a deficiency is cited against the hospital's Medicare participation. The consequence (termination from Medicare) is not encoded; cite has no effects. 'the burden of proof is upon the hospital to demonstrate that the visitation restriction is reasonably necessary to provide safe care' is the one quoted line.

- `hv-cms-r75soma` (A-0215; US; date 2011-12-02): **opened** 2026-11-08: "the burden of proof is upon the hospital to demonstrate that the visitation restriction is reasonably necessary to provide safe care"


## Expected properties

| property | kind | expected | meaning |
|---|---|---|---|
| spouse_visit_guaranteed | structure | holds_to_k | An admitted patient's spouse is admitted as a visitor within two steps of admission-and-marriage both holding, provided visiting was not clinically restricted at those steps (the two grace steps let a must-recognise rule and then a must-admit rule fire, one action per step). Written for the hospital-visitation pair and the coverture composite (plans/informal-rules.md slice 1, preregistered 2026-11-08). holds_to_k where a formal gate recognises the spouse as family and a duty admits family; violated when the only route is staff discretion or an unforced designation. Reads whether the spouse's visit is guaranteed, as opposed to possible. |
| spouse_visit_possible | structure | reachable | Some compliant trace reaches a step where an admitted patient's spouse has been admitted as a visitor. Reachable in both sides of the hospital-visitation pair and in the composite; read with spouse_visit_guaranteed: guaranteed lost while possible kept is the displaced verdict (plans/informal-rules.md D3), both lost is no backstop found. |
| unmarried_partner_visit_possible | structure | reachable | Some compliant trace reaches a step where an admitted patient's unmarried partner has been admitted as a visitor. Before 2011 only through staff discretion (the informal gate: R2 recognises, R8 then admits) or with the staff norm R3 gone; after 2011 also through the patient's designation (R10, R9). unreachable_open when no route exists: the attribute set the formal spouse gate never covered. |
| designated_visit_guaranteed | structure | holds_to_k | A visitor the admitted patient has designated is admitted within one step, provided visiting was not clinically restricted at that step (42 CFR 482.13(h)(2), (h)(4)). Not applicable before 2011 (no designated fluent); holds_to_k after. The differs_on property of the hospital-visitation pair. |

## Pairs

Extends [hospital-visitation-pre2011](hospital-visitation-pre2011.md); one line per change:
- R3 replaced: was "(practice, not written) Staff must not admit as a visitor anyone they do not count as family, or else the hospital may reprimand them (R6)." now "(practice, not written; overridden where the patient has designated the visitor) Staff must not admit as a visitor anyone they do not count as family and whom the patient has not designated, or else the hospital may reprimand them (R6)."
- R9 added: Staff must admit a visitor the patient has designated when the patient is admitted, visiting is not clinically restricted and the visitor is not already admitted, or else the state survey agency may cite the hospital (R11) (42 CFR 482.13(h)(2), (h)(4)).
- R10 added: The patient may designate any person as a visitor (42 CFR 482.13(h)(1)-(2)).
- R11 added: The state survey agency may cite the hospital (the sanction behind R9; CMS Transmittal 75).
- adds role surveyor (the state survey agency acting for CMS; enforces the Conditions of Participation)
- adds fluent designated (p has designated x as a visitor (482.13(h)(2)))
- adds action designate (does: designated(p, x) := true)
- adds action cite (does: )
- overrides expected_properties
- overrides minimal_pair_of
- overrides notes
Minimal pair of [hospital-visitation-pre2011](hospital-visitation-pre2011.md), differing in rule ?; the pair differs on property designated_visit_guaranteed.

<details><summary>Encoder notes (engine internals)</summary>

The after-2011 side of the pair (plans/informal-rules.md R1; preregistered there 2026-11-08 before the first run). Diff from the base: the patient gains designate (R10) and staff a state-sanctioned admission duty on designation (R9, or_else R11, sanctioner state via the surveyor role); the staff norm R3 is narrowed by (not (designated p x)), the one way strict compliance can express 'overridden, not deleted' (ASSUMED). The formal policy gate R4 and the family-admission duty R8 stay, so the spouse is guaranteed admission by R4 + R8 and, if the patient designates, also by R9. Predictions (function): deleting R4 (sorts_who_belongs) flips spouse_visit_guaranteed to violated, because designation is a may (R10) and is not forced, while spouse_visit_possible stays reachable by two routes (R2 then R8; R10 then R9); deleting R9 (settles_who_decides) flips designated_visit_guaranteed to violated and nothing else (R5 still permits, so admission stays possible); deleting R2 leaves unmarried_partner_visit_possible reachable (displaced to designation), unlike the base where it goes unreachable; deleting R8 flips spouse_visit_guaranteed to violated (not forced; possible stays). designated_visit_guaranteed is the differs_on property of the pair: not applicable to the base (no designated fluent), holds_to_k here. (h)(3) protected grounds not encoded; the Medicare termination consequence not encoded (cite has no effects); the 2012 and 2019 amendments to (h) not read. Consent guard note (plans/consent-guard-note-DRAFT.md) ruled not applicable to visitor-access rules by the author, 2026-11-08.

</details>
