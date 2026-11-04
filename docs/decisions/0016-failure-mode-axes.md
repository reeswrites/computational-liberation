# 0016. Failure modes on three axes

Status: accepted 2026-11-03; amended 2026-11-04 (council pass, below).

## Context
docs/theory.md lists four failure modes every proposed change is checked against: dark twin, displacement, backlash, rebundling. All four answer one question — *who absorbs the cost when a bundle is unbundled* (capital, someone weaker, the threatened equilibrium, the people themselves). Three things show the list is incomplete:

1. theory.md, section "Non-human liberation" ("What the non-human cases add to the theory", point 4) calls cosmetic reform "a distinct failure mode" and the engine tests for it, yet it is not in the list.
2. The MWPA backtest (plans/backtest-mwpa.md) had to file `creditor_shield` — husbands moving assets to wives to dodge creditors — under dark twin. Nobody rebundled a freed strand into a product; a third party used the new rule for a purpose it was not written for. The taxonomy forced a misfile. The same run notes that its "displacement" case (`double_burden`) "is a burden that stays, not one that moves" — a second misfit.
3. Nothing in the list names a common way liberation rules fail: they pass and nobody uses them. The MWPA ordering test is exactly that question (did married-women LFP move after the acts?), and the theory has no word for it.

Rule exploit and bad incentives are failures *of the rule itself*; dead letters and erosion are failures *over time*. Both are different axes from *who pays*.

## Decision
Failure modes are organised on three axes. Each mode carries the lowest layer that can detect it, which says which modes a given run can and cannot rank.

| Axis | Mode | What it is | Model case | Lowest layer |
| --- | --- | --- | --- | --- |
| Who pays | Dark twin | Capital rebundles the freed strand into a product | Gig economy and jobs | 3 |
| Who pays | Displacement | The burden moves to someone with less power | Global care chain | 3 |
| Who pays | Backlash | The change threatens an equilibrium enough to provoke active reaction | Reaction to suffrage; MWPA `narrowed` branch (a court power that reinstates R1) | 3 (1 when encoded as a branch, as in MWPA `narrowed`; layer 2 agents adopt actions and never add rules) |
| Who pays | Rebundling | People retreat to another stronghold; remaining bonds become more load-bearing | Family after welfare retrenchment | 3 |
| Rule | Capture | A party the change was not for gains the new power or shelter | MWPA `creditor_shield` | 1 (an unintended property becomes reachable for a role) |
| Rule | Perverse incentive | The payoffs the rule creates reward behaviour that undermines the property it was meant to secure | Cage-free pledges and compliance theatre; equal reward regardless of effort | 2 (adoption under the material module diverges from the rule's intent) |
| Rule | Cosmetic | Renaming or a revocable exit; nothing structural changes | Owner → guardian | 1 (already tested) |
| Time | Dead letter | The rule passes; adoption never crosses threshold | MWPA if LFP did not move | 2 (sweep criterion: adoption of the freed action below C_SHARE_LOW in ≥ 80% of seeds across the whole swept range of payoffs and sanction weights; numbers ASSUMED, mirroring `phil abm gate` (c)) |
| Time | Erosion | Practice drifts back while the rule stays on the books | No MWPA case: when a narrowing is encoded as a court power it is Backlash at layer 1; Erosion is practice drift | 2 (sweep criterion: adoption first crosses C_SHARE_HIGH then falls below C_SHARE_LOW within the run in ≥ 80% of seeds; numbers ASSUMED, mirroring `phil abm gate` (c)) |
| Time | Enforcement decay | `or_else` exists but stops firing; a sanctioned norm becomes unsanctioned | Kibbutz R2 | 3 (needs a mechanism by which `or_else` stops firing; none exists, ADR 0015 A4 makes sanction weight a swept constant; lowest layer 3 until it does) |
| Time | Lock-in | The change succeeds and then cannot be revised | Ostrom's self-revising-rules principle is the guard | 3 |

Two candidate axes are deliberately not modes:
- **What the model cannot see** (Scott's illegibility: the rule conditions on a fact the state cannot observe; encoding misread: a constitutive strand encoded as tying). These are caveats on every result, not events a run can fire. They go in docs/interpreting-results.md as standing caveats; encoding misread is what the council's encoding-faithfulness axis exists to catch.
- **Subject side** (adaptive preference: the freed person does not want the freedom). This is dead letter with the imagination module as the cause. The mode is dead letter; the mechanism tag says why.

## Relabels logged as drift
These change the failure-mode label of preregistered cases after the data was seen. They do not change any verdict, and the original labels stay in the backtest plan with a note.
- MWPA `creditor_shield`: DT → Capture.
- ~~MWPA `narrowed` branch (`backlash` property): BL → Erosion. Backlash is active reaction; a court narrowing a statute while it stands is drift.~~ Reverted 2026-11-04 (council pass, finding 1): the branch adds rules (R17, R18), which is Backlash; `narrowed` is BL again. Drift on drift, logged in the amendment below and in plans/backtest-mwpa.md.
- MWPA `double_burden`: DI stays, with the plan's own note that it is a burden that stays, not one that moves; ~~a cleaner home is Perverse incentive (the earnings rule rewards work without lifting R3's obligation)~~. Left as DI pending the author's call. Amended 2026-11-04 (council pass, finding 4): relabelled "partial reform (no mode)"; the Perverse-incentive suggestion is dropped (nothing rewards undermining the property; R3 is simply untouched). DI is kept in the gloss as history.

## Alternatives rejected
- Keep four modes and record the objection. Rejected: the misfiles are in the data already, and layer 2 is being built to detect exactly the time-axis modes.
- Five axes (add epistemic and subject). Rejected: eleven modes is already a preregistration burden; caveats and causes are not modes.

## Consequences
- theory.md (canonical Claude doc) gets the table; the four-mode paragraph becomes the "who pays" axis.
- claims.md gains a row: the four-mode list was incomplete; found by the first backtest (weakening of the original framing).
- docs/interpreting-results.md §4 and the gate letters get a pass for references to "the four failure modes"; theory.md Roadmap row 5 ("the four failure modes across orders") likewise.
- plans/backtest-mwpa.md: relabels above logged; the Section 4 failure-mode test is restated in the new labels (pass if Capture is top-ranked for 1839-50 and Erosion for 1860-80; restated again in the 2026-11-04 amendment: Backlash, exhaustive).
- Dataset `_gen_institutions.py` property comments carry the new labels; no rule or verdict changes.
- Layer 2 reports tag each fired mode; the ABM gate gains nothing new now, but dead letter and erosion become reportable once breach lands.

## Amendment 2026-11-04 (council pass)

Applied after the author accepted the council's primary recommendation on each finding of docs/reviews/2026-11-04-adr0016-council.md. The table above is edited in place (lowest-layer column and the Backlash / Erosion model-case cells); the drift list keeps its original lines struck through, not deleted.

1. **`narrowed` is Backlash again (finding 1).** The MWPA `narrowed` branch adds rules (R17 court may construe_narrowly, R18 R1 reinstated), which is the glossary's backlash and this ADR's own "active reaction"; the 2026-11-03 relabel BL → Erosion is reverted. The Erosion row keeps lowest layer 2 and gains the note: when a narrowing is encoded as a court power it is Backlash at layer 1; Erosion is practice drift. This is drift on drift and is logged here, in the drift list above, in plans/backtest-mwpa.md and in the `backlash` property gloss (`data/institutions/_gen_properties.py`). No rule, property or verdict changes.
2. **The MWPA Section 4 failure-mode test is exhaustive again (finding 2).** Pass iff Capture ranks first for 1839-50 and Backlash for 1860-80; fail if any other mode ranks first in either window. The layer-1 outcome (inconclusive: verdicts, not a ranking) is unchanged.
3. **"For whom" (finding 3).** In Capture's definition, "a party the change was not for" means a party other than the preregistered liberated role. Each preregistered failure-mode case names that role; for every MWPA case it is the wife, so a husband sheltering assets from creditors is Capture relative to the liberation reading even where the 1839-50 statutes were written as debtor relief.
4. **Orthogonality criterion (finding 4).** Rule-axis modes are reachable from the rule set as written (no new actor, no new rule). Who-pays modes need a new actor or institution. Time-axis modes need dynamics. Cosmetic is Rule (an iso property of the delta). Under this criterion `double_burden` fits neither Displacement nor Perverse incentive (nothing rewards undermining the property; R3 is simply untouched): it is relabelled "partial reform (no mode)", DI kept in the gloss as history, and the Perverse-incentive suggestion is struck from the drift list.
5. **One sweep-level detection criterion per layer-2 mode (finding 5).** Written into the table's lowest-layer column:
   - Backlash: lowest layer 3 (layer 2 agents adopt actions and never add rules); 1 when encoded as a branch, as in MWPA `narrowed`.
   - Enforcement decay: needs a mechanism by which `or_else` stops firing; none exists (A4 makes sanction weight a swept constant); lowest layer 3 until it does.
   - Dead letter: adoption of the freed action below C_SHARE_LOW in ≥ 80% of seeds across the whole swept range of payoffs and sanction weights.
   - Erosion: adoption first crosses C_SHARE_HIGH then falls below C_SHARE_LOW within the run in ≥ 80% of seeds.
   The 80% and the share thresholds are ASSUMED and mirror `phil abm gate` (c)'s (C_SHARE_LOW 0.20, C_SHARE_HIGH 0.80, ASSUMED there too).
6. **Wording (findings 7, 8, 9).** "The commonest way" → "a common way" (unsourced). The Context now cites theory.md by section, not line. And: **this taxonomy is provisional until a second backtest fires a non-MWPA mode.**
7. **Consistency (council items 7, 9).** The glossary's four who-pays entries carry the axis tag like the seven new ones, and its dark-twin and backlash wording follows this ADR's.
