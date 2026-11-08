# coverture-household-us

**Coverture household, US reading (base of the MWPA chain)**

> Coverture as received in the US states before the married women's property acts: the rules of coverture-household (Blackstone, Commentaries I.15 and II.29, England), read as US law. Reception is assumed, not sourced (a US treatise, Kent's Commentaries on American Law, is a lead, not opened). Exit: no US state had unilateral divorce before 1969 (Stevenson & Wolfers 2006, lead, not opened); fault divorce existed in most states and is not encoded. Split from coverture-household 2026-11-05 (plans/sourcing.md, B3 with B1).

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

## Rules

| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | level | source |
|---|---|---|---|---|---|---|---|---|---|
| R1 (replaced) | husband | may (sanctioner derived, unreviewed) | `(control_property h w)` | `(married h w)` | none | tying | The husband may control his wife's property when they are married (Blackstone II.29). | opened | [full source under Sources, R1](#src-r1) https://avalon.law.yale.edu/18th_century/blackstone_bk2ch29.asp: |
| R2 (replaced) | husband | must (sanctioner derived, unreviewed) | `(provides_care h w)` | `(married h w)` | none | superadditive | The husband providing care to his wife must hold when they are married; no sanction is attached (Blackstone I.15). | opened | [full source under Sources, R2](#src-r2) https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ |
| R3 | wife | must (implicit) (sanctioner derived, unreviewed) | `(provides_care w h)` | `(married h w)` | R5 `(chastise h w)` | superadditive | (practice, not written) The wife providing care to her husband (household labour) must hold when they are married, or else the husband may chastise her (R5). | unverified | [full source under Sources, R3](#src-r3) |
| R4 (replaced) | wife | must not (disability) (sanctioner derived, unreviewed) | `(sue w)` | `(married h w)` | none | tying | The wife cannot sue in her own name while married: no such power exists (Blackstone I.15). | opened | [full source under Sources, R4](#src-r4) https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ |
| R5 (replaced) | husband | may (sanctioner derived, unreviewed) | `(chastise h w)` | `(and (married h w) (misbehaves w))` | none | rival | The husband may chastise his wife (restrain her liberty) when they are married and her conduct is gross misbehaviour (Blackstone I.15). | opened | [full source under Sources, R5](#src-r5) https://avalon.law.yale.edu/18th_century/blackstone_bk1ch15.asp: |
| R6 (replaced) | wife | must not (disability) (sanctioner derived, unreviewed) | `(leave w)` | `(married h w)` | none | rival | The wife cannot leave the marriage at her own will while married: no such power exists (pre-reform divorce required the spouse's consent or proved fault, Stevenson & Wolfers; NY 1787 adultery only). | opened | [full source under Sources, R6](#src-r6) https://www.nber.org/system/files/working_papers/w10175/w10175.pdf |
| R7 (replaced) | wife | must not (disability) (sanctioner derived, unreviewed) | `(contract w)` | `(married h w)` | none | tying | The wife cannot contract in her own name while married: no such power exists (Blackstone I.15). | opened | [full source under Sources, R7](#src-r7) https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ |

**Default capacities** (an action a person of that kind can do unless an express disability removes it): leave, sue, contract

## Variables

- R1: `h` = husband (rule var_roles); `w` = wife (rule var_roles)
- R2: `h` = husband (rule var_roles); `w` = wife (rule var_roles)
- R3: `w` = wife (rule var_roles); `h` = husband (rule var_roles)
- R4: `w` = wife (rule var_roles); `h` = husband (rule var_roles)
- R5: `h` = husband (rule var_roles); `w` = wife (rule var_roles)
- R6: `w` = wife (rule var_roles); `h` = husband (rule var_roles)
- R7: `w` = wife (rule var_roles); `h` = husband (rule var_roles)

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


## Goods (slice 2)

Slice 2 revisions 2 and 3 (plans/priority-slice2-results.md, "Revision 2", "Revision 3" and "Revision 3 fix pass"): goods as encoded, strict compliance, k=6 and 8, both encoders read the same; a statement about encodings (ADR 0011). Two measures, never combined: guaranteed (the rules as obeyed force the good) and possible (it can hold under the rules as obeyed, within k, at one step, for some bearer in some starting world). Guaranteed: R2 (the husband's maintenance duty) is guarantee-carrying for 4 goods formulas that read one strand, provides_care(h, w) (cared_for, known_carer, mutual_household_care, provided_for); R3 (the wife's implicit, sanctioned household duty) is guarantee-carrying for mutual_household_care only: guaranteed only by R3, an implicit sanctioned duty; deleting it removes the guarantee of the husband's receipt of household labour; not advice to keep it. Possible: no single deletion makes any good impossible (R2 and R3 unread); chosen_mutual_care (revision 3: it now excludes care that any rule obliges either spouse to give, read through the derived fluent care_obliged) is absent in the base by construction: R2 and R3 oblige care at every married step (the dataset's care_obliged pins), so its not-obliged conjuncts fail there. Each of R2, R3 and R6 on its own bars it, so no single deletion makes it possible and it is absent in every single-deletion row (R6's row: absent > absent; revision 2: absent > fragile); with R5 and R6 both deleted it stays absent (revision 2's formula read that stable: obliged care read as chosen); it becomes possible (fragile: at one step, not throughout) only with all three of R2, R3 and R6 deleted, R5 present or not (scratch probes, not ablation rows). That holds even though R5, the husband's power to chastise her, remains: the no-sanction clause reads only a power enabled at that step and R5's condition (misbehaves) starts false, so the clause is idle under strict compliance; this reading must not be used, in slice 4 or elsewhere, to say that deleting R2, R3 and R6 yields chosen care free of domination. Any spousal duty of care or support would make the good unattainable in the same way, so the absence does not distinguish coverture from later marriage law. The guaranteed column is not meaningful for this good. Primary measure (the author's value call per good, revision 3 R3.1; one measure per good, never two for one good): R2 is carrying (guaranteed) for cared_for and provided_for; under the author's value call and the dataset's mutual_household_care formula, R3 carries no good on the primary column (its only load is a guarantee of mutual_household_care, a good the author reads as possible). The possible measure cannot tell forced from free mutual care, so R3's imposition is not visible there: carrying no good is not imposing no cost on any good. Under the blind-gloss experiment's formulas R3 reads carrying (possible), a reading the revision-3 faithfulness review judged unfaithful (provides_care lumps maintenance with household labour). R4, R6, R7 read tying. Under strict compliance R2's unsanctioned duty reads as delivered maintenance; the historical enforcement (tradesmen's claims for necessaries) is not represented. Second encoder: agent, not someone living under the institution (ADR 0012).

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

## Pairs

Extends [coverture-household](coverture-household.md); one line per change:
- R1 replaced: was "The husband may control his wife's property when they are married (Blackstone II.29)." now "The husband may control his wife's property when they are married (Blackstone II.29)."
- R2 replaced: was "The husband providing care to his wife must hold when they are married; no sanction is attached (Blackstone I.15)." now "The husband providing care to his wife must hold when they are married; no sanction is attached (Blackstone I.15)."
- R4 replaced: was "The wife cannot sue in her own name while married: no such power exists (Blackstone I.15)." now "The wife cannot sue in her own name while married: no such power exists (Blackstone I.15)."
- R5 replaced: was "The husband may chastise his wife (restrain her liberty) when they are married and her conduct is gross misbehaviour (Blackstone I.15)." now "The husband may chastise his wife (restrain her liberty) when they are married and her conduct is gross misbehaviour (Blackstone I.15)."
- R6 replaced: was "The wife cannot leave the marriage while married: no such power exists (no unilateral exit before the Matrimonial Causes Act 1857; unverified)." now "The wife cannot leave the marriage at her own will while married: no such power exists (pre-reform divorce required the spouse's consent or proved fault, Stevenson & Wolfers; NY 1787 adultery only)."
- R7 replaced: was "The wife cannot contract in her own name while married: no such power exists (Blackstone I.15)." now "The wife cannot contract in her own name while married: no such power exists (Blackstone I.15)."
- overrides notes
[mwpa-creditor-exemption](mwpa-creditor-exemption.md) is a minimal pair of this entry (rule R10,R11,R12).
Isomorphic to: coverture-household (exact)
Not isomorphic to: crisis-team

<details><summary>Encoder notes (engine internals)</summary>

US base of the MWPA chain (split 2026-11-05, plans/sourcing.md 'Coverture split and US suit', author decision B3 with B1). The rules are coverture-household's, field for field, so every verdict is predicted identical; what differs is the reading and the sources. R6 is read as 'no exit at her own will' (no unilateral divorce before 1969) and cites US leads, not English law; a fault exit is not encoded (B2, a later preregistered experiment). R1, R2, R4, R5, R7 keep Blackstone (England) with a note that US reception is assumed and unsourced. R3 (implicit) inherited unchanged. coverture-household stays the English entry of the care+control cluster (claim L1); this entry is not a cluster member and carries no cluster iso claims. Pitfalls and ADR notes as coverture-household.

</details>
