# Sourcing worklist: hospital-visitation, ssi-marriage-penalty

Status: todo (2026-11-08). Part of plans/sourcing.md. Some hosts fetched, others did not. Levels below are what was reached. **Caveat on all `opened` rows:** WebFetch returns a small-model summary of the page, not raw text; quoted strings were returned as quotes but the opener should re-confirm against the raw page before CI-grade use. Search-engine summaries are leads and carry no level. Everything under "Proposed vocabulary" is ASSUMED.

## Corrections to the brief (read first)
- CAH visitation is **42 CFR 485.635(f)**, not 485.535(f). CMS transmittal r75soma names "new 42 CFR 485.635(f)" (opened). Cornell's 485.635 fetch showed only (a)-(e), so it was stale or truncated; the FR amendment names (f).
- r75soma is **Transmittal 75, 2011-12-02** (Pub. 100-07, Appendix A/W interpretive guidelines), effective and implemented 2011-12-02. informal-rules.md says "7 September 2011": that date is unconfirmed here (possibly the earlier S&C letter or press release; not found).
- Final rule: 75 FR 70831 (2010-11-19), effective **2011-01-18**; docket CMS-3228-F. informal-rules.md says "November 2010" (publication date; correct).
- 42 CFR 416.1802 is "Effects of marriage on eligibility and amount of benefits"; "Whether you are married and who is your spouse" is 416.1806. Holding-out is not in the 1802 text.

## 1. hospital-visitation, after (2011 rule)

### hv-cfr-482-13-h
- Source: 42 CFR 482.13(h), Cornell LII. Pin: (h)(2)-(4). Jurisdiction: US. Effective 2011-01-18; later amended (2012, 2019). Verification: **opened** (summary-mediated).
- Excerpt: "the right, subject to his or her consent, to receive the visitors whom he or she designates"; (h)(4) "Ensure that all visitors enjoy full and equal visitation privileges consistent with patient preferences."
- URL: https://www.law.cornell.edu/cfr/text/42/482.13
- Note: current eCFR text; the 2011 text is the FR amendment below. (h)(3) lists race, color, national origin, religion, sex, gender identity, sexual orientation, disability: it bars restriction on those grounds, not literally "on relationship". The relationship-agnostic effect comes from (h)(2) plus (h)(4). Written notice: (h)(1)-(2). Clinical restrictions: allowed by the intro.

### hv-fr-2010-final-rule
- Source: 75 FR 70831, Medicare and Medicaid Programs; Changes to the Hospital and CAH CoPs to Ensure Visitation Rights for All Patients (govinfo FR-2010-11-19, doc 2010-29194). Verification: **opened** (first 100,000 of 103,789 chars read; amendatory text read via offset).
- Excerpt: "These regulations are effective on January 18, 2011." (h)(2) text: "to receive the visitors whom he or she designates, including, but not limited to, a spouse, a domestic partner (including a same-sex domestic partner), another family member, or a friend".
- URL: https://www.govinfo.gov/content/pkg/FR-2010-11-19/html/2010-29194.htm
- Note: 485.635(f)(2)-(3) identical to (h)(2)-(3); (f)(1) adds "in advance of furnishing patient care whenever possible". CMS dropped the proposed "no more restrictive than immediate family" standard for "full and equal" because the proposal was hard to define and enforce.

### hv-presmemo-2010
- Source: Presidential Memorandum, Hospital Visitation, 2010-04-15 (White House archive). Verification: **opened**.
- Excerpt: "designated visitors ... should enjoy visitation privileges that are no more restrictive than those that immediate family members enjoy."
- URL: https://obamawhitehouse.archives.gov/the-press-office/presidential-memorandum-hospital-visitation
- Note: addressed to the HHS Secretary, "Initiate appropriate rulemaking".

### hv-cms-r75soma
- Source: CMS Transmittal 75, Pub. 100-07, 2011-12-02. Verification: **opened** (PDF downloaded, pdftotext; A-0215 read).
- Excerpt: "the burden of proof is upon the hospital to demonstrate that the visitation restriction is reasonably necessary to provide safe care."
- URL: https://www.cms.gov/regulations-and-guidance/guidance/transmittals/downloads/r75soma.pdf
- Note: A-0215/0216/0217 (hospitals) and C-1000/1001/1002 (CAHs, 485.635(f)) are new. Surveyors (state survey agencies) enforce; this is the "sanctioner state" evidence.

## 2. hospital-visitation, before (pre-2011 gate)

### hv-ll-2010-wcnc
- Source: Lambda Legal, *When Health Care Isn't Caring* (2010). Verification: **unverified** (could not open).
- URL: https://legacy.lambdalegal.org/sites/default/files/publications/downloads/whcic_report_when-health-care-isnt-caring.pdf
- Note: the host 301-loops between legacy.lambdalegal.org and lambdalegal.org; WebFetch and curl failed. No pages or quotes. Try a browser or Wayback; do not cite from memory.

### hv-pre2011-practice
- Evidence reached: the presidential memo (above, opened) names a spouses-and-immediate-family baseline ("no more restrictive than ... immediate family"); the FR preamble (opened) says "the current practice in some medical institutions ... denies patients access to their loved ones". These show regulators' description of practice, not a hospital's own policy text.
- Verification: **opened** for the regulator description; **unverified** for any hospital policy. A web search found no 2008-09 state hospital association model policy or archived hospital policy with "immediate family" text. Search summaries (unopened) mention ICU/ER limits to spouses and immediate family and a Jackson Health (Miami) April 2010 change.
- Note: the pre-2011 `kind: norm`, sanctioner institution rule therefore rests on regulators' characterisation.

## 3. hospital-visitation, informal gate after 2011

### hv-nv-2012
- Source: NBC News (via AP), "NV hospital denies rights to domestic partners", 2012-08-21. Verification: **opened** (summary-mediated).
- Excerpt: "It didn't matter that we were registered domestic partners." (Simonelli)
- URL: https://www.nbcnews.com/news/world/nv-hospital-denies-rights-domestic-partners-flna957300
- Note: Spring Valley Hospital, Las Vegas; Terri-Ann Simonelli denied access to partner Brittney Leon until she obtained power of attorney; admissions staff cited a policy. NRS 122A.200 gives domestic partners spouse rights but "has no penalty". One anecdote.

### hv-hrc-hei
- Source: HRC Healthcare Equality Index scoring criteria, Equal Visitation. Verification: **snippet** at best (search summary only; fetches failed: hrc.org path 404, assets2.hrc.org unresolvable). Treat as lead.
- Excerpt: none quotable. Summary: policy must allow "the patient's visitor of their choice" (2018 criteria); required for any recognition tier; self-selected sample.
- URLs: https://www.hrc.org/hei-scoring-criteria ; https://assets2.hrc.org/files/assets/resources/HEI_2018_Scoring_Criteria.pdf
- Note: no pass rate or compliance study found.

## 4. Proposed vocabulary, hospital-visitation (ASSUMED throughout)
- Roles (ASSUMED): `patient`, `partner` (the would-be visitor, non-kin), `kin` (spouse or immediate family), `hospital` (the institution; one entity covers charge nurse and policy).
- Fluents (ASSUMED): `married(patient, x)` arity 2; `counts_as_family(patient, x)` arity 2 (norm-layer, staff judgment); `designated(patient, x)` arity 2 (state, set by `designate`); `can_visit(x, patient)` arity 2; `clinically_restricted(patient)` arity 1. Reuse `married` and `is_subject`.
- Actions (ASSUMED): `designate(patient, x)`, `admit_visitor(hospital, x, patient)`, `deny_visitor(hospital, x, patient)`.
- Rules, before (ASSUMED): H1 `kind: norm`, `sanctioner: institution`: hospital may admit x when `counts_as_family`; H2 `kind: norm`: hospital may deny x when not `counts_as_family`; H3 `kind: formal` (hospital policy, sanctioner institution): `counts_as_family` follows `married` or kinship. No state-sanctioned visitor-choice rule exists.
- Rules, after (ASSUMED): F1 `kind: formal`, `sanctioner: state` (CMS via state survey agency, loss of Medicare participation): hospital must admit x when `designated` and not `clinically_restricted` (482.13(h)(2), (h)(4)); F2 `kind: formal`: hospital must not deny on listed protected grounds ((h)(3)); F3 `kind: formal`, sanctioner institution: hospital may restrict when clinically necessary. H1/H2 stay as `kind: norm` (overridden, not deleted), carrying preregistered N1.
- Minimal pair (ASSUMED): the before variant lets `can_visit` hold only through `counts_as_family`, so a patient who is unmarried and unrelated to their partner cannot secure the good by any act of their own. The after variant adds `designate` as an action available to the patient alone and a state-sanctioned rule that makes `designated` sufficient. The diff is one gate: `married or kin` replaced by `designated`, with the clinical exception unchanged. The staff gate remains as a norm; the dataset has only anecdote (hv-nv-2012) for retention, no rate.

## 5. ssi-marriage-penalty

### ssi-cfr-416-1806
- Source: 20 CFR 416.1806 "Whether you are married and who is your spouse". Verification: **opened** (summary-mediated). Jurisdiction US.
- Excerpt: "We will consider someone to be your spouse (and therefore consider you to be married) for SSI purposes if--"; (a)(3) "You and an unrelated person of the opposite sex are living together in the same household"; "you both lead people to believe that you are husband and wife."
- URL: https://www.law.cornell.edu/cfr/text/20/416.1806
- Note: the Cornell text still says "opposite sex", unlike POMS (below), which a search summary says covers same-sex couples. The regulation text may be unamended after Obergefell. Effective date unread.

### ssi-cfr-416-1802
- Source: 20 CFR 416.1802 "Effects of marriage on eligibility and amount of benefits". Verification: **opened** (summary-mediated).
- Excerpt: "we will count your combined income and calculated the benefit amount for you as a couple."; "(d)(1) Benefits depend on whether you are married or not married at the beginning of each month."
- URL: https://www.law.cornell.edu/cfr/text/20/416.1802
- Note: "holding out" does not appear. Spousal deeming proper is 20 CFR 416.1160-1163 (not opened; cited from memory, level recalled). 416.1804, 416.1805: not read.

### ssi-poms-si-00501-150
- Source: SSA POMS SI 00501.150 "Determining Whether a Marital Relationship Exists", TN 80 (02-25). Verification: **opened** (summary-mediated).
- Excerpt: "Two individuals are married for SSI purposes if they are:" ... "Living together in the same household and holding themselves out as a married couple to the community in which they live."
- URL: https://secure.ssa.gov/poms.nsf/lnx/0500501150
- Note: G.2 presumption when former spouses resume living together.

### ssi-poms-si-00501-152
- Source: SSA POMS SI 00501.152 "Determining Whether Two Individuals Are Holding Themselves Out as a Married Couple", TN 85 (12-25). Verification: **opened** (summary-mediated).
- Excerpt: "both individuals lead people in the community in which they reside to believe they are a married couple"
- URL: https://secure.ssa.gov/poms.nsf/lnx/0500501152
- Note: examples include calling each other "spouse"/"husband"/"wife" and a shared last name or joint records.

### ssi-usc-1382a
- Source: 42 U.S.C. 1382(a)(1)(B), (a)(3)(A)-(B), (b)(1)-(2). Verification: **opened** (first 100,000 of 170,641 chars).
- Excerpt: couple "$3,000 on January 1, 1989"; individual "$2,000 on January 1, 1989"; before 1985 "$2,250" / "$1,500". Base benefit rates $1,752 (individual) and $2,628 (couple) for 1974+, indexed by COLA.
- URL: https://www.law.cornell.edu/uscode/text/42/1382
- Note: limits added by Pub. L. 98-369 sec. 2611 (1984), stepped to 1989 and not inflation-indexed. Ratio 1.5 is arithmetic.  2026 rates ($994 / $1,491; $2,000 / $3,000): **unverified lead** (search summary citing SSA 2026 SSI Annual Report, https://www.ssa.gov/OACT/ssir/SSI26/III_ProgramDescription.html, not opened; ssa.gov/oact/cola/SSI.html returned 403).

### ssi-crs-rl33675
- Source: CRS, *Potential Effect of Marriage on SSI Eligibility and Benefits*, RL33675 (2008-01-30). Verification: **opened** (summary-mediated; author not shown).
- Excerpt: "a married couple has a lower resource limit, a lower maximum federal benefit, and a lower amount of excluded income."
- URL: https://www.everycrsreport.com/reports/RL33675.html
- Note: 2008 figures: two singles up to $1,348/month combined vs $1,011 for a couple, resources $4,000 vs $3,000. It lists holding out as the third test but does not frame it as a displaced gate.

## 6. Proposed vocabulary, ssi-marriage-penalty (ASSUMED)
- Fluents (ASSUMED): `married(h, w)` arity 2 with roles aliasable to husband/wife (the composition plan's alias mechanism) and `spouse` neutral; `holds_out(a, b)` arity 2 (a state fluent set by conduct: shared household and public presentation); `cohabits(a, b)`; `couple_status(a, b)` derived as `married or holds_out`; `financial_dependence` per docs/connections.md C2 (property: one party's means depend on the other's).
- Roles (ASSUMED): `claimant`, `partner`, `ssa` (the agency; sanctioner state).
- Rules (ASSUMED): S1 `kind: formal`, sanctioner state: SSA must count combined income and resources when `married` (416.1802); S2 `kind: formal`: must apply the couple rate and the $3,000 limit; S3 `kind: formal`: SSA treats `holds_out` cohabitants as married (416.1806(a)(3), POMS 00501.150/.152). S3 is the displaced gate: it keeps the penalty reaching unmarried couples.

## Gaps
- Lambda Legal 2010 report: not opened (redirect loop). No page-level evidence for pre-2011 "immediate family" practice from advocates.
- No pre-2011 hospital policy text found or opened (state hospital association model policy, archived hospital policy). Jackson Health 2010 change is a search-summary lead.
- The "7 September 2011" CMS memo date: not found. r75soma is 2011-12-02.
- r75soma A-0216/A-0217 and C-1000 to C-1002 not read.
- HRC HEI text: snippet at best; no criterion text opened.
- 416.1804, 416.1805, 416.1160-1163 (deeming): not opened. Effective dates of 416.1806 unread.
- 2026 SSI federal benefit rates: lead only.
- No secondary source found framing holding out as a displaced gate; CRS gives rule and size only. Unopened candidates: SSA ip2003-01 (403), NPR/KUOW 2024 story, S. 73 (2025).
- Vocabulary in sections 4 and 6 is entirely ASSUMED.
