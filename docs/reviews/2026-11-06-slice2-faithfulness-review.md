# Encoding-faithfulness review: slice 2 goods properties and the floor route (2026-11-06)

Fresh agent, encoding-faithfulness seat (ADR 0014; plans/priority-slice2.md section 1 "Council" items i to iv). Not the builder, coordinator or an encoder. Read-only apart from this file. Second encoder: agent, not someone living under the institution (ADR 0012). This review is also by an agent of the same model family as both encoders and the builder.

**Read:** plans/priority-slice2.md, plans/priority-slice2-results.md, data/institutions/goods-encoding/ (encoder-1.yaml, encoder-2.yaml, merge-log.md, bundle-manifest.sha256), data/institutions/src/properties.yaml (five goods; `financial_dependence*`), coverture-floor.yaml, coverture-household.yaml (root change), the rules and actions of police-crisis, cps, kibbutz-childrens-house and ectogenesis, the eight cards named in the brief, docs/intent.md, docs/theory.md, docs/glossary.md, philosophy-engine `rules_ablate.goods_state` and `rules_checks.vacuity` (c69aaf1).

**Checked:** bundle hashes (`sha256sum -c` on the scratch bundle: 11/11 OK); goods-list.md = section 3 verbatim; the repo's encoder files = the scratch outputs. Both encoder transcripts (session subagent logs): encoder 1 made 5 tool calls, encoder 2 made 6. Each read only the bundle, ran only validate.sh and wrote only its own goods.yaml, matching the merge log. The two prompts are identical apart from the encoder number. Per-row goods states were read from the run output (`scratchpad/slice2/run/ablate-27-s2.json`, k=6).

## 0. Back-translation (item i)

My gloss of each formula, written from the formula alone, against section 3:

| good | my gloss of the formula | against section 3 |
| --- | --- | --- |
| `cared_for` | Every agent who has been a subject for two steps running has some carer at the later step. | Matches "receives care". "While the relation lasts" became "while a subject", and no action in any of the five entries unsets `is_subject`, so in practice it means "forever once a subject". Faithful for marriage (the relation never ends in these entries). Not faithful for a police crisis encounter, which ends. |
| `mutual_household_care` | Every married pair: each spouse has care from the other. | Matches the words. It is a conjunction of two care fluents. Nothing in it makes it a product beyond the two strands. Both strands also come from an obligation (see 2). |
| `known_carer` | A continuing subject is cared for now by someone who was already a carer at the last step, if anyone was. | Matches (step-to-step overlap). Where only one carer is possible (every coverture-family entry), it has the same truth value as `cared_for`. |
| `child_with_family` | Kibbutz: the child sleeps at home. cps: a case is open, the child is not in custody, and a parent exists. Ectogenesis: a registered parent cares. | Three different goods under one name. The cps disjunct is "not removed", the absence of a control. That is a freedom-shaped condition, not care by the family: the cps vocabulary has no fluent for parental care. |
| `provided_for` | Every wife is maintained by her husband (encoder 2: by anyone), or has her own earnings, own property, or own income. | Matches the gloss. Three of the four disjuncts are derived power fluents (`owns_earnings`, `controls_own_property`, `has_own_income` are enabledness), so the good is a disjunction of a good with freedoms. Section 3 intends this (the capability reading). It is also the only reason the goods measure can see the floor at all (finding 7). |

## Findings

1. **[red] The goods states are misnamed, and the bundle told the encoders the wrong meaning.** In the engine (`goods_state`, `vacuity`), `absent` = the formula's antecedent is never reachable: no subject, or no marriage. `fragile` = `fails`: some compliant trace lacks the good at some step. That covers both "can lapse" and "never present". `stable` = every compliant trace keeps it. The bundle's conventions.md (and section 2 of the preregistration) say instead that a vacuous persists is "the formula never holds in any compliant trace", which "reads as the good is absent". Both encoders wrote with that meaning: their notes on kibbutz `child_with_family` say "absent until sleep_home". The engine reads it `fragile`. The consequences, observed in the run:
   - In the kibbutz, the good is truly withheld (R4 bars `sleep_home`), yet it reads the same state as care that merely might lapse.
   - Deleting R4 gives gained 0 (fragile to fragile), so the instrument cannot see the children's house take the child from the family. That is the central fact of the institution.
   - F2 fires (finding 4).
   - The order stable > fragile > absent makes "nobody exists" the worst outcome.

   Fix (author or builder, not here): rename `absent` to `no_subject` and leave it out of lost and gained. Split `fragile` into `lapsable` (some trace keeps it, some lose it) and `never` (no trace with a subject has it at any step after grace). That needs one extra reachability check per good. Correct the conventions text.
2. **[red] `stable` measures a rule's guarantee, not the good. So only an obligation can make a good stable, and "constitutive" does not mean what the glossary says.** Under strict compliance, a good reads stable only if a binding `must` with no unregulated breaker forces it in every trace. Care that someone gives by choice is fragile, exactly like no care at all. A deletion that reads "lost" turns a guarantee into a possibility; it does not remove the good:
   - After deleting R2 or R3, `maintain` and `keep_house` still fire freely, so mutual care is still reachable.
   - The glossary's "constitutive: unbundling deletes the good instead of freeing it" is therefore not what the reading reports.

   Strand agreement for the care rules is also close to built in. The goods are written on `provides_care`, and the superadditive-tagged must-be rules are the ones that oblige `provides_care`, so "superadditive ↔ constitutive: agree" is expected by construction. For subsistence goods (`provided_for`, a dependent's `cared_for`), guarantee is the right measure: the floor's reason is "no one's survival depends on being chosen". For relational goods (`mutual_household_care`, `known_carer`), part of the good is that it is chosen. Docs/theory.md's core thesis is "turning imposed bundles into chosen ones", and a guarantee-only measure inverts it.

   Fix: call the reading "guarantee-carrying", not "constitutive". Report goods as guaranteed / attainable / never / no subject (finding 1). Decide per good whether guarantee or attainability is the good.
3. **[red] (a) R3 and `mutual_household_care`: the reading launders the duty if it is reported as advice.** The only thing that guarantees the good is R3, a sanctioned duty (or else R5, restraint), implicit and unverified. Deleting R3 removes only the husband's half: his receipt of household labour. So the good that "rests on" R3 is, in that row, a good for the party who holds the sanction. "Redesign, do not cut" read as advice says: keep the wife obliged, because a good depends on the obligation. That is laundering.

   A faithful encoding distinguishes chosen from imposed mutual care. Either (i) add a good `mutual_care_chosen`: married ⇒ both care, and `can_exit w`, and no sanction attaches to her care; or (ii) read relational goods by attainability, not guarantee. Under (i), coverture reads `never` (no exit) and R3 reads lost 0, so F3 would fire, which is the faithful outcome. Under (ii), deleting R3 changes nothing (the care stays attainable).

   **Reportable**, with this caveat: "Under strict compliance, `mutual_household_care` (as encoded) is guaranteed only while R3, the wife's implicit duty enforced by restraint (R5), binds her; deleting R3 removes the guarantee of the husband's receipt of care, not the possibility of mutual care. The instrument cannot tell chosen from imposed care, so this row is not advice to keep R3 and not evidence that R3 is constitutive in the glossary's sense."
4. **[amber] (b) F2 fired by its letter, through the vacuity artefact.** In the ectogenesis R1~prohibit row (no gestation, so no subject), all three goods move fragile to absent. No subject is deprived of anything:
   - Preventing a person's existence is not a loss to that person (the non-identity point).
   - The project's own theory marks it as a separate kind of choice: "a choice about who exists, not only how they live" (docs/theory.md, non-human lessons, item 3).
   - The mirror error is latent too: any rule that lets subjects come into being reads as a goods gain.

   Faithful reading: the goods do not apply (n/a), lost 0. The report should say: "F2 fired as worded (ectogenesis R1~prohibit, lost 3). Every lost family comes from ordering 'no subject' below 'fragile'. Under the faithful reading (no subject = not applicable) the row carries no goods loss. F2's substantive claim, that goods load sits in must-be duties, is neither confirmed nor refuted by this row." Gestational-surrogacy R2~prohibit gets the same note.
5. **[amber] (c) "Fragile everywhere" outside coverture is partly faithful and partly an artefact.** Per entry:
   - **police-crisis.** It is faithful that crisis care is not guaranteed (the officer may `withdraw` when not `in_crisis`). Not faithful: the subject's own `leave` counts as care lapsing, and because `is_subject` is never cleared, a person whose crisis ended "still" needs police care.
   - **cps.** It is faithful that services are discretionary (R2 is a `may`). But `provides_care` here is the caseworker's services, and the vocabulary has no parental care. So `cared_for` means "receives services", and `known_carer` means "same caseworker". Neither is the child's care.
   - **kibbutz.** Artefact. The real children's house was always staffed by rota. The encoding has an unregulated `release` and no duty to keep someone assigned, so "a child with no carer" is a compliant trace. Rotation weakening `known_carer` is real. `child_with_family` reads fragile rather than never (finding 1).
   - **ectogenesis.** Faithful to the counterfactual as built (R4 is a permission, and R5 binds only a registered female parent).

   So it is not that the goods were written to favour coverture. The check kind does that (finding 2): a good is stable only where a binding duty with a never-ending guard forces it, and among the care entries only coverture has that. Report "as encoded, no rule guarantees these goods in police-crisis, cps, kibbutz and ectogenesis, so the instrument cannot read their care strands". Do not report "care is fragile in these institutions".
6. **[amber] The encoder prompt carried a design instruction that is not in the hashed bundle or the repo.** Both prompts say: "prefer a formula that uses only fluents shared across them". That is why both guarded on `is_subject` rather than `responding` or `assigned`, and it caused the police and kibbutz misses. The results file credits "the bundle's style example and the cross-entry vocabulary" and does not mention the prompt. Other shared inputs:
   - The bundle's style example (`care_duty_on_women`) names ectogenesis R4 and R5 and says "only a duty on the female parent closes the gap".
   - Section 3 names the rules that carry each good by id.

   These are small leaks against section 2's aim ("no formula can be aimed at a rule the predictions name"), and they are shared priors. Fix: commit the prompt text to data/institutions/goods-encoding/, and name it in results 4.2 and 4.3.
7. **[amber] (e) The route comparison's tie-breaker is the same by-construction fact as C.** G(T) = 5 and G(F) = 4 differ only in `provided_for` on R2. With R2 deleted:
   - In T it fails for the wife with neither acquired property nor earnings (R13 and R14 are conditioned on those).
   - In F it holds through `has_own_income` (R20's condition is `true`).

   That is `financial_dependence_margin`, which section 5 flagged by construction for C, now in goods form. It also runs through the freedom-shaped disjunct of `provided_for` (section 0). Both end states have all goods stable in the base, so G counts single-rule redundancy of support, not goods present. The results file's sentence ("the floor route leaves fewer goods resting on a base strand; the difference is exactly `provided_for` on R2") is accurate. It should add: "by construction, the same margin case as C; not a finding that the floor yields more goods".
8. **[amber] Lost counts do not count distinct goods.** In the coverture family, R2's lost 4 is one fact, that `provides_care(h, w)` may lapse, seen through four formulas:
   - `known_carer` has the same truth value as `cared_for` there.
   - `mutual_household_care` contains the same strand.
   - `provided_for` differs only where she has means.

   Report lost and G as "goods families whose formula reads that strand", never as "four goods lost".
9. **[amber] Strict compliance turns the husband's unsanctioned duty into delivered maintenance.** R2 has `or_else` null, and the wife has no standing (R4). Historically the duty was enforced, if at all, through tradesmen's claims for necessaries, not by her. Under strict compliance, `cared_for` and `provided_for` read "stable" in coverture. That reads the law's promise as kept. This is a project-wide convention, not a slice-2 error, but the goods table makes it visible: state it next to any coverture goods row.
10. **[amber] (e) R20 is a defensible layer-1 shape, but it is not the glossary's material floor.** Section 5's reasons are internal ones: a state duty would leave every financial property blind, and an action `must` fills the action slot. They justify a permission as the encodable correlative. What R20 does capture: access that no one in the entry can block (no rule touches `draw_subsistence`), with no condition.

    What it does not capture:
    - **The floor's scope.** The glossary floor is "care, health, housing and income", and Sequence step 2 is "decommodified care, health, housing, income". R20 is income only.
    - **Adequacy.** `draw_subsistence` has no effects.
    - **The state's duty.** Nothing can fail to pay.
    - **"Regardless of any relationship".** Only wives exist in the entry, and every property guards on `is_subject` (section 5 says so).
    - **Strand tag.** The `superadditive` placeholder contradicts the glossary: a floor is outside the bundle by definition. No reading uses the tag today (R20 rows are unread protections).

    Report it as "an unconditional income-access floor for the wife", not as "the material floor".
11. **[amber] The cards do not carry the goods.** None of the seven entry cards shows a goods reading. Coverture-household's card does not say that R3 reads guarantee-carrying, and only coverture-floor's card carries the ADR 0012 sentence. Pass item 5 says "card note", so add a one-line goods note with the ADR 0012 sentence to the cards of the five read entries before any card is cited for slice 2.
12. **[green] (d) `provided_for`, contested.** Encoder 2 ("maintained by anyone") is the closer reading of section 3's "a carer's maintenance". Encoder 1 narrows it to the husband. It makes no difference here: in every coverture-family vocabulary only `marry` and `maintain` set `provides_care(x, w)`, and both bind x to the husband, so no reachable state separates the two (0 of 254 rows). It would matter if the floor also provided care from a non-spouse (the glossary's floor includes care). Encoder 1 would then read that care as no provision. Keep both. Note in the results that encoder 2 is the closer reading of the gloss.
13. **[green, with phrasing] (f) Pass item 1.** Protocol independence is met and I reproduced it: transcripts exist, call counts and reads match the merge log, and the bundle hashes verify. Independent pictures of the good are not shown:
    - Both encoders are one model with the same prompt and bundle.
    - They share an example, a misdefinition (finding 1) and an instruction (finding 6).
    - Two of the five formulas are character-identical, and two more are equivalent.

    Suggested results wording: "Met as protocol independence (no contact; transcripts audited by the coordinator and re-checked by the council). Not independent pictures of the good: two instances of one model with one prompt and one bundle, sharing a style example, the goods conventions (including a misdefinition of 'absent') and an instruction to prefer shared fluents. 4/5 equivalent formulas measure that model's consistency."

## Verdict: weakened

The engine predictions (E1 to E3, 4.4) and the layer-1 floor predictions hold, and the readings table is a correct output of the encodings. What the table is said to mean is not supported as stated:
- "absent" means no subject (1);
- "stable / constitutive" means guaranteed by a duty (2);
- the R3 row is a guarantee of the husband's receipt of care by a sanctioned duty (3);
- F2 fired through an ordering artefact (4);
- the route tie-breaker is by construction (7).

Nothing is refuted. The claims need relabelling and caveats before they are results.

**What can be reported now.**
- Engine E1 to E3 and 4.4.
- The layer-1 floor predictions 1 to 7.
- Coverture family, as a statement about encodings under strict compliance: R2 and R3 are the only rules that guarantee the encoded care goods. Deleting R4, R6 or R7 removes a bond without touching any guarantee. The R3 row carries the caveat in finding 3, and "redesign, do not cut" is not presented as advice.
- Police-crisis, cps, kibbutz and ectogenesis: as encoded, no rule guarantees these goods, so the instrument cannot read their care strands (not "care is fragile there").
- F2: fired by its letter, with the finding 4 sentence beside it.
- Route comparison: tie on N. G differs only by `provided_for` for the wife with no property or wages, which is the same by-construction margin as C. R20 is an income-access floor, not the glossary floor. T1 stays a hypothesis, as preregistered.
- Encoder agreement: one model's consistency, with the prompt disclosed (6).

Not reportable until findings 1 and 2 are addressed: any goods count read as "goods lost"; the kibbutz `child_with_family` row or R4 "gained" as evidence either way; "constitutive" in the glossary's sense.
