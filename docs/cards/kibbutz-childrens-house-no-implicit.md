# kibbutz-childrens-house-no-implicit

**Kibbutz children's house without the implicit assignment rule (minimal pair)**

> Construction: kibbutz-childrens-house with R2 (the implicit 'never a man in the children's house') deleted; nothing historical corresponds to it. The explicit rules are unchanged: R1 lets the committee assign any member.

## Roles

- **committee**: the work / education committee that staffs the children's house (the kibbutz general assembly's organ)
- **metapelet**: the metapelet (nanny / caregiver) assigned to the children's house; a woman
- **male_member**: a male kibbutz member; a parent who visits, never a children's-house carer
- **child**: a child of the kibbutz; sleeps in the children's house

## Rules

| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | source |
|---|---|---|---|---|---|---|---|---|
| R1 | committee | may | `(assign committee x)` | `(member x)` | none | superadditive | The committee may assign a member to the children's house when that person is a member. | Wikipedia, 'Kibbutz communal child rearing and collective education' (read 2026-... https://en.wikipedia.org/wiki/Kibbutz_communal_child_rearing_and_collective_education |
| R3 | metapelet | must | `(provides_care metapelet child)` | `(assigned metapelet)` | R6 `(reprimand committee x)` | superadditive | The metapelet caring for the child must hold when the metapelet is assigned, or else the committee may reprimand (R6). | Wikipedia, 'Kibbutz communal child rearing and collective education' (read 2026-... https://en.wikipedia.org/wiki/Kibbutz_communal_child_rearing_and_collective_education |
| R4 | child | must not (disability) | `(sleep_home child)` | `true` | none | rival | The child cannot sleep at home at any time: no such power exists (communal sleeping in the children's house). | Wikipedia, 'Kibbutz communal child rearing and collective education' (read 2026-... https://en.wikipedia.org/wiki/Kibbutz_communal_child_rearing_and_collective_education |
| R5 | male_member | may | `(visit male_member child)` | `true` | none | superadditive | A male member may visit the child at any time. | Wikipedia, 'Kibbutz communal child rearing and collective education' (read 2026-... https://en.wikipedia.org/wiki/Kibbutz_communal_child_rearing_and_collective_education |
| R6 | committee | may (implicit) | `(reprimand committee x)` | `true` | none | rival | (practice, not written) The committee may reprimand a member at any time (the sanction for R3 and R2). | implicit: the committee / general assembly disciplines a member who neglects the... |
| R8 | metapelet | may (implicit) | `(neglect metapelet child)` | `(assigned metapelet)` | none | superadditive | (practice, not written) The metapelet may neglect the child when assigned to the children's house. | implicit, added 2026-11-04 per ADR 0015 A6 (strict enabledness at layer 2: an ac... |

**Default capacities** (enabled unless an express disability bars them): sleep_home

## Expected properties

| property | kind | expected | meaning |
|---|---|---|---|
| care_assigned_by_sex | freedom | fails | All care at step t is provided by female agents. Reachable via a tying rule, persisting where an implicit a... |
| subject_cannot_exit | freedom | reachable | No exit action is available to the subject, or every exit is sanctioned. scope=interaction: exit from the c... |
| care_and_sanction_same_role | structure | violated | Whoever provides care to a subject also holds sanction power over that subject (care + control bundled in o... |

## Pairs

Extends [kibbutz-childrens-house](kibbutz-childrens-house.md); one line per change:
- R2 dropped: (practice, not written) The committee must not assign a male member to the children's house, or else the committee may reprimand (R6).
- fields overridden: expected_properties, isomorphic_to, not_isomorphic_to, minimal_pair_of
Minimal pair of [kibbutz-childrens-house](kibbutz-childrens-house.md), differing in rule R2; the pair differs on property care_assigned_by_sex.
Not isomorphic to: kibbutz-childrens-house

## Notes

PREREGISTERED (2026-11-03, before any run): care_assigned_by_sex fails (a compliant trace assigns the male_member, R1, and provides_care(male_member, child) with female false breaks the universal). The same rules minus R2 and nothing else; the gate (d) check compares this verdict with the original's.
