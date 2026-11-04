# mwpa-property-narrowed

**Property act under narrow construction (backlash; filed Erosion by ADR 0016 on 2026-11-03, reverted by its council pass 2026-11-04: court reinstates the husband's control)**

> Courts 'narrowly construing' the married women's property acts to keep husbands' control during marriage (Chused 1984 citing Chused 1983 at 1400; the 1983 article [R] not opened). Via plans/backtest-mwpa.md.

## Roles

- **husband**: the husband; the legal person the marriage keeps
- **wife**: the feme covert; her legal existence is suspended during marriage
- **creditor**: a creditor of the husband
- **court**: a court construing the act

## Rules

| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | source |
|---|---|---|---|---|---|---|---|---|
| R2 | husband | must | `(provides_care h w)` | `(married h w)` | none | superadditive | The husband providing care to his wife must hold when they are married; no sanction is attached (Blackstone I.15). | Blackstone, Commentaries on the Laws of England, Book I ch. 15 'Of Husband and W... https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ |
| R3 | wife | must (implicit) | `(provides_care w h)` | `(married h w)` | R5 `(chastise h w)` | superadditive | (practice, not written) The wife providing care to her husband (household labour) must hold when they are married, or else the husband may chastise her (R5). | implicit norm: household labour is the wife's; not in Blackstone's text, assumed... |
| R4 | wife | must not (disability) | `(sue w)` | `(married h w)` | none | tying | The wife cannot sue in her own name while married: no such power exists (Blackstone I.15). | Blackstone, Commentaries on the Laws of England, Book I ch. 15 'Of Husband and W... https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ |
| R5 | husband | may | `(chastise h w)` | `(married h w)` | none | rival | The husband may chastise his wife (moderate correction, restraint of her liberty) when they are married (Blackstone I.15). | Blackstone, Commentaries on the Laws of England, Book I ch. 15 'Of Husband and W... https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ |
| R6 | wife | must not (disability) | `(leave w)` | `(married h w)` | none | rival | The wife cannot leave the marriage while married: no such power exists (Blackstone I.15). | Blackstone, Commentaries on the Laws of England, Book I ch. 15 'Of Husband and W... https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ |
| R7 | wife | must not (disability) | `(contract w)` | `(married h w)` | none | tying | The wife cannot contract in her own name while married: no such power exists (Blackstone I.15). | Blackstone, Commentaries on the Laws of England, Book I ch. 15 'Of Husband and W... https://wams.nyhistory.org/colonies-and-revolution/english-colonies/coverture/ |
| R10 | creditor | may (implicit) | `(attach c w)` | `(married h w)` | none | rival | (practice, not written) A creditor may attach the wife's property when she is married (it reaches what the husband holds). | implicit baseline: a husband's creditors reach the property the husband holds, w... |
| R11 | creditor | must not (disability) | `(attach c w)` | `(and (married h w) (acquired_property w))` | none | tying | A creditor cannot attach the wife's property while she is married and has acquired property: no such power exists (Chused 1984). | Chused 1984 (https://core.ac.uk/download/230496986.pdf [F, via plans/backtest-mw... |
| R12 | husband | may (implicit) | `(transfer_to_wife h w)` | `(married h w)` | none | tying | (practice, not written) The husband may transfer property to his wife when they are married (Chused 1984). | implicit: the transfer vehicle the exemption invites (conveyance to the wife, in... https://core.ac.uk/download/230496986.pdf |
| R13 | wife | may | `(hold_property w)` | `(and (married h w) (acquired_property w) (not (narrowed w)))` | none | tying | The wife may hold property in her own right when married, she has acquired property, and the act has not been narrowly construed (NY MWPA 1848). | New York Married Women's Property Act 1848 (the statute text itself not opened:... https://isnie-archive.sioe.org/assets/files/papers2007/geddes.pdf |
| R17 (added) | court | may | `(construe_narrowly court w)` | `(and (married h w) (acquired_property w))` | none | rival | The court may construe the act narrowly when the wife is married and has acquired property (Chused 1984). | Chused 1984 (https://core.ac.uk/download/230496986.pdf [F, via plans/backtest-mw... |
| R18 (added) | husband | may | `(control_property h w)` | `(and (married h w) (narrowed w))` | none | tying | The husband may control his wife's property when married and the act has been narrowly construed (R1 reinstated, Chused 1984). | R1 reinstated under narrow construction (the plan's BL encoding): Chused 1984 (h... https://core.ac.uk/download/230496986.pdf |

**Default capacities** (enabled unless an express disability bars them): leave, sue, contract

## Expected properties

| property | kind | expected | meaning |
|---|---|---|---|
| subject_cannot_exit | freedom | reachable | No exit action is available to the subject, or every exit is sanctioned. scope=interaction: exit from the c... |
| care_and_sanction_same_role | structure | holds_to_k | Whoever provides care to a subject also holds sanction power over that subject (care + control bundled in o... |
| financial_dependence | freedom | violated | Every subject (married woman) lacks any economic resource under her own control: she neither holds separate... |
| financial_dependence_unpropertied | freedom | holds_to_k | Every subject who has acquired no property by gift or inheritance lacks any economic resource under her own... |
| cannot_contract | freedom | holds_to_k | No subject may contract in her own name. holds_to_k under coverture (R7 disability); violated once a sole-t... |
| no_standing | freedom | reachable | No role may start a claim whose condition refers to the subject's interest and whose effect changes the sub... |
| double_burden | failure_mode | unreachable_open | Partial reform (no mode) check for the MWPA chain (filed as displacement (DI) until 2026-11-04; ADR 0016's... |
| creditor_shield | failure_mode | reachable | Capture check (filed as dark twin (DT) until ADR 0016, 2026-11-03): a husband has conveyed property to his... |
| backlash | failure_mode | reachable | Backlash (BL) check (filed Erosion 2026-11-03 by ADR 0016, reverted 2026-11-04 by its council pass: the bra... |

## Pairs

Extends [mwpa-property](mwpa-property.md); one line per change:
- R17 added: The court may construe the act narrowly when the wife is married and has acquired property (Chused 1984).
- R18 added: The husband may control his wife's property when married and the act has been narrowly construed (R1 reinstated, Chused 1984).
- roles added: court
- actions added: construe_narrowly
- fields overridden: expected_properties, minimal_pair_of
Minimal pair of [mwpa-property](mwpa-property.md), differing in rule R17,R18; the pair differs on property backlash.

## Notes

BACKLASH (BL) entry (backlash; filed Erosion by ADR 0016 on 2026-11-03, reverted by its council pass 2026-11-04; verdicts unchanged; see docs/reviews/2026-11-04-adr0016-council.md): mwpa-property plus a court that may construe the act narrowly (R17, sets narrowed(w)), which re-disables the wife's R13 power (its condition carries (not narrowed)) and reinstates R1 as R18 under narrowed. PREREGISTERED (2026-11-03, before any run): backlash REACHABLE (marry, construe_narrowly: the husband controls again, the wife does not); financial_dependence still VIOLATED (the court may but need not narrow, and before it does the wife holds); creditor_shield REACHABLE again (marry, transfer_to_wife, construe_narrowly: with his management reinstated the conveyance is a shield once more); everything else as mwpa-property. Distance 2 from mwpa-property (the narrowing power and the reinstated R1 are two rules). Not a chain step: a branch off mwpa-property.
