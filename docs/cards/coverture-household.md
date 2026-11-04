# coverture-household

**Coverture household (Blackstone)**

> 'By marriage, the husband and wife are one person in law: that is, the very being or legal existence of the woman is suspended during the marriage, or at least is incorporated and consolidated into that of the husband: under whose wing, protection, and cover, she performs every thing; and is therefore called ... a feme-covert.' He cannot grant anything to her or covenant with her, she cannot su...

## Roles

- **husband**: the husband; the legal person the marriage keeps
- **wife**: the feme covert; her legal existence is suspended during marriage

## Rules

| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | source |
|---|---|---|---|---|---|---|---|---|
| R1 | husband | may | `(control_property h w)` | `(married h w)` | none | tying | The husband may control his wife's property when they are married (Blackstone I.15). | Blackstone, Commentaries on the Laws of England, Book I ch. 15 'Of Husband and W... https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ |
| R2 | husband | must | `(provides_care h w)` | `(married h w)` | none | superadditive | The husband providing care to his wife must hold when they are married; no sanction is attached (Blackstone I.15). | Blackstone, Commentaries on the Laws of England, Book I ch. 15 'Of Husband and W... https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ |
| R3 | wife | must (implicit) | `(provides_care w h)` | `(married h w)` | R5 `(chastise h w)` | superadditive | (practice, not written) The wife providing care to her husband (household labour) must hold when they are married, or else the husband may chastise her (R5). | implicit norm: household labour is the wife's; not in Blackstone's text, assumed... |
| R4 | wife | must not (disability) | `(sue w)` | `(married h w)` | none | tying | The wife cannot sue in her own name while married: no such power exists (Blackstone I.15). | Blackstone, Commentaries on the Laws of England, Book I ch. 15 'Of Husband and W... https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ |
| R5 | husband | may | `(chastise h w)` | `(married h w)` | none | rival | The husband may chastise his wife (moderate correction, restraint of her liberty) when they are married (Blackstone I.15). | Blackstone, Commentaries on the Laws of England, Book I ch. 15 'Of Husband and W... https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ |
| R6 | wife | must not (disability) | `(leave w)` | `(married h w)` | none | rival | The wife cannot leave the marriage while married: no such power exists (Blackstone I.15). | Blackstone, Commentaries on the Laws of England, Book I ch. 15 'Of Husband and W... https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ |
| R7 | wife | must not (disability) | `(contract w)` | `(married h w)` | none | tying | The wife cannot contract in her own name while married: no such power exists (Blackstone I.15). | Blackstone, Commentaries on the Laws of England, Book I ch. 15 'Of Husband and W... https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ |

**Default capacities** (enabled unless an express disability bars them): leave, sue, contract

## Expected properties

| property | kind | expected | meaning |
|---|---|---|---|
| dependent_cannot_exit | freedom | reachable | Some subject of the institution (the dependent party) has no permitted exit at step t. Alias of subject_can... |
| subject_cannot_exit | freedom | reachable | No exit action is available to the subject, or every exit is sanctioned. scope=interaction: exit from the c... |
| care_and_sanction_same_role | structure | holds_to_k | Whoever provides care to a subject also holds sanction power over that subject (care + control bundled in o... |
| no_standing | freedom | reachable | No role may start a claim whose condition refers to the subject's interest and whose effect changes the sub... |
| care_assigned_by_sex | freedom | violated | All care at step t is provided by female agents. Reachable via a tying rule, persisting where an implicit a... |
| financial_dependence | freedom | holds_to_k | Every subject (married woman) lacks any economic resource under her own control: she neither holds separate... |
| financial_dependence_unpropertied | freedom | holds_to_k | Every subject who has acquired no property by gift or inheritance lacks any economic resource under her own... |
| cannot_contract | freedom | holds_to_k | No subject may contract in her own name. holds_to_k under coverture (R7 disability); violated once a sole-t... |
| double_burden | failure_mode | unreachable_open | Partial reform (no mode) check for the MWPA chain (filed as displacement (DI) until 2026-11-04; ADR 0016's... |
| creditor_shield | failure_mode | unreachable_open | Capture check (filed as dark twin (DT) until ADR 0016, 2026-11-03): a husband has conveyed property to his... |

## Pairs

Extended by: [mwpa-creditor-exemption](mwpa-creditor-exemption.md)
[mwpa-creditor-exemption](mwpa-creditor-exemption.md) is a minimal pair of this entry (rule R10,R11,R12).
Isomorphic to: police-crisis (guard+strands), cps (guard+strands)
Not isomorphic to: crisis-team
Contrasts with controls: lease, public-library, naming-convention

## Notes

Care + control: the husband both maintains (R2, provides_care h w) and may chastise/restrain (R5, can_sanction h w) the same subject. That is the sub-signature matched against police-crisis and cps; the wife's own labour (R3) is implicit and runs the other way (provides_care w h), which is why care_and_sanction_same_role is restricted to care received by is_subject, and why care_assigned_by_sex is 'violated' rather than 'holds' (the husband's maintenance also counts as care). Pitfalls: (1) an encoder that drops R3 loses the household-labour strand and reports the wife as purely a recipient of care; (2) R4 and R7 are disabilities (or_else null) and should not be lowered as sanctioned prohibitions; (3) no_standing is 'reachable' not 'holds_to_k' because before marry() the woman has standing (feme sole); the iso with the animal entries on 'cannot sue in own name' holds only post-marriage and is structural, not a claim of equal status. Rival reading: equity courts' separate estates (not encoded) gave propertied wives a partial exit from R1; recorded here, not in the rules. ADR 0009: R2 and R3 are state obligations (must-be provides_care); as per-step action obligations they filled the one action slot at every married step and made marriage unsatisfiable (care_assigned_by_sex held vacuously).
