# Role cardinality: N agents per role in the entailment layer (plan, 2026-11-08)

Status: PLANNED, not started. Named in ADR 0018 as the future engine change poly needs. Sequenced after plans/informal-rules.md slice 1 (first composite, hospital rediscovery) and before marriage batch 2 and plans/dynamics-sticks.md, both of which it feeds. Facts below are from a read of the engine and dataset on 2026-11-08; line numbers from that read.

## Why

Layer 1 has exactly one agent per role, named after the role (`rules_reference.py:95`, `rules_lower.py:866`). Three things cannot be said until that changes:

1. **Poly.** The Somerville and Cambridge multi-partner domestic-partnership ordinances (plans/marriage-bundle.md) differ by a cap on partners. "At most two" is a count over instances of one role; with one instance per role there is nothing to count.
2. **Within-role heterogeneity.** The layer-2 MWPA run needs propertied and unpropertied wives at once (ADR 0015 A2, deferred for exactly this reason). Slice 2 already has `financial_dependence_unpropertied` as a separate property because the layer cannot hold two wives.
3. **Per-agent sanction state.** The frozen layer-2 gate (a) failed because `pledged(family)` is one shared atom: "with one shared atom the first pledger lifts R5 for every family, so the sanction cannot discriminate pledgers from non-pledgers" (docs/reviews/2026-11-04-abm-slice4-review.md, "For the author on A2"). The ABM has twenty agents per role (`abm/model.py:216-222`) but reads rule semantics from a `Reference` with one agent per role and keeps one shared role-level state (`model.py:3`, `:178`, `_readings`). Per-agent state in the ABM needs instance-level grounding in the layer it asks.

## What is already there (smaller than feared)

- **Properties already quantify.** `forall`/`exists` over the sorts `agent` and `step` exist in the property language (`sexpr.Quant`, `rules_lower.py:579+`, expansion at `lower_property` 809-853). All 34 properties quantify over `agent`; none uses a role name as an agent literal. Role identity enters through fluent `arg_roles` only (e.g. `backlash` is `(exists ((h agent) (w agent)) (and (married h w t) ...))`, and `married` typed `[husband, wife]` makes the one tuple). So the property language does not need quantifiers added; it needs the instance domain under it to grow.
- **Correction to ADR 0018 and plans/composition.md, to apply:** the "nine properties name husband/wife literally and stop applying to neutral composites" claim is wrong. Those properties are typed through `arg_roles`, which aliases rewrite, so they should apply to composites unchanged. The `female`-variant work shrinks to the properties that read sex at all (`care_assigned_by_sex`, `female_parent_care_persists`, `care_duty_on_women`), which already read the `female` fluent. Preregister that the nine apply to the first composite with no variant.
- **The ABM population code exists** but has no agent names (Mesa `unique_id` only; `abm/agent.py:95-96`) and no (role, index) key despite its docstring. It cannot be reused as-is for naming, but it shows the N-per-role loop and the role-keyed caches that would need instance keys.

## What changes

| Piece | Today | With cardinality |
|---|---|---|
| `RoleDecl` | name, gloss | plus `count: int = 1` (default keeps every existing entry identical) |
| Agents | `[r.name for r in roles]` | `husband` when count is 1 (unchanged); `husband_1..husband_N` when count > 1 |
| Typed fluent tuples (`rules_reference.py:225-228`) | the single `tuple(arg_roles)` | product over the instances of each arg role; distinctness within a tuple kept (`_bindings` 284-288) |
| Untyped fluents | product over all agents | same, over more agents; see Cost |
| `initial` literals (`rules_lower.py:287-304`, 968-984) | must name roles | may name an instance (`husband_2`) or a role; a role name with count > 1 means EVERY instance (ASSUMED; alternative: error, force instance names) |
| Action-instance restriction (`:273`) | actor slot must be an attribute role | actor slot must be an instance of an attribute role |
| Rule `attribute` | one agent | ranges over instances; a rule instance per actor instance |
| Properties | quantify over agents | unchanged syntax; a `count` atom is new: `(atmost 2 ((x agent)) (partner_of p x t))` lowered to a Z3 PbLe over the instance Bools. Needed only for caps |
| Cards | roles listed | show `count` and instance names when > 1 |
| ABM | shared role-level state, `agents_per_role` | reads instance-level `Reference`; A2 per-agent state becomes the natural reading. Separate slice; see Sequencing |

## Cost

Bools per fluent per step grow as (agents)^arity. A 2-role arity-2 untyped fluent has 4 tuples today, 28 Bools at k=6; at count 3 for both roles it has 36 tuples, 252 Bools. Rule instances grow the same way (a 3-variable untyped rule: 24 distinct bindings today, 1320 at 12 agents). Property expansion is agents^|vars| with no distinctness filter. Mitigations, in order: `count` defaults to 1 and is raised per role per entry only where a question needs it (2 wives, 3 partners); the 97 untyped fluents (of 336) in the dataset are the real exposure, and the coverture-household entries are all-untyped (16 of 16), so the first cardinality entry should be a typed one; k stays at 6; measure wall time on the first entry before writing a second.

## Checks that can fail (preregister before the engine change lands)

- Q1. With every `count` at its default, `phil rules diff` over the 27 entries is clean and `check-all` matches 146/146. The change is invisible until used. Preregistered 2026-11-08 before the run: engine branch cardinality-q1, every count at default; expected diff 0 changed of 146 and check-all 146/146.
  Result 2026-11-08 (engine PR reeswrites/philosophy-engine#4, 994eee0): diff 0 changed of 146; check-all 146/146; 694 tests. New module `rules_roles.py` is the single role→agents mapping; `atmost`/`atleast` lower to PbLe/PbGe in properties and rule conditions; ceiling 3 via `PHIL_MAX_ROLE_COUNT`; `initial` role-name-with-count>1 is an error unless `rules_roles.INITIAL_ROLE_EVERY_INSTANCE` is set (author decision still open). Gaps recorded by the builder: cards do not yet show `count`; typed fluent tuples have no distinctness filter (matches count-1 behaviour); multi-variable `atmost` counts all bindings; 2-wife toy at k=6 is 33 Bools.
- Q2. The first composite (coverture-household-us + hospital-visitation, neutral roles) runs the nine properties ADR 0018 called inapplicable, with no variant. If any is inapplicable, the ADR was right and this plan's correction is wrong; record which.
- Q3. A two-wife MWPA entry (`wife.count: 2`, one `owns` in `initial`, the other not) makes `financial_dependence` and `financial_dependence_unpropertied` readable on one entry; preregistered verdicts: dependence holds for the unpropertied instance and not the propertied one under mwpa-property. Drift recorded.
- Q4. A multi-partner pair: `dp-somerville` (no cap) vs `dp-cambridge` (cap; verify the actual ordinance text first, plans/sourcing-worklist-marriage.md style) differ by one `atmost` rule; property `third_partner_can_register` flips between them. This is the poly test.
- Q5. ABM gate (a) rerun with per-family `pledged` on instance-level grounding. The slice-4 review says per-agent state is necessary but not sufficient for Mackie's collapse (the pledge also pays the default and is lawful), so the honest preregistration is: (a) still FAILS unless the pledge-cost decision is also taken; a PASS would be a surprise and goes in docs/surprises.md.

## Sequencing

1. After informal-rules slice 1 has run (the composite exists and Q2 can be checked at the same time).
2. Engine slice: `count`, instance naming, grounding, `initial` semantics, `atmost`/`atleast`, cards. Q1 first, on the unchanged dataset.
3. Dataset: Q3 (two wives) as the first use, since it closes an open slice-2 workaround; then Q4 (poly pair), which also needs the consent guard note and the marriage batch-2 sourcing.
4. ABM: move state to per-agent on the new grounding (ADR 0015 A2 decided), rerun gate (a) as Q5. This is the step that can reopen layer 2 honestly, and it is the step plans/dynamics-sticks.md needs for its Loving gate.

## Open for the author

- `initial` semantics when a role has count > 1 and a literal names the role: every instance (proposed) or error.
- Whether `atmost`/`atleast` live in the property language only, or also in rule conditions (a cap is a rule: `clerk must_not register when (atleast 2 partners)`). Rules need it for Q4; proposing both, same lowering.
- A ceiling on `count` for runtime (3?) enforced by `build.py --check`, so nobody writes 20 by accident.
- Whether the ABM step (4) is part of this slice or its own, given layer 2 is frozen and reopening it is the author's call.
