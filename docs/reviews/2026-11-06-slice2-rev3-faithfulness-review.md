# Encoding-faithfulness review: slice 2 revision 3 (2026-11-06)

Fresh agent, encoding-faithfulness seat (ADR 0014; plans/priority-slice2.md R3.6 step 8). I was not the builder, coordinator, preregistration author, a gloss author or an encoder in this slice. Read-only apart from this file. This review is by an agent of the same model family as every gloss author, every encoder and the builder. Second encoder: agent, not someone living under the institution (ADR 0012).

**Read:**
- plans/priority-slice2.md: "Author decisions after the revision-2 council" and "Revision 3" (R3.1 to R3.6).
- plans/priority-slice2-results.md: "Revision 3", including the side-by-side tables.
- The revision-2 faithfulness review; each of its findings is checked in section 3.
- data/institutions/goods-encoding/: merge-log.md ("Revision 3: gloss authors", "Revision 3: encoders"); r3/: blind-free-list.yaml, blind-gloss.yaml, regloss.yaml, 3d-encoder-{1,2}.yaml, 3x-encoder-{1,2}.yaml, the five prompt files, the four manifests, validate.sh, experiment-properties.yaml.
- src/properties.yaml: the six goods (`primary_measure`, reason, `measure_note`, `history`).
- coverture-household.yaml (R2, R3, R5, R6, `can_sanction`, `misbehave`).
- The goods notes of the coverture-family cards, ectogenesis and kibbutz; docs/glossary.md (guaranteed, possible, carrying, primary measure, obliged); docs/theory.md and docs/intent.md.

**Checked:**
- **Bundle hashes.** The four scratch bundles (`scratchpad/r3/{glossbundle3, reglossbundle3, bundle3d, bundle3x}`) still exist. Each aggregate recomputes to the hash in its manifest, and every per-file line checks OK.
- **Outputs.** The committed r3/ files (free list, blind gloss, re-gloss, four encoder files) are byte-identical to the scratch outputs. The free list hashes to the recorded `eac8bbbd…`.
- **Transcripts.** The transcripts are not in the repository, but they are in this session's subagent logs. I read all seven directly rather than relying on the merge log. Finding 10 covers what the record can and cannot show.
  - **Blind gloss author.** Message 1 is the committed prompt-gloss-1.md, verbatim. Tool calls: Read theory.md, Read intent.md, Write free-list.yaml, handback.
    - Message 1's free list was written at 18:47:17. The hash record is stamped 18:47:30. Message 2 arrived at 18:47:35: prompt-gloss-2.md verbatim, inside the harness's "The coordinator sent a message while you were working: … Address this before completing your current task" wrapper.
    - After message 2: Write gloss.yaml, handback.
  - **Re-gloss author.** Its message is prompt-regloss.md, verbatim. Tool calls: Read theory.md, Read intent.md, Write, handback.
  - **Four encoders.** Each first message equals its substituted prompt (one trailing newline aside).
    - Tool-call counts: 3d-1 11, 3d-2 11, 3x-1 71 (56 Bash), 3x-2 22.
    - Every Read is a file of the encoder's own bundle, and so is every Glob.
    - Every Bash call invokes only that bundle's validate.sh, with loops, variables and `echo` around it. I parsed every command to check this.
    - The one Write per encoder is its own goods.yaml.
    - 3x-1's Glob listed prompt-api.md, and it did not open it.
  - The merge log's audit is accurate.
- **Validator.** philosophy-engine `rules_lower.validate_property` (7859726) returns only syntax errors and undeclared-fluent warnings. So validate.sh, although it loads full entries (rules included) from the live repository, passes no rule information to an encoder (finding 9).
- **Probes.** I read `scratchpad/r3d6/probes.json`, the coordinator's saved probe output. The D6 and revision-2-control states of `chosen_mutual_care` match the results table for every deleted set at k = 6 and 8.
- **Mapping.** The six `primary_measure` values and reasons in src/properties.yaml match the R3.1 table verbatim. experiment-properties.yaml carries the same six.

## 1. Back-translation

**D6 `chosen_mutual_care`** (3d-1, primary; 3d-2 differs only by `¬∃x` for `∀x¬`):
`∀h w. married(h,w,t) ⇒ care(h,w) ∧ care(w,h) ∧ ¬care_obliged(h,w) ∧ ¬care_obliged(w,h) ∧ can_exit(w) ∧ ∀x ¬can_sanction(x,w)`.

My gloss of it, written from the formula and the coverture vocabulary alone:
- at every married step, both care fluents are on;
- no `must` whose condition holds names either care fluent;
- the wife's `leave` is enabled;
- no `chastise` against her is enabled.

In coverture-household, `care(h,w)` is the husband's maintenance (R2, must-be), and `care(w,h)` is her household labour (R3, must-be, `or_else` R5). `chastise` is enabled only under R5's condition `married ∧ misbehaves`.

Against the re-gloss:
- "care for each other": matches.
- "no act or state of that care, by either of them, is required by any rule in force, penalty-backed or not": matches exactly; `care_obliged`'s gloss says the same.
- "the wife can leave": matches (`can_exit`).
- "no one holds a power to penalise her": matches only as "no penalty power is *enabled at this step*". The re-gloss author gives non-domination as the reason for this clause ("can interfere at will even if they never do"), and the formula does not express that (finding 2).
- "Throughout": not expressed. Under the possible (primary) measure, one witness step is enough. Both encoders said so (finding 7).
- Subject: faithful.

**Verdict on D6: a faithful transcription of the re-gloss, apart from the sanction clause.** The revision-2 laundering is gone ({R5, R6} reads absent, against stable for the revision-2 formula).

**Blind formulas** (each against its own blind gloss, r3/blind-gloss.yaml). "Faithful" means the formula says what the gloss says, where the vocabulary allows.

| good | blind-1 says | blind-2 says | faithful to the blind gloss? |
| --- | --- | --- | --- |
| `cared_for` | every subject gets care from someone else who holds no enabled sanction power over them | the same, without "else"; ectogenesis dropped from entries | **Partly.** "Reliably" is left to the measure, which is acceptable under a guaranteed primary. "Needs care" is proxied by `is_subject`. "Not on terms of control" is read as a *currently enabled* power; under the guaranteed measure a conditional power still shows, because some trace triggers it. Not expressible in ectogenesis: blind-1 keeps the formula there with the clause lowered false, so a different good runs under the same name. Finding 4. |
| `mutual_household_care` | both spouses give care, and care obligations are symmetric | equivalent | **No, in its central case.** The gloss's absent case ("falls mostly on one member … by explicit rule") is coverture. The formula reads coverture **stable**, because `provides_care` lumps R2's money maintenance with R3's household labour and the two duties look symmetric. Both encoders marked every entry "partial" for this reason. Finding 3. |
| `known_carer` | anyone receiving care from another has a carer who still cares at the next step | every subject has a carer who also cared at the previous step (new subjects exempt) | **Partly, both.** Neither formula can express knowing. Each reads "continuing" defensibly, in opposite directions: genuine underdetermination, correctly not a candidate. |
| `child_with_family` | cps only: a child with a parent and in no danger is not in custody | cps only: a parent and not in custody, unless in danger | **Yes for cps**; both drop "family has support" with stated reasons. Kibbutz was dropped because the prompt asks for one formula across the listed entries. blind-1 itself wrote the kibbutz formula (`at_home`) under `not_expressible`. That is a bundle effect, not a gloss effect (finding 6). |
| `provided_for` | own income (power to draw, or earnings owned) and care from another | care and own means, including controlled property | **Partly, both.** "Not hinging on a breadwinner" is read as own means. `has_own_income` is a power fluent, so the revision-2 "freedom-shaped disjunct" limit carries over. Housing and health are not expressible. |
| `chosen_mutual_care` | any subject in a care relation: care both ways, unobliged both ways, she can exit, own income | married couples: the same, with own means | **Yes, both**: "not imposed by law" is read as unobliged both ways, and "could leave and be okay" as exit plus own means. |

Both blind encoders read "imposed by law" as excluding *both* spouses' obliged care, and so did the re-gloss author. Three readings (all by the same model) agree on that point.

## Findings

1. **[major] (a) The D6 absence is by construction and overdetermined. The cards' summary sentence states the opposite of what the probes show.**
   - **By construction.** The O5 dataset pin (`married ⇔ care_obliged(h,w) ∧ care_obliged(w,h)` in coverture-household, holds_to_k) entails, by itself, that the formula's obliged conjuncts fail at every married step. "Absent in the base of all nine entries" is therefore a consequence of the definition plus the pin, not a reading of the institution. Like the revision-2 "~prohibit" rows (revision-2 finding 3), it confirms the implementation. Say "by construction" beside it.
   - **Overdetermined.** Each of R2, R3 and R6 is on its own sufficient to bar the good:
     - with R6 deleted, R2 and R3 bar it;
     - with {R3, R6} deleted, R2 bars it;
     - in the base, R6 also bars it.

     Single-deletion ablation cannot attribute an overdetermined absence. "No single rule moves the good" is correct and reads exactly that way.
   - **The card sentence inverts this.** The goods note of coverture-household, -us, mwpa-earnings and coverture-floor says: "As encoded, no single rule stands between the couple and chosen mutual care." In plain English that says nothing much bars the good. The truth is that three rules each bar it. Replace it with: "each of R2, R3 and R6 on its own bars it, so no single deletion makes it possible; it becomes possible only with all three deleted (probes)."
   - **It does not discriminate coverture.** Any regime with a care or support duty on either spouse reads absent, as the re-gloss author flagged. So does any regime where `provides_care` carries maintenance, which in this vocabulary is the husband's care. The {R5, R6} probe shows this inside the data: a marriage with free exit and no chastisement power, keeping the two duties, reads absent. The duties are what a modern reciprocal-support code would also impose, up to their gendered content.
   - **What may be said about coverture.** "As encoded, coverture has no compliant trace with mutual care that no rule obliges, and it has three independent bars: the husband's duty, the wife's duty and the exit bar." What may not be said: that this distinguishes coverture from marriage under any later law. The dataset has no entry that tests that.
2. **[major] (a) The no-sanction clause is still idle, and it is now consequential: the good becomes possible with the husband's chastisement power intact.**
   - The probes read {R2, R3, R6} **fragile** and {R2, R3, R5, R6} **fragile**, identical under both measures. R5 makes no difference.
   - The reason is R5's condition, `misbehaves`, which starts false. Some trace has a married step with care both ways and no enabled `chastise`, and that is enough under possible.
   - The re-gloss author kept this clause *for non-domination* ("can interfere at will even if they never do"; theory.md, Pettit). The formula reads the opposite: a standing, conditional power to chastise her does not count.
   - The measure_note discloses "the no-sanction conjunct remains idle under strict compliance". The D6 paragraph of the results and the cards, however, say the good becomes possible "only when both duties and the exit bar go" without adding "even though R5, the husband's power to chastise her, stays".
   - **Fix (reporting):** add that clause wherever the {R2, R3, R6} probe is cited.
   - **Fix (encoding, revision 4 or slice 4):** a derived fluent for a *standing* sanction power, for example "some may-rule on `chastise x w` exists whose condition can become true". This is engine work, like `obliged`. Until then, the possible reading of this good cannot see domination, and it must not be used in slice 4 to say that removing the duties and the exit bar yields chosen care.
3. **[major] (c, d) The blind `mutual_household_care` is not faithful to its gloss. Its "R3 carrying (possible)" re-launders R3, and condition 3 of the replacement rule fails. Do not replace.**
   - The blind gloss's absent case is "care in the household falls mostly on one member … by explicit rule". Coverture's R3 is that case. The blind formula reads coverture **stable** in all nine entries, because R2 (money maintenance, `provides_care(h,w)`) and R3 (household labour, `provides_care(w,h)`) make `care_obliged` symmetric.
   - It then reads R3's deletion as **stable > absent**: carrying (possible), and constitutive. Under the author's primary measure, the wife's imposed, sanctioned household duty becomes the rule that makes shared household care possible. This is revision-1 finding 3 (the R3 laundering) in its strongest form: on the primary column and with a "constitutive" label. R2's row is the mirror case.
   - **Better or worse than the dataset (question d)?** Worse. The dataset reading (R3 unread under primary; guarantee-carrying with "not advice to keep it" and "the guarantee is of the husband's receipt of household labour") is the less misleading one.
   - **Shared root.** Both formulas read coverture as having mutual household care, because `provides_care` cannot tell maintenance from household work. Both blind encoders recorded that as "partial" in every entry.
   - **What follows.** Neither formula measures the gloss's good, "how the household's work is actually distributed". The honest record is "not faithfully expressible in this vocabulary". If the author wants the good, revision 4 should first split the care fluent, for example a maintenance fluent and a household-labour fluent; the actions `maintain` and `keep_house` already exist. Then it should re-gloss and re-encode.
4. **[major] (c) The blind `cared_for` is a different good, care without domination. It puts a freedom inside a good and is not expressible in one of the five entries. Condition 1 is not met as written, and condition 3 fails. Do not replace.**
   - **A different good.** The blind gloss adds "it must not depend on someone else's control over the person". The formula reads that as "the carer holds no enabled sanction power". That is the care+control unfreedom the dataset already tracks as a freedom property (`care_and_sanction_same_role`).
   - **It hides the tension.** Folding it into a good makes the goods column re-score a freedom. The project scores freedom and flourishing separately and reports disagreement between them (intent.md), and this fold makes the tension between "R2 delivers care" and "the deliverer can chastise" invisible.
   - **The row consequence.** R2 loses its `cared_for` load (coverture R2 carrying (guaranteed) > carrying (possible); airline-flight R2 unread). A reader would take that as a fact about care, when it is the freedom term at work.
   - **Applicability.** blind-2 dropped ectogenesis from its entries, one of the five preregistered entries. blind-1 kept ectogenesis with the control clause lowered false, so its `cared_for` there is the plain good under the same name. That is the heterogeneity revision-2 finding 8 flagged for `child_with_family`. So condition 1 is met only on rows where both blind formulas apply, and ectogenesis is not among them.
   - **What it is useful for.** Under the guaranteed measure the conditional power does show (fragile in coverture; stable once R5 is deleted). If the author wants "care from someone with no power over you", it should be preregistered as a separate good, not substituted.
5. **[major] (primary mapping) "R3 carries no good under the primary measure … a consequence of the value call, not of the encodings" is mis-worded.**
   - It is reported as a value call in the results (D4 paragraph), in docs/glossary.md and in the four coverture-family cards, with the mapping beside it. That much is as asked.
   - **The experiment refutes the clause "not of the encodings".** Under the same mapping, both blind formulas make R3 carrying (possible) in all nine entries. The result depends on the value call **and** on the dataset formula, which cannot see obligation.
   - **What the possible column can and cannot see.** The reason for `mutual_household_care` reads "mutual care that the rules force is control, not the good". The possible measure cannot implement its first half: it counts stable (forced) as possible. So R3's imposition is invisible on the primary column by design. "Carries no good" must not be read as "imposes no cost on any good".
   - **Write:** "under the author's value call and the dataset's `mutual_household_care` formula, R3 carries no good on the primary column. The possible measure cannot tell forced from free mutual care, so R3's imposition is not visible there. Under the blind formulas R3 reads carrying (possible), a reading judged unfaithful (faithfulness review rev3, finding 3)."
6. **[major] (b) The experiment's causal headline overclaims.**
   - **The overclaim.** "Agreement dropped … to 1 of 6: the earlier convergence depended largely on the gloss fixing the fluents" (results, merge log). Between revision 1 and the blind run, much more than the gloss author changed:
     - the gloss content: richer, multi-clause glosses with control, economics and own-means conditions;
     - the prompt's cross-entry instruction: revision 1's "prefer shared fluents", against revision 3's "one formula for all listed entries if the vocabularies allow it, else not_expressible". This alone explains `child_with_family` going cps-only;
     - the vocabulary (`care_obliged`, `has_own_income`) and the conventions bullet;
     - the six goods encoded together.

     The drop is *consistent with* revision-2 finding 9, but it does not isolate it.
   - **A cheap control.** Two fresh encoders on bundle3x with the revision-1 glosses substituted. If they agree on about 4 of 5, the gloss is the cause.
   - **"0 of 12 blind formulas equal the dataset's" is near-guaranteed.** The blind glosses describe different goods: chosen care with own means, care without control, provided-for as own means. What it shows is that **an id does not fix a good**: two authors starting from the same id write different goods. It also shows that the dataset formulas encode the non-blind author's goods. It does not show that the dataset formulas are wrong encodings of their own glosses.
   - **The free list adds something real.** From theory.md and intent.md alone, the blind author named neither mutual care, chosen care nor child-with-family (X1 borderline). The *selection* of goods is the non-blind author's choice. Report that beside the goods list.
   - **"Blind" covers the gloss text only.** The ids, the `entries` lists (which fix the institutions, and so the bearers, for instance marriage for `chosen_mutual_care`), the vocabularies (written by the dataset authors, `care_obliged` included), and the conventions with their `is_subject` style examples are all non-blind shared inputs.
   - **Same model.** One gloss author, so gloss variance and encoder variance are confounded. Two encoders of one model: 1 of 6 is one model's consistency on these glosses. It is no bound on cross-model or human agreement in either direction.
   - **What to say instead:** "with glosses written blind, the gloss-to-formula step is underdetermined for this model on five of six goods. The ids do not fix the goods, and the theory documents alone did not produce three of the six goods. The cause of the drop from revision 1 is not isolated."
7. **[minor] (a) "Throughout" and the bearer.** The re-gloss says "Throughout, the wife can leave". Under the possible primary measure, one witness step suffices: one step where she can leave and no duty binds. Both encoders noted they added no temporal operator. Add "at one step, not throughout" to the D6 paragraph (glossary "possible" already says "not continuity").
8. **[minor] (f-style) The 3d encoders' equivalence was expected: revision-2 finding 9 recurs in the dataset half.**
   - The re-gloss prompt gave the author the vocabulary's new power ("can say, for each act or state of care, whether some rule in force at that step obliges it … cannot say which rule"). It also gave the revision-2 gloss, written by the non-blind author with the `can_exit` and `can_sanction` readings.
   - The re-gloss paraphrases the `care_obliged`, `can_exit` and `can_sanction` glosses almost verbatim. The encoders were left with quantifier form, and their equivalence was all but certain (R3.5 rated it "medium: the re-gloss names no fluents now").
   - The results headline reports "both dataset encoders wrote z3-equivalent formulas" without this. Add "expected: the re-gloss restates the fluent glosses; not evidence about the good".
9. **[minor] (e) The validator is acceptable; "self-contained" is not the right word.**
   - validate.sh `cd`s into the live repository and loads `data/institutions/institutions.json` (rules included) through the engine. The bundle hash therefore does not pin what the validator does. The manifest helps: it records that file's sha256 and the engine pin.
   - Its output is syntax errors and undeclared-fluent warnings only (checked in `validate_property`), so no rule information reaches the encoder.
   - Replacing the revision-2 validator was right: it warned `care_obliged` undeclared in coverture-floor, which would have pushed encoders off the fluent.
   - Reword the merge log: "loads the dataset entry from the repository at the recorded hash; outputs syntax and declared-fluent checks only".
10. **[minor] (audit) The merge-log record is accurate but cannot be re-audited from the repository.**
    - **Accurate.** I re-derived it from the session's subagent logs: counts, the bundle-only reads, validator-only Bash, own-file writes, the message order with timestamps, and the first messages verbatim.
    - **Not re-auditable.** The repository carries only the coordinator's summary, and the scratch logs are "not kept". Commit, per agent, the tool-call listing (name plus path or command) and the transcript file's hash. A later reviewer would then not depend on this session's scratch.
    - **What no record here can show:**
      - each agent's harness system prompt (about 30k characters, present in the prefix only as a hash, as in revision 2);
      - whatever the model already knows about this project or its documents;
      - whether the coordinator's choice of *which* six ids to give shaped the glosses (it did, by design; X1).
    - The gloss-author audit lists the substantive calls and omits the handbacks: trivial.
11. **[minor] Card coverage.**
    - airline-flight R2 is in `primary_carrying` and gestational-surrogacy R4~prohibit carries (possible), but neither card has a revision-3 goods note.
    - The five MWPA cards other than mwpa-earnings have no goods note at all (unchanged scope from revision 2).
    - Blind goods were also evaluated in entries outside their encoders' `entries` (the companion entries, airline-flight, crisis-team), as the dataset goods are. The blind `cared_for` "absent" in the companion entries is such an extrapolation. Say so if those rows are cited.
12. **[green] (e) The coordinator's stricter-than-spec procedures are acceptable.**
    - **Message 2 held out of glossbundle3.** It strictly reduces exposure, it is verified by timestamps, and the bytes were restored unchanged.
    - **Vocabulary drift.** The current dataset vocabulary, with `has_own_income`, `would_not_benefit` and the real coverture-floor entry, is correct for an experiment run against D6. "`care_obliged` only" was a wrong expectation in the spec, and the drift is disclosed with full diffs.
    - **cps `defaults` kept**, as in revision 1.
    - **Split run.** It is forced by the engine's subject check. Contested readings are computed with the engine's definition across the two runs, and the one consequence (blind-2 `cared_for` unevaluated in ectogenesis) is disclosed.
13. **[green] D6 fixes revision 2's two major findings at the level they were stated.** {R5, R6} reads absent (revision-2 finding 1). The guaranteed column is marked not meaningful (finding 2's second half). Every R3.5 variant-B prediction held, no RF3 fired, and I re-read the probe output.

## 2. Answers to the brief

- **Back-translation.** D6: faithful to the re-gloss except the sanction clause (finding 2) and "throughout" (finding 7). Blind formulas: see the table in section 1. Faithful: `chosen_mutual_care` (both) and `child_with_family` (cps part). Partly faithful: `cared_for`, `known_carer`, `provided_for`. Not faithful in its central case: `mutual_household_care`.
- **Transcripts.** All seven were audited directly from the session logs, and they match the merge log. No breach. The record in the repository is sufficient as a summary but not re-auditable (finding 10).
- **Primary mapping applied as stated.** Yes: six keys and reasons verbatim; experiment-properties.yaml keeps them.
- **"R3 carries no good under the primary measure" reported as a value call.** Yes, in the results, the glossary and the cards. But the clause "not of the encodings" is false (finding 5).
- **(a)** The fair statement is "under coverture as encoded, no compliant trace has mutual care that no rule obliges, and R2, R3 and R6 each bar it on their own". That is by construction (the O5 pin) and does not separate coverture from any marriage with a support duty. "Both spouses' obliged care excluded" is faithful to the re-gloss, and the blind author and both blind encoders read it the same way. It is stricter than theory.md's imposed-vs-chosen bundle, which turns on exit and alternatives. That is a value call the author should own, with the re-gloss author's note beside every absent reading. The card sentence "no single rule stands between the couple and chosen mutual care" inverts the result (finding 1). The good becomes possible with the chastisement power intact (finding 2).
- **(b)** It shows three things: for this model, a blind gloss underdetermines the formula on 5 of 6 goods; ids do not fix goods; the theory documents alone do not produce three of the six goods. It does not show that the dataset formulas misencode their own glosses, or that the drop from revision 1 is caused by the gloss alone (several inputs changed), or anything across models or people. Finding 6.
- **(c)** `mutual_household_care`: unfaithful to its blind gloss in coverture; condition 3 fails. `cared_for`: a different good (care without domination) that duplicates a freedom property, and it is not expressible in ectogenesis; condition 3 fails. **The author should not replace either.** Findings 3 and 4.
- **(d)** Worse. The blind formula reads coverture as having shared household care and makes the wife's imposed duty the rule that keeps it possible, which is R3 laundering on the primary column. Finding 3.
- **(e)** Acceptable; the "self-contained" wording should change (findings 9 and 12).

## 3. Revision-2 findings against revision 3

| r2 | subject | status |
| --- | --- | --- |
| 1 | "chosen" read as "may leave"; obliged care laundered at {R5, R6} | **closed** ({R5, R6} absent; revision-2 formula control stable). New: the absence is by construction and overdetermined; card wording inverted (finding 1) |
| 2 | no-sanction proxy idle; guaranteed not meaningful | guaranteed **closed** (measure_note). Idle proxy **open and now consequential**: possible with R5 intact (finding 2) |
| 3 | "constitutive" = care-act prohibitions | **closed** (glossary "constitutive (reading)", card labels) |
| 4 | measure wording | **closed** (glossary guaranteed, possible) |
| 5 | possible is existential over bearers and worlds | **closed** (glossary "possible") |
| 6 | R3 row: restore "husband's receipt" | **closed** (cards) |
| 7 | "her provision" → income access | **closed** (coverture-floor card) |
| 8 | formula limits beside rows | **closed** (kibbutz disjunct; provided_for power disjuncts in the coverture-floor card) |
| 9 | the gloss chose the fluents | **closed for revision 2; recurs for 3d** (finding 8). The blind experiment tests it but does not isolate it (finding 6) |
| 10 | F2 and n/a | still faithful |

## Verdict: weakened (narrowly)

Supported:
- the D6 encoding is a faithful transcription of the re-gloss, and the laundering is gone;
- every gloss author and encoder stayed inside its bundle, verified from the transcripts;
- the primary mapping is applied as written and called a value call;
- the experiment ran as specified, with disclosed and acceptable departures;
- every number I re-read reproduces.

Weakened:
- the D6 statements in the cards (finding 1) and the omitted R5 caveat (finding 2);
- the "not of the encodings" clause (finding 5);
- the experiment's causal headline (finding 6);
- both replacement candidates, which fail condition 3 (findings 3 and 4).

Nothing is refuted.

**What can be reported now.** Each item is a statement about encodings, under strict compliance, at k = 6 and 8.
- **`chosen_mutual_care` (D6).**
  - Under coverture as encoded, no compliant trace has mutual care that no rule obliges either spouse to give while she can leave. This is by construction: R2 and R3 oblige care at every married step.
  - R2, R3 and R6 each bar the good on their own, so no single deletion moves it.
  - With all three deleted it becomes possible, at one step, **even though the husband's power to chastise her (R5) remains**, because the sanction clause reads only an enabled power.
  - The revision-2 laundering ({R5, R6} read stable) is gone.
  - Any spousal support duty would make the good unattainable in the same way.
  - Not reportable: that this distinguishes coverture from later marriage law; that deleting R2, R3 and R6 yields chosen care free of domination.
- **Primary column.** R2 is carrying (guaranteed) for `cared_for` and `provided_for` in the coverture family, and for `cared_for` in airline-flight. In ectogenesis, R4~prohibit is carrying (possible), a prohibition of the care act.
  - **R3, value call.** Under the author's value call *and the dataset formula*, R3 carries no good on the primary column. The possible measure cannot see forced care.
- **Blind experiment.**
  - With glosses written from theory.md and intent.md alone, two Claude encoders agreed on 1 of 6 goods. No blind formula equals the dataset's, because the blind author wrote different goods for the same ids.
  - The theory documents alone did not yield mutual care, chosen care or child-with-family.
  - The drop from revision 1's 4 of 5 is consistent with the gloss having fixed the fluents, but the cause is not isolated.
  - One model throughout; the non-Claude encoder was not run.
- **Replacement candidates.** None. `mutual_household_care` is not faithfully expressible until the care fluent separates maintenance from household labour. A blind-style `cared_for` would be a new good, care without domination, to preregister separately if wanted.

Not reportable until findings 1, 2, 5 and 6 are answered:
- the card sentence "no single rule stands between the couple and chosen mutual care";
- any use of `chosen_mutual_care`'s possible column in slice 4 as "free of domination";
- "not of the encodings";
- "the earlier convergence depended largely on the gloss" as a demonstrated cause.

Second encoder: agent, not someone living under the institution (ADR 0012).
