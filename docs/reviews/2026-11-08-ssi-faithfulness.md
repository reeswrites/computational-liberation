# Encoding-faithfulness review: ssi-marriage-penalty and -individual (2026-11-08)

Fresh agent, faithfulness seat (ADR 0014). Not the builder. Read-only apart from this file. Same model family as the encoder (ADR 0012 caveat).

**Raw sources opened by me (not summaries):** 20 CFR 416.1802, 416.1806 and 416.1801(c) (eCFR versioner XML, point-in-time 2026-11-01); 42 U.S.C. 1382(a)-(b) (Cornell HTML). POMS SI 00501.152 only by summarising WebFetch (snippet level). POMS .150, 20 CFR 416.1205, 416.537, CRS RL33675 not opened.

## Findings (red = unfaithful, amber = reservation, green = faithful)

- **R1 green.** Self-declared encoder grant, `unverified`. Honest.
- **R2 amber (over-broad).** Source: 416.1802(b)(1) "we will count your combined income and calculated the benefit amount for you as a couple" (typo is in the reg; excerpt verbatim). But (b) applies only to "an eligible spouse as defined in 416.1801(c)", which requires living "in the same household". Rule has `(married c s)` alone, so a separated married pair gets the couple rate; `separate` leaves `married` true. Pin should be (b)(1), not only (d)(1). The couple rate is in 42 U.S.C. 1382(b)(2) ($2,628, 1974 base, or 1382f amount), not "1382(a)(1)(B)" as the source line says. Fix: add `cohabits` to the condition or state the gap in `plain`.
- **R3 amber (over-broad, mis-pinned).** 1382(a)(3)(A) "$3,000 on January 1, 1989" and (B) "$2,000 on January 1, 1989" are verbatim and not indexed. Operative text for which limit applies is (a)(1)(B)(i) "in case such individual has a spouse with whom he is living", and 416.1802(b)(2) "use the couple's resource limit". Same cohabitation gap as R2. "(rather than two individual limits)" is arithmetic ($4,000), not text. Figures are cited to statute, not CRS; the date is a step date, correctly noted.
- **R4 amber (reading of the text).** 416.1806(a)(3) as written: "You and an unrelated person of the opposite sex are living together in the same household at or after the time you apply for SSI benefits, and you both lead people to believe that you are husband and wife." Rule drops "unrelated", "opposite sex" and "at or after the time you apply". POMS 152 (TN 85, effective 12/23/2025): "The instructions in this section also apply to same-sex couples." Encoding follows POMS silently while `plain` cites 416.1806. It should follow current practice (POMS; post-Obergefell) but say so: `plain` must read "(regulation text says opposite sex; POMS applies it to same-sex couples)". `cohabits` carries no sex condition, so the formal rule matches POMS, not the regulation. The `unrelated` and `at or after application` limits are unencoded; list them.
- **R4 sanctioner red-to-reword (deviation 1).** `none` is correct for a `may` power held by the agency, but the stated reason is wrong. 416.1802 holds no sanction language (only cross-references). Overpayment recovery (416.537, not opened) and reporting duties sanction the claimant for misreporting, a different attribute and a different rule (a claimant `must` report, sanctioner state). Honest encoding: keep `sanctioner: none` and replace the reason with "a power, not a duty; claimant reporting and recovery rules are unencoded and unopened". Do not call it "no sanction in any source".
- **R5 amber.** `plain` cites 416.1802, but that text says only that benefits depend on married or not (d)(1); the individual-rate consequence is from CRS (2008, snippet). Complement condition omits 416.1806(a)(2) (SSA spousal-entitlement decision) and the 416.1802(a) ineligible-spouse deeming case. Over-broad: grants individual rate to a pair deemed under (a).
- **R6 amber.** Figure verbatim (1382(a)(3)(B)); same complement gaps; limit applies to individuals without a spouse "with whom he is living".
- **R7 amber.** Bar is real but sits in 1382(a)(1)(B) and (a)(2)(B) as an eligibility condition ("not more than ... shall be an eligible individual"), not a prohibition and not in (a)(3)(A). Re-pin to (a)(1)(B); the `unverified` row can be replaced by that raw reading. `must_not` for the agency is a reading of "eligible only if". Keep `strand: rival` but say so.
- **`function:` values.** R2 `penalises_marriage_rate` and R3 `penalises_marriage_limit`: supported by the figures in 1382(b): $2,628 couple against 2 x $1,752 = $3,504, and $3,000 < $4,000; "penalty" is the analyst's label (CRS gives the word). R4 `extends_penalty_to_holding_out`: no source frames it as a displaced gate (worklist and CRS say so); label it interpretive.
- **Pair R5, R6 (reform).** Counterfactuals, `unverified`: honest. Dropping holding out is the encoder's choice, stated.
- **Entry notes.** Consent-guard ruling is stated ("ruled not applicable ... by the author, 2026-11-08") but without wording; quote the ruling. Unverified items are listed plainly, but the note's "no `opened` re-opened" claim is correct and must be applied to the `verification` fields.

## Provenance level

Carried summary-mediated fetches are not `opened` under ADR 0017 s.3 ("read in full and quoted"). Set every carried row to `snippet`, with R4 weakest-source `snippet` (POMS .150/.152). My raw reads confirm these excerpts verbatim: 416.1802 (b)(1) and (d)(1); 416.1806(a)(3); 1382(a)(3)(A)-(B). After the seat records a raw re-open with accessed date, R2, R3, R6 and the 416.1806 provenance item may return to `opened`. Effective dates: 416.1806 and 416.1802 last amended 60 FR 16376 (30 March 1995); 1382(a)(3) figures 1989-01-01; POMS 152 12/23/2025. These are dates in the text, not verified effective dates of the rule.

## Close

- **Downgrade to snippet:** R2, R3, R4, R5, R6 (and the 416.1806 item until re-recorded). R7 stays unverified until re-pinned.
- **Faithful:** R1 (as declared), pair R5/R6 (as declared counterfactuals).
- **Required fixes:** add cohabitation to R2, R3 and the R5/R6 complement (or declare the gap); re-pin R2 (1382(b)(2), 416.1802(b)), R7 (1382(a)(1)(B)); reword R4 plain for the opposite-sex split; reword deviation 1; quote the consent-guard ruling.

**Verdict: faithful with reservations.** No rule is invented, but R2 and R3 are over-broad on a condition the raw text states.
