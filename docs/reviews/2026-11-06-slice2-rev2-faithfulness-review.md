# Encoding-faithfulness review: slice 2 revision 2 (2026-11-06)

Fresh agent, encoding-faithfulness seat (ADR 0014; plans/priority-slice2.md R2.6 step 8). I was not the builder, coordinator, preregistration author or an encoder. Read-only apart from this file. Second encoder: agent, not someone living under the institution (ADR 0012). This review is also by an agent of the same model family as both encoders and the builder.

**Read:**
- plans/priority-slice2.md: "Author decisions after the council" and "Revision 2" R2.1 to R2.6.
- plans/priority-slice2-results.md: "Revision 2".
- The revision-1 faithfulness review, which is the main input; each of its findings is checked in section 3.
- data/institutions/goods-encoding/: merge-log.md "Revision 2", r2/encoder-1.yaml, r2/encoder-2.yaml, r2/prompt-template.md, r2/bundle-manifest.sha256.
- properties.yaml: `subject` on the five goods, and `chosen_mutual_care`.
- coverture-household.yaml (rules R2, R3, R5, R6 and the vocabulary) and coverture-floor.yaml (R20, name, `source_text`, notes).
- ectogenesis R4 and cps R2.
- The `goods_note` of the eight entries, and the generated cards in docs/cards/ for those eight.
- docs/glossary.md, docs/theory.md, docs/intent.md (the terms these results lean on).
- philosophy-engine `rules_ablate.goods_state` / `goods_transition` / `measure_value` and `rules_checks.goods_queries` (ENGINE_PIN 7a67c21).

**Checked:**
- **Bundle hashes.** `sha256sum -c r2/bundle-manifest.sha256` against the scratch bundle2: 10 of 10 OK, including both substituted prompts.
- **Prompt.** The scratch `bundle2/prompt.md` is identical to `r2/prompt-template.md`. The two substituted prompts differ only in the encoder number and the output path that carries it.
- **Transcripts** (session subagent logs). Each encoder's first message equals its substituted prompt, apart from one trailing newline. Each made 12 tool calls:
  - 9 reads: 8 bundle files and one Glob of the bundle;
  - 1 Bash: a loop calling only `bundle2/validate.sh`, on `formal` and `subject` in the four entries;
  - 1 Write to its own `goods.yaml`;
  - 1 handback.

  The two ran in parallel (same start timestamp). This matches the merge log.
- **Merge.** Encoder 1 writes `forall x. not can_sanction`; encoder 2 writes `not exists x. can_sanction`. These are equivalent by inspection. The subjects are character-identical.
- **Run output.** Per-row goods states were read from the builder's saved revision-2 run (`scratchpad/slice2/run2/ablate-27-r2.json`, k=6). The chosen-care, R3, R5 and R6 rows of coverture-household, mwpa-earnings and coverture-floor, ectogenesis R1~prohibit and R4~prohibit, and cps R2~prohibit all match the results file.
- **One probe of my own (scratch only, nothing committed).** I built two scratch variants of coverture-household: R6 removed; and R5 and R6 removed, with R3's `or_else` cleared because R5 no longer exists. I ran `phil rules ablate --k 6` on them through `--institutions` (scratch `fr2/inst.json`, `fr2/inst2.json`). Results are in findings 1 and 2.

## 1. Back-translation of `chosen_mutual_care` and its subject

Formula (primary): `forall h w. married(h,w,t) => provides_care(h,w,t) ∧ provides_care(w,h,t) ∧ can_exit(w,t) ∧ forall x. ¬can_sanction(x,w,t)`. Subject: `exists h w. married(h,w,t)`.

My gloss, written from the formula and the coverture vocabulary alone: *at every step where a couple is married, both spouses' care fluents are on, the wife's `leave` action is enabled, and no one's `chastise` action against her is enabled.* In this vocabulary:
- `can_exit(w) := enabled leave w`, and `leave` has no effects.
- `can_sanction(h,w) := enabled chastise h w`, and `chastise` is enabled only through R5, whose condition is `married ∧ misbehaves`. `misbehaves` is set by the free action `misbehave`.

Against the gloss ("care both give and she is free not to give"):
- **"Both give"**: matches.
- **"Free not to give"**: not expressed. Nothing in the formula looks at whether her care is obliged. The plan says so ("no fluent says whether her care is obliged"). The consequences are in findings 1 and 2.
- **Subject**: faithful. A married couple exists exactly when the good has a bearer. The premise implies the subject.

## Findings

1. **[major] (b) The formula reads "chosen" as "she may leave", and it accepts care that a binding duty compels as chosen. "Deleting R6 makes chosen mutual care possible" says more than the encoding supports.**
   - **Base.** In the base coverture family the good is absent only because R6 makes `can_exit` false at every married step. The sanction clause plays no part there (finding 2).
   - **R6 deleted.** The good reads fragile. In that row R3, the wife's sanctioned must-be care duty, still binds her. So what becomes "possible" is a state in which she could leave, nobody can chastise her at that step, and she is still under a duty to care, which strict compliance enforces in every trace. That is not "she is free not to give".
   - **Probe.** With R6 and R5 both removed, the good reads **stable** (guaranteed): R2 and R3 force both care strands in every compliant trace. Deleting R3 from that variant reads **guarantee-carrying on `chosen_mutual_care`** (guaranteed lost 2: `chosen_mutual_care` and `mutual_household_care`). Deleting R2 there gives guaranteed lost 5. In the R6-only variant, deleting R5 (or R5~prohibit) moves the good fragile to stable, and the readings table prints "guaranteed gained 1".
   - **What follows.** The good was added to separate chosen from imposed mutual care (revision-1 finding 3, option i). Once the exit bar and the chastisement power go, it reports imposed care as chosen, and guaranteed by the imposing duty. The laundering that revision 1 found in R3's row reappears inside the new good one slice-4 step away. This does not show in the shipped rows only because R6 is present in all nine entries. The plan defers {R5, R6} to slice 4, and the encoding would mislead there.
   - **What is faithful.** Base **absent** in all nine entries. Read narrowly, that says: "as encoded, under coverture no compliant trace has mutual care while the wife has a permitted way out". That is a fair, sayable result, and the strongest thing the good shows about coverture.
   - **R3's lost 0 on this good.** R3 reads lost 0 because the good is already absent with or without R3. It carries no information about R3 (finding 6).
   - **Fix.** Before slice 4 uses this good, either:
     - add a conjunct that sees the duty (no vocabulary supports this today; it needs a derived fluent such as "a binding must on `provides_care(w, h)` is in force", which is an engine change); or
     - declare the good **not readable under the guaranteed measure** (finding 2) and caveat the possible column: "possible = she could leave and no one could chastise her at that step; her care duty R3 may still bind".
2. **[major] (b) The "no sanction" proxy is idle under strict compliance, and the gloss's claim that it is "stricter than the gloss" is wrong in the direction that matters. Reading a chosen good under "guaranteed" contradicts its own gloss.**
   - **The proxy holds at almost every married step.** R3's `or_else` is R5, but R5's condition is `misbehaves`, not her neglect. Under strict compliance she never breaches R3, so no sanction for her care is ever live. `can_sanction(h, w)` is false at every married step until the unrelated free action `misbehave` fires. So "no one holds a power to coerce her" holds at nearly every married step of coverture, the institution in which her care is a sanctioned duty.
   - **The text claims the opposite.** properties.yaml's gloss (and R2.3) says the reading "is stricter than the gloss (any sanction power counts, not only one attached to her care)". In this vocabulary it is looser where it matters: the one sanction attached to her care is invisible, and the clause bites only on an unrelated condition.
   - **The preregistration's reason is wrong.** The prediction text for the R6 row explains fragility by "neglect, neglect_house and misbehave stay free". Under strict compliance `neglect` and `neglect_house` are not compliant while married (R2 and R3 are must-be). The probe shows that `misbehave`, which enables `chastise`, is the only lapse route: removing R5 makes the good stable. The results file does not repeat the wrong reason. Record it as drift in the reasoning, not in a number.
   - **The guaranteed measure contradicts the gloss.** A good defined as care "she is free not to give" should never be guaranteed by the rules. If it is, some rule compels it. So for this good, "stable" is evidence of imposition, not of the good. The results line "guaranteed unchanged" is correct. The guaranteed column for this good should be marked **not meaningful by design**, not shown as a measure that happens to read 0.
3. **[major] (a) Under possible, "constitutive" so far marks only rows that prohibit the care act itself. Those rows are close to tautologies, and they are not the glossary's constitutive bundle.**
   - **Every possible-lost row is a ~prohibit of a care permission.** The rows are ectogenesis R4~prohibit ("an intended parent may provide care", prohibited), gestational-surrogacy R4~prohibit (the same mechanism), and cps R2~prohibit (the caseworker's `may provide_services`, prohibited; an information row). Each reads "forbidding the only way to give care makes care impossible".
   - **The glossary's sense is different.** docs/glossary.md: "constitutive bundle: the good exists only because the parts come together; unbundling deletes the good". A prohibition is not an unbundling. The "agree" cell for ectogenesis R4~prohibit (superadditive) is by construction, for the same reason revision-1 finding 2 gave for guarantees: the goods are written on `provides_care`, and the row forbids `provides_care`.
   - **The headline sentence is accurate.** "In ectogenesis, prohibiting the parent's permission to care makes care impossible." The label "constitutive" (author decision 2: "redesign, do not cut") is not: the advice it implies ("do not ban parental care") is empty.
   - **The glossary has no entries for the reading terms.** It still lacks "guaranteed", "possible" and "guarantee-carrying", and the reading word "constitutive" is not distinguished from "constitutive bundle".
   - **Fix.** In the results and the cards, add beside each constitutive row: "a prohibition of the care act itself; not evidence of a constitutive bundle in the glossary's sense". Add glossary entries for the two measures and the two reading words. Count possible agreement as 4 of 5 plus 1 by construction.
4. **[minor] (a) The state names are now right; two definitions are worded more strongly than the semantics.**
   - **The states and measures are as the results file says.** The four states and the two measures are implemented as R2.1 states (`goods_queries`, `measure_value`, `goods_transition`: n/a is neither under both measures; possible = fragile or stable; guaranteed = stable).
   - **"Possible" is a faithful reading of "the good can happen under the rules", with three qualifiers that belong in the "how to read" paragraph:**
     - "under the rules" means in a strictly compliant trace;
     - within k;
     - at one witness step: for a temporal good such as `cared_for` ("does not lapse while the relation lasts"), possible means care at one step after the grace step, not continuity.
   - **"Guaranteed" is worded as "a rule guarantees the good".** The engine reads "every strictly compliant trace within k has the good at every witness step". That can come from a duty (R2, R3), from a prohibition of the breaker (companion R1~prohibit, guaranteed gained 2), or from a vocabulary in which nothing can unset the fluent. Say "the rules, as obeyed, force it". The strict-compliance caveat is present for coverture (R2's unsanctioned duty read as delivered).
   - **"Fragile" is glossed in decision 1 as "can hold and can lapse".** It is "can hold somewhere and fails somewhere". In kibbutz with R4 deleted, it means that some traces have the child sleep at home and some do not, not that a held good lapses.
5. **[minor] (a, e) "Possible" quantifies existentially over bearers and exogenous starting worlds; "guaranteed" quantifies universally.**
   - A deletion that makes a good impossible for one class of bearer reads possible lost 0 if the good stays possible for another class or in another `initial_free` world. Examples of such classes are the wife with neither property nor wages, which is the margin case, or a second couple.
   - No such row occurs in this run: R2's deletion leaves `maintain` free, so `provided_for` stays possible for every wife.
   - The measure is blind to this by definition, and the project's theory puts "the people who have the least" first. Add one sentence to the "how to read" paragraph: "possible = for some bearer, in some admissible starting world".
6. **[minor] (c) R3 is now reported faithfully, and the caveat is present wherever the row is shown. Two small gaps remain.**
   - **What is present.**
     - The results row reads: guarantee-carrying 1, then "Guaranteed only by R3, an implicit sanctioned duty; not advice to keep it. Under possible, R3 is not constitutive".
     - The cards of coverture-household, coverture-household-us, mwpa-earnings and coverture-floor carry the same words, with "no single deletion makes any good impossible (R2 and R3 unread)".
     - "Possible lost 0" is true for the stated reason: `marry` sets both strands, and `keep_house` is free once R3 is deleted.
   - **Gaps.**
     - The half of the revision-1 caveat that says what the guarantee is for has been dropped. Deleting R3 removes the guarantee of the *husband's receipt* of household labour, a good for the party who holds the sanction. Restore that clause in the row.
     - Do not cite "R3 lost 0 on `chosen_mutual_care`" (results, chosen-care table, "the faithful outcome ... predicted") as evidence about R3. It follows from the good being absent before and after.
7. **[minor] (e) The route comparison now says what it shows. One phrase overreaches.**
   - **What it says correctly.** G guaranteed 5 vs 4 is labelled "by construction: the same margin case as C", in the table and in both route cards. G possible 0 = 0 is a tie. The winner rule per measure is stated. T1 stays a hypothesis, and the floor's advantage is "about guarantee only ... says nothing about order". R20 is called an income-access floor.
   - **The phrase that overreaches.** "Her provision stops depending on R2 being kept." In F, `provided_for` survives R2's deletion through `has_own_income := enabled draw_subsistence`, an action with no effects. What is guaranteed is *access* to an income, a power; no subsistence is delivered (revision-1 finding 10, "adequacy"). Write "her provision, as the formula reads it (an income she may draw), stops depending on R2", and note beside the route rows that this runs through the freedom-shaped disjunct of `provided_for` (finding 8).
8. **[minor] The formula limits that R2.3 promised to report beside the rows they touch are only partly reported.**
   - **Done** (in the cards):
     - police (`is_subject` never cleared);
     - cps (`provides_care` is the caseworker's services; no parental-care fluent);
     - kibbutz (`release` unregulated).
   - **Not done.**
     - `child_with_family` is three goods under one name. The kibbutz reading **absent** rests on its kibbutz disjunct alone, with the cps and ectogenesis disjuncts lowered false there. Its cps disjunct is "not removed", a freedom-shaped condition.
     - Three of `provided_for`'s four disjuncts are power fluents. That is what lets the route comparison see the floor.

     Neither limit appears beside the kibbutz row, the cps rows or the route table. Add one line each.
9. **[minor, phrasing] (f) The revision-2 protocol fixed the three disclosed problems. A new shared input is not disclosed: the gloss chose the fluents.**
   - **Fixed (verified above):**
     - the full prompt is inside the hashed bundle and was each encoder's entire first message;
     - the "prefer shared fluents" instruction is gone;
     - the `care_duty_on_women` style example is gone;
     - conventions.md carries the corrected four-state definitions.
   - **The gloss pre-wrote the formula.** The goods-list row was written by the preregistration author, who had read every revision-1 output and the rules and predicted the result. It reads "can leave" "at the fluent level as her permitted, unsanctioned way out" (the `can_exit` gloss, verbatim) and "no one holds a power to coerce her" (the `can_sanction` gloss, verbatim). So the substantive encoding choice, which fluents stand for "chosen", was made by a non-blind author in the gloss. The encoders were left with quantifier shape, and their equivalence was all but certain.
   - **A pointer to the predicted outcome.** The row also cites "faithfulness review finding 3, option i", the document that predicted the outcome. The encoders could not open it, but the bundle names it.
   - **Residuals, unchanged from revision 1:**
     - `validate.sh` runs a `validate.py` outside the hashed bundle;
     - the harness system prompt of each encoder is not in the transcript.
   - **The pass item is mostly honest.** Pass item 2 ("met ... Same caveat as revision 1: one model, protocol independence") and the merge log ("remove the two disclosed common causes; they do not make the encoders independent people") are honest about the model. They should add: "the gloss fixed the fluent-level reading (`can_exit`, `can_sanction`), written by the non-blind preregistration author; the encoders chose only quantifier form, so their equivalence was expected and is not evidence about the good".
10. **[green] (d) F2 and the not_applicable rows are faithful now.**
    - **The rows.** Ectogenesis R1~prohibit, gestational-surrogacy R2~prohibit and airline-flight R1~prohibit read `not_applicable` after. They are lost 0 under both measures and outside the ranking; ectogenesis R1~prohibit is a protection (down 1). Verified in the run.
    - **The mirror error is closed too.** A rule that makes a bearer exist is not a gain.
    - **The text.** The results file says "A deletion that prevents any bearer from existing is outside the ranking". The ectogenesis card says "the goods are not applicable, outside the ranking, not lost". That is the non-identity reading revision-1 finding 4 asked for.
    - **Kibbutz.** `child_with_family` reads absent, and R4 deleted moves it absent > fragile (possible gained 1, guaranteed gained 0). The children's house now visibly withholds the good, within the limit in finding 8.
11. **[green] Revision-1 fixes carried out as asked.**
    - R20 is relabelled in `plain`, `choices`, the entry name, `source_text`, the notes and the card ("read from but narrower than the material floor"), with `strand: null`.
    - Per-strand counts follow every lost count.
    - The strict-compliance caveat is present at the top of the results section and in the four coverture-family cards.
    - The goods notes carry the ADR 0012 sentence in all eight cards.
    - "As encoded, no rule guarantees these goods" replaces "care is fragile" for police, cps, kibbutz and ectogenesis.
    - The revision-1 wording (pass item 1, `provided_for` encoder 2 as the closer reading, the prompt disclosure) is carried forward.

## 2. Answers to the brief

- **(a)** Yes, with wording fixes. The four states and two measures mean what the results file says. "Possible" faithfully reads "can happen under the (obeyed) rules, within k, at one step, for some bearer". "Guaranteed" is honest if it is worded "the rules as obeyed force it" (findings 4 and 5). Under possible, "constitutive" so far marks only prohibitions of the care act (finding 3).
- **(b)** The formula is a faithful transcription of the R2.3 fluent-level reading. That reading is too loose for "she is free not to give":
  - "chosen" reduces to "may leave";
  - the sanction clause is idle under strict compliance;
  - with exit and chastisement removed, obligated care reads as chosen and guaranteed by R3 (findings 1 and 2).

  Too strict it is not. What may be said: under coverture as encoded, no compliant trace has mutual care while she has a permitted way out, and R6 is the only single rule whose deletion changes that. Do not say that deleting R6 makes chosen care possible.
- **(c)** Yes. "Possible lost 0, not constitutive" is faithful, and the "not advice to keep it" caveat is present in the results row and the four coverture-family cards. Restore "the guarantee is of the husband's receipt" (finding 6).
- **(d)** Faithful (finding 10).
- **(e)** Yes. "By construction", G possible 0 = 0, and T1 a hypothesis are all present. Soften "her provision" to "income access" (finding 7).
- **(f)** All three disclosed problems are fixed and verified. A new non-blind input, the gloss's fluent choice, is undisclosed in the pass item (finding 9).
- **(g)** See section 3.

## 3. Revision-1 findings against revision 2

| r1 | subject | status |
| --- | --- | --- |
| 1 | goods states misnamed; "absent" = no subject | **closed** (four states; bundle2 conventions corrected; kibbutz R4 now visible) |
| 2 | stable = guarantee; "constitutive" misnamed; decide per good which measure is the good | **mostly closed**: renamed guarantee-carrying, possible column added. **Open:** no per-good decision on which measure is the good (for `chosen_mutual_care` the guaranteed column is meaningless, finding 2); "constitutive" under possible has its own by-construction problem (finding 3) |
| 3 | R3 laundering; chosen vs imposed care | **row caveat closed** (finding 6, one clause to restore). **Option (i) only partly achieved:** the new good cannot see the duty and re-launders it once exit and sanction are gone (finding 1) |
| 4 | F2 through the vacuity artefact | **closed** |
| 5 | "fragile everywhere" partly artefact | **closed** in wording (results and cards); limits partly reported (finding 8) |
| 6 | prompt instruction outside the bundle | **closed** for revision 2, disclosed for revision 1. New undisclosed shared input: the gloss's fluent choice (finding 9) |
| 7 | route tie-breaker by construction | **closed**; one phrase to soften (finding 7) |
| 8 | lost counts are not distinct goods | **closed** (per-strand counts) |
| 9 | strict compliance makes R2 delivered maintenance | **closed** (caveat present) |
| 10 | R20 not the glossary's material floor | **closed** |
| 11 | cards do not carry goods | **closed** |
| 12 | `provided_for`: encoder 2 the closer reading | **closed** |
| 13 | pass item 1 phrasing | **closed** |

## Verdict: weakened (narrowly)

Revision 2 fixes the instrument:
- the four states and two measures mean what they are said to mean;
- the n/a rows and F2 are faithful;
- the R3 row is caveated where it is shown;
- the route comparison claims no more than it shows;
- the three disclosed encoder-protocol problems are fixed and verified;
- the cards carry the goods.

What is weakened:
- the new good's headline: "deleting the exit bar makes chosen mutual care possible" (findings 1 and 2);
- the label "constitutive" on the ~prohibit rows (finding 3).

Nothing is refuted. Every number reproduces from the saved run.

**What can be reported now.**
- All of revision-1's "can report now" list stands, plus the following, each as a statement about encodings under strict compliance, within k=6 and 8.
- **Guaranteed column.** In the nine coverture-family entries, R2 and R3 are the only guarantee-carrying rules (R2: 4 formulas, 1 strand; R3: 1 formula, 1 strand). The R3 row carries "guaranteed only by R3, an implicit sanctioned duty; deleting it removes the guarantee of the husband's receipt of household labour; not advice to keep it".
- **Possible column.**
  - No single deletion makes any encoded coverture good impossible.
  - In ectogenesis (and gestational-surrogacy), *prohibiting the parent's care act* makes care impossible. This is a prohibition of care itself, not evidence of a constitutive bundle.
  - In kibbutz, the children's house rule R4 makes `child_with_family` (its sleep-at-home disjunct) impossible, and deleting it makes that possible.
- **No-subject rows.** Ectogenesis R1~prohibit and its two siblings are not applicable: no bearer exists, so nothing is lost.
- **`chosen_mutual_care`.** Under coverture as encoded, no compliant trace has mutual care while the wife has a permitted way out. The exit bar R6 is the only single rule whose deletion changes that; her care duty R3 still binds in that row, and the formula cannot see it. Not reportable: "chosen care becomes possible", and any guaranteed reading of this good.
- **Route comparison.** Tie on N and on G possible. G guaranteed 5 vs 4 is by construction (the margin case) and runs through income *access*. T1 stays a hypothesis.
- **Encoder agreement on the new good.** Protocol independence, audited. Equivalence was expected because the gloss fixed the fluents.

Not reportable until findings 1 to 3 are addressed:
- any use of `chosen_mutual_care` in slice 4 (the {R5, R6} pair reads obligated care as chosen and guaranteed);
- "constitutive" without the prohibition caveat;
- a glossary-sense reading of either measure before the glossary defines them.

Second encoder: agent, not someone living under the institution (ADR 0012).
