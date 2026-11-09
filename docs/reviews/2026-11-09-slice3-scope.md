# Priority slice 3 (transfer graph, `rebundling`): scope seat, 2026-11-09

Seat: Scope (ADR 0014: "does this batch move the thin path in docs/plan.md, or open a front? Name what should be parked."). SEATS.md has no standing brief for this seat; this review follows the Correctness seat's format and the precedent in docs/reviews/2026-11-04-adr0016-council.md ("Scope seat").

**Independence.** Fresh agent. I did not build, encode, gloss or coordinate this batch. I read the builder's Results as a claim, not as evidence.

**Read.** plans/priority-slice3.md at 56d3e4a and 54fe58f; plans/priority.md (Design, Slices, Open questions, Decisions, revision 2); docs/plan.md (Where to pick up, two-track note, Thin path, Log); docs/claims.md T1, T11; ADR 0016 with its amendment; docs/glossary.md "rebundling"; docs/ablation/2026-11-09-slice3/ (README, seven `.txt`, `transfer-summary.json`); docs/negative-results.md (tail); engine diff 50ed97f..d763cb4 and the engine worktree's uncommitted diff.

**Ran (short commands only, no z3).** `git log`, `git diff --stat` on both repos; a `diff` of the plan text above "### Results" between 56d3e4a and 54fe58f; a script that reads `transfer-summary.json` and prints edges, relief, nonzero deltas, unranked rules, out-transfer and cache counters per entry and k. I did not re-run any transfer graph or check.

## Findings

1. **green. The batch moves the thin path and opens no front in the dataset.** It is docs/plan.md "Next, in order" item 8 (Thin path item 4, Track A of the two-track note), and it is slice 3 as plans/priority.md defines it: transfer graph on kibbutz and MWPA, a `rebundling` property, the RuleCache measurement (Open questions, item 2), the T1 observation. d5d3a92..54fe58f touches only plans/priority-slice3.md and docs/ablation/2026-11-09-slice3/. No entry, rule, strand tag, property, verdict, baseline row, claim row or ENGINE_PIN (still e46f6ea) changed.
   fix: none.

2. **green. Preregistration precedes results and is append-only.** 56d3e4a (09:05:23) holds "(empty until the run)"; engine d763cb4 is 09:05:33; 54fe58f is 09:34:01. The 29 minute gap fits the longest reported entry (1512 s). The text above "### Results" is byte-identical between the two commits (`diff` of both versions cut at that heading: empty). The preregistration says plainly what it was not blind to (first-order loads, the engine code, one toy).
   fix: none.

3. **green. The committed engine diff stays inside the slice.** Six files, +493 -6: `transfer_graph` and friends in rules_ablate.py, `phil rules transfer`, the derived check, one fixture property row, one test file. `rules_gate.py` is untouched, as the Out of scope list promises. `ablate()` gains a `variants` argument whose default keeps the old rows; `applicable_which` skips derived properties so first-order ablation cannot read them.
   fix: none.

4. **amber. The engine worktree is dirty with fix-pass work done before council.** Uncommitted on top of d763cb4: the drift-3 fix (`kinds` threaded through `run_all`, `cmd_check`, `cmd_check_all`, `_run_reports`, `derived_check`), a new test, and the fixture expectation `"rebundling": "unreachable_open"` with the count moved 22/22 to 23/23. Two consequences. At d763cb4, the commit Results cites, no fixture entry lists `rebundling`, so Build item 7's "engine CI's check-all sees it" is not yet true there. And the plan's "Post-council fix pass (appended only)" is empty while the fix already exists. The fix also changes the call path of check-all for every entry (the argument is documented as read only by a derived check; I did not test that).
   fix: commit it as its own engine commit; name the hash in the fix pass; re-run `phil rules diff` (0 of 192) and the seven `rebundling` checks at that commit before the pin bump.

5. **amber. Results cites ledger rows that do not exist.** N79 (null graph), N80 (cost predictions missed) and N81 (T1 uninformative) are named, but docs/negative-results.md ends at N73. The drift rule in the preregistration requires these rows. docs/plan.md's Log and "Where to pick up" also have no slice 3 line.
   fix: add N79 to N81 and a Log line in the fix pass. N79 should be typed `null`, N80 `refuted`, N81 `untested`.

6. **amber. Pass test part 1 ("graph matches preregistered edges"): met, as a null, and on a small denominator.** Zero edges predicted, zero found, both graphs, both k, seven entries; the kibbutz relief pair and the D1 and D2 deltas hit exactly, which shows the pairwise machinery sees interactions and is not blind. But the headline hides how few pairs can carry an edge. Build items 3 and 4 together remove every `deregulated` row as source and target, and the `~prohibit` variant (the ranked cut of a permission since slice 1 revision 2 (c)) is not run. From `unranked_rules` in the summary, the pairs that can be a ranked edge are at most 6 of 30 (kibbutz), 30 of 90 (creditor-exemption, property), 30 of 110 (earnings, sole-trader), 42 of 132 (suit), 30 of 132 (property-narrowed). The one load that rises anywhere (R14 to R13, `freedom_down`) sits in the excluded region. It would not be an edge in any case, since revision 2 (b), ratified by the author, ranks on freedom-up only.
   fix: say "met by a preregistered empty graph (null, N79)" in docs/plan.md, never "passed"; add the ranked-pair denominator per entry to the Results headline (appended, not edited in).

7. **amber. Pass test part 2 ("`rebundling` property written and checked"): half met.** Written: in the engine fixture only (`data/example/properties.json`), not in `data/institutions/src/properties.yaml`. Checked: on the seven entries through an overlay properties file that is not in the repo, and the seven `phil rules check` outputs are not in docs/ablation/2026-11-09-slice3/ (the `.txt` files are `phil rules transfer` output). So the evidence that the derived check, as distinct from the report, printed `open` is one sentence in Results. Deferring the dataset rows to the pin bump is the right order (plan.md: "PR the engine first") and was preregistered.
   fix: save the overlay (or the one-row patch) and the seven check outputs beside the transfer outputs; call this part "engine side written; dataset rows pending the ENGINE_PIN bump".

8. **amber. Pass test part 3 ("T11 moves from three of four who-pays modes to four"): not met, and should not be claimed.** Three reasons, none of them the builder's fault, all named or half-named in P9.
   - The property is a relation over the rule set as written. ADR 0016 amendment 4 makes that the Rule-axis criterion and says who-pays modes "need a new actor or institution"; the table puts rebundling at lowest layer 3. The engine gloss itself says "not about what people do after a reform".
   - Three definitions now carry one word: glossary ("the same strands recombined under new names or roles"), ADR 0016 ("people retreat to another stronghold; remaining bonds become more load-bearing"), priority.md and the engine (a transfer edge onto a rule that reads tying). Only the second half of the ADR's sentence matches the third.
   - The starting count is already soft. T11's own evidence says `double_burden` is "partial reform (no mode)" and `creditor_shield` is Capture (Rule axis). On ADR 0016's current labels, two who-pays modes have a property (dark twin, backlash), not three.
   The row was not edited, which is why this is amber and not red.
   fix: T11 stays `untested`, count unchanged. Append to its evidence: "2026-11-09, slice 3: a layer-1 proxy (`rebundling`, derived check: a ranked freedom-up transfer edge onto a rule reading tying) exists in the engine fixture, not yet in the dataset; `open` on kibbutz and six MWPA entries at k=6,8; `reachable` only on a constructed toy. Not ADR 0016's layer-3 mode (no new actor or institution); RB still has no property at its own layer." T1 stays `untested`. Append: "2026-11-09, slice 3: out-transfer is 0 for every rule in seven entries (deletions only, ranked rows); a tie at zero, uninformative (N81)."

9. **green. "Tying" as the ablation reading, not the hand tag.** priority.md says an edge "whose target reads as a tying strand", and Readings are defined from loads; the hand tag is printed beside it. This is the plan's wording, not a new decision. Note for the record: R13 and R14 are hand-tagged tying and unranked, so this choice does not by itself decide any verdict here.
   fix: none.

10. **amber. Deletions only and unranked exclusion were decided alone and shape the null.** Both are flagged ASSUMED in the preregistration, which is honest, and both extend settled slice-1 conventions (deregulated deletions are listed, not ranked). But slice-1 pairs that convention with the `~prohibit` row so that a permission still has a ranked cut. Here it has none, so permissions are out of the graph entirely (finding 6). Slice 4's whack-a-mole test ("a rule with load above its starting load") inherits the same choice.
    fix: the author ratifies both, or orders a `~prohibit` rerun, before slice 4 is preregistered.

11. **amber. The derived check kind is a wider engine change than the slice's file list, with a cost tail.** The slice names `rules_ablate.py`, `properties.json` and optionally the gate. The batch added a fourth `CheckKind` and a branch in `run_all`, and made `formal` a documentation string for such rows. The reason given (check-all, verdicts and diff can see it) is sound, and the alternative is recorded. The cost is not: one `rebundling` row in an entry's `expected_properties` makes check-all pay a full pairwise ablation for that entry (13 to 25 minutes cold per entry here). Listing it on 33 entries would change what CI is.
    fix: before the pin bump, the author chooses derived check or report-only, and which entries list it; measure check-all wall time with the row on a warm and a cold cache first.

12. **green. Open question 2 is answered.** Cold hit rate 52 to 55%, 18 to 25 minutes per MWPA entry, 2.3 CPU-hours for seven. The two missed cost predictions are recorded as drift against P7 and F5 fired as stated. This is the number slice 4 needs for its budget.
    fix: none.

## Park

- `rebundling` rows in the dataset for any entry beyond the seven, and any gate criterion on it.
- Transfer graphs under `step_mode many`, `compliance sanctioned`, on `-no-implicit` or the other 25 entries.
- The T1 out-transfer test, until some entry has a nonempty ranked graph. A tie at zero should not be re-run in new forms.
- Reconciling the three definitions of rebundling by editing the glossary or ADR 0016 from inside a slice. That is an ADR amendment and the author's call (decision A).
- The R13 / R14 "substitute protections" and R1 / R2 "conjunctive pair" observations as theory points. They are worth one line each in the results and nothing more for now.

## Decisions for the author before slice 4 starts

A. **Name.** Either amend ADR 0016's rebundling row to "3 (1 as a rule-set proxy: a transfer edge onto a tying reading)", following the Backlash row's "1 when encoded as a branch" precedent, and bring the glossary into line; or rename the engine property so the who-pays word is not spent on a layer-1 relation. Until then T11 reads as in finding 8.
B. **Coverage.** Ratify deletions only plus unranked exclusion, or add `~prohibit` rows as sources and targets (finding 10). Slice 4 inherits the answer.
C. **Where slice 4 runs.** On these seven entries the pairwise graph is empty, so cut-set search and sequencing are likely a second null by construction. Decide whether slice 4 is preregistered on them anyway, or first picks entries where a first-order scan shows one family carried by two rules. Either is on the thin path; a foregone null is not progress on it.
D. **Derived check or report.** Finding 11, with the list of entries that carry the row at the pin bump.

## Verdict

Scope: **supported, with parks.** The batch moves the thin path and stays inside its preregistered scope. Tally: 5 green, 7 amber, 0 red. No red, so the batch does not pause; the ambers go to the fix pass, and decisions A to D go to the author before slice 4 is preregistered. Honest status of the plan's three-part pass test: part 1 met as a null; part 2 half met (engine only); part 3 not met.
