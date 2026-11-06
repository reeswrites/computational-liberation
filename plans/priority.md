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
5. **Slice-1 preregistered ranking table:** filled 2026-11-04 (late), before any ablation run. These are the assistant's guesses, endorsed by the author as the preregistration ("use your guesses"); labelled as such so a hit is not read as the author's intuition confirmed.

| entry | rule expected to carry the highest load_freedom | why |
| --- | --- | --- |
| coverture-household | R6 wife must_not leave | flips subject_cannot_exit and its persists twin; R4 (sue) and R7 (contract) each carry one property |
| kibbutz-childrens-house | R2 committee must_not assign male_member | the one rule gate (d) already showed carries care_assigned_by_sex |
| footbinding | R3 family must_not leave_unbound | carries binding_practised and marriage_requires_binding; R1 (may bind) is a permission, deleting it is labelled not ranked |
| mwpa-property | R11 creditor must_not attach | the creditor shield is what the act changed; R13 (may hold_property) is a permission |
| ectogenesis | R5 intended_parent must provide_care (tying, implicit) | only once `female_parent_care_persists` (plans/ectogenesis.md v2 §5) is in the dataset; without it R5 reads load 0 by construction, and that reading is itself the T3 test |

Ties are expected (several rules carry exactly one property); a tie with the named rule counts as a hit, a different top rule counts as a miss.


### Slice 1 revision 2 (settled 2026-11-05 with the author, preregistered before the rerun)

Decisions from plans/priority-slice1-results.md, all accepted:
- (a) **Property families.** Each property carries a `family` (default: its own id). A flip counts once per family per rule. `dependent_cannot_exit` / `subject_cannot_exit` / `subject_cannot_exit_persists` are one family (`cannot_exit`); `no_standing` / `no_standing_persists` one (`no_standing`); `financial_dependence` / `financial_dependence_unpropertied` one (`financial_dependence`).
- (b) **Ranking on freedom-up only.** `load_freedom_up` ranks; `load_freedom_down` is shown beside it and names the rule a load-bearing protection, never a cut.
- (c) **Prohibit variant.** Every `may` rule is ablated twice: deleted (deregulates when it is the sole regulator; listed, not ranked) and replaced by `must_not` with the same attribute, aim and conditions (a real cut of the permission; ranked, labelled `prohibited`).
- (d) **R5 property.** `care_duty_on_women` (kind freedom, family `care_duty_on_women`, invariant-shaped): whenever a subject is born and has a female parent, some female parent provides care; written so that ectogenesis R5 carries it and R4 does not.
  POST-HOC NOTE (2026-11-05, before the revision-2 run, after the dataset builder's probe): the plain same-step invariant is violated even with R5 in force, because an action `must` fires in the step its condition first holds and its effect lands the next step (ADR 0009 state obligations lower same-step; action obligations do not). The formula was therefore written with a one-step grace. The criterion (R5 > 0, R4's prohibit variant 0) was preregistered; the formula was not, and was chosen after seeing the plain form fail on the ectogenesis data. Recorded as instrument tuning toward the target, disclosed, not hidden (docs/reviews/2026-11-05-ablation-slice1-rev2-review.md finding 7).
- (e) **Revision-2 preregistered tops**, the assistant's guesses endorsed by the author before the rerun; v1 (1/5) stays in the record. A tie with the named rule is a hit; ties are expected now that families collapse the exit twins.

| entry | expected top (load_freedom_up) | why |
| --- | --- | --- |
| coverture-household | R6 wife must_not leave (tie with R4, R7 expected) | one family each: cannot_exit, no_standing, cannot_contract |
| kibbutz-childrens-house | R2 committee must_not assign male_member (tie with R4 expected) | care_assigned_by_sex vs cannot_exit, one family each |
| footbinding | R3 family must_not leave_unbound | binding_practised and marriage_requires_binding are two families; R9 carries cannot_exit once |
| mwpa-property | R7 wife must_not contract | the act's own strand; R6 ties at one family; R11 still expected 0 (its property is failure_mode kind) |
| ectogenesis | R5 intended_parent must provide_care | only via care_duty_on_women; the T3 test is informative only if R5 > 0 and R4's prohibit variant reads 0 |

   Original statement of the decision: the author names, before the run, the rule expected to carry the highest load_freedom in coverture-household, kibbutz-childrens-house, footbinding, mwpa-property and ectogenesis. Note found while settling: no freedom property currently reads ectogenesis R5 (care_assigned_by_sex is already `violated` there because R4 permits male care), so the T3 expectation "R5 is next" needs a property R5 actually carries (e.g. a `persists`-shaped care duty on female intended parents) written and preregistered in slice 1, or the expectation reads load 0 by construction.
6. **Ectogenesis drift 1:** fix under a v2 preregistration (start_gestation and implant merged; surrogacy `birth_labor_rival` preregistered holds_to_k), committed before the rerun.

### Slice 1 revision 3: liberty flag (preregistered 2026-11-05, before any run)

Author decision (2026-11-05): option (c) from plans/priority-slice1-results.md. An action declaration gets `liberty: bool` (default false). For a liberty action, `(enabled a args)` at t is true iff no disability (`must_not`, `or_else` null) on that instance holds at t, whether or not any `may`/`must` names it. Power actions (the default) keep ADR 0013's 2026-11-03 amendment: constant false when nameless. Trace semantics unchanged either way. Encoder marks a liberty only where the institution withholds by prohibition something people do by default; initial set: `contract` in the coverture chain (coverture-household and every mwpa-* entry). Nothing else.

Predictions, written before the engine change or the dataset change:

1. Layer 1: zero verdict changes across all 25 entries against the committed semantics (`phil rules check-all --no-cache` diffed row by row). R7 (`must_not contract`) holds through coverture, mwpa-creditor-exemption, mwpa-property, mwpa-property-narrowed, mwpa-earnings; R15 (`may contract`) grants from mwpa-sole-trader on.
2. Ablation, k=6 and 8: deleting R7 flips `cannot_contract` holds_to_k -> violated (freedom, up) in coverture-household, mwpa-creditor-exemption, mwpa-property, mwpa-property-narrowed, mwpa-earnings. R7 is a `must_not`, so it has no prohibit variant and the deletion is not `deregulated` (the flag is `may`-only).
3. Tops: coverture-household top set becomes {R6, R7} at load_freedom_up 1 (R4 joins only if it already reads 1 in revision 2; not predicted). mwpa-property top set becomes {R6, R7}; the revision-2 miss turns into a hit on the "R7 in top set" criterion. Kibbutz R2, footbinding R3, ectogenesis R5 unchanged. Rediscovery 5/5.
4. Every row on an entry with no liberty action is byte-identical to revision 2 (ablate-25-v4) apart from timing.
5. Monotonicity laws (tests/test_rules_meta.py, `enablement_polarity`): a `must_not` on a liberty action is the only rule that moves it; "removing a may never adds reachability" still holds for liberty actions because a `may` on a liberty is redundant. Prediction: the existing metamorphic tests pass unchanged.

Drift from any of 1-5 is recorded in plans/priority-slice1-results.md, never edited to match.

### Candidate for slice 2: floor route vs title route (noted 2026-11-05)

Author's point: MWPA reached material independence through private title, which is the vehicle on offer, not the goal; the theory's sequence puts a decommodified floor ahead of it. Candidate encoding `coverture-floor`: coverture plus a state obligation on the institution (`must provide_subsistence w when (is_subject w)`), no property grant. Preregister before any run: `financial_dependence` and `financial_dependence_unpropertied` violated with no R13/R14; `double_burden` still reachable (the floor does not touch the care rule); `creditor_shield` open. Then compare cut sets for the same freedom: title route (R1 deleted, R13+R14 added) against floor route (one rule added). The question is which leaves fewer load-bearing strands behind. Not scheduled; author decides at slice 2 go/no-go.

### Slice 1 revision 4: one convention for default capacities (preregistered 2026-11-04 local, before any edit or run)

Author decisions 2026-11-04 (after docs/reviews/2026-11-05-liberty-flag-rev3-review.md): (1) one convention, the flag; (2) the flag is renamed `default_capacity`; (3) only a disability (`must_not`, `or_else` null) removes a default capacity, a sanctioned `must_not` punishes its exercise; (4) the layer-2 gate is rerun on the affected entries once the engine runs in parallel.

Dataset change (generator only):
- Flag `default_capacity: true` on: `leave` in coverture-household, the six mwpa-* entries, police-crisis, cps, crisis-team, the three companion-* entries, public-library, airline-flight (15 entries); `sue` in the coverture chain (7), police-crisis, crisis-team (9 entries; NOT companion-*, where R11 is a personhood statement and the power reading is faithful); `sleep_home` in both kibbutz entries; `refuse_binding` in both footbinding entries; `contract` stays (7).
- Delete the permission rows that only encoded the capacity: the implicit `may leave when true` (coverture chain R8 x7, police R9, cps R9, companion R12 x3, airline R5), the implicit `may sleep_home when true` (kibbutz R7 x2), the implicit `may refuse_binding when true` (footbinding R8 x2), and the coverture chain's `may sue when (not married)` (R9 x7, the prohibition's complement, not an act). 24 rows.
- Keep the explicit, sourced permissions on capacity actions: crisis-team R5 (may leave) and R9 (may sue), police R10 (may sue), public-library R4 (may leave), mwpa-sole-trader/suit R15 (may contract), mwpa-suit R16 (may sue when married). They are redundant for enablement under the flag; they stay because they are the institution's own text or the historical act. Their deletion rows read load 0.
- Engine change before the run: `rules_ablate` must not flag the deletion of a `may` on a default-capacity action as `deregulated` (the action was never regulated by permission; it fires freely and is enabled unless barred). Such rows rank normally at load 0. If the engine change is not in by the run, those rows carry `deregulated` and the artefact is recorded as drift, not fixed in place.

Predictions:
1. Layer 1: zero verdict flips across all 25 entries (`check-all --no-cache`, row by row). Each deleted `may X when true` equals the capacity default, and R9's `(not married)` equals "no R4 disability holds".
2. Layer-1 gate (a) to (f) still passes. Iso matches at guard+strands may move because 24 rules leave the matrix; prediction: the care+control cluster (police, cps, coverture) and the airline control still match at the precommitted level, crisis-team still matches nothing, the pairs (c) and (f) are unchanged. If any iso level moves, that is drift and is recorded.
3. Ablation at k=6 and 8: deleting R4 (`must_not sue when married`) flips `no_standing` reachable -> open (freedom up, family no_standing) in coverture-household, mwpa-creditor-exemption, mwpa-property, mwpa-property-narrowed, mwpa-earnings, mwpa-sole-trader (6 entries; mwpa-suit has no R4). `no_standing_persists` does not flip (it already fails for an unmarried subject). R4 load_freedom_up = 1, not deregulated.
4. Tops: coverture-household, mwpa-creditor-exemption, mwpa-property, mwpa-property-narrowed, mwpa-earnings: {R4, R6, R7} at 1. mwpa-sole-trader: {R4, R6}. mwpa-suit: {R6}. All other entries' top sets unchanged from revision 3: police R4, cps R10, companion-* R6, kibbutz {R2, R4}, kibbutz-no-implicit R4, airline R4, footbinding {R3, R9} x2, ectogenesis R5, gestational-surrogacy R5, the controls and the leave pair empty.
5. Row counts: 24 deletion rows and their 24 `~prohibit` variants vanish at each k (48 fewer rows per k); `deregulated_not_ranked` and `offcondition_free_not_ranked` lists lose exactly those ids. No new inconsistent_after, uncounted 0.
6. Rediscovery is not claimed for this revision; the five test entries' expected tops are unchanged and the run is a consistency check of the convention, not evidence (claims L21).

Drift from 1-6 is recorded in plans/priority-slice1-results.md, never edited to match.

### Slice 1 revision 4b: prohibit-variant label on default-capacity actions (preregistered 2026-11-04 local, before the edit)

Author decision (2026-11-04, after docs/reviews/2026-11-04-capacity-convention-rev4-review.md item 2): the `offcondition_free` label is skipped for a `may` on a default-capacity action, because "free off-condition" is that action's baseline, so the prohibit variant is a clean "add a disability" row and ranks normally.

Predictions: (1) exactly one row changes status across the dataset: mwpa-suit `R16~prohibit` leaves `offcondition_free_not_ranked` and ranks with a freedom_down flip (no_standing), load_freedom_up 0; (2) no entry's top set changes; (3) all other rows byte-identical to the revision-4 run apart from timing; (4) layer 1 untouched (no diff run needed; rules_ablate only).

### Decisions settled 2026-11-06 (author, in session; answers to plans/priority-slice1-results.md "Decisions waiting on the author" and the R19 drift in plans/sourcing.md)

1. Derived power for unregulated actions: settled earlier by the default-capacity flag (revisions 3-4; ADR 0013 amendment). Closed.
2. **Ratified**: ASSUMED b (a `~prohibit` row whose rule is already free off-condition is listed, not ranked) and mixed-neither (a family flipping both up and down counts as neither; 0 occurrences so far). No result changes.
3. One-step-effect convention for action obligations: recorded in ADR 0009 (engine); `care_duty_on_women` gloss states the grace. Closed.
4. **Slice 1 close-out first**: run `step_mode` stability and tabulate strand-tag mismatches against the ablation readings, so the layer-4 pass test reads passed or failed, not incomplete.
5. **Flip direction derived from `kind`**: `rules_ablate.UNFREEDOM` (a hand list of names) is replaced by reading `kind: freedom`, with a check that every freedom property is written unfreedom-shaped (its holding is bad for the subject). Preregistered before the engine change; expected effect: mwpa-suit R19 (`no_standing_against_spouse`) ranks.
6. **Slice 2: go, core plus the floor route.** Core as in "Slices" item 2 (goods list and expected readings preregistered; at least three goods properties written independently by a second, fresh-agent encoder; `contested` mandatory; readings table on the care+control cluster). Plus `coverture-floor` from "Candidate for slice 2" with its predictions and the title-route vs floor-route cut-set comparison. Slice 2's plan and preregistration live in plans/priority-slice2.md.

### Slice 1 revision 5: flip direction from `kind` (preregistered 2026-11-06, before any engine edit or run)

Author decision 5 of 2026-11-06. Today the engine signs a freedom flip (up/down) only if the property's name is in a hand table, `rules_ablate.UNFREEDOM`; a freedom property missing from it flips `unsigned` and cannot rank (mwpa-suit R19, plans/sourcing.md "Coverture split and US suit: results").

**Engine change (philosophy-engine).**
- `UNFREEDOM` is deleted. `flip_direction` reads the property: `kind == "freedom"` is signed (verdict moving from {reachable, holds_to_k, persists} to {open, violated, fails} is freedom_up, the reverse freedom_down); any other kind, or a name with no Property, is `unsigned`. The job tuple no longer carries a polarity table.
- **How "unfreedom-shaped" is checked.** The shape (the property's holding is bad for the subject) is a reading of the formula, not something z3 can decide, so it is made an explicit encoder declaration that the loader enforces: `Property` gains `polarity: Literal["unfreedom"] | None = None`, and a model validator rejects any `kind: freedom` property whose `polarity` is not `unfreedom` (loader error, naming the property). Writing a freedom property in the good-when-holds direction is therefore a load error, not a silent sign inversion. Other kinds are not constrained (slice 2 decides what goods carry). Plus an engine dataset test: every freedom-kind property in the dataset declares `polarity: unfreedom`, and every name in the old table is a dataset property of kind freedom (old table kept as a test constant); the residual (freedom-kind names not in the old table) is printed, not pinned, so slice 2 can add freedom properties without editing the engine test.
- Tests that monkeypatched `UNFREEDOM` drop the patch; fixture freedom properties carry `polarity="unfreedom"`. `test_direction_unsigned_without_polarity` is rewritten: a freedom fixture property now signs, a structure one stays unsigned. `load_freedom_unsigned` stays in the row (it can be non-zero only for a freedom flip that does not cross the two verdict classes, which a single check kind cannot produce; expected 0 everywhere).

**Dataset change (computational-liberation).** `properties.yaml` gains `polarity: unfreedom` on each of the 17 freedom properties (read one by one: every gloss states a condition bad for the subject: no exit, no standing, no resources, no contract, uninsured, bound, care by sex, owner controls reproduction, offspring owned, care duty on women). `build.py` passes keys through, so properties.json gains the key; no other line changes. The engine ignores the key until the engine change; layer 1 does not read it.

**Checked from the data before writing this (no run).** Freedom-kind properties: 17. Old table: 16. Freedom-kind minus table = {no_standing_against_spouse}. Table minus freedom-kind = {} (every table name is a dataset property of kind freedom; `female_parent_care_persists` and `care_duty_on_women` included). No property of another kind is in the table.

**Predictions.**
1. The rows that change between the old engine and the new one (ablation, 26 entries, k=6 and 8, same dataset) are exactly the rows whose old output has `load_freedom_unsigned > 0`, and every such unsigned flip is on `no_standing_against_spouse` in mwpa-suit. In each, the flip turns signed (reachable -> open: freedom_up), `load_freedom_unsigned` goes to 0, and family `no_standing` joins `families_up` (raising `load_freedom_up` by 1 unless `no_standing` was already up in that row). `load_freedom` is unchanged in every row.
2. Among ranked rows, exactly one changes: mwpa-suit R19 (deleted, must_not, not deregulated) at k=6 and 8: `flip_directions` {no_standing_against_spouse: freedom_up}, `load_freedom_up` 0 -> 1, `families_up` [no_standing]. Unranked rows of mwpa-suit (a deregulated `may marry` deletion or an offcondition_free prohibit, if their flips include the property) may change too; they are listed, not predicted individually.
3. Top sets: mwpa-suit {R6} -> **{R6, R19}** at load_freedom_up 1; the other 25 entries unchanged. Scoreboard `top_rule_changes` = 1 against a summary from the old engine on the same dataset.
4. inconsistent_after 0, uncounted 0, k-disagreements 0.
5. Layer 1 unchanged: `build.py --check` ok after the rebuild, `pytest -q` passes, `check-all` 134/134 as expected, `diff --baseline` 0 changed / 0 added / 0 removed, gate PASS. (rules_ablate and the Property schema only; rules_lower/rules_reference/rules_checks untouched.)
6. Engine suite passes after the test edits; the only test semantics that change are the ones named above.
7. Strand reading (close-out section below): mwpa-suit R19 (tagged tying) moves from "tying unconfirmed" (up 0) to agreeing with its tag.

Drift from 1-7 is recorded in plans/priority-slice1-results.md ("Revision 5 run"), never edited to match.

### Slice 1 close-out (preregistered 2026-11-06, before any run)

Author decision 4 of 2026-11-06. Two clauses of the layer-4 pass test have no evidence yet: stability across `step_mode`, and a strand-mismatch label. Both are run on the current engine (ENGINE_PIN 27e24c0, before revision 5) and the current dataset (26 entries, with the coverture split), so revision 5 does not leak into them.

**(i) step_mode.** The engine has two modes (`rules_lower.STEP_MODES`): `one` (default; at most one action per step) and `many` (any set of enabled actions per step; the only difference in the lowering is that the at-most-one constraint is dropped). Every `one` trace is a `many` trace, so per property, `many` can only move reachable-side: open -> reachable, holds_to_k -> violated, persists -> fails, never back; this holds for the base and for every ablated entry alike, so flips can still appear or vanish.
Runs: `phil rules ablate --k 6,8 --workers 4 --step-mode one|many`, 26 entries, plus a second `one` run for determinism. Comparison per (entry, row id, k): ranked status, load_freedom_up, load_freedom_down, flips; per entry: top set.
Criterion (fixed now): the clause passes iff every ranked row's `load_freedom_up` is identical across the two modes at k=6 and at k=8 (which implies identical top sets). Differences only in unranked rows, freedom_down, or structure/failure-mode flips are reported and do not fail it. The determinism clause passes iff the two `one` runs agree on every row apart from timing.
Predictions:
1. Top sets identical in all 26 entries at both k. Reason: every top is a disability on one actor's capacity (leave, sue, contract, sleep_home, refuse_binding, assign) or one obligation (ectogenesis/surrogacy R5); the unfreedom it carries holds from the first steps and does not need two actions in one step.
2. Every ranked row's load_freedom_up identical: clause passes.
3. Some rows differ elsewhere: at most 10 rows per k over the dataset, in unranked rows, freedom_down columns or failure-mode/structure flips; most likely where two parties' actions must coincide (care plus birth in ectogenesis/surrogacy under the one-step-grace `care_duty_on_women`; bind plus marry_off in footbinding; double_burden/creditor_shield in the MWPA chain).
4. inconsistent_after 0, uncounted 0 in both modes; k-disagreements 0 under `one` (as before) and under `many`.
5. The two `one` runs are identical row for row.

**(ii) strand mismatches.** Method (fixed now). For each rule of each entry, its reading uses its *ranked* rows at k=6 (the deletion row and, for a `may`, the `~prohibit` row; a deregulated or offcondition_free row is not used); a rule with no ranked row is "not readable (unranked)". up = max load_freedom_up over those rows, down = max load_freedom_down. Goods load does not exist yet (no goods property), so load_goods = 0 everywhere and the table's "zero goods" half is vacuous: a reading of "tying" now means "high freedom load and goods unmeasured", and every reading below is provisional until slice 2. "High" = up >= 1 (the dataset's maximum is 1).
What can be read now:
- **reads tying** (up >= 1). Tag `tying`: agrees. Tag `rival` or `superadditive`: **mismatch M1** (the table would call it tying, or a hard case once goods exist; it cannot read rival or superadditive).
- **reads protection** (up 0, down >= 1: the rule, or the permission, is load-bearing for a freedom). Tag `tying`: **mismatch M3** (a tie that protects). Tag rival/superadditive: no reading to compare.
- **no reading** (up 0, down 0). Tag `tying`: "tying unconfirmed" (M2): not a contradiction, the table has no row for low freedom and zero goods; listed, not counted as a mismatch. Tag rival/superadditive: not readable (telling rival from superadditive or constitutive needs goods load).
What cannot be read now: any `constitutive` or `hard case` reading; any confirmation of `rival` or `superadditive`.
Predictions (the up >= 1 rows are known from the revision-4b run and the coverture-split results; tags read from the dataset, no run):
6. reads tying: 36 rule instances. Tagged `tying`, agreeing, 18: R4 (sue) in the seven chain entries that keep it (coverture-household, -us, mwpa-creditor-exemption, -property, -property-narrowed, -earnings, -sole-trader), R7 (contract) in six (all those but sole-trader), kibbutz-childrens-house R2, footbinding and footbinding-no-pledge R3, ectogenesis and gestational-surrogacy R5.
7. **M1: 18, all tagged `rival`, none superadditive**: the exit bar R6 in eight chain entries (coverture-household, -us, and the six mwpa-*), police-crisis R4, cps R10, companion-* R6 (3), kibbutz R4 (both entries; sleep_home), airline-flight R4, footbinding R9 (both; refuse_binding). All carry the `cannot_exit` family. Reading: the hand tags file bars on exit as rival; the ablation reads them as the most load-bearing ties.
8. M3: at least 1: mwpa-suit R16 (`may sue`, tagged tying) via `R16~prohibit` (freedom_down on no_standing, revision 4b). Expected 1 to 5 in all.
9. M2 (tying unconfirmed): 20 to 45 rule instances, including mwpa-suit R19 (its flip is unsigned on this engine; revision 5 is predicted to move it to "agrees"), the chain's R11 (creditor must_not attach; its only property is a failure mode), and tying obligations in police-crisis, cps and the leave pair.
10. Clause (ii) passes (at least one mismatch labelled and reported). Tags are not edited.

**Verdict rule.** With (i) and (ii) passing, plus the clauses already evidenced (zero silent errors, stable across k, kibbutz R2 and ectogenesis R5 at the top), the layer-4 test reads **passed**, carrying the revision-3 calibration disclosure: the rediscovery clause was met after fixes that saw the misses, so it is not blind evidence (claims L21). If either clause fails, the verdict is "failed on <clause>", reported as such.

Drift from 1-10 is recorded in plans/priority-slice1-results.md, never edited to match.
