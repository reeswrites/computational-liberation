# Parked: formal + informal rule layer (handoff received 2026-11-06)

Status: slice 1 STARTED 2026-11-08 (see "Slice 1 preregistration" below); decisions below are the author's (2026-11-06/07). The faithfulness batch (plans/readability.md) is still owed and the composition verb exists in the engine (compose(), 47cd94b).

## Coordinator note (2026-11-07)

The handoff (verbatim below) asks for five things. Checked against the repo, three of them collide with decisions already made here. What follows is the version the author accepted after the discussion.

**What the repo already has.** The rule schema is ADICO (`attribute`, `deontic`, `aim`, `conditions`, `or_else`; engine `philengine/schemas_rules.py`, `Rule`). Deliverable 1 of the handoff is therefore two fields, not a schema. `implicit: true` marks "a norm nobody writes down" (glossary); a "sanctioned norm" is an implicit `must_not` with an `or_else` (kibbutz R2, footbinding R3). There is no `sanctioner`, no formal/norm/strategy tag, no function field. `load_freedom` / `load_goods` are measured by ablation, never declared.

**Collision 1: the Crawford–Ostrom subtraction cannot be used literally.** The handoff says "remove the Or else and you have a norm." Here, `or_else: null` on a `must_not` already means a disability (no power exists; `data/institutions/README.md` conventions, ADR 0013, revision 4). Using absence of a sanction to mean "norm" would silently relabel every disability. So the norm marker is an explicit tag, and `or_else` keeps its meaning.

**Collision 2: declared function fields repeat the strand-tag problem.** Strand tags are hand inputs the cluster match depends on; the third review weakened them and their redesign is parked. `implicit` flips no verdict (L6). A function field nobody tests would be the same kind of decoration. Resolution below.

**Collision 3: layer 2 is frozen.** The handoff's dynamics layer is an agent-based model. Layer 2 was frozen 2026-11-04 after an honest FAIL on gate (a) footbinding and (b) committed minority, and the author's stated reason was that it ate tokens replicating Mackie and Centola instead of advancing the goal. The new model differs in kind (expectations, peer sanctions) but is still an ABM with hand-set payoffs and no validation. Resolution: static first; the time question is parked with a stated goal in plans/dynamics-sticks.md.

### Decisions (author, 2026-11-07)

**D1. Marking informal rules.** Two new rule fields, both hand-typed by the encoder and reviewable from sources:
- `kind`: `formal | norm | strategy`. `formal` = written and enforced by a named body. `norm` = unwritten, sanctioned by people. `strategy` = unwritten, unsanctioned (a shared expectation with no deontic bite). `kind` replaces nothing: `implicit` stays, since a rule can be implicit and formal (a statute everyone forgets is there).
- `sanctioner`: `state | institution | peers | family | self | none`. Hand-typed rather than inferred from the `or_else` target's attribute, because `self` and `none` are real answers that inference cannot produce. Where an `or_else` exists its attribute should agree with `sanctioner`; `build.py --check` should fail on disagreement.
- Existing rules: `kind: formal`, `sanctioner` derived once from the `or_else` target (or `state` for sourced statutes, `none` for disabilities) and then reviewed by hand in the faithfulness batch. Byte-identical JSON is not expected; the verdict baseline must not move (`phil rules diff`).

**D2. Function as a preregistered prediction, not a label.** A rule may declare `function:` with a short name (`proves_commitment`, `sorts_who_belongs`, `settles_who_decides`) and a source. The field is a prediction: "if this rule does that job, deleting it flips these properties." The ablation result confirms or embarrasses it; drift is logged the way L21 drift is logged. A function whose prediction never fires is reported as unsupported, not kept as a description. ASSUMED until the first batch shows the predictions do work.

**D3. Static first.** Removing a formal gate from a composed entry yields one of three verdicts, read from the ablation of the composite:
- **absorbed**: the property still holds, carried by a remaining `norm` or `strategy` rule.
- **displaced → to whom**: the property holds for a narrower attribute set than before, or is now carried by a rule whose `sanctioner` differs; the engine names who lost it and who now gates it. This gives the who-pays displacement mode (ADR 0016, theory.md "Displacement") a mechanism and a check.
- **no backstop found**: nothing in the composite carries the property. This is NOT "sticks." Whether a norm grows back is a time question and is parked (plans/dynamics-sticks.md). The verdict name is chosen to refuse the overclaim.

**D4. Composition first; sequencing as an exposure path.** The marriage bundle needs rules from several institutions reading one `married` fluent (docs/connections.md section 3; plans/marriage-bundle.md coordinator note). The composition verb (roles unioned, fluents unified by name, rules concatenated with ids prefixed, ablation over the composite) is a prerequisite; its sketch belongs in plans/composition.md, which is still to write. Ordered removal over the composite gives an **exposure path**: after each step, who is exposed and which good is lost. The author wants order of removals to be judgeable; this is what a static layer can honestly offer. Two things it cannot:
- Endpoint path dependence. Removing a fixed set of rules yields the same final rule set in any order, so static verdicts at the endpoint are order-independent by construction. A different endpoint from a different order needs something that reacts. That is the stated goal of plans/dynamics-sticks.md.
- Crystallization. Optional, ASSUMED if used: a single explicit reaction rule ("an informal gate that absorbs a function at step k gains an `or_else` at step k+1"). It lets sequencing results say something about endpoints, but the reaction rule is then the whole claim and must be reported as such.

**D5. Rediscovery case for the static layer.** Loving v. Virginia and same-sex marriage are both lag-over-time cases; a static layer cannot reproduce a lag, so neither is a fair test of it. Both move to plans/dynamics-sticks.md as its validation pair. The static layer needs a case where a formal marital-status gate was removed and the record says whether an informal gate absorbed it, moved it, or let it vanish. See "Rediscovery case" below.

**D6. Queue position.** After the faithfulness batch. Informal rules will carry the weakest sources in the dataset (hospital practice, workplace custom), and 24/211 rules are already known-unfaithful. The card-only seat (ADR 0014 fifth seat) runs on every informal rule.

### Sanctioner and kind review (hand review by a fresh agent, 2026-11-08; author acted on it the same day)

Of the ten derived `sanctioner` values, five were right (coverture R3 → family, cps R5 → state after the hand fix, companion R3 → state, footbinding R3 → peers and its copy). Four were wrong and are fixed in this branch with `sanctioner_review: reviewed`: kibbutz R2 and R3 → **peers** (R6's source says the general assembly and public opinion discipline members; there is no body above the committee), lease R5 → **state** (CCP 1161 unlawful detainer is a court process the landlord only initiates), gestational-surrogacy R3 → **state** (parentage is registered by courts and vital records). Ectogenesis R3 (registry → institution) is left derived: the registry sanction is itself an encoder invention (ectogenesis.yaml line 212) and the real fix is a real sanction holder at the faithfulness batch. Sanctioner touches no verdict; `phil rules diff` confirmed.

`kind` was derived as norm iff `implicit: true`. The review found the tag drifts both ways. **Faithfulness-batch item, needs its own preregistration; not applied:**

| Direction | Rows | Reason |
|---|---|---|
| norm → formal | crisis-team R8 (WIC 5150(a), a statute); paternity-quota R9, transferable-leave R9 (reconstruction of the scheme); companion R6, R9, R11 (+copies; leash/impound law, property and standing doctrine); mwpa-* R10 (Blackstone creditor reach), R12 (Chused, trustee conveyance); footbinding R10 (explicit pledge commitment) | written law tagged implicit for another reason |
| norm → strategy | police-crisis R1 (dispatch routine); cps R6 ("mother called first"); paternity-quota R7, transferable-leave R7 (the pattern the quota was introduced to break); ectogenesis R5, surrogacy R5 ("care-norm ... no sanction"); crisis-team R7 | regularity nobody sanctions; Bicchieri requires a sanction for a norm |
| norm → drop (default capacity) | footbinding R2, kibbutz R8 | added for ADR 0015 A6; the README says default capacities are not written as implicit `may ... true` |
| formal → norm | kibbutz R1, R3, R4, R5 (Wikipedia practice source, no by-law); footbinding R1, R4, R6, R7 (Mackie convention, unwritten) | practices tagged as written |
| formal → strategy | naming-convention R1, R2 | Centola tipping convention with no sanction; the clearest strategy case |

Rules at `sanctioner: none` whose source implies a real sanction the encoding never gave an `or_else` (candidates for the same batch): companion-ownership R5 (Penal Code 597(b) misdemeanor; R4 prosecute power already exists to link), lease R2 (Civ. Code 1941 repair duty), ectogenesis/surrogacy R5 (Kleven motherhood penalty, peers), coverture R2 (necessaries enforced through creditors; inference, not text).

### Rediscovery case

Researched 2026-11-07 (standard web search, no page fetches; advocacy-sourced items marked). Three candidates; the first two are usable, the third is a near-vanish.

**R1. US hospital visitation, 2010–11 (best fit: clean before/after rule structure).**
- Before: no federal visitor-choice rule in the Medicare Conditions of Participation. Each hospital set policy, commonly "immediate family only," and staff decided who counted. `kind: norm` or institution policy, `sanctioner: institution`.
- Change: Presidential Memorandum 15 April 2010; CMS final rule 42 CFR 482.13(h) (critical access hospitals 485.635(f)), 75 FR 70831, published 2010-11-19, effective 2011-01-18; CMS Transmittal 75 (r75soma), 2011-12-02, giving surveyors the interpretive guidance (A-0215). The patient designates visitors "including, but not limited to, a spouse, a domestic partner (including a same-sex domestic partner), another family member, or a friend" ((h)(2)); (h)(4) requires "full and equal" visitation privileges; (h)(3) bars restriction on race, sex, sexual orientation and similar grounds. Clinical restriction remains. Corrected 2026-11-08 from plans/sourcing-worklist-marriage.md; the earlier "7 September 2011" memo date was unconfirmed and is dropped.
- After: the formal gate moved from marital status or kinship to patient designation. Denials continued in reported cases (Lambda Legal 2010 survey anecdotes; a 2012 Nevada domestic-partner denial). No systematic post-2011 compliance study found.
- Expected static verdict, to preregister before encoding: **displaced** (gate moved to designation, clinical exception retained), with the informal staff gate still present as a `norm` rule that the formal rule now overrides but does not delete. The record for "informal gate persisted" is anecdotal; the engine must not be read as confirming a rate.
- Sources: CMS 2011 press release (cms.gov/newsroom/press-releases/medicare-steps-enforcement-equal-visitation-and-representation-rights-hospitals); CMS transmittal r75soma (cms.gov/regulations-and-guidance/guidance/transmittals/downloads/r75soma.pdf); Lambda Legal, *When Health Care Isn't Caring* (2010); Center for American Progress overview. Second lookup 2026-11-07: **no systematic compliance study exists** (no GAO report, academic survey, Joint Commission or CMS survey-finding rate found). HRC's Healthcare Equality Index requires a documented equal-visitation policy (hrc.org/hei/equal-visitation) but is a self-selected sample and no pass rate surfaced. Consequence: the rediscovery pass criterion must be about rule structure, not a compliance rate the record does not contain.

**R2. Domestic-partner registries and employer benefits, 1984–1998 (best example of displacement to a new proof-of-commitment test).**
- Before: benefit to the legal spouse only.
- Change: Berkeley registry 1984 [unverified], San Francisco 1989 (after a 1982 veto), NYC 1998 [unverified]; employer DP benefits attached to a registry certificate or an affidavit.
- After: gate displaced to registered status or affidavit. San Francisco Admin Code ch. 62 (Proposition K, 6 November 1990; amended 2004) defines partners at § 62.2(a) as two adults "who live together, and who have agreed to be jointly responsible for basic living expenses," registered by a sworn Declaration filed with the County Clerk (§ 62.3(a)); no cohabitation-duration requirement appears in the fetched text, and the six-month wait after a prior partnership is unconfirmed (snippet only, may be in § 62.3 or 62.4 or the 2004 amendment). So the substitute test is **cohabitation plus shared expenses, sworn**, not a time threshold. Berkeley's attestations require shared residence; SFERS does not recognise partnerships formed only by notarisation. Six- or twelve-month cohabitation affidavits are common in employer forms (Kaiser sample affidavit is primary), but no 1990s employer policy with requirement text was found (Lotus 1991 is described as gay-only with no requirements; the 1993 law-review article "Non-Traditional Family Values" cites the Lotus policy and could not be fetched).
- Expected static verdict: **displaced** to a new formal test (`sanctioner: institution`), no informal absorption. This is the "proof of commitment moves" case the handoff asks about. Record gap: the claim that employers introduced the tests *in response to* unbundling is still unsourced.
- Sources: SF Admin Code § 62.2, § 62.3 (gocodebook.com mirror of the Admin Code); sf.gov/node/6320; berkeleyca.gov/city-services/domestic-partnership; SFERS DP FAQ; Kaiser DP affidavit; Newsweek on Lotus 1991 (newsweek.com/domesticated-bliss-196122).

**R3. Sweden individual taxation 1971 (near-vanish, not clean).** The married-couple tax gate vanished formally; residual couple-level transfer rules remain and the 2003 Cohabitation Act is a separate regime. Not documented as moving to an informal test. Useful as the **no backstop found** control if the residual transfers are encoded honestly. Sources: Springer 10.1007/BF00160329; NBER c11497; IFAU wp00-5. Pre-1971 cohabitant status unverified.

Recommendation (not decided): R1 as the blind rediscovery (preregister "displaced, informal gate retained"), R2 as the second encoding (preregister "displaced to new formal test"), R3 as the vanish control. Author picks.

## Slice 1 preregistration: hospital-visitation pair (2026-11-08, committed before the first run)

Status: slice 1 STARTED 2026-11-08 on branch `informal-rules-slice1` (the faithfulness batch is not done; the author scheduled this slice ahead of it, so every informal rule here is sourced at the level the worklist reached and the card-only seat runs on all of them). Encoded: `hospital-visitation-pre2011` (8 rules) and `hospital-visitation` (extends it: R3 narrowed, R9–R11 added). Properties added (kind `structure`, so ablation lists their flips and counts no load): `spouse_visit_guaranteed` (invariant, two grace steps), `spouse_visit_possible` (reachable), `unmarried_partner_visit_possible` (reachable), `designated_visit_guaranteed` (invariant, one grace step; the pair's `differs_on`). The properties read `visiting` on compliant traces, not a derived power, because the engine's `(enabled ...)` ignores a sanctioned `must_not` (only an or_else-null disability blocks enablement), so no power fluent could see the staff norm. Engine facts relied on, from rules_lower.py: a regulated action fires only at a step where some may/must condition on that instance holds; one action per step; a step where two different must-do instances fire has no compliant continuation and is excluded.

Encoding departures from the worklist vocabulary (section 4 there), all ASSUMED: `hospital` split into `staff` (decide, admit) and `hospital` (sanction); `kin` dropped (one visitor role; `married` exogenous in the standalone entries, set by `marry` in the composite); `deny_visitor` and `can_visit` dropped; a family-admission duty R8 added so the spouse's visit can be guaranteed and not merely possible; the 2011 override of the staff norm written as a narrowing of R3's condition by `(not (designated p x))`.

**Expected verdicts (k = 6 and 8, strict, step-mode one), never to be edited after the run:**

| property | pre2011 | post-2011 (hospital-visitation) |
|---|---|---|
| spouse_visit_guaranteed | holds_to_k | holds_to_k |
| spouse_visit_possible | reachable | reachable |
| unmarried_partner_visit_possible | reachable | reachable |
| designated_visit_guaranteed | not applicable (no `designated`) | holds_to_k |

**Function predictions (D2), per rule, on single-rule ablation (`phil rules ablate`), read as flips of the four structure properties:**

| rule | kind / sanctioner | function | predicted flips on deletion |
|---|---|---|---|
| pre R4 (must recognise spouse) | formal / institution | sorts_who_belongs | spouse_visit_guaranteed holds_to_k → violated; spouse_visit_possible stays reachable (R2 route) |
| pre R2 (staff may recognise anyone) | norm / none (sanction on R3) | sorts_who_belongs | unmarried_partner_visit_possible reachable → unreachable_open |
| pre R3 (must not admit non-family) | norm / institution | sorts_who_belongs | nothing on the four (R5 then lets the unmarried partner through without recognition, which the reachable property cannot distinguish); recorded as the sole-prohibition reading if so |
| pre R8 (must admit family) | formal / institution | (none declared) | spouse_visit_guaranteed → violated |
| pre R5 (may admit any visitor) | formal / none | (none) | nothing (R8 also permits) |
| pre R1, R6, R7 | formal / none | (none) | R1: everything that needs admission becomes unreachable or vacuous (admit is the only setter of `admitted`); R6: nothing (sanction rule, strict compliance); R7: nothing (restriction only removes traces) |
| post R4 | formal / institution | sorts_who_belongs | spouse_visit_guaranteed → violated (designation is a `may`, not forced); spouse_visit_possible stays reachable by two routes |
| post R9 (must admit designated) | formal / state | settles_who_decides | designated_visit_guaranteed → violated; nothing else |
| post R2 | norm / none | sorts_who_belongs | nothing (unmarried partner reachable through R10 + R9: displaced to designation) |
| post R3 (narrowed norm) | norm / institution | sorts_who_belongs | nothing |
| post R8 | formal / institution | (none) | spouse_visit_guaranteed → violated |
| post R10 (patient may designate) | formal / none | (none) | designated_visit_guaranteed holds vacuously (no designation ever) — a vacuous flag, not a flip; nothing else |
| post R5, R6, R7, R11, R1 | | | as the pre row for the same rule |

A function whose prediction misses is reported as unsupported (D2). Flips not in this table go in docs/surprises.md.

**Static verdict for R1 (D3), read from the post-2011 entry alone:** removing the formal spouse gate R4 is **displaced**: the guarantee is lost (`spouse_visit_guaranteed` violated), the good stays possible (`spouse_visit_possible` reachable) through the staff norm (R2, `sanctioner: institution` on its sanctioned half R3) and through designation (R10 → R9, `sanctioner: state`, the patient's own act). Who loses: the spouse loses the guarantee that attached to marital status; who now gates: staff discretion and the patient. The N1 wording "naming chosen family as the party that loses" is kept as written and judged against this reading after the run; the record for "informal gate persisted" is one anecdote (hv-nv-2012), and no rate is claimed. The composite reading (N1 proper) is preregistered in plans/composition.md ("First composite, preregistered").

### Slice 1, run 1 (2026-11-08, engine b5fd019, z3 5.3.3, k = 6 and 8, strict, step-mode one)

**Pair: every preregistered verdict matched** (`phil rules check`: pre2011 3/3, post 4/4, at k = 6; the ablation's base verdicts at k = 8 agree, no k disagreement on any row). Baseline diff: 0 changed, 0 removed over the 146 pre-slice rows, 21 added. Wall-clock: ablation of both entries 1 min 19 s (6.5 cores).

Function predictions against the ablation (deleted-rule rows; the `~prohibit` variant rows were not preregistered and are listed after):

| rule | predicted | got | ruling |
|---|---|---|---|
| pre R4 (sorts_who_belongs) | spouse_visit_guaranteed → violated; possible stays | as predicted | prediction fired |
| pre R2 (sorts_who_belongs) | unmarried_partner_visit_possible → open | as predicted | fired |
| pre R3 | nothing | nothing | as predicted (sole-prohibition reading) |
| pre R8 | spouse_visit_guaranteed → violated | as predicted | — |
| pre R5, R6, R7 | nothing | nothing | as predicted |
| pre R1 | "everything that needs admission unreachable or vacuous" | nothing: `deregulated` | **miss**: deleting the sole `may` on `admit` deregulates it (always enabled, plans/priority-slice1-results.md S1 reading), so admission still happens; the prediction forgot the deregulation semantics |
| post R4 | → violated; possible stays by two routes | as predicted | fired |
| post R9 (settles_who_decides) | designated_visit_guaranteed → violated only | as predicted | fired |
| post R2 | nothing (displaced to designation) | nothing | as predicted |
| post R3, R5, R6, R7, R11 | nothing | nothing | as predicted |
| post R8 | spouse_visit_guaranteed → violated | as predicted | — |
| post R10 | vacuous flag on designated_visit_guaranteed | nothing: `deregulated` | **miss**, same cause: deleting the sole `may` on `designate` lets the patient designate freely, the opposite of "never designates" |
| post R1 | as pre R1 | nothing: `deregulated` | miss, same cause |

Every `function:` prediction fired (R4 twice, R2 once where predicted and correctly silent where predicted silent, R9 once) and none was edited after the run; N3's condition is met on this pair, though N3 is stated for the marriage bundle and stays untested until that batch. Two misses, both the same known engine reading (deregulation of a sole `may`), recorded, not tuned. Not-preregistered `~prohibit` rows: prohibiting R1 (off-condition leak, `offcondition_free`), R2 or R5 makes both reachable properties open in pre2011; in the post entry prohibiting R2 makes only spouse_visit_possible open (the unmarried partner still reaches admission by designation), prohibiting R1 or R5 makes both open. Consistent with the readings above; nothing new.

**Static verdict for R1 (read on the post entry, as preregistered): displaced.** Deleting R4 loses the guarantee and keeps the good possible; the carriers are R2/R3 (norm, institution) and R10 → R9 (formal, state). The N1 phrase "naming chosen family as the party that loses" is not what the row says: the party that loses is the spouse (the guarantee rode on marital status); chosen family never had it. N1 proper is read on the composite, which run 1 could not deliver (next).

**Composite: 12/14, P1 FAILED on `check`, and the failure is an artifact (docs/surprises.md S5).** `cannot_contract` came back violated (expected holds_to_k) and `spouse_visit_possible` open (expected reachable); `spouse_visit_guaranteed` held vacuously (antecedent unreachable) and so did `care_and_sanction_same_role` at k = 8. Scratch probes on the composite (reachability of `married`, `admitted`, both, `is_subject partner_a`, `is_subject staff`): `married(partner_a, partner_b)` is never reachable, while `is_subject(partner_a)` and `is_subject(staff)` are. Cause, from rules_lower.py `_action_types`: coverture's actions declare no `arg_roles`, so their parameters are typed by the prefix heuristic over the *composite's* roles after aliasing; `h` no longer matches `husband` and now matches `hospital` (the one role starting with h), `w` matches nothing (all agents). So `marry` grounds as marry(hospital, anyone): it sets `is_subject` on anyone (hence `cannot_contract` violated: partner_a becomes a subject with no disability binding him) and never sets the typed `married(partner_a, partner_b)`. ADR 0018's freeze covered rule variables (`var_roles`) and not action parameters; plans/composition.md's cost note ("the freeze step should type the rest from the member's resolution") named the gap and nothing did it. Consequences in run 1: the hospital rows `hospital_visitation__R4`, `R8`, `R2` flip nothing in the composite (no marriage, so nothing to lose), the N1 row is unreadable, `chosen_mutual_care` and `mutual_household_care` read not_applicable (their subject, a married pair, never exists); the coverture rows match coverture-household-us's own ablation (R4 → no_standing open; R6 → dependent_cannot_exit, subject_cannot_exit open); `hospital_visitation__R9` → designated_visit_guaranteed violated (marriage-independent). **Q2 held exactly**: the composite's applicable set is 22 = coverture-household-us's 18 ∪ hospital-visitation's 4, and the six of the nine predicted applicable are applicable; backlash and no_standing_against_spouse are inapplicable on both for the fluent reason, creditor_shield forced in by expected_properties. Wall-clock: composite ablation 2 min 37 s (6.5 cores), check 2 s.

Fix, preregistered as P1b in plans/composition.md before the rerun: build.py freezes each member's action parameter types from the member's own roles (writes `arg_roles` the way the member's heuristic resolved them) before composition. The member entries are not edited.

### Slice 1, run 2 (2026-11-08, after P1b; engine b5fd019, k = 6 and 8)

**Composite: 14/14 at k = 6 and at k = 8, no vacuity flags; P1 PASSES after P1b** (`phil rules diff`: 0 changed, 0 removed over the 146 pre-slice rows; the baseline then regenerated with the 21 new rows; `build.py --check` ok; `check-all` passes, see the plan log). The scratch probes now read `married`, `admitted`, both, `counts_as_family` with `married`, and `visiting` with `married` reachable, and `is_subject(partner_a)` and `is_subject(staff)` open, as the typing intends. Every coverture row of the composite's ablation (flips and goods states, k = 6 and 8) is identical to coverture-household-us's own ablation run the same day: R2 → cared_for, known_carer, mutual_household_care, provided_for persists → fails; R3 → mutual_household_care; R4 → no_standing open; R6 → dependent_cannot_exit, subject_cannot_exit open and subject_cannot_exit_persists fails; R7 → cannot_contract violated; R1, R5 deregulated, no flips. No coverture rule moves a visitation property and no hospital rule moves a coverture property or goods state. Wall-clock: composite ablation 2 min 40 s.

**N1, read on the composite as preregistered (plans/composition.md "First composite, preregistered"): displaced.** Row `hospital_visitation__R4` (the formal spouse gate, `function: sorts_who_belongs`): spouse_visit_guaranteed holds_to_k → violated at both k; spouse_visit_possible stays reachable; nothing else moves. The good survives through the staff norm (`hospital_visitation__R2`, whose sanctioned half `R3` has `sanctioner: institution`) and the patient's designation (`R10` → `R9`, `sanctioner: state`): with R4 gone, `R2` deletion still flips nothing (designation carries it) and `R9` deletion still flips only designated_visit_guaranteed (the norm carries the spouse). Who loses: the spouse's guarantee, which rode on marital status; who now gates: staff discretion and the patient. N1 as worded said "naming chosen family as the party that loses"; the row names the spouse, and chosen family (the unmarried partner) never had the guarantee in any entry. N1's falsifiers did not fire (the property neither vanished nor held for the same attribute set), so N1 is **supported on the encoding** with its "to whom" clause corrected by the row, not by the author: the party named in the preregistration was wrong, the verdict was right. Record for the real world: one anecdote of a post-2011 denial (hv-nv-2012); no rate, and none is claimed. Other hospital rows in the composite as in the post entry alone: `R8` → spouse_visit_guaranteed violated; `R9` → designated_visit_guaranteed violated; `R2`, `R3`, `R5` no flips; `R1`, `R6`, `R7`, `R10`, `R11` deregulated, no flips; the `~prohibit` rows of `R1` and `R5` make both reachable properties open.

**Status after run 2.** R1 rediscovery (static): displaced, as preregistered, on the post entry and on the composite. P1: passed after one preregistered fix (P1b) for an artifact (S5). Q2: held exactly in run 1 and run 2. N4: the hospital entries add rows and change none (0 changed of 146). N3 condition met on this pair (every `function:` prediction fired unedited), formally still untested until the marriage bundle. Two deregulation misses in the function table (R1, R10) recorded.

### Preregistered claims (enter in docs/claims.md when this batch is scheduled, not before)

- N1. In the composed marriage bundle, removing the formal hospital-visitation gate (spouse may visit) leaves `partner_can_visit` carried by a `norm` rule gated on `counts_as_family`, with `sanctioner: institution` (staff discretion): verdict **displaced** to a narrower attribute set, naming chosen family as the party that loses. Falsified if the property vanishes (no backstop) or holds for the same attribute set (absorbed).
- N2. Removing goods one at a time in two different orders over the composite yields the same endpoint verdicts and different exposure paths. This is a check on the engine, not a theory claim; failure means composition or ablation is wrong.
- N3. At least one `function:` prediction in the marriage bundle fires on ablation without having been edited after the run. Falsified if every prediction misses or if any was edited to match.
- N4. The `kind` and `sanctioner` tags change no verdict on the existing 27 entries (`phil rules diff` clean after migration). If they do, the migration mis-derived a sanctioner.

### Citation corrections to the handoff (checked 2026-11-06)

- Crawford & Ostrom 1995, APSR 89(3): 582–600. Correct. The "drop Or-else = norm" mapping is the standard reading but is not usable here (collision 1).
- Institutional Grammar 2.0: Frantz & Siddiki, *Institutional Grammar: Foundations and Applications for Institutional Analysis*, Palgrave Macmillan 2022. Its parser (IG-Parser) is Go, not Python. Its constitutive-statement form ("X counts as Y in context C") is exactly what informal gates look like, but adopting it means a new Z3 encoding. Decision: encode "counts as" as a fluent plus a regulative rule; revisit if theory.md's open question "is any bundle purely constitutive" is scheduled.
- Watzlawick, Weakland & Fisch 1974, *Change*. Exists; the first/second-order gloss is fair; wording not checked against the text.
- Jackson 1965, "The Study of the Family," *Family Process* 4(1): 1–20. The "family rules" idea is more directly cited to Jackson 1965, "Family Rules: Marital Quid Pro Quo," *Archives of General Psychiatry* 12: 589–594. Neither full text was fetchable; whether "metarules" appears in either is unverified. A secondary source defines metarules as "the rules about the rules" and cites Jackson 1965a/b without pinning a paper. The term is more commonly credited to Watzlawick, Beavin & Jackson, *Pragmatics of Human Communication* (1967) [unverified]. Safe wording: "metarules (family-systems usage; Jackson 1965, Watzlawick et al. 1967)."
- Bicchieri 2006, *The Grammar of Society*. Definition as stated. Footbinding and FGM are Mackie 1996 (ASR 61(6): 999–1017), who frames them as conventions, not norms; Bicchieri's FGM treatment is *Norms in the Wild* (2017), not 2006.
- Loving v. Virginia 1967. Gallup approval of Black–White marriage: 4% (1958), 20% (1968), 64% (1997, first majority). The 30-year lag holds. Moved to plans/dynamics-sticks.md.
- "Identified patient": no single coiner; "a family-systems term from the 1950s–60s Palo Alto and Ackerman circles" is the safe wording.
- The handoff says 25 entries; the dataset has 27 (coverture-floor added 2026-11-06). README and claims L23/L24 are also stale on this count.

### Tasks (in order; none started)

- [ ] plans/composition.md: sketch the verb (docs/connections.md section 3), engine ADR, one CLI subcommand, ablation over composites.
- [ ] Engine: `kind` and `sanctioner` on `Rule`; `function` optional; `build.py --check` fails on `or_else` / `sanctioner` disagreement.
- [ ] Migration of the 27 entries: derive, then hand-review in the faithfulness batch; `phil rules diff` must be clean (N4).
- [ ] Consent/sexual-violence guard note before any marriage encoding runs (plans/marriage-bundle.md).
- [ ] Marriage bundle encoded flat first with formal + informal gates, each sourced; split into composable pieces once the verb exists.
- [ ] Preregister N1–N4 and the `function:` predictions; commit before the first run.
- [ ] Ordered ablation; exposure-path table.
- [ ] Rediscovery case encoded and run blind.
- [ ] Council after the batch, card-only seat on every informal rule.
- [ ] Short doc explaining the layer (docs/), claims rows entered.

## Handoff text, verbatim

# Handoff: formal + informal rule layer with a dynamics test for computational-liberation

## Goal
Add a layer to computational-liberation (github.com/reeswrites/computational-liberation, built on github.com/reeswrites/philosophy-engine) that can tell whether a rule change *sticks*, gets *absorbed*, or gets *displaced*. Right now the engine reasons about explicit formal rules and what they entail. Most real systems also run on informal rules — norms, expectations, roles — that push back when the formal rules change. This work makes those informal rules visible to the engine and testable.

Read the repo first: the theory, the plan, the claims register, the institutions dataset, and how philosophy-engine encodes rules. Fit the work to the existing structure. Don't impose a new one.

## Core ideas to put into the model
1. **One schema for every rule: ADICO** (Crawford & Ostrom 1995, "A Grammar of Institutions," *APSR* 89(3)).
   Attributes (who) · Deontic (may / must / must not) · aIm (action) · Conditions (when / where) · Or else (sanction).
   - Remove the Or else and you have a **norm**. Remove the Deontic as well and you have a **shared strategy**.
   - The sanctioner is a field of its own: the state, an institution, family or peers, or the self.
   - Also look at Institutional Grammar 2.0 (Frantz & Siddiki). Check whether its extensions are worth using.
2. **First-order vs second-order change** (Watzlawick, Weakland & Fisch 1974, *Change*). A first-order change is a move inside the rules, and the system absorbs it. A second-order change alters the rules, or the rules about changing rules (metarules; Don Jackson 1965, "The Study of the Family," *Family Process*).
3. **Norms as equilibria of expectations** (Bicchieri 2006, *The Grammar of Society*). A norm holds while people hold both *empirical* expectations (others do X) and *normative* expectations (others think I should do X). It breaks when those expectations shift.
4. **Function conservation and displacement.** This is the family-systems "identified patient" idea applied to rules. A rule often does a *job*, such as signaling trust, sorting who belongs, or settling who decides. Remove the rule and keep the job, and the job tends to move to some other rule, norm, or group. "Displacement" is already in the repo's falsifier list, and this gives it a mechanism.

## Proposed architecture
- **Rule layer:** encode formal and informal rules together in ADICO, each tagged formal / norm / strategy plus its sanctioner. Keep encodings human-readable.
- **Function audit:** every rule declares the function(s) it serves. Make this a first-class field with sources cited.
- **Entailment layer:** the existing engine. Leave it alone apart from teaching it to read the new schema.
- **Dynamics layer:** a small, readable agent-based model. Agents hold roles and Bicchieri-style expectations, and both formal and informal sanctions apply to them. Run it over time to see whether a change sticks, is absorbed, or is displaced.
- **Output per intervention:** one of {sticks, absorbed (first-order), displaced → where to}, plus the effect on the liberation score (freedom plus flourishing, kept separate).

## First slice: the marriage bundle
This case is already planned in the repo. Encode the formal gates (immigration sponsorship, medical proxy, and others already listed) **and** the informal gates that sit alongside them (who counts as family at the hospital, workplace recognition, and the like, each sourced). Simulate removing the formal gates one at a time. Questions to answer:
- Which removals are absorbed by informal gating?
- Where does the "proof of commitment" function go once marriage stops carrying it?
- Does the order of removals change the outcome? This is the sequencing question at the heart of the theory.

## Validation (rediscovery, using the repo's own falsifier)
Encode at least one historical case honestly and check whether the model reproduces it before trusting it on anything new. Candidates:
- **Loving v. Virginia (1967):** formal legalization arrived decades before majority public approval of interracial marriage. Formal change led and the norm lagged. Use real polling data.
- **Norm-led cases from Bicchieri's work** (e.g., footbinding, FGM abandonment): here the norm changed first, with or without formal rules.
Together these test the open question already on the repo's list, "do rules lead or trail?", in both directions.

## Constraints
- Every claim cites a source in the claims register. **Verify every citation in this brief** before relying on it.
- The code and the encodings should be easy for humans to read and review.
- Add the work to the repo's plan instead of setting a time budget, and run the review council after each batch.
- Go fast, but keep it right and legible.

## Deliverables
1. An ADICO schema plus a migration or adapter for the existing institutions dataset.
2. The function-audit field, filled in for the marriage bundle.
3. A minimal dynamics model and its run results for the marriage slice.
4. One rediscovery case, with a pass/fail write-up.
5. Additions to the claims register, plus a short doc explaining how the layer works and why it's built this way.
