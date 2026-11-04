# Parked: domination predicate (handoff, received 2026-11-05)

Status: PARKED. Author: "doesn't have to be right now but something to keep in mind." Not started. Sequencing: after the ablation slices in plans/priority.md; needs the voice/collective-choice extension the README lists as a dataset gap ("Rules for changing rules"), so it should land with that encoding rather than before it.

Coordinator note: leg 3 (no voice over the rule granting the power) requires a rule whose object is another rule; neither the grammar nor the dataset has one as of 2026-11-05. Leg 2 "exit costly" has no cost model at layer 1 (exit is a disability or not); ordinal exit stays a TODO unless layer 2 is unfrozen. The three claims below must be preregistered in docs/claims.md and committed before the predicate runs over data/institutions.

## Handoff text, verbatim

# Handoff: domination predicate (philosophy-engine + computational-liberation)

## Context
From a conversation about anarchy ≠ "no rules." The anarchist distinction is between
authority/rules (fine) and domination (not fine). The engine already derives power
fluents from rules (an actor can sanction only if some rule enables it) and has a
three-leg care+control+exit-bar match. This adds a sibling predicate for domination.

## Definition
A dominates B iff all three legs hold:
1. **Power**: some rule enables A to sanction or control B (use existing derived power fluents).
2. **No exit**: B is barred from leaving, or exit is costly.
3. **No voice**: B has no collective-choice position (propose/vote/veto) over the
   rule(s) that grant A that power.

Output per pair: each leg separately, plus a verdict:
`dominates` / `authority-without-domination` / `no-power`.
Exit should be graded (ordinal none/low/high) if the encoding supports it; otherwise
boolean with a TODO.

## Build
- Mirror the care+control match: same module, reporting style, test conventions.
  Likely lives in the engine (generic pattern check); justify if not.
- If the grammar can't encode "who can change a rule," add the minimal extension
  (e.g. a collective-choice rule whose object is another rule) plus a short ADR.

## Tests (small inline toy institutions)
- Conventional firm: boss can fire, exit costly, no voice → dominates
- Worker co-op: manager can discipline, exit costly, workers vote on rules/manager → authority-without-domination
- Open-source project: maintainer rejects, contributor forks cheaply → authority-without-domination
- Peer arrangement, no sanction rule → no-power
- Edge: voice over some rules but not the one granting power → dominates

## Claims register (computational-liberation/docs/claims.md), PREREGISTERED, not run
1. Which dataset institutions show zero domination edges at small scale, and which
   gain them as they scale or nest (federation joints).
2. Freeman effect: removing formal rules leads to informal sanction powers emerging
   (test later in the ABM).
3. Definitional choice: "anarchic institution" = has rules/authority but zero
   domination edges. Open to review.
Make predictions concrete enough to be wrong.

## Don't
- Don't run the predicate over data/institutions until the claims are committed.
- Send the council reviewer over it before anything is called a result.
