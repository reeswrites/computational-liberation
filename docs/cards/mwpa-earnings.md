# mwpa-earnings

**Married women's earnings act (property act plus may keep_earnings)**

> Earnings acts (GLT Table 1): a married woman's earnings from her own labour are her separate property. Statute texts not opened ([R]); via plans/backtest-mwpa.md.

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

- **husband**: the husband; the legal person the marriage keeps
- **wife**: the feme covert; her legal existence is suspended during marriage
- **creditor**: a creditor of the husband

## Rules

| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | level | source |
|---|---|---|---|---|---|---|---|---|---|
| R2 | husband | must [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(provides_care h w)` | `(married h w)` | none | superadditive | The husband providing care to his wife must hold when they are married; no sanction is attached (Blackstone I.15). | opened | [full source under Sources, R2](#src-r2) https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ |
| R3 | wife | must (implicit) [kind: norm; sanctioner: family] (sanctioner derived, unreviewed) | `(provides_care w h)` | `(married h w)` | R5 `(chastise h w)` | superadditive | (practice, not written) The wife providing care to her husband (household labour) must hold when they are married, or else the husband may chastise her (R5). | unverified | [full source under Sources, R3](#src-r3) |
| R4 | wife | must not (disability) [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(sue w)` | `(married h w)` | none | tying | The wife cannot sue in her own name while married: no such power exists (Blackstone I.15; unless the husband has abjured the realm or is banished, when she sues as a feme sole: an exception not encoded). | opened | [full source under Sources, R4](#src-r4) https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ |
| R5 | husband | may [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(chastise h w)` | `(and (married h w) (misbehaves w))` | none | rival | The husband may chastise his wife (restrain her liberty) when they are married and her conduct is gross misbehaviour (Blackstone I.15). | opened | [full source under Sources, R5](#src-r5) https://avalon.law.yale.edu/18th_century/blackstone_bk1ch15.asp: |
| R6 | wife | must not (disability) [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(leave w)` | `(married h w)` | none | rival | The wife cannot leave the marriage at her own will while married: no such power exists (pre-reform divorce required both spouses' consent or proved fault, Stevenson & Wolfers; NY 1787 adultery only). | opened | [full source under Sources, R6](#src-r6) https://www.nber.org/system/files/working_papers/w10175/w10175.pdf |
| R7 | wife | must not (disability) [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(contract w)` | `(married h w)` | none | tying | The wife cannot contract in her own name while married: no such power exists (Blackstone I.15: her legal existence is suspended during the marriage; Blackstone: her acts during coverture are 'void, or at least voidable'; encoded as no power to contract). | opened | [full source under Sources, R7](#src-r7) https://avalon.law.yale.edu/18th_century/blackstone_bk1ch15.asp: |
| R10 | creditor | may (implicit) [kind: formal; sanctioner: none] | `(attach c w)` | `(married h w)` | none | rival | (inferred from written law, Blackstone II.29) A creditor may attach the wife's property when she is married (it reaches what the husband holds). | unverified | [full source under Sources, R10](#src-r10) |
| R11 | creditor | must not (disability) [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(attach c w)` | `(and (married h w) (acquired_property w))` | none | tying | A creditor cannot attach the wife's property while she is married and has acquired property: no such power exists (Chused 1984). | unverified | [full source under Sources, R11](#src-r11) https://core.ac.uk/download/230496986.pdf |
| R12 | husband | may (implicit) [kind: norm; sanctioner: none] (sanctioner derived, unreviewed) | `(transfer_to_wife h w)` | `(married h w)` | none | tying | (practice, not written; written law in substance, text not opened) The husband may transfer property to his wife when they are married (Chused 1984). | unverified | [full source under Sources, R12](#src-r12) https://core.ac.uk/download/230496986.pdf |
| R13 | wife | may [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(hold_property w)` | `(and (married h w) (acquired_property w) (not (narrowed w)))` | none | tying | The wife may hold property in her own right when married, she has acquired property, and the act has not been narrowly construed (NY MWPA 1848). | unverified | [full source under Sources, R13](#src-r13) https://isnie-archive.sioe.org/assets/files/papers2007/geddes.pdf |
| R14 (added) | wife | may [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(keep_earnings w)` | `(and (married h w) (earns w))` | none | tying | The wife may keep her earnings as her own when married and she earns wages outside the household (earnings acts, Geddes et al. 2007). | unverified | [full source under Sources, R14](#src-r14) https://isnie-archive.sioe.org/assets/files/papers2007/geddes.pdf |

**Default capacities** (an action a person of that kind can do unless an express disability removes it): leave, sue, contract

## Variables

- R2: `h` = husband (rule var_roles); `w` = wife (rule var_roles)
- R3: `w` = wife (rule var_roles); `h` = husband (rule var_roles)
- R4: `w` = wife (rule var_roles); `h` = husband (rule var_roles)
- R5: `h` = husband (rule var_roles); `w` = wife (rule var_roles)
- R6: `w` = wife (rule var_roles); `h` = husband (rule var_roles)
- R7: `w` = wife (rule var_roles); `h` = husband (rule var_roles)
- R10: `c` = creditor (rule var_roles); `w` = wife (rule var_roles); `h` = husband (rule var_roles)
- R11: `c` = creditor (rule var_roles); `w` = wife (rule var_roles); `h` = husband (rule var_roles)
- R12: `h` = husband (rule var_roles); `w` = wife (rule var_roles)
- R13: `w` = wife (rule var_roles); `h` = husband (rule var_roles)
- R14: `w` = wife (rule var_roles); `h` = husband (rule var_roles)

## Sources

Per rule: the full source where the table cell is cut, then each provenance item (bibliography id in `data/sources/`, pin, jurisdiction, effective date, verification level with access date, excerpt). The `level` column is the weakest item; levels: opened > snippet > recalled > unverified.

<a id="src-r2"></a>
**R2**: Blackstone, Commentaries on the Laws of England, Book I ch. 15 'Of Husband and Wife' (1765); https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ (the husband is bound to provide his wife with necessaries). [ADR 0009: converted from an action obligation to a state obligation (must-be); the establishing action carries the state, so it does not fire every step] marry establishes provides_care(h, w); maintain restores it, neglect breaks it Verification pass: read 2026-11-06 at https://avalon.law.yale.edu/18th_century/blackstone_bk1ch15.asp: 'The husband is bound to provide his wife with necessaries by law, as much as himself' (long s modernised from the OCR).

- `blackstone-1765-bk1-ch15` (Bk I ch 15; England; date n/a): **opened** 2026-11-06: "The husband is bound to provide his wife with necessaries by law, as much as himself" <https://avalon.law.yale.edu/18th_century/blackstone_bk1ch15.asp>

<a id="src-r3"></a>
**R3**: implicit norm: household labour is the wife's; not in Blackstone's text, assumed by it. UNVERIFIED (general knowledge; no source opened). [ADR 0009: converted from an action obligation to a state obligation (must-be); the establishing action carries the state, so it does not fire every step] marry establishes provides_care(w, h); keep_house restores it, neglect_house breaks it (sanction R5)

- no work named: **unverified** (rationale: implicit norm: household labour is the wife's; not in Blackstone's text, assumed by it)

<a id="src-r4"></a>
**R4**: Blackstone, Commentaries on the Laws of England, Book I ch. 15 'Of Husband and Wife' (1765); https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ (she cannot sue or be sued in her own name without her husband); a disability, not a sanctioned prohibition, hence or_else null. [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] has_standing(w) = sue enabled (a default capacity), which this disability removes while married Verification pass: read 2026-11-06 at https://avalon.law.yale.edu/18th_century/blackstone_bk1ch15.asp: 'If the wife be injured in her person or her property, she can bring no action for redress without her husband's concurrence, and in his name, as well as her own' ... 'neither can she be sued, without making the husband a defendant' (long s modernised from the OCR; the same passage excepts a husband who 'has abjured the realm, or is banished').

- `blackstone-1765-bk1-ch15` (Bk I ch 15; England; date n/a): **opened** 2026-11-06: "If the wife be injured in her person or her property, she can bring no action for redress without her husband's concurrence, and in his name, as well as her own ... neither can she be sued, without making the husband a defendant" <https://avalon.law.yale.edu/18th_century/blackstone_bk1ch15.asp>

<a id="src-r5"></a>
**R5**: Blackstone, Commentaries on the Laws of England, Book I ch. 15 'Of Husband and Wife' (1765), read 2026-11-04 at https://avalon.law.yale.edu/18th_century/blackstone_bk1ch15.asp: 'The husband also (by the old law) might give his wife moderate correction' ... 'the courts of law will still permit a husband to restrain a wife of her liberty, in case of any gross misbehaviour' (long s modernised from the OCR). Earlier pointer: https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/. The condition (misbehaves w) is set by the free action misbehave, which no rule regulates: the encoder's way to make Blackstone's condition reachable.

- `blackstone-1765-bk1-ch15` (Bk I ch 15; England; date n/a): **opened** 2026-11-04: "The husband also (by the old law) might give his wife moderate correction ... the courts of law will still permit a husband to restrain a wife of her liberty, in case of any gross misbehaviour"

<a id="src-r6"></a>
**R6**: Stevenson & Wolfers, 'Bargaining in the Shadow of the Law: Divorce Laws and Family Distress' (NBER working paper w10175, December 2003; Quarterly Journal of Economics 121(1), 2006), read 2026-11-06 at https://www.nber.org/system/files/working_papers/w10175/w10175.pdf (the NBER working paper, not the QJE version): 'from the preexisting divorce laws (which typically required either the consent of both spouses or a demonstration of marital fault)' ... 'prior to unilateral divorce, a partner wishing to dissolve the marriage could leave' ... 'However, in such a situation, a legal divorce is not granted'; its Table 1 lists 'Pre-existing Unilateral Divorce statutes (predate beginning of sample in 1964)' in nine states (Alaska, Louisiana, Maryland, North Carolina, Oklahoma, Utah, Virginia, Vermont, West Virginia), so the paper does not say that no state had unilateral divorce before 1969. New York, Laws of 1787 ch. 69 (passed 30 March 1787), read 2026-11-06 through the OCR at https://archive.org/download/bim_eighteenth-century_laws-of-the-state-of-new_new-york-state_1787/bim_eighteenth-century_laws-of-the-state-of-new_new-york-state_1787_djvu.txt: 'in all cases of adultery that have already been committed, or may hereafter be committed, where the parties are inhabitants of this State, for the party injured, to exhibit or present a petition or bill to the Chancellor' (long s modernised; letters clipped at line starts restored): one state's fault statute, absolute divorce for adultery only until the 1966 reform. Reading (option B1): R6 encodes no exit at her own will. Consent divorce and a judicial divorce on the husband's proved fault (grounds varied by state; South Carolina had none) are exits this encoding does not represent (option B2, now the exit_ground experiment, faithfulness batch 3d, its own preregistration). Both works were cited 2026-11-05 as leads before either text was opened (plans/sourcing-worklist-mwpa.md, Jurisdiction mismatch B); source string reordered 2026-11-08 (faithfulness batch 3a, A7) so the opened texts lead. The English sources of coverture-household R6 (Shanley 1989, Stone 1990, on England before the Matrimonial Causes Act 1857) are not cited here. [ADR 0013: or_else null: the exit bar is a disability, not a prohibition the subject answers for. Power fluents are derived from rule enabledness; this rule is what the derived fluent reads] can_exit(w) = leave enabled (a default capacity), which this disability makes false while married.

- `stevenson-wolfers-2006` (s. 2; Table 1; date n/a): **opened** 2026-11-06: "from the preexisting divorce laws (which typically required either the consent of both spouses or a demonstration of marital fault) ... prior to unilateral divorce, a partner wishing to dissolve the marriage could leave ... However, in such a situation, a legal divorce is not granted" <https://www.nber.org/system/files/working_papers/w10175/w10175.pdf>
- `us-ny-laws-1787-divorce` (ch. 69, s. 1; US-NY; date 1787-03-30): **opened** 2026-11-06: "in all cases of adultery that have already been committed, or may hereafter be committed, where the parties are inhabitants of this State, for the party injured, to exhibit or present a petition or bill to the Chancellor"

<a id="src-r7"></a>
**R7**: Blackstone, Commentaries on the Laws of England, Book I ch. 15 'Of Husband and Wife' (1765), p. 430, read 2026-11-06 and re-read 2026-11-08 at https://avalon.law.yale.edu/18th_century/blackstone_bk1ch15.asp: 'By marriage, the husband and wife are one person in law: that is, the very being or legal existence of the woman is suspended during the marriage, or at least is incorporated and consolidated into that of the husband: under whose wing, protection, and cover, she performs every thing'; the incapacity to contract with third parties is encoded from this passage as a disability (no power). The chapter's literal sentence on her acts, p. 432, introduced as instances where she is 'separately considered; as inferior to him, and acting by his compulsion': 'all deeds executed, and acts done, by her, during her coverture, are void, or at least voidable' (long s modernised; the OCR prints 'converture'); voidable acts bind until avoided, so the row is the stronger reading, kept on the author's ruling of 2026-11-08 (faithfulness batch 3a, A6: the general doctrine and every secondary source the dataset cites treat her contracts with third parties as void at common law; the card says 'encoded as no power'). The earlier second fragment ('all compacts made between husband and wife, when single, are voided by the intermarriage', p. 430) concerns compacts between the spouses, not her capacity with third parties, and is no longer cited for this row (council 2026-11-06). Earlier pointer: https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/.

- `blackstone-1765-bk1-ch15` (Bk I ch 15, pp. 430, 432; England; date n/a): **opened** 2026-11-08: "the very being or legal existence of the woman is suspended during the marriage, or at least is incorporated and consolidated into that of the husband ... all deeds executed, and acts done, by her, during her coverture, are void, or at least voidable" <https://avalon.law.yale.edu/18th_century/blackstone_bk1ch15.asp>

<a id="src-r10"></a>
**R10**: implicit baseline: a husband's creditors reach the property the husband holds, which under R1 includes his wife's. UNVERIFIED as to the creditor's reach (an inference; the Blackstone vesting it rests on is opened, see the provenance item and the excerpt below). [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] can_attach(c, w) = attach enabled (R10) and not barred (R11) Retagged formal 2026-11-08 (batch 3b, B1 ruling): Blackstone Bk II ch 29 (opened 2026-11-04 on coverture-household R1) vests the wife's chattels in the husband as his absolute property; that a husband's creditors reach what he holds is the encoder's inference from it, not a quoted sentence. Excerpt (coverture-household R1 read): chattels 'which belonged formerly to the wife, are by act of law vested in the husband' and 'the husband hath therein an immediate and absolute property, devolved to him by the marriage'.

- no work named: **unverified** (rationale: implicit baseline: a husband's creditors reach the property the husband holds, which under R1 includes his wife's)
- `blackstone-1766-bk2-ch29` (Bk II ch 29; England; date n/a): **opened** 2026-11-04: "which belonged formerly to the wife, are by act of law vested in the husband ... the husband hath therein an immediate and absolute property, devolved to him by the marriage"

<a id="src-r11"></a>
**R11**: Chused 1984 (https://core.ac.uk/download/230496986.pdf [F, via plans/backtest-mwpa.md]): the 1839-50 acts 'generally contained nothing more than statements exempting married women's property from the debts of husbands'; courts 'narrowly construing' the acts to keep husbands' control during marriage (citing Chused 1983 at 1400; Chused 1983 itself [R], PDF refused: UNVERIFIED); Khan 1996, Married Women's Property Laws and Female Commercial Activity, Table 1 (sole-trader dates; the 1839-50 wave as debt relief); https://www.laits.utexas.edu/~mbs31415/Khan_MarriedWomenPropertyRights.pdf [F, via plans/backtest-mwpa.md] (Mississippi 1839 shielded property from husbands' creditors; Khan excludes it as debt relief). A disability (or_else null): the exemption removes the creditor's power, no sanction is involved

- `chused-1984` (date n/a): **recalled**
- `chused-1983` (at 1400; date n/a): **unverified**
- `khan-1996` (Table 1; date n/a): **recalled**
- no work named: **unverified** (the Mississippi 1839 act the row names ('Mississippi 1839 shielded property from husbands' creditors; Khan excludes it as debt relief') is named only through Khan 1996; statute text not opened; no bibliography entry)

<a id="src-r12"></a>
**R12**: implicit: the transfer vehicle the exemption invites (conveyance to the wife, in practice through a trustee); Chused 1984 (https://core.ac.uk/download/230496986.pdf [F, via plans/backtest-mwpa.md]): the 1839-50 acts 'generally contained nothing more than statements exempting married women's property from the debts of husbands'; courts 'narrowly construing' the acts to keep husbands' control during marriage (citing Chused 1983 at 1400; Chused 1983 itself [R], PDF refused: UNVERIFIED). UNVERIFIED (general knowledge; no source opened) as a rule of the 1839-50 acts; Blackstone's bar on grants between spouses is read as lifted by the exemption acts for property so conveyed Kind held at norm 2026-11-08 (batch 3b post-council fix pass: the faithfulness seat refused the B1 promotion, no opened text): written law in substance, text not opened; retag to formal when opened.

- `chused-1984` (date n/a): **recalled**
- `chused-1983` (at 1400; date n/a): **unverified**
- `blackstone-1765-bk1-ch15` (England; date n/a): **recalled**
- no work named: **unverified** (the conveyance to the wife as a rule of the 1839-50 acts: UNVERIFIED (general knowledge; no source opened))

<a id="src-r13"></a>
**R13**: New York Married Women's Property Act 1848 (the statute text itself not opened: [R] UNVERIFIED; dates from Geddes, Lueck & Tennyson 2007 (draft), Table 1 dates of property / earnings acts; https://isnie-archive.sioe.org/assets/files/papers2007/geddes.pdf [F, via plans/backtest-mwpa.md]); Geddes, Lueck & Tennyson 2007 (draft), Table 1 dates of property / earnings acts; https://isnie-archive.sioe.org/assets/files/papers2007/geddes.pdf [F, via plans/backtest-mwpa.md] (property acts: the wife holds and controls property acquired by gift or inheritance as if a feme sole). Conditioned on (not narrowed): a narrow construction (BL entry, R17) re-disables the power. [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] controls_own_property(w) = hold_property enabled (R13)

- `ny-mwpa-1848` (US-NY; date n/a): **unverified**
- `geddes-lueck-tennyson-2007` (Table 1; date n/a): **recalled**

<a id="src-r14"></a>
**R14**: Geddes, Lueck & Tennyson 2007 (draft), Table 1 dates of property / earnings acts; https://isnie-archive.sioe.org/assets/files/papers2007/geddes.pdf [F, via plans/backtest-mwpa.md] (earnings acts: NY 1860, MA 1846/1874, PA 1872, ...: a married woman's wages are her separate property). Statute texts not opened ([R]). [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] owns_earnings(w) = keep_earnings enabled (R14)

- `geddes-lueck-tennyson-2007` (Table 1; date n/a): **recalled**
- no work named: **unverified** (the statutes the row encodes are named only through the secondary work; statute texts not opened ([R]); no bibliography entry)


## Goods (slice 2)

Slice 2 revisions 2 and 3 (plans/priority-slice2-results.md, "Revision 2", "Revision 3" and "Revision 3 fix pass"): goods as encoded, strict compliance, k=6 and 8, both encoders read the same; a statement about encodings (ADR 0011). Two measures, never combined: guaranteed (the rules as obeyed force the good) and possible (it can hold under the rules as obeyed, within k, at one step, for some bearer in some starting world). Guaranteed: R2 (the husband's maintenance duty) is guarantee-carrying for 4 goods formulas that read one strand, provides_care(h, w) (cared_for, known_carer, mutual_household_care, provided_for); R3 (the wife's implicit, sanctioned household duty) is guarantee-carrying for mutual_household_care only: guaranteed only by R3, an implicit sanctioned duty; deleting it removes the guarantee of the husband's receipt of household labour; not advice to keep it. Possible: no single deletion makes any good impossible (R2 and R3 unread); chosen_mutual_care (revision 3: it now excludes care that any rule obliges either spouse to give, read through the derived fluent care_obliged) is absent in the base by construction: R2 and R3 oblige care at every married step (the dataset's care_obliged pins), so its not-obliged conjuncts fail there. Each of R2, R3 and R6 on its own bars it, so no single deletion makes it possible and it is absent in every single-deletion row (R6's row: absent > absent; revision 2: absent > fragile); with R5 and R6 both deleted it stays absent (revision 2's formula read that stable: obliged care read as chosen); it becomes possible (fragile: at one step, not throughout) only with all three of R2, R3 and R6 deleted, R5 present or not (scratch probes, not ablation rows). That holds even though R5, the husband's power to chastise her, remains: the no-sanction clause reads only a power enabled at that step and R5's condition (misbehaves) starts false, so the clause is idle under strict compliance; this reading must not be used, in slice 4 or elsewhere, to say that deleting R2, R3 and R6 yields chosen care free of domination. Any spousal duty of care or support would make the good unattainable in the same way, so the absence does not distinguish coverture from later marriage law. The guaranteed column is not meaningful for this good. Primary measure (the author's value call per good, revision 3 R3.1; one measure per good, never two for one good): R2 is carrying (guaranteed) for cared_for and provided_for; under the author's value call and the dataset's mutual_household_care formula, R3 carries no good on the primary column (its only load is a guarantee of mutual_household_care, a good the author reads as possible). The possible measure cannot tell forced from free mutual care, so R3's imposition is not visible there: carrying no good is not imposing no cost on any good. Under the blind-gloss experiment's formulas R3 reads carrying (possible), a reading the revision-3 faithfulness review judged unfaithful (provides_care lumps maintenance with household labour). R4, R6, R7 read tying. Title-route end state of the route comparison: G guaranteed 5 here vs 4 in coverture-floor, by construction: the same margin case as C (provided_for on R2 for a wife with neither property nor wages); G possible 0 vs 0. Under strict compliance R2's unsanctioned duty reads as delivered maintenance; the historical enforcement (tradesmen's claims for necessaries) is not represented. Second encoder: agent, not someone living under the institution (ADR 0012).

## Expected properties

| property | kind | expected | meaning |
|---|---|---|---|
| subject_cannot_exit | freedom | reachable | No exit action is available to the subject, or every exit is sanctioned. scope=interaction: exit from the current encounter (detention, conversation); scope=institution: exit from the standing relation (marriage, ownership, deployment). The scope split is what lets the ai-property / ai-end-conversation pair come apart. |
| care_and_sanction_same_role | structure | holds_to_k | Whoever provides care to a subject also holds sanction power over that subject (care + control bundled in one role). Checked as an invariant: holds_to_k in cps and coverture; violated in police-crisis read to WIC 5150, where a second role (the officer) holds concurrent control (L1 landing 2026-11-06), violated where care is unbundled from sanction. Formula shape since 2026-11-03 (see history): no agent other than the carer holds sanction power over the subject. |
| financial_dependence | freedom | violated | Every subject (married woman) lacks any economic resource under her own control: she neither holds separate property nor owns her earnings. holds_to_k under coverture; violated by a property act for a propertied wife (MWPA backtest, plans/backtest-mwpa.md, preregistered 2026-11-03). |
| financial_dependence_unpropertied | freedom | violated | Every subject who has acquired no property by gift or inheritance lacks any economic resource under her own control. Still holds_to_k after a property act (the act flips dependence 'for propertied wives only'); violated by an earnings act for a wage-earning wife (MWPA backtest, preregistered 2026-11-03). |
| cannot_contract | freedom | holds_to_k | No subject may contract in her own name. holds_to_k under coverture (R7 disability); violated once a sole-trader act grants the power (MWPA backtest, preregistered 2026-11-03). |
| no_standing | freedom | reachable | No role may start a claim whose condition refers to the subject's interest and whose effect changes the subject's custody or liberty; encoded as the subject lacking has_standing and no rule enabling a claim on its behalf. Fails (is violated) as soon as a rule like court-may-reassign-on-best-interest exists. |
| double_burden | failure_mode | reachable | Partial reform (no mode) check for the MWPA chain (filed as displacement (DI) until 2026-11-04; ADR 0016's 2026-11-03 note kept it DI, its 2026-11-04 council-pass amendment relabelled it: a burden that stays, not one that moves, and nothing rewards undermining the property, so neither DI nor Perverse incentive; property name kept, it is a preregistered identifier): some married wife owns her earnings and is still bound to the household's care (the implicit R3 unchanged). Reachable from the earnings act on; open before (preregistered 2026-11-03). |
| creditor_shield | failure_mode | unreachable_open | Capture check (filed as dark twin (DT) until ADR 0016, 2026-11-03): a husband has conveyed property to his wife, still manages it, and no creditor can attach it. Reachable in the 1839-50 exemption form and under narrow construction; open once the property act removes the husband's management (preregistered 2026-11-03). |
| backlash | failure_mode | unreachable_open | Backlash (BL) check (filed Erosion 2026-11-03 by ADR 0016, reverted 2026-11-04 by its council pass: the branch adds rules R17 and R18, which is active reaction; property name is a preregistered identifier): a court has construed the property act narrowly as to a propertied wife, the husband controls her property again and she does not. Reachable only where a narrowing power exists (preregistered 2026-11-03). |

## Pairs

Extends [mwpa-property](mwpa-property.md); one line per change:
- R14 added: The wife may keep her earnings as her own when married and she earns wages outside the household (earnings acts, Geddes et al. 2007).
- overrides expected_properties
- overrides minimal_pair_of
- overrides notes
Minimal pair of [mwpa-property](mwpa-property.md), differing in rule R14; the pair differs on property financial_dependence_unpropertied.
[mwpa-sole-trader](mwpa-sole-trader.md) is a minimal pair of this entry (rule R7->R15).

<details><summary>Encoder notes (engine internals)</summary>

Plan delta `earnings`: add wife may keep_earnings (R14). PREREGISTERED (2026-11-03, before any run): financial_dependence_unpropertied VIOLATED (a wage-earning wife without property is no longer dependent); DISPLACEMENT (plan's DI): the implicit care obligation R3 is unchanged, so double_burden (a wife who owns her wages and still must keep house) becomes REACHABLE here and was open before; no burden moves to another role (the plan names none). cannot_contract holds, no_standing reachable, exit unchanged.

</details>
