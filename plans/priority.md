# layers 4 and 5: priority and sequencing by rule ablation

Replaces the one-line "First priority computation" step in docs/plan.md (thin path, step 4).

Status: draft, agreed with the author 2026-11-04. Nothing built. Slice 1 waits on the author's preregistered ranking table (slice 1, below). Layer 2 (ABM) is frozen after the 2026-11-04 gate record in plans/layer2-abm.md.

## Why

The thesis (docs/theory.md, "Core thesis") is that oppression is a bundle of strands, some tying, some rival, some superadditive, and that liberation is choosing which strands to cut and in what order. The six-test scoring would need ABM output the project has just failed to validate (gate FAIL, layer2-abm.md). The intent file says disagreement is reported, never resolved, and the ADR 0004 rule stands: no forward claim before backtests. So the revised vision is narrower and checkable now: given honestly encoded institutions, the tool says which rule carries an outcome, which strands are tying, which cuts must happen together to avoid rebundling, and where two encoders disagree. It becomes a planner only after backtests. Everything below runs at layer 1.

## Design

**Ablation.** For an entry `E` (`InstitutionJSON`) and rule `r`, `E \ r` is `E` with `r` removed from `rules`. For each property `p` the entry already checks, run the same check kind as `E`'s `expected_properties` names (`check_for_expected`) through `rules_checks.run_all(E \ r, properties, k, which=...)` with the same `k`, `init`, `compliance`, `step_mode`. The result is a `PropertyResult.verdict` from the engine's real vocabulary: `reachable`, `open` (dataset spelling `unreachable_open`), `holds_to_k`, `violated`, `persists`, `fails`, plus `inconsistent` and `error`. A **flip** is a change of verdict between `E` and `E \ r` among `{reachable, open, holds_to_k, violated, persists, fails}`. `error` and z3-unknown results are never counted; they are listed. `inconsistent` after deletion is reported as its own row ("no compliant trace"), not as a flip. `open` means "not found within k", not "safe", so readings carry the bound k.

**Load.** Two counts, never summed (docs/intent.md: disagreement reported, not resolved).
- `load_freedom(r)` = number of freedom properties that flip. Freedom family: exit (`subject_cannot_exit`, `subject_cannot_exit_persists`, `dependent_cannot_exit`), standing (`no_standing`, `no_standing_persists`, `cannot_contract`), non-domination (`care_and_sanction_same_role`, `financial_dependence`), voice, recognition. The class is a new field `kind: freedom | goods | failure_mode` on `Property`, set by hand and decided by the author (see Decisions).
- `load_goods(r)` = number of goods properties that flip. Goods are products of superadditive strands (being known, co-parenting intact), written as `persists`-style properties. Each carries a mandatory `contested` field (ADR 0012) and counts only once a second encoder has written it independently.

**Readings (labels, not scores).**
| load_freedom | load_goods | Reading | Move |
| --- | --- | --- | --- |
| high | zero | tying strand | cut |
| any | high | constitutive strand | redesign, do not cut |
| high | high | hard case | hand to the disagreement locator |

Each rule's hand-set `strand` tag is compared with its reading; mismatches are reported (feeds the strand-tag redesign in docs/plan.md).

**Transfer graph.** For rules `r1 != r2`, `load(r2 | E \ r1)` minus `load(r2 | E)`; a positive difference is a directed edge `r1 -> r2` with weight equal to the rise, kept separately for freedom and goods. **Rebundling** (ADR 0016, who-pays axis, the one mode with no property; claim T11) is any edge whose target reads as a tying strand. "Remaining bonds become more load-bearing" is that edge. As a property `rebundling(E, r1)`: some tying `r2` has `load_freedom` up after deleting `r1`.

**Cut sets and sequencing.** Let `L(S)` be the vector of `load_freedom` over remaining rules after deleting set `S`. A cut sequence `S1, S2, ...` is **whack-a-mole** if some intermediate state has a rule `r` with `load(r)` above its starting load. A cut set `C` is **simultaneous-safe** if deleting all of `C` in one step reaches the same end state, with no intermediate load rise. A **minimal must-go-together set** is a cut set that is simultaneous-safe while no proper subset is (found by search over subsets, smallest first). **Sequencing** orders the sets so that `max_r load(r)` stays flat. Floor-first (claim T1) becomes a testable prediction: floor strands have the highest out-transfer.

**Disagreement locator.** Given two encodings `E_a`, `E_b` of one institution (or two strand taggings of one rule set) whose verdict on property `p` differs, diff them at the rule/tag level and report the smallest set of rule or tag differences whose transplant from `E_b` to `E_a` flips the verdict (ablation again, over differences instead of rules). This is claim L19 made a tool: the engine says which single rule carries the outcome given the encoding, and now which difference between encodings carries the disagreement.

**The six tests demoted to interpretation labels** on ablation output, not scored: leverage/bottleneck = load; power shift = deletion removes a derived `can_sanction` or power fluent (ADR 0013); margins first = deletion raises freedoms for the role with the fewest; surplus = deletion enables more actions afterward; durability = deletion creates a role whose exit now depends on the new rule.

## Slices

Each slice: a pass test, a preregistration committed before the run, and a council seat (ADR 0014). Engine files are in philosophy-engine.

1. **Ablation and `load_freedom` over the 25 entries** (the 23 institutions plus the ectogenesis pair). Files: new `philengine/rules_ablate.py`, `cli_rules.py` (`phil rules ablate`), `schemas_rules.py` (`Property.kind`), reuse `rules_checks.run_all` and `rules_cache.RuleCache`. Preregistration: before the run the author fills a ranking table, one row per entry (placeholder rows: `entry | predicted top rule | predicted load_freedom | predicted tying rules | confidence`), committed; the run may not read it. Pass: ranking table produced for all 25 with zero silent errors; Spearman between preregistered and computed rank per entry reported (no threshold asserted, per layer2's ASSUMED-numbers rule). Council: soundness.
2. **Goods properties, `contested`, second encoder.** Files: `data/institutions/properties.json` and `_gen_properties.py`, `schemas_rules.py` (`contested` required on `kind: goods`), `rules_ablate.py` (`load_goods`). Preregistration: the goods-property list and expected readings per strand type before any run. Pass: at least 3 goods properties each written by a second encoder who has not seen the first; disagreements recorded, not merged; the table of readings above computed for the care and control cluster. First job for ADR 0012. Council: faithfulness.
3. **Transfer graph and `rebundling` property.** Files: `rules_ablate.py` (`transfer_graph`), `properties.json`, `rules_gate.py` if a gate criterion is added. Pass: graph on the kibbutz and MWPA entries matches preregistered edges; `rebundling` property written and checked; T11 moves from three of four who-pays modes to four. Council: scope.
4. **Cut sets and sequencing.** Files: new `rules_cuts.py`, `cli_rules.py` (`phil rules sequence`). Pass: finds minimal must-go-together sets on the ectogenesis pair and MWPA, whack-a-mole detected on a hand-built toy where the answer is known, and the T1 out-transfer prediction reported either way. Council: soundness (brute-force check on tiny entries).
5. **Disagreement locator CLI.** Files: new `rules_diff.py`, `cli_rules.py` (`phil rules disagree A B`). Pass: on two encodings that differ by a known rule it names that rule; on the care and control cluster under two strand taggings it names the tag. Council: faithfulness.

**First preregistered ablation target (slice 1): the ectogenesis pair** (plans/ectogenesis.md). Expected: after the technology removes the rival strand (R2/R3), the next-highest `load_freedom` rule in `ectogenesis` is R5, the female care norm (tying). That is Firestone's "technology necessary not sufficient" (claim T3). It is stated here before any run.

## Pass tests (roadmap layers 4 and 5, restated)

- **Layer 4 (priority):** the ablation ranking is deterministic and stable across `k` in a preregistered range and across `step_mode`; it rediscovers known findings (kibbutz R2 carries gate (d); ectogenesis R5 outlives R2/R3); it labels at least one strand mismatch against hand tags, reported not fixed.
- **Layer 5 (sequence):** the cut-set search returns the same must-go-together sets under reordered rule lists; floor-before-standing versus standing-before-floor is evaluated by max-load flatness, and the result is reported even if T1 fails. Backtest agreement waits on layer 3.

## Non-goals

- No ABM work (layer 2 frozen); no `imagination` module.
- No whaling or kerosene backtest. Backtests, when they come, stay in reproductive labor: formula and the pill as rules-trail cases, ectogenesis as the forward case.
- No summed or weighted freedom-plus-goods score; no single ranked "do this first" list.
- No forward claim about a real institution before layer 3 passes (ADR 0004); outputs are statements about encodings (ADR 0011).

## Open questions

- Deleting a rule changes derived power fluents (ADR 0013); report flips and lost power separately.
- Pairwise transfer is O(n^2) engine runs per entry; measure `RuleCache` hit rates in slice 3.
- Can goods ever be encoded without the encoder's own picture of the good? Slice 2 measures it by inter-encoder agreement; it may not close.

## Decisions waiting on the author

Settled 2026-11-04 (late) with the author:

1. **Property kinds** (`kind` field on every property, added in slice 1): `freedom` (counted in load_freedom): dependent_cannot_exit, subject_cannot_exit, subject_cannot_exit_persists, no_standing, no_standing_persists, financial_dependence, financial_dependence_unpropertied, cannot_contract, worker_uninsured, binding_practised, marriage_requires_binding, care_assigned_by_sex, reproduction_controlled_by_owner, offspring_owned. `goods` (counted in load_goods): none yet; slice 2 writes them. `structure` (diagnostic, listed not counted): care_and_sanction_same_role, solo_care_by_non_birthing_parent, leave_reserved_for_non_birthing_parent, new_convention_adopted, birth_labor_rival, care_decoupled_from_birth. `failure_mode` (listed not counted): double_burden, creditor_shield, backlash.
2. **k bound:** ablation runs at k=6 and k=8; any verdict disagreement between them is reported per rule, never averaged.
3. **`may` deletion:** ablation deletes the rule (permission removed, labelled "permission removed" in the output); no prohibit variant in slice 1. Revisit only if a `may` deletion tops a ranking.
4. **Second goods encoder (ADR 0012):** a fresh agent that never saw the first encoding writes its own goods properties; disagreements fill `contested`; every report says "second encoder: agent, not someone living under the institution".
5. **Slice-1 preregistered ranking table:** still open; the author names, before the run, the rule expected to carry the highest load_freedom in coverture-household, kibbutz-childrens-house, footbinding, mwpa-property and ectogenesis. Note found while settling: no freedom property currently reads ectogenesis R5 (care_assigned_by_sex is already `violated` there because R4 permits male care), so the T3 expectation "R5 is next" needs a property R5 actually carries (e.g. a `persists`-shaped care duty on female intended parents) written and preregistered in slice 1, or the expectation reads load 0 by construction.
6. **Ectogenesis drift 1:** fix under a v2 preregistration (start_gestation and implant merged; surrogacy `birth_labor_rival` preregistered holds_to_k), committed before the rerun.
