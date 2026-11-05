# coverture-household

**Coverture household (Blackstone)**

> 'By marriage, the husband and wife are one person in law: that is, the very being or legal existence of the woman is suspended during the marriage, or at least is incorporated and consolidated into that of the husband: under whose wing, protection, and cover, she performs every thing; and is therefore called ... a feme-covert.' He cannot grant anything to her or covenant with her, she cannot sue in her own name, and 'the husband is bound to provide his wife with necessaries by law'. Blackstone, Commentaries on the Laws of England, Book I, ch. 15 (Oxford: Clarendon, 1765). Passage checked at https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/

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

| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | source |
|---|---|---|---|---|---|---|---|---|
| R1 | husband | may | `(control_property h w)` | `(married h w)` | none | tying | The husband may control his wife's property when they are married (Blackstone I.15). | Blackstone, Commentaries on the Laws of England, Book I ch. 15 'Of Husband and Wife' (1765); https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ (the husband and wife are one person in law; her property passes to him) |
| R2 | husband | must | `(provides_care h w)` | `(married h w)` | none | superadditive | The husband providing care to his wife must hold when they are married; no sanction is attached (Blackstone I.15). | [full source under Sources, R2](#src-r2) https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ |
| R3 | wife | must (implicit) | `(provides_care w h)` | `(married h w)` | R5 `(chastise h w)` | superadditive | (practice, not written) The wife providing care to her husband (household labour) must hold when they are married, or else the husband may chastise her (R5). | [full source under Sources, R3](#src-r3) |
| R4 | wife | must not (disability) | `(sue w)` | `(married h w)` | none | tying | The wife cannot sue in her own name while married: no such power exists (Blackstone I.15). | [full source under Sources, R4](#src-r4) https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ |
| R5 | husband | may | `(chastise h w)` | `(married h w)` | none | rival | The husband may chastise his wife (moderate correction, restraint of her liberty) when they are married (Blackstone I.15). | Blackstone, Commentaries on the Laws of England, Book I ch. 15 'Of Husband and Wife' (1765); https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ (the old law allowed the husband 'moderate correction' and to restrain her liberty for gross misbehaviour) |
| R6 | wife | must not (disability) | `(leave w)` | `(married h w)` | none | rival | The wife cannot leave the marriage while married: no such power exists (Blackstone I.15). | [full source under Sources, R6](#src-r6) https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ |
| R7 | wife | must not (disability) | `(contract w)` | `(married h w)` | none | tying | The wife cannot contract in her own name while married: no such power exists (Blackstone I.15). | Blackstone, Commentaries on the Laws of England, Book I ch. 15 'Of Husband and Wife' (1765); https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ (contracts between husband and wife void; her contracts are his) |

**Default capacities** (an action a person of that kind can do unless an express disability removes it): leave, sue, contract

## Variables

- R1: `h` = unbound (encoder to fix); `w` = unbound (encoder to fix)
- R2: `h` = unbound (encoder to fix); `w` = unbound (encoder to fix)
- R3: `w` = unbound (encoder to fix); `h` = unbound (encoder to fix)
- R4: `w` = unbound (encoder to fix); `h` = unbound (encoder to fix)
- R5: `h` = unbound (encoder to fix); `w` = unbound (encoder to fix)
- R6: `w` = unbound (encoder to fix); `h` = unbound (encoder to fix)
- R7: `w` = unbound (encoder to fix); `h` = unbound (encoder to fix)

## Sources

<a id="src-r2"></a>
**R2**: Blackstone, Commentaries on the Laws of England, Book I ch. 15 'Of Husband and Wife' (1765); https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ (the husband is bound to provide his wife with necessaries). [ADR 0009: converted from an action obligation to a state obligation (must-be); the establishing action carries the state, so it does not fire every step] marry establishes provides_care(h, w); maintain restores it, neglect breaks it

<a id="src-r3"></a>
**R3**: implicit norm: household labour is the wife's; not in Blackstone's text, assumed by it. UNVERIFIED (general knowledge; no source opened). [ADR 0009: converted from an action obligation to a state obligation (must-be); the establishing action carries the state, so it does not fire every step] marry establishes provides_care(w, h); keep_house restores it, neglect_house breaks it (sanction R5)

<a id="src-r4"></a>
**R4**: Blackstone, Commentaries on the Laws of England, Book I ch. 15 'Of Husband and Wife' (1765); https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ (she cannot sue or be sued in her own name without her husband); a disability, not a sanctioned prohibition, hence or_else null. [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] has_standing(w) = sue enabled (a default capacity), which this disability removes while married

<a id="src-r6"></a>
**R6**: Blackstone, Commentaries on the Laws of England, Book I ch. 15 'Of Husband and Wife' (1765); https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ (restraint of liberty; no unilateral divorce). [ADR 0013: or_else -> null. The subject's exit bar is a disability (no permitted exit exists), not a prohibition the subject answers for; the sanction power that used to be linked here keeps its own trigger condition, so under strict compliance nothing changes and the link only duplicated it. Same reading for coverture R6, police-crisis R4, cps R10 and companion R6.] [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] can_exit(w) = leave enabled (a default capacity), which this disability makes false while married


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
| cannot_contract | freedom | holds_to_k | No subject may contract in her own name. holds_to_k under coverture (R7 disability); violated once a sole-trader act grants the power (MWPA backtest, preregistered 2026-11-03). |
| double_burden | failure_mode | unreachable_open | Partial reform (no mode) check for the MWPA chain (filed as displacement (DI) until 2026-11-04; ADR 0016's 2026-11-03 note kept it DI, its 2026-11-04 council-pass amendment relabelled it: a burden that stays, not one that moves, and nothing rewards undermining the property, so neither DI nor Perverse incentive; property name kept, it is a preregistered identifier): some married wife owns her earnings and is still bound to the household's care (the implicit R3 unchanged). Reachable from the earnings act on; open before (preregistered 2026-11-03). |
| creditor_shield | failure_mode | unreachable_open | Capture check (filed as dark twin (DT) until ADR 0016, 2026-11-03): a husband has conveyed property to his wife, still manages it, and no creditor can attach it. Reachable in the 1839-50 exemption form and under narrow construction; open once the property act removes the husband's management (preregistered 2026-11-03). |

## Pairs

Extended by: [mwpa-creditor-exemption](mwpa-creditor-exemption.md)
[mwpa-creditor-exemption](mwpa-creditor-exemption.md) is a minimal pair of this entry (rule R10,R11,R12).
Isomorphic to: police-crisis (guard+strands), cps (guard+strands)
Not isomorphic to: crisis-team
Contrasts with controls: lease, public-library, naming-convention

<details><summary>Encoder notes (engine internals)</summary>

Care + control: the husband both maintains (R2, provides_care h w) and may chastise/restrain (R5, can_sanction h w) the same subject. That is the sub-signature matched against police-crisis and cps; the wife's own labour (R3) is implicit and runs the other way (provides_care w h), which is why care_and_sanction_same_role is restricted to care received by is_subject, and why care_assigned_by_sex is 'violated' rather than 'holds' (the husband's maintenance also counts as care). Pitfalls: (1) an encoder that drops R3 loses the household-labour strand and reports the wife as purely a recipient of care; (2) R4 and R7 are disabilities (or_else null) and should not be lowered as sanctioned prohibitions; (3) no_standing is 'reachable' not 'holds_to_k' because before marry() the woman has standing (feme sole); the iso with the animal entries on 'cannot sue in own name' holds only post-marriage and is structural, not a claim of equal status. Rival reading: equity courts' separate estates (not encoded) gave propertied wives a partial exit from R1; recorded here, not in the rules. ADR 0009: R2 and R3 are state obligations (must-be provides_care); as per-step action obligations they filled the one action slot at every married step and made marriage unsatisfiable (care_assigned_by_sex held vacuously).

</details>
