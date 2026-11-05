# mwpa-property

**Married women's property act: separate property (coverture minus R1, plus may hold_property)**

> Property acts (GLT Table 1: MA 1845, NY 1848, PA 1848, ...): a married woman holds property acquired by gift or inheritance in her own right, beyond her husband's control and his creditors. Statute texts not opened ([R]); dates and the gloss via plans/backtest-mwpa.md.

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
| R2 | husband | must | `(provides_care h w)` | `(married h w)` | none | superadditive | The husband providing care to his wife must hold when they are married; no sanction is attached (Blackstone I.15). | recalled | [full source under Sources, R2](#src-r2) https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ |
| R3 | wife | must (implicit) | `(provides_care w h)` | `(married h w)` | R5 `(chastise h w)` | superadditive | (practice, not written) The wife providing care to her husband (household labour) must hold when they are married, or else the husband may chastise her (R5). | unverified | [full source under Sources, R3](#src-r3) |
| R4 | wife | must not (disability) | `(sue w)` | `(married h w)` | none | tying | The wife cannot sue in her own name while married: no such power exists (Blackstone I.15). | recalled | [full source under Sources, R4](#src-r4) https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ |
| R5 | husband | may | `(chastise h w)` | `(and (married h w) (misbehaves w))` | none | rival | The husband may chastise his wife (restrain her liberty) when they are married and her conduct is gross misbehaviour (Blackstone I.15). | opened | [full source under Sources, R5](#src-r5) https://avalon.law.yale.edu/18th_century/blackstone_bk1ch15.asp: |
| R6 | wife | must not (disability) | `(leave w)` | `(married h w)` | none | rival | The wife cannot leave the marriage at her own will while married: no such power exists (no unilateral divorce in any US state before 1969; unverified). | unverified | [full source under Sources, R6](#src-r6) |
| R7 | wife | must not (disability) | `(contract w)` | `(married h w)` | none | tying | The wife cannot contract in her own name while married: no such power exists (Blackstone I.15). | recalled | Blackstone, Commentaries on the Laws of England, Book I ch. 15 'Of Husband and Wife' (1765); https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ (contracts between husband and wife void; her contracts are his) |
| R10 | creditor | may (implicit) | `(attach c w)` | `(married h w)` | none | rival | (practice, not written) A creditor may attach the wife's property when she is married (it reaches what the husband holds). | unverified | [full source under Sources, R10](#src-r10) |
| R11 | creditor | must not (disability) | `(attach c w)` | `(and (married h w) (acquired_property w))` | none | tying | A creditor cannot attach the wife's property while she is married and has acquired property: no such power exists (Chused 1984). | unverified | [full source under Sources, R11](#src-r11) https://core.ac.uk/download/230496986.pdf |
| R12 | husband | may (implicit) | `(transfer_to_wife h w)` | `(married h w)` | none | tying | (practice, not written) The husband may transfer property to his wife when they are married (Chused 1984). | unverified | [full source under Sources, R12](#src-r12) https://core.ac.uk/download/230496986.pdf |
| R13 (added) | wife | may | `(hold_property w)` | `(and (married h w) (acquired_property w) (not (narrowed w)))` | none | tying | The wife may hold property in her own right when married, she has acquired property, and the act has not been narrowly construed (NY MWPA 1848). | unverified | [full source under Sources, R13](#src-r13) https://isnie-archive.sioe.org/assets/files/papers2007/geddes.pdf |

**Default capacities** (an action a person of that kind can do unless an express disability removes it): leave, sue, contract

## Variables

- R2: `h` = husband (fluent married); `w` = wife (fluent married)
- R3: `w` = wife (fluent married); `h` = husband (fluent married)
- R4: `w` = wife (fluent married); `h` = husband (fluent married)
- R5: `h` = husband (fluent married); `w` = wife (fluent married)
- R6: `w` = wife (fluent married); `h` = husband (fluent married)
- R7: `w` = wife (fluent married); `h` = husband (fluent married)
- R10: `c` = creditor (rule var_roles); `w` = wife (rule var_roles); `h` = husband (rule var_roles)
- R11: `c` = creditor (rule var_roles); `w` = wife (rule var_roles); `h` = husband (rule var_roles)
- R12: `h` = husband (rule var_roles); `w` = wife (rule var_roles)
- R13: `w` = wife (rule var_roles); `h` = husband (rule var_roles)

## Sources

Per rule: the full source where the table cell is cut, then each provenance item (bibliography id in `data/sources/`, pin, jurisdiction, effective date, verification level with access date, excerpt). The `level` column is the weakest item; levels: opened > snippet > recalled > unverified.

<a id="src-r2"></a>
**R2**: Blackstone, Commentaries on the Laws of England, Book I ch. 15 'Of Husband and Wife' (1765); https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ (the husband is bound to provide his wife with necessaries). [ADR 0009: converted from an action obligation to a state obligation (must-be); the establishing action carries the state, so it does not fire every step] marry establishes provides_care(h, w); maintain restores it, neglect breaks it

- `blackstone-1765-bk1-ch15` (Bk I ch 15; England; date n/a): **recalled**

<a id="src-r3"></a>
**R3**: implicit norm: household labour is the wife's; not in Blackstone's text, assumed by it. UNVERIFIED (general knowledge; no source opened). [ADR 0009: converted from an action obligation to a state obligation (must-be); the establishing action carries the state, so it does not fire every step] marry establishes provides_care(w, h); keep_house restores it, neglect_house breaks it (sanction R5)

- no work named: **unverified** (rationale: implicit norm: household labour is the wife's; not in Blackstone's text, assumed by it)

<a id="src-r4"></a>
**R4**: Blackstone, Commentaries on the Laws of England, Book I ch. 15 'Of Husband and Wife' (1765); https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ (she cannot sue or be sued in her own name without her husband); a disability, not a sanctioned prohibition, hence or_else null. [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] has_standing(w) = sue enabled (a default capacity), which this disability removes while married

- `blackstone-1765-bk1-ch15` (Bk I ch 15; England; date n/a): **recalled**

<a id="src-r5"></a>
**R5**: Blackstone, Commentaries on the Laws of England, Book I ch. 15 'Of Husband and Wife' (1765), read 2026-11-04 at https://avalon.law.yale.edu/18th_century/blackstone_bk1ch15.asp: 'The husband also (by the old law) might give his wife moderate correction' ... 'the courts of law will still permit a husband to restrain a wife of her liberty, in case of any gross misbehaviour' (long s modernised from the OCR). Earlier pointer: https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/. The condition (misbehaves w) is set by the free action misbehave, which no rule regulates: the encoder's way to make Blackstone's condition reachable.

- `blackstone-1765-bk1-ch15` (Bk I ch 15; England; date n/a): **opened** 2026-11-04: "The husband also (by the old law) might give his wife moderate correction ... the courts of law will still permit a husband to restrain a wife of her liberty, in case of any gross misbehaviour"

<a id="src-r6"></a>
**R6**: UNVERIFIED (leads, not opened 2026-11-05; network fetches blocked): Stevenson & Wolfers, 'Bargaining in the Shadow of the Law: Divorce Laws and Family Distress', Quarterly Journal of Economics 121(1) (2006), NBER w10175, on unilateral (no-fault) divorce adopted state by state from 1969; New York's 1787 divorce act (absolute divorce for adultery only, until the 1966 reform) as one state's fault statute (plans/sourcing-worklist-mwpa.md, Jurisdiction mismatch B). Reading (option B1): R6 encodes no exit at her own will. A judicial divorce on the husband's proved fault (grounds varied by state; South Carolina had none) is an exit this encoding does not represent (option B2, a later preregistered experiment, plans/sourcing.md). The English sources of coverture-household R6 (Shanley 1989, Stone 1990, on England before the Matrimonial Causes Act 1857) are not cited here. [ADR 0013: or_else null: the exit bar is a disability, not a prohibition the subject answers for. Power fluents are derived from rule enabledness; this rule is what the derived fluent reads] can_exit(w) = leave enabled (a default capacity), which this disability makes false while married

- `stevenson-wolfers-2006` (date n/a): **unverified**
- `us-ny-laws-1787-divorce` (US-NY; date n/a): **unverified**

**R7**

- `blackstone-1765-bk1-ch15` (Bk I ch 15; England; date n/a): **recalled**

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

<a id="src-r13"></a>
**R13**: New York Married Women's Property Act 1848 (the statute text itself not opened: [R] UNVERIFIED; dates from Geddes, Lueck & Tennyson 2007 (draft), Table 1 dates of property / earnings acts; https://isnie-archive.sioe.org/assets/files/papers2007/geddes.pdf [F, via plans/backtest-mwpa.md]); Geddes, Lueck & Tennyson 2007 (draft), Table 1 dates of property / earnings acts; https://isnie-archive.sioe.org/assets/files/papers2007/geddes.pdf [F, via plans/backtest-mwpa.md] (property acts: the wife holds and controls property acquired by gift or inheritance as if a feme sole). Conditioned on (not narrowed): a narrow construction (BL entry, R17) re-disables the power. [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] controls_own_property(w) = hold_property enabled (R13)

- `ny-mwpa-1848` (US-NY; date n/a): **unverified**
- `geddes-lueck-tennyson-2007` (Table 1; date n/a): **recalled**


## Expected properties

| property | kind | expected | meaning |
|---|---|---|---|
| subject_cannot_exit | freedom | reachable | No exit action is available to the subject, or every exit is sanctioned. scope=interaction: exit from the current encounter (detention, conversation); scope=institution: exit from the standing relation (marriage, ownership, deployment). The scope split is what lets the ai-property / ai-end-conversation pair come apart. |
| care_and_sanction_same_role | structure | holds_to_k | Whoever provides care to a subject also holds sanction power over that subject (care + control bundled in one role). Checked as an invariant: holds_to_k in the care+control cluster, violated where care is unbundled from sanction. Formula shape since 2026-11-03 (see history): no agent other than the carer holds sanction power over the subject. |
| financial_dependence | freedom | violated | Every subject (married woman) lacks any economic resource under her own control: she neither holds separate property nor owns her earnings. holds_to_k under coverture; violated by a property act for a propertied wife (MWPA backtest, plans/backtest-mwpa.md, preregistered 2026-11-03). |
| financial_dependence_unpropertied | freedom | holds_to_k | Every subject who has acquired no property by gift or inheritance lacks any economic resource under her own control. Still holds_to_k after a property act (the act flips dependence 'for propertied wives only'); violated by an earnings act for a wage-earning wife (MWPA backtest, preregistered 2026-11-03). |
| cannot_contract | freedom | holds_to_k | No subject may contract in her own name. holds_to_k under coverture (R7 disability); violated once a sole-trader act grants the power (MWPA backtest, preregistered 2026-11-03). |
| no_standing | freedom | reachable | No role may start a claim whose condition refers to the subject's interest and whose effect changes the subject's custody or liberty; encoded as the subject lacking has_standing and no rule enabling a claim on its behalf. Fails (is violated) as soon as a rule like court-may-reassign-on-best-interest exists. |
| double_burden | failure_mode | unreachable_open | Partial reform (no mode) check for the MWPA chain (filed as displacement (DI) until 2026-11-04; ADR 0016's 2026-11-03 note kept it DI, its 2026-11-04 council-pass amendment relabelled it: a burden that stays, not one that moves, and nothing rewards undermining the property, so neither DI nor Perverse incentive; property name kept, it is a preregistered identifier): some married wife owns her earnings and is still bound to the household's care (the implicit R3 unchanged). Reachable from the earnings act on; open before (preregistered 2026-11-03). |
| creditor_shield | failure_mode | unreachable_open | Capture check (filed as dark twin (DT) until ADR 0016, 2026-11-03): a husband has conveyed property to his wife, still manages it, and no creditor can attach it. Reachable in the 1839-50 exemption form and under narrow construction; open once the property act removes the husband's management (preregistered 2026-11-03). |
| backlash | failure_mode | unreachable_open | Backlash (BL) check (filed Erosion 2026-11-03 by ADR 0016, reverted 2026-11-04 by its council pass: the branch adds rules R17 and R18, which is active reaction; property name is a preregistered identifier): a court has construed the property act narrowly as to a propertied wife, the husband controls her property again and she does not. Reachable only where a narrowing power exists (preregistered 2026-11-03). |

## Pairs

Extends [mwpa-creditor-exemption](mwpa-creditor-exemption.md); one line per change:
- R1 dropped: The husband may control his wife's property when they are married (Blackstone II.29).
- R13 added: The wife may hold property in her own right when married, she has acquired property, and the act has not been narrowly construed (NY MWPA 1848).
- overrides expected_properties
- overrides minimal_pair_of
- overrides notes
Minimal pair of [mwpa-creditor-exemption](mwpa-creditor-exemption.md), differing in rule R1->R13; the pair differs on property financial_dependence.
[mwpa-earnings](mwpa-earnings.md) is a minimal pair of this entry (rule R14).
[mwpa-property-narrowed](mwpa-property-narrowed.md) is a minimal pair of this entry (rule R17,R18).

<details><summary>Encoder notes (engine internals)</summary>

Plan delta `property`: delete R1 (husband may control_property), add wife may hold_property (R13); the creditor exemption (R11) and conveyance (R12) carry over from the 1839-50 form. PREREGISTERED (2026-11-03, before any run): financial_dependence VIOLATED (a propertied wife now controls her own property), financial_dependence_unpropertied holds_to_k (a wife without acquired property is as dependent as before: the flip is 'for propertied wives only'), can_exit unchanged (subject_cannot_exit reachable), has_standing unchanged (no_standing reachable), cannot_contract holds; creditor_shield OPEN (with R1 gone the husband no longer manages what he conveys: the dark twin is extinguished by the real act), backlash open, double_burden open.

</details>
