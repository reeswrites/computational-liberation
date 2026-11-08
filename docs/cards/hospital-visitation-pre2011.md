# hospital-visitation-pre2011

**US hospital visitation before 2011: policy admits immediate family, staff decide who counts (minimal pair base)**

> Before the 2011 Medicare rule there was no federal visitor-choice standard. The Presidential Memorandum of 2010-04-15 describes the baseline it set out to change as visitation 'no more restrictive than those that immediate family members enjoy' and the final rule's preamble says 'the current practice in some medical institutions ... denies patients access to their loved ones' (75 FR 70831). Both are regulators' descriptions; no pre-2011 hospital policy text was opened (plans/sourcing-worklist-marriage.md). Encoded as a formal policy gate (R4: the spouse must be recognised as family; R8: family are admitted) over an informal staff gate (R2: staff decide who else counts; R3: staff may not admit anyone they do not count), a general permission to admit visitors (R5) that R3 narrows, and the clinical-restriction exception (R7) that the 2011 rule kept.

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

## Rules

| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | level | source |
|---|---|---|---|---|---|---|---|---|---|
| R1 | staff | may | `(admit s p)` | `(not (admitted p))` | none | untagged (null) | Staff may admit a patient who is not already admitted. | unverified | Encoder's device: admission is the event that makes visitation a question; no source read for it. UNVERIFIED (general knowledge; no source opened). |
| R2 | staff | may (implicit) | `(recognize_family s p x)` | `(and (admitted p) (not (counts_as_family p x)))` | none | tying | (practice, not written) Staff may treat any visitor as family of an admitted patient: the charge nurse decides who counts. | unverified | [full source under Sources, R2](#src-r2) |
| R3 | staff | must not (implicit) | `(admit_visitor s x p)` | `(not (counts_as_family p x))` | R6 `(reprimand o s)` | tying | (practice, not written) Staff must not admit as a visitor anyone they do not count as family, or else the hospital may reprimand them (R6). | opened | [full source under Sources, R3](#src-r3) |
| R4 | staff | must | `(recognize_family s p x)` | `(and (admitted p) (married p x) (not (counts_as_family p x)))` | R6 `(reprimand o s)` | tying | Staff must recognise an admitted patient's spouse as family (hospital policy admits immediate family), or else the hospital may reprimand them (R6). | opened | [full source under Sources, R4](#src-r4) |
| R5 | staff | may | `(admit_visitor s x p)` | `(and (admitted p) (not (clinically_restricted p)))` | none | superadditive | Staff may admit any visitor to an admitted patient when visiting is not clinically restricted (the general permission that the staff norm R3 narrows). | opened | [full source under Sources, R5](#src-r5) |
| R6 | hospital | may | `(reprimand o s)` | `true` | none | untagged (null) | The hospital may reprimand staff (the sanction behind R3 and R4). | unverified | Encoder's sanction holder for the hospital's own policy (R4) and the staff norm (R3): employer discipline. No disciplinary text found. UNVERIFIED (general knowledge; no source opened). |
| R7 | staff | may | `(restrict s p)` | `(admitted p)` | none | untagged (null) | Staff may restrict visiting to an admitted patient on clinical grounds. | opened | [full source under Sources, R7](#src-r7) |
| R8 | staff | must | `(admit_visitor s x p)` | `(and (admitted p) (counts_as_family p x) (not (clinically_restricted p)) (not (visiting x p)))` | R6 `(reprimand o s)` | superadditive | Staff must admit a visitor they count as family of an admitted patient when visiting is not clinically restricted and the visitor is not already admitted, or else the hospital may reprimand them (R6). | opened | [full source under Sources, R8](#src-r8) |

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
**R3**: The sanctioned side of the informal gate: a visitor staff do not count as family is not admitted, and staff who admit one answer to the hospital. Same evidence base as R2 (the Presidential Memorandum's 'no more restrictive than those that immediate family members enjoy' baseline and the final rule's 'denies patients access to their loved ones', both opened by the worklist); that the hospital disciplined staff who admitted non-family is the encoder's inference from the existence of a policy (ASSUMED, no disciplinary text found).

- `hv-presmemo-2010` (para. 1; US; date 2010-04-15): **opened** 2026-11-08: "no more restrictive than those that immediate family members enjoy"
- `hv-fr-2010-final-rule` (preamble (Background); US; date 2011-01-18): **opened** 2026-11-08: "denies patients access to their loved ones"

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


## Expected properties

| property | kind | expected | meaning |
|---|---|---|---|
| spouse_visit_guaranteed | structure | holds_to_k | An admitted patient's spouse is admitted as a visitor within two steps of admission-and-marriage both holding, provided visiting was not clinically restricted at those steps (the two grace steps let a must-recognise rule and then a must-admit rule fire, one action per step). Written for the hospital-visitation pair and the coverture composite (plans/informal-rules.md slice 1, preregistered 2026-11-08). holds_to_k where a formal gate recognises the spouse as family and a duty admits family; violated when the only route is staff discretion or an unforced designation. Reads whether the spouse's visit is guaranteed, as opposed to possible. |
| spouse_visit_possible | structure | reachable | Some compliant trace reaches a step where an admitted patient's spouse has been admitted as a visitor. Reachable in both sides of the hospital-visitation pair and in the composite; read with spouse_visit_guaranteed: guaranteed lost while possible kept is the displaced verdict (plans/informal-rules.md D3), both lost is no backstop found. |
| unmarried_partner_visit_possible | structure | reachable | Some compliant trace reaches a step where an admitted patient's unmarried partner has been admitted as a visitor. Before 2011 only through staff discretion (the informal gate: R2 recognises, R8 then admits) or with the staff norm R3 gone; after 2011 also through the patient's designation (R10, R9). unreachable_open when no route exists: the attribute set the formal spouse gate never covered. |

## Pairs

Extended by: [hospital-visitation](hospital-visitation.md)
[hospital-visitation](hospital-visitation.md) is a minimal pair of this entry (rule ?).

<details><summary>Encoder notes (engine internals)</summary>

Base of the hospital-visitation minimal pair (plans/informal-rules.md R1; preregistered there 2026-11-08 before the first run). Vocabulary follows plans/sourcing-worklist-marriage.md section 4 with these changes: the hospital is split into staff (who decide and admit) and hospital (who sanction), so the institution sanction has a holder; the kin role is dropped (one visitor role, married exogenous, so the same role is the spouse in some traces and the unmarried partner in others); deny_visitor is dropped (non-admission is the default); can_visit as a derived power is dropped, because the engine's (enabled ...) ignores a sanctioned must_not (only an or_else-null disability blocks enablement, rules_lower.py), so a power fluent could not see the staff norm; the properties read the admission itself (visiting) on compliant traces, where every must_not binds under strict compliance. married has no setter here, so it is exogenous and free; in the coverture composite marry sets it. Engine facts the encoding leans on: a regulated action (one some may/must names) fires only at a step where some may/must condition on that instance holds, so R5 is what lets any visitor through and R3 is what stops non-family; one action per step (step-mode one), so a must-do that fires takes the step; a trace where two different must-do instances fire at one step is not compliant and is excluded, not counted. spouse_visit_guaranteed therefore has two grace steps (R4 recognises at t0, R8 admits at t1, visiting holds at t2). The formal gate is R4 (function: sorts_who_belongs; prediction: deleting it flips spouse_visit_guaranteed to violated while spouse_visit_possible stays reachable via R2). The informal gate is R2 + R3 (function: sorts_who_belongs; predictions: deleting R2 flips unmarried_partner_visit_possible to unreachable_open, since no other rule lets a non-spouse count; deleting R3 keeps it reachable and makes it reachable without recognition, since R5 permits any visitor). Deleting R8 flips spouse_visit_guaranteed to violated (admission no longer forced) and nothing else; deleting R5 flips nothing (R8 is also a permission). ASSUMED: the split roles, the family-admission duty (R8) and R4 as an action obligation; the card-only seat judges them. Consent guard note (plans/consent-guard-note-DRAFT.md) ruled not applicable to visitor-access rules by the author, 2026-11-08.

</details>
