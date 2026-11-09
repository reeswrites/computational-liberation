# ssi-marriage-penalty-individual

**SSI with the couple resource limit removed (one-rule pair of ssi-marriage-penalty: R3 dropped; couple rate and holding-out test kept; a deletion, not a reform); power reading only**

**Read first:** This entry drops only the couple resource limit (R3) from ssi-marriage-penalty; the couple rate (R2) and the holding-out test (R4) are kept. A married pair living together then has NO resource-limit rule at all: the couple limit is gone and the individual limit (R6) does not cover them. So this is a one-rule deletion for comparison, not a reform anyone proposed, and no bill was read. The id `ssi-marriage-penalty-individual` is historical (kept from an earlier five-rule pair) and no longer describes the entry. `violated` on married_couple_limited means the agency holds no power to apply the couple limit, not that a law is broken.

> Per the sourcing worklist (summarising fetches, not raw text): 20 CFR 416.1802 ('we will count your combined income and calculated the benefit amount for you as a couple.'; '(d)(1) Benefits depend on whether you are married or not married at the beginning of each month.'); 20 CFR 416.1806 (a)(3) (cohabitants who 'lead people to believe that you are husband and wife' are spouses for SSI); SSA POMS SI 00501.150 and .152 (holding out); 42 U.S.C. 1382(a)(3) (resource limits $2,000 individual and $3,000 couple as of 1 January 1989); CRS RL33675 (a married couple has a lower resource limit, a lower maximum federal benefit and a lower amount of excluded income).

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
- **power reading only**: every `may` row and default capacity on this card is a power the body holds, not the source's mandatory duty and not an applied rate or limit; a `must not (disability)` row removes such a power. A property verdict of `violated` then means "no such power exists", not that a law is broken.

## Roles

- **claimant**: the person who applies for or receives SSI (the benefit's subject)
- **spouse**: the other person of the pair, a legal spouse or a cohabitant who holds out as one
- **agency**: the Social Security Administration, which decides marital status and applies the rate and the limit

## Rules

| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | level | source |
|---|---|---|---|---|---|---|---|---|---|
| R2 | agency | may [kind: formal; sanctioner: none] | `(apply_couple_rate g c s)` | `(and (married c s) (cohabits c s))` | none | tying | The agency may rate the claimant and the other person as a couple, counting combined income at the couple rate, when they are married and living together (20 CFR 416.1802(b)(1); 42 U.S.C. 1382(b)(2)). The statute states this for a spouse "with whom he is living" (42 U.S.C. 1382(a)(1)(B)(i)) and the regulation for an eligible spouse "in the same household" (20 CFR 416.1801(c)), both as recorded by the 2026-11-08 faithfulness seat from raw text (no excerpt in this entry); the condition is married and cohabits since revision 2 (2026-11-09), so a married pair living apart is not rated as a couple. A power the agency holds, not an applied rate (power reading only). | unverified | [full source under Sources, R2](#src-r2) https://www.law.cornell.edu/cfr/text/20/416.1802 |
| R4 | agency | may [kind: formal; sanctioner: none] | `(apply_couple_rate g c s)` | `(and (cohabits c s) (holds_out c s))` | none | tying | The agency may rate cohabitants as a couple, as if married, when they live together and lead people to believe they are husband and wife. Text as written (20 CFR 416.1806(a)(3)): "an unrelated person of the opposite sex ... at or after the time you apply". The encoding follows POMS SI 00501.152, which applies the test to same-sex couples, so the formal rule carries no sex condition. | snippet | [full source under Sources, R4](#src-r4) https://www.law.cornell.edu/cfr/text/20/416.1806 |
| R5 | agency | may [kind: formal; sanctioner: none] | `(apply_individual_rate g c s)` | `(not (and (cohabits c s) (or (married c s) (holds_out c s))))` | none | tying | The agency may rate the claimant as an individual when the pair are not living together as a married or holding-out couple (a married pair living apart is rated individually; revision 2, 2026-11-09). The individual-rate consequence for the unmarried is from CRS RL33675 (snippet); 20 CFR 416.1802(d)(1) says only that benefits depend on whether you are married. | snippet | [full source under Sources, R5](#src-r5) https://www.everycrsreport.com/reports/RL33675.html |
| R6 | agency | may [kind: formal; sanctioner: none] | `(apply_individual_limit g c s)` | `(not (and (cohabits c s) (or (married c s) (holds_out c s))))` | none | tying | The agency may apply the individual resource limit ($2,000) when the pair are not living together as a married or holding-out couple (a married pair living apart gets the individual limit; revision 2, 2026-11-09) (42 U.S.C. 1382(a)(3)). | snippet | [full source under Sources, R6](#src-r6) |
| R7 | agency | must not (disability) [kind: formal; sanctioner: none] | `(pay_benefit g c)` | `(not (resources_under_limit c))` | none | rival | The agency cannot pay the claimant a benefit while the claimant's countable resources exceed the applicable limit: no such power exists then (the power to pay is a default capacity of the agency since revision 2, 2026-11-09, formerly the encoder's grant R1; the bar is an eligibility condition, 42 U.S.C. 1382(a)(1)(B), (a)(2)(B); the limits are in (a)(3)(A)-(B)). | unverified | [full source under Sources, R7](#src-r7) https://www.law.cornell.edu/uscode/text/42/1382 |

**Free fluents** (inputs the model varies, not set by any rule; see the Legend): none

**Default capacities** (an action a person of that kind can do unless an express disability removes it; these replaced the implicit `may ... when true` rows that once encoded them, README revision 4):

- `pay_benefit`: An agency may pay a benefit to a claimant unless a rule forbids it; rule rows naming it: R7 (must not, a disability).

## Variables

- R2: `g` = agency (rule var_roles); `c` = claimant (rule var_roles); `s` = spouse (rule var_roles)
- R4: `g` = agency (rule var_roles); `c` = claimant (rule var_roles); `s` = spouse (rule var_roles)
- R5: `g` = agency (rule var_roles); `c` = claimant (rule var_roles); `s` = spouse (rule var_roles)
- R6: `g` = agency (rule var_roles); `c` = claimant (rule var_roles); `s` = spouse (rule var_roles)
- R7: `g` = agency (rule var_roles); `c` = claimant (rule var_roles)

## Sources

Per rule: the full source where the table cell is cut, then each provenance item (bibliography id in `data/sources/`, pin, jurisdiction, effective date, verification level with access date, excerpt). The `level` column is the weakest item; levels: opened > snippet > recalled > unverified.

<a id="src-r2"></a>
**R2**: 20 CFR 416.1802 'Effects of marriage on eligibility and amount of benefits' (https://www.law.cornell.edu/cfr/text/20/416.1802), as carried from plans/sourcing-worklist-marriage.md section 5 (a summarising fetch, not raw text; not re-opened for this row; level snippet): 'we will count your combined income and calculated the benefit amount for you as a couple.' (the worklist's quotation, typo included) and '(d)(1) Benefits depend on whether you are married or not married at the beginning of each month.' The couple federal rate is lower than two individual rates (42 U.S.C. 1382(b)(2), not (a)(1)(B), per the faithfulness review's raw read; 1974 base rates $1,752 individual, $2,628 couple per the worklist; 2026 rates $994 / $1,491 are an unverified lead). Sanctioner none: no enforcement of the agency's duty is in the text read. Read as a power (`may`), not an applied rate; the statute is mandatory, which the encoding does not carry. Revision 2 (2026-11-09, item 1): the condition gained `cohabits` (20 CFR 416.1801(c); 42 U.S.C. 1382(a)(1)(B)(i), both read raw by the faithfulness seat, not re-opened by the builder; no excerpt added).

- `ssi-cfr-416-1802` (s. 416.1802(b)(1); (d)(1); US; date n/a): **snippet** 2026-11-08: "we will count your combined income and calculated the benefit amount for you as a couple. ... (d)(1) Benefits depend on whether you are married or not married at the beginning of each month." <https://www.law.cornell.edu/cfr/text/20/416.1802>
- `ssi-usc-1382a` (s. 1382(b)(2); US; date n/a): **unverified** <https://www.law.cornell.edu/uscode/text/42/1382>

<a id="src-r4"></a>
**R4**: 20 CFR 416.1806 (https://www.law.cornell.edu/cfr/text/20/416.1806), as carried from the worklist (a summarising fetch; not re-opened; level snippet): someone is a spouse for SSI purposes where (a)(3) 'You and an unrelated person of the opposite sex are living together in the same household' and 'you both lead people to believe that you are husband and wife.' POMS SI 00501.150 (TN 80, 02-25): 'Living together in the same household and holding themselves out as a married couple to the community in which they live.' POMS SI 00501.152 (TN 85, 12-25): 'both individuals lead people in the community in which they reside to believe they are a married couple'. POMS covers same-sex couples per a search summary; the Cornell regulation text still says opposite sex. This is the displaced gate: a conduct test that carries the couple rate to unmarried pairs. Sanctioner none (see notes): R4 is an agency `may` power with no duty to sanction, and the engine rejects a sanctioner without an or_else. Unencoded qualifiers: the regulation's `unrelated` and `at or after the time you apply`; the opposite-sex limit is deliberately not encoded (POMS). Overpayment recovery (20 CFR 416.537, not opened) sanctions the claimant under a different, unencoded rule.

- `ssi-cfr-416-1806` (s. 416.1806(a)(3); US; date n/a): **snippet** 2026-11-08: "You and an unrelated person of the opposite sex are living together in the same household ... you both lead people to believe that you are husband and wife." <https://www.law.cornell.edu/cfr/text/20/416.1806>
- `ssi-poms-si-00501-150` (SI 00501.150; US; date n/a): **snippet** 2026-11-08: "Living together in the same household and holding themselves out as a married couple to the community in which they live." <https://secure.ssa.gov/poms.nsf/lnx/0500501150>
- `ssi-poms-si-00501-152` (SI 00501.152; US; date n/a): **snippet** 2026-11-08: "both individuals lead people in the community in which they reside to believe they are a married couple" <https://secure.ssa.gov/poms.nsf/lnx/0500501152>

<a id="src-r5"></a>
**R5**: CRS RL33675 (https://www.everycrsreport.com/reports/RL33675.html), as carried from the worklist (summarising fetch; not re-opened): 'a married couple has a lower resource limit, a lower maximum federal benefit, and a lower amount of excluded income.' (so the unmarried are rated as individuals). 20 CFR 416.1802(d)(1) as in R2 (it does not itself state an individual rate for the unmarried). The complement condition is the encoder's reading of the three tests in the worklist; since revision 2 (2026-11-09) it is the exact complement of the two couple-rate routes (R2, R4): not (living together and (married or holding out)).

- `ssi-crs-rl33675` (US; date 2008-01-30): **snippet** 2026-11-08: "a married couple has a lower resource limit, a lower maximum federal benefit, and a lower amount of excluded income." <https://www.everycrsreport.com/reports/RL33675.html>
- `ssi-cfr-416-1802` (s. 416.1802(d)(1); US; date n/a): **snippet** 2026-11-08: "Benefits depend on whether you are married or not married at the beginning of each month." <https://www.law.cornell.edu/cfr/text/20/416.1802>

<a id="src-r6"></a>
**R6**: 42 U.S.C. 1382(a)(3)(B) as carried from the worklist (summarising fetch; not re-opened; level snippet): '$2,000 on January 1, 1989' for an individual, '$3,000 on January 1, 1989' for a couple. The condition is the encoder's reading and is the complement of the couple RATE routes (R2, R4), not of the couple limit (R3 is the only couple-limit rule, so an unmarried cohabiting holding-out pair has neither limit power; see notes); since revision 2 (2026-11-09) it is not (living together and (married or holding out)), so a spouse not living with the claimant leaves the individual limit in place (1382(a)(1)(B)(i), read raw by the faithfulness seat only).

- `ssi-usc-1382a` (s. 1382(a)(3)(B); US; date 1989-01-01): **snippet** 2026-11-08: "$2,000 on January 1, 1989" <https://www.law.cornell.edu/uscode/text/42/1382>

<a id="src-r7"></a>
**R7**: 42 U.S.C. 1382(a)(1)(B) and (a)(2)(B) (the bar: eligible only if resources are not more than the limit; pin from the faithfulness seat's raw read, not re-opened by the builder) and (a)(3)(A)-(B) (the limits) (https://www.law.cornell.edu/uscode/text/42/1382), as carried from the worklist (summarising fetch; not re-opened; level snippet): the resource limits '$2,000 on January 1, 1989' (individual) and '$3,000 on January 1, 1989' (couple). A disability, not a sanctioned prohibition, hence or_else null. That exceeding the limit bars payment is read from the eligibility condition in (a)(1)(B); the `must_not` form is a reading of 'eligible only if'.

- `ssi-usc-1382a` (s. 1382(a)(1)(B); (a)(2)(B); US; date n/a): **unverified** <https://www.law.cornell.edu/uscode/text/42/1382>
- `ssi-usc-1382a` (s. 1382(a)(3)(A)-(B); US; date 1989-01-01): **snippet** 2026-11-08: "$2,000 on January 1, 1989 ... $3,000 on January 1, 1989" <https://www.law.cornell.edu/uscode/text/42/1382>


## Expected properties

The `formal` cell is the checked formula (`t` is the step; `=>` reads "whenever ... then"); the meaning cell is its plain gloss.

| property | kind | expected | meaning | formal |
|---|---|---|---|---|
| married_couple_rated | freedom | holds_to_k | Whenever two people are married and living together, the benefits agency holds the power to rate them as a couple (the couple federal rate, combined income): marriage with a shared household brings the couple rate (the living-together conjunct added in SSI revision 2, 2026-11-09, with the rule it restates). Its holding is the SSI marriage penalty (preregistered plans/ssi-entry.md, 2026-11-08); read as a power the rules grant (derived), not as an applied rate. | `(forall ((c agent) (s agent)) (=> (and (married c s t) (cohabits c s t)) (couple_rate c s t)))` |
| married_couple_limited | freedom | violated | Whenever two people are married and living together, the agency holds the power to apply the couple resource limit (the living-together conjunct added in SSI revision 2, 2026-11-09, with the rule it restates). The differs_on property of the one-rule SSI pair (R3 dropped). Its holding is the resource half of the SSI marriage penalty (plans/ssi-entry.md). | `(forall ((c agent) (s agent)) (=> (and (married c s t) (cohabits c s t)) (couple_limit c s t)))` |
| penalty_reaches_unmarried | failure_mode | reachable | Some pair who are not married are rated as a couple: the penalty reaches people the marriage rule alone would not touch, through a test of conduct (holding out). Reachable when a holding-out gate exists; open when only legal marriage gates the couple rate (plans/ssi-entry.md). | `(exists ((c agent) (s agent)) (and (not (married c s t)) (couple_rate c s t)))` |
| married_rated_individually | structure | reachable | Some married pair are rated as individuals: marriage does not by itself bring the couple rate. The mirror of married_couple_rated (preregistered 2026-11-08, plans/ssi-entry.md). Since SSI revision 2 (2026-11-09) it is reachable in ssi-marriage-penalty and in its one-rule pair alike: a married pair living apart is rated individually. It does not distinguish the two entries; married_couple_limited does. | `(exists ((c agent) (s agent)) (and (married c s t) (individual_rate c s t)))` |
| over_limit_ineligible | freedom | holds_to_k | A claimant whose countable resources exceed the applicable limit is not eligible for payment. Its holding is the resource test itself (42 U.S.C. 1382(a)(3)); the encoding reads the limit as a boolean, not a dollar amount (plans/ssi-entry.md). | `(forall ((c agent)) (=> (not (resources_under_limit c t)) (not (eligible c t))))` |

## Pairs

Extends [ssi-marriage-penalty](ssi-marriage-penalty.md); one line per change:
- R3 dropped (base wording, not in this entry): The agency may apply the couple resource limit ($3,000) when they are married and living together (42 U.S.C. 1382(a)(3)(A)). The source states the couple limit for an individual with a spouse "with whom he is living" (42 U.S.C. 1382(a)(1)(B)(i)); the condition is married and cohabits since revision 2 (2026-11-09). Note, the CRS reading, not the text: two individuals may hold $4,000 together, so the couple limit is the lower.
- overrides expected_properties
- overrides minimal_pair_of
- overrides notes
Minimal pair of [ssi-marriage-penalty](ssi-marriage-penalty.md), differing in rule R3; the pair differs on property married_couple_limited.
Not isomorphic to: coverture-household, police-crisis, cps, lease

<details><summary>Encoder notes (engine internals)</summary>

One-rule pair since revision 2 (plans/ssi-entry.md, "Revision 2 run", preregistered 2026-11-09; item 4 ruled 2026-11-09): the base with R3, the couple resource limit, dropped and nothing else changed; preregistered to differ from the base on married_couple_limited (holds_to_k in the base, violated here). Power reading only, as the base: `violated` means the agency holds no power to apply the couple limit, not that a law is broken; dollar amounts are not modelled. Known limit: with R3 gone a married pair living together has neither the couple limit nor the individual limit (R6 excludes them), so this is a one-rule deletion in the ADR 0007 sense, not a coherent reform text; no reform bill was read (S. 73 of 2025 is an unopened lead). The entry id is kept from the earlier pair and no longer describes it: R2 (couple rate), R4 (holding out), R5 and R6 (individual rate and limit, conditioned) and R7 (resource bar) are all inherited unchanged, and `pay_benefit` is the base's default capacity. PREVIOUS PAIR, superseded 2026-11-09 and recorded here: a five-rule reform pair, `rules_drop: [R2, R3, R4]` with R5 and R6 replaced by `may ... when true` rows (individual rate and limit whatever the marital status; unverified counterfactuals resting on no source), `minimal_pair_of.rule: R2,R3,R4,R5,R6`, `differs_on: married_couple_rated`; its verdicts at k 6 and 8 were married_couple_rated violated, married_couple_limited violated, penalty_reaches_unmarried unreachable_open, married_rated_individually reachable, over_limit_ineligible holds_to_k (plans/ssi-entry.md Results, run 2026-11-08). Its notes read: This is a 5-rule reform pair, not a minimal pair (the field name `minimal_pair_of` is the dataset's, ADR 0007 names one-rule pairs as the model). Revision 2 options for a one-rule pair: drop R3 alone (flips married_couple_limited), or drop R4 alone (holding out removed; flips penalty_reaches_unmarried). Dropping R2 alone leaves married pairs with no rate, which is why the reform edits R5 and R6. Penalty removed: R2, R3 (couple rate and limit gated on marriage) and R4 (the holding-out gate) are dropped, and R5, R6 lose their marital-status condition, so the individual rate and limit apply to every claimant. This is not one rule apart (three dropped, two edited); `rule` names the five rules (R2,R3,R4 dropped; R5,R6 replaced) and the pair is read on verdicts, not on the one-rule gate. R5 and R6 of the pair rest on no source (unverified counterfactuals). `violated` here means the power is absent, not that a law is broken; dollar amounts are not modelled. Holding out is DROPPED, not kept: with no couple rate there is nothing for the test to gate, and no reform text was read that keeps it (S. 73 of 2025 is an unopened lead; the CRS report gives rule and size only). The fluents `holds_out`, `cohabits` and the actions remain declared so the two entries share a vocabulary and can be compared; here they gate nothing. The resource bar (R1, R7) is kept: the reform removes the penalty, not the resource test. Preregistered in plans/ssi-entry.md before any run. (end of the previous pair's notes). Consent guard ruling, quoted exactly: "Consent guard note (plans/consent-guard-note-DRAFT.md) ruled not applicable to benefits rules by the author, 2026-11-08."

</details>
