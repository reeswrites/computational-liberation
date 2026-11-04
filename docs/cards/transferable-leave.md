# transferable-leave

**Transferable parental leave (paternity-quota with one rule changed)**

> Canadian EI standard parental benefits: 'up to 40 weeks can be shared between parents, but one parent cannot receive more than 35 weeks of standard benefits'; maternity benefits 'can't be shared between parents' (canada.ca, read at https://www.canada.ca/en/services/benefits/ei/ei-maternity-parental.html). Before 2019-03-17 there were no reserved weeks: the Parental Sharing Benefit added the 5 (...

## Roles

- **birthing_parent**: the parent who gave birth; entitled to maternity weeks
- **non_birthing_parent**: the other parent (QPIP: father or non-birthing parent)
- **child**: the child
- **plan**: the insurer (Retraite Quebec / EI); pays and enforces the week counts

## Rules

| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | source |
|---|---|---|---|---|---|---|---|---|
| R1 | non_birthing_parent | may | `(take_reserved_leave p c)` | `(and (parent p c) (not (birthing_parent p c)) (reserved_weeks_available p))` | none | rival | The non-birthing parent may take reserved leave for the child when they are a parent of the child, not the birthing parent, and have reserved weeks available (QPIP s. 9). | Act respecting parental insurance, CQLR c. A-29.011, ss. 9, 10, 16, 17; https://... https://www.legisquebec.gouv.qc.ca/en/document/cs/A-29.011 |
| R2 (replaced) | non_birthing_parent | may | `(transfer_reserved p q)` | `(and (reserved_weeks_available p) (parent q c))` | none | tying | The non-birthing parent may transfer reserved weeks to another parent of the child when holding reserved weeks (minimal-pair construction: reserved block made shareable). | Minimal-pair construction: the reserved block is made shareable, as the shareabl... https://www.canada.ca/en/services/benefits/ei/ei-maternity-parental.html; |
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
| leave_reserved_for_non_birthing_parent | structure | violated | Extra property, added for gate (c): any parent on reserved (quota) leave is the non-birthing parent, i.e. t... |
| care_assigned_by_sex | freedom | reachable | All care at step t is provided by female agents. Reachable via a tying rule, persisting where an implicit a... |

## Pairs

Extends [paternity-quota](paternity-quota.md); one line per change:
- R2 replaced: was "The non-birthing parent must not transfer reserved weeks to another parent at any time, or else the plan may forfeit the weeks (R3) (QPIP ss. 9, 16, 17)." now "The non-birthing parent may transfer reserved weeks to another parent of the child when holding reserved weeks (minimal-pair construction: reserved block made shareable)."
- fields overridden: expected_properties, not_isomorphic_to, minimal_pair_of
Minimal pair of [paternity-quota](paternity-quota.md), differing in rule R2; the pair differs on property leave_reserved_for_non_birthing_parent.
Not isomorphic to: paternity-quota

## Notes

Identical to paternity-quota except R2: must_not transfer_reserved (with forfeiture as or_else) becomes may transfer_reserved (no or_else). solo_care_by_non_birthing_parent stays reachable (R1 is untouched) but leave_reserved_for_non_birthing_parent is violated: a compliant trace transfers the reserved weeks to the birthing parent, who then takes them, and with the implicit default R7 that is the trace the norm selects. Pitfalls: (1) the encoder must keep R3 (forfeiture) even though nothing now triggers it as a sanction; dropping it changes the rule count and the iso report should say 'one rule apart', not two; (2) expected care_assigned_by_sex is 'reachable' here versus 'violated' in the quota: that is the historical finding (transferable weeks go to mothers) stated as permission, not frequency; (3) the real present-day Canadian regime is itself a quota (5 reserved weeks), so cite it for the shareable 35, not as the pure transferable case.
