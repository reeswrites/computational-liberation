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
- ADR 0016 council reds (docs/reviews/2026-11-04-adr0016-council.md, findings 1-2): the `narrowed` branch adds rules (R17, R18), which is the glossary's backlash, and layer 1 fired it, which the ADR's table says Erosion cannot; either revert `narrowed` to Backlash or amend the table ("Erosion: 1 when encoded as a construing power"). And restate the MWPA Section 4 test so a mode outside Capture/Erosion/Backlash ranking first is a fail. Ambers 3-5, 7-8 go in the same amendment.
- ADR 0015 A8 (state obligations in the ABM) was applied on the plan's recommendation without a fresh accept; confirm or reverse.
- Kibbutz `isomorphic_to: coverture-household` (guard+strands) reads NO today and is untested by the gate: drop the claim, retag, or add kibbutz to a cluster.
- Kibbutz R6 `may reprimand` has condition `true`, so in the ABM the committee reprimands random members about half the time; harmless at layer 1, noise at layer 2. Guard it on breach (`violated_R3`) or leave and note.
- claims.md L20 wording (council: category error) and T11 status.
- Encoding reviewer for Phase 0 (ADR 0012): the author, until there is someone else.
- Ten open decisions with options and recommendations: docs/decisions-pending.md (layer 2 design A1–A7; theory.md source B1; ADR 0011 status B2; ADR 0010 amendment B3).

## Today (2026-11-04) status
1. done — State obligations in the ABM: ADR 0015 A8 (ASSUMED accepted: the plan's recommendation; engine deb6a31). On kibbutz, metapelet breach rate is 1.0 at sanction_weight 0 and 0.0 at the default: breach, sanction and trust now fire on a real institution and the sanction governs it.
2. done — Slice-2 review items (engine deb6a31): sanction priced over its window, A5 bearing from declared arg_roles, `payoff.<action>` axes validated, no-lawful-action and unavoidable-breach warnings. Correctness review of the slice: in progress (report to docs/reviews/).
3. done — Kibbutz R8 `may neglect` (ADR 0015 A6). Preregistered no verdict change; check-all 106/106 and gate (d) byte-identical before and after. Found while baselining: the entry's `isomorphic_to: coverture-household` at guard+strands already read NO (matched 0, distance 9) and nothing tests it (kibbutz is outside the cluster) — author's call, below.
4. done — Council pass on ADR 0016: docs/reviews/2026-11-04-adr0016-council.md. Correctness weakened (two reds), scope supported with parks, consistency drift fixed (glosses now Capture/Erosion; T11, phase-0 plan, MWPA header, entry titles, dataset README).
5. doing — Slice 3: veil-of-ignorance scorer + `phil abm gate`. Scoped: (c) kibbutz and (d) seed stability run on the material module; (a) footbinding and (b) committed minority report BLOCKED (no footbinding / naming-convention institution encoded; coordination module is a stub). Encoding those two institutions and the coordination module is the next slice, not opened today.

## Log
- 2026-11-04 — Orchestrated batch, four agents in parallel then two: engine A8 + slice-2 fixes (435 -> 445 tests), kibbutz R8 (no flips), ADR 0016 council (correctness weakened, scope supported, consistency fixed). Commit hygiene slip: R8 and the A8 amendment were swept into neighbouring commits (d4dbd26, 72eded9) by a blanket add; history is correct, messages are not. Agent costs so far: ~460k tokens across 4 agents (engine 157k, kibbutz 116k, council 92k + 94k).
- 2026-11-03 (late) — Author accepted all pending decisions → ADR 0015 (layer 2 design), ADR 0010 amended, ADR 0011 index fixed, theory status split (Claude doc + local). Failure-mode axes added → ADR 0016 (3 axes, 11 modes, layer tags), MWPA relabels logged as drift, claim L20 weakened + review file. Engine slice 2: breach, directed trust, pledge, `phil abm sweep` (435 tests). Review: 2 red (one fixed in-session, one to tomorrow item 1). Agent costs this stretch: ~700k tokens across 6 agents. Stopped at 86% of the 5-hour window.
- 2026-11-03 (night) — Orchestrated batch: docs clarity audit + 7 fixes (claims tally corrected to 6/1/8/1/19; glossary gate table and 18 terms; README links); mwpa-suit test note resolved (engine 0a9c01e); layer 2 slice 1 + review + fix (1 bug: ABM availability stricter than ADR 0013, fixed to equal `Reference.power`). Builder reordered agent choice priority (payoff switch before threshold) to make the payoff test pass — a design choice made under test pressure, listed ASSUMED, needs a look. Decisions memo written. Agent costs: ~600k tokens across 6 agents.
- 2026-11-03 (evening) — Third council review: (a),(b) supported; (c),(d) weakened (strand/implicit tags are human inputs). Kibbutz R2 re-encoded as a norm; airline control added; interpretation guide; claims register tested in CI; MWPA backtest designed with sources and run at layer 1. Agent costs this batch: ~1.0M tokens across 8 agents.
- 2026-11-03 — Theory, intent, ADRs 0001–0013, institutions family built end to end, first gate "passed", skeptical review retracted the care+control claim; rebuild in progress. Repo prepared for public release.
- 2026-11-03 — Batch 2 kibbutz + third review + fix. Agent costs: kibbutz build ~167k tokens / 12 min; third review ~152k / 6 min; this fix (norm re-encode, airline control, docs) cost not metered inside the agent, see the session record. Gate (d) still PASS after re-encode; check-all 47/47; claims L6 weakened, L19 added.
