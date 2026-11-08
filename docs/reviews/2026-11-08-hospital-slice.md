# Council review: informal-rules slice 1 (hospital-visitation pair, first composite), 2026-11-08

Three fresh seats (ADR 0014), each a separate Sonnet agent that did not build the slice, run after run 2 (branch `hospital-slice`, engine b5fd019). Reports are reproduced below as filed; the builder's response and the fix pass follow at the end. Under review: `hospital-visitation-pre2011`, `hospital-visitation`, `coverture-us-hospital-visitation`, the four structure properties, `build.py` composites support, plans/informal-rules.md "Slice 1 preregistration", "run 1", "run 2", plans/composition.md "First composite, preregistered", P1b, docs/interpreting-results.md section 8, docs/surprises.md S6 (filed as S5 at review time; renumbered after, since the SSI batch holds S5).

Verdict in one paragraph. The pair and the composite behave as preregistered (7/7, then 14/14 after the preregistered P1b fix), the R1 static verdict is **displaced**, and all three seats find the result honest as an encoding statement and weaker than the write-up first made it as a statement about 2011. The guarantee that "displaced" says is lost exists because the encoder wrote two pre-2011 hospital duties (R4 recognise the spouse, R8 admit family) that the sources show only as custom; the carrier labels mixed sanctioner tags that enter no verdict; one plan sentence reported a pair deletion that was inferred, not run; section 8's displaced criterion ("guarantee lost, possibility kept") operationalises D3 rather than restating it; and the only fluent the composite shares between its members is `married`, so N1 on the composite restates the post entry's verdict rather than testing it independently. The cards were legible on roles and provenance and short on URLs, the initial state, and the reconstructed status of four rules; those are fixed in the fix pass below. Claim statuses set from this review: N1 weakened, N4 supported, P1 supported (after P1b), Q2 supported.

## Seat 1: correctness

## Council, correctness seat: slice 1 (hospital-visitation pair + composite)

Read: ADR 0014, ADR 0018; plans/informal-rules.md D1-D3, slice 1 preregistration, run 1, run 2; plans/composition.md first composite, P1b, P1b result; the two hospital YAML sources, `_composites.yaml`, the four new properties; build.py (`load_composites`, `freeze_action_types`, `compose_entry`, `build_all`); docs/surprises.md; docs/interpreting-results.md section 8; rules_lower.py docstring; rules_compose.py. Note: the brief says surprises row S5; the row is S6 (S5 is the SSI batch), but plans/informal-rules.md run 1 still says "S5" (see item 6).

Ran (all read-only, no repo edits): `uv run python data/institutions/build.py --check` (ok: 30 institutions, 38 properties, JSON and 31 cards match src/); `phil rules check --inst <id> --k 8` on hospital-visitation-pre2011, hospital-visitation, coverture-us-hospital-visitation, coverture-household-us (all match expected; composite 14/14, no vacuous flags). Scratch variants (copies of institutions.json/properties.json under `/private/tmp/claude-501/-Users-rees-Documents/c034c583-7ac6-4485-a0a3-b5c925205e68/scratchpad/run2/corr/`, `mk.py` builds them, `inst_v.json` holds them): single and multi-rule deletions, `may` for `must`, R3 at full width, composite with `female` free, vacuity probe properties (`properties_probe.json`). I did not run ablate, check-all or pytest. Composite vacuity probes at k=8 were too slow and were killed; the composite evidence for non-vacuity is item 1c.

### 1. Is "displaced" a finding about the rules or about how the properties were written?

**1a. AMBER (leaning RED for the phrase "finding about the rule set").** The guaranteed-to-violated flip on deleting R4 follows from deontic arithmetic plus three ASSUMED encoding choices, not from anything the sources show.
- `spouse_visit_guaranteed` holds only because both links of the chain are `must`. Replace either with `may` and the property fails on the full, undeleted entry (scratch, k=8):
  - `v_R8may` (post, R8 as may): spouse_visit_guaranteed holds_to_k -> violated.
  - `v_R4may`: violated.
  - `v_R4R8may`: violated.
  - `p_R8may` and `p_R4R8may` (pre): violated.
  - So the preregistered `holds_to_k` exists only because the author wrote R8 as a duty. hospital-visitation.yaml notes say so: R8 is "Written as a duty (must), not a permission, so that the spouse's visit is guaranteed and not merely possible"; the pre-2011 source field for R8 admits the source (Presidential Memorandum, "no more restrictive than those that immediate family members enjoy") describes a baseline, not a hospital duty ("ASSUMED").
- Given that, deleting any link of a must-chain whose neighbours are `may` yields "guaranteed lost, possible kept". Deleting R8 does the same (post and pre rows, as the write-up lists). `possible` stays reachable because R2 is a universal `may` ("staff may treat any visitor as family", no condition on who) and R5 a universal `may`. With R2 universal, the spouse can never become unreachable by deleting R4; "no backstop found" is not a reachable outcome for this row in this encoding. Scratch confirms the other direction is not reachable by deletion either: `c_noR4R2R10` (composite, k=6) and `p_noR4R2` (pre, k=8) both keep spouse_visit_possible reachable, because deleting the sole rules on `recognize_family` / `designate` deregulates the action (always enabled), see item 4.
- So "displaced" here reads: "a duty was deleted and a permission remains." That is a true statement about the encoding, and the write-up's own words ("the spouse loses the guarantee that rode on marital status") are accurate at that level. What is not supported is presenting it as a finding that informal discretion absorbed a function: the engine cannot return the other two outcomes for this row.

**1b. AMBER. Section 8 / run 2 apply a wider "displaced" than D3 defines, and the "differs in sanctioner" evidence is mislabelled.**
- plans/informal-rules.md D3 defines displaced as: "holds for a narrower attribute set ... or is now carried by a rule whose sanctioner differs". docs/interpreting-results.md section 8 leads with a new criterion, "the guarantee is lost (invariant holds_to_k -> violated) while the good stays possible". That criterion is not in D3. The row does not show a narrower attribute set: the property is about spouses before and after, and unmarried_partner_visit_possible does not move (c_noR4: reachable).
- Run 2 says the good survives through "the staff norm (`R2`, whose sanctioned half `R3` has `sanctioner: institution`) and ... `R10` -> `R9`, `sanctioner: state`". Check against the tags: R2 is `sanctioner: none` (hospital-visitation.yaml); R10 is `none`; R3 is a must_not whose institution sanction attaches to a *prohibition that blocks*, it carries nothing. The spouse's R2 route ends in R8 (`institution`, the same sanctioner as R4), so only the designation route (R9, state) has a different sanctioner. Under `compliance=strict` (default, used throughout) or_else and sanctioner never enter a verdict at all (rules_lower.py docstring: "every must/must_not is a hard constraint"), so "who now gates" in sanctioner terms is label reading, not engine output.
- "With R4 gone, R2 deletion still flips nothing (designation carries it) and R9 deletion still flips only designated_visit_guaranteed" (run 2) was not run. Ablation deletes one rule from the full composite; there is no R4+R2 row. The claim is inferred. My scratch: `c_noR4` -> spouse_visit_possible reachable (k=6); `v_noR4R2` (post) -> reachable; `v_noR4R2R9` -> reachable (R10 then R5, no R9 needed); the two-rule deletions therefore support the inference, but only because of deregulation (item 4) and R5, not because designation "carries" the spouse in a clean sense.

**1c. GREEN. No vacuity, no hold for a different reason.**
- Non-vacuity probes (k=6 and 8 as noted), on pre and post, window = the property's antecedent with `counts_as_family` false at t0 (so a rule must do work):
  - `probe_work` (window with no recognition at t0): reachable on pre (k=8) and post (k=6).
  - `probe_work_visit` (same, and visiting at t): reachable on both.
  - `probe_work_novisit` (same, and NOT visiting at t): `open` on both.
  - `probe_win_novisit` (any window, not visiting at t): `open` on both.
  So in the full entries the guarantee is exercised and holds; it does not hold only because the antecedent is unreachable.
- Composite: `c_noR4` -> spouse_visit_guaranteed violated at k=6, so an unvisited window is reachable in the composite once R4 goes; the unmodified composite shows no `vacuous` flag at k=8.
- Other routes into `visiting`: R9 needs designation (`may`, R10), R5 is a `may`. Only R4 -> R8 forces. Staff can escape only through R7 (`restrict`, a permanent, unconditioned `may`) and that sits in the antecedent (`not clinically_restricted` at t0 and t1), not in the consequent. One-action-per-step stops staff restricting at t0 or t1 (R4 or R8 is forced then), so the escape cannot be used inside the window.

**1d. AMBER. Strict compliance plus one action per step create unreported dead ends.** With R4 and R9 both present, a married patient who designates the spouse before recognition reaches a step where two different must-do instances are due (R4 recognize, R9 admit_visitor). No compliant continuation exists, the trace is excluded, and no conflict is reported (the conflict check pairs only must/must_not on one aim). Probe `probe_deadlock` (post, k=6, --trace): reachable only at t=6, the final step, via `designate` then `admit` ... true at t=6 with no action left; at any earlier step the state is unreachable. Consequences: (i) the "two routes" for spouse_visit_possible after R4's deletion exist only because R4's removal removes the deadlock; in the full entry the designate-then-admit route for a spouse is dead. (ii) `reachable` verdicts can be witnessed by boundary states with no compliant future; the reported witnesses (traces above) are not of that kind, but the write-up's "reachable" should not be read as "continuable". Not a flip of any reported verdict.

### 2. The R3 narrowing `(not (designated p x))`

**2a. AMBER. Not "inconsistent" as the notes say, but the engine does flag a conflict, and the narrowing decides one preregistered row.**
- Scratch `v_R3full` (post with R3 conditions `(not (counts_as_family p x))`): the checker prints `v_R3full: deontic conflicts [('R9', 'R3')]`, but all four property verdicts are unchanged (holds_to_k / reachable / reachable / holds_to_k at k=8). So the claim "would make the entry inconsistent" is true in the sense of a flagged R9/R3 conflict and dead-end states (designated, unrecognised, unrestricted, admitted: R9 requires admit_visitor, R3 forbids it), not in the sense that any reported property fails.
- What the narrowing does change: `w_R3full_noR2` (post, R3 full width, R2 deleted): unmarried_partner_visit_possible -> reachable NO (unreachable). With the narrowing (`w_noR2`, the real post entry minus R2): reachable. So the prediction and result "post R2 deletion: nothing, displaced to designation" holds only because R3 was narrowed; at full width the designation route for a non-recognised partner is a dead end. The narrowing is the author's only way to write "override" under strict compliance (no priority mechanism; I found none in rules_lower.py), so it is a defensible encoding, but "R3 overridden, not deleted" is what the encoding asserts, not what the engine shows.
- R3 does no observable work in either entry: pre `q_noR3` and post `v_noR3` flip nothing (R5 admits everyone, and no property reads "admitted with no recognition"). The informal gate's verdict-bearing part is R2 alone. The "norm, institution" R3 is untested by any property.

### 3. P1b fix and `initial_free`: faithfulness to members

**3a. GREEN. `freeze_action_types` matches the engine's own typing.** It uses `var_role` (the same function `_action_types` uses) and keeps declared `arg_roles`. The composite's actions (printed from institutions.json) all carry explicit roles: coverture `marry [partner_a, partner_b]`, `maintain`, `neglect`, `keep_house` [partner_b, partner_a], `hold_property [partner_b]`, etc.; hospital actions as declared. No action parameter is left None.

**3b. GREEN with scope caveat. `initial_free` is correct for the two fluents it names and sex does not change coverture verdicts.**
- Composite with sex left free (`c_femalefree`: `initial: []`, `initial_free: [acquired_property, earns, female]`), k=8: the ten coverture verdicts and four visitation verdicts equal the preregistered ones; `care_assigned_by_sex` stays violated. Standalone `coverture-household-us` k=8 gives the same ten. So fixing `female(partner_b)` narrows traces without moving any `check` verdict.
- `married` goes from free-at-t0 (standalone hospital, empty mode) to false-at-t0 and set only by `marry` in the composite; typing comes from the hospital's `arg_roles` (compose takes the typed one). Coverture only ever used (husband, wife); the other tuples were never set. No effect.

**3c. AMBER. "Coverture rows identical to coverture-household-us's own ablation" is checked at verdict level only, and the composite adds nothing to the hospital rows.**
- All 16 coverture fluents have `arg_roles: None`, so in the composite they ground over 5 agents (partner_a, partner_b, staff, hospital, surveyor) instead of 2; `acquired_property`/`earns` are free for all five. The ablation of coverture rows was not re-run by me (instruction); the identical check verdicts above and the structure (coverture's must-be rules on `provides_care` are state obligations that take no action slot; hospital musts are action obligations on disjoint fluents) make a difference unlikely, but "identical rows, flips and goods states" rests on the builder's run.
- The only shared fluent is `married`. So the composite's hospital rows are the post entry's rows by construction: "no coverture rule moves a visitation property and no hospital rule moves a coverture property" cannot fail with this overlap. N1 "read on the composite" is therefore not independent evidence beyond the post entry, and the composite does not exercise anything coverture does to a wife (no standing, no exit) on the visiting wife. The write-up presents composite and post-entry agreement as if it were a test.

### 4. The two function-prediction misses (pre R1, post R10)

**4a. GREEN. Attribution to deregulation of a sole `may` is correct.**
- rules_lower.py docstring: "An action with no may/must rule is always enabled". `admit` is named only by R1, `designate` only by R10 (hospital-visitation.yaml), so deleting either frees the action.
- Independent confirmation: `p_noR4R2` (pre, k=8) keeps spouse_visit_possible reachable although no rule can recognise anyone; `recognize_family` lost its last rules and became free. Same mechanism.

**4b. AMBER. The same mechanism makes the "as predicted" rows for R6, R7, R11 uninformative.** `reprimand` (R6 only), `restrict` (R7 only) and `cite` (R11 only) are also sole-`may` actions. Deleting them deregulates, so "nothing flips" is the deregulated outcome, not evidence the rule did nothing. The preregistration's reason for R7 ("restriction only removes traces") is not what happens (restriction becomes available before admission). The write-up counts these as "as predicted" and records only R1 and R10 as misses. N3's "every function prediction fired" is also loose for R4: its predicted flip is the must-chain effect of item 1a, and R8 (no declared function) flips the identical property, so R4's `sorts_who_belongs` is not distinguished from R8. The substantive confirmations are R2 (pre: unmarried -> unreachable, `q_noR2` reproduced; this works because R4 keeps `recognize_family` regulated) and R9.

### 5. Other things that weaken "as preregistered"

- **k-boundedness.** `holds_to_k` at k=6/8 on traces of at most k steps; the guarantee window needs t0 >= 1, and composite witnesses need marry/admit/recognise/admit_visitor in sequence (visiting at step 4, k=6 leaves little slack). Both k's agree; fine, but `unreachable_open` rows (unmarried at full width, double_burden, creditor_shield) are open, not absent. AMBER, caveat is in section 8 but not in run 2's verdict.
- **`~prohibit` rows** were not preregistered; the write-up says so and draws nothing. GREEN.
- **Deregulated rows.** Run 2 lists R1, R6, R7, R10, R11 as "deregulated, no flips" for the composite: accurate, but six of the twelve "nothing" predictions are of this kind (item 4b). AMBER.
- **`declared` init.** The composite alone runs `declared`; the pair runs `empty`. Equivalent for the hospital fluents (only `married` differs, 3b), but the composite is a different trace set from the standalone entry, so "composite verdicts = entry verdicts" is two checks, not one. Minor.
- **Pre R1 prediction text.** The preregistration says deleting R1 makes admission "unreachable or vacuous"; that contradicts the engine semantics the same document relies on two sentences earlier. Recorded as a miss; fine.

### 6. Consistency notes found on the way (not correctness)

- plans/informal-rules.md run 1 cites "docs/surprises.md S5" for the arg_roles artifact; docs/surprises.md has it as S6 (line 13) and says S5 is the SSI batch. composition.md uses S6.
- docs/decisions/0018 and `_composites.yaml` notes say the composite's `initial` fixes sex only; fine, but D3's definition and section 8's definition of displaced differ (item 1b).

### What should change

1. In plans/informal-rules.md "Slice 1, run 2" and docs/interpreting-results.md section 8, state that the displaced reading follows from R4 and R8 being `must` and R2 and R5 universal `may`; cite scratch `v_R8may`/`v_R4may` (violated on the full entry). Say that "no backstop found" is not reachable for the spouse row in this encoding. Add one sentence: R8 as a duty is ASSUMED and fixes the preregistered `holds_to_k`.
2. Fix section 8's displaced definition to match D3, or amend D3 explicitly to add "guarantee lost, possibility kept" as a displaced criterion, with the amendment dated and the slice 1 verdict re-labelled as read under it.
3. Correct the "who now gates" sentence: the spouse's R2 route ends in R8 (sanctioner institution, same as R4); R2 and R10 are `sanctioner: none`; only R10 -> R9 differs (state); and under strict compliance sanctioner labels do not enter verdicts. Drop "R3 institution" as a carrier.
4. Either run `phil rules ablate` on the composite with R4+R2 and R4+R9 pair deletions (or a single scratch variant, as above) and report them, or mark the "with R4 gone, R2 deletion still flips nothing" sentences as inferred. Note that pair rows through R2/R4/R10 pass only via deregulation.
5. Record that the post R2 prediction ("displaced to designation") depends on the R3 narrowing: at full width the engine reports `deontic conflicts [('R9', 'R3')]` and R2's deletion makes the unmarried partner unreachable (`w_R3full_noR2`). Add a property that reads "admitted with no recognition and no designation" so R3 has an observable function, or say R3 is untested.
6. In the function-prediction table, mark R6, R7, R11 "nothing, deregulated" with the same status as R1 and R10 (uninformative, not confirmed). Restate N3 as satisfied by R2 and R9 (and not R4, which R8 duplicates).
7. Say in the composite write-up that the only shared fluent with hospital is `married`, so hospital rows on the composite equal the post entry's by construction, and N1-on-composite is a restatement of the post-entry verdict. Keep the "coverture rows identical" claim, but label it as the builder's ablation, not a re-derivation (my check-level re-run agrees at k=8, including with `female` free).
8. Note the one-action-per-step dead end (R4 and R9 both due at one step) as an engine limit in section 8 or ADR 0018: it excludes designate-before-recognise traces silently and lets `reachable` be witnessed at step k with no compliant continuation. Consider a `step_mode many` run of the pair as a robustness row.
9. Fix the S5/S6 reference in plans/informal-rules.md run 1.


## Seat 2: encoding faithfulness

## Encoding-faithfulness seat: hospital-visitation pair (hospital-visitation-pre2011, hospital-visitation) and composite

Reviewer did not encode. Read-only; no repo file edited.

### What I read
ADR 0014, ADR 0017; plans/sourcing-worklist-marriage.md (corrections, sections 1-4, gaps); plans/informal-rules.md D1-D2, R1, and the N1 passages; data/institutions/README.md Conventions; both YAML entries in full; the `coverture-us-hospital-visitation` block of `_composites.yaml`; the six `hv-*` rows of data/sources/rules.yaml; the four new properties; `phil rules check --inst hospital-visitation --trace` (4/4 match; traces read).

### What I opened (all by me, 2026-11-08)
| Source | Result |
|---|---|
| CMS Transmittal 75 (r75soma.pdf) | OPENED, raw text via pdftotext (not a summary). Transmittal 75, 2011-12-02, effective and implemented 2011-12-02. A-0215 intro (burden-of-proof sentence at hospital text, "when a hospital adopts policies that limit or restrict..."), A-0216 ((h)(1)-(2) text plus guidelines), A-0217 ((h)(3)-(4) text plus guidelines). Appendix W 485.635(f) = C-1000/1001/1002, and the transmittal says "new 42 CFR 485.635(f)". |
| 42 CFR 482.13 (Cornell, current text) | OPENED, WebFetch summary (verbatim paragraph (h) returned). |
| 75 FR 70831 (govinfo) | OPENED first 100,000 of 103,789 chars, WebFetch. The amendatory regulatory text (after char 100,000) was NOT reached; the preamble quotes (h)(1) and (f)(1). |
| Presidential Memorandum 2010-04-15 | OPENED, WebFetch summary. |
| NBC/AP Nevada 2012 | OPENED, WebFetch summary. |
| Lambda Legal 2010, HRC HEI | NOT opened (not tried; worklist says hosts fail; neither is cited at a level above unverified). |

### Verdict table

| Rule | Verdict | Reason |
|---|---|---|
| pre R1 admit | cannot tell (declared device) | Honestly `unverified`, no source. Encoder device. Fine as declared. |
| pre R2 staff may recognise any visitor as family | over-reads; kind questionable | The sources say some institutions deny access and that family is the benchmark. Neither says staff (charge nurse) decide who counts. That is stated as ASSUMED in `source`, but the plain line asserts it flatly ("the charge nurse decides who counts"). `kind: norm, sanctioner: none` fails D1 (see finding 5). |
| pre R3 staff must not admit non-family, else reprimand | over-reads | Evidence is regulators' descriptions of denial. No source shows a must-not on staff or an employer sanction (declared ASSUMED, no disciplinary text). `sanctioner: institution` is an inference from the existence of a policy. |
| pre R4 staff must recognise spouse as family | over-reads | Sole source is the memo's "no more restrictive than those that immediate family members enjoy". That sentence is the memo's target standard for designated visitors, not a description of pre-2011 hospital policy (finding 2). `kind: formal` (= written, named body, per D1) with no policy text opened. |
| pre R5 staff may admit any visitor unless clinically restricted | cannot tell / anachronistic provenance | Engine device ("a regulated action fires only where some may/must holds"). Provenance cites a 2011 text for a pre-2011 rule and says in its note that it does not support the pre-2011 permission. `kind: formal` unsupported. |
| pre R6 hospital may reprimand | cannot tell (declared) | Honestly `unverified`. Encoder's sanction holder. |
| pre R7 staff may restrict on clinical grounds | faithful as to the exception; over-reads staff power | Exception is in the 2011 text (intro). Pre-2011 existence is asserted without a source. Declared: free `restrict` over-reads staff power. Burden-of-proof sentence correctly attributed to A-0215 but is a hospital-policy-adoption burden, not a staff burden. |
| pre R8 staff must admit family | over-reads (the largest) | A duty on staff, `kind: formal`, `sanctioner: institution`, resting on the same memo sentence. Declared ASSUMED, but it carries the `spouse_visit_guaranteed` result (finding 3). |
| post R3 (replaced) | over-reads | Narrowing by `not designated` is declared and defensible as a strict-compliance device. But the Nevada anecdote does not evidence a persisting staff norm (finding 4), and CMS's A-0217 guidance says the hospital may not differentiate among visitors without a clinical or reasonable basis, which is wider than "designated only" (finding 6). |
| post R9 must admit designated visitor, else state cites | over-reads on the cited paragraph; supported on the effect | (h)(2) as codified is "Inform each patient ... of the right ... to receive the visitors whom he or she designates". It is a duty to inform, not an admit duty. The admit duty comes from (h)(4) (full and equal, consistent with patient preferences) plus A-0216/A-0217 guidance ("hospitals must accept a patient's designation"; "not permissible for the hospital ... to differentiate among visitors"). The entry quotes (h)(2) without its "Inform" head and cites (h)(2) for the duty. |
| post R10 patient may designate any person | faithful in effect; mis-pinned | Right and its recognition are in A-0216 ("hospitals must accept a patient's designation, orally or in writing"). The cited (h)(1)-(2) text is the hospital's duty to inform. The excerpt joins an (h)(2) fragment to a CAH 485.635(f)(1) fragment with "...", labelled in the note. Right to withdraw consent, support person and incapacitated-patient route are not encoded. |
| post R11 surveyor may cite | faithful as a power; sanction mislocated | The source for the consequence is the FR preamble (noncompliance "could result in the provider's termination from the Medicare program"; CMS has no other sanction authority), a CMS (federal) act, not a state survey agency "citing". `cite` has no effects and is unconditional (conditions `true`), so in the traces the surveyor cites at t=0 with nothing wrong. |
| composite aliases | cannot tell / hypothetical | Husband as patient, wife as visitor is a stipulated pairing; no source joins coverture to 2011 hospital rules. Declared as a composite, not a historical claim. |
| composite `initial: female(partner_b)` | faithful to ADR 0018 | n/a to this source set. |

### Findings

#### RED
1. **R9 cites the wrong paragraph for the duty it encodes.** (h)(2) is "Inform each patient ... of the right ... to receive the visitors whom he or she designates ... and his or her right to withdraw or deny such consent at any time" (Cornell; identical in A-0216 of r75soma). It creates no admit duty; its `excerpt` in provenance starts mid-sentence at "to receive the visitors ..." and drops "Inform each patient". The admit-on-designation duty is (h)(4) read with the A-0216/A-0217 guidelines, which are in r75soma and could be quoted verbatim (I did read them). Evidence for the effect exists; the citation as written does not support the plain line "(42 CFR 482.13(h)(2), (h)(4))" for a staff must. Fix wording and pin; do not drop the rule.
2. **The memo sentence is used as pre-2011 baseline evidence for R2, R3, R4, R8, and it is not that.** The memo says "designated visitors ... should enjoy visitation privileges that are no more restrictive than those that immediate family members enjoy": a proposed standard for designees. The FR preamble reports that CMS replaced this proposed language with "full and equal" because it "may have been difficult to define, measure, and enforce". The entries (`source`, `source_text`, notes) say the memo "describes the baseline it set out to change". The memo's actual practice statements (widow with no children denied a friend; religious order members unable to choose a non-relative; gay and lesbian Americans "often barred" from partners' bedsides) are better evidence for R3-style exclusion, are not in the worklist or any excerpt, and show nothing about a hospital policy admitting immediate family as a duty. The memo also cites North Carolina's law giving designated visitors family-equivalent privileges, so "no state-sanctioned visitor-choice rule" (worklist section 4) is true only federally; the entry title says "US hospital visitation before 2011". This is the principal over-read in the base entry. R4 and R8 (formal gate, family duty) rest on it alone.
3. **The spouse guarantee is built into R4+R8, both ASSUMED, and the pair's headline result rests on them.** `spouse_visit_guaranteed: holds_to_k` pre and post, and the N1 flip when R4 is ablated, exist only because the encoder added a must-recognise (R4) and a must-admit-family (R8). The notes declare R8 and R4-as-action-obligation ASSUMED ("added so that the guarantee is a duty rather than a permission"). Declared, but the card, claims and N1 text present "the guarantee that rode on marital status" as a finding about 2010 hospitals. No source shows a spouse had a guaranteed (as opposed to customary) right to visit pre-2011. The sources would equally support spouse_visit as a permission with discretion; under that encoding the guarantee never exists and there is nothing to displace.

#### AMBER
4. **Nevada 2012 is not evidence for the R3 norm.** Opened: the hospital's admissions officer said "hospital policy required power of attorney for all gay couples"; the registered domestic-partnership document was refused. That is (a) a stated hospital policy targeted by sexual orientation, so a formal-policy or discriminatory-practice datum, not an unwritten staff norm sanctioned by peers/employer; (b) a likely violation of (h)(3) and (h)(4) by the hospital, which the strict-compliance engine cannot represent; (c) silent on whether the patient had designated the partner (the narrowed R3 applies only to non-designated visitors, so a designated-visitor denial is outside the narrowed rule). The worklist note has it right ("admissions staff cited a policy"); the YAML note repeats "the hospital's stated ground was its admissions policy" but the rule, `source_text` and R1 nonetheless use it as evidence the norm persisted. One anecdote, one hospital, one state (US-NV; jurisdiction tag correct). Say "persistence of discriminatory denial after 2011 is anecdotally attested" and stop; do not tie it to R3's kind or sanctioner.
5. **`kind` per D1.** D1: `norm` = unwritten, sanctioned by people; `strategy` = unwritten, unsanctioned (Bicchieri: no sanction, not a norm).
   - **R2** is `norm` with `sanctioner: none`; the source line says the sanction is R3's. A `may` cannot itself be sanctioned. By D1 it is not a norm; it is the permissive half of R3's norm. Mark `strategy` (regularity of discretion, no sanction) or fold R2 into the description of R3 and say so. As it stands, the pair's central informal gate has `kind: norm` and `sanctioner: none` on one half, which is the conflict D1 and the 2026-11-08 review table (norm -> strategy rows) exist to prevent.
   - **R3** `norm` / `institution`: acceptable only because the sanction is encoded as employer reprimand (R6), ASSUMED. If the hospital's policy text was what excluded non-family (as Nevada's "hospital policy" suggests), R3 is `formal` (written, named body), not `norm`. Evidence cannot tell; say so.
   - **R4, R8** `formal` means written and enforced by a named body; no policy text was opened (worklist gap). They should be `norm`/institution with the "reconstructed policy" caveat, or `kind: formal` should carry an explicit note "written-ness ASSUMED".
   - **R5** `formal` for an unsourced engine device; per README, default capacities are not written as `implicit` may true. This is exactly the class of row flagged in the 2026-11-08 sanctioner review for dropping.
6. **R3 narrowed understates what the 2011 rule forbids.** A-0217 (read raw): hospital policies "must ensure that all visitors ... enjoy full and equal visitation privileges, consistent with the preferences the patient has expressed"; "it is not permissible for the hospital, on its own, to differentiate among visitors without any clinically necessary or reasonable basis." That bars staff differentiation among visitors generally, not only when the patient has designated. Narrowing R3 by `not designated` is declared as the one way strict compliance expresses "overridden, not deleted"; it is not what the guidance says the rule does. The note in `source` ("a norm kept at full width would contradict R9 and leave no compliant trace") is correct as engine mechanics, but the plain line should say the narrowing is an encoding concession.
7. **R5/R7 cite post-2011 text for pre-2011 rules, and the quoted phrase is not in the worklist.** "clinically necessary or reasonable restriction" appears nowhere in the worklist excerpts (it says only "Clinical restrictions: allowed by the intro"). I confirmed it in the intro of 482.13(h) (Cornell) and in A-0216/A-0217 (raw). Level `opened` is therefore reached, but by me, not by the worklist; provenance and rules.yaml state "levels are those the worklist reached". Also the intro does not grant a permission: it requires hospitals to have written policies "setting forth any clinically necessary or reasonable restriction". `plain` for R7 ("Staff may restrict...") and the post-2011 reading of the intro as a standing exception is fair, but staff (not hospital policy) restricting is the encoder's step.
8. **R9 enforcement item mislabelled `snippet`.** The worklist records r75soma as opened (PDF text). A `snippet` in ADR 0017 means a search-engine summary. Claiming a lower level than reached is safe but inconsistent; either reopen and cite an opened excerpt, or use `opened` with a pin. Also the sanction itself (termination from Medicare, FR preamble) is not in r75soma at the hospital-visitation pages I read; cite hv-fr-2010-final-rule for it. `sanctioner: state` is acceptable in D1's broad sense (government, not a private institution), but the actor is CMS (termination), reached through state surveyors; R11's role "state survey agency may cite" names the investigator, not the sanction holder.
9. **Omitted from the model but material to "designate".** (h)(2): consent and the right to withdraw it; "support person" and incapacitated patients. A-0216: with no advance directive, the hospital "is expected to accept" an individual's assertion that he or she is the support person, without documentation. For the group the rule most protects (unable to speak), `designate` as a patient act (R10 conditions `true`, set only by the patient) does not apply. Not declared in notes (only (h)(3) and termination are listed as unencoded).
10. **Excerpts not in the worklist.** R2 FR excerpt "the current practice in some medical institutions ... denies patients access to their loved ones" is in the worklist (hv-pre2011-practice), but I found it in the FR as "...in some medical institutions that denies patients access to their loved ones in times of need", in the response to the advance-directives comment. The preamble pin "(Background)" is wrong: it is Section II, a comment response about advance directives, not a description of visitation policy. R10 quote "in advance of furnishing patient care whenever possible" is in the worklist note and in r75soma (C-1000/1001 text, 485.635(f)(1)); fine.

#### GREEN
11. 42 CFR 482.13(h) reading: (h)(2) designation, (h)(4) "full and equal", intro clinical restriction, (h)(3) omitted, all as quoted; (h)(3) omission is declared and correct to disclose (list incl. sexual orientation). The relationship-agnostic effect is from (h)(2) plus (h)(4) as the worklist says (and A-0217 supports (h)(4) doing this work).
12. CAH citation: 485.635(f) is correct (r75soma: "new 42 CFR 485.635(f)", C-1000 to C-1002). The worklist correction (485.635 not 485.535) is carried into the entries. Effective date 2011-01-18 confirmed in the FR; Transmittal 75 date and effective/implementation 2011-12-02 confirmed raw. The old "7 September 2011" is correctly absent.
13. r75soma excerpt (burden of proof) is verbatim in A-0215 (hospital) and in the CAH equivalent; pin A-0215 correct. Declared not encoded.
14. Declared departures are in the notes: staff/hospital split, `kin` dropped, `deny_visitor` and `can_visit` dropped with the engine reason, `married` exogenous, R8 ASSUMED, R3 narrowing ASSUMED, `cite` without effects, (h)(3) and termination not encoded. Justifications are sound as engine mechanics; the problems are source over-reads (findings 1-4), not concealment.
15. Levels claimed vs worklist: no `opened` item exceeds what the worklist records (hv-ll `unverified` kept as lead; hv-nv-2012 `opened` summary-mediated as worklist). Only the two exceptions above (finding 7 phrase, finding 8 downgrade). Worklist's own caveat (WebFetch summaries, re-confirm raw) is not repeated on each row; the rules.yaml header says "summary-mediated". Acceptable; note r75soma I read raw, the others via summary.
16. Trace back-translation: spouse trace (admit; recognize_family; admit_visitor) reads as the encoding says. Traces contain filler `cite(surveyor, hospital)` at t=0,1 with nothing wrong and `reprimand(hospital, staff)` with no breach; this reads oddly on the card ("the surveyor cites a hospital with no deficiency") because sanction powers have `true` conditions. Not a faithfulness error; a readability one.

### Is the pair a fair minimal pair of the 2011 change?
Only partly. The diff is not one gate: post adds `designate` (R10), R9, R11, the `surveyor` role, `cite`, and narrows R3. `differs_on: designated_visit_guaranteed` is a property that is "not applicable" to the base (no `designated` fluent), so the pair cannot show a changed verdict between the entries; the informative content is the ablation inside the post entry. The pair keeps R4 and R8 (the spouse gate) in both, which matches the sources (the 2011 rule added designation; nothing in them says hospitals stopped treating spouses as family). So the pair is a fair minimal pair of "add patient designation backed by a state sanction", conditional on the base's R4/R8/R2/R3 being the right description of the old regime, which findings 1-3 say the sources do not establish.

### Does N1's "displaced" rest on anything the sources do not support?
Yes, three things.
- It is read from deleting R4 in the post entry, a counterfactual, not from the 2011 change, which kept R4. The sources show an addition, not a removal or relocation of the spouse gate. "Displaced" describes the ablation, not history.
- The "guarantee" that is lost (finding 3) exists because the encoder wrote spouse admission as a duty (R4+R8, ASSUMED, memo-only support).
- The backstops named, "staff norm R2/R3 (institution)" and "designation R10/R9 (state)", rest respectively on a norm with no direct evidence and a sanctioner none (R2), and on a paragraph whose duty is to inform (finding 1). The Nevada anecdote does not bear on either carrier (finding 4). N1's own wording ("naming chosen family as the party that loses") was already noted in informal-rules.md as not what the row says (the spouse loses). The composite's null result ("no coverture property moves") reflects composing two institutions with no shared fluent beyond `married`; it is not evidence from any source.
A defensible statement: "In this encoding, removing the formal spouse gate loses the spouse's guarantee and leaves visits possible through staff discretion and designation; the encoding's gate, duties and norm are assumptions the cited sources describe only indirectly."

### What should change
1. `hospital-visitation.yaml`, R9, `plain` and `source` and provenance pin: say the duty is (h)(4) "full and equal ... consistent with patient preferences" read with A-0216 ("hospitals must accept a patient's designation") and A-0217 ("not permissible for the hospital, on its own, to differentiate among visitors without any clinically necessary or reasonable basis"); cite (h)(2) only for the designation right and note it is phrased as a duty to inform. Replace the FR excerpt with the full "Inform each patient ... of the right ... to receive the visitors whom he or she designates ..." sentence, or quote the A-0217 sentence from r75soma (opened raw).
2. R9 provenance item 3: set r75soma to `opened`, pin A-0216/A-0217, and add the A-0217 excerpt; add hv-fr-2010-final-rule pin "Section II, enforcement" with the termination sentence as the source for the sanction; in R11 `source`, say the sanction is termination by CMS, with state surveyors as investigators.
3. `hospital-visitation-pre2011.yaml`, R2, R3, R4, R8 `source`: replace "the Presidential Memorandum describes the baseline" with "the memorandum states as its target that designated visitors enjoy privileges no more restrictive than immediate family; CMS dropped that wording for 'full and equal' (75 FR 70831); the memo's own practice descriptions are [quote from memo]." Add the memo's practice sentences to provenance with the same `opened` level (I opened them). Mention NC's designation law (cited in the memo) in `notes` and narrow the entry's claim to "no federal rule".
4. R2: `kind: strategy` (sanctioner none), or merge into R3 and re-run `phil rules diff`; if the author keeps `norm`, change `source` to state that D1's sanction requirement is knowingly not met. R4 and R8: `kind: norm`, `sanctioner: institution`, or keep `formal` with `source` stating "written-ness ASSUMED; no policy text opened". R5: consider dropping or marking as the default-capacity device per README and ADR 0015 A6 line.
5. `plain` of R2/R3/R8 pre: prefix with "(reconstruction, no policy text found)" like the existing "(practice, not written)", so the card shows the strength of the evidence on the line.
6. Post R3 `source` and `source_text`, and `hv-nv-2012` use: replace "That the norm persisted is anecdotal" with "A 2012 Las Vegas denial of a registered domestic partner is reported; the hospital's admissions officer cited hospital policy requiring power of attorney for gay couples (a stated hospital policy, probably contrary to (h)(3)/(h)(4)); it says nothing about the unwritten staff norm or its sanction." Add the A-0217 sentence as a note that the 2011 rule bars non-clinical differentiation among visitors generally, so the narrowing by `designated` is an encoding concession.
7. Post notes, "not encoded" list: add consent and withdrawal of consent, support person, incapacitated patients ((h)(2); A-0216), and the (h)(4) breadth.
8. R5/R7 (pre) provenance: drop the 2011 `effective_date` pairing or state "post-2011 text; pre-2011 existence ASSUMED"; add the intro's "must have written policies ... setting forth any clinically necessary or reasonable restriction" and note I confirmed it (Cornell and r75soma A-0216/A-0217).
9. rules.yaml header and `hv-fr-2010-final-rule` note: correct the pin for the "current practice" sentence to Section II (response to an advance-directive comment) and give the full sentence; note that amendatory text beyond char 100,000 was not read by this seat.
10. plans/composition.md N1 and plans/informal-rules.md R1 "Static verdict": add the sentence in "Does N1's displaced rest on..." above (counterfactual deletion, ASSUMED duty, carriers' evidence); keep "naming chosen family" correction.


## Seat 3: card-only

## Card-only seat report (ADR 0014, fifth seat)

### Header

Cards read (only these): `hospital-visitation-pre2011.md`, `hospital-visitation.md`, `coverture-us-hospital-visitation.md` (all under /Users/rees/Documents/cl-hospital/docs/cards/). No yaml/json/py/plans/other docs opened.

Sources. The two hospital cards print NO URLs anywhere (only bibliography ids such as `hv-presmemo-2010`, `hv-fr-2010-final-rule`, `hv-cms-r75soma`, `hv-nv-2012`). I could not resolve those ids without opening files this seat may not open. So **no hospital source was checked by me**; every hospital "faithful to source" judgment below is judged against what the card itself says its sources say. One probe: eCFR 482.13 (a public URL I supplied, not the card's) redirected to a bot-block page (unblock.federalregister.gov); not followed.

Composite card URLs:

| URL | Result |
|---|---|
| avalon.law.yale.edu/18th_century/blackstone_bk2ch29.asp (R1) | Opened. Both quoted clauses present. The text limits "immediate and absolute property" to chattels personal in possession (ready money, jewels, household goods); choses in action and chattels real work differently. |
| avalon.law.yale.edu/18th_century/blackstone_bk1ch15.asp (R2, R4, R5, R7 quotes) | Opened. All quoted passages present (necessaries; no action without husband's concurrence; not sued without husband as defendant; moderate correction; restrain of liberty for gross misbehaviour; deeds void or at least voidable). |
| wams.nyhistory.org/.../coverture/ (shown in the table source cell for R2, R4, R7) | Could not open: HTTP 403. |
| nber.org/.../w10175.pdf (R6) | Fetched but returned as unreadable binary; could not read the wording. R6 unchecked. |

---

### Card 1: hospital-visitation-pre2011

| Rule | (a) plain says what formal cells say? | (b) faithful to cited source at the shown level? | Verdict | Reason |
|---|---|---|---|---|
| R1 staff may admit (not admitted) | yes | level "unverified", honest | faithful (as labelled) | Encoder's device, says so. |
| R2 staff may (implicit) recognize_family | mostly. Plain says "any visitor"; formal is "any x not already counted" | level "unverified". Quotes are regulators' descriptions that do not mention staff discretion; card says ASSUMED | cannot tell | Honest level, but the sources cannot confirm the content. |
| R3 staff must not (implicit) admit_visitor if not family; else R6 | yes | level "opened" but the opened quotes (a floor "no more restrictive than family enjoy"; "denies patients access to their loved ones") do not state a ban on non-family or any discipline. Card's own source cell calls this ASSUMED | unfaithful (level overstated) | A floor for family does not imply a bar on others. Row should read inferred or unverified, not opened. |
| R4 staff must recognize spouse as family; else R6 | yes. The parenthetical "(hospital policy admits immediate family)" is not in any formal cell | level "opened"; card admits "No pre-2011 hospital policy text ... opened"; rests on a press description | unfaithful (level overstated) | The duty and its sanction have no source text. |
| R5 staff may admit any visitor when not clinically restricted | yes, but "clinically" narrows the quoted "clinically necessary or reasonable" | level "opened"; the opened quote is the 2011 rule; card says "UNVERIFIED for the pre-2011 permission itself" | unfaithful (level overstated) | This is the pre-2011 card, and the cited quote post-dates it. |
| R6 hospital may reprimand | yes | "unverified", honest | faithful (as labelled) | |
| R7 staff may restrict (admitted p) | no. Plain adds "on clinical grounds"; formal has no such condition; card says "Clinical grounds are not modelled" | opened quotes are 2011 rule and 2011 CMS text; pre-2011 "same clinical judgment existed" unsourced | unfaithful | Plain over-reads the formal cell; source is post-2011. |
| R8 staff must admit counted-as-family visitor; else R6 | mostly. Plain "visitor is not already admitted" collides with `(admitted p)` (patient admitted); formal is `(not (visiting x p))` | level "opened"; card says presupposed, ASSUMED, no policy text | unfaithful (level overstated) | Inference from a baseline description, shown as opened. |

**Card verdict: unfaithful at the shown levels.** Plain-to-formal agreement is good (R7 and R8 wording aside). The failure is the `level` column. R3, R4, R5, R8 read "opened", while the card's own blockquote says "no pre-2011 hospital policy text was opened". The prose is honest and the table contradicts it. For R3 and R8 the explanation is that the weakest-item rule counts only the items listed, and the listed items are opened regulator descriptions, so "opened" means "the description was opened", not "the rule was verified".

---

### Card 2: hospital-visitation (after 2011)

| Rule | (a) plain = formal? | (b) faithful to source at shown level? | Verdict | Reason |
|---|---|---|---|---|
| R1, R2, R6 | as card 1 | as card 1 | faithful / cannot tell / faithful (as labelled) | Same rows. |
| R3 (replaced) | yes. "overridden where designated" matches `(not (designated p x))` | level "opened": Nevada 2012 anecdote ("It didn't matter that we were registered domestic partners") shows denial happened, not that a staff must-not norm or reprimand exists. Card says anecdotal | cannot tell | Quote supports persistence of denial only. I cannot open hv-nv-2012. |
| R4 | yes | still sourced as "formal gate before 2011" | unfaithful (level overstated) | In a post-2011 card, nothing shows R4 persisted after 2011. Blockquote says kept, no evidence. |
| R5 | yes | "clinically" vs quoted "clinically necessary or reasonable restriction"; quote is the 2011 rule, which is fine here | faithful with caveat | Plain drops "or reasonable". |
| R7 | "on clinical grounds" not in formal cells (as card 1) | 2011 rule and Transmittal quotes are on point | faithful at gist; plain over-reads formal | Same wording issue. |
| R8 | as card 1 | sourced "Hospital policy before 2011", ASSUMED; not mentioned in the blockquote's list of kept rules | unfaithful (level overstated) | Same as card 1, plus unexplained survival after 2011. |
| R9 (added) staff must admit designated visitor; else R11 | yes | (h)(2) "right ... to receive the visitors whom he or she designates", (h)(4) "full and equal visitation privileges"; level "snippet", honest | faithful (caveat: could not open) | The CFR binds the hospital; row's who is staff, sanction lands on the hospital; plain says so. Plain omits "subject to consent". |
| R10 (added) patient may designate | yes | right to designate, (h)(1)-(2); CAH "in advance" supports `when true` | faithful (could not open) | |
| R11 (added) surveyor may cite hospital | yes | level "opened", but the one quoted line is the burden-of-proof sentence, which does not state a citing power. The card's prose says deficiencies are cited | cannot tell | Excerpt does not match the claim it supports. |

**Card verdict: unfaithful at the shown levels (inherited rows R3, R4, R8); new rows R9, R10 faithful, R11 cannot tell.** The Pairs section is good (one line per change). Defect: "differing in rule ?" prints a literal question mark.

---

### Card 3: coverture-us-hospital-visitation (composite)

Hospital rows: same verdicts as card 2 (the card says they are the member's rows unchanged). Coverture rows:

| Rule | (a) plain = formal? | (b) faithful to source at shown level? | Verdict | Reason |
|---|---|---|---|---|
| coverture R1 husband may control wife's property when married | yes | Avalon II.29 opened by me. Quote supports chattels personal in possession only; plain says "his wife's property" | faithful at gist, plain broader than source | Should say "her movable goods". |
| coverture R2 husband must provide care | yes, but "providing care ... must hold" is clumsy; source says "necessaries" | Avalon I.15 confirms the quote | faithful | "care" widens "necessaries". |
| coverture R3 wife must provide care (implicit), else husband may chastise (R5) | yes | level "unverified", honest | faithful (as labelled) | The plain's "(R5)" is ambiguous (see finding 5). |
| coverture R4 wife cannot sue in own name | formal says no sue power at all; plain says "in her own name" | Avalon: she can bring an action "in his name, as well as her own" with his concurrence | faithful at gist, overstated | Should say "without her husband's concurrence and joinder". |
| coverture R5 husband may chastise (restrain) when misbehaves | yes. Plain says "gross" misbehaviour; formal `(misbehaves w)` | Avalon confirms both quotes | faithful | |
| coverture R6 wife cannot leave the marriage at will | formal `(leave w)` has no "marriage"; plain adds it | I could not read the NBER PDF. By the card's own source cell: consent-or-fault requirement is stated for both spouses; paper lists nine pre-existing unilateral-divorce states; fault divorce was an exit | unfaithful | Plain is absolute, wife-specific, and "at her own will", while the cited sources are gender-neutral, partly contrary (nine states), and the card says fault exit is "not represented". Gloss should say so. |
| coverture R7 wife cannot contract in own name | yes; "no power exists" is stronger than "void, or at least voidable" | Avalon confirms the deeds quote. The second quote (compacts made when single) is about pre-marriage compacts, not her capacity | faithful at gist, overstated | "voidable" is not "no power". |

**Card verdict: unfaithful** (coverture R6, plus the inherited hospital levels).

#### Composite legibility questions

- **Which roles were renamed?** Yes, from the Members list (husband to partner_a, wife to partner_b; patient to partner_a, partner to partner_b). But the Roles section describes partner_a only as "the husband" and partner_b only as "the feme covert", and drops the patient/visitor descriptions. The hospital plain lines still say "patient", "visitor", "spouse".
- **Initial state?** Partly. `female(partner_b)` and "fluents not listed start false" are stated. That means `married` starts false, yet every coverture rule and the spouse rules need `married`, and no rule on the card sets it. I guessed that a `marry` action exists (the pre-2011 card calls married "exogenous and free"; the composite says only `acquired_property` and `earns` are free). Not answerable from the card.
- **Which member each rule came from?** Yes, via the `coverture_household_us__` / `hospital_visitation__` prefixes.

---

### Findings (places the card made me guess)

1. Level column vs prose contradict on the pre-2011 rows (R3, R4, R5, R8). The prose says no policy text was opened; the table says "opened".
2. The `level` is the weakest item, but for R2 the weakest item (Lambda Legal, unverified) is not what supports the rule, and for R3/R4/R8 the "opened" items support only the baseline description, not the rule.
3. R7 and R5 plain lines say "clinical grounds"; the quoted standard is "clinically necessary or reasonable restriction", and the formal R7 has no ground condition.
4. R8 and R4 are sourced "before 2011" inside the post-2011 card; I cannot tell whether the card claims they still hold.
5. Bare rule numbers in plain lines are ambiguous in the composite: coverture R3 says "(R5)" (chastise) while hospital R5 is a different rule; hospital rows say "(R6)" without the prefix.
6. Composite table source cells for coverture R2, R4, R7 print the wams URL, but the quoted text came from Avalon (and the card's R1 note says wams "did not support" a property claim). R1 and R5 cells show Avalon. R1/R5 cells end in a stray colon.
7. Tag "(sanctioner derived, unreviewed)" is not in the Legend.
8. Composite title says "US", but every coverture quote is Blackstone (England), shown only in the provenance bullets.
9. `married` initial value and the `marry` action are absent from the card (see above).
10. Hospital cards print no URLs, so a card-only reader cannot reach any hospital source at all.
11. "differing in rule ?" in the Pairs section of card 2.
12. Plain R8: "not already admitted" vs patient `admitted`.
13. Strand tags (tying/superadditive/rival) have a legend definition but no per-row rationale; I could not judge them.
14. Blockquote on card 1 and encoder notes cite `plans/...` files a card-only reader cannot open.

### What should change

- Pre-2011 R3/R4/R8: set level to "inferred" (or "unverified") and keep "opened" for the baseline quotes only; or add a level for "description opened, rule inferred".
- R5/R7 plain: "Staff may admit any visitor unless visiting is restricted (the model treats all restriction as clinical; the rule says clinically necessary or reasonable)." R7: "Staff may restrict visiting (grounds not modelled)."
- R8 plain: "...and that visitor is not already visiting."
- R4/R8 on card 2: add "(still assumed to apply after 2011; no post-2011 source)".
- R11 source: quote a line stating the survey agency's citing role, or lower the level.
- Composite coverture R1: "may control her movable goods (chattels)"; R4: "cannot sue without her husband's concurrence (he joins)"; R7: "her deeds are void or voidable"; R6: say "no unilateral exit; divorce by consent or proved fault (not wife-specific in the sources)" or lower to unverified/unfaithful-flagged.
- Composite: prefix rule references in plain lines ("hospital R6", "coverture R5"); add "partner_a = husband = patient, partner_b = wife = visitor" to Roles; state in Initial that `married` starts false and name the rule/action that sets it, or mark it free; define "(sanctioner derived, unreviewed)" in the Legend; put the Avalon URL (not wams) in the R2/R4/R7 table cells; say "England (Blackstone) used as the proxy" near the title.
- Print the bibliography URL next to each source id on every card; fix "rule ?".


## Builder's response and fix pass (same day, commits 954b48b and after)

Done, no verdict changed (check 3/3, 4/4, 14/14; `phil rules diff` 0 changed of 167; gate PASS):
- Sources re-pinned on the pre-2011 entry: the memo's "no more restrictive than immediate family" sentence is now cited as its target standard, and the memo's own practice sentences (widow denied a friend; religious orders unable to choose a non-relative; gay and lesbian Americans barred from partners' bedsides, opened 2026-11-08) carry the exclusion evidence; the FR "denies patients access to their loved ones in times of need" sentence is pinned to Part II (comment response). R3, R4, R5, R7, R8 carry an `unverified` item for the hospital rule itself, so their card level reads unverified; plain lines of R2, R3, R4, R8 say "(reconstruction, no policy text found)"; R4 and R8 `source` say the duty is ASSUMED and is what makes spouse_visit_guaranteed hold. North Carolina's designation law is noted; the entry claims no federal rule.
- Post entry: R9's duty pinned to (h)(4) read with Transmittal 75 A-0217 (opened from the PDF: "it is not permissible for the hospital, on its own, to differentiate among visitors without any clinically necessary or reasonable basis"), (h)(2) kept for the designation right and described as a duty to inform; R11 states the sanction is CMS termination ("noncompliance with this provision could result in the provider's termination from the Medicare program", FR Part II, opened) collapsed into the surveyor role; the Nevada 2012 report is described as a stated hospital policy, silent on designation, not evidence of an unwritten norm; A-0217's breadth noted against the designation narrowing of R3; consent, support person and incapacitated patients listed as not encoded; `minimal_pair_of.rule: R9`; notes say the pair is not one-rule.
- Cards: provenance lines show URLs; a Legend line defines "sanctioner derived, unreviewed"; the composite card shows a role map, the actions with their typed parameters and effects (so a reader can see `marry` sets `married`), and rule references inside plain lines carry the member prefix.
- plans/informal-rules.md: N1's reading states the losing party (the spouse) and what in the encoding makes it so; the "with R4 gone, R2 deletion still flips nothing" sentences are marked inferred, not run; the carrier labels corrected (R2 and R10 are `sanctioner: none`, the spouse's discretion route ends in R8 with the same sanctioner as R4; sanctioner enters no verdict under strict compliance; R3 is not a carrier); R6, R7, R11 rows marked deregulated and uninformative like R1 and R10; N3 restated as met by R2 and R9 only (R8 duplicates R4's flip); "no backstop found" noted as unreachable for the spouse row in this encoding, because deleting a sole `may` deregulates the action; the post R2 prediction's dependence on the R3 narrowing recorded, with R3 untested by any property; the composite's hospital rows noted as equal to the post entry's by construction (the only shared fluent is `married`), and the "coverture rows identical" claim labelled as the builder's ablation, confirmed by the seat at check level only.
- docs/interpreting-results.md section 8: the displaced criterion is labelled the encoder's operationalisation of D3 (ASSUMED, dated), the sanctioner column corrected, and the one-action-per-step dead end recorded as an engine limit.

Open for the author (not done here):
- D1 amendment or ruling: whether "guarantee lost, possibility kept" is a displaced criterion (section 8 reads it so; D3 says narrower attribute set or a different sanctioner); whether R2, a `may` tagged `norm` with `sanctioner: none`, should read `strategy`; whether R4 and R8 stay `formal` with written-ness ASSUMED or become `norm`.
- A property that reads "admitted with no recognition and no designation", so R3 has an observable function; or R3 stays recorded as untested.
- A `step_mode many` robustness row for the pair (one action per step silently excludes designate-before-recognise traces).
- Engine: `freeze_bindings` should write action `arg_roles` (P1b lives in build.py only); pair-deletion rows in `ablate` (or `--path`) so carrier claims can be run rather than inferred.
- Pre-existing coverture findings the card seat raised on the composite (R6 absolute and wife-specific against gender-neutral sources; wams URL in the table cell where the quote came from Avalon; "US" entry on English quotes) belong to the coverture faithfulness list in plans/sourcing.md, not to this slice.
