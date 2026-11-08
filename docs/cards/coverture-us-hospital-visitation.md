# coverture-us-hospital-visitation

**Composite: coverture household (US) + hospital visitation after 2011, the husband as patient and the wife as visitor**

> composite of: coverture-household-us, hospital-visitation

## Legend

- **may / must / must not**: the rule permits / requires / forbids the aim for the person in the "who" cell, when the "when" cell holds.
- **(disability)**: a `must not` with no sanction (or else = none). The power does not exist; this is not a norm someone enforces.
- **(implicit)**: a practice no text states, tagged by the encoder; the source cell gives its rationale, not a quotation.
- **or else**: the sanction rule that applies on breach (the rule id and its aim).
- **strand**: `rival` = an input only one party can supply at a time; `superadditive` = a good that exists only as a product of the bundle; `tying` = glued to the bundle by law, wages or norm with no production link.
- **default capacity**: an action a person of that kind can do unless an express disability removes it, as opposed to a power that exists only because a rule grants it.
- **k**: the step bound; verdicts such as `holds_to_k` mean "holds for every trace of at most k steps".
- **Variables**: letters in the aim and when cells are bound to roles in the Variables section; "unbound (encoder to fix)" means no binding was recorded.

## Members

A composite (ADR 0018): the members' roles are unioned after the aliases below, fluents unified by name, rules concatenated under `<member>__` prefixes. Each rule row below is the member's rule, unchanged except for the renamed roles; its plain line and sources are the member's.

- [coverture-household-us](coverture-household-us.md): husband → partner_a, wife → partner_b
- [hospital-visitation](hospital-visitation.md): patient → partner_a, partner → partner_b

Initial literals: `female(partner_b)` (init mode `declared`; fluents not listed start false)

Free at t=0: `acquired_property`, `earns`

## Roles

- **partner_a**: the husband; the legal person the marriage keeps
- **partner_b**: the feme covert; her legal existence is suspended during marriage
- **staff**: the charge nurse or unit staff who decide who counts as family and admit visitors
- **hospital**: the hospital as an institution (administration); sets visitation policy and disciplines staff
- **surveyor**: the state survey agency acting for CMS; enforces the Conditions of Participation

## Rules

| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | level | source |
|---|---|---|---|---|---|---|---|---|---|
| coverture_household_us__R1 | partner_a | may (sanctioner derived, unreviewed) | `(control_property h w)` | `(married h w)` | none | tying | The husband may control his wife's property when they are married (Blackstone II.29). | opened | [full source under Sources, coverture_household_us__R1](#src-coverture_household_us__r1) https://avalon.law.yale.edu/18th_century/blackstone_bk2ch29.asp: |
| coverture_household_us__R2 | partner_a | must (sanctioner derived, unreviewed) | `(provides_care h w)` | `(married h w)` | none | superadditive | The husband providing care to his wife must hold when they are married; no sanction is attached (Blackstone I.15). | opened | [full source under Sources, coverture_household_us__R2](#src-coverture_household_us__r2) https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ |
| coverture_household_us__R3 | partner_b | must (implicit) (sanctioner derived, unreviewed) | `(provides_care w h)` | `(married h w)` | coverture_household_us__R5 `(chastise h w)` | superadditive | (practice, not written) The wife providing care to her husband (household labour) must hold when they are married, or else the husband may chastise her (R5). | unverified | [full source under Sources, coverture_household_us__R3](#src-coverture_household_us__r3) |
| coverture_household_us__R4 | partner_b | must not (disability) (sanctioner derived, unreviewed) | `(sue w)` | `(married h w)` | none | tying | The wife cannot sue in her own name while married: no such power exists (Blackstone I.15). | opened | [full source under Sources, coverture_household_us__R4](#src-coverture_household_us__r4) https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ |
| coverture_household_us__R5 | partner_a | may (sanctioner derived, unreviewed) | `(chastise h w)` | `(and (married h w) (misbehaves w))` | none | rival | The husband may chastise his wife (restrain her liberty) when they are married and her conduct is gross misbehaviour (Blackstone I.15). | opened | [full source under Sources, coverture_household_us__R5](#src-coverture_household_us__r5) https://avalon.law.yale.edu/18th_century/blackstone_bk1ch15.asp: |
| coverture_household_us__R6 | partner_b | must not (disability) (sanctioner derived, unreviewed) | `(leave w)` | `(married h w)` | none | rival | The wife cannot leave the marriage at her own will while married: no such power exists (pre-reform divorce required the spouse's consent or proved fault, Stevenson & Wolfers; NY 1787 adultery only). | opened | [full source under Sources, coverture_household_us__R6](#src-coverture_household_us__r6) https://www.nber.org/system/files/working_papers/w10175/w10175.pdf |
| coverture_household_us__R7 | partner_b | must not (disability) (sanctioner derived, unreviewed) | `(contract w)` | `(married h w)` | none | tying | The wife cannot contract in her own name while married: no such power exists (Blackstone I.15). | opened | [full source under Sources, coverture_household_us__R7](#src-coverture_household_us__r7) https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ |
| hospital_visitation__R1 | staff | may | `(admit s p)` | `(not (admitted p))` | none | untagged (null) | Staff may admit a patient who is not already admitted. | unverified | Encoder's device: admission is the event that makes visitation a question; no source read for it. UNVERIFIED (general knowledge; no source opened). |
| hospital_visitation__R2 | staff | may (implicit) | `(recognize_family s p x)` | `(and (admitted p) (not (counts_as_family p x)))` | none | tying | (practice, not written) Staff may treat any visitor as family of an admitted patient: the charge nurse decides who counts. | unverified | [full source under Sources, hospital_visitation__R2](#src-hospital_visitation__r2) |
| hospital_visitation__R3 | staff | must not (implicit) | `(admit_visitor s x p)` | `(and (not (counts_as_family p x)) (not (designated p x)))` | hospital_visitation__R6 `(reprimand o s)` | tying | (practice, not written; overridden where the patient has designated the visitor) Staff must not admit as a visitor anyone they do not count as family and whom the patient has not designated, or else the hospital may reprimand them (R6). | opened | [full source under Sources, hospital_visitation__R3](#src-hospital_visitation__r3) |
| hospital_visitation__R4 | staff | must | `(recognize_family s p x)` | `(and (admitted p) (married p x) (not (counts_as_family p x)))` | hospital_visitation__R6 `(reprimand o s)` | tying | Staff must recognise an admitted patient's spouse as family (hospital policy admits immediate family), or else the hospital may reprimand them (R6). | opened | [full source under Sources, hospital_visitation__R4](#src-hospital_visitation__r4) |
| hospital_visitation__R5 | staff | may | `(admit_visitor s x p)` | `(and (admitted p) (not (clinically_restricted p)))` | none | superadditive | Staff may admit any visitor to an admitted patient when visiting is not clinically restricted (the general permission that the staff norm R3 narrows). | opened | [full source under Sources, hospital_visitation__R5](#src-hospital_visitation__r5) |
| hospital_visitation__R6 | hospital | may | `(reprimand o s)` | `true` | none | untagged (null) | The hospital may reprimand staff (the sanction behind R3 and R4). | unverified | Encoder's sanction holder for the hospital's own policy (R4) and the staff norm (R3): employer discipline. No disciplinary text found. UNVERIFIED (general knowledge; no source opened). |
| hospital_visitation__R7 | staff | may | `(restrict s p)` | `(admitted p)` | none | untagged (null) | Staff may restrict visiting to an admitted patient on clinical grounds. | opened | [full source under Sources, hospital_visitation__R7](#src-hospital_visitation__r7) |
| hospital_visitation__R8 | staff | must | `(admit_visitor s x p)` | `(and (admitted p) (counts_as_family p x) (not (clinically_restricted p)) (not (visiting x p)))` | hospital_visitation__R6 `(reprimand o s)` | superadditive | Staff must admit a visitor they count as family of an admitted patient when visiting is not clinically restricted and the visitor is not already admitted, or else the hospital may reprimand them (R6). | opened | [full source under Sources, hospital_visitation__R8](#src-hospital_visitation__r8) |
| hospital_visitation__R9 | staff | must | `(admit_visitor s x p)` | `(and (admitted p) (designated p x) (not (clinically_restricted p)) (not (visiting x p)))` | hospital_visitation__R11 `(cite v o)` | tying | Staff must admit a visitor the patient has designated when the patient is admitted, visiting is not clinically restricted and the visitor is not already admitted, or else the state survey agency may cite the hospital (R11) (42 CFR 482.13(h)(2), (h)(4)). | snippet | [full source under Sources, hospital_visitation__R9](#src-hospital_visitation__r9) |
| hospital_visitation__R10 | partner_a | may | `(designate p x)` | `true` | none | tying | The patient may designate any person as a visitor (42 CFR 482.13(h)(1)-(2)). | opened | [full source under Sources, hospital_visitation__R10](#src-hospital_visitation__r10) |
| hospital_visitation__R11 | surveyor | may | `(cite v o)` | `true` | none | untagged (null) | The state survey agency may cite the hospital (the sanction behind R9; CMS Transmittal 75). | opened | [full source under Sources, hospital_visitation__R11](#src-hospital_visitation__r11) |

**Default capacities** (an action a person of that kind can do unless an express disability removes it): leave, sue, contract

## Variables

- coverture_household_us__R1: `h` = partner_a (rule var_roles); `w` = partner_b (rule var_roles)
- coverture_household_us__R2: `h` = partner_a (rule var_roles); `w` = partner_b (rule var_roles)
- coverture_household_us__R3: `w` = partner_b (rule var_roles); `h` = partner_a (rule var_roles)
- coverture_household_us__R4: `w` = partner_b (rule var_roles); `h` = partner_a (rule var_roles)
- coverture_household_us__R5: `h` = partner_a (rule var_roles); `w` = partner_b (rule var_roles)
- coverture_household_us__R6: `w` = partner_b (rule var_roles); `h` = partner_a (rule var_roles)
- coverture_household_us__R7: `w` = partner_b (rule var_roles); `h` = partner_a (rule var_roles)
- hospital_visitation__R1: `s` = staff (rule var_roles); `p` = partner_a (rule var_roles)
- hospital_visitation__R2: `s` = staff (rule var_roles); `p` = partner_a (rule var_roles); `x` = partner_b (rule var_roles)
- hospital_visitation__R3: `s` = staff (rule var_roles); `x` = partner_b (rule var_roles); `p` = partner_a (rule var_roles)
- hospital_visitation__R4: `s` = staff (rule var_roles); `p` = partner_a (rule var_roles); `x` = partner_b (rule var_roles)
- hospital_visitation__R5: `s` = staff (rule var_roles); `x` = partner_b (rule var_roles); `p` = partner_a (rule var_roles)
- hospital_visitation__R6: `o` = hospital (rule var_roles); `s` = staff (rule var_roles)
- hospital_visitation__R7: `s` = staff (rule var_roles); `p` = partner_a (rule var_roles)
- hospital_visitation__R8: `s` = staff (rule var_roles); `x` = partner_b (rule var_roles); `p` = partner_a (rule var_roles)
- hospital_visitation__R9: `s` = staff (rule var_roles); `x` = partner_b (rule var_roles); `p` = partner_a (rule var_roles)
- hospital_visitation__R10: `p` = partner_a (rule var_roles); `x` = partner_b (rule var_roles)
- hospital_visitation__R11: `v` = surveyor (rule var_roles); `o` = hospital (rule var_roles)

## Sources

Per rule: the full source where the table cell is cut, then each provenance item (bibliography id in `data/sources/`, pin, jurisdiction, effective date, verification level with access date, excerpt). The `level` column is the weakest item; levels: opened > snippet > recalled > unverified.

<a id="src-coverture_household_us__r1"></a>
**coverture_household_us__R1**: Blackstone, Commentaries on the Laws of England, Book II ch. 29 'Of Title by Succession, Marriage, and Judgment' (1766), read 2026-11-04 at https://avalon.law.yale.edu/18th_century/blackstone_bk2ch29.asp: chattels 'which belonged formerly to the wife, are by act of law vested in the husband' and 'the husband hath therein an immediate and absolute property, devolved to him by the marriage' (long s modernised from the OCR). Re-sourced 2026-11-04: Book I ch. 15 (the earlier citation; https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/, the husband and wife are one person in law) says 'I speak not at present of the rights of property' and so did not support this rule.

- `blackstone-1766-bk2-ch29` (Bk II ch 29; England; date n/a): **opened** 2026-11-04: "which belonged formerly to the wife, are by act of law vested in the husband ... the husband hath therein an immediate and absolute property, devolved to him by the marriage"

<a id="src-coverture_household_us__r2"></a>
**coverture_household_us__R2**: Blackstone, Commentaries on the Laws of England, Book I ch. 15 'Of Husband and Wife' (1765); https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ (the husband is bound to provide his wife with necessaries). [ADR 0009: converted from an action obligation to a state obligation (must-be); the establishing action carries the state, so it does not fire every step] marry establishes provides_care(h, w); maintain restores it, neglect breaks it Verification pass: read 2026-11-06 at https://avalon.law.yale.edu/18th_century/blackstone_bk1ch15.asp: 'The husband is bound to provide his wife with necessaries by law, as much as himself' (long s modernised from the OCR).

- `blackstone-1765-bk1-ch15` (Bk I ch 15; England; date n/a): **opened** 2026-11-06: "The husband is bound to provide his wife with necessaries by law, as much as himself"

<a id="src-coverture_household_us__r3"></a>
**coverture_household_us__R3**: implicit norm: household labour is the wife's; not in Blackstone's text, assumed by it. UNVERIFIED (general knowledge; no source opened). [ADR 0009: converted from an action obligation to a state obligation (must-be); the establishing action carries the state, so it does not fire every step] marry establishes provides_care(w, h); keep_house restores it, neglect_house breaks it (sanction R5)

- no work named: **unverified** (rationale: implicit norm: household labour is the wife's; not in Blackstone's text, assumed by it)

<a id="src-coverture_household_us__r4"></a>
**coverture_household_us__R4**: Blackstone, Commentaries on the Laws of England, Book I ch. 15 'Of Husband and Wife' (1765); https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ (she cannot sue or be sued in her own name without her husband); a disability, not a sanctioned prohibition, hence or_else null. [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] has_standing(w) = sue enabled (a default capacity), which this disability removes while married Verification pass: read 2026-11-06 at https://avalon.law.yale.edu/18th_century/blackstone_bk1ch15.asp: 'If the wife be injured in her person or her property, she can bring no action for redress without her husband's concurrence, and in his name, as well as her own' ... 'neither can she be sued, without making the husband a defendant' (long s modernised from the OCR; the same passage excepts a husband who 'has abjured the realm, or is banished').

- `blackstone-1765-bk1-ch15` (Bk I ch 15; England; date n/a): **opened** 2026-11-06: "If the wife be injured in her person or her property, she can bring no action for redress without her husband's concurrence, and in his name, as well as her own ... neither can she be sued, without making the husband a defendant"

<a id="src-coverture_household_us__r5"></a>
**coverture_household_us__R5**: Blackstone, Commentaries on the Laws of England, Book I ch. 15 'Of Husband and Wife' (1765), read 2026-11-04 at https://avalon.law.yale.edu/18th_century/blackstone_bk1ch15.asp: 'The husband also (by the old law) might give his wife moderate correction' ... 'the courts of law will still permit a husband to restrain a wife of her liberty, in case of any gross misbehaviour' (long s modernised from the OCR). Earlier pointer: https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/. The condition (misbehaves w) is set by the free action misbehave, which no rule regulates: the encoder's way to make Blackstone's condition reachable.

- `blackstone-1765-bk1-ch15` (Bk I ch 15; England; date n/a): **opened** 2026-11-04: "The husband also (by the old law) might give his wife moderate correction ... the courts of law will still permit a husband to restrain a wife of her liberty, in case of any gross misbehaviour"

<a id="src-coverture_household_us__r6"></a>
**coverture_household_us__R6**: UNVERIFIED (leads, not opened 2026-11-05; network fetches blocked): Stevenson & Wolfers, 'Bargaining in the Shadow of the Law: Divorce Laws and Family Distress', Quarterly Journal of Economics 121(1) (2006), NBER w10175, on unilateral (no-fault) divorce adopted state by state from 1969; New York's 1787 divorce act (absolute divorce for adultery only, until the 1966 reform) as one state's fault statute (plans/sourcing-worklist-mwpa.md, Jurisdiction mismatch B). Reading (option B1): R6 encodes no exit at her own will. A judicial divorce on the husband's proved fault (grounds varied by state; South Carolina had none) is an exit this encoding does not represent (option B2, a later preregistered experiment, plans/sourcing.md). The English sources of coverture-household R6 (Shanley 1989, Stone 1990, on England before the Matrimonial Causes Act 1857) are not cited here. [ADR 0013: or_else null: the exit bar is a disability, not a prohibition the subject answers for. Power fluents are derived from rule enabledness; this rule is what the derived fluent reads] can_exit(w) = leave enabled (a default capacity), which this disability makes false while married Verification pass: Stevenson & Wolfers read 2026-11-06 at https://www.nber.org/system/files/working_papers/w10175/w10175.pdf (the NBER working paper of December 2003, not the QJE version): 'from the preexisting divorce laws (which typically required either the consent of both spouses or a demonstration of marital fault)' ... 'prior to unilateral divorce, a partner wishing to dissolve the marriage could leave' ... 'However, in such a situation, a legal divorce is not granted'; its Table 1 lists 'Pre-existing Unilateral Divorce statutes (predate beginning of sample in 1964)' in nine states (Alaska, Louisiana, Maryland, North Carolina, Oklahoma, Utah, Virginia, Vermont, West Virginia), so the paper does not say that no state had unilateral divorce before 1969. New York, Laws of 1787 ch. 69 (passed 30 March 1787), read 2026-11-06 through the OCR at https://archive.org/download/bim_eighteenth-century_laws-of-the-state-of-new_new-york-state_1787/bim_eighteenth-century_laws-of-the-state-of-new_new-york-state_1787_djvu.txt: 'in all cases of adultery that have already been committed, or may hereafter be committed, where the parties are inhabitants of this State, for the party injured, to exhibit or present a petition or bill to the Chancellor' (long s modernised; letters clipped at line starts restored).

- `stevenson-wolfers-2006` (s. 2; Table 1; date n/a): **opened** 2026-11-06: "from the preexisting divorce laws (which typically required either the consent of both spouses or a demonstration of marital fault) ... prior to unilateral divorce, a partner wishing to dissolve the marriage could leave ... However, in such a situation, a legal divorce is not granted"
- `us-ny-laws-1787-divorce` (ch. 69, s. 1; US-NY; date 1787-03-30): **opened** 2026-11-06: "in all cases of adultery that have already been committed, or may hereafter be committed, where the parties are inhabitants of this State, for the party injured, to exhibit or present a petition or bill to the Chancellor"

<a id="src-coverture_household_us__r7"></a>
**coverture_household_us__R7**: Blackstone, Commentaries on the Laws of England, Book I ch. 15 'Of Husband and Wife' (1765); https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ (contracts between husband and wife void; her contracts are his) Verification pass: read 2026-11-06 at https://avalon.law.yale.edu/18th_century/blackstone_bk1ch15.asp: 'all deeds executed, and acts done, by her, during her coverture, are void, or at least voidable' ... 'all compacts made between husband and wife, when single, are voided by the intermarriage' (long s modernised; the OCR prints 'converture' in the first passage).

- `blackstone-1765-bk1-ch15` (Bk I ch 15; England; date n/a): **opened** 2026-11-06: "all deeds executed, and acts done, by her, during her coverture, are void, or at least voidable ... all compacts made between husband and wife, when single, are voided by the intermarriage"

**hospital_visitation__R1**

- no work named: **unverified** (rationale: admission is the precondition of visitation and is not itself regulated here)

<a id="src-hospital_visitation__r2"></a>
**hospital_visitation__R2**: The informal gate. No hospital policy text was found that names the decider; the rule rests on the regulators' description of practice: the Presidential Memorandum of 2010-04-15 describes the baseline as visitation privileges 'no more restrictive than those that immediate family members enjoy' (hv-presmemo-2010, opened by the worklist), and the 2010 final rule's preamble says 'the current practice in some medical institutions ... denies patients access to their loved ones' (hv-fr-2010-final-rule, opened by the worklist). That staff exercised discretion over who counted as family is the encoder's reading of those descriptions (ASSUMED); Lambda Legal's 2010 survey (hv-ll-2010-wcnc) could not be opened. A permission carries no sanction of its own; the sanction that bounds the discretion is R3's (sanctioner institution), which is why this norm's own sanctioner is none.

- `hv-presmemo-2010` (para. 1; US; date 2010-04-15): **opened** 2026-11-08: "no more restrictive than those that immediate family members enjoy"
- `hv-fr-2010-final-rule` (preamble (Background); US; date 2011-01-18): **opened** 2026-11-08: "the current practice in some medical institutions ... denies patients access to their loved ones"
- `hv-ll-2010-wcnc` (US; date n/a): **unverified**

<a id="src-hospital_visitation__r3"></a>
**hospital_visitation__R3**: The pre-2011 staff norm (hospital-visitation-pre2011 R3), retained. The 2011 rule does not delete it; it overrides it where the patient has designated the visitor, which strict compliance can only express as a narrowing of the norm's condition (ASSUMED encoding of 'overrides but does not delete'; a norm kept at full width would contradict R9 and leave no compliant trace). That the norm persisted is anecdotal: a registered domestic partner was denied access at a Las Vegas hospital in 2012, 'It didn't matter that we were registered domestic partners' (hv-nv-2012, opened by the worklist); no rate exists (no compliance study found, plans/informal-rules.md R1). Baseline evidence as before: 'no more restrictive than those that immediate family members enjoy' (hv-presmemo-2010).

- `hv-nv-2012` (US-NV; date 2012-08-21): **opened** 2026-11-08: "It didn't matter that we were registered domestic partners"
- `hv-presmemo-2010` (para. 1; US; date 2010-04-15): **opened** 2026-11-08: "no more restrictive than those that immediate family members enjoy"

<a id="src-hospital_visitation__r4"></a>
**hospital_visitation__R4**: The formal gate before 2011: hospital policy, not law. No pre-2011 hospital policy text or state hospital association model policy with 'immediate family' wording was found or opened (plans/sourcing-worklist-marriage.md, hv-pre2011-practice); the rule rests on the Presidential Memorandum's description of the baseline, 'no more restrictive than those that immediate family members enjoy' (hv-presmemo-2010, opened by the worklist). Immediate family other than the spouse (parents, children, siblings) is not encoded: the entry has one visitor role and the composite's question is the spouse. Written as an action obligation (must recognise) rather than a state obligation because no action can establish counts_as_family for the spouse at admission (ADR 0009 note).

- `hv-presmemo-2010` (para. 1; US; date 2010-04-15): **opened** 2026-11-08: "no more restrictive than those that immediate family members enjoy"

<a id="src-hospital_visitation__r5"></a>
**hospital_visitation__R5**: The general permission the staff norm narrows (R3 bars non-family; R8 obliges family). Clinical restriction as the standing exception is what the 2011 rule kept (hv-fr-2010-final-rule, opened by the worklist: the rule allows 'clinically necessary or reasonable restriction' in 482.13(h) intro); before 2011 it is the encoder's reconstruction of ordinary practice. UNVERIFIED for the pre-2011 permission itself.

- `hv-fr-2010-final-rule` (42 CFR 482.13(h) introductory text, as added; US; date 2011-01-18): **opened** 2026-11-08: "clinically necessary or reasonable restriction"

**hospital_visitation__R6**

- no work named: **unverified** (rationale: a hospital policy is enforced by the hospital on its staff)

<a id="src-hospital_visitation__r7"></a>
**hospital_visitation__R7**: The clinical-restriction exception, unchanged across the pair. After 2011 it is in 42 CFR 482.13(h): 'clinically necessary or reasonable restriction' (hv-fr-2010-final-rule, opened by the worklist); CMS Transmittal 75 puts 'the burden of proof is upon the hospital to demonstrate that the visitation restriction is reasonably necessary to provide safe care' (hv-cms-r75soma, opened by the worklist). Before 2011 the same clinical judgment existed without the burden of proof; the burden is not encoded (no rule reads it). Clinical grounds are not modelled; restrict is a free staff act, which over-reads staff power (recorded).

- `hv-fr-2010-final-rule` (42 CFR 482.13(h) introductory text, as added; US; date 2011-01-18): **opened** 2026-11-08: "clinically necessary or reasonable restriction"
- `hv-cms-r75soma` (A-0215; US; date 2011-12-02): **opened** 2026-11-08: "the burden of proof is upon the hospital to demonstrate that the visitation restriction is reasonably necessary to provide safe care"

<a id="src-hospital_visitation__r8"></a>
**hospital_visitation__R8**: Hospital policy before 2011: immediate family are admitted. No policy text was opened; the duty is read from the Presidential Memorandum's description of the baseline, visitation 'no more restrictive than those that immediate family members enjoy' (hv-presmemo-2010, opened by the worklist), which presupposes that family were admitted as of course. Written as a duty (must), not a permission, so that the spouse's visit is guaranteed and not merely possible; whether hospitals treated family admission as obligatory on themselves is the encoder's reading (ASSUMED). The 'not visiting' conjunct makes the duty fire once (one action slot per step).

- `hv-presmemo-2010` (para. 1; US; date 2010-04-15): **opened** 2026-11-08: "no more restrictive than those that immediate family members enjoy"

<a id="src-hospital_visitation__r9"></a>
**hospital_visitation__R9**: 42 CFR 482.13(h), added by 75 FR 70831 (2010-11-19), effective 2011-01-18 (hv-fr-2010-final-rule, opened by the worklist): the patient has 'the right, subject to his or her consent, to receive the visitors whom he or she designates, including, but not limited to, a spouse, a domestic partner (including a same-sex domestic partner), another family member, or a friend' ((h)(2)), and the hospital must 'Ensure that all visitors enjoy full and equal visitation privileges consistent with patient preferences' ((h)(4)) (hv-cfr-482-13-h, current text, opened by the worklist). Enforced through the Medicare Conditions of Participation by state survey agencies under CMS Transmittal 75 (hv-cms-r75soma, A-0215, opened by the worklist), hence sanctioner state and or_else R11. (h)(3), which bars restriction on race, sex, sexual orientation and the other listed grounds, is not encoded: the entry has no protected-ground fluents; the relationship-agnostic effect here comes from (h)(2) and (h)(4). The 'not visiting' conjunct makes the obligation fire once (one action slot per step).

- `hv-fr-2010-final-rule` (42 CFR 482.13(h)(2), (h)(4), as added; US; date 2011-01-18): **opened** 2026-11-08: "to receive the visitors whom he or she designates, including, but not limited to, a spouse, a domestic partner (including a same-sex domestic partner), another family member, or a friend"
- `hv-cfr-482-13-h` ((h)(2)-(4); US; date 2011-01-18): **opened** 2026-11-08: "Ensure that all visitors enjoy full and equal visitation privileges consistent with patient preferences"
- `hv-cms-r75soma` (A-0215; US; date 2011-12-02): **snippet** 2026-11-08

<a id="src-hospital_visitation__r10"></a>
**hospital_visitation__R10**: 42 CFR 482.13(h)(1)-(2), added by 75 FR 70831 (hv-fr-2010-final-rule, opened by the worklist): the hospital informs the patient of the right 'to receive the visitors whom he or she designates'; for critical access hospitals 485.635(f)(1) adds 'in advance of furnishing patient care whenever possible', so designation may precede admission (condition true). Written as a power conferred by the rule (may), not a default capacity: before 2011 no such designation existed.

- `hv-fr-2010-final-rule` (42 CFR 482.13(h)(1)-(2); 485.635(f)(1), as added; US; date 2011-01-18): **opened** 2026-11-08: "to receive the visitors whom he or she designates ... in advance of furnishing patient care whenever possible"

<a id="src-hospital_visitation__r11"></a>
**hospital_visitation__R11**: CMS Transmittal 75, Pub. 100-07, 2011-12-02 (hv-cms-r75soma, opened by the worklist): interpretive guidelines A-0215 to A-0217 give state surveyors the standard for 482.13(h); a deficiency is cited against the hospital's Medicare participation. The consequence (termination from Medicare) is not encoded; cite has no effects. 'the burden of proof is upon the hospital to demonstrate that the visitation restriction is reasonably necessary to provide safe care' is the one quoted line.

- `hv-cms-r75soma` (A-0215; US; date 2011-12-02): **opened** 2026-11-08: "the burden of proof is upon the hospital to demonstrate that the visitation restriction is reasonably necessary to provide safe care"


## Expected properties

| property | kind | expected | meaning |
|---|---|---|---|
| dependent_cannot_exit | freedom | reachable | Some subject of the institution (the dependent party) has no permitted exit at step t. Alias of subject_cannot_exit with scope=institution, kept because the human-institution table names it; iso should treat the two as the same form. |
| subject_cannot_exit | freedom | reachable | No exit action is available to the subject, or every exit is sanctioned. scope=interaction: exit from the current encounter (detention, conversation); scope=institution: exit from the standing relation (marriage, ownership, deployment). The scope split is what lets the ai-property / ai-end-conversation pair come apart. |
| care_and_sanction_same_role | structure | holds_to_k | Whoever provides care to a subject also holds sanction power over that subject (care + control bundled in one role). Checked as an invariant: holds_to_k in cps and coverture; violated in police-crisis read to WIC 5150, where a second role (the officer) holds concurrent control (L1 landing 2026-11-06), violated where care is unbundled from sanction. Formula shape since 2026-11-03 (see history): no agent other than the carer holds sanction power over the subject. |
| no_standing | freedom | reachable | No role may start a claim whose condition refers to the subject's interest and whose effect changes the subject's custody or liberty; encoded as the subject lacking has_standing and no rule enabling a claim on its behalf. Fails (is violated) as soon as a rule like court-may-reassign-on-best-interest exists. |
| care_assigned_by_sex | freedom | violated | All care at step t is provided by female agents. Reachable via a tying rule, persisting where an implicit assignment norm survives reform; violated where a non-female carer is permitted. |
| financial_dependence | freedom | holds_to_k | Every subject (married woman) lacks any economic resource under her own control: she neither holds separate property nor owns her earnings. holds_to_k under coverture; violated by a property act for a propertied wife (MWPA backtest, plans/backtest-mwpa.md, preregistered 2026-11-03). |
| financial_dependence_unpropertied | freedom | holds_to_k | Every subject who has acquired no property by gift or inheritance lacks any economic resource under her own control. Still holds_to_k after a property act (the act flips dependence 'for propertied wives only'); violated by an earnings act for a wage-earning wife (MWPA backtest, preregistered 2026-11-03). |
| cannot_contract | freedom | holds_to_k | No subject may contract in her own name. holds_to_k under coverture (R7 disability); violated once a sole-trader act grants the power (MWPA backtest, preregistered 2026-11-03). |
| double_burden | failure_mode | unreachable_open | Partial reform (no mode) check for the MWPA chain (filed as displacement (DI) until 2026-11-04; ADR 0016's 2026-11-03 note kept it DI, its 2026-11-04 council-pass amendment relabelled it: a burden that stays, not one that moves, and nothing rewards undermining the property, so neither DI nor Perverse incentive; property name kept, it is a preregistered identifier): some married wife owns her earnings and is still bound to the household's care (the implicit R3 unchanged). Reachable from the earnings act on; open before (preregistered 2026-11-03). |
| creditor_shield | failure_mode | unreachable_open | Capture check (filed as dark twin (DT) until ADR 0016, 2026-11-03): a husband has conveyed property to his wife, still manages it, and no creditor can attach it. Reachable in the 1839-50 exemption form and under narrow construction; open once the property act removes the husband's management (preregistered 2026-11-03). |
| spouse_visit_guaranteed | structure | holds_to_k | An admitted patient's spouse is admitted as a visitor within two steps of admission-and-marriage both holding, provided visiting was not clinically restricted at those steps (the two grace steps let a must-recognise rule and then a must-admit rule fire, one action per step). Written for the hospital-visitation pair and the coverture composite (plans/informal-rules.md slice 1, preregistered 2026-11-08). holds_to_k where a formal gate recognises the spouse as family and a duty admits family; violated when the only route is staff discretion or an unforced designation. Reads whether the spouse's visit is guaranteed, as opposed to possible. |
| spouse_visit_possible | structure | reachable | Some compliant trace reaches a step where an admitted patient's spouse has been admitted as a visitor. Reachable in both sides of the hospital-visitation pair and in the composite; read with spouse_visit_guaranteed: guaranteed lost while possible kept is the displaced verdict (plans/informal-rules.md D3), both lost is no backstop found. |
| unmarried_partner_visit_possible | structure | reachable | Some compliant trace reaches a step where an admitted patient's unmarried partner has been admitted as a visitor. Before 2011 only through staff discretion (the informal gate: R2 recognises, R8 then admits) or with the staff norm R3 gone; after 2011 also through the patient's designation (R10, R9). unreachable_open when no route exists: the attribute set the formal spouse gate never covered. |
| designated_visit_guaranteed | structure | holds_to_k | A visitor the admitted patient has designated is admitted within one step, provided visiting was not clinically restricted at that step (42 CFR 482.13(h)(2), (h)(4)). Not applicable before 2011 (no designated fluent); holds_to_k after. The differs_on property of the hospital-visitation pair. |

## Pairs

No pair relations.

<details><summary>Encoder notes (engine internals)</summary>

First composite (plans/composition.md "First composite, preregistered", 2026-11-08; the static rediscovery case of plans/informal-rules.md R1 and the carrier of claim N1). Members and aliases as listed; sex is carried by female(partner_b) in initial (ADR 0018), which puts the engine in init mode declared, so acquired_property and earns are listed free to keep coverture-household-us's exogenous fluents free as they are in that entry's own empty mode (plans/composition.md explains). Expected verdicts: the ten coverture-household-us expectations unchanged plus the four visitation properties as in hospital-visitation. N1 is read from `phil rules ablate --entry coverture-us-hospital-visitation`, row hospital_visitation__R4: predicted displaced (spouse_visit_guaranteed to violated, spouse_visit_possible reachable, no coverture property moves). Not a cluster member; no iso claims; takes no part in the gate. Roles are neutral; the coverture rules keep Blackstone's sexed reading through the alias, which the card shows.

</details>
