# The worth-it slice: one small test of whether the solver earns its keep

Status: PLANNED 2026-11-09, **top priority, not started**. The author's framing: "a path where we can validate as we go, or build a slice, to see if this repo / idea is actually worth anything." Run this before anything else in docs/plan.md. It is steps T1a and T1c of plans/direction-tests.md cut down to the minimum; the rest of that file is backlog until this reports.

## The question

So far the value has come from the discipline (writing rules down; seats attacking them), and the solver has mostly confirmed predictions. This slice asks one thing: **does the solver tell us something the encoding process did not already tell us?**

Budget: one to two working days. No new engine slice. If it runs past three days, stop and report why; that is itself an answer.

## Part 1. Can it see the pattern at all? (sensitivity)

**Entry:** `voting-devices`, a bundle where the record says the rules had to go together. Candidate rules, each to be sourced under the provenance rule (`opened` needs an accessed date and a verbatim excerpt); none is verified in this file:

| Device | Struck by (to verify) |
|---|---|
| grandfather clause | *Guinn v. United States* (1915) |
| replacement registration window | *Lane v. Wilson* (1939) |
| white primary | *Smith v. Allwright* (1944) |
| poll tax | Twenty-fourth Amendment (1964); *Harper v. Virginia Board of Elections* (1966) |
| literacy test | Voting Rights Act of 1965, section 4 |
| preclearance of new devices | Voting Rights Act of 1965, section 5 (a rule about rule changes: declare as a gap, do not work around) |

**Properties, written before the rules:** `cannot_register` (a qualified citizen of the barred class cannot reach `registered` within k) and `cannot_vote_in_deciding_election`. Two is enough.

**Method:** the tools on main (`phil rules ablate`, `phil rules transfer`) plus one small script, `scripts/cut_sets.py` (about 60 lines): for every subset of the entry's rules up to size 4, write a copy of the entry with those rules removed, call `rules_checks.run_all` in-process with the result cache, and record the verdict vector. From that table read off (a) minimal sets whose removal flips a property, (b) whether any intermediate state raises another rule's load.

**Preregistered before the run** (plans/_templates/preregistration.md):
- no single deletion flips `cannot_register`;
- the minimal flipping set is all the sufficient devices together;
- transfer edges exist between the devices.

| Outcome | Reading | Next |
|---|---|---|
| all three hold | the method can see substitution | go to part 2 |
| the minimal set is right and no transfer edge appears | cut sets work, the load measure does not | part 2 using cut sets only; note the load measure for redesign |
| no single-deletion result and no cut set | the method cannot see the thing the thesis is about | **stop.** Write it up; sequencing work is abandoned as designed |

**Guard against rigging.** The encoder knows this history, so part 1 can only show sensitivity, never validity. To keep it honest anyway: the entry is encoded by a fresh subagent given the opened texts and the README conventions, not this file or the hypothesis; properties and the prediction are committed before that agent starts; the card-only seat reads the result.

## Part 2. Does it say anything we did not already know? (the real test)

**Entry:** `coverture-household`, already on main, already reviewed. It has ten properties and three rules whose single deletion breaks the cluster match (R2, R5, R6), so it is the entry most likely to have structure.

**Before the run, the author writes down, in two minutes, what they expect:** which rules must go together for a wife to stop being financially dependent and to be able to contract, and in what order they would cut. Saved verbatim as `plans/worth-it-author-expectation.md` and committed. This is what makes "non-obvious" checkable.

**Run:** the same `scripts/cut_sets.py`, all subsets up to size 4, properties `financial_dependence`, `financial_dependence_unpropertied`, `cannot_contract`, `subject_cannot_exit`.

**Output:** one page. Minimal must-go-together sets per property; any cut that makes another rule more load-bearing; any order that reaches a different end state than another order.

**The judge is the author**, with three questions:
1. Did the tool say anything that is not in your written expectation?
2. If so, is it true of coverture as you understand it, or an artifact of the encoding? (The faithfulness seat checks any claimed artifact against the sources.)
3. Would you act differently, or argue differently, knowing it?

| Outcome | Reading | Next |
|---|---|---|
| at least one claim is new, true, and would change an argument | the solver earns its keep | adopt plans/direction-tests.md as the roadmap; every later bundle gets this same treatment and a hit-or-miss row in docs/scoreboard.md |
| claims are new and turn out to be encoding artifacts | the tool is finding its own encoding, not the institution | one more bundle with a second encoder before deciding |
| nothing beyond the written expectation | the repo is a careful rule-writing practice, not a tool that computes anything | stop engine work; write up what the practice is good for; decide whether to keep it as that |

## Validate as we go, if it passes

Each new bundle after this follows the same four steps and adds one row to a hit-or-miss table: author writes expectation; encode; run cut sets; compare with the expectation and, where one exists, the recorded order of reform. The project continues only while that table keeps earning rows the author calls new and true.

## What pauses until this reports

SSI revision 3, companion-ownership R4 typing, P2c, the prohibit-variant graph, slice 4 as an engine feature, the second encoder, two-wife and poly, marriage batch 2, and the dynamics decision. All are recorded in docs/plan.md and plans/direction-tests.md and lose nothing by waiting.

## Needed from the author before it starts

1. Yes to adding the `voting-devices` entry (it is not among the six entries in plans/race-entries.md).
2. Two minutes to write the part 2 expectation, before the run.
