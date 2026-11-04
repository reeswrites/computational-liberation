# Priority slice 1: ablation results (25 entries)

Status: engine 343a0e9 (includes the fix pass). Run 2026-11-05, k=6 and k=8, 25 entries, 235 rules. Totals: inconsistent_after 0, uncounted 0, k-disagreements 0 (no rule changes verdict between k=6 and k=8 in any entry). Drift is recorded below, nothing tuned. Ranking uses `load_freedom` (unsigned: up plus down) over rules that are not deregulated.

## Preregistered vs observed (plans/priority.md, Decisions item 5)

| entry | expected | observed top (load, up+down) | expected rule's load | result |
| --- | --- | --- | --- | --- |
| coverture-household | R6 | R6 (3, 3+0) | 3 | hit |
| kibbutz-childrens-house | R2 | R4 (2, 2+0) | 1 (1+0) | miss |
| footbinding | R3 | R9 (2, 2+0) | 1 (1+0) | miss |
| mwpa-property | R11 | R6 (3, 3+0) | 0 | miss |
| ectogenesis | R5 | R4 (1, 0+1) | 0 | miss |

Score: 1/5. Loads are identical at k=6 and k=8.

## Full ranking (k=6; top ranked rule, load, deregulated-not-ranked / total rules)

| entry | top | load (up+down) | dereg/rules |
| --- | --- | --- | --- |
| coverture-household | R6 | 3 (3+0) | 4/9 |
| police-crisis | R4 | 2 (2+0) | 8/10 |
| cps | R10 | 2 (2+0) | 7/11 |
| crisis-team | none | 0 | 6/9 |
| paternity-quota | R1 | 1 (0+1) | 3/9 |
| transferable-leave | none | 0 | 4/9 |
| companion-ownership | R6 | 3 (3+0) | 7/12 |
| companion-guardianship | R6 | 3 (3+0) | 8/12 |
| companion-guardian-renamed | R6 | 3 (3+0) | 7/12 |
| lease | none | 0 | 3/5 |
| public-library | none | 0 | 5/6 |
| naming-convention | none | 0 | 2/2 |
| kibbutz-childrens-house | R4 | 2 (2+0) | 5/8 |
| kibbutz-childrens-house-no-implicit | R4 | 2 (2+0) | 5/7 |
| airline-flight | R4 | 3 (3+0) | 4/6 |
| mwpa-creditor-exemption | R6 | 3 (3+0) | 6/12 |
| mwpa-property | R6 | 3 (3+0) | 6/12 |
| mwpa-earnings | R6 | 3 (3+0) | 7/13 |
| mwpa-sole-trader | R6 | 3 (3+0) | 8/13 |
| mwpa-suit | R6 | 3 (3+0) | 7/13 |
| mwpa-property-narrowed | R6 | 3 (3+0) | 8/14 |
| footbinding | R9 | 2 (2+0) | 8/10 |
| footbinding-no-pledge | R9 | 2 (2+0) | 6/8 |
| ectogenesis | R4 | 1 (0+1) | 5/7 |
| gestational-surrogacy | R4 | 1 (0+1) | 4/6 |

No ties at the top in any entry. Five entries rank no rule above 0.

## What the misses say

Facts, then the reading.

(i) Exit twins. 17 of 25 entries have a top rule that flips both `dependent_cannot_exit` and `subject_cannot_exit` (reachable to open). The dataset README calls these the same form, so one prohibition on leaving counts twice. Coverture R6 (3) adds `subject_cannot_exit_persists` on top. Reading: the exit prohibition tops by construction wherever it exists, so the ranking cannot say much else until the twins are merged.

(ii) Kibbutz R2 carries one property (`care_assigned_by_sex`, persists to fails), R4 carries the twins (2). Footbinding R3 carries one (`binding_practised`, persists to fails), R9 the twins (2). The preregistered intuition was about which rule matters; the scorer counts properties, and the twins count twice. Not a finding about the institutions.

(iii) mwpa-property R11 flips nothing. Twelve properties are applicable: dependent_cannot_exit, subject_cannot_exit, subject_cannot_exit_persists, no_standing, care_and_sanction_same_role, care_assigned_by_sex, financial_dependence, financial_dependence_unpropertied, cannot_contract, plus the failure modes double_burden, creditor_shield, backlash. None flips on deleting R11, including `creditor_shield` (a failure mode, listed not counted: no failure-mode flips). The cause was not diagnosed here. R13 (`may hold_property`, deregulated, not ranked) flips `financial_dependence` violated to holds_to_k (0+1). Reading: the properties as encoded do not read the thing the act changed.

(iv) Ectogenesis. R4 tops at 1 with a freedom_down flip: deleting `may provide_care` leaves only the female `must`, so `care_assigned_by_sex` goes violated to holds_to_k. R5 reads 0 because `female_parent_care_persists` reads `persists` with or without R5 (council finding 6). The T3 test is uninformative, not refuted. Same pattern in gestational-surrogacy (R4, 0+1) and paternity-quota (R1, 0+1).

(v) Deregulation. 136 of 148 `may` rules (92%) are deregulated-not-ranked; 12 are "permission removed". 23 of 25 entries have most of their `may` rules deregulated (the exceptions: paternity-quota 3 of 7, transferable-leave 4 of 8). Under strict enabledness most permissions are each action's sole regulator, so the "permission removed" reading of decision 3 applies to few rules. Deregulated rows still carry flips (kibbutz R1 care_assigned_by_sex 1+0, mwpa-property R13 0+1, crisis-team R5 0+3); they are shown, not ranked.

## Council findings (2026-11-05 review, written before the fix pass)

Addressed: 1 and 2 (deregulation flag, excluded from ranking, derived power noted), 3 (orphan column), 4 (z3-unknown flag from `_check`, not message text), 7 (check kinds in header), 8 (stronger tests), 9 (`--summary`, zero-uncounted check). Partly: 5, flips are signed and reported up+down, but ranking still uses the unsigned sum. Stands: 6, R5 is property-blind.

## Pass test (plans/priority.md, layer 4)

Written test: deterministic and stable across k; rediscovers kibbutz R2 and ectogenesis R5; labels at least one strand mismatch, reported not fixed. Observed: runs on all 25 with zero silent errors; stable across k=6 and 8 (0 disagreements; step_mode not varied in this run); rediscovery fails both named cases (kibbutz R2 is second at 1, ectogenesis R5 is 0); strand mismatches against hand tags were not tabulated in this run. Verdict: runs, stable, 1/5 on the preregistered tops. Weakened; not passed.

## Decisions waiting on the author

a. Count property families, not properties (merge the exit twins), or keep.
b. Rank on `load_freedom_up` only, or the unsigned sum.
c. Deregulated deletions: keep excluded (ASSUMED option a), add the prohibit variant, or count them.
d. A property R5 actually carries (council: invariant-shaped companion) before re-running the ectogenesis expectation.
e. Re-preregister the five tops under a to d as revision 2; v1 stays in the record.

## Reproduction

`cd /Users/rees/Documents/computational-liberation && uv run phil rules ablate --k 6,8 --json ablate-25-v2.json --summary ablate-25-summary.json > ablate-25-v2.txt`

Outputs from this run: `/private/tmp/claude-501/-Users-rees-Documents/3aaae34a-2247-402e-bd6d-424feea4d706/scratchpad/ablate-25-v2.{txt,json}` and `ablate-25-summary.json`.

Decisions (a)-(e) settled 2026-11-05: families, freedom-up ranking, prohibit variant, `care_duty_on_women`, revision-2 preregistration. Recorded in plans/priority.md "Slice 1 revision 2".
