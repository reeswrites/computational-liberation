# 0015. Layer 2 ABM design choices

## Context
The layer-2 agent-based model (plans/layer2-abm.md) puts N agents per role on a social graph and asks which mechanism module (material, coordination, imagination) reproduces known collapse, persistence or regendering. The memo in docs/decisions-pending.md posed seven open design questions (A1–A7). The author accepted every recommendation on 2026-11-03. Gate tests: footbinding collapses, a committed minority tips a naming convention without a hand-tuned constant, the kibbutz children's house regenders, rankings are stable across seeds.

## Decision
**A1. Payoffs.** An optional `payoffs` block on the dataset entry (absent means every action pays 1.0), with the gate sweeping payoff ranges. Reason: leaves the rules schema and layer 1 verdicts untouched, and "swept, not calibrated" matches the plan. Forecloses: payoffs derived from the rules, which is the layer-3 goal; payoffs stay hand inputs until then.

**A2. Per-agent vs per-role state.** Deferred until the MWPA layer-2 run. Shared role-level state is used for the three gate institutions (footbinding, naming, kibbutz), none of which needs a within-role split. Reason: the MWPA run needs within-role heterogeneity (propertied vs unpropertied wives), and choosing between per-agent state and an outside-the-rules attribute is better made against that case. Forecloses nothing yet.

**A3. Pledges.** A naming convention (actions ending `_pledge`) now, documented as a stand-in, with a pledge as a derived public fluent as the target. Reason: ships gate test (b) fastest with no schema change. Forecloses a schema flag on `ActionDecl`.

**A4. Breach.** Breach of a `must` is a choice weighed against the sanction (`or_else`), with the sanction weight a swept parameter. Reason: without it trust and sanction dynamics are dead code and the footbinding and kibbutz tests cannot run on the described mechanism. Forecloses always-obey; the norm/law refinement waits for a tag across the dataset.

**A5. Trust.** Trust rises when a neighbour keeps an obligation bearing on me, derived from `arg_roles`. Reason: this is the plan's reading and uses an existing field. Forecloses own-obligation trust; moot until A4 lands.

**A6. Unmentioned actions.** Strict enabledness stays (an action needs a `may` or `must` rule), plus breach from A4. Encodings that really leave something open gain explicit `may` rules; the kibbutz encoding gets a review pass (needs a `may neglect`) before gate (c). Reason: one enabledness source for layers 1 and 2. Forecloses default-available actions.

**A7. Parameters.** DEFAULT_PARAMS are hand-set and unsourced; every reported result is a rate over a sweep, never a single point. Reason: plan line 92 and gate (b). Forecloses single-point reporting.

## Alternatives rejected
Per option, in the memo: derived or separate-file payoffs (A1), per-agent state now (A2), schema flag for pledges (A3), always-obey and norm-only breach (A4), own-obligation or blended trust (A5), default-available actions (A6).

## Consequences
Layer 2 results inherit hand-set payoffs and parameters, so a sceptic can say numbers set the result; sweeps are the defence. Encodings get richer (explicit `may` rules). A2 stays open and blocks the MWPA layer-2 run until decided; a follow-up ADR records it.

## Status
accepted (2026-11-03)
