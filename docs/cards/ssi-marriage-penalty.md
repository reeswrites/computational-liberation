# ssi-marriage-penalty

**SSI marriage penalty (couple rate and resource limit gated on marriage and living together, extended to unmarried couples who hold out); power reading only**

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

## Roles

- **claimant**: the person who applies for or receives SSI (the benefit's subject)
- **spouse**: the other person of the pair, a legal spouse or a cohabitant who holds out as one
- **agency**: the Social Security Administration, which decides marital status and applies the rate and the limit

## Rules

| id | who | deontic | what (aim) | when (conditions) | or else | strand | plain | level | source |
|---|---|---|---|---|---|---|---|---|---|
| R2 | agency | may [kind: formal; sanctioner: none] | `(apply_couple_rate g c s)` | `(and (married c s) (cohabits c s))` | none | tying | The agency may rate the claimant and the other person as a couple, counting combined income at the couple rate, when they are married and living together (20 CFR 416.1802(b)(1); 42 U.S.C. 1382(b)(2)). The source states this for a spouse "with whom he or she is living" (20 CFR 416.1801(c); 42 U.S.C. 1382(a)(1)(B)(i)); the condition is married and cohabits since revision 2 (2026-11-09), so a married pair living apart is not rated as a couple. A power the agency holds, not an applied rate (power reading only). | unverified | [full source under Sources, R2](#src-r2) https://www.law.cornell.edu/cfr/text/20/416.1802 |
| R3 | agency | may [kind: formal; sanctioner: none] | `(apply_couple_limit g c s)` | `(and (married c s) (cohabits c s))` | none | tying | The agency may apply the couple resource limit ($3,000) when they are married and living together (42 U.S.C. 1382(a)(3)(A)). The source states the couple limit for an individual with a spouse "with whom he is living" (42 U.S.C. 1382(a)(1)(B)(i)); the condition is married and cohabits since revision 2 (2026-11-09). Note, the CRS reading, not the text: two individuals may hold $4,000 together, so the couple limit is the lower. | snippet | [full source under Sources, R3](#src-r3) https://www.law.cornell.edu/uscode/text/42/1382 |
| R4 | agency | may [kind: formal; sanctioner: none] | `(apply_couple_rate g c s)` | `(and (cohabits c s) (holds_out c s))` | none | tying | The agency may rate cohabitants as a couple, as if married, when they live together and lead people to believe they are husband and wife. Text as written (20 CFR 416.1806(a)(3)): "an unrelated person of the opposite sex ... at or after the time you apply". The encoding follows POMS SI 00501.152, which applies the test to same-sex couples, so the formal rule carries no sex condition. | snippet | [full source under Sources, R4](#src-r4) https://www.law.cornell.edu/cfr/text/20/416.1806 |
| R5 | agency | may [kind: formal; sanctioner: none] | `(apply_individual_rate g c s)` | `(not (and (cohabits c s) (or (married c s) (holds_out c s))))` | none | tying | The agency may rate the claimant as an individual when the pair are not living together as a married or holding-out couple (a married pair living apart is rated individually; revision 2, 2026-11-09). The individual-rate consequence for the unmarried is from CRS RL33675 (snippet); 20 CFR 416.1802(d)(1) says only that benefits depend on whether you are married. | snippet | [full source under Sources, R5](#src-r5) https://www.everycrsreport.com/reports/RL33675.html |
| R6 | agency | may [kind: formal; sanctioner: none] | `(apply_individual_limit g c s)` | `(not (and (cohabits c s) (or (married c s) (holds_out c s))))` | none | tying | The agency may apply the individual resource limit ($2,000) when the pair are not living together as a married or holding-out couple (a married pair living apart gets the individual limit; revision 2, 2026-11-09) (42 U.S.C. 1382(a)(3)). | snippet | [full source under Sources, R6](#src-r6) |
| R7 | agency | must not (disability) [kind: formal; sanctioner: none] | `(pay_benefit g c)` | `(not (resources_under_limit c))` | none | rival | The agency cannot pay the claimant a benefit while the claimant's countable resources exceed the applicable limit: no such power exists then (the power to pay is a default capacity of the agency since revision 2, 2026-11-09, formerly the encoder's grant R1; the bar is an eligibility condition, 42 U.S.C. 1382(a)(1)(B), (a)(2)(B); the limits are in (a)(3)(A)-(B)). | unverified | [full source under Sources, R7](#src-r7) https://www.law.cornell.edu/uscode/text/42/1382 |

**Free fluents** (inputs the model varies, not set by any rule; see the Legend): none

**Default capacities** (an action a person of that kind can do unless an express disability removes it; these replaced the implicit `may ... when true` rows that once encoded them, README revision 4):

- `pay_benefit`: A agency may pay benefit a claimant unless a rule forbids it; rule rows naming it: R7 (must not, a disability).

## Variables

- R2: `g` = agency (rule var_roles); `c` = claimant (rule var_roles); `s` = spouse (rule var_roles)
- R3: `g` = agency (rule var_roles); `c` = claimant (rule var_roles); `s` = spouse (rule var_roles)
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

<a id="src-r3"></a>
**R3**: 42 U.S.C. 1382(a)(3)(A)-(B) (https://www.law.cornell.edu/uscode/text/42/1382), as carried from the worklist (first 100,000 of 170,641 characters, through a summarising fetch; not re-opened; level snippet): '$3,000 on January 1, 1989' for a couple and '$2,000 on January 1, 1989' for an individual (Pub. L. 98-369 s. 2611, not indexed to inflation; the 1.5 ratio is arithmetic). A pair of individuals may hold $4,000 together, so the couple limit is the lower of the two. Sanctioner none: no enforcement in the text read. The 2026 limits equal the 1989 figures per an unverified search-summary lead. Revision 2 (2026-11-09, item 1): the condition gained `cohabits` (42 U.S.C. 1382(a)(1)(B)(i), a spouse with whom he is living, read raw by the faithfulness seat, not re-opened by the builder; no excerpt added).

- `ssi-usc-1382a` (s. 1382(a)(3)(A)-(B); US; date 1989-01-01): **snippet** 2026-11-08: "$3,000 on January 1, 1989 ... $2,000 on January 1, 1989" <https://www.law.cornell.edu/uscode/text/42/1382>

<a id="src-r4"></a>
**R4**: 20 CFR 416.1806 (https://www.law.cornell.edu/cfr/text/20/416.1806), as carried from the worklist (a summarising fetch; not re-opened; level snippet): someone is a spouse for SSI purposes where (a)(3) 'You and an unrelated person of the opposite sex are living together in the same household' and 'you both lead people to believe that you are husband and wife.' POMS SI 00501.150 (TN 80, 02-25): 'Living together in the same household and holding themselves out as a married couple to the community in which they live.' POMS SI 00501.152 (TN 85, 12-25): 'both individuals lead people in the community in which they reside to believe they are a married couple'. POMS covers same-sex couples per a search summary; the Cornell regulation text still says opposite sex. This is the displaced gate: a conduct test that carries the couple rate to unmarried pairs. Sanctioner none (see notes): R4 is an agency `may` power with no duty to sanction, and the engine rejects a sanctioner without an or_else. Unencoded qualifiers: the regulation's `unrelated` and `at or after the time you apply`; the opposite-sex limit is deliberately not encoded (POMS). Overpayment recovery (20 CFR 416.537, not opened) sanctions the claimant under a different, unencoded rule.

- `ssi-cfr-416-1806` (s. 416.1806(a)(3); US; date n/a): **snippet** 2026-11-08: "You and an unrelated person of the opposite sex are living together in the same household ... you both lead people to believe that you are husband and wife." <https://www.law.cornell.edu/cfr/text/20/416.1806>
- `ssi-poms-si-00501-150` (SI 00501.150; US; date n/a): **snippet** 2026-11-08: "Living together in the same household and holding themselves out as a married couple to the community in which they live." <https://secure.ssa.gov/poms.nsf/lnx/0500501150>
- `ssi-poms-si-00501-152` (SI 00501.152; US; date n/a): **snippet** 2026-11-08: "both individuals lead people in the community in which they reside to believe they are a married couple" <https://secure.ssa.gov/poms.nsf/lnx/0500501152>

<a id="src-r5"></a>
**R5**: CRS RL33675 (https://www.everycrsreport.com/reports/RL33675.html), as carried from the worklist (summarising fetch; not re-opened): 'a married couple has a lower resource limit, a lower maximum federal benefit, and a lower amount of excluded income.' (so the unmarried are rated as individuals). 20 CFR 416.1802(d)(1) as in R2 (it does not itself state an individual rate for the unmarried). The complement condition is the encoder's reading of the three tests in the worklist; since revision 2 (2026-11-09) it is the exact complement of the two couple routes: not (living together and (married or holding out)).

- `ssi-crs-rl33675` (US; date 2008-01-30): **snippet** 2026-11-08: "a married couple has a lower resource limit, a lower maximum federal benefit, and a lower amount of excluded income." <https://www.everycrsreport.com/reports/RL33675.html>
- `ssi-cfr-416-1802` (s. 416.1802(d)(1); US; date n/a): **snippet** 2026-11-08: "Benefits depend on whether you are married or not married at the beginning of each month." <https://www.law.cornell.edu/cfr/text/20/416.1802>

<a id="src-r6"></a>
**R6**: 42 U.S.C. 1382(a)(3)(B) as carried from the worklist (summarising fetch; not re-opened; level snippet): '$2,000 on January 1, 1989' for an individual, '$3,000 on January 1, 1989' for a couple. The complement condition is the encoder's reading; since revision 2 (2026-11-09) it is not (living together and (married or holding out)), so a spouse not living with the claimant leaves the individual limit in place (1382(a)(1)(B)(i), read raw by the faithfulness seat only).

- `ssi-usc-1382a` (s. 1382(a)(3)(B); US; date 1989-01-01): **snippet** 2026-11-08: "$2,000 on January 1, 1989" <https://www.law.cornell.edu/uscode/text/42/1382>

<a id="src-r7"></a>
**R7**: 42 U.S.C. 1382(a)(1)(B) and (a)(2)(B) (the bar: eligible only if resources are not more than the limit; pin from the faithfulness seat's raw read, not re-opened by the builder) and (a)(3)(A)-(B) (the limits) (https://www.law.cornell.edu/uscode/text/42/1382), as carried from the worklist (summarising fetch; not re-opened; level snippet): the resource limits '$2,000 on January 1, 1989' (individual) and '$3,000 on January 1, 1989' (couple). A disability, not a sanctioned prohibition, hence or_else null. That exceeding the limit bars payment is read from the eligibility condition in (a)(1)(B); the `must_not` form is a reading of 'eligible only if'.

- `ssi-usc-1382a` (s. 1382(a)(1)(B); (a)(2)(B); US; date n/a): **unverified** <https://www.law.cornell.edu/uscode/text/42/1382>
- `ssi-usc-1382a` (s. 1382(a)(3)(A)-(B); US; date 1989-01-01): **snippet** 2026-11-08: "$2,000 on January 1, 1989 ... $3,000 on January 1, 1989" <https://www.law.cornell.edu/uscode/text/42/1382>


## Expected properties

| property | kind | expected | meaning |
|---|---|---|---|
| married_couple_rated | freedom | holds_to_k | Whenever two people are married and living together, the benefits agency holds the power to rate them as a couple (the couple federal rate, combined income): marriage brings the couple rate (the living-together conjunct added in SSI revision 2, 2026-11-09, with the rule it restates). Its holding is the SSI marriage penalty (preregistered plans/ssi-entry.md, 2026-11-08); read as a power the rules grant (derived), not as an applied rate. |
| married_couple_limited | freedom | holds_to_k | Whenever two people are married and living together, the agency holds the power to apply the couple resource limit (the living-together conjunct added in SSI revision 2, 2026-11-09, with the rule it restates). The differs_on property of the one-rule SSI pair (R3 dropped). Its holding is the resource half of the SSI marriage penalty (plans/ssi-entry.md). |
| penalty_reaches_unmarried | failure_mode | reachable | Some pair who are not married are rated as a couple: the penalty reaches people the marriage rule alone would not touch, through a test of conduct (holding out). Reachable when a holding-out gate exists; open when only legal marriage gates the couple rate (plans/ssi-entry.md). |
| married_rated_individually | structure | reachable | Some married pair are rated as individuals: marriage does not by itself bring the couple rate. The mirror of married_couple_rated, preregistered to separate ssi-marriage-penalty from its individual-rate pair (plans/ssi-entry.md). Since SSI revision 2 (2026-11-09) it is reachable in the base too: a married pair living apart is rated individually, and it no longer separates the pair. |
| over_limit_ineligible | freedom | holds_to_k | A claimant whose countable resources exceed the applicable limit is not eligible for payment. Its holding is the resource test itself (42 U.S.C. 1382(a)(3)); the encoding reads the limit as a boolean, not a dollar amount (plans/ssi-entry.md). |

## Pairs

Extended by: [ssi-marriage-penalty-individual](ssi-marriage-penalty-individual.md)
[ssi-marriage-penalty-individual](ssi-marriage-penalty-individual.md) is a minimal pair of this entry (rule R3).
Not isomorphic to: coverture-household, police-crisis, cps, lease

<details><summary>Encoder notes (engine internals)</summary>

POWER READING ONLY (revision 2 item 2, ruled 2026-11-09): every rule here is a power the agency holds (`may`, or a default capacity a disability removes), not the statute's mandatory duty and not an applied rate or limit; the ADR 0009 must-be encoding is not attempted in this entry and is a later preregistration of its own. Revision 2 (plans/ssi-entry.md, "Revision 2 run", preregistered 2026-11-09): (item 1) R2 and R3 are conditioned on married and cohabits, R5 and R6 on the complement not (cohabits and (married or holds_out)), so a married pair living apart gets the individual rate and limit; `cohabits` was already declared (set by `cohabit` / `separate`, false at the start, not a free fluent). (item 3) `pay_benefit` is a `default_capacity` action typed `arg_roles [agency, claimant]` and the grant rule R1 (`may pay_benefit when true`) is deleted, ids not renumbered; R5 and R6 stay rules because they carry a condition, which a default capacity cannot. (item 4) the pair ssi-marriage-penalty-individual is now a one-rule pair that drops R3. The properties married_couple_rated and married_couple_limited read married and cohabits since the same revision. SSI marriage penalty, encoded as powers the rules grant the agency (the project's convention: a derived fluent reads `enabled`). Roles claimant, spouse, agency; `married` arity 2 typed [claimant, spouse] so it can be aliased to partner_a / partner_b for composition with coverture-household-us (plans/composition.md; ADR 0018). Preregistered in plans/ssi-entry.md before any run. Encoded as `may` powers, not the statute's mandatory 'must': a must on an action fires every step and blocks the other actions (ADR 0009), and a must-be would need the establishing action to carry the rate. Dollar amounts are not represented: the couple penalty appears only as which limit and which rate the agency is empowered to apply. Deviations from the brief, recorded: (1) R4, the displaced gate, is `kind: formal, sanctioner: none`, not `state`: R4 is an agency `may` power with no duty to sanction, and the engine rejects a sanctioner without an or_else; overpayment recovery (20 CFR 416.537, not opened) sanctions the claimant under a different, unencoded rule; the displaced reading therefore cannot lean on a sanctioner difference and reads attribute sets only. (2) Holding out is encoded as a power on the same aim as R2 (a second route to the couple rate), not as a rewrite of `married`, because a derived fluent cannot read `married or holds_out`. Unverified or unread: 20 CFR 416.1804, 416.1805 and the deeming sections 416.1160-1163; effective dates of 416.1806; 2026 federal benefit rates and limits (a search-summary lead); 20 CFR 416.537 (overpayment recovery); no secondary source frames holding out as a displaced gate (CRS gives rule and size only); every provenance level is `snippet` or `unverified` (ADR 0017 s.3): the excerpts were carried from the worklist, whose fetches returned a summary, not raw text, and were not re-opened by the builder (the faithfulness seat confirmed 416.1802(b)(1) and (d)(1), 416.1806(a)(3) and 1382(a)(3)(A)-(B) verbatim from raw text). `divorce` is an unsourced encoder action (a bare setter of married false; no source mentions divorce, and no rule uses it). `marry` was renamed `wed` for composition (P2b, plans/p2-ssi-composite.md) because coverture-household-us also has a `marry`; no rule, plain line or source changed. Vocabulary is the worklist's ASSUMED vocabulary. No `is_subject`, `can_exit` or care fluents are declared, so none of the 34 older properties is applicable to this entry alone; they become applicable only in a composite (what P2 needs is in plans/ssi-entry.md). Unencoded: R4 qualifiers `unrelated` and timing, R5/R6 complement omits 416.1806(a)(2) and the 416.1802(a) deeming case. R4 follows POMS SI 00501.152 (same-sex included), not the opposite-sex text of 416.1806(a)(3). Consent guard ruling, quoted exactly: "Consent guard note (plans/consent-guard-note-DRAFT.md) ruled not applicable to benefits rules by the author, 2026-11-08."

</details>
