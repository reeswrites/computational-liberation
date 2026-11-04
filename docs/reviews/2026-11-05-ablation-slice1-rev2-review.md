# Correctness review: ablation slice 1 revision 2 (philosophy-engine 343a0e9 + 75fdd30) — 2026-11-05

Fresh agent, correctness seat (ADR 0014); not the builder. Read-only. Ran `pytest -k ablate` (20 pass, of which 19 in tests/test_rules_ablate.py) and `phil rules ablate --entry ectogenesis --k 6`; called `regulated_actions` on a prohibited fixture.

## 1. Findings 1-9 of the first review (docs/reviews/2026-11-05-ablation-slice1-review.md)

- F1 deregulation: **fixed** for deletions (`deregulated` flag, separate block, not ranked). The same artefact is **standing** for the prohibit variant (see 2).
- F2 derived powers: **fixed** by the same flag. The prohibit variant is exposed too, because `(enabled X)` still reads false once the action is unregulated.
- F3 orphan column: **fixed** (`orphaned_or_else` printed and stored). Strict mode ignores orphans, so it is harmless there.
- F4 z3 unknown: **fixed**. `z3_unknown` is set at rules_checks.py:149/160/171/343, and `effective_verdict` keys on the flag, not on message text.
- F5 signed flips: **fixed**, with a caveat. The UNFREEDOM list is a hand input. The ranking on `load_freedom_up` works, but see 3.
- F6 check-kind source: **fixed**. An explicit `check` key wins, and `check_sources` is printed. Caveat: the CLI marks only non-"expected" sources. `female_parent_care_persists` shows `[suffix]`, so its explicit `check: persists` is not read, because the key is not in `properties.json` for it. Harmless today.
- F7 stronger tests: **partly** (see 6).
- F8 summary file: **fixed** (`--summary`, with totals for uncounted and inconsistent_after). There is still no Spearman or 25-entry ranking table, and no non-zero exit when uncounted is above 0.
- F9 R5 property: **fixed in effect**. `care_duty_on_women` gives ectogenesis R5 `holds_to_k>violated`, load 1 up. R4 deletion reads 0 and R4's prohibit variant reads 0+1 down, so R5 is the top ranked rule. Reproduced both.

## 2. Prohibit variant

- **[red] It is not a clean upper bound, and `deregulated` is never computed for it.** Under strict compliance a `must_not` with `or_else` null is a hard disability. The action never fires while the conditions hold, and it overrides any other `may` on that action.
  - That makes the cut stronger than deletion under the conditions.
  - But `regulated_actions` ignores `must_not`. When the prohibited `may` was the sole regulator (R1 in the keeper fixture), the action leaves the regulated set ({exit, seize} becomes {exit}).
  - The action is then forbidden when C holds and always enabled when C is false. For a `may` with conditions other than `true`, that widens the action off-condition.
  - So the load can fall in either direction. `test_prohibit_variant_ranks_where_deletion_deregulates` asserts `not p.deregulated` only because the flag is never set on that branch.
  - Fix: compute `regulated_actions` on the prohibited institution and flag `offcondition_free` (or leave the row unranked). Or add a catch-all `may` with the negated conditions to keep the action regulated. State which in the ADR.
- The intent "overrides other regulators" makes it an upper bound for `may` rules with conditions `true` and a sole regulator. Elsewhere it is neither bound.

## 3. Families (`_fill`)

- `fam_all` takes any freedom flip. `fam_up` and `fam_down` are separate sets, so a family with one member up and another down **counts in both** `load_freedom_up` and `load_freedom_down`, and as 1 in `load_freedom`.
- **[amber]** Such a rule ranks (up>0) and is never tagged load-bearing, which hides the mixed effect. Fix: report `families_mixed`, and for twins that disagree in direction, flag it or take the net.
- A family's unsigned flips count only in `load_freedom_unsigned`, so they never rank.

## 4. `care_duty_on_women` grace

- **[amber] Faithful, but it exposes an unrecorded convention.**
  - ADR 0009 state obligations lower to C(t)=>F(t) at the same step. An action `must` (R5 `must provide_care`) fires at t and its effect lands at t+1. So the lag is the action/state split working as designed, not a hidden gap.
  - `care_assigned_by_sex` (female ⊒ provides) and `subject_cannot_exit_persists` (derived `can_exit`, same step) are implications over same-step state, so they never needed the grace.
  - Cost: the grace form is blind at the last step and for a child born at the final step. Its `properties.json` gloss still says "violated at any step where ... none yet cares", which contradicts the formula (stale text).
  - Fix: record the one-step-effect convention in the ADR, and correct the gloss.

## 5. "Load-bearing protection" label

- Sound only for non-deregulated rows. The label needs down>0 and up==0, and deletions that deregulate are excluded from ranking.
- **[amber]** It is still printed on deregulated rows, and on prohibit rows where the off-condition leak (2) could produce the down flip. R1~prohibit and R4~prohibit in ectogenesis (care_assigned_by_sex violated>holds_to_k) are legitimate, since R1/R4 prohibit leave R5 regulating. Fix: suppress the label when `deregulated` or when the prohibit leaks.

## 6. Vacuous tests

- The rename test is non-vacuous, and (a) now asserts non-zero. Remaining weak spots:
  - `test_e_k_disagreement_empty_when_ks_agree` can pass with an always-empty field, but the positive chain test covers that.
  - `test_ranking_ignores_down_flips` uses synthetic rows and does not run the pipeline.
  - `test_explicit_property_check_wins` ends with `"care_duty_on_women" in UNFREEDOM`, a constant membership check.
  - Nothing tests the orphan-sanctioned path, a derived-power fixture, a family where members flip in opposite directions, or the prohibit off-condition leak.

## 7. Preregistration

- **[amber]** Order: 05fb9cc (14:06, preregistration) then 75fdd30 (14:14, engine). The dataset change (`care_duty_on_women`, families, `check`) was uncommitted in computational-liberation at review time (committed after, 78f8f09). The preregistration named the property and the criterion ("R5>0, R4-prohibit 0"), but not the formula.
- The grace form was written after the plain form failed on the ectogenesis data. This is instrument tuning toward the preregistered target, since the dataset builder saw the failure first. It is disclosed in the README, which keeps it from counting as hidden tuning.
- The criterion itself did not change. The other four tops were not touched by the dataset edit.
- Fix: commit the dataset, and mark the formula as post-hoc in `plans/priority.md` (done at 78f8f09).

## Verdict: weakened

Findings 1-9 are mostly fixed and ectogenesis R5 now ranks, but the prohibit variant leaks (2), and the family and label semantics (3, 5) can mislead.

**What the author must decide.** How the prohibit variant should handle a sole-regulator `may` with non-trivial conditions: (a) keep an explicit catch-all permission off the condition; (b) flag and exclude such rows; (c) drop the prohibit variant for sole regulators and rely on deletion rows. Also: whether mixed-direction families count as up (as now), as both, or as neither; and whether the grace form is ratified with the one-step-effect convention written into the ADR. Then rerun with the preregistration stating the formula was post-hoc.

Coordinator's note (2026-11-05): fix pass takes (b) for the prohibit leak and "neither" for mixed families, both ASSUMED for slice 1; the author may revise.
