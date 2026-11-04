# Backtest: Married Women's Property Acts (preregistered, 2026-11-03)

Tags as in `backtest-data-inventory.md`: [F] opened; [R] recalled, verify. Failure modes DT/DI/BL/RB. Blows: (A) do rules trail material change? (B) did standing precede any floor and persist?

## 1. Timeline and ordering

Dates from Geddes, Lueck & Tennyson 2007 draft Table 1 (https://isnie-archive.sioe.org/assets/files/papers2007/geddes.pdf [F], "GLT"); sole-trader dates from Khan 1996 Table 1 (https://www.laits.utexas.edu/~mbs31415/Khan_MarriedWomenPropertyRights.pdf [F]). Geddes & Tennyson 2013 (https://ideas.repec.org/h/eme/rehizz/s0363-3268(2013)0000029007.html [F]) give corrected dates (paywalled); the table is a working copy.

| State | Property | Earnings | Sole trader (Khan) | Note |
| --- | --- | --- | --- | --- |
| MS | 1871 (GLT) | 1871 | 1871 | 1839 act shielded slave property from husbands' creditors; Khan excludes it as debt relief [F] |
| ME | 1855 (GLT; Khan 1844) | 1857 | 1844 | |
| MA | 1845 | 1846 (GLT; Khan 1874) | 1860 | |
| NY | 1848 | 1860 | 1860 | |
| PA | 1848 | 1872 | not listed | |
| WI | 1850 | 1872 | not listed | |
| NJ | 1852 | 1874 | 1874 | |
| MD | 1860 | 1842 (OCR, suspect) | 1860 | |
| OH | 1861 | 1861 | not listed | HWZ event state [F] |
| IL | 1861 | 1869 (GLT; Khan 1861) | 1874 | HWZ event state [F] |
| CA | 1872 | 1872 | 1872 | community property |
| IN | 1879 | 1879 | not listed | |
| TX | 1913 | 1913 | none in 19th c. | late control |

Material series:
- Married women's LFP: 4.6% (1890), 5.6% (1900), 9.0% (1920), 11.7% (1930); marital status not asked until 1880, no series before 1890 (Goldin 1986, https://www.nber.org/system/files/chapters/c9688/c9688.pdf [F]). Every property act above except TX, and every earnings act except TX, precedes the first observation.
- Women's patenting: 0.3 per million women before 1860, sharp rise after; 1890s metropolitan counties 52.9 vs 3.3 per million with vs without an earlier property law (Khan [F]). The 1844-1861 property acts precede the rise; the 1860-1879 earnings/sole-trader acts overlap it.
- Wealth and finance: census real and personal property 1860/1870; Comptroller national-bank deposits, loans and rates from 1865 (Hazan, Weiss & Zoabi, https://cepr.org/voxeu/columns/womens-liberation-financial-innovation [F]; working paper https://en-econ.tau.ac.il/sites/economy_en.tau.ac.il/files/media_server/Economics/foerder/papers/15-2016.pdf [F], "HWZ"). Deposits and loans per capita rose ~35% of mean, rates fell 50-90bp after rights; industrialisation flat before, +7-10pp two decades after. But a one-s.d. rise in non-agricultural TFP raises the propensity to grant rights 6-8pp: technology leads the law, finance follows.

Per-state ordering: for MA, NY, PA, WI, NJ, ME, MD, OH, IL the first property act (1844-1861) came before any measured women's labour, patenting or deposit series; for CA, IN, MS (1871-79) the acts came after the post-1860 patenting rise had begun nationally but before any state LFP observation. What leads the acts, where measured, is state wealth, urbanisation and schooling (Geddes & Lueck 2002, https://sfu.ca/~allen/LueckGeddes.PDF [F]: wealth per capita and share in cities >100k positive and significant for having both acts; 0/27 states in 1840, 30/38 by 1880) and TFP (HWZ). The 1839-1850 wave was debtor-relief: acts "generally contained nothing more than statements exempting married women's property from the debts of husbands", passed after the panics (Chused 1984, https://core.ac.uk/download/230496986.pdf [F], citing Chused 1983; the 1983 article itself [R], PDF refused).

## 2. Two rival readings

(A) Rights-first. The acts removed a disability; schooling (GLT: girls' attendance rises relative to boys after passage [F]), patenting (Khan), deposits and industry (HWZ) followed. (B) Material-first. Rising wealth, cities and TFP raised the cost of husbands' control; legislatures codified a shift already under way. Geddes & Lueck 2002's own adoption model is this reading, and HWZ's TFP result is too. Khan disagrees: the laws were "driven by forces other than growth in female nonhousehold production" [F].

Distinguishing observations: (i) state pre-trends in deposits and women's patenting 20 years before passage (HWZ: no industrial pre-trend; deposits untested); (ii) who lobbied: debtor coalitions in 1839-50 (B, for husbands' creditors), suffrage societies in 1860-80 (G&L: positive); (iii) whether earnings acts follow a state's own married-women's work or a neighbour's law (G&L: neighbours negative).

## 3. Predictions, written before running

Layer 1 (rules engine). Encode `mwpa-household` as four separable deltas on `coverture-household`:
- `property`: delete R1 (husband may control_property); add `wife may hold_property`. Flips: `financial_dependence` false for propertied wives only; `can_exit`, `has_standing` unchanged.
- `earnings`: add `wife may keep_earnings`; flips `financial_dependence` for wage-earning wives. Predicted DI: care obligation R3 (implicit) unchanged, so a wife now carries wages and housework.
- `sole-trader`: delete R7 disability on `contract`. Flips `can_contract`; `can_exit` still false (R6 stands).
- `suit`: delete R4; R9 enabled, so `has_standing` flips true. `can_exit` flips only with divorce reform, not here: the engine should say standing before exit.
Failure modes: DT, the 1839-50 acts protect family assets from husbands' creditors (Khan, Chused), encode as `creditor must_not attach wife_property`, husband's management kept; BL, courts "narrowly construing" the acts to keep husbands' control during marriage (Chused 1984 citing Chused 1983 at 1400 [F]), encode as a reinstated R1 under `narrow_construction`; RB, dower trade-offs [R].

Ordering (layer 3). Floor-first predicts acts after a labour or wealth floor; the author expects rules to lead. Author's prediction: property and suit rights precede measured married-women's LFP and patenting in >= 8 of 10 early states (blow B lands); but wealth, urbanisation and TFP precede adoption (blow A lands too, on the adoption margin). Against floor-first: standing (suit, contract) arriving before married LFP exceeds 10%, with gains persisting (GLT schooling, HWZ deposits). Against rules-lead: a state-level deposit or patenting pre-trend rising 10-20 years before the act.

## 4. Outcome measures and pass/fail

- Direction: engine flips `financial_dependence`, `has_standing` in the stated per-delta order; `can_exit` does not flip. Pass if verdicts match; fail if `suit` leaves `has_standing` false or `property` alone flips `can_exit`.
- Failure mode: pass if DT is the engine's top-ranked risk for the 1839-50 wave and BL for 1860-80; fail if it ranks DI or RB first with no historical trace.
- Ordering: pass if the per-state table shows rule before measured material series for the property/suit deltas and material-before-rule on adoption predictors; fail if deposit/patenting pre-trends rise 10+ years before passage in most states; inconclusive if the 1880-90 gap in LFP leaves >3 states undecidable.

## 5. Difficulty and data gaps

Medium-high. Gaps: no married-women's LFP before 1890; patenting is a thin proxy; three date lists disagree (Khan, GLT, G&T 2013 paywalled); Chused 1983 and G&L 2002's duration companion (Geddes & Lueck 2000) not opened [R]; HWZ tested no deposit pre-trend; dower and community-property states (CA, TX, LA) need separate encoding.

## Layer-1 run (2026-11-03)

Encoding: `data/institutions/_gen_institutions.py`, six entries off `coverture-household` (check-all 106/106, gate PASS; `phil rules iso --pair` per link). Chain: coverture -> `mwpa-creditor-exemption` (DT, 1839-50 form: +R10 creditor may attach [implicit], +R11 creditor must_not attach wife's acquired property, +R12 husband may transfer_to_wife; R1 kept; distance 3) -> `mwpa-property` (R1 -> R13 wife may hold_property; 1) -> `mwpa-earnings` (+R14 keep_earnings; 1) -> `mwpa-sole-trader` (R7 -> R15 may contract; 1) -> `mwpa-suit` (R4 -> R16 may sue while married; 1); branch `mwpa-property-narrowed` (BL: +R17 court may construe_narrowly, +R18 R1 reinstated under `narrowed`, R13 carries `not narrowed`; 2). Properties added: `financial_dependence` (all wives), `financial_dependence_unpropertied` (wives without acquired property), `cannot_contract`, `double_burden` (DI), `creditor_shield` (DT), `backlash` (BL). Verdicts below were written into the generator before the first run and not edited.

| step | predicted (section 3) | got |
| --- | --- | --- |
| creditor-exemption (DT) | nothing on the wife's side flips; creditor_shield reachable | as predicted: financial_dependence holds_to_k, creditor_shield reachable |
| property | financial_dependence violated for propertied wives only; can_exit, has_standing unchanged | financial_dependence violated, financial_dependence_unpropertied holds_to_k, subject_cannot_exit reachable, no_standing reachable; creditor_shield open (R1 gone) |
| earnings | dependence flips for wage-earning wives; DI: double burden | financial_dependence_unpropertied violated; double_burden reachable (open before) |
| sole-trader | can_contract flips; can_exit still false | cannot_contract violated; subject_cannot_exit reachable |
| suit | has_standing flips true; can_exit does not | no_standing unreachable (open); subject_cannot_exit reachable |
| property-narrowed (BL) | reinstated R1 under narrow construction | backlash reachable; creditor_shield reachable again; financial_dependence still violated (the court may, not must, narrow) |

Every verdict matched its preregistration (36 MWPA rows + 5 new coverture rows). Section 4, direction: **pass** (`financial_dependence` and `has_standing` flip in the stated per-delta order; `suit` does not leave standing false; `property` alone does not flip `can_exit`). Section 4, failure mode: **inconclusive**. The engine returns verdicts, not a ranking of risks, so "top-ranked risk" cannot be read off it; what it says is that DT (`creditor_shield`) is reachable in the 1839-50 form and extinguished by the property act, that BL is reachable only where a narrowing power is encoded (and re-opens DT), and that DI (`double_burden`) appears at the earnings step, not before. RB (dower) was not encoded ([R]). Section 4, ordering: not run (layer 3). Reachable failure modes: DT (exemption, narrowed), BL (narrowed), DI (earnings onward). Not reachable: none predicted that failed to appear. Displacement to another role: the plan names none and none is encoded; DI here is a burden that stays (R3), not one that moves.

Caveats. (1) Rules are reconstructed from GLT, Khan and Chused 1984; no statute text was opened, so every MWPA rule is UNVERIFIED as a reading of a statute. (2) The DT entry is at distance 3, not 1 (R10 exists so that the exemption removes a granted power rather than a constant). (3) The matcher pairs exemption R1 with property R12 (same skeleton) and prints R12 vs R13 as the differing rules; the distance is 1 as intended. (4) This is one encoder's chain checked against that encoder's predictions written minutes earlier; it tests that the engine reads the deltas as the plan says, not that the plan is right about history.

Engine test note (resolved 2026-11-03, engine commit 0a9c01e): `tests/test_rules_meta.py::test_removing_a_may_never_adds_reachable_dataset` failed on `mwpa-suit` (drop R16 -> `no_standing` goes open -> reachable) because the law assumed removing a `may` only shrinks reachability. A property over a negated derived power (`not has_standing`) is anti-monotone in enablement. The engine now splits properties by polarity (`is_monotone_in_enablement` / `is_antimonotone_in_enablement`): monotone properties keep the old law, anti-monotone ones get the mirror law (reachable stays reachable). Verdicts unchanged; 141/141 in that file.
