# layer 2: agent-based Phase 1 plan

Agent-based layer over the same `InstitutionJSON` that `phil rules` checks. **Phase 1 scope:** instantiate simple
adaptive agents from `roles`, let them pick among rule-enabled actions, run three switchable mechanism modules
(material, coordination, imagination), score runs under a veil of ignorance, and backtest four historical cases.
Layer 1 says what rules permit or force (ADR 0004); this layer says what adaptive agents under those rules do, how
often, and which mechanism a change needed (`docs/intent.md`, "How change happens").

The question this phase answers: **given verified rules, which mechanism module is needed to reproduce a known
collapse, persistence or regendering, and do the rankings survive random seeds?**

Status: slices 1-3 built in philosophy-engine (2026-11-03/04; ADR 0015 A1-A8). `phil abm run`, `sweep`, `score`, `gate` exist; `material` and `coordination` built, `imagination` a stub; frozen 2026-11-04 (docs/plan.md). Gate run below.

## Gate run 2026-11-04, late (engine 0abf7a4 slice-4 fix pass, `phil abm gate --seeds 100 --workers 4`; serial on macOS since `parallel.py` does not fork under darwin: 1132 s wall clock, 1 worker, 18800 runs; 23 entries: the dataset was loaded before the ectogenesis pair was regenerated)

| letter | status | detail |
| --- | --- | --- |
| (a) footbinding | FAIL | iff pattern holds at NONE of 9 grid points (sanction_weight x payoff of leave_unbound); sanction band NONE; persistence never collapses below a band. No longer BLOCKED: either pledge action is read as a collapse signal through its base (`leave_unbound@family`; `accept_match@suitor` is lawful and reported only); step-0 share guard did not fire (`initial_practice: bind` is set). The A2 per-agent pledge state and the pledge-cost decision remain the named causes; not pursued (layer 2 frozen, docs/plan.md) |
| (b) committed minority | FAIL | max adjacent jump 0.1845 at [0.3, 0.35] under both coordination configurations (plan criterion > 0.5, unchanged). Information only: midpoint 0.325 is outside the ASSUMED Centola band 21-31%; the max-share threshold rule carries an implicit 0.5 (review finding 7), so "no constant sets the location" is not claimed |
| (c) kibbutz | PASS | all three configurations; sanction band [0.25..4.0] excludes the forbidden assignment at every payoff, adopted at weight 0 where it out-pays; no-implicit pair adopted everywhere it out-pays |
| (d) seed stability | PASS | Spearman 0.963 / 0.958 / 0.957 over 23 institutions; caveat as before (necessary, not sufficient) |

Overall FAIL (exit 1). Not tuned. This is the layer-2 record at the freeze: the frequency layer reproduces the kibbutz result and is seed-stable, and does not reproduce Mackie's collapse or Centola's step as encoded.

## Gate run 2026-11-04, evening (engine 8e246b7 slice 4 + performance, `phil abm gate --seeds 100 --workers 4`, six configurations, 23 entries, 289 s)

| letter | status | detail |
| --- | --- | --- |
| (a) footbinding | BLOCKED | the entry now has two pledge actions (family and suitor, encoding review finding 2) and the gate's collapse-action reading is ambiguous; before that edit it ran and FAILED at every grid point (docs/reviews/2026-11-04-abm-slice4-review.md: persistence arm vacuous without `initial_practice: bind`; shared `pledged` lifts the sanction for all) |
| (b) committed minority | FAIL | max adjacent jump 0.19 against the plan's 0.5; the rise is a sigmoid under the max-share threshold rule (review finding 7: the implicit 0.5 in `max` sets the location) |
| (c) kibbutz | PASS | as in the earlier run, all three configurations |
| (d) seed stability | PASS | Spearman 0.948 / 0.960 / 0.960 over 23 institutions |

Overall FAIL. Not tuned; the fix list is in docs/plan.md.

## Gate run 2026-11-04 (engine 59ee9f7, `phil abm gate --seeds 100`, material only)

| letter | status | detail |
| --- | --- | --- |
| (a) footbinding | BLOCKED | no footbinding institution in the dataset; coordination module is a stub |
| (b) committed minority | BLOCKED | no naming-convention institution; coordination stub; `committed_minority` not a parameter |
| (c) kibbutz | PASS | two-axis sweep (sanction_weight {0, 0.25, 0.5, 1, 2, 4} × payoff of `assign(committee,male_member)` {1, 1.5, 2, 3}, 50 seeds per point, read off the committee's late-window adoption share). kibbutz-childrens-house: the forbidden assignment is excluded at every sanction_weight ≥ 0.25 for every payoff (100% of seeds) and adopted at sanction_weight 0 wherever it out-pays (100%). no-implicit pair: adopted at every sanction_weight wherever it out-pays (100%). Preregistered from the choice rule before the run; matched exactly. |
| (d) seed stability | PASS | Spearman 0.966 over 20 institutions, halves 50/50, 0 errors; necessary not sufficient (freedom components are static per role on this dataset) |

Overall: BLOCKED (exit 2) until (a) and (b) can run. What (c) demonstrates: the sanctioned norm R2 governs whether the committee assigns a man (graduated escalation evicts the forbidden assignment within a few steps at any positive weight on the grid, even when it pays 3×; with R2 removed it is adopted at every weight). The collapse region is only sanction_weight 0 on this grid, so the demonstration is that sanctions bite, not where the threshold lies. The earlier property-trace reading (property true at t=0, pair broken at step 1 by a bootstrap draw) was the layer-1 verdict replayed and is now an information line only (docs/reviews/2026-11-04-abm-slice3-review.md). Reviews: docs/reviews/2026-11-04-abm-state-obligations-review.md, 2026-11-04-abm-slice3-review.md; both fix passes landed (engine 313b508, 59ee9f7).

Resolved open questions: payoffs live in an optional `payoffs` block on the dataset entry, keys may name an action, an action instance (`assign(committee,male_member)`, A1 extension, accepted 2026-11-04) or an income fluent; pledges are a `_pledge` naming convention (A3).

## Handoff decisions

- **Same JSON, same enabledness.** The ABM reads `schemas_rules.InstitutionJSON` unchanged. An action is available
  at step t iff the ADR 0013 `enabled` reading says so; the ABM imports `rules_reference`'s reading and never
  reimplements rule semantics.
- **Frequency, not entailment.** Outputs are rates over seeds ("collapsed by step 40 in 94/100 seeds"): statements
  about encodings plus a policy, not about real populations (ADR 0011).
- **Mechanisms are switches.** `material`, `coordination`, `imagination` are on/off; a run reports which subset was
  necessary (outcome fails with the switch off).
- **Modular additive scoring.** Freedom and flourishing reported separately and summed; disagreement is an output
  row, never resolved.
- **Expectations before runs**, written in the dataset, as in Phase 0.

## Design

**Framework: Python Mesa 3.x.** Same language as `philengine/`, so `enabled` is imported, not ported; `batch_run`
sweeps parameters over seeds into DataFrames; `model.rng` threads one seed through every agent; `AgentSet.shuffle_do`
is the random activation threshold models assume. Agents.jl is faster per step but would split the codebase and put
rule semantics behind an FFI. A few hundred agents over a few hundred steps runs in seconds.

**Agents.** One class parametrised by `RoleDecl.name`; `agents_per_role` (default 20) replaces layer 1's
one-agent-per-role domain. State: the institution's fluents for its tuple plus `trust` [0,1], `threshold` [0,1]
(drawn once per seed), `surplus` ≥ 0. Agents sit on a Watts–Strogatz graph (k=6, p=0.1); neighbours are the
reference group for every mechanism.

**Step.** An agent (a) lists enabled actions, (b) drops those a module forbids, (c) chooses: with probability
`copy_rate` it imitates the neighbour whose last action earned most (Axelrod-style success imitation); otherwise it
takes the action whose neighbour adoption share exceeds its `threshold` (Granovetter 1978), else keeps its practice.
`must` rules are followed unless expected gain from breach exceeds the `or_else` cost weighted by the agent's belief
that sanction will land.

**Trust.** Per-dyad `trust` rises by δ when a neighbour kept an obligation bearing on this agent and falls by βδ
(β>1) on betrayal, per the solidarity-modeling design: calibrated asymmetric trust, Ostrom-style light monitoring
(each agent observes a random sample of neighbours per step) and graduated sanctions (`or_else` cost escalates on
repeat breach, fires only if a monitor saw it). Trust feeds the assurance test below (Skyrms 2004: cooperation is
risk-dominated without assurance).

**Modules.**
- `material`: `surplus` accrues from income fluents and decays by a floor cost. Below `floor` the choice set
  collapses to current practice; scarcity narrows choice, a material floor widens it.
- `coordination`: actions tagged `coordinated` pay off only when neighbour share ≥ `threshold` (assurance game).
  A `pledge` action counts as adoption for neighbours' thresholds without changing practice; practice flips when
  pledged share crosses the threshold (Mackie 1996). A `committed_minority` fraction holds an action regardless of
  payoff (Centola et al. 2018).
- `imagination`: an agent can only choose actions it has a `script` for; seeing a neighbour act adds the script with
  probability `exposure_rate`. Off, every agent has every script.

Eight configurations; `necessary_modules` lists the minimal subsets under which the expected outcome occurs in
≥ 80% of seeds.

**Scoring (veil of ignorance).** After stabilisation, drop a fresh agent into a random role and position and replay
`L` steps. Freedom: share of steps where an unsanctioned exit action was enabled (exit), a rule-change action was
enabled (voice), some rule's condition named the agent's interest (recognition). Flourishing: mean realised payoff
(pleasure), share of steps chosen by own threshold rather than imitation (meaning), neighbours with trust > 0.5
toward it (being-known). Report both vectors, sums, and `disagreement` where freedom and flourishing rank a pair
oppositely.

**Reproducibility.** `phil abm run --inst ID --seeds 100 --modules m,c,i`, `phil abm sweep` (8 switch sets × seeds),
`phil abm gate`, mirroring `phil rules`. `AbmReport` JSON per run: seed, modules, parameters, per-step adoption
shares, final fluent rates, score vectors, `necessary_modules`. Seed 0 default; every draw from `model.rng`.

## Pass tests (`phil abm gate`)

(a) **Footbinding collapse** (Mackie 1996): a `footbinding` institution collapses within 60 steps in ≥ 80% of seeds
    iff `coordination` is on and pledge actions exist; with either absent it persists.
(b) **Committed minority without hand-tuning**: sweep `committed_minority` 0.05–0.50 on a naming-convention
    institution; pass iff adoption jumps > 0.5 between adjacent sweep points and no constant in the code sets the
    location. Centola's band (about a quarter) is recorded in the dataset, not asserted by the model.
(c) **Kibbutz regendering**: on `kibbutz-childrens-house` with the implicit assignment rule, `care_assigned_by_sex`
    rate rises toward 1; with it removed it stays flat under every module configuration.
(d) **Seed stability**: Spearman rank of institutions by summed score ≥ 0.9 between disjoint halves of ≥ 100
    seeds, for every switch set.

## Note 2026-11-04: frozen record may not reproduce on the coverture chain

ADR 0013 amendment 3 (liberty flag, engine 9cf3672) changes `Reference.power`, which `abm/model.py` uses to gate an agent's available actions. `contract` is now a lawful candidate for unmarried wife agents in coverture-household and the six mwpa-* entries; it has no effects and zero payoff but changes the random-lawful-candidate draw, so the gate record above (engine 0abf7a4) is not guaranteed to reproduce on those seven entries. Not rerun. See plans/priority-slice1-results.md "Revision 3 run".

## Non-goals

- No LLM agents in Phase 1; rule-based policies until (d) passes.
- No simulated real populations or named groups (ADR 0011); roles are institutional sorts, not demographics.
- No forward claim about any real institution before layer 3 and passing backtests (ADR 0004).
- No fitting of trust, thresholds or payoffs to data; parameters are swept, not calibrated.

## Open questions

- Does `enabled` need per-agent typing beyond `arg_roles` when several agents share a role?
- Do (a)–(c) depend on the small-world graph? Rerun on lattice and random graphs.
- Where do payoffs live? Proposal: a `payoffs` block on the dataset entry, not on `InstitutionJSON`.
- Pledge actions: dataset convention or a first-class `ActionDecl` flag?

## Sources cited (not verified as opened)

Status corrected 2026-11-04 (consistency council). This section previously read "Sources opened". The dataset entries
(`footbinding`, `footbinding-no-pledge`, `naming-convention` in data/institutions/institutions.json) record that the
Mackie 1996 and Centola 2018 articles were never opened by the encoder (search-index snippets only; every host refused
or was outside the allowed network) and mark their figures UNVERIFIED. This plan has no record of which of the works
below were actually read, so treat all as cited, not verified; the entries are the source of truth.

Granovetter, "Threshold Models of Collective Behavior", AJS 1978. Centola, Becker, Brackbill, Baronchelli,
"Experimental evidence for tipping points in social convention", Science 360(6393):1116–1119, 2018. Mackie, "Ending
Footbinding and Infibulation: A Convention Account", ASR 61(6):999–1017, 1996. Skyrms, The Stag Hunt and the
Evolution of Social Structure, CUP 2004 (via the Economics & Philosophy review). Axelrod, The Evolution of
Cooperation, 1984 (imitation policy; not reopened). Mesa documentation, "Overview" (readthedocs, stable). Ostrom,
Governing the Commons, 1990 (monitoring, graduated sanctions; via project glossary).
