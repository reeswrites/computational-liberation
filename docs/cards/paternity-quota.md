# paternity-quota

**Non-transferable paternity quota (Quebec Parental Insurance Plan)**

> 'The maximum number of weeks of paternity benefits or exclusive benefits for the non-birthing parent is five' (s. 9; three under the s. 18 election). 'The number of weeks of shareable parental benefits to which the parents may be entitled is 32' (s. 10), and shareable weeks 'may be taken by either parent or shared between the parents' (s. 16); the sharing rule covers only the shareable block, a...

## Roles

- **birthing_parent**: the parent who gave birth; entitled to maternity weeks
- **non_birthing_parent**: the other parent (QPIP: father or non-birthing parent)
- **child**: the child
- **plan**: the insurer (Retraite Quebec / EI); pays and enforces the week counts

## Rules

| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | source |
|---|---|---|---|---|---|---|---|---|
| R1 | non_birthing_parent | may | `(take_reserved_leave p c)` | `(and (parent p c) (not (birthing_parent p c)) (reserved_weeks_available p))` | none | rival | The non-birthing parent may take reserved leave for the child when they are a parent of the child, not the birthing parent, and have reserved weeks available (QPIP s. 9). | Act respecting parental insurance, CQLR c. A-29.011, ss. 9, 10, 16, 17; https://... https://www.legisquebec.gouv.qc.ca/en/document/cs/A-29.011 |
| R2 | non_birthing_parent | must not | `(transfer_reserved p q)` | `true` | R3 `(forfeit plan p)` | tying | The non-birthing parent must not transfer reserved weeks to another parent at any time, or else the plan may forfeit the weeks (R3) (QPIP ss. 9, 16, 17). | Act respecting parental insurance, CQLR c. A-29.011, ss. 9, 10, 16, 17; https://... https://www.legisquebec.gouv.qc.ca/en/document/cs/A-29.011 |
| R3 | plan | may | `(forfeit plan p)` | `(and (reserved_weeks_available p) (benefit_period_ended c))` | none | rival | The plan may forfeit a parent's reserved weeks when reserved weeks remain and the child's benefit period has ended (use-it-or-lose-it, QPIP s. 9). | Act respecting parental insurance, CQLR c. A-29.011, ss. 9, 10, 16, 17; https://... https://www.legisquebec.gouv.qc.ca/en/document/cs/A-29.011 |
| R4 | birthing_parent | may | `(take_shareable_leave p c)` | `(and (parent p c) (shareable_weeks_available p))` | none | rival | The birthing parent may take shareable leave for the child when they are a parent of the child and have shareable weeks available (QPIP ss. 10, 16). | Act respecting parental insurance, CQLR c. A-29.011, ss. 9, 10, 16, 17; https://... https://www.legisquebec.gouv.qc.ca/en/document/cs/A-29.011 |
| R5 | non_birthing_parent | may | `(take_shareable_leave p c)` | `(and (parent p c) (shareable_weeks_available p))` | none | rival | The non-birthing parent may take shareable leave for the child when they are a parent of the child and have shareable weeks available (QPIP s. 16). | Act respecting parental insurance, CQLR c. A-29.011, ss. 9, 10, 16, 17; https://... https://www.legisquebec.gouv.qc.ca/en/document/cs/A-29.011 |
| R6 | birthing_parent | may | `(transfer_shareable p q)` | `(and (shareable_weeks_available p) (parent q c))` | none | tying | The birthing parent may transfer shareable weeks to another parent of the child when she has shareable weeks available (QPIP s. 16). | Act respecting parental insurance, CQLR c. A-29.011, ss. 9, 10, 16, 17; https://... https://www.legisquebec.gouv.qc.ca/en/document/cs/A-29.011 |
| R7 | birthing_parent | must (implicit) | `(take_shareable_leave p c)` | `(and (parent p c) (shareable_weeks_available p) (female p))` | none | tying | (practice, not written) The birthing parent must take shareable leave for the child when she is a female parent of the child and has shareable weeks available. | implicit norm: the shareable block is taken by the mother by default (the patter... |
| R8 | plan | may | `(grant_reserved plan p)` | `(and (parent p c) (not (birthing_parent p c)))` | none | tying | The plan may grant reserved weeks to a parent of the child who is not the birthing parent (QPIP s. 9). | Act respecting parental insurance, CQLR c. A-29.011, ss. 9, 10, 16, 17; https://... https://www.legisquebec.gouv.qc.ca/en/document/cs/A-29.011 |
| R9 | birthing_parent | may (implicit) | `(take_reserved_leave p c)` | `(and (parent p c) (reserved_weeks_available p))` | none | rival | (practice, not written) The birthing parent may take reserved leave for the child when they are a parent of the child and have reserved weeks available. | whoever holds reserved weeks may take them; shared by both leave entries so the... |

**Default capacities** (enabled unless an express disability bars them): none

## Expected properties

| property | kind | expected | meaning |
|---|---|---|---|
| solo_care_by_non_birthing_parent | structure | reachable | Some non-birthing parent is the sole carer of the child at step t. |
| leave_reserved_for_non_birthing_parent | structure | holds_to_k | Extra property, added for gate (c): any parent on reserved (quota) leave is the non-birthing parent, i.e. t... |
| care_assigned_by_sex | freedom | violated | All care at step t is provided by female agents. Reachable via a tying rule, persisting where an implicit a... |

## Pairs

Extended by: [transferable-leave](transferable-leave.md)
[transferable-leave](transferable-leave.md) is a minimal pair of this entry (rule R2).
Not isomorphic to: transferable-leave

## Notes

The quota does not force the father to care; it forces that whoever uses the reserved weeks is the non-birthing parent (R2 blocks transfer, R3 makes the alternative forfeiture). So solo_care_by_non_birthing_parent is reachable (R1 then the mother returns to work) and leave_reserved_for_non_birthing_parent holds at every step. The 'forced vs merely reachable' distinction of gate (c) lives in that second property, not in the first, which is reachable in both members of the pair. Pitfalls: (1) an encoder that drops R2 (or lowers must_not without its or_else) produces transferable-leave and the pair collapses; iso must report 'one rule apart' (R2); (2) R7 is the implicit default that makes the shareable block gendered; without it care_assigned_by_sex looks unreachable and the reason a quota was needed disappears; (3) 'reachable' says the rules permit a father as sole carer, not that fathers take the weeks; uptake is Phase 1. Note that Canada's EI since 2019-03-17 also reserves 5 extra weeks (Parental Sharing Benefit), so the pure transferable case is Canada pre-2019 or the QPIP shareable block alone.
