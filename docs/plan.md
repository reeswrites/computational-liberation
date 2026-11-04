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

## Next slice (2026-11-04, accepted): gate (a) and (b)
1. doing — Encode `footbinding` (Mackie 1996; pledge actions per A3) and `naming-convention` (Centola 2018; `committed_minority` recorded, not asserted) with preregistered verdicts; properties `binding_practised`, `new_convention_adopted`.
2. doing — Engine `coordination` module (assurance payoff, pledge flip, committed minority, `necessary_modules`); `imagination` stays a stub.
3. todo — Engine performance pass (accepted 2026-11-04): process pool over seeds in `phil abm run|sweep|gate` (seeds are independent; ~4x on 4 cores), pytest-xdist, per-letter and per-institution wall-clock in the gate report, memoize `breaches()` per step and role (profile: 22k calls per run). Builders iterate on targeted tests and small seed counts; full suite and 100-seed gate once at the end.
4. todo — Run `phil abm gate` on the new entries; council review of both encodings (encoding-faithfulness seat) and the module.
5. doing — README cold-visitor pass with diagrams (docs/overview.md, both READMEs).

## Log
- 2026-11-04 (afternoon) — Author accepted every pending decision: ADR 0016 council reds (the `narrowed` branch is Backlash again, Section 4 test exhaustive, "for whom" = the preregistered liberated role, orthogonality criterion, per-mode sweep criteria, provisional-taxonomy sentence); ADR 0015 A8 and the A1 per-instance-payoff extension accepted; kibbutz: R6 guarded (preregistered, revert on any flip), the coverture iso disagreement recorded not edited, R8 step-0 reading documented; L20 reworded, T11 evidence refreshed. Next slice opened: footbinding + naming-convention encodings and the coordination module.
- 2026-11-04 (later) — Slice 3 built, reviewed (weakened: gate (c) replayed the layer-1 verdict), fixed (two-axis sweep on the forbidden instance, preregistered and matched), and the A8 slice reviewed (weakened: breach rate mixed chosen and forced breach) and fixed (separate `unavoidable` series, diagnostics once per step). Engine tests 445 -> 467. Agent costs this stretch: ~830k tokens across 5 agents (slice 3 205k, two reviews 135k + 145k, two fix passes 143k + 200k). Batch total ~1.3M tokens across 9 agents.
- 2026-11-04 — Orchestrated batch, four agents in parallel then two: engine A8 + slice-2 fixes (435 -> 445 tests), kibbutz R8 (no flips), ADR 0016 council (correctness weakened, scope supported, consistency fixed). Commit hygiene slip: R8 and the A8 amendment were swept into neighbouring commits (d4dbd26, 72eded9) by a blanket add; history is correct, messages are not. Agent costs so far: ~460k tokens across 4 agents (engine 157k, kibbutz 116k, council 92k + 94k).
- 2026-11-03 (late) — Author accepted all pending decisions → ADR 0015 (layer 2 design), ADR 0010 amended, ADR 0011 index fixed, theory status split (Claude doc + local). Failure-mode axes added → ADR 0016 (3 axes, 11 modes, layer tags), MWPA relabels logged as drift, claim L20 weakened + review file. Engine slice 2: breach, directed trust, pledge, `phil abm sweep` (435 tests). Review: 2 red (one fixed in-session, one to tomorrow item 1). Agent costs this stretch: ~700k tokens across 6 agents. Stopped at 86% of the 5-hour window.
- 2026-11-03 (night) — Orchestrated batch: docs clarity audit + 7 fixes (claims tally corrected to 6/1/8/1/19; glossary gate table and 18 terms; README links); mwpa-suit test note resolved (engine 0a9c01e); layer 2 slice 1 + review + fix (1 bug: ABM availability stricter than ADR 0013, fixed to equal `Reference.power`). Builder reordered agent choice priority (payoff switch before threshold) to make the payoff test pass — a design choice made under test pressure, listed ASSUMED, needs a look. Decisions memo written. Agent costs: ~600k tokens across 6 agents.
- 2026-11-03 (evening) — Third council review: (a),(b) supported; (c),(d) weakened (strand/implicit tags are human inputs). Kibbutz R2 re-encoded as a norm; airline control added; interpretation guide; claims register tested in CI; MWPA backtest designed with sources and run at layer 1. Agent costs this batch: ~1.0M tokens across 8 agents.
- 2026-11-03 — Theory, intent, ADRs 0001–0013, institutions family built end to end, first gate "passed", skeptical review retracted the care+control claim; rebuild in progress. Repo prepared for public release.
- 2026-11-03 — Batch 2 kibbutz + third review + fix. Agent costs: kibbutz build ~167k tokens / 12 min; third review ~152k / 6 min; this fix (norm re-encode, airline control, docs) cost not metered inside the agent, see the session record. Gate (d) still PASS after re-encode; check-all 47/47; claims L6 weakened, L19 added.
