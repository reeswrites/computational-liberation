# Parked: dynamics layer for "sticks" and endpoint path dependence (2026-11-07)

Status: PARKED. Written so the time question raised by plans/informal-rules.md stays findable and someone can pick it up without re-deriving the discussion. Not started. Goal set by the author 2026-11-07: this layer exists to deliver **endpoint path dependence**, not only "sticks."

## Why it exists

The static layer (plans/informal-rules.md, D3) reports one of absorbed, displaced → to whom, or **no backstop found**. The third verdict refuses to say "sticks," because "sticks" means no norm grows back, and that is a claim about time. The static layer also reports an exposure path for ordered removals but cannot produce a different endpoint from a different order: removing a fixed set of rules yields the same rule set in any order. Both gaps need something that reacts to a step.

## Relation to layer 2 (frozen)

Layer 2 (plans/layer2-abm.md, ADR 0015) is frozen after the 2026-11-04 gate record: (a) footbinding collapse FAIL, (b) committed-minority step FAIL, (c) kibbutz PASS, (d) seed stability PASS. The author's reason for freezing was that it consumed effort replicating Mackie and Centola without advancing the goal. This plan is not an unfreeze. It is a different question with a different gate, and it reuses the engine's `Reference.power` enabledness (ADR 0013) and `or_else` sanction mechanics rather than rebuilding them. If it is ever built, it should be a small module beside `philengine/abm/`, not a rewrite of it. A stub that raises, like the `imagination` module, is acceptable as the named seam in the verdict code and costs nothing.

## Design sketch (from the handoff, adjusted to the repo)

- Agents hold roles (from the entry) and two expectations per informal rule, after Bicchieri 2006: an **empirical** expectation (share of relevant others who comply) and a **normative** expectation (share who think one should). An informal rule is live for an agent while both are above that agent's thresholds; it lapses when either falls.
- Formal sanctions: as now, `or_else`-based, charged by the rule.
- Informal sanctions: an agent action by neighbours whose `sanctioner` is `peers` or `family`, triggered on observed breach. This is the piece the existing ABM lacks (plans/layer2-abm.md:81 mentions Ostrom-style monitoring as plan text only; the code has none).
- Crystallization: an informal rule that has carried a function for k steps gains an `or_else` and a `sanctioner`; this is the reaction that makes endpoints order-dependent. In the static layer this is an optional hand-typed rule marked ASSUMED; here it is the mechanism under test.
- Output per intervention: {sticks, absorbed, displaced → to whom} over time, and the exposure path, with freedom and goods kept separate as in plans/priority.md.

## Gate (write the preregistration before any run; commit it before the first run)

The handoff proposed Loving v. Virginia and Bicchieri's footbinding/FGM cases. Adjusted:

- **Loving v. Virginia (formal-led).** Ruling 1967; Gallup approval of Black–White marriage 4% (1958), 20% (1968), 64% (1997, first majority). The lag is thirty years. The gate is an **ordering** prediction, never a curve fit: with the formal gate removed by `sanctioner: state` and the informal gate held by `family`/`peers`, the model must show the informal gate outlasting the formal change, and must not show it collapsing on removal. Fitting the thirty-year lag with free parameters would be calibration, not evidence (claims L21 is the precedent).
- **Same-sex marriage (norm-led).** Already queued in plans/marriage-bundle.md as the rules-lead-vs-trail backtest. Attitudes moved before the law. The model must show the informal gate lapsing before the formal gate is removed, and the formal removal then absorbed. The pair with Loving tests claims T8 in both directions, which is what intent.md's falsifier ("outcomes move BEFORE the rule change and the rule merely ratifies them") asks for.
- **Footbinding: do not reuse.** It already failed gate (a) in the frozen layer, and Mackie 1996 frames it as a convention, not a Bicchieri norm. Reusing it would re-enter a lost test under a looser fit.
- **Endpoint path dependence.** At least one preregistered pair of removal orders over the composed marriage bundle must yield different endpoint verdicts, and the difference must be traceable to crystallization at a named step. If every order converges, the layer has not delivered its goal and says so.

Pass is all four. Partial passes are recorded, not promoted.

## What it must not do

- No curve fitting to polling series. Polling data sets the ordering and the sign of the lag, nothing finer.
- No hand-tuned payoffs that differ between the Loving and same-sex runs beyond what the encodings carry.
- No claim above layer 3 (theory.md roadmap: no forward claim until the backtest layer passes).

## Preregistered claims (enter in docs/claims.md only when this is scheduled)

- S1. A no-backstop verdict from the static layer becomes "sticks" only when this layer shows no informal rule reaching both expectation thresholds within the run. Until then every such result is reported as "no backstop found."
- S2. Ordered removal over the composed marriage bundle is endpoint-path-dependent under crystallization and endpoint-path-independent without it. This is the claim that justifies the layer; if it fails, the layer is a description of lag, not of sequencing.

## Sources carried from the handoff check (2026-11-06)

Bicchieri 2006 *The Grammar of Society* (definition); Bicchieri 2017 *Norms in the Wild* (FGM, Tostan); Mackie 1996 ASR 61(6) (convention account; original source for footbinding/infibulation); Gallup interracial-marriage series (news.gallup.com/poll/354638 and /poll/28417); Watzlawick, Weakland & Fisch 1974 *Change* (first/second-order, gloss unchecked against text); Jackson 1965 *Arch Gen Psychiatry* 12: 589–594 (family rules); no single source for "identified patient."

## Sequencing

After plans/informal-rules.md lands and its rediscovery case has a verdict. Not before the faithfulness batch. Decision to build at all is the author's, at that point, with the gate above as the price.
