# 0016. Failure modes on three axes

Status: accepted 2026-11-03.

## Context
docs/theory.md lists four failure modes every proposed change is checked against: dark twin, displacement, backlash, rebundling. All four answer one question — *who absorbs the cost when a bundle is unbundled* (capital, someone weaker, the threatened equilibrium, the people themselves). Three things show the list is incomplete:

1. theory.md:155 calls cosmetic reform "a distinct failure mode" and the engine tests for it, yet it is not in the list.
2. The MWPA backtest (plans/backtest-mwpa.md) had to file `creditor_shield` — husbands moving assets to wives to dodge creditors — under dark twin. Nobody rebundled a freed strand into a product; a third party used the new rule for a purpose it was not written for. The taxonomy forced a misfile. The same run notes that its "displacement" case (`double_burden`) "is a burden that stays, not one that moves" — a second misfit.
3. Nothing in the list names the commonest way liberation rules fail: they pass and nobody uses them. The MWPA ordering test is exactly that question (did married-women LFP move after the acts?), and the theory has no word for it.

Rule exploit and bad incentives are failures *of the rule itself*; dead letters and erosion are failures *over time*. Both are different axes from *who pays*.

## Decision
Failure modes are organised on three axes. Each mode carries the lowest layer that can detect it, which says which modes a given run can and cannot rank.

| Axis | Mode | What it is | Model case | Lowest layer |
| --- | --- | --- | --- | --- |
| Who pays | Dark twin | Capital rebundles the freed strand into a product | Gig economy and jobs | 3 |
| Who pays | Displacement | The burden moves to someone with less power | Global care chain | 3 |
| Who pays | Backlash | The change threatens an equilibrium enough to provoke active reaction | Reaction to suffrage | 2 |
| Who pays | Rebundling | People retreat to another stronghold; remaining bonds become more load-bearing | Family after welfare retrenchment | 3 |
| Rule | Capture | A party the change was not for gains the new power or shelter | MWPA `creditor_shield` | 1 (an unintended property becomes reachable for a role) |
| Rule | Perverse incentive | The payoffs the rule creates reward behaviour that undermines the property it was meant to secure | Cage-free pledges and compliance theatre; equal reward regardless of effort | 2 (adoption under the material module diverges from the rule's intent) |
| Rule | Cosmetic | Renaming or a revocable exit; nothing structural changes | Owner → guardian | 1 (already tested) |
| Time | Dead letter | The rule passes; adoption never crosses threshold | MWPA if LFP did not move | 2 |
| Time | Erosion | Practice drifts back while the rule stays on the books | Courts construing the acts narrowly (MWPA `narrowed` branch) | 2 |
| Time | Enforcement decay | `or_else` exists but stops firing; a sanctioned norm becomes unsanctioned | Kibbutz R2 | 2 (needs the breach model, ADR 0015 A4) |
| Time | Lock-in | The change succeeds and then cannot be revised | Ostrom's self-revising-rules principle is the guard | 3 |

Two candidate axes are deliberately not modes:
- **What the model cannot see** (Scott's illegibility: the rule conditions on a fact the state cannot observe; encoding misread: a constitutive strand encoded as tying). These are caveats on every result, not events a run can fire. They go in docs/interpreting-results.md as standing caveats; encoding misread is what the council's encoding-faithfulness axis exists to catch.
- **Subject side** (adaptive preference: the freed person does not want the freedom). This is dead letter with the imagination module as the cause. The mode is dead letter; the mechanism tag says why.

## Relabels logged as drift
These change the failure-mode label of preregistered cases after the data was seen. They do not change any verdict, and the original labels stay in the backtest plan with a note.
- MWPA `creditor_shield`: DT → Capture.
- MWPA `narrowed` branch (`backlash` property): BL → Erosion. Backlash is active reaction; a court narrowing a statute while it stands is drift.
- MWPA `double_burden`: DI stays, with the plan's own note that it is a burden that stays, not one that moves; a cleaner home is Perverse incentive (the earnings rule rewards work without lifting R3's obligation). Left as DI pending the author's call.

## Alternatives rejected
- Keep four modes and record the objection. Rejected: the misfiles are in the data already, and layer 2 is being built to detect exactly the time-axis modes.
- Five axes (add epistemic and subject). Rejected: eleven modes is already a preregistration burden; caveats and causes are not modes.

## Consequences
- theory.md (canonical Claude doc) gets the table; the four-mode paragraph becomes the "who pays" axis.
- claims.md gains a row: the four-mode list was incomplete; found by the first backtest (weakening of the original framing).
- docs/interpreting-results.md §4 and the gate letters get a pass for references to "the four failure modes"; theory.md Roadmap row 5 ("the four failure modes across orders") likewise.
- plans/backtest-mwpa.md: relabels above logged; the Section 4 failure-mode test is restated in the new labels (pass if Capture is top-ranked for 1839-50 and Erosion for 1860-80).
- Dataset `_gen_institutions.py` property comments carry the new labels; no rule or verdict changes.
- Layer 2 reports tag each fired mode; the ABM gate gains nothing new now, but dead letter and erosion become reportable once breach lands.
