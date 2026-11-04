# Plan (living)

Revised whenever a batch lands. Status words: todo · doing · done · parked · blocked. Keep it short; history is in git.

## Goal
Compute liberation: given institutions as rules and candidate changes, say which change to make first and what it sets off. Five layers (docs/theory.md, Roadmap). No forward claim until layer 3 passes.

## Thin path (do these in order; everything else waits)
1. doing — Layer 1 passes the second skeptical review (power derived from rules, breakers for every obligation, negative controls, gate reads precommitted levels). Owner: build agent + council.
2. done — Added kibbutz-childrens-house and hit gate (d) (PASS); third review weakened the claim (L6) and R2 is now a sanctioned norm.
3. doing — One backtest end to end: Married Women's Property Acts (layer 1 run 2026-11-03: direction PASS, every preregistered flip matched; failure modes reachable but unranked, so inconclusive until layer 2; ordering test needs layer 2 + state dates) (plans/backtest-data-inventory.md), chosen because it can land both of the author's falsifiers (docs/intent.md). Verify dates first.
4. todo — First priority computation on the institutions already encoded; report per-module (freedom, flourishing) and combined.

## Parked (written, not started; revisit after step 3)
- Batch-2 institutions other than kibbutz (family-wage, fair-play-domains, gig-platform, ostrom-fishery and their pairs).
- Non-human institutions (plans/institutions-phase0.md, Extension).
- Layer 2 agent-based model (plans/layer2-abm.md): slice 1 built 2026-11-03 in philosophy-engine (`phil abm run --seeds N`, material module only, engine commits a1b2a6c + 4f55306, 14 tests). Blocked on design decisions A1–A6 in docs/decisions-pending.md (breach A4 and unruled actions A6 gate the footbinding/kibbutz tests). Not parked any more; next slice after decisions.
- Worked examples for the interpretation guide (docs/interpreting-results.md exists).
- Methods write-up and blog posts (after step 3).
- Launch checklist (after step 3; gate: one falsifiable result that survived or failed honestly). Blog post first, thread second, repo in reply. Lead with the MWPA preregistered-verdicts table, not the theory; claims-register tally as the differentiator; one ask ("encoding reviewer wanted"). Prep now, cheap: README cold-visitor pass (one agreed headline across README/theory/claims), a current Status line, demo gif of `phil rules gate`.
- Weekly scheduled consistency review.
- Parked by the ADR 0016 scope seat until the layer 2 gate exists: mode tagging in ABM reports, Enforcement decay, Lock-in, the mechanism tag; preregistrations name only modes at or below the run's layer.
- Footbinding and naming-convention encodings (gate (a), (b)) and the coordination/imagination modules: next layer-2 slice.
- Airline control: gate support for expected-match controls (engine change), then move `airline-flight` into the cluster's control list as an expected-match check.
- Strand-tag redesign: strand tags are hand inputs the cluster match depends on (third review); find a derivation or a robustness test.

## Standing process
- Preregistration: expected verdicts are written before runs and never edited to match; drift is recorded (CONTRIBUTING.md).
- Council after every batch (docs/decisions/0014-review-council.md): correctness, consistency, scope, encoding faithfulness; fresh agents, never the builder. Reports go in docs/reviews/.
- docs/claims.md is the honest summary; README points to it. CI fails if a `supported` claim has no passing evidence (todo).
- This file is revised at the end of each batch.

## Housekeeping after the split (2026-11-03)
- todo — Decouple philosophy-engine tests from data/institutions (move dataset-dependent tests here, or skip when PHIL_DATA_DIR has no institutions), then delete from philosophy-engine: data/institutions/, docs/theory.md, intent.md, plan.md, claims.md, docs/reviews/, plans/, ADRs 0001/0005/0006/0007/0008/0010/0011/0012/0014 (rebuild its index). Keep glossary and CONTRIBUTING in both.
- todo — Split ADR 0007 and 0010 into theory/process halves (here) and engine halves (there).
- todo — Re-export docs/theory.md from the Claude doc when the theory changes; make this file canonical once it stabilises.

## Decisions waiting on the author
- Encoding reviewer for Phase 0 (ADR 0012): the author, until there is someone else.
- (All 2026-11-04 decisions accepted by the author in-session; see the log and ADR 0016's council amendment.)

## Restart list (2026-11-04, evening; in order)
1. todo — Engine fix pass on slice 4 (docs/reviews/2026-11-04-abm-slice4-review.md): (1) dataset-backed test asserts (a) BLOCKED, now FAIL/BLOCKED; (2) gate (a) persistence arm vacuous: needs `initial_practice: bind` on both footbinding entries (dataset) and a step-0 share guard; gate (a) must read two pledge actions (family + suitor) since the encoding fix; (6) committed-minority draw perturbs the rng stream, use a child rng; (7) the max-share threshold rule puts an implicit 0.5 in the (b) location: restate (b) honestly or compare against θ only; docstrings for 4, 5, 9; add the crit_c band condition to (a) (8).
2. todo — Then rerun `phil abm gate --seeds 100 --workers 4` (~5 min now) and record.
3. todo — Council consistency seat: reconcile plans/layer2-abm.md "Sources opened" with the entries' "never opened"; ADR 0011 status differs between repos; engine ADR index lacks pointers to 0015/0016.
4. done — Footbinding + naming-convention encoded, reviewed (faithful with reservations), fixes applied with preregistration committed before the run (b6f48aa → 584ef7d); `marriage_requires_binding` flagged by construction.
5. done — Coordination module (engine 20f60d7), reviewed weakened; performance pass (engine 8e246b7): 45 min → 5 min gate, 3.3 min → 1 min tests, outputs identical.
6. done — README cold-visitor pass with diagrams.

## Decisions waiting on the author (from slice 4; see the slice-4 review's closing paragraph)
- **A2 per-agent pledge state**: necessary but not sufficient for Mackie's mechanism. Also give the pledge a cost or zero payoff and set `initial_practice: bind`; otherwise (a) is decided by step-0 ties.
- **Sanction-in-force reading**: keep (no layer-2 number changed on kibbutz, cps, paternity-quota) with the docstring caveat that a sanction conditioned on a fluent the breach clears never lands.
- **Gate (b) criterion**: the plan's "jump > 0.5" fails on this mechanism (0.19); restate as a location-in-band test, or keep and record.
- `marriage_requires_binding`: redefine via `married` or drop; `new_cohort` action for footbinding (one-cohort layer 1).
- Reserved `payoffs`-block keys as the declaration mechanism.

## Standing process
- Preregistration: expected verdicts are written before runs and never edited to match; drift is recorded (CONTRIBUTING.md).
- Council after every batch (docs/decisions/0014-review-council.md): correctness, consistency, scope, encoding faithfulness; fresh agents, never the builder. Reports go in docs/reviews/.
- docs/claims.md is the honest summary; README points to it. CI fails if a `supported` claim has no passing evidence (todo).
- This file is revised at the end of each batch.

## Housekeeping after the split (2026-11-03)
- todo — Decouple philosophy-engine tests from data/institutions (move dataset-dependent tests here, or skip when PHIL_DATA_DIR has no institutions), then delete from philosophy-engine: data/institutions/, docs/theory.md, intent.md, plan.md, claims.md, docs/reviews/, plans/, ADRs 0001/0005/0006/0007/0008/0010/0011/0012/0014 (rebuild its index). Keep glossary and CONTRIBUTING in both.
- todo — Split ADR 0007 and 0010 into theory/process halves (here) and engine halves (there).
- todo — Re-export docs/theory.md from the Claude doc when the theory changes; make this file canonical once it stabilises.

## Decisions waiting on the author
- Encoding reviewer for Phase 0 (ADR 0012): the author, until there is someone else.
- (All 2026-11-04 decisions accepted by the author in-session; see the log and ADR 0016's council amendment.)

## Next slice (2026-11-04, accepted): gate (a) and (b)
1. done — `footbinding` + `footbinding-no-pledge` (Mackie 1996; sources mostly UNVERIFIED, network refused every page) and `naming-convention` (Centola 2018, cited from memory, UNVERIFIED) encoded with preregistered layer-1 verdicts; check-all 115/115, layer-1 gate PASS, 23 entries. Encoding-faithfulness review owed.
2. done — Engine `coordination` module (slice 4, engine 20f60d7, 479 tests): assurance payoff, pledge flip, `committed_minority`, `initial_practice`, sanction-in-force reading, `necessary_modules`; gate runs six configurations. Correctness review owed.
3. todo — Performance pass (see below) BEFORE the next full gate: the 50-seed six-configuration gate took 45 min single-core.
4. todo — Full `phil abm gate --seeds 100` on the 23 entries with the merged naming entry; record in plans/layer2-abm.md. Early results (engine 20f60d7, 50 seeds, before naming merged): (a) FAIL at every grid point; (c) PASS under all three configs; (d) Spearman 0.805 over 22 (was 0.966 over 20), needs the 100-seed rerun; (b) BLOCKED then, now runnable; the toy sweep shows a smooth rise (max adjacent jump 0.20), so the plan's "jump > 0.5" will likely FAIL.
5. todo — Council: correctness seat on slice 4, encoding-faithfulness seat on the two new entries.
6. todo — Engine performance pass: process pool over seeds in `phil abm run|sweep|gate` (~4x on 4 cores), pytest-xdist, per-letter and per-institution wall-clock in the gate report, memoize `breaches()` per step and role.
7. done — README cold-visitor pass with diagrams (README.md, docs/overview.md, engine README).

## Decisions waiting on the author (from slice 4)
- **A2 per-agent pledge state.** Gate (a) fails honestly: with role-level state one family's pledge sets `pledged(family)` for all and lifts the marriage sanction R5 for everyone, so `material` alone reproduces collapse once leaving unbound out-pays binding (100%), while `coordination` alone gives 48%. Mackie's mechanism (assurance among pledgers) needs per-agent `pledged`, which is the deferred A2. Decide: per-agent state for pledge fluents now, or accept (a) as not testable on shared state.
- **Sanction-in-force reading** (slice 4 ASSUMED 7): an `or_else` lands only if some instance of the named rule has its condition true in the successor; kibbutz unchanged, cps R3 and paternity-quota R3 now deferred until their trigger holds. Keep or revert.
- **Gate (b) criterion.** Threshold dynamics give a sigmoid, not Centola's step; "adoption jumps > 0.5 between adjacent sweep points" will fail. Options: keep the criterion and record the failure; or restate (b) as "the crossing location is inside Centola's 21-31% band and moves with thresholds/graph, no constant sets it". Not tuned.
- Reserved `payoffs`-block keys (`coordinated`, `committed_action`, `initial_practice`) as the declaration mechanism (slice 4 ASSUMED 1).

## Standing process
- Preregistration: expected verdicts are written before runs and never edited to match; drift is recorded (CONTRIBUTING.md).
- Council after every batch (docs/decisions/0014-review-council.md): correctness, consistency, scope, encoding faithfulness; fresh agents, never the builder. Reports go in docs/reviews/.
- docs/claims.md is the honest summary; README points to it. CI fails if a `supported` claim has no passing evidence (todo).
- This file is revised at the end of each batch.

## Housekeeping after the split (2026-11-03)
- todo — Decouple philosophy-engine tests from data/institutions (move dataset-dependent tests here, or skip when PHIL_DATA_DIR has no institutions), then delete from philosophy-engine: data/institutions/, docs/theory.md, intent.md, plan.md, claims.md, docs/reviews/, plans/, ADRs 0001/0005/0006/0007/0008/0010/0011/0012/0014 (rebuild its index). Keep glossary and CONTRIBUTING in both.
- todo — Split ADR 0007 and 0010 into theory/process halves (here) and engine halves (there).
- todo — Re-export docs/theory.md from the Claude doc when the theory changes; make this file canonical once it stabilises.

## Decisions waiting on the author
- Encoding reviewer for Phase 0 (ADR 0012): the author, until there is someone else.
- (All 2026-11-04 decisions accepted by the author in-session; see the log and ADR 0016's council amendment.)

## Next slice (2026-11-04, accepted): gate (a) and (b)
1. doing — Encode `footbinding` (Mackie 1996; pledge actions per A3) and `naming-convention` (Centola 2018; `committed_minority` recorded, not asserted) with preregistered verdicts; properties `binding_practised`, `new_convention_adopted`.
2. doing — Engine `coordination` module (assurance payoff, pledge flip, committed minority, `necessary_modules`); `imagination` stays a stub.
3. todo — Engine performance pass (accepted 2026-11-04): process pool over seeds in `phil abm run|sweep|gate` (seeds are independent; ~4x on 4 cores), pytest-xdist, per-letter and per-institution wall-clock in the gate report, memoize `breaches()` per step and role (profile: 22k calls per run). Builders iterate on targeted tests and small seed counts; full suite and 100-seed gate once at the end.
4. todo — Run `phil abm gate` on the new entries; council review of both encodings (encoding-faithfulness seat) and the module.
5. doing — README cold-visitor pass with diagrams (docs/overview.md, both READMEs).

## Log
- 2026-11-04 (night, wound down for usage) — Performance pass landed (pool over seeds, memoised readings, timing, xdist). Reviews: coordination slice weakened (suite fails with footbinding present, (a) persistence vacuous, max-share rule sets the (b) location); encodings faithful with reservations, fixes applied with preregistration committed before the run (first time the order is in git). 100-seed six-configuration gate: (a) BLOCKED, (b) FAIL 0.19, (c) PASS, (d) PASS 0.95-0.96 over 23. Agent costs this stretch: ~730k tokens across 5 agents (perf 252k, slice-4 review 176k, encoding review 128k, dataset fixes ~170k). Day total ~3.0M across 20 agents.
- 2026-11-04 (evening, spun down at the author's request until the session reset) — Next slice: footbinding + naming-convention encoded (branches merged, 23 entries, 115/115), coordination module built (479 tests), gate (a) runs and fails honestly (shared state lets one pledge lift the sanction for all), README pass with five Mermaid diagrams and docs/overview.md. Kibbutz R6 guard tried and reverted (flips care_and_sanction_same_role to vacuous). All 2026-11-04 decisions applied. Agent costs this stretch: ~1.0M tokens across 6 agents (docs 109k, kibbutz 119k, footbinding 169k, naming 178k, coordination 242k, README 202k). Day total ~2.3M across 15 agents.
- 2026-11-04 (afternoon) — Author accepted every pending decision: ADR 0016 council reds (the `narrowed` branch is Backlash again, Section 4 test exhaustive, "for whom" = the preregistered liberated role, orthogonality criterion, per-mode sweep criteria, provisional-taxonomy sentence); ADR 0015 A8 and the A1 per-instance-payoff extension accepted; kibbutz: R6 guarded (preregistered, revert on any flip), the coverture iso disagreement recorded not edited, R8 step-0 reading documented; L20 reworded, T11 evidence refreshed. Next slice opened: footbinding + naming-convention encodings and the coordination module.
- 2026-11-04 (later) — Slice 3 built, reviewed (weakened: gate (c) replayed the layer-1 verdict), fixed (two-axis sweep on the forbidden instance, preregistered and matched), and the A8 slice reviewed (weakened: breach rate mixed chosen and forced breach) and fixed (separate `unavoidable` series, diagnostics once per step). Engine tests 445 -> 467. Agent costs this stretch: ~830k tokens across 5 agents (slice 3 205k, two reviews 135k + 145k, two fix passes 143k + 200k). Batch total ~1.3M tokens across 9 agents.
- 2026-11-04 — Orchestrated batch, four agents in parallel then two: engine A8 + slice-2 fixes (435 -> 445 tests), kibbutz R8 (no flips), ADR 0016 council (correctness weakened, scope supported, consistency fixed). Commit hygiene slip: R8 and the A8 amendment were swept into neighbouring commits (d4dbd26, 72eded9) by a blanket add; history is correct, messages are not. Agent costs so far: ~460k tokens across 4 agents (engine 157k, kibbutz 116k, council 92k + 94k).
- 2026-11-03 (late) — Author accepted all pending decisions → ADR 0015 (layer 2 design), ADR 0010 amended, ADR 0011 index fixed, theory status split (Claude doc + local). Failure-mode axes added → ADR 0016 (3 axes, 11 modes, layer tags), MWPA relabels logged as drift, claim L20 weakened + review file. Engine slice 2: breach, directed trust, pledge, `phil abm sweep` (435 tests). Review: 2 red (one fixed in-session, one to tomorrow item 1). Agent costs this stretch: ~700k tokens across 6 agents. Stopped at 86% of the 5-hour window.
- 2026-11-03 (night) — Orchestrated batch: docs clarity audit + 7 fixes (claims tally corrected to 6/1/8/1/19; glossary gate table and 18 terms; README links); mwpa-suit test note resolved (engine 0a9c01e); layer 2 slice 1 + review + fix (1 bug: ABM availability stricter than ADR 0013, fixed to equal `Reference.power`). Builder reordered agent choice priority (payoff switch before threshold) to make the payoff test pass — a design choice made under test pressure, listed ASSUMED, needs a look. Decisions memo written. Agent costs: ~600k tokens across 6 agents.
- 2026-11-03 (evening) — Third council review: (a),(b) supported; (c),(d) weakened (strand/implicit tags are human inputs). Kibbutz R2 re-encoded as a norm; airline control added; interpretation guide; claims register tested in CI; MWPA backtest designed with sources and run at layer 1. Agent costs this batch: ~1.0M tokens across 8 agents.
- 2026-11-03 — Theory, intent, ADRs 0001–0013, institutions family built end to end, first gate "passed", skeptical review retracted the care+control claim; rebuild in progress. Repo prepared for public release.
- 2026-11-03 — Batch 2 kibbutz + third review + fix. Agent costs: kibbutz build ~167k tokens / 12 min; third review ~152k / 6 min; this fix (norm re-encode, airline control, docs) cost not metered inside the agent, see the session record. Gate (d) still PASS after re-encode; check-all 47/47; claims L6 weakened, L19 added.
