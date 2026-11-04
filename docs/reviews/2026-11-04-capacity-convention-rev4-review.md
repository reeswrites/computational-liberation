# Council review: slice 1 revision 4, "one convention for default capacities" (correctness and encoding-faithfulness seats)

Date: 2026-11-04 local (commit-date convention, plans/priority-slice1-results.md:196). Fresh reviewer (ADR 0014); did
not build this. Read-only; this file is the only write. Follows up docs/reviews/2026-11-05-liberty-flag-rev3-review.md.

Subject: computational-liberation a7ca980 (preregistration), 2d83419 (dataset), 726e39f + 4b780c0 (results);
philosophy-engine faefef1, 7dc108c, 5275d11, 5cd81a0. The engine moved during the review: 3da984b (dataset sync) and
e53a442 (ablate scoreboard rows, `liberty` alias dropped) landed at 18:25-18:26, and computational-liberation 2b2584e
(layer-2 gate rerun, ENGINE_PIN -> e53a442) at 18:29. Engine code was read at e53a442; where a line differs from 7dc108c
it is said.

Targeted tests run: `PHIL_START_METHOD=spawn uv run pytest -q tests/test_rules_ablate.py -k "default_capacity or
deregulat or spawn" tests/test_rules_default_capacity.py` -> 11 passed.

Artefacts read (not committed; scratchpad of the author's session): ablate-25-v6.json / -summary.json (18:23),
ablate-25-v5-summary.json (rev 3, 16:29), rev4-gate.txt, rev4-diff.txt (16:52), gate-rerun.json (18:28).

## 1. Preregistration integrity: [green]

Order by `git log --format='%h %ci %s'`: a7ca980 16:48:08 (preregister) < 5275d11 16:48:39 (engine: verdicts/diff
tooling, no semantics) < 971d279 16:49:20 (golden baseline from the pre-change dataset) < 2d83419 16:51:17 (dataset)
< faefef1 16:52:20 (rename + sanctioned-must_not pin) < 726e39f 16:53:30 (predictions 1-2 recorded) < 7dc108c 18:22:02
(spawn pool) < 4b780c0 18:24:29 (predictions 3-6 recorded). `git diff a7ca980 HEAD -- plans/priority.md` is empty: not
a line of the preregistration changed, appended or otherwise. The results table (plans/priority-slice1-results.md:
216-225) restates each prediction in its own terms and the v6 summary bears them out row for row (tops, R4 flips in
exactly the six entries, `families_up` = [no_standing], 335 rows per k = 383 - 48, totals 0/0; checked against the
artefact, not the prose). Two things the record should say and does not: the layer-1 diff artefact kept for the run
(rev4-diff.txt) printed "0 changed, 0 added, 0 removed (of 123 rows)" and then exited 1 (`scoreboard.append_row`
header mismatch, cli_rules.py:236); the count stands, the exit code should be stated. And the scoreboard rows read
`dirty+5275d11` / `dirty+faefef1`: the engine tree was dirty when layer 1 ran; say what was dirty, or rerun at the pin.

## 2. One convention: [green]

A script over data/institutions/institutions.json finds 35 `default_capacity: true` action declarations (the README's
count) and exactly seven surviving `may` rules on flagged actions: police-crisis R10 (`may sue`, true), crisis-team R5
(`may leave`, true) and R9 (`may sue`, true), public-library R4 (`may leave`, true), mwpa-sole-trader R15 and mwpa-suit
R15 (`may contract`, true), mwpa-suit R16 (`may sue when married`). All seven are the preregistration's six kept items
(plans/priority.md:133 lists "mwpa-sole-trader/suit R15" as one item). No leak. The rev-3 item 1 is closed: there is one
mechanism (the flag) and the surviving `may` rows are explicit, sourced, `implicit: false`, and redundant for
enablement, which the README says (data/institutions/README.md:421-424). companion-* `sue` is unflagged with a stated
reason (README:409-410), which is the "by default for that kind of agent" clause the rev-3 review asked for.

## 3. Default-capacity skip in rules_ablate.py: [green] for (a) and (b); [amber] for (c)

(a) rules_ablate.py:252-256: for a deleted `may` on an action aim, `deregulated = head not in regulated_actions(inst2)
and not default_cap`; a sole-may deletion on a flagged action is not flagged. (b) `default_cap` is False for a power
action, so the same deletion is flagged; tests/test_rules_ablate.py:332 pins both on one fixture (R3 `may exit`, with
and without the flag). The 25-entry run agrees: the six kept permissions are absent from every `deregulated_not_ranked`
list in ablate-25-v6-summary.json. At 7dc108c line 254 also read the dead `getattr(decl, "liberty", False)`; e53a442
removed it with the alias. (c) The prohibit variant (rules_ablate.py:258-263) reads only `TRUE_WORDS` and
`regulated_actions(inst2)` (rules_lower.py:95-98 counts may/must only); the flag does not reach it. Consequence, visible
in the artefact: mwpa-suit `R16~prohibit` is listed `offcondition_free_not_ranked`, with a real flip (`no_standing`
open -> reachable at k=6) that is the faithful reading of turning `may sue when married` into a disability. The label's
rationale ("off-condition the action is free because no may remains") is a power-action rationale; for a default
capacity, off-condition freedom is the convention, not a leak. Tops are unaffected (the flip is freedom_down, load up
0), but the flag misdescribes the row and would exclude a freedom_up flip of the same shape. `permission_removed`
(:257) is likewise set on capacity-action deletions where permission never enabled anything; cosmetic.

## 4. Spawn parallelism: [amber]

Rows-identical serial vs spawn is tested on the keeper_free fixture (tests/test_rules_ablate.py:317; includes a
prohibit variant, no default-capacity action). No 25-entry serial-vs-parallel artefact was kept for revision 4
(time_ablate.py in the scratchpad compares workers 1 vs 4 but its output was not saved; ablate-w1/w2.txt are the
fixture). Module-level mutable state a spawned worker would not see, besides UNFREEDOM (now shipped per job,
rules_ablate.py:228, 333; monkeypatched at tests/test_rules_ablate.py:103, 121, 196, 217, 245, 255, 264, 278, 305):
- `rules_ablate._BASE` (:210): per-process memo of the base report, keyed on entry JSON, k, run options and the
  property set; deterministic, so divergence is impossible, only duplicated work. Benign.
- `rules_checks._LOG` and `_CTX` (:66-67): the z3 timing/unknown log, mutated by every query and drained inside
  `run_all` (:255ff) in the same process, so `z3_unknown` travels in the returned result; parent-side `--timing`
  would not see worker timings. Cosmetic.
- `rules_checks._check` is monkeypatched by tests/test_review_fixes.py:58 and tests/test_rules_cache.py:187; a spawned
  worker imports the real one. No test combines it with workers > 1, and nothing guards it; a future test that does
  will pass vacuously. Worth a one-line assertion in `run_map` or a note in parallel.py's docstring.
- `config.*` constants (Z3_TIMEOUT_MS and friends) are read from the environment at import; spawn inherits the
  environment and no runtime assignment to `config.X` exists in philengine (tests patch `config.ISO_MAX_PREDS`,
  test_review_fixes.py:139, outside the ablate path). Fine.
- `parallel._ACTIVE / _ACTIVE_WORKERS / _ACTIVE_METHOD / _INHERITED`: by design; the docstring says `_INHERITED`
  falls back to serial under spawn.
No `RuleCache` crosses the pool: cli_rules.py:363 calls `ablate_multi_k` without `cache`. Nothing here can change a
row; the amber is for the untested real-dataset equality and the unguarded `_check` patch.

## 5. Encoding faithfulness of the convention: [amber]

Of the 24 deleted rows, 17 were `implicit: true` with "implicit:" sources (coverture R8 x7, police R9, cps R9,
companion R12 x3, kibbutz R7 x2, footbinding R8 x2, airline R5); nothing sourced is lost there. The seven coverture-chain
R9 rows were `implicit: false` and cited Blackstone I.15 for "a feme sole may sue and be sued; it is marriage that
suspends her legal existence" (a7ca980:institutions.json, coverture-household R9 source). After 2d83419 no rule, note
or declaration in the chain cites Blackstone for the capacity to sue: R4's gloss says "a default capacity, which this
disability removes while married" and `grep "feme sole"` hits only the property-narrowing and animal-iso notes. The
deletion itself is right under the one-convention rule: keeping R9 would reinstate the second convention (a `may` with
condition `(not married)` doing the flag's work), and `(not married)` is literally "no R4 disability holds". What is
lost is the citation that grounds the encoder's judgment to flag `sue`, which the README (:405-407) says must be made
before any run; the judgment now rests on nothing in the data file. Move the Blackstone sentence onto the `sue`
declaration (a `source` on the action, or the entry notes), as mwpa-suit R16 keeps Geddes et al. for the restored
capacity. `petition` (cps R11, `child may petition when counsel_appointed`, UNVERIFIED): a conferred power is the
defensible reading, since a minor has no default capacity to claim in their own name and WIC 317(e) confers it through
appointed counsel; the asymmetry adult `sue` = capacity / child `petition` = power is faithful but unstated. Its
consequence should be recorded: cps `no_standing` reads through a conferred power, so deleting R11 flips `no_standing`
open -> reachable and the row is `deregulated`, never ranked (ablate-25-v6.json, cps R11).

## 6. ADR 0013 amendment after the rename: [amber]

docs/decisions/0013-derived-power-fluents.md, amendment "default-capacity actions": the mechanism is now stated
correctly ("A default capacity is what a person of that kind can do unless an express disability removes it ...; a
power, the default for actions, exists only when a may/must confers it"), the sanctioned-must_not choice is recorded
("Decided 2026-11-04: only a disability ... removes a default capacity; a sanctioned must_not leaves the capacity in
place ... Pinned by test", tests/test_rules_default_capacity.py:135), and the ABM effect is in the trailing Note. Three
things lag: the heading and "Experiment" line still say 2026-11-05 against the stated commit-date convention; the Note
still says the layer-2 record "is not guaranteed to reproduce" and the docstring "is out of date", while
plans/layer2-abm.md:122 now records the rerun (all four verdicts reproduce, (d) 0.950 vs 0.963 over a different entry
set, honestly flagged as not the same measurement); and philengine/abm/model.py:8 is still stale: "An action no
may/must rule names is never available to an agent." is false for a default-capacity action, which is exactly the
case the Note was written about. Also stale after the rename: docs/claims.md L23 (flag named `liberty`,
tests/test_rules_liberty.py, which no longer exists) and data/institutions/README.md:399 ("the engine accepts both
keys"; e53a442 dropped the alias and ENGINE_PIN is now e53a442).

## 7. Overclaim check: [amber]

"Drift: none" is accurate for what was tested; predictions 1, 3 and 4 are specific and could have failed (prediction
4 names every top set). Three clauses could not: prediction 5's "`deregulated_not_ranked` and
`offcondition_free_not_ranked` lists lose exactly those ids" (deleted rows cannot appear in any list); prediction 6
("rediscovery is not claimed") is a disclaimer, not a prediction, and its "none made" row is padding; and prediction
2's "the airline control still match[es] at the precommitted level" names a test the gate does not run (airline-flight
has `isomorphic_to: []`, no `not_isomorphic_to`, and is not a gate-(b) control; the controls are lease, public-library,
naming-convention), yet the results row repeats "airline control ... unchanged: held". Prediction 2's real content
(partial(care+control) at guard+strands for the six directed pairs, crisis-team none, controls none) did hold
(rev4-gate.txt). Say which clauses were untestable rather than counting them held.

## Verdict: sound

The convention is single, the dataset matches the preregistration, no prediction was edited, the engine skip does what
it says, and the run reproduces from the artefacts. The ambers are record hygiene (a lost citation, a stale docstring
and claim row, two vacuous prediction clauses, an exit-1 artefact) and one mislabel (`offcondition_free` on a
default-capacity prohibit variant) with no effect on any top set.

## What the author must decide

1. Put the Blackstone feme-sole citation back where the `sue` flag can be read against it: a `source` on the action
   declaration in the coverture chain (generator kwarg) or a sentence in each chain entry's notes. The flag is "an
   encoder's judgment made before any run"; its evidence should not live only in git history.
2. Decide whether the prohibit variant of a `may` on a default-capacity action is `offcondition_free` at all. Either
   skip the label when `default_cap` is true (rules_ablate.py:258-263, mirroring :256) and say that mwpa-suit
   `R16~prohibit` now ranks (its flip is freedom_down, so no top moves), or record in the README that the label is
   kept by the power-action rationale and why. Add the case to tests/test_rules_ablate.py:332.
3. Fix philengine/abm/model.py:8 and the ADR 0013 Note (rerun done; docstring fixed), and the two stale names:
   docs/claims.md L23 (`default_capacity`, tests/test_rules_default_capacity.py) and README:399 ("accepts both keys").
4. State in the revision-4 results that rev4-diff.txt exited 1 after printing the counts, what `dirty+` covered on the
   scoreboard rows, and that two engines (faefef1 layer 1, 7dc108c ablation) were used; or rerun both at ENGINE_PIN.
5. Record in the results table which prediction clauses were untestable (5's "lose exactly those ids", 6, 2's airline
   clause) instead of "held"; keep the convention that a disclaimer is not a numbered prediction.
6. Record the `petition` decision in the dataset README under "Default-capacity actions": a minor's claim is a conferred
   power (through counsel), an adult's `sue` is a default capacity; note that cps R11 is therefore never ranked.
7. Either keep one serial 25-entry ablation artefact per engine bump for row equality against the parallel run, or
   extend tests/test_rules_ablate.py:317 with a default-capacity action and a non-true-condition `may` so the spawn
   path covers every branch of `_ablate_one`; and guard or document that monkeypatches of `rules_checks._check` do
   not reach spawned workers.
8. Date hygiene: the ADR 0013 amendment heading and its "Experiment 2026-11-05" line predate the convention stated at
   plans/priority-slice1-results.md:196; either relabel to the commit date or add the convention note to the ADR.
