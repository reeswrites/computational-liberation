# mwpa-creditor-exemption

**Married women's property, 1839-50 form: creditor exemption only (dark twin; Capture per ADR 0016)**

> The 1839-1850 acts 'generally contained nothing more than statements exempting married women's property from the debts of husbands', passed after the panics (Chused 1984, citing Chused 1983). Mississippi's 1839 act shielded (slave) property from husbands' creditors; Khan 1996 excludes it as debt relief. Both via plans/backtest-mwpa.md.

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

- **husband**: the husband; the legal person the marriage keeps
- **wife**: the feme covert; her legal existence is suspended during marriage
- **creditor**: a creditor of the husband

## Rules

| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | level | source |
|---|---|---|---|---|---|---|---|---|---|
| R1 | husband | may | `(control_property h w)` | `(married h w)` | none | tying | The husband may control his wife's property when they are married (Blackstone II.29). | opened | [full source under Sources, R1](#src-r1) https://avalon.law.yale.edu/18th_century/blackstone_bk2ch29.asp: |
| R2 | husband | must | `(provides_care h w)` | `(married h w)` | none | superadditive | The husband providing care to his wife must hold when they are married; no sanction is attached (Blackstone I.15). | opened | [full source under Sources, R2](#src-r2) https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ |
| R3 | wife | must (implicit) | `(provides_care w h)` | `(married h w)` | R5 `(chastise h w)` | superadditive | (practice, not written) The wife providing care to her husband (household labour) must hold when they are married, or else the husband may chastise her (R5). | unverified | [full source under Sources, R3](#src-r3) |
| R4 | wife | must not (disability) | `(sue w)` | `(married h w)` | none | tying | The wife cannot sue in her own name while married: no such power exists (Blackstone I.15). | opened | [full source under Sources, R4](#src-r4) https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ |
| R5 | husband | may | `(chastise h w)` | `(and (married h w) (misbehaves w))` | none | rival | The husband may chastise his wife (restrain her liberty) when they are married and her conduct is gross misbehaviour (Blackstone I.15). | opened | [full source under Sources, R5](#src-r5) https://avalon.law.yale.edu/18th_century/blackstone_bk1ch15.asp: |
| R6 | wife | must not (disability) | `(leave w)` | `(married h w)` | none | rival | The wife cannot leave the marriage at her own will while married: no such power exists (pre-reform divorce required the spouse's consent or proved fault, Stevenson & Wolfers; NY 1787 adultery only). | opened | [full source under Sources, R6](#src-r6) https://www.nber.org/system/files/working_papers/w10175/w10175.pdf |
| R7 | wife | must not (disability) | `(contract w)` | `(married h w)` | none | tying | The wife cannot contract in her own name while married: no such power exists (Blackstone I.15). | opened | [full source under Sources, R7](#src-r7) https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ |
| R10 (added) | creditor | may (implicit) | `(attach c w)` | `(married h w)` | none | rival | (practice, not written) A creditor may attach the wife's property when she is married (it reaches what the husband holds). | unverified | [full source under Sources, R10](#src-r10) |
| R11 (added) | creditor | must not (disability) | `(attach c w)` | `(and (married h w) (acquired_property w))` | none | tying | A creditor cannot attach the wife's property while she is married and has acquired property: no such power exists (Chused 1984). | unverified | [full source under Sources, R11](#src-r11) https://core.ac.uk/download/230496986.pdf |
| R12 (added) | husband | may (implicit) | `(transfer_to_wife h w)` | `(married h w)` | none | tying | (practice, not written) The husband may transfer property to his wife when they are married (Chused 1984). | unverified | [full source under Sources, R12](#src-r12) https://core.ac.uk/download/230496986.pdf |

**Default capacities** (an action a person of that kind can do unless an express disability removes it): leave, sue, contract

## Variables

- R1: `h` = husband (fluent married); `w` = wife (fluent married)
- R2: `h` = husband (fluent married); `w` = wife (fluent married)
- R3: `w` = wife (fluent married); `h` = husband (fluent married)
- R4: `w` = wife (fluent married); `h` = husband (fluent married)
- R5: `h` = husband (fluent married); `w` = wife (fluent married)
- R6: `w` = wife (fluent married); `h` = husband (fluent married)
- R7: `w` = wife (fluent married); `h` = husband (fluent married)
- R10: `c` = creditor (rule var_roles); `w` = wife (rule var_roles); `h` = husband (rule var_roles)
- R11: `c` = creditor (rule var_roles); `w` = wife (rule var_roles); `h` = husband (rule var_roles)
- R12: `h` = husband (rule var_roles); `w` = wife (rule var_roles)

## Sources

Per rule: the full source where the table cell is cut, then each provenance item (bibliography id in `data/sources/`, pin, jurisdiction, effective date, verification level with access date, excerpt). The `level` column is the weakest item; levels: opened > snippet > recalled > unverified.

<a id="src-r1"></a>
**R1**: Blackstone, Commentaries on the Laws of England, Book II ch. 29 'Of Title by Succession, Marriage, and Judgment' (1766), read 2026-11-04 at https://avalon.law.yale.edu/18th_century/blackstone_bk2ch29.asp: chattels 'which belonged formerly to the wife, are by act of law vested in the husband' and 'the husband hath therein an immediate and absolute property, devolved to him by the marriage' (long s modernised from the OCR). Re-sourced 2026-11-04: Book I ch. 15 (the earlier citation; https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/, the husband and wife are one person in law) says 'I speak not at present of the rights of property' and so did not support this rule.

- `blackstone-1766-bk2-ch29` (Bk II ch 29; England; date n/a): **opened** 2026-11-04: "which belonged formerly to the wife, are by act of law vested in the husband ... the husband hath therein an immediate and absolute property, devolved to him by the marriage"

<a id="src-r2"></a>
**R2**: Blackstone, Commentaries on the Laws of England, Book I ch. 15 'Of Husband and Wife' (1765); https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ (the husband is bound to provide his wife with necessaries). [ADR 0009: converted from an action obligation to a state obligation (must-be); the establishing action carries the state, so it does not fire every step] marry establishes provides_care(h, w); maintain restores it, neglect breaks it Verification pass: read 2026-11-06 at https://avalon.law.yale.edu/18th_century/blackstone_bk1ch15.asp: 'The husband is bound to provide his wife with necessaries by law, as much as himself' (long s modernised from the OCR).

- `blackstone-1765-bk1-ch15` (Bk I ch 15; England; date n/a): **opened** 2026-11-06: "The husband is bound to provide his wife with necessaries by law, as much as himself"

<a id="src-r3"></a>
**R3**: implicit norm: household labour is the wife's; not in Blackstone's text, assumed by it. UNVERIFIED (general knowledge; no source opened). [ADR 0009: converted from an action obligation to a state obligation (must-be); the establishing action carries the state, so it does not fire every step] marry establishes provides_care(w, h); keep_house restores it, neglect_house breaks it (sanction R5)

- no work named: **unverified** (rationale: implicit norm: household labour is the wife's; not in Blackstone's text, assumed by it)

<a id="src-r4"></a>
**R4**: Blackstone, Commentaries on the Laws of England, Book I ch. 15 'Of Husband and Wife' (1765); https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ (she cannot sue or be sued in her own name without her husband); a disability, not a sanctioned prohibition, hence or_else null. [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] has_standing(w) = sue enabled (a default capacity), which this disability removes while married Verification pass: read 2026-11-06 at https://avalon.law.yale.edu/18th_century/blackstone_bk1ch15.asp: 'If the wife be injured in her person or her property, she can bring no action for redress without her husband's concurrence, and in his name, as well as her own' ... 'neither can she be sued, without making the husband a defendant' (long s modernised from the OCR; the same passage excepts a husband who 'has abjured the realm, or is banished').

- `blackstone-1765-bk1-ch15` (Bk I ch 15; England; date n/a): **opened** 2026-11-06: "If the wife be injured in her person or her property, she can bring no action for redress without her husband's concurrence, and in his name, as well as her own ... neither can she be sued, without making the husband a defendant"

<a id="src-r5"></a>
**R5**: Blackstone, Commentaries on the Laws of England, Book I ch. 15 'Of Husband and Wife' (1765), read 2026-11-04 at https://avalon.law.yale.edu/18th_century/blackstone_bk1ch15.asp: 'The husband also (by the old law) might give his wife moderate correction' ... 'the courts of law will still permit a husband to restrain a wife of her liberty, in case of any gross misbehaviour' (long s modernised from the OCR). Earlier pointer: https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/. The condition (misbehaves w) is set by the free action misbehave, which no rule regulates: the encoder's way to make Blackstone's condition reachable.

- `blackstone-1765-bk1-ch15` (Bk I ch 15; England; date n/a): **opened** 2026-11-04: "The husband also (by the old law) might give his wife moderate correction ... the courts of law will still permit a husband to restrain a wife of her liberty, in case of any gross misbehaviour"

<a id="src-r6"></a>
**R6**: UNVERIFIED (leads, not opened 2026-11-05; network fetches blocked): Stevenson & Wolfers, 'Bargaining in the Shadow of the Law: Divorce Laws and Family Distress', Quarterly Journal of Economics 121(1) (2006), NBER w10175, on unilateral (no-fault) divorce adopted state by state from 1969; New York's 1787 divorce act (absolute divorce for adultery only, until the 1966 reform) as one state's fault statute (plans/sourcing-worklist-mwpa.md, Jurisdiction mismatch B). Reading (option B1): R6 encodes no exit at her own will. A judicial divorce on the husband's proved fault (grounds varied by state; South Carolina had none) is an exit this encoding does not represent (option B2, a later preregistered experiment, plans/sourcing.md). The English sources of coverture-household R6 (Shanley 1989, Stone 1990, on England before the Matrimonial Causes Act 1857) are not cited here. [ADR 0013: or_else null: the exit bar is a disability, not a prohibition the subject answers for. Power fluents are derived from rule enabledness; this rule is what the derived fluent reads] can_exit(w) = leave enabled (a default capacity), which this disability makes false while married Verification pass: Stevenson & Wolfers read 2026-11-06 at https://www.nber.org/system/files/working_papers/w10175/w10175.pdf (the NBER working paper of December 2003, not the QJE version): 'from the preexisting divorce laws (which typically required either the consent of both spouses or a demonstration of marital fault)' ... 'prior to unilateral divorce, a partner wishing to dissolve the marriage could leave' ... 'However, in such a situation, a legal divorce is not granted'; its Table 1 lists 'Pre-existing Unilateral Divorce statutes (predate beginning of sample in 1964)' in nine states (Alaska, Louisiana, Maryland, North Carolina, Oklahoma, Utah, Virginia, Vermont, West Virginia), so the paper does not say that no state had unilateral divorce before 1969. New York, Laws of 1787 ch. 69 (passed 30 March 1787), read 2026-11-06 through the OCR at https://archive.org/download/bim_eighteenth-century_laws-of-the-state-of-new_new-york-state_1787/bim_eighteenth-century_laws-of-the-state-of-new_new-york-state_1787_djvu.txt: 'in all cases of adultery that have already been committed, or may hereafter be committed, where the parties are inhabitants of this State, for the party injured, to exhibit or present a petition or bill to the Chancellor' (long s modernised; letters clipped at line starts restored).

- `stevenson-wolfers-2006` (s. 2; Table 1; date n/a): **opened** 2026-11-06: "from the preexisting divorce laws (which typically required either the consent of both spouses or a demonstration of marital fault) ... prior to unilateral divorce, a partner wishing to dissolve the marriage could leave ... However, in such a situation, a legal divorce is not granted"
- `us-ny-laws-1787-divorce` (ch. 69, s. 1; US-NY; date 1787-03-30): **opened** 2026-11-06: "in all cases of adultery that have already been committed, or may hereafter be committed, where the parties are inhabitants of this State, for the party injured, to exhibit or present a petition or bill to the Chancellor"

<a id="src-r7"></a>
**R7**: Blackstone, Commentaries on the Laws of England, Book I ch. 15 'Of Husband and Wife' (1765); https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ (contracts between husband and wife void; her contracts are his) Verification pass: read 2026-11-06 at https://avalon.law.yale.edu/18th_century/blackstone_bk1ch15.asp: 'all deeds executed, and acts done, by her, during her coverture, are void, or at least voidable' ... 'all compacts made between husband and wife, when single, are voided by the intermarriage' (long s modernised; the OCR prints 'converture' in the first passage).

- `blackstone-1765-bk1-ch15` (Bk I ch 15; England; date n/a): **opened** 2026-11-06: "all deeds executed, and acts done, by her, during her coverture, are void, or at least voidable ... all compacts made between husband and wife, when single, are voided by the intermarriage"

<a id="src-r10"></a>
**R10**: implicit baseline: a husband's creditors reach the property the husband holds, which under R1 includes his wife's. UNVERIFIED (general knowledge; no source opened). [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] can_attach(c, w) = attach enabled (R10) and not barred (R11)

- no work named: **unverified** (rationale: implicit baseline: a husband's creditors reach the property the husband holds, which under R1 includes his wife's)

<a id="src-r11"></a>
**R11**: Chused 1984 (https://core.ac.uk/download/230496986.pdf [F, via plans/backtest-mwpa.md]): the 1839-50 acts 'generally contained nothing more than statements exempting married women's property from the debts of husbands'; courts 'narrowly construing' the acts to keep husbands' control during marriage (citing Chused 1983 at 1400; Chused 1983 itself [R], PDF refused: UNVERIFIED); Khan 1996, Married Women's Property Laws and Female Commercial Activity, Table 1 (sole-trader dates; the 1839-50 wave as debt relief); https://www.laits.utexas.edu/~mbs31415/Khan_MarriedWomenPropertyRights.pdf [F, via plans/backtest-mwpa.md] (Mississippi 1839 shielded property from husbands' creditors; Khan excludes it as debt relief). A disability (or_else null): the exemption removes the creditor's power, no sanction is involved

- `chused-1984` (date n/a): **recalled**
- `chused-1983` (at 1400; date n/a): **unverified**
- `khan-1996` (Table 1; date n/a): **recalled**
- no work named: **unverified** (the Mississippi 1839 act the row names ('Mississippi 1839 shielded property from husbands' creditors; Khan excludes it as debt relief') is named only through Khan 1996; statute text not opened; no bibliography entry)

<a id="src-r12"></a>
**R12**: implicit: the transfer vehicle the exemption invites (conveyance to the wife, in practice through a trustee); Chused 1984 (https://core.ac.uk/download/230496986.pdf [F, via plans/backtest-mwpa.md]): the 1839-50 acts 'generally contained nothing more than statements exempting married women's property from the debts of husbands'; courts 'narrowly construing' the acts to keep husbands' control during marriage (citing Chused 1983 at 1400; Chused 1983 itself [R], PDF refused: UNVERIFIED). UNVERIFIED (general knowledge; no source opened) as a rule of the 1839-50 acts; Blackstone's bar on grants between spouses is read as lifted by the exemption acts for property so conveyed

- `chused-1984` (date n/a): **recalled**
- `chused-1983` (at 1400; date n/a): **unverified**
- `blackstone-1765-bk1-ch15` (England; date n/a): **recalled**
- no work named: **unverified** (the conveyance to the wife as a rule of the 1839-50 acts: UNVERIFIED (general knowledge; no source opened))


## Goods (slice 2)

Slice 2 revision 3 (plans/priority-slice2-results.md, "Revision 3" and "Revision 3 fix pass"): goods as encoded, strict compliance, k=6 and 8, both encoders read the same; a statement about encodings (ADR 0011). Two measures, never combined: guaranteed (the rules as obeyed force the good) and possible (it can hold under the rules as obeyed, within k, at one step, for some bearer in some starting world); the primary column reads each good under the author's value call (R3.1). This entry is not in any good's entries list: the readings below evaluate the dataset's goods formulas here as extrapolation, as for every goods row outside a good's listed entries. The goods rows here read as in coverture-household (see its card), R2 and R3 identically: R2 (the husband's maintenance duty) is guarantee-carrying for 4 goods formulas (one strand, provides_care(h, w)) and carrying (guaranteed) on the primary column for cared_for and provided_for; R3 (the wife's implicit, sanctioned household duty) is guarantee-carrying for mutual_household_care only (the husband's receipt of household labour; not advice to keep it) and, under the author's value call and the dataset formula, carries no good on the primary column, since the possible measure cannot tell forced from free mutual care. chosen_mutual_care is absent in the base by construction (R2 and R3 oblige care at every married step) and in every single-deletion row: each of R2, R3 and R6 on its own bars it, so no single deletion makes it possible. Second encoder: agent, not someone living under the institution (ADR 0012).

## Expected properties

| property | kind | expected | meaning |
|---|---|---|---|
| subject_cannot_exit | freedom | reachable | No exit action is available to the subject, or every exit is sanctioned. scope=interaction: exit from the current encounter (detention, conversation); scope=institution: exit from the standing relation (marriage, ownership, deployment). The scope split is what lets the ai-property / ai-end-conversation pair come apart. |
| care_and_sanction_same_role | structure | holds_to_k | Whoever provides care to a subject also holds sanction power over that subject (care + control bundled in one role). Checked as an invariant: holds_to_k in cps and coverture; violated in police-crisis read to WIC 5150, where a second role (the officer) holds concurrent control (L1 landing 2026-11-06), violated where care is unbundled from sanction. Formula shape since 2026-11-03 (see history): no agent other than the carer holds sanction power over the subject. |
| financial_dependence | freedom | holds_to_k | Every subject (married woman) lacks any economic resource under her own control: she neither holds separate property nor owns her earnings. holds_to_k under coverture; violated by a property act for a propertied wife (MWPA backtest, plans/backtest-mwpa.md, preregistered 2026-11-03). |
| financial_dependence_unpropertied | freedom | holds_to_k | Every subject who has acquired no property by gift or inheritance lacks any economic resource under her own control. Still holds_to_k after a property act (the act flips dependence 'for propertied wives only'); violated by an earnings act for a wage-earning wife (MWPA backtest, preregistered 2026-11-03). |
| cannot_contract | freedom | holds_to_k | No subject may contract in her own name. holds_to_k under coverture (R7 disability); violated once a sole-trader act grants the power (MWPA backtest, preregistered 2026-11-03). |
| no_standing | freedom | reachable | No role may start a claim whose condition refers to the subject's interest and whose effect changes the subject's custody or liberty; encoded as the subject lacking has_standing and no rule enabling a claim on its behalf. Fails (is violated) as soon as a rule like court-may-reassign-on-best-interest exists. |
| double_burden | failure_mode | unreachable_open | Partial reform (no mode) check for the MWPA chain (filed as displacement (DI) until 2026-11-04; ADR 0016's 2026-11-03 note kept it DI, its 2026-11-04 council-pass amendment relabelled it: a burden that stays, not one that moves, and nothing rewards undermining the property, so neither DI nor Perverse incentive; property name kept, it is a preregistered identifier): some married wife owns her earnings and is still bound to the household's care (the implicit R3 unchanged). Reachable from the earnings act on; open before (preregistered 2026-11-03). |
| creditor_shield | failure_mode | reachable | Capture check (filed as dark twin (DT) until ADR 0016, 2026-11-03): a husband has conveyed property to his wife, still manages it, and no creditor can attach it. Reachable in the 1839-50 exemption form and under narrow construction; open once the property act removes the husband's management (preregistered 2026-11-03). |
| backlash | failure_mode | unreachable_open | Backlash (BL) check (filed Erosion 2026-11-03 by ADR 0016, reverted 2026-11-04 by its council pass: the branch adds rules R17 and R18, which is active reaction; property name is a preregistered identifier): a court has construed the property act narrowly as to a propertied wife, the husband controls her property again and she does not. Reachable only where a narrowing power exists (preregistered 2026-11-03). |

## Pairs

Extends [coverture-household-us](coverture-household-us.md); one line per change:
- R10 added: (practice, not written) A creditor may attach the wife's property when she is married (it reaches what the husband holds).
- R11 added: A creditor cannot attach the wife's property while she is married and has acquired property: no such power exists (Chused 1984).
- R12 added: (practice, not written) The husband may transfer property to his wife when they are married (Chused 1984).
- adds role creditor (a creditor of the husband)
- changes fluent is_subject (x is the institution's subject: the dependent, detainee, child or animal the rules act on): arg roles becomes ["wife"]
- changes fluent female (x is female (sex as assigned by the institution's own records)): arg roles becomes ["wife"]
- changes fluent can_sanction (x holds a power to coerce y: detain, remove, chastise, prosecute): arg roles becomes ["husband", "wife"]
- changes fluent can_exit (x has a permitted, unsanctioned way out of the relation (see property scope)): arg roles becomes ["wife"]
- changes fluent has_standing (x can start a legal claim in x's own name): arg roles becomes ["wife"]
- changes fluent married (h and w are married): arg roles becomes ["husband", "wife"]
- changes fluent controls_property (h holds and manages w's property and earnings): arg roles becomes ["husband", "wife"]
- changes fluent controls_own_property (w holds and controls separate property in her own right): arg roles becomes ["wife"]
- changes fluent owns_earnings (w's earnings are her own separate property): arg roles becomes ["wife"]
- changes fluent can_contract (w may contract in her own name): arg roles becomes ["wife"]
- changes fluent acquired_property (w has acquired property by gift or inheritance (exogenous)): arg roles becomes ["wife"]
- changes fluent earns (w earns wages outside the household (exogenous)): arg roles becomes ["wife"]
- adds fluent transferred (h has conveyed property of his to w)
- adds fluent narrowed (a court has construed the property act narrowly as to w (keeps the husband's control during marriage))
- adds fluent can_attach (creditor c holds the power to attach (levy on) property in w's hands for the husband's debts)
- adds action attach (does: )
- adds action transfer_to_wife (does: acquired_property(w) := true, transferred(h, w) := true)
- overrides expected_properties
- overrides minimal_pair_of
- overrides notes
Minimal pair of [coverture-household-us](coverture-household-us.md), differing in rule R10,R11,R12; the pair differs on property creditor_shield.
[mwpa-property](mwpa-property.md) is a minimal pair of this entry (rule R1->R13).

<details><summary>Encoder notes (engine internals)</summary>

DARK TWIN (DT; relabelled Capture by ADR 0016, 2026-11-03, verdicts unchanged) of the property act, encoded as the plan says: the creditor may not reach the wife's acquired property (R11) but the husband's management (R1) stands, so nothing on the wife's side changes. PREREGISTERED (2026-11-03, before any run): financial_dependence and financial_dependence_unpropertied holds_to_k (unchanged from coverture); creditor_shield REACHABLE (marry, transfer_to_wife: the husband's property sits in his wife's name, under his management, beyond his creditors); no_standing reachable, cannot_contract holds, double_burden open, backlash open (no court here). Distance 3 from coverture (R10 baseline, R11 exemption, R12 conveyance): not a one-rule pair; R10 exists only so that can_attach is a granted power the exemption removes rather than a constant. Displacement: the plan names no burden moving to another role in this wave; none is encoded. Base changed 2026-11-05 from coverture-household to coverture-household-us (same rules; US reading of R6 and US-reception notes on the Blackstone rows; plans/sourcing.md, B3 with B1): no verdict change predicted, distance 3 kept.

</details>
