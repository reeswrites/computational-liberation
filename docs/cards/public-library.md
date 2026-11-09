# public-library

**Public library (negative control: service duty + suspension power, patron may leave)**

> The Berkeley Public Library's Patron Suspension Policy (orig. 2002-09-11, rev. 2018-11-14, Res. R18-053) aims to 'provide and maintain a welcoming and safe environment for all patrons and library staff'; 'Violation of the Library's Rules of Use Policy may warrant a suspension of library privileges'; 'Authorized library staff will instruct anyone displaying these behaviors to leave the library facility immediately'; a patron suspended for one to six months 'has the right to a hearing with the Suspension Hearing Panel'. Read at https://www.berkeleypubliclibrary.org/sites/default/files/files/inline/patron_suspension_policy_approved_14nov2018.pdf

## Legend

- **may / must / must not**: the rule permits / requires / forbids the aim for the person in the "who" cell, when the "when" cell holds.
- **(disability)**: a `must not` with no sanction (or else = none). The power does not exist and nobody enforces anything, whether the disability is written law (`formal`) or custom that people, not a body, uphold (`norm`).
- **(implicit)**: not written as a rule in the cited source; reconstructed from it or from practice. The source cell gives the rationale, not a quotation.
- **or else**: the sanction rule that applies on breach (the rule id and its aim).
- **strand**: `rival` = an input only one party can supply at a time; `superadditive` = a good that exists only as a product of the bundle; `tying` = glued to the bundle by law, wages or norm with no production link.
- **default capacity**: an action a person of that kind can do unless an express disability removes it, as opposed to a power that exists only because a rule grants it. The "Default capacities" list under the table names the bearer role for each.
- **free fluent**: an input the model varies, not set by any rule; a when cell that names one waits on a fact the world supplies (a report arrives, it is visiting time), not on something a role does. Listed with its gloss under "Free fluents" below the table.
- **(replaced) / (added)** after a row id: this entry `extends` another, and the row replaces the base entry's row of that id, or adds one; the base card holds the original wording.
- **linked to no rule**: a sanction-shaped rule (such as `may reprimand`) that no row's or else points at; it fires on no breach and is kept for the record only.
- **k**: the step bound; verdicts such as `holds_to_k` mean "holds for every trace of at most k steps".
- **Variables**: letters in the aim and when cells are bound to roles in the Variables section; "unbound (encoder to fix)" means no binding was recorded.
- **kind**: what sort of rule it is. `formal` = written law or contract (the default, always shown so it can be questioned); `norm` = an unwritten practice that others enforce; `strategy` = a regularity nobody enforces. A `strategy` rule written as `must` is still read by the engine as a duty under strict compliance, though nobody enforces it.
- **sanctioner**: who enforces the or-else: `state`, `institution`, `peers`, `family`, `self`, or `none` (no or-else, so nobody).
- **sanctioner derived, unreviewed**: the rule's `sanctioner` was derived once by the 2026-11-07 migration from the or-else target's role and has not been hand-reviewed yet (plans/informal-rules.md D1).

## Roles

- **librarian**: library staff; serves and may suspend
- **patron**: a library user; the counterparty, not a dependent

## Rules

| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | level | source |
|---|---|---|---|---|---|---|---|---|---|
| R1 | librarian | may [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(open_library lb)` | `(not (open lb))` | none | tying | The librarian may open the library when it is not open. | unverified | opening hours. UNVERIFIED (general knowledge; no source opened) |
| R2 | librarian | must [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(served lb p)` | `(and (open lb) (present p) (not (suspended p)))` | none | superadditive | The patron being served must hold when the library is open and the patron is present and not suspended (Berkeley Patron Suspension Policy). | unverified | [full source under Sources, R2](#src-r2) https://www.berkeleypubliclibrary.org/sites/default/files/files/inline/patron_suspension_policy_approved_14nov2018.pdf |
| R3 | librarian | may [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(suspend lb p)` | `(and (present p) (disruptive p))` | none | rival | The librarian may suspend the patron when the patron is present and continues to be disruptive after being warned (Berkeley Patron Suspension Policy B.2). | opened | [full source under Sources, R3](#src-r3) https://www.berkeleypubliclibrary.org/sites/default/files/files/inline/patron_suspension_policy_approved_14nov2018.pdf |
| R4 | patron | may [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(leave p)` | `true` | none | rival | The patron may leave at any time. | unverified | a patron is free to leave at any time; nothing in the policy holds them. UNVERIFIED (general knowledge; no source opened). [ADR 0013: power fluents are derived from rule enabledness; this rule is what the derived fluent reads] can_exit(p) = leave enabled |
| R5 | patron | may [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(enter p)` | `(and (open lb) (not (suspended p)))` | none | tying | The patron may enter when the library is open and the patron is not suspended. | opened | [full source under Sources, R5](#src-r5) https://www.berkeleypubliclibrary.org/sites/default/files/files/inline/patron_suspension_policy_approved_14nov2018.pdf |
| R6 | patron | may [kind: formal; sanctioner: none] (sanctioner derived, unreviewed) | `(borrow p)` | `(and (present p) (not (suspended p)))` | none | tying | The patron may borrow when present and not suspended. | unverified | library privileges. UNVERIFIED (general knowledge; no source opened) |

**Free fluents** (inputs the model varies, not set by any rule; see the Legend):

- `disruptive(patron)`: p continues to be disruptive after the B.1 warning (Berkeley policy B.2 'Continued disruption'; the warning step is not encoded; exogenous); no action in this institution sets it.

**Default capacities** (an action a person of that kind can do unless an express disability removes it; these replaced the implicit `may ... when true` rows that once encoded them, README revision 4):

- `leave`: A patron (the who cell of R4; the action parameter is untyped) may leave unless a rule forbids it; rule rows naming it: R4 (may).

## Variables

- R1: `lb` = librarian (rule var_roles)
- R2: `lb` = librarian (rule var_roles); `p` = patron (rule var_roles)
- R3: `lb` = librarian (rule var_roles); `p` = patron (rule var_roles)
- R4: `p` = patron (rule var_roles)
- R5: `p` = patron (rule var_roles); `lb` = librarian (rule var_roles)
- R6: `p` = patron (rule var_roles)

## Sources

Per rule: the full source where the table cell is cut, then each provenance item (bibliography id in `data/sources/`, pin, jurisdiction, effective date, verification level with access date, excerpt). The `level` column is the weakest item; levels: opened > snippet > recalled > unverified.

**R1**

- no work named: **unverified** (rationale: opening hours)

<a id="src-r2"></a>
**R2**: Berkeley Public Library, Patron Suspension Policy (orig. 2002-09-11, rev. 2018-11-14, Res. R18-053): the Library aims to 'provide and maintain a welcoming and safe environment for all patrons and library staff'; 'Violation of the Library's Rules of Use Policy may warrant a suspension of library privileges'; 'Authorized library staff will instruct anyone displaying these behaviors to leave the library facility immediately'; https://www.berkeleypubliclibrary.org/sites/default/files/files/inline/patron_suspension_policy_approved_14nov2018.pdf (service to all patrons is the policy's premise; the duty to serve is read from it, not stated as such: UNVERIFIED as a rule). [ADR 0009: converted from an action obligation to a state obligation (must-be); the establishing action carries the state, so it does not fire every step] enter establishes served; serve restores it, refuse_service breaks it Verification pass: read 2026-11-06 at https://www.berkeleypubliclibrary.org/sites/default/files/files/inline/patron_suspension_policy_approved_14nov2018.pdf: 'In order to provide and maintain a welcoming and safe environment for all patrons and library staff'.

- `berkeley-public-library-2018-patron-suspension-policy` (p. 1; date n/a): **opened** 2026-11-06: "In order to provide and maintain a welcoming and safe environment for all patrons and library staff" <https://www.berkeleypubliclibrary.org/sites/default/files/files/inline/patron_suspension_policy_approved_14nov2018.pdf>
- no work named: **unverified** (the rule (a duty to serve) is read from the policy's premise, not stated: UNVERIFIED as a rule)

<a id="src-r3"></a>
**R3**: Berkeley Public Library, Patron Suspension Policy (orig. 2002-09-11, rev. 2018-11-14, Res. R18-053): the Library aims to 'provide and maintain a welcoming and safe environment for all patrons and library staff'; 'Violation of the Library's Rules of Use Policy may warrant a suspension of library privileges'; 'Authorized library staff will instruct anyone displaying these behaviors to leave the library facility immediately'; https://www.berkeleypubliclibrary.org/sites/default/files/files/inline/patron_suspension_policy_approved_14nov2018.pdf (violation of the Rules of Use 'may warrant a suspension of library privileges'; staff 'will instruct anyone displaying these behaviors to leave') Verification pass: read 2026-11-06 at https://www.berkeleypubliclibrary.org/sites/default/files/files/inline/patron_suspension_policy_approved_14nov2018.pdf: 'Continued disruption (same or different day): Library privileges will be suspended for the day by an authorized staff-member and the patron will be asked to leave the Library building.'

- `berkeley-public-library-2018-patron-suspension-policy` (p. 2, B.2; date n/a): **opened** 2026-11-06: "Continued disruption (same or different day): Library privileges will be suspended for the day by an authorized staff-member and the patron will be asked to leave the Library building." <https://www.berkeleypubliclibrary.org/sites/default/files/files/inline/patron_suspension_policy_approved_14nov2018.pdf>

**R4**

- no work named: **unverified** (rationale: a patron is free to leave at any time; nothing in the policy holds them)

<a id="src-r5"></a>
**R5**: Berkeley Public Library, Patron Suspension Policy (orig. 2002-09-11, rev. 2018-11-14, Res. R18-053): the Library aims to 'provide and maintain a welcoming and safe environment for all patrons and library staff'; 'Violation of the Library's Rules of Use Policy may warrant a suspension of library privileges'; 'Authorized library staff will instruct anyone displaying these behaviors to leave the library facility immediately'; https://www.berkeleypubliclibrary.org/sites/default/files/files/inline/patron_suspension_policy_approved_14nov2018.pdf (a suspended patron is excluded for the suspension's term) Verification pass: read 2026-11-06 at https://www.berkeleypubliclibrary.org/sites/default/files/files/inline/patron_suspension_policy_approved_14nov2018.pdf: 'Suspension of library privileges will result in removal from, and denial of access to, all Berkeley Public Library services and facilities for a designated period of time.'

- `berkeley-public-library-2018-patron-suspension-policy` (p. 1; date n/a): **opened** 2026-11-06: "Suspension of library privileges will result in removal from, and denial of access to, all Berkeley Public Library services and facilities for a designated period of time." <https://www.berkeleypubliclibrary.org/sites/default/files/files/inline/patron_suspension_policy_approved_14nov2018.pdf>

**R6**

- no work named: **unverified** (rationale: library privileges)


## Expected properties

| property | kind | expected | meaning |
|---|---|---|---|
| dependent_cannot_exit | freedom | unreachable_open | Some subject of the institution (the dependent party) has no permitted exit at step t. Alias of subject_cannot_exit with scope=institution, kept because the human-institution table names it; iso should treat the two as the same form. |

## Pairs

Not isomorphic to: coverture-household, police-crisis, cps

<details><summary>Encoder notes (engine internals)</summary>

Second negative control for gate (b), unrelated to the lease: a service duty (R2) and a rival power over the same person by the same attribute (R3, suspend) with no bar on the patron's own exit (R4). The duty to serve is inferred from the policy's premise of service to all, so R2 is marked UNVERIFIED as a rule. refuse_service is the breaker that keeps R2 from being inert.

</details>
