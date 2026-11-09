# ssi-marriage-penalty entry and pair (2026-11-08)

Status: PREREGISTERED (commit ba5b4b0, before any run); RUN 2026-11-08, results recorded under "Results" below; COUNCIL DONE 2026-11-08 (docs/reviews/2026-11-08-ssi-{correctness,faithfulness,card-only}.md; faithful with reservations); MECHANICAL FIX PASS APPLIED (wording, pins, levels; no verdict moved); REVISION 2 RULED 2026-11-08/09 AND RUN 2026-11-09 (section "Revision 2 run" at the end); REVISION 2 COUNCIL DONE 2026-11-09 (docs/reviews/2026-11-09-ssi-rev2-{correctness,faithfulness,card-only}.md; the card-only seat paused the batch) AND POST-COUNCIL FIX PASS APPLIED 2026-11-09 (prose and card rendering only; no verdict moved; five items open for the author). The preregistration sections are unedited. Written and committed before the first `phil rules check`, `ablate` or `diff` over either entry. Engine: ENGINE_PIN b5fd019. Branch `ssi-entry`. Inputs: plans/sourcing-worklist-marriage.md section 5 (Entry 2) and its Gaps, docs/connections.md section 4 (C2), plans/disability.md (SSI), plans/composition.md, ADR 0018, data/institutions/src/lease.yaml as the model.

## What was built

- `data/institutions/src/ssi-marriage-penalty.yaml`: roles claimant, spouse, agency. Base fluents `married`, `cohabits`, `holds_out`, `resources_under_limit`; derived power fluents `couple_rate`, `couple_limit`, `individual_rate`, `individual_limit`, `eligible` (each reads `enabled` of an agency action, the convention of `can_sanction` and `has_standing`). Seven rules: R1 agency may pay a benefit; R2 may apply the couple rate when married; R3 may apply the couple resource limit when married; R4 may apply the couple rate when cohabiting and holding out (the displaced gate); R5, R6 individual rate and limit when neither married nor holding out; R7 disability: must_not pay when resources are not under the limit. `function:` on R2 (`penalises_marriage_rate`), R3 (`penalises_marriage_limit`), R4 (`extends_penalty_to_holding_out`).
- `ssi-marriage-penalty-individual`: the pair, penalty removed. R2, R3, R4 dropped; R5, R6 lose their marital-status condition. **Holding out is dropped, not kept**: with no couple rate there is nothing for the test to gate, and no reform text was read that retains it (S. 73 of 2025 is an unopened lead).
- Five new properties in `properties.yaml`, which are encoding checks (each restates one rule), not findings (the 34 older ones all need fluents this entry does not declare): `married_couple_rated`, `married_couple_limited` (both freedom/unfreedom, invariant: the penalty holding), `penalty_reaches_unmarried` (failure_mode, reachable), `married_rated_individually` (structure, reachable: the penalty absent), `over_limit_ineligible` (freedom/unfreedom, invariant). Names, formulas and kinds are fixed here, before the run.
- Six bibliography works in `data/sources/rules.yaml`. Every provenance excerpt was carried from the worklist, whose fetches returned model summaries rather than raw text; none was re-opened by the builder. After the council all carried rows are `snippet` (ADR 0017 s.3), not `opened`; the faithfulness seat confirmed 416.1802(b)(1) and (d)(1), 416.1806(a)(3) and 1382(a)(3)(A)-(B) verbatim from raw text.

## Declared deviations from the brief (before the run)

1. R4 has `sanctioner: none`, not `state`, because R4 is an agency `may` power with no duty to sanction (the engine also rejects a sanctioner without an `or_else`). Overpayment recovery (20 CFR 416.537, not opened) sanctions the claimant under a different, unencoded rule. This is not "no sanction in any source". The displaced reading therefore cannot use a sanctioner difference; it can read attribute sets only. (Wording corrected after the council, 2026-11-08; the earlier reason was wrong.)
2. Rules are `may` powers, not the statute's mandatory `must`: an action `must` fires every step and blocks every other action (ADR 0009), and a must-be needs the establishing action to carry the rate. The penalty is therefore represented as a power the rules grant. Because an action no rule names stays free in traces, only the derived fluents see the rules; this is why every property here reads a derived fluent.
3. Holding out is a second route to the couple rate on the same aim as R2, not a rewrite of `married`, because a derived fluent cannot read `married or holds_out`.
4. Dollar amounts ($2,000 / $3,000; $994 / $1,491) are not representable; only which limit and rate the agency may apply.
5. "Consent guard note (plans/consent-guard-note-DRAFT.md) ruled not applicable to benefits rules by the author, 2026-11-08."

## Preregistered verdicts (k = 6 and 8, `--init declared`, strict, step-mode one)

| Property | ssi-marriage-penalty | ssi-marriage-penalty-individual |
|---|---|---|
| married_couple_rated | holds_to_k (non-vacuous) | violated |
| married_couple_limited | holds_to_k (non-vacuous) | violated |
| penalty_reaches_unmarried | reachable | unreachable_open |
| married_rated_individually | unreachable_open | reachable |
| over_limit_ineligible | holds_to_k (non-vacuous) | holds_to_k |

The 34 older properties: all `not_applicable` on both entries (no fluent they need is declared except `married`, which no older property reads alone). Any older property that turns out applicable is a miss on this line.

Why these: in the base, R2 gives every married pair the couple-rate power, R3 the limit power, R4 gives the power to a cohabiting holding-out pair (so a non-married pair can have it), nothing grants an individual rate to a married pair (R5's condition excludes marriage), and R7 bars payment over the limit. In the pair no rule names `apply_couple_rate` or `apply_couple_limit`, so the derived couple fluents are constant false (the engine warns), and R5 grants the individual rate to married pairs.

## Preregistered ablation of the base (`phil rules ablate --entry ssi-marriage-penalty`, k 6,8)

Flips expected, per deleted rule, among the five new properties:

| Deleted | Expected flip | Rationale |
|---|---|---|
| R1 | none | R7 still names `pay_benefit`, but no `may` remains, so `eligible` is false throughout, which makes `over_limit_ineligible` true as before. A deregulation flag may appear; it is not a verdict flip. |
| R2 | married_couple_rated holds_to_k -> violated | a married pair that is not holding out has no couple-rate power; R4 does not cover it |
| R3 | married_couple_limited holds_to_k -> violated | nothing else grants the couple limit |
| R4 | penalty_reaches_unmarried reachable -> unreachable_open | the only non-marriage route to the couple rate is gone |
| R5 | none | no property reads the individual rate except through `married`, and R5 excludes marriage |
| R6 | none | no property reads `individual_limit` |
| R7 | over_limit_ineligible holds_to_k -> violated | R1 still grants the power and nothing bars it |

Total expected flips: 4 rules with one flip each (R2, R3, R4, R7); three rules with none (R1, R5, R6). `function:` predictions are the same three rows: deleting R2, R3, R4 flips respectively the property named; an unsupported function (no flip) would be recorded as such.

## C2, first half (docs/connections.md section 4)

Claim as written: an SSI/Medicaid asset-and-marriage entry will not match the care+control cluster at any level, and deleting its marriage-penalty rule alone flips nothing among the existing properties.

Preregistered here:

- (i) `phil rules iso` of `ssi-marriage-penalty` against coverture-household, police-crisis, cps and lease reports no match at any level (the entry has no care strand and no `provides_care`, `is_subject`, `can_sanction` or `can_exit`).
- (ii) Deleting R2 (and, separately, R3) flips none of the 34 older properties, because all 34 are `not_applicable` on the standalone entry.
- Expected reading: (ii) holds **vacuously**. A check over properties that are not applicable cannot fail, so it is evidence recorded, not evidence for. The claim stays `untested` unless an older property is applicable and unflipped. The flips in the table above (R2 flips `married_couple_rated`) are among five new properties written for this entry; the claim as written names the existing ones, so they neither support nor refute it. The second half (deleting it in the composite flips `financial_dependence`) is P2 and is not run here.

## `phil rules diff` over the existing 27 entries

Expected: 0 changed, 0 removed over the baseline's rows; new rows only for the two new entries (and possibly none, if the baseline file lists only its own entries). Properties added to `properties.json` are `not_applicable` on every older entry (each names fluents only the SSI entries declare, `couple_rate` and the like, or reads `married` with `individual_rate`), so no old row should move. Anything else is recorded, not tuned.

## Drift and surprises

Any result other than the tables above is recorded below against the row it contradicts, in the entry that follows this section, and never edited into the preregistration; an unpredicted flip also gets a row in docs/surprises.md.

## Results (run 2026-11-08, engine b5fd019, k 6 and 8, declared, strict, step-mode one)

Recorded against the preregistration; nothing above was edited.

**Verdicts.** `phil rules check` on both entries at k=6 and k=8: all 10 property verdicts match the table (5/5 on each entry at each k; `open` is the engine's word for unreachable_open). Both entries pass with no vacuity flags. The pair prints two warnings (derived `couple_rate`, `couple_limit` name actions no rule regulates), as predicted. The older properties: not applicable (the ablation header reads "5 properties applicable, 35 not applicable"; the dataset lists 39 properties, and the header's 40 is explained: `expand_contested` adds the contested-reading variant `provided_for@encoder-2`, so 39 becomes 40; on the raw 39 the split is 5 applicable and 34 not (correctness review, item 5)).

**Ablation of the base** (`phil rules ablate --entry ssi-marriage-penalty`). Expected flips held: R2 -> married_couple_rated holds_to_k > violated; R3 -> married_couple_limited holds_to_k > violated; R4 -> penalty_reaches_unmarried reachable > open; R7 -> over_limit_ineligible holds_to_k > violated; R1, R5, R6 -> no flip. `function:` predictions on R2, R3, R4 all fired (none unsupported). Total 4 of 4 predicted flips, 0 of 3 predicted non-flips contradicted.

Drift and readings, recorded, not tuned:

1. **R4's prohibit variant flips a second property.** `R4~prohibit` (the engine's prohibit variant of a `may`, a disability on the couple-rate power under the holding-out condition) flips `married_couple_rated` as well as `penalty_reaches_unmarried`. Not preregistered (the preregistration covered deletion only). Reason: the disability bars `apply_couple_rate` for any pair that is cohabiting and holding out, including a married pair, so married holding-out pairs lose the power. An artifact of what a prohibit of R4 means, not a finding about SSI. Logged as a surprise (docs/surprises.md S5, artifact).
2. **Deregulation flags.** R1, R3, R5, R6 are each the sole regulator of their action, so the engine files their deletion under "deregulated, not ranked" (action becomes unregulated, derived power zeroed). R3 flips `married_couple_limited` but is excluded from the ranking for that reason; R2 and R4 share `apply_couple_rate`, so both are ranked. The preregistration expected a possible flag on R1 only. Reading, not a miss: it means the ranked load table undercounts R3, and the unranked row is the one to read.
3. **Load is zero for R4 in the ranked table.** `penalty_reaches_unmarried` is a failure_mode, which the engine lists but does not count toward load_freedom. R4's flip is real and listed, its `load_freedom` is 0/0. Not predicted in those words.
4. **Isomorphism (C2 (i)).** `phil rules iso` of the entry against coverture-household, police-crisis, cps and lease: iso False at exact and at guard, with and without strands, `care+control: -` in every run. Wording after the council: exact 0/7; guard 1/7 (R2 -> police-crisis R3, agency -> officer); care+control '-' in every run; weak evidence of non-match, since at guard any conditional `may` pairs with any other. The preregistration said "no match at any level"; one run is not literally empty: against police-crisis at the guard level the matcher reports a partial 1/7 pairing, R2 -> R3 (agency -> officer, apply_couple_rate -> detain), a single conditional `may`, which is not a cluster and not iso. Recorded as drift in my wording (partial pairings exist at guard), not as a match. Pair against base: iso False at guard, 2/7 matched (R1, R7), distance 5.
5. **C2 (ii) held vacuously, as preregistered.** All 34 older properties are not_applicable on the entry; deleting R2 or R3 flips none of them because none is run. A check that could not have failed.

**`phil rules diff --baseline data/verdicts-baseline.json`** (after `build.py --write --cards` then `--check`: ok, 29 institutions, 39 properties, 30 cards; pytest 38 passed):

```
note: engine source hash differs from the baseline's
ssi-marriage-penalty: added x5 (married_couple_limited holds_to_k, married_couple_rated holds_to_k, married_rated_individually open, over_limit_ineligible holds_to_k, penalty_reaches_unmarried reachable)
ssi-marriage-penalty-individual: added x5 (married_couple_limited violated, married_couple_rated violated, married_rated_individually reachable, over_limit_ineligible holds_to_k, penalty_reaches_unmarried open)
0 changed, 10 added, 0 removed (of 156 rows)   exit 0
```

The 27 existing entries are clean. The preregistration guessed "possibly none" new rows; the ten additions are the two new entries' own rows.

## Not done here (named, not hidden)

- Mechanical fix pass (2026-11-08): the three council files were read and the wording, pins and levels fixed; every verdict row is unchanged (`phil rules check` output for both entries identical before and after; `phil rules diff` 0 changed, 10 added, 0 removed).
- No composite. `ssi-marriage-penalty` with `coverture-household-us` is P2 (plans/composition.md) and the second half of C2.
- The council has run (see Status); the self-review checklist below is kept as written before it.
- No raw-source re-opening by the builder in the fix pass: carried rows are `snippet`, and R2's 1382(b)(2) pin and R7's 1382(a)(1)(B) bar pin are `unverified` (pins supplied by the faithfulness seat's raw read).

## What P2 will need (composite with coverture-household-us)

1. **Aliases:** `coverture-household-us`: husband -> partner_a, wife -> partner_b; this entry: claimant -> one of them (the claimant may be either; the choice decides whose penalty `financial_dependence` reads), spouse -> the other, agency stays a third role. `married` is typed [claimant, spouse] and coverture's is untyped, so typed wins by the unification table; confirm the arg order matches (h, w) after aliasing.
2. **A shared fluent that carries SSI into `financial_dependence`.** The property reads `is_subject`, `controls_own_property`, `owns_earnings`; this entry declares none and writes none. Without one, deleting R2 in the composite flips nothing the older properties read, and C2's second half fails by construction, not by the claim. Options to preregister: declare `is_subject` on the claimant; have the benefit supply `has_own_income` (coverture's is derived `(enabled draw_subsistence w)`, so a same-name derived fluent with a different definition is a unification error, ADR 0018); or add an SSI-specific `means_tested_income` fluent and a new property. This is an entry change and should be preregistered.
3. **Derived-fluent names in common:** none now (`couple_rate`, `eligible` and the rest are new to the dataset), so no conflict, but `eligible` and `individual_rate` need `exists g` over the agency role, which composition must keep typed.
4. **Prohibit/deregulation reading:** R3 and R1, R5, R6 land under "deregulated, not ranked" in the entry; in a composite, check that the composite's ranking does not hide them again.
5. **A dollar-valued penalty is out of scope** of the engine's boolean fluents; P2 can show where load moves, not how large the penalty is.

## Self-review checklist (council pending)

The council could not be spawned. These are what each seat must check; the batch is marked **council pending** until they run.

**Correctness seat** (does the engine mean what the entry says?):
- Does every derived fluent actually read the rule it is named for? Probe by deleting R2 and reading `couple_rate`, and by deleting R4 with a married holding-out pair.
- Is the `exists ((g agent))` over the agency role really one agent, and does `(enabled apply_couple_rate g c s)` respect the attribute scoping (agency only)?
- The R4~prohibit double flip: confirm it is the disability reading and not a lowering bug; confirm the base R2/R4 overlap (both name `apply_couple_rate`) makes R2 deletion non-deregulating.
- Is `resources_under_limit` initial-true the only initial literal needed, and does `init declared` honour it? Does `over_limit_ineligible` hold only because R7 is a hard must_not (not vacuously because `accumulate` is unreachable)? Check the vacuity flags and the antecedent reachability by trace.
- The invariant `married_couple_rated` is `holds_to_k` at k=6 and 8; is `marry` reachable at k=6 (so it is not vacuous)?
- Does `married_rated_individually` unreachable_open mean "not within k" only, never "safe"?

**Faithfulness seat** (does the entry say what the sources say?):
- Re-open the six sources raw (the worklist's fetches were summaries): confirm every excerpt carried into `provenance`, including the worklist's own typo in 416.1802 ("calculated"), and upgrade or downgrade the levels.
- R2 and R3 are `may`, the statute is mandatory: is the power reading acceptable, or must a state-obligation encoding be tried? R4 should be checked against 416.1806 (a)(3) in full: the reg says opposite sex; POMS covers same-sex pairs; the encoding follows POMS.
- R7's bar (over the limit, no payment) rests on no excerpt (unverified); open 42 U.S.C. 1382(a)(3)(A) and 20 CFR 416.1205.
- R5 and R6 conditions (neither married nor holding out) are the encoder's complement; the three tests in 416.1806 (a)(1)-(3) are not all encoded (formal marriage, and (a)(3) holding out; the other test is not read).
- The `sanctioner: none` on R4 against the brief's `state`: decide whether to invent the recovery or appeal sanction, with a source, or to accept none.
- 2026 rates and limits are an unverified lead; `penalty` size is nowhere in the encoding.
- The pair keeps R1 and R7 and drops holding out; confirm no reform text keeps the test.

**Card-only seat** (reading the generated cards without the source):
- Read `docs/cards/ssi-marriage-penalty.md` and `docs/cards/ssi-marriage-penalty-individual.md` only: can the reader say what `couple_rate` means, that it is a power not an applied rate, and which rule makes a married pair penalised? Is the word "penalty" defined? Is `holds_out` readable as conduct?
- Does the card show the weakest provenance per rule (R1 and R7 unverified) and the dropped holding-out rule in the pair?
- Do the card's property names (`married_couple_rated`) read as the penalty holding, and `married_rated_individually` as the penalty absent, without the plan?

Council pending.

## Revision 2 (author decisions)

Items the council raised that could move a verdict or change a rule. The mechanical pass did not touch them.

1. **Cohabitation condition on R2 and R3.** The source states the couple rate and limit for a spouse "with whom he or she is living" (416.1801(c); 1382(a)(1)(B)(i)); the rules carry `married` alone, so a separated married pair gets the couple rate. Add `cohabits`, or keep the gap declared. Same complement gap on R5 and R6.
2. **`must` on a state fluent with an establishing action, or `may`.** The lease R2 pattern (ADR 0009 must-be) is available here; `may ... when true` was a choice, not forced (correctness item 3). Either try the must-be encoding or label the entry "power reading only".
3. **R1 and the pair's R5/R6 as `default_capacity`** instead of `may ... when true` (cards/README.md convention).
4. **One-rule pair choice.** The pair is a 5-rule reform pair. Candidates: drop R3 alone (flips married_couple_limited) or drop R4 alone (flips penalty_reaches_unmarried).
5. **R4: follow POMS or the text as written.** The rule follows POMS SI 00501.152 (same-sex couples included); 416.1806(a)(3) says opposite sex. Also unencoded: `unrelated`, and timing (`at or after the time you apply`).
6. **Two unrun checks** (correctness item 9): whether `(exists ((g agent)) ...)` is limited to the agency role (rather than any agent), and R4 deletion on a married holding-out pair.

### Revision 2 rulings (author, 2026-11-08; applied in the faithfulness batch, preregistered there before any run)

- Item 1 (cohabitation): **add a `cohabits` fluent** and condition R2, R3, R5, R6 on it. Chosen over "keep the gap declared" because every composite built on SSI inherits the over-application, and the same fluent is wanted by the hospital and two-wife entries. Verdicts may move; preregister and rerun.
- Item 5 (R4 sex condition): **leave sex unencoded.** No opposite-sex condition; notes cite both 416.1806(a)(3) (opposite sex) and POMS SI 00501.152 (same-sex included) and declare the gap. Chosen over following the text (historically true pre-2015, not now) and over following POMS (not the cited regulation). Consistent with ADR 0018 neutral roles.
- Items 2, 3, 4, 6: still open; recommendations go in plans/faithfulness-batch.md.
- Item 2 (must-be vs `may`), ruled 2026-11-09: **add the "power reading only" label** in the cohabits revision, then try the ADR 0009 must-be encoding afterwards as its own preregistration. Chosen over doing both at once so the two sources of verdict movement are not mixed in one run.
- Item 3 (`default_capacity`), ruled 2026-11-09: **convert R1 and the pair's R5/R6** from `may ... when true` to `default_capacity: true` on the actions, inside the cohabits revision (same convention as batch 3c's B3). Predicted no verdict change.
- Item 4 (one-rule pair), ruled 2026-11-09: **drop R3 alone** (flips married_couple_limited). Chosen over dropping R4 because the couple resource limit is the lever the marriage-penalty bills actually pull.

### Revision 2 item 6 probes (run 2026-11-08, engine at ENGINE_PIN)

Engine 81d5b9e (ENGINE_PIN; philosophy-engine HEAD). Both probes run on copies of `data/institutions/{institutions,properties}.json` in the scratchpad dir `ssi-probe/`; no file under data/ was touched. Runner: `/Users/rees/Documents/computational-liberation/.venv/bin/phil` (the worktree has no .venv), cwd the scratchpad, flags as in Results: `--k {6,8} --init declared --compliance strict --step-mode one`, plus `--no-cache --institutions <copy> --properties <copy>` on every `check`.

**Probe A: does `(exists ((g agent)) (enabled apply_couple_rate g c s))` range over any agent, or only the agency?**

Code reading (`philengine/rules_lower.py`): `lower_state_formula` lowers a `Quant` with `_typed_domains(names, {}, G.agents)`, an empty type map, so the `exists` enumerates every agent (claimant, spouse, agency). It is `G.enabled` that confines it: it returns constant False for any args tuple not in `G.action_instances[action]`, and `ground()` builds those instances (1) typed by the action's `arg_roles` or the prefix heuristic (`apply_couple_rate` declares no arg_roles; `g` is a prefix of no role, so it is untyped; `c` -> claimant, `s` -> spouse), (2) pairwise distinct, and (3) attribute-scoped: the first argument's role must be the `attribute` of some rule naming the action. The fluent's own `arg_roles: [claimant, spouse]` types only the fluent's tuple (c, s), not the witness `g`. So the restriction to the agency is a property of the rules as written (every rule on `apply_couple_rate` has `attribute: agency`), not of the `exists`.

Direct enumeration (`ssi-probe/instances.py`, `ground(inst, k=2, init="declared")`):

| file | `apply_couple_rate` instances | `(enabled apply_couple_rate g claimant spouse)@1` per g |
|---|---|---|
| base copy | `[(agency, claimant, spouse)]` | claimant: const False; spouse: const False; agency: `Or(married, And(cohabits, holds_out))` |
| probeA2 (R2, R4 `attribute: other`, `var_roles g: other`; new role `other`, no other rule) | `[(other, claimant, spouse)]` | claimant, spouse, agency: const False; other: `Or(married, And(cohabits, holds_out))` |

Verdicts (`phil rules check --inst ssi-marriage-penalty`, k 6 and 8 identical):

| Property | base copy | probeA1 (R2 -> `other`, R4 stays agency) | probeA2 (R2 and R4 -> `other`; no agency rule on the action) |
|---|---|---|---|
| married_couple_rated | holds_to_k | holds_to_k | holds_to_k |
| married_couple_limited | holds_to_k | holds_to_k | holds_to_k |
| penalty_reaches_unmarried | reachable | reachable | reachable |
| married_rated_individually | open | open | open |
| over_limit_ineligible | holds_to_k | holds_to_k | holds_to_k |

Verdict does not differ: with no agency rule at all on `apply_couple_rate`, a non-agency bearer satisfies the `exists`, so `married_couple_rated` still holds. Reading: the `exists` is over any agent and the agency restriction is borrowed from the rules' `attribute` lines, which is adequate for this entry alone but is the gap item 6 names for composition: in a composite, any rule by any role on `apply_couple_rate` (or on a same-named action after aliasing) would count as "the agency holds the power". Declaring `arg_roles: [agency, claimant, spouse]` on the five `apply_*`/`pay_benefit` actions would type `g` at the action level; this names the gap only, no edit made.

**Probe B: R4 (holding-out rule) ablated on a married holding-out pair.**

Plain ablation: `phil rules ablate --entry ssi-marriage-penalty --k 6,8 --init declared --compliance strict --step-mode one --institutions <copy> --properties <copy> --json ssi-probe/ablate.json` (exit 0; identical to Results: R2, R3, R4, R7 flip the predicted property; R1, R5, R6 none; R4~prohibit double flip as in S5). R4 rows:

| row | load_freedom (k6/k8) | note | flips |
|---|---|---|---|
| R4 (deleted) | 0/0 | permission removed | penalty_reaches_unmarried: reachable > open |
| R4~prohibit | 1/1 | prohibited | married_couple_rated: holds_to_k > violated [freedom_up]; penalty_reaches_unmarried: reachable > open |

Initial-state override: `phil rules ablate` and `phil rules check` have no flag for it (`--init` selects empty/free/declared only; `--help` read 2026-11-08). The override was done by file: a copy with `initial: [(resources_under_limit claimant), (married claimant spouse), (cohabits claimant spouse), (holds_out claimant spouse)]`, run with `--init declared`, once with all seven rules (probeB1) and once with R4 removed from `rules` (probeB2). k 6 and 8 identical:

| Property | probeB1 married + holding out, all rules | probeB2 same initial, R4 deleted | flip |
|---|---|---|---|
| married_couple_rated | holds_to_k | holds_to_k | no |
| married_couple_limited | holds_to_k | holds_to_k | no |
| penalty_reaches_unmarried | reachable | open | yes |
| married_rated_individually | open | open | no |
| over_limit_ineligible | holds_to_k | holds_to_k | no |

Reading: starting married and holding out, deleting R4 flips only `penalty_reaches_unmarried` (the pair can still `divorce` and keep holding out, but no rule then grants the couple rate to an unmarried pair), while `married_couple_rated` keeps holding because R2 covers the married pair whatever its conduct, so the derived `couple_rate` does read R2 and R4 as two routes and R4 alone is never load-bearing for a married pair. The plain ablation's R4 row says the same (one flip, load 0/0 because the flipped property is a failure_mode); the only R4 verdict movement on `married_couple_rated` is the prohibit variant, S5, an artifact of the disability reading, not of the initial state.

## Revision 2 run: preregistered 2026-11-09, before any edit or run

Engine: ENGINE_PIN e46f6ea; the installed philengine checkout is at 50ed97f (PR #6 on top of the pin, "drop the stale dataset copy"; not touched by this batch, a separate session works there). Baseline 192 rows (k=6, strict, step_mode one). Branch `ssi-cohabits` off main d5d3a92. Inputs read: this file in full; data/institutions/src/{ssi-marriage-penalty,ssi-marriage-penalty-individual,_composites,properties,kibbutz-childrens-house}.yaml; data/institutions/README.md (Conventions; "Default-capacity actions (revision 4)"); plans/faithfulness-batch.md section 8 with its post-council fix pass; plans/informal-rules.md "Rulings 2026-11-09" item 2; docs/claims.md C2a/C2b/C2c; docs/reviews/2026-11-08-ssi-faithfulness.md (R2, R3, R6 rows); scripts/checks.sh; data/verdicts-baseline.json (the 15 SSI and composite rows); philengine rules_lower.py `enabled` and rules_gate.py `crit_c` (read only). No `phil` command was run before this commit.

### Scope

Revision 2 items 1 to 4 as ruled, and the kibbutz R2/R3 `sanctioner` retag (plans/informal-rules.md Rulings 2026-11-09 item 2). Not changed: R4 and R7 of the base (conditions, sources, levels); no provenance level; no excerpt; no new provenance item; no `kind`; the pair's entry id; the four `apply_*` actions stay untyped (the Probe A gap stays declared); no must-be encoding (item 2 is a label only); coverture-household-us; no cluster match row; `penalty_reaches_unmarried`, `married_rated_individually` and `over_limit_ineligible` formulas.

Three things found on reading that the brief did not have, decided here before any run and flagged for the author:

(a) **`cohabits` already exists.** The base declares `cohabits` (arity 2, arg_roles [claimant, spouse]) with setters `cohabit` and `separate`; R4 reads it; it is false in `initial` and it is NOT in `initial_free`. So item 1 adds no fluent and no free world: it adds a conjunct to four conditions. No holds_to_k row becomes conditional on a free input.

(b) **Item 1 x item 4 need the two invariant formulas to follow the rules.** `married_couple_rated` and `married_couple_limited` are `(=> (married c s t) (couple_rate|couple_limit c s t))`. Once R2 and R3 carry `cohabits`, a pair that weds without living together violates both in the base, and then dropping R3 flips nothing (violated on both sides), against ruling 4 ("drop R3 alone (flips married_couple_limited)"). The two properties are, by this file's own words, "encoding checks (each restates one rule)"; the rule they restate now reads "a spouse with whom he or she is living". Resolution: the antecedent of both becomes `(and (married c s t) (cohabits c s t))`, glosses reworded. This is a property edit the rulings do not name. Alternative not taken: leave the formulas, in which case the predicted moves would be base and composite `married_couple_rated` and `married_couple_limited` holds_to_k -> violated and the pair would separate on nothing. `married_rated_individually` is NOT edited (it restates no rule); it is predicted to move, below.

(c) **Item 3 x items 1 and 4: only R1 converts.** Ruling 3 names "R1 and the pair's R5/R6" as `may ... when true` rows. The pair's R5/R6 were `when true` only because the five-rule pair replaced them; under ruling 4 the pair is `rules_drop: [R3]` and has no R5/R6 of its own, it inherits the base's, and under ruling 1 those carry a condition. A default capacity cannot carry a condition (README revision 4: enabled "whenever no disability ... holds"). Rule text: base R5 `plain` "The agency may rate the claimant as an individual when the pair are neither married nor holding out"; R6 "may apply the individual resource limit ($2,000) when the pair are neither married nor holding out", and the limit text is for an individual without a spouse "with whom he is living" (faithfulness review R6 row). Both are conditioned powers, not plain liberties. So: **plain liberty: R1 only** (`pay_benefit`, `conditions: 'true'`, "the encoder's grant, so that the resource bar in R7 has a power to remove") -> `default_capacity: true` on `pay_benefit`, R1 deleted. **Conditioned, stay rules: R5 and R6** in both entries, with the cohabits condition of item 1. Not done: turning R5/R6 into default capacities with must_not disabilities for couples (it would invert who bears the burden of the text and is a re-encoding nobody ruled).

Known consequence of (c) and ruling 4, recorded not fixed: in the one-rule pair a married pair living together has neither the couple limit (R3 dropped) nor the individual limit (R6 excludes them). The pair is a one-rule deletion in the ADR 0007 sense, not a coherent reform; the old note said the same of dropping R2 alone. The id `ssi-marriage-penalty-individual` and its old name no longer describe it; the id is kept (renaming removes and adds baseline rows), the `name` is rewritten.

### Edits / Build

1. ssi-marriage-penalty.yaml R2 `conditions`: `(married c s)` -> `(and (married c s) (cohabits c s))`. R3 the same. `plain`, `source` tail and provenance `note` of both: "cohabitation condition not encoded; revision 2 item" -> encoded 2026-11-09 (revision 2 item 1), citing 20 CFR 416.1801(c) and 42 U.S.C. 1382(a)(1)(B)(i) as already cited; excerpts and levels untouched.
2. Same file R5, R6 `conditions`: `(not (or (married c s) (and (cohabits c s) (holds_out c s))))` -> `(not (and (cohabits c s) (or (married c s) (holds_out c s))))`, the exact complement of the two couple routes (R2: married and living together; R4: living together and holding out). `plain`: "neither married nor holding out" -> "not living together as a married or holding-out couple (a married pair living apart is rated individually)".
3. Same file, item 3: action `pay_benefit` gains `arg_roles: [agency, claimant]` and `default_capacity: true`; rule R1 deleted (ids not renumbered). R7 `plain`/`source` and `notes` say the power R7 removes is now a default capacity. `eligible` gloss unchanged.
4. Same file, item 2: `name` gains "power reading only"; `notes` gains a "POWER READING ONLY" sentence (every rule is a power the agency holds, not the statute's mandatory duty; the ADR 0009 must-be encoding is a later preregistration) and the revision 2 record; the "Unencoded, revision 2 items" sentence drops the R2/R3 cohabitation gap. `expected_properties.married_rated_individually`: unreachable_open -> reachable.
5. ssi-marriage-penalty-individual.yaml, item 4: `rules_drop: [R2, R3, R4]` -> `[R3]`; `rules_replace` removed; `minimal_pair_of: {id: ssi-marriage-penalty, rule: R3, differs_on: married_couple_limited}`; `name` rewritten (couple resource limit removed; one-rule pair; power reading only); `expected_properties`: married_couple_rated holds_to_k, married_couple_limited violated, penalty_reaches_unmarried reachable, married_rated_individually reachable, over_limit_ineligible holds_to_k; `notes` records the previous five-rule pair (R2, R3, R4 dropped; R5, R6 replaced by `when true` rows; differs_on married_couple_rated; its five verdicts) and the known consequence above.
6. properties.yaml: `married_couple_rated` and `married_couple_limited` antecedent `(married c s t)` -> `(and (married c s t) (cohabits c s t))`; glosses reworded ("married and living together"). `married_rated_individually` gloss gains one clause (reachable in the base since revision 2: a married pair living apart).
7. _composites.yaml coverture-us-ssi: `expected_properties.married_rated_individually`: unreachable_open -> reachable; `notes` gains one sentence (revision 2, power reading only). Nothing else.
8. kibbutz-childrens-house.yaml R2 and R3: `sanctioner: peers` -> `institution`. The brief also says to drop their `sanctioner_review: derived`; both rows already read `sanctioner_review: reviewed` (only R6 is `derived`, and R6 is not in scope), so there is nothing to drop and `reviewed` stays. kibbutz-childrens-house-no-implicit inherits R3.
9. `python data/institutions/build.py --write --cards`; data/institutions/README.md line for the SSI pair if it states the pair's shape.

### Predictions

- `build.py --check` after `--write --cards`: ok, 33 institutions, 43 properties, 34 cards. Emitted rule rows 287 -> 286 (base 7 -> 6; composite 14 -> 13; pair 4 -> 5: R2, R4, R5, R6, R7).
- `phil rules diff --baseline data/verdicts-baseline.json`, first run: **4 changed, 0 added, 0 removed of 192** (so checks.sh prints CHECKS FAILED and exits 1 on the first run, by design):

| # | institution | property | baseline | predicted |
|---|---|---|---|---|
| 1 | ssi-marriage-penalty | married_rated_individually | open | reachable |
| 2 | ssi-marriage-penalty-individual | married_couple_rated | violated | holds_to_k |
| 3 | ssi-marriage-penalty-individual | penalty_reaches_unmarried | open | reachable |
| 4 | coverture-us-ssi | married_rated_individually | open | reachable |

- `phil rules check-all`: 192/192 (the three `expected_properties` edits above are these predictions written into the data before the run).
- `phil rules gate`: PASS; (b) the cluster pairs `partial(care+control)` as now; (e) 192/192. No SSI entry is in a gate criterion.
- `scripts/drop_one_match.py`: (b) fails on deleting exactly coverture-household R2, R5, R6; police-crisis R2, R4, R11; cps R3, R4, R10; `b=PASS rows: 19`. Unchanged.
- `pytest -q`: 40 passed.
- After the baseline is regenerated (`phil rules verdicts --k 6 --no-cache --out data/verdicts-baseline.json`, only if every moved row is one of the four): 192 rows, `0 changed, 0 added, 0 removed (of 192 rows)`, ALL CHECKS OK.

Per-property expectations, k = 6 and 8 (declared, strict, step-mode one), the same at both k:

| Property | ssi-marriage-penalty | ssi-marriage-penalty-individual (drops R3) | coverture-us-ssi |
|---|---|---|---|
| married_couple_rated (edited formula) | holds_to_k, non-vacuous | holds_to_k, non-vacuous | holds_to_k |
| married_couple_limited (edited formula) | holds_to_k, non-vacuous | violated | holds_to_k |
| penalty_reaches_unmarried | reachable | reachable | reachable |
| married_rated_individually | reachable (moves) | reachable | reachable (moves) |
| over_limit_ineligible | holds_to_k | holds_to_k | holds_to_k |

Reasons. married_couple_rated: R2 grants the couple-rate power exactly when married and cohabiting, which is the new antecedent; `wed` then `cohabit` reaches the antecedent by step 2, so no vacuity flag; the pair keeps R2. married_couple_limited: R3 the same in the base and composite; in the pair no rule names `apply_couple_limit`, the derived `couple_limit` is constant false (the engine warns, one warning where the old pair printed two), and the antecedent is reachable, so violated. penalty_reaches_unmarried: R4 (cohabit, present_as_married, never wed) in all three; the pair now keeps R4, hence its move. married_rated_individually: after `wed` and before any `cohabit` the pair are married and R5's new condition holds (not cohabiting), so `individual_rate` is true of a married pair: reachable at step 1 in the base and the pair, and in the composite through `wed` or coverture's `marry` (cohabits starts false and no coverture action sets it). over_limit_ineligible: `pay_benefit` is a default capacity removed by R7's disability exactly when resources are over the limit, the same Bool as `true and not over` under R1; `accumulate` keeps the antecedent reachable.

coverture-us-ssi, the ten coverture rows (dependent_cannot_exit reachable, subject_cannot_exit reachable, care_and_sanction_same_role holds_to_k, no_standing reachable, care_assigned_by_sex violated, financial_dependence holds_to_k, financial_dependence_unpropertied holds_to_k, cannot_contract violated, double_burden open, creditor_shield open): unchanged. The SSI edits touch conditions of effect-less `may` actions and one default-capacity flag on an effect-less action; no `must` is added or removed, so strict-compliance pruning and every coverture fluent's reachable set are as before; `divorce` (S7) is untouched.

Kibbutz (both entries): care_assigned_by_sex persists / fails, subject_cannot_exit reachable, care_and_sanction_same_role violated, unchanged; `sanctioner` is prose the checker does not read (validate needs only none iff or_else null; R2 and R3 keep `or_else: R6`).

Exploratory, reported, not stop conditions:
- `phil rules ablate --entry ssi-marriage-penalty --k 6,8`: no R1 row; R2 -> married_couple_rated holds_to_k > violated; R3 -> married_couple_limited holds_to_k > violated (still under "deregulated, not ranked"); R4 -> penalty_reaches_unmarried reachable > open; **R5 -> married_rated_individually reachable > open (new flip; R5 is the sole regulator of its action, so expected in the deregulated table)**; R6 none; R7 -> over_limit_ineligible holds_to_k > violated (pay_benefit stays enabled by the default capacity once the bar is gone).
- `phil rules ablate --entry coverture-us-ssi --k 6,8`: ssi R2 flips married_couple_rated only, R3 married_couple_limited only, R5 married_rated_individually only; no row flips `financial_dependence`.
- `phil rules iso` base against coverture-household, police-crisis, cps, lease at guard: iso False, `care+control: -`; denominators 6 where they were 7.

Claims afterwards: **C2b stays "refuted as written"** (its evidence, no SSI rule flips financial_dependence in the composite, is predicted to stand; the rule now reads married and living together, which touches no fluent financial_dependence reads). **C2c stays `untested`** (no shared fluent is added; P2c work). C2a unchanged (still vacuous on the 34 older properties). No claim was attached to the five-rule pair in docs/claims.md.

### Drift rule

Any result other than the above is recorded in Results against the row it contradicts and never edited into this section; an unpredicted verdict flip also gets a row in docs/surprises.md. Stop conditions: a changed, added or removed diff row other than the four in the table (then the baseline is NOT regenerated); gate FAIL; a different drop-one set; a build failure not caused by a typo of this batch.

**Nothing above "### Results" is edited after the first run.** Commit this section before any edit, build or run.

### Results (run 2026-11-09; installed engine 50ed97f, ENGINE_PIN e46f6ea, baseline engine_hash 58c4c54222de before and after; z3 5.3.3; preregistration commit ecca295)

Every verdict, diff, gate, drop-one and pytest prediction held; no stop condition met; the baseline was regenerated. Nothing above this heading was edited, except the file's Status line (line 3), which is kept current (wording corrected in the post-council fix pass; correctness finding 3).

**First run of `scripts/checks.sh`** (old baseline; CHECKS FAILED by design, the diff line is the only failing check):

- `build.py --check`: `ok: 33 institutions, 43 properties, JSON and 34 cards match src/`
- `rules diff`: `4 changed, 0 added, 0 removed (of 192 rows)` (`[FAIL] diff (exit 0)`)
- `rules check-all`: `agreement: 192/192 = 100%`
- `rules gate`: `b          PASS    coverture-household~police-crisis@guard+strands: partial(care+control); coverture-household~cps@guard+strands: partial(care+control); police-crisis~cps@guard+strands: partial(care+c...`; `e          PASS    agreement 192/192 = 100% (min 60%)`; `GATE PASS  (deferred criteria do not fail the gate)`
- `drop_one_match`: `b=PASS rows: 19`; `coverture-household R2,coverture-household R5,coverture-household R6,police-crisis R2,police-crisis R4,police-crisis R11,cps R3,cps R4,cps R10`
- `pytest`: `40 passed in 380.30s (0:06:20)`
- `CHECKS FAILED` (exit 1)

**Moved rows, predicted against actual** (`phil rules diff --baseline data/verdicts-baseline.json`, verbatim rows):

| # | institution | property | baseline | predicted | actual | hit |
|---|---|---|---|---|---|---|
| 1 | ssi-marriage-penalty | married_rated_individually | open | reachable | `changed  married_rated_individually [reachable]: open -> reachable` | yes |
| 2 | ssi-marriage-penalty-individual | married_couple_rated | violated | holds_to_k | `changed  married_couple_rated [invariant]: violated -> holds_to_k` | yes |
| 3 | ssi-marriage-penalty-individual | penalty_reaches_unmarried | open | reachable | `changed  penalty_reaches_unmarried [reachable]: open -> reachable` | yes |
| 4 | coverture-us-ssi | married_rated_individually | open | reachable | `changed  married_rated_individually [reachable]: open -> reachable` | yes |

4 of 4 predicted rows moved; 0 unpredicted rows moved, added or removed.

**Baseline.** Regenerated with `phil rules verdicts --k 6 --no-cache --out data/verdicts-baseline.json`: `wrote data/verdicts-baseline.json: 192 rows, engine_hash 58c4c54222de`. Old 192 rows, new 192 rows; compared by script: same key set, same engine_hash, params and z3, and exactly the four rows above differ.

**Second run of `scripts/checks.sh`** (new baseline):

- `build.py --check`: `ok: 33 institutions, 43 properties, JSON and 34 cards match src/`
- `rules diff`: `0 changed, 0 added, 0 removed (of 192 rows)`
- `rules check-all`: `agreement: 192/192 = 100%`
- `rules gate`: `b          PASS    coverture-household~police-crisis@guard+strands: partial(care+control); coverture-household~cps@guard+strands: partial(care+control); police-crisis~cps@guard+strands: partial(care+c...`; `e          PASS    agreement 192/192 = 100% (min 60%)`; `GATE PASS  (deferred criteria do not fail the gate)`
- `drop_one_match`: `b=PASS rows: 19`; `coverture-household R2,coverture-household R5,coverture-household R6,police-crisis R2,police-crisis R4,police-crisis R11,cps R3,cps R4,cps R10`
- `pytest`: `40 passed in 159.06s (0:02:39)`
- `ALL CHECKS OK` (exit 0)

**Per-property** (`phil rules check --inst X --k {6,8} --init declared --compliance strict --step-mode one --no-cache`): all 25 rows as preregistered at both k (base 5/5, pair 5/5, composite 15/15), flags column `-` on every row, so neither edited invariant is vacuous. The pair prints one warning (derived `couple_limit` names an action no rule regulates), as predicted. Emitted rule rows 287 -> 286, as predicted. Cards regenerated: the two SSI entries, coverture-us-ssi, the two kibbutz entries, cards/README.md.

**Exploratory, as predicted on every line.** `phil rules ablate --entry ssi-marriage-penalty --k 6,8`: no R1 row; R2 -> married_couple_rated holds_to_k>violated (load 1/1); R3 -> married_couple_limited holds_to_k>violated (deregulated table); R4 -> penalty_reaches_unmarried reachable>open (load 0/0); R5 -> married_rated_individually reachable>open (deregulated table; the new flip); R6 none; R7 -> over_limit_ineligible holds_to_k>violated. `R4~prohibit` still flips married_couple_rated as well (S5, unchanged artifact). `phil rules ablate --entry coverture-us-ssi --k 6,8`: the six ssi rows flip the same properties and nothing else; the string `financial_dependence:` occurs in no flips cell of the table. `phil rules iso --cond guard`, base against coverture-household 0/6|7, police-crisis 1/6|11 (R2->R3, as before), cps 0/6|10, lease 0/6|5; iso False in all four.

**Claims.** C2b stays refuted as written (no SSI rule flips `financial_dependence` in the composite after the revision). C2c stays untested (no shared fluent added). C2a unchanged. docs/claims.md not edited.

**Drift** (none in a verdict, diff row, gate, drop-one set or test count):

1. Brief against data, found before the run and written into the preregistration, so recorded here for the record rather than as a miss: the brief called `cohabits` a new free fluent; it was already declared and is not free (Scope (a)). No row became conditional on a free input.
2. Brief against data: the brief said to drop `sanctioner_review: derived` from kibbutz R2 and R3; both were already `reviewed`, nothing was dropped (Edit 8).
3. Deviation from the rulings as worded, decided in the preregistration (Scope (b)): the formulas of `married_couple_rated` and `married_couple_limited` were edited to read married and cohabits. No ruling names a property edit. Flagged for the author; N75.
4. Deviation from ruling 3 as worded, decided in the preregistration (Scope (c)): only R1 became a default capacity; "the pair's R5/R6" no longer exist as `when true` rows and stay conditioned rules. Flagged for the author; N74.
5. Edit not listed in the preregistration's Edits: data/institutions/README.md Conventions bullet gained `pay_benefit` in the default-capacity example list, and kibbutz-childrens-house `notes` gained one sentence on the retag. Prose only.
6. Card wording seen, not fixed (build.py is out of scope): the Default capacities line reads "A agency may pay benefit a claimant unless a rule forbids it".
7. The installed engine is one merge past ENGINE_PIN (50ed97f, PR #6, dataset-copy drop); the baseline's engine_hash did not change across the regeneration, so the verdict code is the pinned one. ENGINE_PIN not edited.

Surprises ledger: none (no unpredicted verdict). Negative results: N74 (declined: R5/R6 default-capacity conversion), N75 (weakened: ruling 1 needed a property edit for ruling 4's flip to exist), N76 (untested: the one-rule pair is not a coherent reform). The superseded five-rule pair had no claim attached in docs/claims.md, so it gets no `declined` row; it is recorded in the pair's `notes`.

### Council

Pending (coordinator). Correctness seat: the two edited invariant formulas (is the antecedent reachable, flags `-`; is the edit the right resolution or should the formulas have stayed and the base read violated); `pay_benefit` default capacity with `arg_roles [agency, claimant]` equals the dropped R1 in enabledness, alone and after aliasing in the composite; R5/R6 condition is the exact complement of R2 or R4. Faithfulness seat: R2/R3 "married and living together" against 20 CFR 416.1801(c) and 42 U.S.C. 1382(a)(1)(B)(i) (no excerpt was added; the phrases rest on the 2026-11-08 seat's raw read); whether a married pair living apart really gets the individual rate and limit (R5/R6 complement; the 416.1802(a) deeming case stays unencoded); whether a one-rule pair that leaves a married cohabiting pair with no limit power is acceptable; kibbutz R2/R3 `institution`. Card-only seat: does "power reading only" read on the three cards; the Default capacities line for `pay_benefit`; the pair card's name against its id; the previous pair recorded in notes.

Done 2026-11-09 (the paragraph above is the brief as it stood at commit 3bc056a, kept). Reviews: docs/reviews/2026-11-09-ssi-rev2-{correctness,faithfulness,card-only}.md.

- Correctness: 11 findings, **8 green / 3 amber / 0 red**. Process integrity green (the two property-formula edits are in the preregistration commit ecca295, before properties.yaml changed; not the S7 pattern); the four moved verdicts, the `pay_benefit` default capacity against the dropped R1, the R5 complement, the baseline (192 and 192 rows, exactly four differ) and `cohabits` non-vacuity all re-run and confirmed. Amber: the property edit needs the author (N75); the composite's shortest witness is a never-cohabited couple, not a separation; R6 is not the complement of R3. Does not pause.
- Faithfulness: 9 items, counted by the seat as **5 faithful / 1 understates / 2 overstates / 0 cannot tell** (understates: `pay_benefit` as a default capacity, disclosed by the label; overstates: R5's married-apart branch, pre-existing and disclosed, and the one-rule pair if read as a reform). Does not pause.
- Card-only: 15 rows, **8 says it / 1 overstates / 4 understates / 2 cannot tell**. The two cannot-tell rows (the pair card did not say a married cohabiting pair has no limit rule; the property formulas were not on the cards) fail legibility under SEATS.md and **paused the batch** until the fix pass below.

### Post-council fix pass (2026-11-09)

Scope: prose and card rendering only. No rule's attribute, deontic, aim, conditions or or_else, no property formula, no id, no `kind` or `sanctioner` value, no provenance level or excerpt was changed. Items that need the author's ruling are recorded under "Open for the author", not decided. Nothing above "### Council" was edited except the Status line and one Results sentence (fix C3).

Fixes applied (the review each answers):

A. Card-only seat.

1. build.py Default capacities line (rows 5, 13): the article is chosen from the role ("An agency", and "An animal" on the companion cards); the verb phrase comes from a new card-only action key `plain` (stripped before the JSON, like a rule's `plain`), set on `pay_benefit` as "pay a benefit to", so the line reads "An agency may pay a benefit to a claimant unless a rule forbids it"; an action without `plain` falls back to its name as before. On a composite the phrase and the role name are read from the member that declares the action and the aliased role is printed beside it: "a claimant (partner_a in this composite)", "A wife (partner_b in this composite)".
2. Legend and header (rows 6, 15): a card whose name carries "power reading only" (or a composite with such a member) gets a Legend line saying what the label means, including that `violated` then means "no such power exists"; on the composite the line is scoped to the rows of the SSI member and the header reads "...; power reading only (from member ssi-marriage-penalty)". The composite's `name` in the data is unchanged.
3. Pair card "Pairs" section (row 9): a dropped rule now prints as "R3 dropped (base wording, not in this entry): ...". This is the wording on every card with a dropped rule.
4. Pair card face (rows 8, 10, 11): a new card-only entry key `card_note` (stripped before the JSON, never inherited, as `goods_note`) prints a "Read first" paragraph under the title: the entry drops only the couple resource limit; a married pair living together then has no resource-limit rule at all; it is a deletion, not a reform; the id `ssi-marriage-penalty-individual` is historical; `violated` on married_couple_limited means no such power.
5. Properties (rows 11, 12): the "Expected properties" table of every card gains a `formal` column with the property's full formula beside its gloss (the whole formula, not only the antecedent; the change was small, so all 34 cards carry it). Gloss text only: `married_rated_individually` no longer says it "separates the pair" (it is reachable in both entries; married_couple_limited is what distinguishes them); `married_couple_rated` reads "marriage with a shared household brings the couple rate". No formula touched.

B. Faithfulness seat.

1. R2 `plain` (fix 1): the quoted "with whom he or she is living" is replaced by the words the repo records, attributed separately: "with whom he is living" (42 U.S.C. 1382(a)(1)(B)(i)) and "in the same household" (20 CFR 416.1801(c)). The older "he or she" in "Revision 2 (author decisions)" item 1 of this file stays as written (a dated record); it is not a quotation the repo holds.
2. Base `notes` item 3 (fix 2): says keeping R5 and R6 as conditioned rules is a departure from ruling 3 as worded (N74).
3. Pair `name` (fix 3): gains "a deletion, not a reform".
4. `married_couple_rated` gloss (fix 4): as in A5.
5. Base `notes` (fix 5): "every rule here is a power" corrected: R2 to R6 are powers, `pay_benefit` a default capacity, R7 a disability that removes one.

C. Correctness seat.

1. Finding 8: **R6 is NOT the exact complement of R3.** R6 carries R5's condition, the complement of the two couple-rate routes (R2, R4); the couple limit has one route only (R3: married and living together). An unmarried pair who live together and hold out therefore has neither the couple limit power nor the individual limit power; the seat's probe finds it reachable at k=6 (present_as_married, cohabit). Pre-existing (the old R3 and R6 had the same hole). Recorded in the base `notes` ("KNOWN GAP"), in R6 `source`, and as N77. Wording corrected where it is not frozen: R5 `source` now says "the exact complement of the two couple-rate routes (R2, R4)", which is true of the rate. Edit 2 of the preregistration above calls the R5/R6 condition "the exact complement of the two couple routes"; that sentence is frozen and is wrong for R6 as a statement about limits. Not encoded: whether R3 should read cohabits and (married or holds_out) is open item (v).
2. Finding 5: composite `notes` gains a sentence: coverture's `marry` leaves `cohabits` false, so the shortest witness of married_rated_individually is a couple who never cohabited, not a separation.
3. Finding 3: Results now says "except the file's Status line".
4. Finding 2 (N75) is the author's: open item (i).

Not done, with reason: renaming the pair id (it removes and adds baseline rows; next dataset PR, open item (iii)); a README sentence on `pay_benefit` as an encoder's grant (it would decide open item (iv)); the R3 widening (open item (v)).

Rebuild and light checks. The machine was busy, so the full `scripts/checks.sh` was NOT rerun after this pass (it ran twice before it, Results above); check-all, gate and drop-one are not re-verified here. Prediction, written before the run: institutions.json changes in `name`, `notes` and `source` strings only and properties.json in two glosses, so 0 of 192 rows move. Verbatim:

- `python data/institutions/build.py --check`: `ok: 33 institutions, 43 properties, JSON and 34 cards match src/`
- `phil rules diff --baseline data/verdicts-baseline.json`: `0 changed, 0 added, 0 removed (of 192 rows)`
- `python -m pytest -q`: `40 passed in 132.26s (0:02:12)`

Ledger: docs/negative-results.md N73 retyped `artifact` (resolved as a test defect, engine PR #8); N74 to N76 carry the seats' recommendations; N77 (`weakened`, the R6/R3 non-complement gap); N78 (`refused`, the card-only pause, fixed). Scoreboard: seats column filled on the SSI revision 2 row.

#### Open for the author

Recorded, not decided. Each with the seats' recommendation.

1. **(i) N75, the two property-formula edits** (`married_couple_rated`, `married_couple_limited` gained the cohabits conjunct). Declared in the preregistration before the run (correctness finding 1), but no ruling names a property edit, and each property now restates its rule's condition, so `holds_to_k` holds by construction. Ratify or reverse before any claim cites these two rows. Faithfulness seat: accept, the properties restate the rules. Correctness seat: the author's call; with the old formulas both are violated in the base and the pair differs on nothing.
2. **(ii) N74, ruling 3.** Only R1 became a default capacity; R5 and R6 stay conditioned rules. Faithfulness seat: yes, amend ruling 3 to "R1 only"; a default capacity cannot carry the condition, and couple disabilities would state a prohibition the text does not.
3. **(iii) N76, the one-rule pair is a deletion, not a reform.** Seats: keep it as a deletion pair, never cited as a bill; rename the `-individual` id in the next dataset PR (for example `ssi-marriage-penalty-no-couple-limit`); and consider a real two-rule reform pair (drop R3, widen R6 so married cohabitants get the individual limit), after opening a bill and with its own preregistration.
4. **(iv) Should `pay_benefit` be a default capacity at all?** Paying benefits is a power the statute confers, and the README reserves the flag for "a capacity a person of that kind holds by default" (it calls cps `petition` a conferred power, not a default capacity), so the definition is strained and the card line reads as a fact about agencies. Faithfulness seat: either one README sentence that here the flag marks an encoder's grant to an agency, or revert to a labelled R1 at the must-be revision. No verdict moves either way (correctness finding 6).
5. **(v) The R6/R3 non-complement gap (N77).** Encode it (R3 to read cohabits and (married or holds_out), or R6 narrowed to the complement of R3) or keep it declared. Correctness seat: it is a faithfulness ruling and a new preregistration; kept declared for now.

The prediction held: 0 of 192 rows moved. The three checks were run on the data, build.py and cards as committed; the edits to this file, docs/negative-results.md, docs/scoreboard.md and docs/plan.md were written while pytest ran and are read by no test or check.
