# public-library

**Public library (negative control: service duty + suspension power, patron may leave)**

> The Berkeley Public Library's Patron Suspension Policy (orig. 2002-09-11, rev. 2018-11-14, Res. R18-053) aims to 'provide and maintain a welcoming and safe environment for all patrons and library staff'; 'Violation of the Library's Rules of Use Policy may warrant a suspension of library privileges'; 'Authorized library staff will instruct anyone displaying these behaviors to leave the library f...

## Roles

- **librarian**: library staff; serves and may suspend
- **patron**: a library user; the counterparty, not a dependent

## Rules

| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | source |
|---|---|---|---|---|---|---|---|---|
| R1 | librarian | may | `(open_library lb)` | `(not (open lb))` | none | tying | The librarian may open the library when it is not open. | opening hours. UNVERIFIED (general knowledge; no source opened) |
| R2 | librarian | must | `(served lb p)` | `(and (open lb) (present p) (not (suspended p)))` | none | superadditive | The patron being served must hold when the library is open and the patron is present and not suspended (Berkeley Patron Suspension Policy). | Berkeley Public Library, Patron Suspension Policy (orig. 2002-09-11, rev. 2018-1... https://www.berkeleypubliclibrary.org/sites/default/files/files/inline/patron_suspension_policy_approved_14nov2018.pdf |
| R3 | librarian | may | `(suspend lb p)` | `(and (present p) (disruptive p))` | none | rival | The librarian may suspend the patron when the patron is present and disruptive (Berkeley Patron Suspension Policy). | Berkeley Public Library, Patron Suspension Policy (orig. 2002-09-11, rev. 2018-1... https://www.berkeleypubliclibrary.org/sites/default/files/files/inline/patron_suspension_policy_approved_14nov2018.pdf |
| R4 | patron | may | `(leave p)` | `true` | none | rival | The patron may leave at any time. | a patron is free to leave at any time; nothing in the policy holds them. UNVERIF... |
| R5 | patron | may | `(enter p)` | `(and (open lb) (not (suspended p)))` | none | tying | The patron may enter when the library is open and the patron is not suspended. | Berkeley Public Library, Patron Suspension Policy (orig. 2002-09-11, rev. 2018-1... https://www.berkeleypubliclibrary.org/sites/default/files/files/inline/patron_suspension_policy_approved_14nov2018.pdf |
| R6 | patron | may | `(borrow p)` | `(and (present p) (not (suspended p)))` | none | tying | The patron may borrow when present and not suspended. | library privileges. UNVERIFIED (general knowledge; no source opened) |

**Default capacities** (enabled unless an express disability bars them): leave

## Expected properties

| property | kind | expected | meaning |
|---|---|---|---|
| dependent_cannot_exit | freedom | unreachable_open | Some subject of the institution (the dependent party) has no permitted exit at step t. Alias of subject_can... |

## Pairs

Not isomorphic to: coverture-household, police-crisis, cps

## Notes

Second negative control for gate (b), unrelated to the lease: a service duty (R2) and a rival power over the same person by the same attribute (R3, suspend) with no bar on the patron's own exit (R4). The duty to serve is inferred from the policy's premise of service to all, so R2 is marked UNVERIFIED as a rule. refuse_service is the breaker that keeps R2 from being inert.
