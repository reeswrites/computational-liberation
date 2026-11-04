# mwpa-creditor-exemption

**Married women's property, 1839-50 form: creditor exemption only (dark twin; Capture per ADR 0016)**

> The 1839-1850 acts 'generally contained nothing more than statements exempting married women's property from the debts of husbands', passed after the panics (Chused 1984, citing Chused 1983). Mississippi's 1839 act shielded (slave) property from husbands' creditors; Khan 1996 excludes it as debt relief. Both via plans/backtest-mwpa.md.

## Roles

- **husband**: the husband; the legal person the marriage keeps
- **wife**: the feme covert; her legal existence is suspended during marriage
- **creditor**: a creditor of the husband

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
| R10 (added) | creditor | may (implicit) | `(attach c w)` | `(married h w)` | none | rival | (practice, not written) A creditor may attach the wife's property when she is married (it reaches what the husband holds). | implicit baseline: a husband's creditors reach the property the husband holds, w... |
| R11 (added) | creditor | must not (disability) | `(attach c w)` | `(and (married h w) (acquired_property w))` | none | tying | A creditor cannot attach the wife's property while she is married and has acquired property: no such power exists (Chused 1984). | Chused 1984 (https://core.ac.uk/download/230496986.pdf [F, via plans/backtest-mw... |
| R12 (added) | husband | may (implicit) | `(transfer_to_wife h w)` | `(married h w)` | none | tying | (practice, not written) The husband may transfer property to his wife when they are married (Chused 1984). | implicit: the transfer vehicle the exemption invites (conveyance to the wife, in... https://core.ac.uk/download/230496986.pdf |

**Default capacities** (enabled unless an express disability bars them): leave, sue, contract

## Expected properties

| property | kind | expected | meaning |
|---|---|---|---|
| subject_cannot_exit | freedom | reachable | No exit action is available to the subject, or every exit is sanctioned. scope=interaction: exit from the c... |
| care_and_sanction_same_role | structure | holds_to_k | Whoever provides care to a subject also holds sanction power over that subject (care + control bundled in o... |
| financial_dependence | freedom | holds_to_k | Every subject (married woman) lacks any economic resource under her own control: she neither holds separate... |
| financial_dependence_unpropertied | freedom | holds_to_k | Every subject who has acquired no property by gift or inheritance lacks any economic resource under her own... |
| cannot_contract | freedom | holds_to_k | No subject may contract in her own name. holds_to_k under coverture (R7 disability); violated once a sole-t... |
| no_standing | freedom | reachable | No role may start a claim whose condition refers to the subject's interest and whose effect changes the sub... |
| double_burden | failure_mode | unreachable_open | Partial reform (no mode) check for the MWPA chain (filed as displacement (DI) until 2026-11-04; ADR 0016's... |
| creditor_shield | failure_mode | reachable | Capture check (filed as dark twin (DT) until ADR 0016, 2026-11-03): a husband has conveyed property to his... |
| backlash | failure_mode | unreachable_open | Backlash (BL) check (filed Erosion 2026-11-03 by ADR 0016, reverted 2026-11-04 by its council pass: the bra... |

## Pairs

Extends [coverture-household](coverture-household.md); one line per change:
- R10 added: (practice, not written) A creditor may attach the wife's property when she is married (it reaches what the husband holds).
- R11 added: A creditor cannot attach the wife's property while she is married and has acquired property: no such power exists (Chused 1984).
- R12 added: (practice, not written) The husband may transfer property to his wife when they are married (Chused 1984).
- roles added: creditor
- fluents changed: is_subject, female, can_sanction, can_exit, has_standing, married, controls_property, controls_own_property, owns_earnings, can_contract, acquired_property, earns
- fluents added: transferred, narrowed, can_attach
- actions added: attach, transfer_to_wife
- fields overridden: expected_properties, isomorphic_to, not_isomorphic_to, not_isomorphic_to_control, minimal_pair_of, initial, initial_free
Minimal pair of [coverture-household](coverture-household.md), differing in rule R10,R11,R12; the pair differs on property creditor_shield.
[mwpa-property](mwpa-property.md) is a minimal pair of this entry (rule R1->R13).

## Notes

DARK TWIN (DT; relabelled Capture by ADR 0016, 2026-11-03, verdicts unchanged) of the property act, encoded as the plan says: the creditor may not reach the wife's acquired property (R11) but the husband's management (R1) stands, so nothing on the wife's side changes. PREREGISTERED (2026-11-03, before any run): financial_dependence and financial_dependence_unpropertied holds_to_k (unchanged from coverture); creditor_shield REACHABLE (marry, transfer_to_wife: the husband's property sits in his wife's name, under his management, beyond his creditors); no_standing reachable, cannot_contract holds, double_burden open, backlash open (no court here). Distance 3 from coverture (R10 baseline, R11 exemption, R12 conveyance): not a one-rule pair; R10 exists only so that can_attach is a granted power the exemption removes rather than a constant. Displacement: the plan names no burden moving to another role in this wave; none is encoded.
