# Faithfulness batch 3c: encoding-faithfulness seat (ADR 0014)

Seat: fresh; did not build the batch. Read: docs/reviews/SEATS.md (this seat); plans/faithfulness-batch.md A1, A3, B3, B7, section 6, section 8 (preregistration and Results); `git diff 2252983..987d996 -- data/institutions/src/`; the full YAML of cps R1, kibbutz R3/R5/R6 and dropped R8, footbinding R3 and dropped R2, ectogenesis R3/R5/R6, surrogacy R3; README "Default-capacity actions". No external source fetched; no engine run; no other seat's review read. Judgments are against the excerpts the YAML itself records.

Model-family caveat: same model family as the encoders; a shared misreading of an excerpt would not show here.

Confirmed from the diff: no `kind`, `deontic`, `aim` or `implicit` changes; only the preregistered edits and prose.

## Counts

Rules judged 7: faithful 5, understates 1 (cps R1, disclosed), overstates 1 (ectogenesis/surrogacy R6 as retained), cannot tell 0. No `unsourced` or `overstates` on a rule the headline result reads (R6 carries load 0 and feeds no property), so the batch does not pause.

## Findings

1. **cps R1** (`must investigate when (and (report_received c) (cause_to_believe c))`): **understates, disclosed**. The recorded excerpt, "the social worker shall immediately make any investigation the social worker deems necessary ...", does not contain the trigger clause, so whether the statute says "cause to believe ... described in s. 300" cannot be told from the excerpt; it rests on the provenance `note`. Taking the note as read, the statute's trigger is cause to believe alone; the row keeps `report_received` as a second conjunct, so the encoded duty fires in fewer worlds than the statute's. The `note` says so ("not a received report (encoded as both since 3c)"); `plain` says what the formal says. Provenance honest: `opened`, accessed 2026-11-06, verbatim excerpt. "Immediately" is unencoded and unmentioned; minor. A stale `notes` sentence understates the provenance: "Only WIC 306 was read; R1, R2, R7, R8 cite sections from memory" is false for R1, opened since batch 2.

2. **kibbutz-childrens-house R5** (`may visit when (visiting_time child)`): **faithful**. Excerpts: "visited their parents for 2-3 hours a day"; "Fathers were supposed to bond with their children through quality time". A bounded daily window is what the page reports; "at any time" is gone. The pre-existing direction gap (page: children visit parents; row: a male member visits the child) is disclosed in `plain`, `source` and the item note. Prereg deviation, arity 1 on the child rather than nullary: acceptable; "2-3 hours a day" is said of the children, so a per-child window is at least as faithful, and with one child in the domain the readings coincide. Recorded before the run.

3. **kibbutz R8 dropped; `neglect` `default_capacity: true`**: **faithful**. R8's source was "UNVERIFIED (general knowledge; no source opened)", added for a layer-2 engine need. A capacity held unless a disability bars it is a weaker claim than a norm permitting neglect; R3's unchanged source ("neglect breaks it (sanction R6)") still names the breach. The `notes` sentence is accurate.

4. **footbinding R2 dropped; `leave_unbound` `default_capacity: true`**: **faithful**. R2's source said "leaving a daughter unbound is always physically open to the family; R3 is what sanctions it": the README's definition of a default capacity, not a `may` norm. R3 is untouched and still matches the Mackie snippet ("maintained by interdependent expectations on the marriage market"). Stale prose: `notes` still says "leave_unbound (R2) becomes costless"; R2 no longer exists.

5. **ectogenesis R3** (`or_else` R6 -> null, `sanctioner: none`): **faithful**. `source` records Firestone "from memory", UNVERIFIED; the reprimand had no text behind it, so removing it removes an invention. `plain` ("no sanction is encoded") says what the formal says. Observation only: `kind: formal` on a rule drawn from a manifesto is pre-existing; a later kind pass should look.

6. **gestational-surrogacy R3** (`or_else` R6 -> null, `sanctioner: state` -> none): **faithful**. "UNVERIFIED: no statute or case opened"; neither the sanction nor the `state` sanctioner had a source. The new `source` sentence gives an engine reason (the iso bit), not a source reason; honest under the UNVERIFIED frame.

7. **ectogenesis R6, inherited by surrogacy** (`registry may reprimand when true`, kept, "linked to no rule"): **overstates**. The story is coherent ("formerly the sanction for R3"), but what remains is a written-law (`kind: formal`) power to reprimand anyone at any time, `source` admitting "no text opened for this rule", with no function left. The reason for keeping it ("so the pair's rule set stays symmetric") is weak: surrogacy inherits R6 and would drop it symmetrically. The provenance `note` is stale: "rationale: the registry's sanction for R3 (or_else target ...)" still reads as current. Not read by any headline verdict (ablation load 0); fix pass.

## Fixes requested (prose only)

1. cps `notes`: strike R1 from "Only WIC 306 was read; R1, R2, R7, R8 cite sections from memory", since R1 carries an opened WIC 328(a) item. Optional, at the next page open: extend the R1 excerpt to the trigger clause so "cause to believe" is quoted.
2. footbinding `notes`: "leave_unbound (R2) becomes costless" -> "leave_unbound (a default capacity since 3c) becomes costless".
3. ectogenesis R6 provenance `note`: "the registry's sanction for R3 (or_else target ...)" -> "formerly the sanction for R3 (link dropped 2026-11-09); no text names this power"; and add the same "no text names this power" to R6 `plain`, since "linked to no rule" alone does not tell a card reader the power is unsourced. Deleting R6 is cleaner but is an encoding change for a later preregistration.
