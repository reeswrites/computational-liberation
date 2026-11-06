# coverture-floor

**Coverture with an income-access floor (counterfactual: US coverture plus an income in her own right)**

> Counterfactual, not a historical institution (ADR 0004: no forward claim; ADR 0011: every result is a statement about encodings). The US coverture base (coverture-household-us) plus one rule, R20, giving the wife an income in her own right regardless of marriage: an unconditional income-access floor for the wife, read from but narrower than the material floor of docs/glossary.md (care, health, housing and income). Preregistered in plans/priority-slice2.md section 5 (2026-11-06) as the floor route, compared against the title route (the MWPA chain ending in mwpa-earnings).

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
| R1 | husband | may | `(control_property h w)` | `(married h w)` | none | tying | The husband may control his wife's property when they are married (Blackstone II.29). | opened | [full source under Sources, R1](#src-r1) https://avalon.law.yale.edu/18th_century/blackstone_bk2ch29.asp: |
| R2 | husband | must | `(provides_care h w)` | `(married h w)` | none | superadditive | The husband providing care to his wife must hold when they are married; no sanction is attached (Blackstone I.15). | recalled | [full source under Sources, R2](#src-r2) https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ |
| R3 | wife | must (implicit) | `(provides_care w h)` | `(married h w)` | R5 `(chastise h w)` | superadditive | (practice, not written) The wife providing care to her husband (household labour) must hold when they are married, or else the husband may chastise her (R5). | unverified | [full source under Sources, R3](#src-r3) |
| R4 | wife | must not (disability) | `(sue w)` | `(married h w)` | none | tying | The wife cannot sue in her own name while married: no such power exists (Blackstone I.15). | recalled | [full source under Sources, R4](#src-r4) https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ |
| R5 | husband | may | `(chastise h w)` | `(and (married h w) (misbehaves w))` | none | rival | The husband may chastise his wife (restrain her liberty) when they are married and her conduct is gross misbehaviour (Blackstone I.15). | opened | [full source under Sources, R5](#src-r5) https://avalon.law.yale.edu/18th_century/blackstone_bk1ch15.asp: |
| R6 | wife | must not (disability) | `(leave w)` | `(married h w)` | none | rival | The wife cannot leave the marriage at her own will while married: no such power exists (no unilateral divorce in any US state before 1969; unverified). | unverified | [full source under Sources, R6](#src-r6) |
| R7 | wife | must not (disability) | `(contract w)` | `(married h w)` | none | tying | The wife cannot contract in her own name while married: no such power exists (Blackstone I.15). | recalled | Blackstone, Commentaries on the Laws of England, Book I ch. 15 'Of Husband and Wife' (1765); https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ (contracts between husband and wife void; her contracts are his) |
| R20 (added) | wife | may | `(draw_subsistence w)` | `true` | none | untagged (null) | (counterfactual, not historical) The wife may draw subsistence, an income in her own right from outside the marriage, at any time: an unconditional income-access floor for the wife, not the glossary's material floor (plans/priority-slice2.md section 5 and R2.5). | unverified | [full source under Sources, R20](#src-r20) |

**Default capacities** (an action a person of that kind can do unless an express disability removes it): leave, sue, contract

## Variables

- R1: `h` = husband (fluent married); `w` = wife (fluent married)
- R2: `h` = husband (fluent married); `w` = wife (fluent married)
- R3: `w` = wife (fluent married); `h` = husband (fluent married)
- R4: `w` = wife (fluent married); `h` = husband (fluent married)
- R5: `h` = husband (fluent married); `w` = wife (fluent married)
- R6: `w` = wife (fluent married); `h` = husband (fluent married)
- R7: `w` = wife (fluent married); `h` = husband (fluent married)
- R20: `w` = wife (rule var_roles)

## Sources

Per rule: the full source where the table cell is cut, then each provenance item (bibliography id in `data/sources/`, pin, jurisdiction, effective date, verification level with access date, excerpt). The `level` column is the weakest item; levels: opened > snippet > recalled > unverified.

<a id="src-r1"></a>
**R1**: Blackstone, Commentaries on the Laws of England, Book II ch. 29 'Of Title by Succession, Marriage, and Judgment' (1766), read 2026-11-04 at https://avalon.law.yale.edu/18th_century/blackstone_bk2ch29.asp: chattels 'which belonged formerly to the wife, are by act of law vested in the husband' and 'the husband hath therein an immediate and absolute property, devolved to him by the marriage' (long s modernised from the OCR). Re-sourced 2026-11-04: Book I ch. 15 (the earlier citation; https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/, the husband and wife are one person in law) says 'I speak not at present of the rights of property' and so did not support this rule.

- `blackstone-1766-bk2-ch29` (Bk II ch 29; England; date n/a): **opened** 2026-11-04: "which belonged formerly to the wife, are by act of law vested in the husband ... the husband hath therein an immediate and absolute property, devolved to him by the marriage"

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

<a id="src-r20"></a>
**R20**: counterfactual encoding: no work cited and none claimed; the rule is the floor route of plans/priority-slice2.md section 5 (preregistered 2026-11-06), read from the material floor of docs/glossary.md (subsistence regardless of any relationship). UNVERIFIED as history: no jurisdiction ever enacted it on the coverture frame.

- no work named: **unverified** (rationale: counterfactual encoding: no work cited and none claimed; the rule is the floor route of plans/priority-slice2.md section 5 (preregistered 2026-11-06), read from the material floor of docs/glossary.md (subsistence regardless of any relationship))


## Goods (slice 2)

Slice 2 revision 2 (plans/priority-slice2-results.md, "Revision 2"): goods as encoded, strict compliance, k=6 and 8, both encoders read the same; a statement about encodings (ADR 0011). Two measures, never combined: guaranteed (a rule guarantees the good) and possible (the good can hold for an existing bearer). Guaranteed: R2 (the husband's maintenance duty) is guarantee-carrying for 3 goods formulas that read one strand, provides_care(h, w) (cared_for, known_carer, mutual_household_care); R3 (the wife's implicit, sanctioned household duty) is guarantee-carrying for mutual_household_care only: guaranteed only by R3, an implicit sanctioned duty; not advice to keep it. Possible: no single deletion makes any good impossible (R2 and R3 unread); deleting R6 (the exit bar) makes chosen_mutual_care possible (absent > fragile), the only rule that does. R4, R6, R7 read tying. provided_for stays guaranteed with R2 deleted because R20 provides income; R20 is an unconditional income-access floor for the wife, not the glossary's material floor, untagged (strand null), and its rows are unread. Route comparison: G guaranteed 4 here vs 5 in mwpa-earnings, by construction: the same margin case as C; G possible 0 vs 0. Under strict compliance R2's unsanctioned duty reads as delivered maintenance; the historical enforcement (tradesmen's claims for necessaries) is not represented. Second encoder: agent, not someone living under the institution (ADR 0012).

## Expected properties

| property | kind | expected | meaning |
|---|---|---|---|
| dependent_cannot_exit | freedom | reachable | Some subject of the institution (the dependent party) has no permitted exit at step t. Alias of subject_cannot_exit with scope=institution, kept because the human-institution table names it; iso should treat the two as the same form. |
| subject_cannot_exit | freedom | reachable | No exit action is available to the subject, or every exit is sanctioned. scope=interaction: exit from the current encounter (detention, conversation); scope=institution: exit from the standing relation (marriage, ownership, deployment). The scope split is what lets the ai-property / ai-end-conversation pair come apart. |
| care_and_sanction_same_role | structure | holds_to_k | Whoever provides care to a subject also holds sanction power over that subject (care + control bundled in one role). Checked as an invariant: holds_to_k in the care+control cluster, violated where care is unbundled from sanction. Formula shape since 2026-11-03 (see history): no agent other than the carer holds sanction power over the subject. |
| no_standing | freedom | reachable | No role may start a claim whose condition refers to the subject's interest and whose effect changes the subject's custody or liberty; encoded as the subject lacking has_standing and no rule enabling a claim on its behalf. Fails (is violated) as soon as a rule like court-may-reassign-on-best-interest exists. |
| care_assigned_by_sex | freedom | violated | All care at step t is provided by female agents. Reachable via a tying rule, persisting where an implicit assignment norm survives reform; violated where a non-female carer is permitted. |
| financial_dependence | freedom | holds_to_k | Every subject (married woman) lacks any economic resource under her own control: she neither holds separate property nor owns her earnings. holds_to_k under coverture; violated by a property act for a propertied wife (MWPA backtest, plans/backtest-mwpa.md, preregistered 2026-11-03). |
| financial_dependence_unpropertied | freedom | holds_to_k | Every subject who has acquired no property by gift or inheritance lacks any economic resource under her own control. Still holds_to_k after a property act (the act flips dependence 'for propertied wives only'); violated by an earnings act for a wage-earning wife (MWPA backtest, preregistered 2026-11-03). |
| financial_dependence_means | freedom | violated | Every subject (married woman) lacks any means of her own, counting income as well as property and earnings: she neither holds separate property, nor owns her earnings, nor has an income in her own right (has_own_income, the floor route's fluent). Written for coverture-floor (plans/priority-slice2.md section 5); in the other coverture-family entries has_own_income is false (draw_subsistence unregulated), so it reads as financial_dependence. |
| financial_dependence_margin | freedom | violated | Every subject who has neither acquired property nor earns lacks any means of her own (property, earnings, or an income in her own right). BY CONSTRUCTION in coverture-floor (flagged in advance, plans/priority-slice2.md section 5): R13 and R14 are conditioned on acquired property and on earning, R20 on nothing, so the margin verdicts restate the rule conditions: information, not a finding. |
| cannot_contract | freedom | holds_to_k | No subject may contract in her own name. holds_to_k under coverture (R7 disability); violated once a sole-trader act grants the power (MWPA backtest, preregistered 2026-11-03). |
| double_burden | failure_mode | unreachable_open | Partial reform (no mode) check for the MWPA chain (filed as displacement (DI) until 2026-11-04; ADR 0016's 2026-11-03 note kept it DI, its 2026-11-04 council-pass amendment relabelled it: a burden that stays, not one that moves, and nothing rewards undermining the property, so neither DI nor Perverse incentive; property name kept, it is a preregistered identifier): some married wife owns her earnings and is still bound to the household's care (the implicit R3 unchanged). Reachable from the earnings act on; open before (preregistered 2026-11-03). |
| creditor_shield | failure_mode | unreachable_open | Capture check (filed as dark twin (DT) until ADR 0016, 2026-11-03): a husband has conveyed property to his wife, still manages it, and no creditor can attach it. Reachable in the 1839-50 exemption form and under narrow construction; open once the property act removes the husband's management (preregistered 2026-11-03). |

## Pairs

Extends [coverture-household-us](coverture-household-us.md); one line per change:
- R20 added: (counterfactual, not historical) The wife may draw subsistence, an income in her own right from outside the marriage, at any time: an unconditional income-access floor for the wife, not the glossary's material floor (plans/priority-slice2.md section 5 and R2.5).
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
- overrides expected_properties
- overrides notes

<details><summary>Encoder notes (engine internals)</summary>

COUNTERFACTUAL ENCODING (plans/priority-slice2.md section 5; provenance unverified). Base coverture-household-us, so the title route (mwpa-creditor-exemption -> mwpa-property -> mwpa-earnings) and the floor route start from one rule set; initial_free and the fluent arg_roles are mwpa-creditor-exemption's, so both end states quantify over the same exogenous worlds. One rule added (R20: an unconditional income-access floor for the wife, not the glossary's material floor; strand null, untagged; plans/priority-slice2.md R2.5); no R13, no R14, R1 kept: no property grant. PREREGISTERED (2026-11-06, before any run): financial_dependence and financial_dependence_unpropertied holds_to_k (both read only property and earnings, so they cannot see a floor: as written, material independence means title); financial_dependence_means violated; financial_dependence_margin violated BY CONSTRUCTION (R20's condition is true); double_burden unreachable_open (needs owns_earnings, which only R14 grants); creditor_shield unreachable_open by construction (no creditor role; transferred and can_attach undeclared); exit, standing, contract, care and sanction as in the US base. Goods (slice 2): second encoder: agent, not someone living under the institution (ADR 0012). Rejected base: mwpa-creditor-exemption (would put the floor on a debtor-relief statute and make creditor_shield reachable); a later variant, not built.

</details>
