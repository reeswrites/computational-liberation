# Direction tests: what to run to find out whether this approach can reach the goal

Status: PROPOSED 2026-11-09, at the author's request ("whatever would help us achieve our goal or rule out bad directions / show good directions"). Nothing here is run or preregistered. Each item still needs its own preregistration; items marked **needs ruling** need the author's yes first.

## Why this file

The goal (docs/plan.md) is to say which change to make first and what it sets off. After today the project has a well-calibrated layer 1, one goal-shaped result (slice 3, a null on a thin sample), a frozen layer 2 with two honest gate failures, and 29 `untested` rows in docs/negative-results.md. The risk is not error; the process catches errors. The risk is spending months polishing a method that cannot answer the question. So the next work should be chosen by **decision value**: for each item, what would we do differently depending on how it comes out.

## The five questions, in the order they block each other

### Q1. Can the method see load transfer at all? (sensitivity)

Slice 3 found no transfer edge on seven entries. That is uninformative until the method has found transfer somewhere transfer is known to exist. Today the only positive is a constructed toy.

- **T1a. Real positive control: disenfranchisement devices.** **needs ruling** (new entry; race entries are parked in plans/race-entries.md and this is not one of the six named there). The historical record is the textbook case of rebundling: several devices each sufficient to bar registration, struck one at a time, with another carrying the load each time, until one statute removed them together and added a rule against replacements. Candidate rule set, every item to be sourced under the provenance rule and none verified here: grandfather clause (struck in *Guinn v. United States*, 1915) and its replacement registration scheme (*Lane v. Wilson*, 1939); white primary (*Smith v. Allwright*, 1944); poll tax (Twenty-fourth Amendment, 1964; *Harper v. Virginia Board of Elections*, 1966); literacy test and the preclearance rule (Voting Rights Act of 1965, sections 4 and 5).
  - Preregistered expectation: every device is a substitute carrier of `cannot_register`; deleting any one leaves the property holding and raises the load of the others (transfer edges); the minimal must-go-together set is all of them.
  - **If found:** the method is sensitive; nulls elsewhere mean something. Slice 4's sequencing output can be compared with the recorded order of the cases (a static ordering backtest, see Q4).
  - **If not found on an honest encoding:** the load measure (flip counts over a few properties) cannot see substitution. Stop slices 4 and 5 as designed and redesign the measure before any further encoding work.
  - Known limit to state up front: preclearance is a rule about rule changes, which the grammar lacks (plans/domination-predicate.md). Encode it as a declared gap, not a workaround.
- **T1b. Prohibit-variant transfer graph** (ruled 2026-11-09). Widens the denominator on existing entries. Run it on the positive control too.
- **T1c. Slice 4 on multi-carrier entries** (ruled 2026-11-09): coverture-household and the two composites, plus the positive control if T1a is approved.

**Gate G1 (after T1a to T1c).** Three outcomes, each with a different next step:

| Positive control | Care / marriage entries | Reading | Next |
|---|---|---|---|
| structure found | structure found | static sequencing works and the thesis has support at layer 1 | Q4 static ordering backtests; then decide on dynamics |
| structure found | none | the method works and these institutions do not rebundle as encoded: a real finding against "simultaneous where possible" for them | write it up; check encoding granularity once (Q3) before believing it |
| none | none | the method is insensitive | redesign the load measure; freeze new entries |

### Q2. Are the results the encoder's or the institution's? (encoder dependence)

Every encoding and every second encoder so far is the same model family (N17, N60). If a different encoder produces different ablation rankings from the same sources, every ranking in the project is an artifact, and no later slice is worth running until that is fixed.

- **T2a. Non-Claude second encoder on three entries** (procedure already in data/institutions/goods-encoding/r3/prompt-api.md; needs an API key from the author). Entries: one MWPA entry, kibbutz-childrens-house, ssi-marriage-penalty. Measure: verdict agreement on shared properties, and rank agreement of rule loads.
  - **If rankings agree:** proceed; record the agreement as the first evidence that rankings are not encoder-specific.
  - **If they diverge:** slice 5 (the disagreement locator) moves ahead of slice 4, because locating why encoders differ becomes the main instrument.
- **T2b. One human reviewer who lives or has lived under an entry's institution** (ADR 0012). Not schedulable by an agent; listed so it is not forgotten. SSI is the most reachable.

### Q3. Are the verdicts artifacts of the bounds? (horizon and granularity)

- **T3a. Step-bound sweep.** Rerun the 192-row baseline at k = 6, 8, 10 and record every verdict that changes (N15). The check set now takes seconds warm, so this is cheap.
  - **If nothing changes:** k = 6 stands, with evidence. **If rows change:** those properties are horizon-sensitive and must be flagged before any ablation ranking uses them.
- **T3b. Property-density probe.** Load is a count of flips over the properties an entry lists; an entry with five properties cannot rank ten rules. On one entry (coverture-household), add the already-written goods properties and count how many ordered rule pairs can then carry a ranked edge. This says whether the slice 3 denominator problem is fixable by properties or is structural.

### Q4. Is there a route to validity that does not need the frozen dynamics layer? (layer 3 without layer 2)

The roadmap rule is no forward claim until blind backtests pass. Two obstacles: backtests were parked with layer 2, and an encoder that has read the history cannot be blind to it (project memory: rediscovery is calibrated, not blind).

- **T4a. Static ordering backtest.** If slice 4 produces a sequencing for a bundle whose reforms happened in a recorded order, compare the two. Candidates: the positive control (order of the cases), and MWPA across states (which act came first where; needs Geddes and Tennyson 2013 opened, N59). This is an ordering prediction, never a curve fit, in the spirit of plans/dynamics-sticks.md.
  - **If the predicted order matches better than a stated chance baseline:** first validity evidence, obtained at layer 1.
  - **If not:** sequencing output is structure without predictive content; say so in docs/claims.md.
- **T4b. Sealed prediction registry.** **needs ruling** (it sits close to ADR 0004's no-forward-claim rule). For reforms whose outcomes are not yet observable, record a dated, hashed structural prediction (who loses a guarantee, displaced to whom, which rule becomes load-bearing) and do not publish or act on it. Score it when the outcome exists. This is the only test in which the encoder cannot have seen the answer. A sealed prediction is not a claim; the registry would say so on its first line.
- **T4c. The two preregistered, never-encoded controls:** gig platform (dark twin: cheap exit, no insurance, no voice; N11) and Ostrom fishery (users can revise the rules; N12). Both are layer 1 and both test who-pays modes that currently have no entry.

### Q5. Should the dynamics layer reopen? (what it sets off)

Do not decide now. Decide at G1 with this rule:

- Reopen only if G1's first row holds **and** slice 4 shows that order matters (two cut sequences reaching different end states or different intermediate loads). Then the question dynamics answers, path dependence, is known to exist statically, and the gate in plans/dynamics-sticks.md (Loving, same-sex marriage, ordering only) is the price.
- If order never matters statically, reopening layer 2 would be building a simulator for a question the static layer says is empty. Leave it frozen and say why.

## Proposed order

| Step | Items | Cost | Blocks |
|---|---|---|---|
| 0 | T3a step sweep; rename the transfer check (ruled) | hours | nothing |
| 1 | T2a second encoder | a day once a key exists | author provides key |
| 2 | T1a positive control (if approved), T1b prohibit graph, T3b density probe | a batch each | T1a needs ruling and sourcing |
| 3 | T1c slice 4 | one engine slice | steps 0 and 2 |
| G1 | read the table above | | |
| 4 | T4a ordering backtest; T4c two control entries; T4b registry if approved | batches | G1 |
| 5 | Q5 dynamics decision | a ruling | G1 and slice 4 |

Track B (SSI revision 3, companion R4 typing, P2c) continues beside this; it does not gate any step here except that composites used in slice 4 should be on the revised SSI entry.

## What this plan deliberately leaves out

- The untested theory claims T2, T3, T4, T6 to T10 (N19 to N26). Most need either new institutions or dynamics; planning them before G1 would be planning on an unknown.
- Marriage batch 2, two-wife and poly. They enrich the dataset and none of them tells us whether the method works.
- The unread sources (N57 to N59) except Geddes and Tennyson, which T4a needs.

## Stop conditions for the whole approach

Recorded so they are decided before the results are in:

1. Third row of the G1 table (no structure on a real positive control): static sequencing as designed is abandoned; the ledger gets an `abandoned` row and the project turns to redesigning the load measure.
2. T2a divergence that slice 5 cannot localise to specific rules: rankings are withdrawn from docs/claims.md until a second encoder agrees.
3. T4a no better than chance on two bundles: the project says plainly that it is a theory-checker with no validity evidence, and stops describing sequencing output as guidance.
