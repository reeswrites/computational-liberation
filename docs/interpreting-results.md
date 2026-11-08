# Interpreting engine output

For anyone who will see `phil rules ...` output and must not over-read it. Output below was run 2026-11-03 (z3 4.15.4, k=6). ADRs 0003, 0004, 0009, 0013 are in philosophy-engine `docs/decisions/` (`../philosophy-engine/docs/decisions/` when checked out as a sibling); 0010 is in `docs/decisions/` here.

## 1. What a check answers

A check answers one question: given this encoding, what do the rules permit or force within 6 steps? That is entailment under an encoding, not prediction (ADR 0004). Results use the verbs "permits", "forces" and "open". Frequency and uptake are not modelled. Every output footer says `'open' means not reached within k, never 'safe'` (ADR 0003). README: a verdict "is a statement about the encoding, not about the institution."

## 2. The verdicts

| Verdict | Real output line | A careful person may say |
|---|---|---|
| reachable | `police-crisis  subject_cannot_exit  reachable  reachable  reachable` | The encoded rules permit a compliant trace in which the subject cannot exit. Not that it happens. |
| open | `police-crisis  no_standing  reachable  unreachable_open  open` | No trace found within 6 steps. Say "open"; never "safe" or "impossible". |
| holds_to_k | `coverture-household  care_and_sanction_same_role  invariant  holds_to_k  holds_to_k` | Every compliant trace up to step 6 satisfies it. Nothing beyond 6. |
| violated | `crisis-team  care_and_sanction_same_role  invariant  violated  violated` | Some compliant trace breaks it, and a counterexample exists (`--trace`). |
| persists | `kibbutz-childrens-house  care_assigned_by_sex  persists  persists  persists` | Once true, it stays true within k. |
| fails | `cps  no_standing_persists  persists  fails  fails` | Some compliant trace has it true, then false. |
| inconsistent | `police-contra  subject_cannot_exit  reachable  inconsistent  inconsistent` (scratch variant: I added a `must` and a `must_not` of `provides_care` on `true`; not in the dataset) | The rules admit no compliant trace at all, so every property is meaningless. |
| inert | `police-inert: inert R11: must (provides_care o s) when ...: no compliant trace of the other rules breaks it within k=6` (scratch variant: a duplicate of R2) | A must-be rule nothing can breach within k. It constrains nothing, so its "load-bearing" status is unearned. Gate (a) fails on an inert rule marked `load_bearing` (ADR 0013). |
| vacuous | `police-no-power  care_and_sanction_same_role  invariant  holds_to_k  holds_to_k  yes  vacuous,antecedent-unreachable` (scratch variant: police-crisis minus R3 and R5) | The `holds_to_k` is true only because the antecedent never occurs; nobody holds sanction power. A `no-subject` flag is the other case: no subject ever exists. Read a flagged `holds_to_k` as no information. |

`match: yes` means agreement with a preregistered expectation, not a judgment of the institution. `check-all` reported `agreement: 47/47 = 100%`, but claims L15 and M4 record expectation edits after runs, so that is weaker evidence than it looks.

## 3. Isomorphism

`iso` compares canonical rule skeletons under a role and predicate bijection (glossary), reports what matched and what did not, and is never moral equivalence. Two switches:

- **Level.** `exact` compares conditions literally; `guard` reduces them to conditional or unconditional. At exact, the care+control trio shares no rule (ADR 0010). The level is precommitted per claim, and a pass at an unplanned level is a finding, not a gate pass (ADR 0010).
- **Strands.** `--with-strands` adds the human-assigned tags (rival, superadditive, tying) to the skeleton.

Real output, coverture vs police, guard level:

```
coverture-household ~ police-crisis: iso=False ... matched=6/9|10 strands=off cond=guard
coverture-household ~ police-crisis: iso=False ... matched=5/9|10 strands=on cond=guard
  care+control: care R2:(provides_care h w) ~ R2:(provides_care o s); control R5:(chastise h w) ~ R3:(detain o s); exit_bar R6:(leave w) ~ R4:(leave s); ... sub-signature 5/9|10 rules (50%)
```

`iso=False` throughout: the institutions are not isomorphic. The gate calls this `partial(care+control)@guard+strands`. That licenses: "a sub-signature of three legs (a care duty, a control permission on the same subject, an exit bar) lines up, about half the rules, with the remaining four and five rules unmatched." It does not license: "they are the same institution", "one explains the other", or any claim about outcomes.

**The airline control.** `airline-flight` also matches at guard+strands (`coverture-household ~ airline-flight ... matched=5/9|6 strands=on cond=guard`, with a care+control line). The dataset README calls it a deliberately preregistered expected match, structural (in-flight custody). So the match detects form (care, control, exit bar on one subject) and is theory-neutral: it cannot tell oppression from a seat belt sign. README: retagging the airline care rule from superadditive to tying removes every match (the reviewer's run, reported, not repeated here), so the strand tags are load-bearing.

**Strand and implicit tags are human inputs reported back.** The engine does not find care, control or implicitness (README). Claims L11 (refuted) and L1 (weakened) record this.

## 4. The gate

`gate --verbose` prints `GATE PASS (deferred criteria do not fail the gate)`. A pass proves only the following.

- **(a)** All institutions load (23 at 2026-11-04); no load-bearing must-be rule is inert.
- **(b)** The care+control trio matches at its precommitted level and `lease` and `public-library` do not, and the crisis team matches nothing. Not that the engine found the care/control line itself, and not that the controls are enough: `airline-flight` is excluded from the control list because gate (b) cannot hold an expected-match mode (dataset README).
- **(c)** The minimal pair is one rule apart (`paternity-quota:R2 vs transferable-leave:R2`) and differs on the named property.
- **(d)** `care_assigned_by_sex` persists with implicit R2 and fails without it; R2 is the one separating rule. Not that the engine detected implicitness.
- **(e)** Agreement against expectations (115/115 at 2026-11-04; minimum 60%). See the caveat in section 2.
- **(f)** Rename is detected (`companion-ownership ~ companion-guardian-renamed: iso=True pure_rename=True`) and guardianship is not ownership (distance 1).

Read the "findings (true, not counted)" under the verdict first.

Failure modes. Anywhere this guide or a gate letter refers to "the failure modes" or to DT/DI/BL/RB as the full set, read the eleven modes on three axes (who pays / rule / time) in `docs/decisions/0016-failure-mode-axes.md`, not a closed list of four. DT, DI, BL and RB are its "who pays" axis. Each mode carries the lowest layer that can detect it; layer 1 can only fire Capture, Cosmetic and Backlash when the reaction is encoded as a branch (MWPA `narrowed`, which adds rules R17 and R18; its 2026-11-03 relabel to Erosion was reverted by the ADR's 2026-11-04 amendment). Erosion is practice drift and needs layer 2.

Standing caveats (ADR 0016). Two things the model cannot see apply to every result and are not modes. Illegibility: a rule that conditions on a fact the state cannot observe (Scott) is encoded as if the fact were visible. Encoding misread: a constitutive strand encoded as tying makes unbundling look free; the council's encoding-faithfulness axis exists to catch it, and the engine cannot.

## 5. Three worked readings

**Coverture vs police.** The output in section 3. Sayable: under these encodings both give one party a care duty, a control permission and an exit bar over the same subject (husband maps to officer). Not sayable: that policing is coverture.

**Paternity quota vs transferable leave.** The pair differs by exactly one rule (R2, distance 1). On the property preregistered in the plan (`solo_care_by_non_birthing_parent`) both read `reachable`, so it did not separate them. `leave_reserved_for_non_birthing_parent` was chosen after seeing both verdicts: gate (c) says `post hoc leave_reserved_for_non_birthing_parent: differs`, and the lines read `holds_to_k` (quota) and `violated` (transferable). Sayable: the one rule changes whether reserved weeks can be taken by another; the property was picked post hoc and the original did not separate the pair (dataset README, gate findings).

**Kibbutz pair.** Output: `kibbutz-childrens-house care_assigned_by_sex persists` vs `...-no-implicit ... fails`. The one rule carrying the outcome is R2 (`implicit rule flagged: R2`). Qualifications (dataset README, L6): "implicit" is a tag the encoder wrote, and the engine reports it back (setting `implicit: false` changes no verdict); the ablation bites only because R1 was written sex-blind; the sources support a practice, not a written rule, which is why R2 is encoded as a sanctioned norm (`must_not`, or_else R6). Gate (d) reads strict compliance. Sayable: given this encoding, removing R2 is what lets assignment become sex-blind within k.

## 6. Red flags for a reviewer

- Power asserted in effects rather than derived from rules (ADR 0013): a power that survives deleting its rule can't tell a rule set from its paraphrase.
- Expectations edited after runs, or properties swapped after seeing verdicts without a "post hoc" mark (M4, L15).
- Iso level chosen after the result (ADR 0010); a match reported with no level, or without `--with-strands` stated.
- Negative or expected-match controls missing (airline, lease, library); a cluster claim with no control.
- Flags ignored: vacuous, `no-subject`, inert, inconsistent, or `open` read as safe.
- Tags cited as findings rather than inputs; forward claims about a real institution instead of "the encoding permits/forces".

## 7. What the engine can and cannot find

Written 2026-11-07 after the question "can this find new liberation paths, or does it only nail down specifics?" Both, through three mechanisms, and the limits are worth stating before the claims table.

**Nothing comes out that was not put in.** The engine cannot propose a rule, a gate or an institution that no entry encodes. Its outputs are combinations and comparisons of the encodings. A surprising verdict is a combination the author did not hold in mind, or an encoding error; the council decides which, and so far every surprise on record has been the second kind (prohibit-variant leak, deregulation zeroing a power, exit twins double-counted; see plans/priority-slice1-results.md). The blind rediscovery hit 1 of 5 preregistered top rules (L21). Read together: intuition about which rule carries the load is unreliable even for a careful author, and the engine's first return is forcing that intuition to be written down and checked.

**Where novelty can come from, in order of how much the repo already has:**
- *Cut sets.* A minimal set of rules whose removal flips a freedom property is a path. When it is not the obvious set, it is a path nobody saw. Bounded by the encoded rules; still more than a person holds in mind at twenty rules.
- *Isomorphism as an analogy library.* If entry A matches entry B at the rule level and history records a move that worked on B, that move is a candidate path for A. The engine proposes the transfer; the human did not have to think of it. docs/connections.md C1–C4 preregister this for guardianship against coverture. Every faithfully encoded historical case adds a known move; every match is a proposal.
- *Recombination through composition* (plans/composition.md, not built). Institutions that never existed, built from rules that did. Selection and arrangement of grounded pieces, not blank-page generation.
- *Edit search* (not built, riskier). Enumerate single-rule edits beyond delete and prohibit, such as reattaching a condition from `married` to a designation, and report which flip a freedom without costing a good. Bounded edit types only; it generates nonsense otherwise.

**Where the thinking happens.** Mostly in the encoding. Writing "who counts as family at the hospital, sanctioned by whom" as a rule with a source is where the encoder finds out they do not know. The engine then refuses vagueness. That is the main return in any first slice; cut sets are the second; sequencing over endpoints is not a return until a dynamics layer exists (plans/dynamics-sticks.md).

**Limits to state up front:** one agent per role, no counts, no distributions; no time; k-bounded search; hand tags the verdicts depend on (strand; see the parked redesign); faithfulness of the encodings (L24: 24 of 211 rule rows unfaithful on the card-only pass). The honest tally and the preregistration rule are what make the claims believable, and saying the limits first is part of that.

**Surprise ledger.** Until there is a place where "the engine saw something the author did not" is recorded as such, nobody can tell when it first happens. docs/surprises.md holds one row per unpredicted flip, with the council's ruling: artifact or finding. The ledger starting empty of findings is itself the current result.

## 8. Reading absorbed, displaced and no backstop found

Written 2026-11-08 for the informal-rules layer (plans/informal-rules.md D3). These three words are readings of an ablation row on a composite, not engine verdicts. The engine prints the same six verdicts as always; the reader pairs two properties and looks at how each moves when one formal gate rule is deleted.

| Reading | What the row shows | What may be said | What may not |
|---|---|---|---|
| absorbed | the property a formal gate carried holds exactly as before after the gate is deleted, and the rule now carrying it is tagged `kind: norm` or `strategy` | the encoded informal rule does the same job for the same people | that the norm would hold up over time, or that anyone follows it: `kind` and `sanctioner` are hand tags (D1) |
| displaced → to whom | the guarantee is lost (an invariant goes `holds_to_k` → `violated`) while the good stays possible (a `reachable` stays `reachable`), or the good holds only for a narrower attribute set, or the remaining carrier has a different `sanctioner` | who lost the guarantee, and which rule, tagged how, now gates the good; the hospital case reads: the spouse loses the guarantee that rode on marital status; staff discretion (institution) and the patient's designation (state) now gate it | a rate: one anecdote of a denial is not a compliance figure, and the engine has no frequencies |
| no backstop found | both properties move: the guarantee is lost and the good becomes unreachable within k | nothing in this composite carries the good once the gate is gone | "sticks": whether a norm grows back is a time question the static layer refuses (plans/dynamics-sticks.md) |

Three things to check before using any of the words. First, whether the gate carried anything: a formal rule whose deletion flips nothing is not absorbed, it was redundant under strict compliance (a sanctioned `must_not` beside a narrower permission is the usual case; `(enabled ...)` also ignores sanctioned prohibitions, so a power fluent cannot see a norm, which is why the visitation properties read the admission itself). Second, k: `unreachable_open` after the deletion may mean the remaining route is longer than k, not absent; run k = 8 as well and say which. Third, who the "to whom" names: the attribute set is read from the property's quantifier and the roles the surviving rule binds, both of which are on the card, not inferred from the rule's prose.
