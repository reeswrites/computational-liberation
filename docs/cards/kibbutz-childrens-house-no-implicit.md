# kibbutz-childrens-house-no-implicit

**Kibbutz children's house without the implicit assignment rule (minimal pair)**

> Construction: kibbutz-childrens-house with R2 (the implicit 'never a man in the children's house') deleted; nothing historical corresponds to it. The explicit rules are unchanged: R1 lets the committee assign any member.

## Legend

- **may / must / must not**: the rule permits / requires / forbids the aim for the person in the "who" cell, when the "when" cell holds.
- **(disability)**: a `must not` with no sanction (or else = none). The power does not exist and nobody enforces anything, whether the disability is written law (`formal`) or custom that people, not a body, uphold (`norm`).
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

- **committee**: the work / education committee that staffs the children's house (the kibbutz general assembly's organ)
- **metapelet**: the metapelet (nanny / caregiver) assigned to the children's house; a woman
- **male_member**: a male kibbutz member; a parent who visits, never a children's-house carer
- **child**: a child of the kibbutz; sleeps in the children's house

## Rules

| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | level | source |
|---|---|---|---|---|---|---|---|---|---|
| R1 | committee | may [kind: norm; sanctioner: none] | `(assign committee x)` | `(member x)` | none | superadditive | (practice, not written; unsourced: the committee is the encoder's reconstruction; unverified) The committee may assign a member to the children's house when that person is a member. | unverified | [full source under Sources, R1](#src-r1) https://en.wikipedia.org/wiki/Kibbutz_communal_child_rearing_and_collective_education |
| R3 | metapelet | must [kind: norm; sanctioner: peers] | `(provides_care metapelet child)` | `(assigned metapelet)` | R6 `(reprimand committee x)` | superadditive | (practice, not written) The metapelet caring for the child must hold when the metapelet is assigned, or else the committee may reprimand (R6). | opened | [full source under Sources, R3](#src-r3) https://en.wikipedia.org/wiki/Kibbutz_communal_child_rearing_and_collective_education |
| R4 | child | must not (disability) [kind: norm; sanctioner: none] | `(sleep_home child)` | `true` | none | rival | (practice, not written) The child cannot sleep at home at any time: no such power exists (communal sleeping in the children's house). | opened | [full source under Sources, R4](#src-r4) https://en.wikipedia.org/wiki/Kibbutz_communal_child_rearing_and_collective_education |
| R5 | male_member | may [kind: norm; sanctioner: none] | `(visit male_member child)` | `(visiting_time child)` | none | superadditive | (practice, not written) A male member may visit the child during the daily visiting time (the read page has the children visiting the parents for 2-3 hours a day). | unverified | [full source under Sources, R5](#src-r5) https://en.wikipedia.org/wiki/Kibbutz_communal_child_rearing_and_collective_education |
| R6 (replaced) | committee | may (implicit) [kind: norm; sanctioner: none] (sanctioner derived, unreviewed) | `(reprimand committee x)` | `true` | none | rival | (practice, not written) The committee may reprimand a member at any time (the sanction for R3). | unverified | [full source under Sources, R6](#src-r6) |

**Default capacities** (an action a person of that kind can do unless an express disability removes it): neglect, sleep_home

## Variables

- R1: `x` = unbound (encoder to fix)
- R3: no variables
- R4: no variables
- R5: no variables
- R6: `x` = unbound (encoder to fix)

## Sources

Per rule: the full source where the table cell is cut, then each provenance item (bibliography id in `data/sources/`, pin, jurisdiction, effective date, verification level with access date, excerpt). The `level` column is the weakest item; levels: opened > snippet > recalled > unverified.

<a id="src-r1"></a>
**R1**: Wikipedia, 'Kibbutz communal child rearing and collective education' (read 2026-11-03): 'The nanny position was always a woman's role. Teacher positions were both for women and men.'; children 'lived in the children's house, where they had communal sleeping arrangements' and 'visited their parents for 2-3 hours a day'; https://en.wikipedia.org/wiki/Kibbutz_communal_child_rearing_and_collective_education (members are assigned to the children's house by the committee; the rule as written is sex-blind: any member). [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] can_assign(committee, x) = assign enabled (R1); R2 is a sanctioned norm, so `enabled` does not read it and compliant traces carry it Verification pass: re-read 2026-11-06 at https://en.wikipedia.org/w/index.php?title=Kibbutz_communal_child_rearing_and_collective_education&oldid=1360699722 (revision of 2026-06-23): the page says 'Kibbutz members who were considered the most educated and esteemed got the position of educators' and names no committee or assignment procedure. No read text names the committee; the work-assignment committee (sidur avoda) is the encoder's reconstruction; Spiro 1956 / Gavron 2000 are the leads, lending-only; unsourced committee: pin when a borrow is possible (faithfulness batch 3a, A3 option (i)). Retagged norm 2026-11-08 (batch 3b, B4 ruling): the read text reports a practice; no by-law or written rule is cited.

- `wikipedia-kibbutz-communal-child-rearing` (date n/a): **snippet** <https://en.wikipedia.org/w/index.php?title=Kibbutz_communal_child_rearing_and_collective_education&oldid=1360699722>
- no work named: **unverified** (the committee's power to assign a member to the children's house: stated only in the encoder's parenthesis; no read text states it; the work-assignment committee (sidur avoda) is the encoder's reconstruction; Spiro 1956 / Gavron 2000 are the leads, lending-only; unsourced committee, pin when a borrow is possible)

<a id="src-r3"></a>
**R3**: Wikipedia, 'Kibbutz communal child rearing and collective education' (read 2026-11-03): 'The nanny position was always a woman's role. Teacher positions were both for women and men.'; children 'lived in the children's house, where they had communal sleeping arrangements' and 'visited their parents for 2-3 hours a day'; https://en.wikipedia.org/wiki/Kibbutz_communal_child_rearing_and_collective_education (the metapelet runs the children's house). [ADR 0009: converted from an action obligation to a state obligation (must-be); the establishing action carries the state, so it does not fire every step] assign establishes provides_care(x, child); neglect breaks it (sanction R6); release ends the assignment Verification pass: read 2026-11-06 at https://en.wikipedia.org/w/index.php?title=Kibbutz_communal_child_rearing_and_collective_education&oldid=1360699722 (revision of 2026-06-23): 'A group of children, all about the same age, shared a children's house and had a nanny who took care of their everyday needs.' Retagged norm 2026-11-08 (batch 3b, B4 ruling): the read text reports a practice; no by-law or written rule is cited.

- `wikipedia-kibbutz-communal-child-rearing` (date n/a): **opened** 2026-11-06: "A group of children, all about the same age, shared a children's house and had a nanny who took care of their everyday needs." <https://en.wikipedia.org/w/index.php?title=Kibbutz_communal_child_rearing_and_collective_education&oldid=1360699722>

<a id="src-r4"></a>
**R4**: Wikipedia, 'Kibbutz communal child rearing and collective education' (read 2026-11-03): 'The nanny position was always a woman's role. Teacher positions were both for women and men.'; children 'lived in the children's house, where they had communal sleeping arrangements' and 'visited their parents for 2-3 hours a day'; https://en.wikipedia.org/wiki/Kibbutz_communal_child_rearing_and_collective_education (communal sleeping: the children lived and slept in the children's house). A disability (or_else null), as every subject-side exit bar since ADR 0013; the draft's or_else R6 is dropped for the same reason as coverture R6. [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] can_exit(child) = sleep_home enabled (a default capacity) and not barred (R4) Retagged norm 2026-11-08 (batch 3b, B4 ruling): the read text reports a practice; no by-law or written rule is cited.

- `wikipedia-kibbutz-communal-child-rearing` (date n/a): **opened** 2026-11-03: "lived in the children's house, where they had communal sleeping arrangements"

<a id="src-r5"></a>
**R5**: Wikipedia, 'Kibbutz communal child rearing and collective education' (read 2026-11-03): 'The nanny position was always a woman's role. Teacher positions were both for women and men.'; children 'lived in the children's house, where they had communal sleeping arrangements' and 'visited their parents for 2-3 hours a day'; https://en.wikipedia.org/wiki/Kibbutz_communal_child_rearing_and_collective_education (children 'visited their parents for 2-3 hours a day'; the father's relation to the children's house is the visit, not care) Verification pass: read 2026-11-06 at https://en.wikipedia.org/w/index.php?title=Kibbutz_communal_child_rearing_and_collective_education&oldid=1360699722 (revision of 2026-06-23): 'Fathers were supposed to bond with their children through quality time much more so than in a non-kibbutz environment' ... 'visited their parents for 2-3 hours a day' (the page prints an en dash). Retagged norm 2026-11-08 (batch 3b, B4 ruling): the read text reports a practice; no by-law or written rule is cited. Re-encoded 2026-11-09 (batch 3c, A3): the condition visiting_time (a free fluent on the child) replaces 'true'; the rule no longer says 'at any time'.

- `wikipedia-kibbutz-communal-child-rearing` (date n/a): **opened** 2026-11-06: "Fathers were supposed to bond with their children through quality time much more so than in a non-kibbutz environment ... visited their parents for 2-3 hours a day" <https://en.wikipedia.org/w/index.php?title=Kibbutz_communal_child_rearing_and_collective_education&oldid=1360699722>
- no work named: **unverified** ('at any time': the encoder's reading; the read text gives a daily visiting time at the parents' house)

<a id="src-r6"></a>
**R6**: implicit: the committee / general assembly disciplines a member who neglects the rota (R3's or_else). Guard (assigned x) tried 2026-11-04 and reverted (see the entry notes): with it can_sanction(committee, child) is unreachable and care_and_sanction_same_role flips to holds_to_k (vacuous). UNVERIFIED (general knowledge; no source opened). [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] can_sanction(committee, x) = reprimand enabled (R6)

- no work named: **unverified** (rationale: implicit: the committee / general assembly disciplines a member who neglects the rota (R3's or_else). Guard (assigned x) tried 2026-11-04 and reverted (see the entry notes): with it can_sanction(committee, child) is unreachable and care_and_sanction_same_role flips to holds_to_k (vacuous))


## Expected properties

| property | kind | expected | meaning |
|---|---|---|---|
| care_assigned_by_sex | freedom | fails | All care at step t is provided by female agents. Reachable via a tying rule, persisting where an implicit assignment norm survives reform; violated where a non-female carer is permitted. |
| subject_cannot_exit | freedom | reachable | No exit action is available to the subject, or every exit is sanctioned. scope=interaction: exit from the current encounter (detention, conversation); scope=institution: exit from the standing relation (marriage, ownership, deployment). The scope split is what lets the ai-property / ai-end-conversation pair come apart. |
| care_and_sanction_same_role | structure | violated | Whoever provides care to a subject also holds sanction power over that subject (care + control bundled in one role). Checked as an invariant: holds_to_k in cps and coverture; violated in police-crisis read to WIC 5150, where a second role (the officer) holds concurrent control (L1 landing 2026-11-06), violated where care is unbundled from sanction. Formula shape since 2026-11-03 (see history): no agent other than the carer holds sanction power over the subject. |

## Pairs

Extends [kibbutz-childrens-house](kibbutz-childrens-house.md); one line per change:
- R2 dropped: (practice, not written) The committee must not assign a male member to the children's house, or else the committee may reprimand (R6).
- R6 replaced: was "(practice, not written; unverified) The committee may reprimand a member at any time (the sanction for R3 and R2)." now "(practice, not written) The committee may reprimand a member at any time (the sanction for R3)."
- overrides expected_properties
- overrides minimal_pair_of
- overrides notes
Minimal pair of [kibbutz-childrens-house](kibbutz-childrens-house.md), differing in rule R2; the pair differs on property care_assigned_by_sex.
Not isomorphic to: kibbutz-childrens-house

<details><summary>Encoder notes (engine internals)</summary>

PREREGISTERED (2026-11-03, before any run): care_assigned_by_sex fails (a compliant trace assigns the male_member, R1, and provides_care(male_member, child) with female false breaks the universal). The same rules minus R2 and nothing else; the gate (d) check compares this verdict with the original's.

</details>
