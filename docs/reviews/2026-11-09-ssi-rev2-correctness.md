# SSI revision 2: correctness seat (ADR 0014)

Seat: fresh; did not build or encode the batch. Read: SEATS.md; plans/ssi-entry.md Revision 2 decisions, rulings and run (preregistration, Results, drift); `git show ecca295`; `git diff ecca295..3bc056a`; `git diff d5d3a92..3bc056a` on the SSI sources, _composites.yaml, properties.yaml, verdicts-baseline.json; the three built entries in institutions.json; surprises S7; N74 to N76. Engine 50ed97f: rules_lower.py `enabled` (729-742), action instances and attribute scoping (910-916), rule-instance typing (925-957). The builder's Results were read as claims.

Ran (worktree root, pinned venv): `phil rules check --inst ssi-marriage-penalty|ssi-marriage-penalty-individual|coverture-us-ssi --k 6|8 --init declared --compliance strict --step-mode one --no-cache`; twelve scratch probe properties via `--properties <scratch> --prop` at k=6; a baseline comparison script. Not run: checks.sh, check-all, ablate, iso, pytest (machine busy; those Results lines are not re-verified).

## Findings

1. **Process integrity (Q1): green, correct. Not the S7 pattern.** ecca295 (08:53) touches only plans/ssi-entry.md (+81) and already contains Scope (b) (both antecedents become married and cohabits; the alternative not taken, with its verdicts), Edit 6, and "(edited formula)" in the prediction table. properties.yaml first changes in 3bc056a (09:27). Drift 3 is accurate. This is a property edit declared before the run, not one made after seeing results; S7 was an expectation edited post hoc. Git cannot show that no `phil` ran before 08:53. fix: none.

2. **The edit still needs the author (Q1, by-construction): amber.** No ruling names a property edit; the builder chose it so that ruling 4's flip exists. Probes with the old formulas: both `violated` in the base (wed, no cohabit) and the limit one `violated` in the pair, so the pair would differ on nothing, as Scope (b) said. Each antecedent is now its rule's condition, so `holds_to_k` is by construction. fix: author ratifies or reverses N75 before any claim cites these two rows; no data edit.

3. **Append-only: green, with one line.** 3bc056a replaces `### Results / (pending)` and appends; the only edit above it is the file's Status line (line 3). The preregistration itself is unedited. fix: optional, say "except the Status line".

4. **Four moved verdicts genuine (Q2): green, correct.** All 25 rows re-run as reported at k=6 and 8, flags `-`; both edited invariants `vacuous=False`, `antecedent_reachable=True`. Witnesses: base `married_rated_individually` at t=1 (wed, never cohabited) and at t=4 after `separate`; pair `penalty_reaches_unmarried` by present_as_married, cohabit, never wed; pair `married_couple_limited` violated after wed, cohabit (couple_rate true, couple_limit false); composite `married_rated_individually` at t=1 after coverture `marry`. fix: none.

5. **Composite witness is the initial default, not a separation: amber.** In coverture-us-ssi only SSI's `cohabit` sets `cohabits`, so every coverture couple starts "living apart", individually rated. The row is also reachable by `separate`, but the shortest witness is a coverture couple not yet sharing a household. fix: one sentence in the composite `notes`.

6. **`pay_benefit` default capacity equals dropped R1 (Q3): green, correct.** Before: `g` scoped to agency by the R1/R7 attributes: one instance (agency, claimant); enabled = true and not over-limit. After: `arg_roles [agency, claimant]` gives the same single instance without R1 (and keeps it under R7 ablation); enabled = true minus R7. Firing: gated on `true` before, ungated now. Composite: `arg_roles [agency, partner_a]`, one instance. Probe `resources_under_limit -> eligible` holds_to_k in base and composite beside `over_limit_ineligible`: eligible iff under limit. fix: none.

7. **R5 complement (Q4, rate): green, correct.** R2 or R4 = cohabits and (married or holds_out); R5 is its negation. Probes, base and composite: both powers at once `open`; neither `open`; married, cohabiting and individual_rate `open`.

8. **R6 is not the complement of R3 (Q4, limit): amber, incorrect as worded.** R6 carries the same condition as R5, but the couple limit has one route (R3: married and cohabits), not two. Probe, base, k=6: an unmarried, cohabiting, holding-out pair has neither `couple_limit` nor `individual_limit`: `reachable` (present_as_married, cohabit). Pre-existing (old R3/R6 had the same hole), but Edit 2 calls R6 "the exact complement of the two couple routes" and no note or negative-results row records it. fix: declare the gap in `notes` and a negative-results row; whether R3 should read `cohabits and (married or holds_out)` is a faithfulness ruling and a new preregistration.

9. **One-rule pair, married cohabiting pair (Q4): green, confirmed; intended, disclosed.** Pair probe: married with neither limit power `reachable`. This is what "drop R3 alone" means as an ADR 0007 deletion. Recorded in Scope, the pair's notes and N76. fix: none beyond N76.

10. **Baseline (Q5): green, correct.** Script, d5d3a92 against HEAD: 192 and 192 rows, same key set, identical engine_hash (58c4c54222de...), format, params, z3; exactly four rows differ, the four in the table.

11. **`cohabits` is not vacuous (Q6): green, correct.** Declared before this batch, false in `initial`, not in `initial_free`; set by `cohabit`, cleared by `separate`. Conditioning changes which states grant R2/R3/R5/R6 and adds no free world. A separated married pair is reached in 3 steps (wed, cohabit, separate), and a wed-never-cohabited pair in 1.

## Counts

Findings 11: green 8, amber 3, red 0. Questions: correct 5 (Q1, Q2, Q3, Q5, Q6), incorrect 0, cannot tell 0; Q4 correct for the rate, incorrect as worded for the limit (finding 8). Batch does not pause.

## Fixes requested (fix pass)

1. Finding 2: author ratifies or reverses the two formula edits (N75).
2. Finding 8: record the holding-out limit gap (notes, negative-results); correct "exact complement" for R6.
3. Finding 5: composite `notes` sentence on `marry` leaving `cohabits` false.
4. Finding 3 (optional): Results wording on the Status line.
