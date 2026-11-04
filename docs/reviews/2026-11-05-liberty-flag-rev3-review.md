# Council review: slice 1 revision 3, the liberty flag (ADR 0014 seats: correctness, encoding faithfulness)

Reviewer: fresh council seat, did not build this. Read-only; this file is the only write. Nothing committed.

Subject: `ActionDecl.liberty` (philosophy-engine 9cf3672, ADR 0013 amendment 2026-11-05), `contract` flagged in the
coverture chain (computational-liberation 97b2542), preregistered in plans/priority.md "Slice 1 revision 3" (98ae2f2),
results in plans/priority-slice1-results.md "Revision 3 run".

What I ran: `uv run pytest -q tests/test_rules_liberty.py tests/test_rules_meta.py` (162 passed, 104 s);
`uv run phil rules check-all --json` with and without `--no-cache` on HEAD (both 25 reports, 123 rows, identical row
sets and verdicts; 123/123 against `expected_properties` once `unreachable_open` is normalised to `open`;
`cannot_contract` holds_to_k on coverture, creditor-exemption, property, earnings, property-narrowed and violated on
sole-trader and suit, as prediction 1 said). The ablation outputs (ablate-25-v5) were not kept, so predictions 2 to 4
are checked against the record only.

## 1. Correctness: do the two lowerings implement the same semantics? [green, with one amber note]

Yes. `rules_lower.Grounded.enabled` sets `en = True` for a liberty action and then conjoins `not (or disabilities)`;
`rules_reference.Reference.power` skips the grant test when `self.actions[action].liberty` and then returns
`not any(disability holds)`. Both take "disability" as `must_not` with `or_else is None` (`self.disabilities` in the
reference, `ri.rule.or_else is None` in the lowering), both return false for a non-instance, both leave firing
untouched. `test_reference_agrees_with_the_z3_lowering` pins five configurations and the direct `power()` reading.

The case you asked about, a liberty action with a sanctioned prohibition (`must_not` with an `or_else`): ignored by
both lowerings, so they agree. Whether it *should* be ignored is a different question and the ADR's own gloss says
no. The amendment defines a liberty as "the absence of a duty not to"; a sanctioned `must_not` is precisely a duty not
to, so under that gloss a sanctioned prohibition negates a liberty while leaving a power intact (one can validly
contract and be punished). The engine treats both kinds alike, which is right for powers and arguably wrong for
liberties. No dataset liberty currently carries a sanctioned prohibition (the only liberty is `contract`; the seven
sanctioned prohibitions in the dataset are on `transfer_reserved`, `abandon`, `assign`, `leave_unbound`), so no
committed verdict turns on it, and no test pins the choice either way. Record the choice in the amendment and add a
test, or change it; do not leave it implicit.

Minor: `next(a.liberty for a in self.inst.actions if a.name == action)` is a linear scan per `(enabled ...)` call;
harmless at this dataset size.

## 2. Interaction with step_mode, compliance=sanctioned, and the ABM [amber]

`step_mode` and `compliance`: no interaction. The liberty flag touches only the `(enabled ...)` pseudo-predicate; the
firing-enablement block (unregulated actions fire freely; under `sanctioned` a breached sanction also enables) and the
one-action-per-step constraint are unchanged by the commit. The cache key carries both modes, so no stale cross-mode
hit is possible.

ABM: yes, there is a semantic change to the frozen layer. `philengine/abm/model.py::_readings` gates an agent's
`available` list on `self.ref.power(...)`, and the module docstring (line 8) states "An action no may/must rule names
is never available to an agent", which was true at the 2026-11-04 gate record (engine 0abf7a4, 23 entries including
the coverture chain). After 9cf3672, `contract w` is available to every unmarried wife agent in the seven
coverture-chain entries. `contract` has no effects and zero payoff, so it never wins on `net`, but `agent.choose`
step 7 draws "a random lawful candidate" from `model.random` when obligations are in force and no practice is usable
(agent.py ~line 230), so an extra lawful candidate changes which action is drawn and consumes the shared RNG
differently. The frozen gate (a)/(b) sweep over those entries is therefore not guaranteed to reproduce. This is not
recorded anywhere: the ADR amendment says "Trace semantics is unchanged" and is silent on the ABM; plans/priority.md
says "No ABM work (layer 2 frozen)". Required: a line in the amendment and in plans/layer2-abm.md, plus either a
rerun of the gate on the seven entries with the result recorded, or an assertion (with evidence) that `contract` is
never drawn. The ABM docstring line 8 is now false and should be amended.

## 3. Preregistration integrity [green on sequence, amber on labelling]

Sequence holds: 98ae2f2 (preregistration) 2026-11-04 16:15:47 -0500; 9cf3672 (engine) and 97b2542 (dataset) both
16:31:10 -0500. `git diff 98ae2f2 HEAD -- plans/priority.md` touches only an appended "Candidate for slice 2" section;
the five predictions are byte-identical. The results table answers each prediction with what was predicted (five
entries for R7, `{R6, R7}` tops with R4 not joining, 18 of 18 non-liberty entries identical, 536 tests), and my
check-all reproduction matches prediction 1 where I could check it.

Two labelling problems. (i) Every heading says "2026-11-05" while every commit is 2026-11-04 local time; the
preregistration claims to be dated after the clock says it was. Pick one convention and state it. (ii) The evidence
section (799daae, 16:14) that precedes the preregistration by one minute already contains the global-flip experiment
run on the full dataset, the diagnosis of exactly which rule flips under which semantics, and the predicted tops. By
the time prediction 3 was written the engine is deterministic and the author had already computed the answer; the
preregistration records a design consequence, not a forecast that could have failed. That is fine as a record of
intent; it is not independent confirmation, and the results file treats it as one (see 5).

## 4. Encoding faithfulness [amber]

**`contract` under Blackstone I.15.** The wife's "legal existence is suspended during the marriage"; she cannot
contract in her own name (her contracts are void, save as her husband's agent for necessaries), cannot sue or be sued
without him. A feme sole has full capacity: she contracts, sues, holds property. So "an unmarried woman could contract"
is right, and encoding coverture as a disability on a default capacity rather than as silence is faithful. The flag
on `contract` is defensible.

**The name is a Hohfeldian misnomer.** The amendment glosses "a liberty is the absence of a duty not to, a power is a
granted ability to change legal relations" and then classifies contracting, the paradigm Hohfeldian power, as a
liberty. Incapacity to contract is a *disability* (the correlative of no-power), which is the word the dataset already
uses for `or_else: null`. What the flag actually encodes is "general capacity of a person of that kind, held by
default, removed only by an express disability" versus "special power conferred by a rule". Rename (`capacity`,
`default_capacity`) or fix the gloss; as written, future encoders will reach for it on `carry_weapon`-shaped liberties
and skip it on `sue`-shaped capacities, which is the opposite of what the mechanism does.

**Every other disability in the dataset, against the README rule "mark a liberty only where the institution withholds
by prohibition something people do by default":**

| disability | grant on the same action | reading the README rule gives | reading the dataset uses |
| --- | --- | --- | --- |
| coverture chain R4 `sue w` when married | R9 `may sue when (not married)`; mwpa-suit adds R16 | **liberty**: a feme sole sues by default; coverture withholds by prohibition, the acts restore | power, with the prohibition's complement baked into R9. R4 is then redundant for `has_standing` and its deletion can never score: the same blindness that hid R7. The README's "the acts GRANT these" applies equally to `contract` (R15), which was flagged anyway; the asymmetry is unexplained. |
| coverture chain R6 `leave w`; police R4, cps R10, airline R4, companion R6 `leave` | implicit `may leave when true` (R8/R9/R5/R12) | **liberty** (the README's own words: "the physical possibility of leaving is always there") | liberty encoded by the *older* convention, an implicit universal `may`. Two encodings of one concept now coexist; they differ for the ablation (an implicit may is a deletable row with a `~prohibit` variant, a flag is not). |
| kibbutz R4 `sleep_home` when true | R7 implicit may when true | **liberty** (a child sleeps at home by default) | implicit-may convention |
| footbinding R9 `refuse_binding` when is_subject | R8 implicit may when true | **liberty** (refusing is the default) | implicit-may convention |
| companion R11 `sue a` when true (animal) | none | power: animals have no default standing; the explicit prohibition is a personhood statement | power. Faithful, but note the README rule as worded ("withholds by prohibition") matches it; the rule needs "by default for that kind of agent". |
| companion-ownership/renamed R9 `reassign court` when true | guardianship R9 `may reassign when ...` | power (judicial reassignment is conferred) | power. Faithful. |
| crisis-team R4 `detain`, R6 `carry_weapon` when true | R8 implicit may detain when responding and danger | power (detention is conferred on a role) | power. Faithful. |
| mwpa R11 `attach c w` | R10 implicit may attach when married | power (attachment is a creditor's legal remedy) | power. Faithful. |

Conclusion: applying the README rule consistently makes `sue` a liberty in the coverture chain and `leave`,
`sleep_home` and `refuse_binding` liberties everywhere; the dataset encodes all of those by implicit `may ... when
true` and flags exactly the one action that missed. Nothing here makes a committed verdict wrong (every row still
reads as expected), but the dataset now carries two conventions for one idea with no stated rule for which to use.
One consequence should be said plainly: an implicit `R: wife may contract when true` (the existing convention, as
used for `leave`) would have produced the same `cannot_contract` flip on R7 deletion, the same zero layer-1 blast
radius, and the same 5/5, with no engine change at all. The engine change is justifiable (a flag does not add
ablation rows; the global flip was rightly rejected) but the record does not say why the convention was not used.

**Not a liberty but worth a line:** `keep_earnings`, `hold_property`, `control_property` are left nameless under
coverture and the README says "the acts GRANT these". For `hold_property` that is partly wrong under Blackstone: a
feme sole holds property by default and coverture passes it to the husband; the MWPA restored, not granted. The power
reading survives only because `financial_dependence` was preregistered and the global experiment showed it flips
under the liberty reading. That is a reason to keep it a power for now, and a reason to record it as a known
unfaithfulness, not as settled.

## 5. Is "rediscovery 5/5" over-claimed? [amber, leaning red on the disclosure]

Yes. Plainly: this is instrument tuning. The sequence is miss (rev 2, 14:33) -> diagnosis of the engine's blind spot
on that item -> experiment on the full dataset -> preregistration of a semantics that, by construction, turns that
item into a hit -> run. The fix was applied to exactly one action, the one needed for the hit, although the author's
own rule reaches `sue`, `leave`, `sleep_home` and `refuse_binding` (section 4). Prediction 3's "the revision-2 miss
turns into a hit" could not have failed short of a coding error. Tuning a known blind spot on a known-answer item is
legitimate calibration, but a calibrated hit is not evidence; it is a check that the instrument now does what it was
just told to do.

The score history is 1/5 (v1, blind) -> 4/5 (rev 2, after seeing the misses) -> 5/5 (rev 3, after seeing the miss).
The record keeps all three numbers, which is to its credit. The disclosure in the rev-3 results is not sufficient:
the commit message says "(5/5, no drift)", the table says "Drift: none", and the "Honest limits" paragraph discloses
only that the flag is an encoder's judgment and invites review of the flag. It does not say that the fifth hit was
produced by a semantics change motivated by the miss, that the change was applied to that action alone, or that the
headline number is therefore 4 blind + 1 engineered. docs/claims.md M4 ("expectations are written before runs") is
already "weakened"; this entry belongs on it.

## 6. The cache-key gap [red on the diagnosis, green on verdict impact]

Refuted as stated. `rules_cache.make_key` hashes `"institution": inst.model_dump(mode="json")`, and
`InstitutionJSON.expected_properties` is a field (schemas_rules.py:159), so adding an expected property changes every
cache key for that entry. Row selection is also not cache-dependent: `run_all` builds `which` from
`inst.expected_properties` on every call and appends a row per (property, check) whether the verdict came from the
cache or z3 (rules_checks.py ~322-370). On HEAD I get 123 rows cached and 123 uncached, identical sets, identical
verdicts. Whatever produced the author's 116 was not the cache key omitting expected properties; the seven "missing"
rows are exactly the twin-formal properties (`dependent_cannot_exit` and `subject_cannot_exit` share a formula, and
property keys are formal-text based, see the `res.property = name` comment at ~line 352), which suggests the 116-row
artefact was a saved earlier output or a report assembled elsewhere, not a live cached run. The author should find
what the 116-row file actually was before filing an "engine fix needed". No committed verdict is affected: verdicts
agree where both report (author's statement) and in my run everywhere.

## Verdict: weakened

The engine change is small, correct, and the two lowerings agree; the preregistration precedes the code and was not
edited; layer 1 is unchanged on HEAD as predicted. It is weakened because (a) the 5/5 is a calibrated hit reported as
a blind one, with insufficient disclosure; (b) the flag was applied to the one action that missed while the author's
own rule reaches four others encoded by a different convention, so the dataset now has two encodings of one concept
chosen per action; (c) the ABM reads the changed `power()` and the frozen layer-2 record is no longer guaranteed to
reproduce, unrecorded; (d) the cache diagnosis written into the results file is wrong on the evidence in the code.

## What the author must decide

1. Rewrite the rev-3 result line everywhere it appears (commit message cannot change; results file, claims.md M4,
   any summary) as "5/5 after a semantics change motivated by the rev-2 miss; 4/5 blind at rev 2, 1/5 at v1", and
   stop citing 5/5 as rediscovery evidence. Decide whether the rediscovery test is now a calibration fixture (then say
   so and retire it as a claim) or whether a fresh, untouched entry set is needed for any future rediscovery claim.
2. One convention for default capacities. Either (i) flag `sue` (coverture chain), `leave` (six entries),
   `sleep_home`, `refuse_binding` as liberties and delete the implicit universal `may` rows, or (ii) un-flag `contract`
   and give it the implicit `may contract when true` that `leave` has. Either way, preregister the layer-1 blast
   radius and the ablation deltas first (R4 `sue` will start to score in the coverture chain under (i); the
   implicit-may rows vanish from the ablation denominators). Record in the README why a flag rather than an implicit
   may, since the two are not equivalent for the ablation.
3. Rename `liberty` or fix the ADR gloss: the mechanism is "default capacity vs conferred power", not Hohfeld's
   liberty/power. Add "by default for that kind of agent" to the README rule so companion R11 does not match it.
4. Decide, and pin with a test, whether a sanctioned `must_not` on a flagged action bars its derived power. The ADR's
   own gloss says yes; the code says no.
5. Record the ABM effect in ADR 0013 amendment 3 and plans/layer2-abm.md; fix abm/model.py docstring line 8; either
   rerun the gate sweep on the seven coverture-chain entries and record the diff, or show that `contract` is never
   drawn.
6. Withdraw the "cache key omits expected properties; engine fix needed" finding, or reproduce it with the actual
   116-row artefact named. Until then the results file carries a wrong diagnosis.
7. Note `hold_property` as a known unfaithful power reading (feme sole held property by default; the MWPA restored
   it), kept because the global experiment showed `financial_dependence` would flip. A known deviation recorded is
   fine; an unrecorded one is not.
8. Fix the date labels: headings say 2026-11-05, commits say 2026-11-04 local. State the convention.
