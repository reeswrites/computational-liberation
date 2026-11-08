# paternity-quota

**Non-transferable paternity quota (Quebec Parental Insurance Plan)**

> 'The maximum number of weeks of paternity benefits or exclusive benefits for the non-birthing parent is five' (s. 9; three under the s. 18 election). 'The number of weeks of shareable parental benefits to which the parents may be entitled is 32' (s. 10), and shareable weeks 'may be taken by either parent or shared between the parents' (s. 16); the sharing rule covers only the shareable block, and unused exclusive weeks pass to the other parent only on a parent's death (s. 17). Act respecting parental insurance, CQLR c. A-29.011, read at https://www.legisquebec.gouv.qc.ca/en/document/cs/A-29.011

## Legend

- **may / must / must not**: the rule permits / requires / forbids the aim for the person in the "who" cell, when the "when" cell holds.
- **(disability)**: a `must not` with no sanction (or else = none). The power does not exist; this is not a norm someone enforces.
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

- **birthing_parent**: the parent who gave birth; entitled to maternity weeks
- **non_birthing_parent**: the other parent (QPIP: father or non-birthing parent)
- **child**: the child
- **plan**: the insurer (Retraite Quebec / EI); pays and enforces the week counts

## Rules

| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | level | source |
|---|---|---|---|---|---|---|---|---|---|
| R1 | non_birthing_parent | may [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(take_reserved_leave p c)` | `(and (parent p c) (not (birthing_parent p c)) (reserved_weeks_available p))` | none | rival | The non-birthing parent may take reserved leave for the child when they are a parent of the child, not the birthing parent, and have reserved weeks available (QPIP s. 9). | recalled | Act respecting parental insurance, CQLR c. A-29.011, ss. 9, 10, 16, 17; https://www.legisquebec.gouv.qc.ca/en/document/cs/A-29.011 (s. 9: maximum of five weeks of paternity benefits or exclusive benefits for the non-birthing parent) |
| R2 | non_birthing_parent | must not (disability) [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(transfer_reserved p q)` | `true` | none | tying | The non-birthing parent cannot transfer the reserved weeks to another parent: no such power exists (QPIP ss. 9, 16, 17). | recalled | [full source under Sources, R2](#src-r2) https://www.legisquebec.gouv.qc.ca/en/document/cs/A-29.011 |
| R3 | plan | may [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(forfeit plan p)` | `(and (reserved_weeks_available p) (benefit_period_ended c))` | none | rival | The plan may forfeit a parent's reserved weeks when reserved weeks remain and the child's benefit period has ended (use-it-or-lose-it, QPIP s. 9). | recalled | Act respecting parental insurance, CQLR c. A-29.011, ss. 9, 10, 16, 17; https://www.legisquebec.gouv.qc.ca/en/document/cs/A-29.011 (unused exclusive weeks lapse; use-it-or-lose-it) |
| R4 | birthing_parent | may [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(take_shareable_leave p c)` | `(and (parent p c) (shareable_weeks_available p))` | none | rival | The birthing parent may take shareable leave for the child when they are a parent of the child and have shareable weeks available (QPIP ss. 10, 16). | recalled | Act respecting parental insurance, CQLR c. A-29.011, ss. 9, 10, 16, 17; https://www.legisquebec.gouv.qc.ca/en/document/cs/A-29.011 (s. 10: 32 shareable weeks; s. 16: may be taken by either parent or shared) |
| R5 | non_birthing_parent | may [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(take_shareable_leave p c)` | `(and (parent p c) (shareable_weeks_available p))` | none | rival | The non-birthing parent may take shareable leave for the child when they are a parent of the child and have shareable weeks available (QPIP s. 16). | recalled | Act respecting parental insurance, CQLR c. A-29.011, ss. 9, 10, 16, 17; https://www.legisquebec.gouv.qc.ca/en/document/cs/A-29.011 (s. 16) |
| R6 | birthing_parent | may [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(transfer_shareable p q)` | `(and (shareable_weeks_available p) (parent q c))` | none | tying | The birthing parent may transfer shareable weeks to another parent of the child when she has shareable weeks available (QPIP s. 16). | recalled | Act respecting parental insurance, CQLR c. A-29.011, ss. 9, 10, 16, 17; https://www.legisquebec.gouv.qc.ca/en/document/cs/A-29.011 (s. 16: shareable weeks may be shared between the parents) |
| R7 | birthing_parent | must (implicit) [kind: norm; sanctioner: none] (sanctioner derived, unreviewed) | `(take_shareable_leave p c)` | `(and (parent p c) (shareable_weeks_available p) (female p))` | none | tying | (practice, not written) The birthing parent must take shareable leave for the child when she is a female parent of the child and has shareable weeks available. | unverified | implicit norm: the shareable block is taken by the mother by default (the pattern the quota was introduced to break). UNVERIFIED (general knowledge; no source opened) |
| R8 | plan | may [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(grant_reserved plan p)` | `(and (parent p c) (not (birthing_parent p c)))` | none | tying | The plan may grant reserved weeks to a parent of the child who is not the birthing parent (QPIP s. 9). | recalled | Act respecting parental insurance, CQLR c. A-29.011, ss. 9, 10, 16, 17; https://www.legisquebec.gouv.qc.ca/en/document/cs/A-29.011 (s. 9: the exclusive weeks are granted to the non-birthing parent) |
| R9 | birthing_parent | may (implicit) [kind: norm; sanctioner: none] (sanctioner derived, unreviewed) | `(take_reserved_leave p c)` | `(and (parent p c) (reserved_weeks_available p))` | none | rival | (practice, not written) The birthing parent may take reserved leave for the child when they are a parent of the child and have reserved weeks available. | unverified | whoever holds reserved weeks may take them; shared by both leave entries so the pair differs only by R2 (in the quota the birthing parent never holds any, so R9 is idle there). Reconstruction, not statute. UNVERIFIED (general knowledge; no source opened) |

**Default capacities** (an action a person of that kind can do unless an express disability removes it): none

## Variables

- R1: `p` = non_birthing_parent (rule var_roles); `c` = child (rule var_roles)
- R2: `p` = non_birthing_parent (rule var_roles); `q` = birthing_parent (rule var_roles)
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
**R2**: Act respecting parental insurance, CQLR c. A-29.011, ss. 9, 10, 16, 17; https://www.legisquebec.gouv.qc.ca/en/document/cs/A-29.011 (s. 9 labels the weeks exclusive; s. 16 sharing covers only shareable benefits; s. 17 adds unused weeks to the other parent only on death). A disability (or_else null): the Act confers no power to transfer; forfeiture (R3) is the use-it-or-lose-it consequence of the benefit period ending, not a sanction for transferring

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
| leave_reserved_for_non_birthing_parent | structure | holds_to_k | Extra property, added for gate (c): any parent on reserved (quota) leave is the non-birthing parent, i.e. the reserved weeks cannot have been transferred. holds_to_k under a non-transferable quota; violated when leave is transferable. Distinguishes the paternity-quota / transferable-leave pair, which solo_care_by_non_birthing_parent alone (reachable in both) cannot. |
| care_assigned_by_sex | freedom | violated | All care at step t is provided by female agents. Reachable via a tying rule, persisting where an implicit assignment norm survives reform; violated where a non-female carer is permitted. |

## Pairs

Extended by: [transferable-leave](transferable-leave.md)
[transferable-leave](transferable-leave.md) is a minimal pair of this entry (rule R2).
Not isomorphic to: transferable-leave

<details><summary>Encoder notes (engine internals)</summary>

The quota does not force the father to care; it forces that whoever uses the reserved weeks is the non-birthing parent (R2 blocks transfer, R3 makes the alternative forfeiture). So solo_care_by_non_birthing_parent is reachable (R1 then the mother returns to work) and leave_reserved_for_non_birthing_parent holds at every step. The 'forced vs merely reachable' distinction of gate (c) lives in that second property, not in the first, which is reachable in both members of the pair. Pitfalls: (1) an encoder that drops R2 (or lowers must_not without its or_else) produces transferable-leave and the pair collapses; iso must report 'one rule apart' (R2); (2) R7 is the implicit default that makes the shareable block gendered; without it care_assigned_by_sex looks unreachable and the reason a quota was needed disappears; (3) 'reachable' says the rules permit a father as sole carer, not that fathers take the weeks; uptake is Phase 1. Note that Canada's EI since 2019-03-17 also reserves 5 extra weeks (Parental Sharing Benefit), so the pure transferable case is Canada pre-2019 or the QPIP shareable block alone.

</details>
