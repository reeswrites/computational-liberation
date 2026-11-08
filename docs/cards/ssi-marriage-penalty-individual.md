# ssi-marriage-penalty-individual

**SSI without the marriage penalty (individual rate and limit regardless of marital status; holding-out test dropped)**

> Per the sourcing worklist (summarising fetches, not raw text): 20 CFR 416.1802 ('we will count your combined income and calculated the benefit amount for you as a couple.'; '(d)(1) Benefits depend on whether you are married or not married at the beginning of each month.'); 20 CFR 416.1806 (a)(3) (cohabitants who 'lead people to believe that you are husband and wife' are spouses for SSI); SSA POMS SI 00501.150 and .152 (holding out); 42 U.S.C. 1382(a)(3) (resource limits $2,000 individual and $3,000 couple as of 1 January 1989); CRS RL33675 (a married couple has a lower resource limit, a lower maximum federal benefit and a lower amount of excluded income).

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

- **claimant**: the person who applies for or receives SSI (the benefit's subject)
- **spouse**: the other person of the pair, a legal spouse or a cohabitant who holds out as one
- **agency**: the Social Security Administration, which decides marital status and applies the rate and the limit

## Rules

| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | level | source |
|---|---|---|---|---|---|---|---|---|---|
| R1 | agency | may | `(pay_benefit g c)` | `true` | none | tying | The agency may pay the claimant a benefit (42 U.S.C. 1382(a)); the encoder's grant, so that the resource bar in R7 has a power to remove. | unverified | The SSI payment power, 42 U.S.C. 1382(a). UNVERIFIED as a rule row: no excerpt supports a bare grant of the power to pay; it is the encoder's skeleton so that R7 (the resource bar) removes something. Sanctioner none: the sources opened name no enforcement of the agency's payment duty. |
| R5 (replaced) | agency | may | `(apply_individual_rate g c s)` | `true` | none | tying | The agency may rate the claimant as an individual whatever the marital status of the pair (a reform: individual rate for all). | unverified | [full source under Sources, R5](#src-r5) |
| R6 (replaced) | agency | may | `(apply_individual_limit g c s)` | `true` | none | tying | The agency may apply the individual resource limit whatever the marital status of the pair (a reform: individual limit for all). | unverified | UNVERIFIED reform: no reform text was read. The rule is the base R6 with its marital-status condition removed. Baseline text for the rule it replaces: 42 U.S.C. 1382(a)(3)(B), '$2,000 on January 1, 1989' for an individual (carried from the worklist; summarising fetch). |
| R7 | agency | must not (disability) | `(pay_benefit g c)` | `(not (resources_under_limit c))` | none | rival | The agency cannot pay the claimant a benefit while the claimant's countable resources exceed the applicable limit: no such power exists (42 U.S.C. 1382(a)(3)). | unverified | [full source under Sources, R7](#src-r7) https://www.law.cornell.edu/uscode/text/42/1382 |

**Default capacities** (an action a person of that kind can do unless an express disability removes it): none

## Variables

- R1: `g` = agency (rule var_roles); `c` = claimant (rule var_roles)
- R5: `g` = agency (rule var_roles); `c` = claimant (rule var_roles); `s` = spouse (rule var_roles)
- R6: `g` = agency (rule var_roles); `c` = claimant (rule var_roles); `s` = spouse (rule var_roles)
- R7: `g` = agency (rule var_roles); `c` = claimant (rule var_roles)

## Sources

Per rule: the full source where the table cell is cut, then each provenance item (bibliography id in `data/sources/`, pin, jurisdiction, effective date, verification level with access date, excerpt). The `level` column is the weakest item; levels: opened > snippet > recalled > unverified.

**R1**

- no work named: **unverified** (encoder skeleton; 42 U.S.C. 1382(a) is the program statute (ssi-usc-1382a) but the grant row rests on no excerpt)

<a id="src-r5"></a>
**R5**: UNVERIFIED reform: no reform text was read (S. 73 of 2025, named in plans/sourcing-worklist-marriage.md Gaps, is an unopened lead). The rule is the base R5 with its marital-status condition removed, which is what 'penalty removed' means in the preregistration (plans/ssi-entry.md). Baseline text for the rule it replaces: CRS RL33675, 'a married couple has a lower resource limit, a lower maximum federal benefit, and a lower amount of excluded income.' (carried from the worklist; summarising fetch).

- no work named: **unverified** (a counterfactual, not a law: no reform text opened; condition deleted from base R5 by the encoder)

**R6**

- no work named: **unverified** (a counterfactual, not a law: no reform text opened; condition deleted from base R6 by the encoder)

<a id="src-r7"></a>
**R7**: 42 U.S.C. 1382(a)(3) (https://www.law.cornell.edu/uscode/text/42/1382), as carried from the worklist (summarising fetch; not re-opened): the resource limits '$2,000 on January 1, 1989' (individual) and '$3,000 on January 1, 1989' (couple). A disability, not a sanctioned prohibition, hence or_else null. That exceeding the limit bars payment is the encoder's reading: the operative text of (a)(3)(A) was not read.

- `ssi-usc-1382a` (s. 1382(a)(3)(A)-(B); US; date 1989-01-01): **opened** 2026-11-08: "$2,000 on January 1, 1989 ... $3,000 on January 1, 1989"
- no work named: **unverified** (the bar itself (an over-limit claimant is ineligible) rests on no excerpt; the (a)(3)(A) operative text was not read)


## Expected properties

| property | kind | expected | meaning |
|---|---|---|---|
| married_couple_rated | freedom | violated | Whenever two people are married, the benefits agency holds the power to rate them as a couple (the couple federal rate, combined income): marriage brings the couple rate. Its holding is the SSI marriage penalty (preregistered plans/ssi-entry.md, 2026-11-08); read as a power the rules grant (derived), not as an applied rate. |
| married_couple_limited | freedom | violated | Whenever two people are married, the agency holds the power to apply the couple resource limit. Its holding is the resource half of the SSI marriage penalty (plans/ssi-entry.md). |
| penalty_reaches_unmarried | failure_mode | unreachable_open | Some pair who are not married are rated as a couple: the penalty reaches people the marriage rule alone would not touch, through a test of conduct (holding out). Reachable when a holding-out gate exists; open when only legal marriage gates the couple rate (plans/ssi-entry.md). |
| married_rated_individually | structure | reachable | Some married pair are rated as individuals: marriage does not by itself bring the couple rate. The mirror of married_couple_rated, preregistered to separate ssi-marriage-penalty from its individual-rate pair (plans/ssi-entry.md). |
| over_limit_ineligible | freedom | holds_to_k | A claimant whose countable resources exceed the applicable limit is not eligible for payment. Its holding is the resource test itself (42 U.S.C. 1382(a)(3)); the encoding reads the limit as a boolean, not a dollar amount (plans/ssi-entry.md). |

## Pairs

Extends [ssi-marriage-penalty](ssi-marriage-penalty.md); one line per change:
- R2 dropped: The agency may rate the claimant and the other person as a couple, counting combined income at the couple rate, when they are married (20 CFR 416.1802).
- R3 dropped: The agency may apply the couple resource limit ($3,000) rather than two individual limits ($2,000 each) when they are married (42 U.S.C. 1382(a)(3)).
- R4 dropped: The agency may rate cohabitants as a couple, as if married, when they live together and lead people to believe they are husband and wife (20 CFR 416.1806; POMS SI 00501.150, .152).
- R5 replaced: was "The agency may rate the claimant as an individual when the pair are neither married nor holding out (20 CFR 416.1802)." now "The agency may rate the claimant as an individual whatever the marital status of the pair (a reform: individual rate for all)."
- R6 replaced: was "The agency may apply the individual resource limit ($2,000) when the pair are neither married nor holding out (42 U.S.C. 1382(a)(3))." now "The agency may apply the individual resource limit whatever the marital status of the pair (a reform: individual limit for all)."
- overrides expected_properties
- overrides minimal_pair_of
- overrides notes
Minimal pair of [ssi-marriage-penalty](ssi-marriage-penalty.md), differing in rule None; the pair differs on property married_couple_rated.
Not isomorphic to: coverture-household, police-crisis, cps, lease

<details><summary>Encoder notes (engine internals)</summary>

Minimal pair of ssi-marriage-penalty with the penalty removed: R2, R3 (couple rate and limit gated on marriage) and R4 (the holding-out gate) are dropped, and R5, R6 lose their marital-status condition, so the individual rate and limit apply to every claimant. This is not one rule apart (three dropped, two edited); `rule` is null for that reason and the pair is read on verdicts, not on the one-rule gate. Holding out is DROPPED, not kept: with no couple rate there is nothing for the test to gate, and no reform text was read that keeps it (S. 73 of 2025 is an unopened lead; the CRS report gives rule and size only). The fluents `holds_out`, `cohabits` and the actions remain declared so the two entries share a vocabulary and can be compared; here they gate nothing. The resource bar (R1, R7) is kept: the reform removes the penalty, not the resource test. Preregistered in plans/ssi-entry.md before any run. Consent guard note (plans/consent-guard-note-DRAFT.md) ruled not applicable to benefits rules by the author, 2026-11-08.

</details>
