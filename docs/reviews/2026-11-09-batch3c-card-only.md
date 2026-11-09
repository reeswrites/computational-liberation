# Batch 3c: card-only seat review (2026-11-09)

**Read (and nothing else):** docs/reviews/SEATS.md; cards cps, kibbutz-childrens-house, kibbutz-childrens-house-no-implicit, footbinding, footbinding-no-pledge, ectogenesis, gestational-surrogacy; the Edits list in plans/faithfulness-batch.md section 8 (lines 301-345 region). No YAML, JSON, code, other reviews, or external sources. Sources judged are only the excerpts printed on the cards.

**Counts: says it 7 / overstates 0 / understates 1 / cannot tell 0**

## Row judgements

1. **cps R1** (must investigate when `(and (report_received c) (cause_to_believe c))`): says it. The plain line repeats both conjuncts and names the worker as bound. Two gaps. (a) `cause_to_believe` is glossed nowhere on the card and the Legend has no term for a condition the world supplies (free/exogenous), so a lay reader cannot tell it is not something the worker or court does. (b) The only excerpt printed for R1 (WIC 328(a), "deems necessary") shows no cause-to-believe trigger; the added condition rests on the Source cell's own sentence about the statute. Quote the trigger text.
2. **kibbutz R5** (male member may visit when `(visiting_time child)`): says it. Plain says "during the daily visiting time (2-3 hours a day)"; the excerpt "visited their parents for 2-3 hours a day" supports it, and the old "at any time" is gone. Same gloss gap as (1): `visiting_time` is not defined as an outside-supplied clock fact. Tags (norm, none, may) plausible.
3. **kibbutz `neglect` as default capacity (old R8 removed)**: understates. The only table-level trace is "**Default capacities** ...: neglect, sleep_home". No table row mentions neglect, and the line says neither who may neglect nor what neglect is. A reader who never sees the YAML must dig into the long Notes block at the bottom (jargon: `default_capacity: true`, "layer-2 ABM") to learn that the metapelet may neglect unless a disability bars it. Legend wording ("a person of that kind") does not say which kind. The same line next to R4 is clear for `sleep_home` (R4 shows the disability), so a reader can learn the pattern, but not for neglect, which no rule touches.
4. **footbinding `leave_unbound` (old R2 removed)**: says it. The Default capacities line lists it, R3 on the same card ("must not leave its daughter unbound ... or else the suitor may reject") visibly punishes an act that is otherwise available, and Notes say R3 "punishes its exercise and does not remove it". Notes still say "leave_unbound (R2)" in the older gate-(a) paragraph, a dangling row id; the batch-3c sentence two lines on corrects it.
5. **ectogenesis R3** (provider must decant, no sanction): says it. Plain says "no sanction is encoded"; or-else none, sanctioner none, consistent. Tag plausibility is weak: Legend defines `formal` as written law or contract, but the source is a recalled 1970 book (UNVERIFIED). A reader sees a "formal" duty with no law behind it. Plain should say it is a proposed, not enacted, duty.
6. **gestational-surrogacy R3 (replaced)** (gestator must give birth, no sanction): says it, same reasoning. The "(replaced)" suffix in the id is not in the Legend.
7. **ectogenesis R6** (registry may reprimand at any time, "formerly the sanction for R3; since batch 3c linked to no rule"): says it. The card is honest that it is orphaned, and the "or else" column of every row shows none, so the reader can confirm nothing points to it. Left unexplained: why an unused rule is kept (Source cell says "kept so the pair's rule set stays symmetric", in jargon) and `x` shown "unbound (encoder to fix)" reads as a defect.
8. **gestational-surrogacy R6** (inherited): says it, same as 7. The card does not say it is inherited from ectogenesis; "since batch 3c" assumes the reader knows what 3c is.

## Legend coverage

Covers: may/must/must not, disability, implicit, or else, strand values, default capacity, k, Variables, kind, sanctioner, "sanctioner derived, unreviewed", the strategy tag. Missing: free/exogenous condition (`cause_to_believe`, `visiting_time`); "(replaced)" on a row id; "batch 3c" and "formerly/linked to no rule".

## Fixes requested

1. build.py cards: add a "Conditions set from outside" list (fluent name, gloss, "no rule in the institution makes this true") for free fluents that appear in a `when` cell, plus one Legend line defining it.
2. build.py cards: render the Default capacities line per action with the role and a plain sentence, e.g. "metapelet can neglect (nothing forbids it; no rule grants it)", and say "no rule mentions it" when no row names the action. Move or repeat the conversion sentence near the table.
3. `plain` of cps R1: quote the s. 300 trigger text in the source excerpt, or mark that part "from the encoder's reading of the statute".
4. `plain` of ectogenesis R3 / surrogacy R3: add "(a proposed duty, not enacted law)" or retag away from `formal`.
5. Legend: one line for "(replaced)" and for "linked to no rule"; replace "batch 3c" in R6 plain with a date or a gloss.
