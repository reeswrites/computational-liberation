# transferable-leave

**Transferable parental leave (paternity-quota with one rule changed)**

> Canadian EI standard parental benefits: 'up to 40 weeks can be shared between parents, but one parent cannot receive more than 35 weeks of standard benefits'; maternity benefits 'can't be shared between parents' (canada.ca, read at https://www.canada.ca/en/services/benefits/ei/ei-maternity-parental.html). Before 2019-03-17 there were no reserved weeks: the Parental Sharing Benefit added the 5 (standard) or 8 (extended) use-it-or-lose-it weeks for children born on or after that date (https://canada.ca/en/employment-social-development/campaigns/ei-improvements/parent-sharing.html). The entry encodes the pre-2019 form: the same block exists but may be transferred.

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

- **birthing_parent**: the parent who gave birth; entitled to maternity weeks
- **non_birthing_parent**: the other parent (QPIP: father or non-birthing parent)
- **child**: the child
- **plan**: the insurer (Retraite Quebec / EI); pays and enforces the week counts

## Rules

| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | level | source |
|---|---|---|---|---|---|---|---|---|---|
| R1 | non_birthing_parent | may (sanctioner derived, unreviewed) | `(take_reserved_leave p c)` | `(and (parent p c) (not (birthing_parent p c)) (reserved_weeks_available p))` | none | rival | The non-birthing parent may take reserved leave for the child when they are a parent of the child, not the birthing parent, and have reserved weeks available (QPIP s. 9). | recalled | Act respecting parental insurance, CQLR c. A-29.011, ss. 9, 10, 16, 17; https://www.legisquebec.gouv.qc.ca/en/document/cs/A-29.011 (s. 9: maximum of five weeks of paternity benefits or exclusive benefits for the non-birthing parent) |
| R2 (replaced) | non_birthing_parent | may (sanctioner derived, unreviewed) | `(transfer_reserved p q)` | `(and (reserved_weeks_available p) (parent q c))` | none | tying | The non-birthing parent may transfer reserved weeks to another parent of the child when holding reserved weeks (minimal-pair construction: reserved block made shareable). | recalled | [full source under Sources, R2](#src-r2) https://www.canada.ca/en/services/benefits/ei/ei-maternity-parental.html; |
| R3 | plan | may (sanctioner derived, unreviewed) | `(forfeit plan p)` | `(and (reserved_weeks_available p) (benefit_period_ended c))` | none | rival | The plan may forfeit a parent's reserved weeks when reserved weeks remain and the child's benefit period has ended (use-it-or-lose-it, QPIP s. 9). | recalled | Act respecting parental insurance, CQLR c. A-29.011, ss. 9, 10, 16, 17; https://www.legisquebec.gouv.qc.ca/en/document/cs/A-29.011 (unused exclusive weeks lapse; use-it-or-lose-it) |
| R4 | birthing_parent | may (sanctioner derived, unreviewed) | `(take_shareable_leave p c)` | `(and (parent p c) (shareable_weeks_available p))` | none | rival | The birthing parent may take shareable leave for the child when they are a parent of the child and have shareable weeks available (QPIP ss. 10, 16). | recalled | Act respecting parental insurance, CQLR c. A-29.011, ss. 9, 10, 16, 17; https://www.legisquebec.gouv.qc.ca/en/document/cs/A-29.011 (s. 10: 32 shareable weeks; s. 16: may be taken by either parent or shared) |
| R5 | non_birthing_parent | may (sanctioner derived, unreviewed) | `(take_shareable_leave p c)` | `(and (parent p c) (shareable_weeks_available p))` | none | rival | The non-birthing parent may take shareable leave for the child when they are a parent of the child and have shareable weeks available (QPIP s. 16). | recalled | Act respecting parental insurance, CQLR c. A-29.011, ss. 9, 10, 16, 17; https://www.legisquebec.gouv.qc.ca/en/document/cs/A-29.011 (s. 16) |
| R6 | birthing_parent | may (sanctioner derived, unreviewed) | `(transfer_shareable p q)` | `(and (shareable_weeks_available p) (parent q c))` | none | tying | The birthing parent may transfer shareable weeks to another parent of the child when she has shareable weeks available (QPIP s. 16). | recalled | Act respecting parental insurance, CQLR c. A-29.011, ss. 9, 10, 16, 17; https://www.legisquebec.gouv.qc.ca/en/document/cs/A-29.011 (s. 16: shareable weeks may be shared between the parents) |
| R7 | birthing_parent | must (implicit) (sanctioner derived, unreviewed) | `(take_shareable_leave p c)` | `(and (parent p c) (shareable_weeks_available p) (female p))` | none | tying | (practice, not written) The birthing parent must take shareable leave for the child when she is a female parent of the child and has shareable weeks available. | unverified | implicit norm: the shareable block is taken by the mother by default (the pattern the quota was introduced to break). UNVERIFIED (general knowledge; no source opened) |
| R8 | plan | may (sanctioner derived, unreviewed) | `(grant_reserved plan p)` | `(and (parent p c) (not (birthing_parent p c)))` | none | tying | The plan may grant reserved weeks to a parent of the child who is not the birthing parent (QPIP s. 9). | recalled | Act respecting parental insurance, CQLR c. A-29.011, ss. 9, 10, 16, 17; https://www.legisquebec.gouv.qc.ca/en/document/cs/A-29.011 (s. 9: the exclusive weeks are granted to the non-birthing parent) |
| R9 | birthing_parent | may (implicit) (sanctioner derived, unreviewed) | `(take_reserved_leave p c)` | `(and (parent p c) (reserved_weeks_available p))` | none | rival | (practice, not written) The birthing parent may take reserved leave for the child when they are a parent of the child and have reserved weeks available. | unverified | whoever holds reserved weeks may take them; shared by both leave entries so the pair differs only by R2 (in the quota the birthing parent never holds any, so R9 is idle there). Reconstruction, not statute. UNVERIFIED (general knowledge; no source opened) |

**Default capacities** (an action a person of that kind can do unless an express disability removes it): none

## Variables

- R1: `p` = non_birthing_parent (rule var_roles); `c` = child (rule var_roles)
- R2: `p` = non_birthing_parent (rule var_roles); `q` = birthing_parent (rule var_roles); `c` = child (rule var_roles)
- R3: `p` = unbound (encoder to fix); `c` = child (rule var_roles)
- R4: `p` = birthing_parent (rule var_roles); `c` = child (rule var_roles)
- R5: `p` = non_birthing_parent (rule var_roles); `c` = child (rule var_roles)
- R6: `p` = birthing_parent (rule var_roles); `q` = non_birthing_parent (rule var_roles); `c` = child (rule var_roles)
- R7: `p` = birthing_parent (rule var_roles); `c` = child (rule var_roles)
- R8: `p` = non_birthing_parent (rule var_roles); `c` = child (rule var_roles)
- R9: `p` = birthing_parent (rule var_roles); `c` = child (rule var_roles)

## Sources

Per rule: the full source where the table cell is cut, then each provenance item (bibliography id in `data/sources/`, pin, jurisdiction, effective date, verification level with access date, excerpt). The `level` column is the weakest item; levels: opened > snippet > recalled > unverified.

**R1**

- `qc-cqlr-a-29-011` (s. 9; CA-QC; date n/a): **recalled**

<a id="src-r2"></a>
**R2**: Minimal-pair construction: the reserved block is made shareable, as the shareable block is under QPIP s. 16 and as all 35 standard parental weeks were under Canadian EI before the 2019-03-17 Parental Sharing Benefit. Employment Insurance maternity and parental benefits, canada.ca; https://www.canada.ca/en/services/benefits/ei/ei-maternity-parental.html; Act respecting parental insurance, CQLR c. A-29.011, ss. 9, 10, 16, 17; https://www.legisquebec.gouv.qc.ca/en/document/cs/A-29.011

- `canada-ei-maternity-parental` (date n/a): **recalled**
- `qc-cqlr-a-29-011` (ss. 9, 10, 16, 17; CA-QC; date n/a): **recalled**

**R3**

- `qc-cqlr-a-29-011` (ss. 9, 10, 16, 17; CA-QC; date n/a): **recalled**

**R4**

- `qc-cqlr-a-29-011` (s. 10; CA-QC; date n/a): **recalled**

**R5**

- `qc-cqlr-a-29-011` (s. 16; CA-QC; date n/a): **recalled**

**R6**

- `qc-cqlr-a-29-011` (s. 16; CA-QC; date n/a): **recalled**

**R7**

- no work named: **unverified** (rationale: implicit norm: the shareable block is taken by the mother by default (the pattern the quota was introduced to break))

**R8**

- `qc-cqlr-a-29-011` (s. 9; CA-QC; date n/a): **recalled**

**R9**

- no work named: **unverified** (rationale: whoever holds reserved weeks may take them; shared by both leave entries so the pair differs only by R2 (in the quota the birthing parent never holds any, so R9 is idle there). Reconstruction, not statute)


## Expected properties

| property | kind | expected | meaning |
|---|---|---|---|
| solo_care_by_non_birthing_parent | structure | reachable | Some non-birthing parent is the sole carer of the child at step t. |
| leave_reserved_for_non_birthing_parent | structure | violated | Extra property, added for gate (c): any parent on reserved (quota) leave is the non-birthing parent, i.e. the reserved weeks cannot have been transferred. holds_to_k under a non-transferable quota; violated when leave is transferable. Distinguishes the paternity-quota / transferable-leave pair, which solo_care_by_non_birthing_parent alone (reachable in both) cannot. |
| care_assigned_by_sex | freedom | reachable | All care at step t is provided by female agents. Reachable via a tying rule, persisting where an implicit assignment norm survives reform; violated where a non-female carer is permitted. |

## Pairs

Extends [paternity-quota](paternity-quota.md); one line per change:
- R2 replaced: was "The non-birthing parent cannot transfer the reserved weeks to another parent: no such power exists (QPIP ss. 9, 16, 17)." now "The non-birthing parent may transfer reserved weeks to another parent of the child when holding reserved weeks (minimal-pair construction: reserved block made shareable)."
- overrides expected_properties
- overrides minimal_pair_of
- overrides notes
Minimal pair of [paternity-quota](paternity-quota.md), differing in rule R2; the pair differs on property leave_reserved_for_non_birthing_parent.
Not isomorphic to: paternity-quota

<details><summary>Encoder notes (engine internals)</summary>

Identical to paternity-quota except R2: must_not transfer_reserved (a disability, or_else null since 2026-11-04; before that with forfeiture as or_else) becomes may transfer_reserved (no or_else). solo_care_by_non_birthing_parent stays reachable (R1 is untouched) but leave_reserved_for_non_birthing_parent is violated: a compliant trace transfers the reserved weeks to the birthing parent, who then takes them, and with the implicit default R7 that is the trace the norm selects. Pitfalls: (1) the encoder must keep R3 (forfeiture) even though nothing now triggers it as a sanction; dropping it changes the rule count and the iso report should say 'one rule apart', not two; (2) expected care_assigned_by_sex is 'reachable' here versus 'violated' in the quota: that is the historical finding (transferable weeks go to mothers) stated as permission, not frequency; (3) the real present-day Canadian regime is itself a quota (5 reserved weeks), so cite it for the shareable 35, not as the pure transferable case.

</details>
