# Sourcing worklist: police, CPS, kibbutz, footbinding, naming, theory.md

Status: todo (2026-11-05). Part of plans/sourcing.md, order-of-work step 3. Written by a read-only research session that could run web searches but could not open any page (every host refused fetch). **Nothing here changes a verification level.** Every "lead" below is a search-result summary or a pointer: a lead, not a snippet (plans/sourcing.md, "Verification levels"). Whoever opens a lead records `opened` with an excerpt, or `snippet` if only an abstract or partial page was read.

Columns used per item: **rule/claim**, **current level** (what the migration should give it today from its `source` string), **lead** (URL, plus the search query that found it), **settling passage** (what to look for), **kind** (primary / secondary / empirical).

Order: falsifier impact. L1 (care+control match) reads police-crisis and cps; L6 (gate (d)) reads kibbutz; T7 and the footbinding pair read Centola and Mackie; theory.md last.

## 0. Which police / CPS rules does the care+control match read?

The handoff named the implicit practice norms police R1, R5, R6 as what the match reads. The YAML does not say that.

- The precommitted sub-signatures (ADR 0010, `isomorphic_to` in the YAML) are police R2~cps R4 (care), police R3~cps R3 (detain~remove), police R4~cps R10 (exit bar); against coverture: police R2~R2, R3~R5 (detain~chastise), R4~R6; cps R4~R2, R3~R5, R10~R6. **All six are statute-cited and were fetched in the 2026-11-04 card review (WIC 5150, 306).** None of police R1, R5, R6 or cps R5, R6 is in a declared sub-signature.
- They still matter, for three reasons: (i) L1's `sources` cell is `police-crisis:*; cps:*`, so under check 5 every row counts; (ii) the match is computed at guard+strands over the whole rule set, and ADR 0010's original witness was chastise~**use_force** (police R5), so R5 is a plausible alternative witness; (iii) cps R5 is the rule the cps notes call "the care relationship itself the lever" (the narrative of the cluster), and cps R6 is what makes cps `care_assigned_by_sex` reachable.
- Not confirmed by running the matcher (read-only session). A drop-one ablation (delete each UNVERIFIED rule, re-run gate (b)) would settle which UNVERIFIED rows the verdict actually depends on. Until then, treat police R5 and cps R5 as match-adjacent, and police R1/R6, cps R6 as entry-defining (they make the entry "police" / "gendered") but not match-reading.

UNVERIFIED count: police 5 of 9 (R1, R5, R6, R8, R10); cps 6 of 10 (R1, R2, R5, R6, R8, R11). As expected.

## 1. Police-crisis (Cal.)

### police-crisis R5: officer may use force when subject in custody and resists (match-adjacent; ADR 0010's original witness)
- Current level: unverified ("general knowledge").
- Claim: force is authorised incident to lawful custody when the person resists.
- Source kind: statute (primary) plus departmental policy (primary).
- Leads:
  - Cal. Penal Code 835a as amended by AB 392 (2019, eff. 2020-01-01): https://california.public.law/codes/ca_penal_code_section_835a ; bill text https://legiscan.com/CA/text/AB392/id/2049351/California-2019-AB392-Chaptered.html . Query: `California Penal Code 835a use of force peace officer overcome resistance`. Settling passage: 835a(b) "objectively reasonable force to effect the arrest, to prevent escape, or to overcome resistance", and (d) the officer "need not retreat or desist ... by reason of the resistance".
  - **Caveat the opener must resolve:** 835a speaks of *arrest* for a *public offense*; a 5150 hold is "custody", not an arrest. Look for whether 835a or the agency policy reaches 5150 detentions. Model departmental policy: Lexipol "Use of Force" (300) and "Mental Illness Commitments" (418) as adopted by a California agency, e.g. San Diego PD AB 392 training bulletin https://www.sandiego.gov/sites/default/files/tb20-01ab392trainingbulletin.pdf . Settling passage: force policy scope covering "detention" or "custody", not only arrest.
- Note: under the post-2020 text the rule's condition (custody and resists) is narrower than the statute's (arrest, escape, resistance) and the statute adds a de-escalation duty ("sound tactics, including the use of time, distance"). Not a wrong rule; the pin is the question.

### police-crisis R1: dispatcher must dispatch an officer on a crisis call (implicit practice norm; defines the entry against crisis-team)
- Current level: unverified.
- Claim: police are the default responder to a mental-health crisis call. No statute requires it; WIC 5150(a) gives the power to peace officers *and* designated mobile crisis team members.
- Source kind: only empirical / secondary work can support an implicit practice norm. What counts: a study of 911 dispatch data or agency survey that reports the share of behavioural-health calls routed to police, or a statement that police are the default first responder, ideally in California.
- Leads:
  - Vera Institute, "911 Analysis: How Civilian Crisis Responders Can Divert Behavioral Health Calls from Police" (2022): https://vera.org/publications/911-analysis ; PDF https://vera-institute.files.svdcdn.com/production/downloads/publications/911-analysis-civilian-crisis-responders.pdf ; methodology https://vera-institute.files.svdcdn.com/production/downloads/publications/911-analysis-methodology-and-limitations.pdf . Query: `percentage mental health crisis calls police first responders study 911 dispatch`. Settling passage: that in the nine cities studied behavioural-health calls are dispatched to police (the summary quotes Vera calling police "default first responders"). Secondary/empirical. Check whether any of the nine cities is Californian.
  - Treatment Advocacy Center, "Road Runners" (2019), national survey of sheriffs and police: https://www.treatmentadvocacycenter.org/road-runners . Settling passage: share of agency staff time (reported ~21%) and budget (~10%) on responding to and transporting people with mental illness; and the thematic finding that lack of community services makes police the responder. Empirical, national.
  - Primary context for "police by default until recently": California mobile-crisis Medi-Cal benefit and the 988 law (AB 988, 2022). Settling passage: a legislative finding that crisis response has defaulted to law enforcement. Not yet searched for text.
- The readability review judged R1 faithful as common knowledge; the sourcing standard needs one of the above.

### police-crisis R6: officer may carry a weapon at any time (tying strand; what crisis-team removes)
- Current level: unverified.
- Source kind: statute (primary) for the power; departmental policy (primary) for the practice of carrying on duty.
- Leads:
  - Cal. Penal Code 830.1 (peace-officer authority) and 25450 (peace officers exempt from the concealed-carry prohibition, on and off duty). Recalled, not searched to text; open on california.public.law. Settling passage: the exemption covering "any peace officer ... authorized to carry a firearm".
  - Lexipol Firearms policy (300-series) as adopted by California agencies, e.g. Fontana PD 312 https://www.fontanaca.gov/DocumentCenter/View/47741/312-Firearms-2 , Chico PD 312 https://chico.ca.us/documents/City-Services/Public-Safety/Police-Department/Regulatory/AB-481-–-Military-Equipment-Use-Policy/policy_312_-_firearms.pdf . Query: `Lexipol policy Firearms shall carry duty firearm California`. Settling passage: 312.4.1 "Duty weapons": uniformed personnel "shall carry" the issued or an approved handgun. Primary (agency policy).
- Note: "at any time" is broader than on-duty policy; 25450 is what supports off-duty.

### police-crisis R8: subject may petition for review of the hold (WIC 5275)
- Current level: unverified.
- Leads: WIC 5275 https://california.public.law/codes/ca_welf_and_inst_code_section_5275 ; WIC 5276 (hearing within two judicial days); county guidance on AB 2275 (Stats. 2022, ch. 960): https://www.smchealth.org/sites/main/files/file-attachments/bhrs_policy_23-04_-_5150_certification_review_hearing_procedure_ab2275.pdf , https://www.dhcs.ca.gov/provgovpart/Documents/BHIN-23-051.pdf . Query: `Welfare and Institutions Code 5275 habeas corpus 5150 72-hour detention`.
- Settling passage: the current opening of 5275, which a statute database renders as "Every person detained under this part shall have a right to a hearing by writ of habeas corpus for their release" (amended Stats. 2023 ch. 131).
- **Possible date problem:** the readability reviewer understood 5275 as covering certified (14-day) persons only, and county guidance describes AB 2275 (eff. 2023-01-01) as extending the writ to 5150 detainees. If the pre-2023 text read "detained by certification", R8 is right today but carries an `effective_date` of 2023, and before that a 72-hour detainee relied on general habeas (Cal. Penal Code 1473; Cal. Const. art. I s. 11). Record `effective_date` when opened.

### police-crisis R10: subject may sue in own name
- Current level: unverified. Low impact (feeds `no_standing`, not the match).
- Lead: WIC 5325 / 5325.1 (rights of persons with mental health disorders, "same legal rights ... as all other persons") and WIC 5331 (no person shall be presumed incompetent because evaluated or treated). Recalled; open on california.public.law. Primary.

## 2. CPS (Cal.)

### cps R5: parent must cooperate, or else removal (R3) (implicit practice norm; "the care relationship itself the lever")
- Current level: unverified. Readability review: cannot tell.
- Claim: non-cooperation is read as risk and feeds removal. A practice norm; no statute says it.
- Source kind: empirical, plus the state's risk-assessment instrument (primary, administrative). What would count: (a) a study reporting that parental cooperation predicts removal holding other risk constant; or (b) the California SDM (Structured Decision Making) safety / risk assessment item that scores caregiver cooperation or motivation.
- Leads (all secondary/empirical, found via query `parental non-cooperation child protective services removal decision study caseworker cooperation`):
  - NSCAW CPS-sample report (2005), caseworker removal decisions driven by parenting quality and "the parent's willingness to change and work with the agency": https://ojp.gov/ncjrs/virtual-library/abstracts/national-survey-child-and-adolescent-well-being-nscaw-cps-sample . US national.
  - Davidson-Arad (2001), 194 Israeli workers, parental cooperation related to removal decision: https://www.ojp.gov/ncjrs/virtual-library/abstracts/parental-features-and-quality-life-decision-remove-children-risk . Not California.
  - SSWR 2021 caseworker decision study, theme "Caregiver Behavior & Compliance": https://sswr.confex.com/sswr/2021/webprogram/Paper42828.html .
  - Primary to find: the California SDM Safety Assessment / Risk Assessment manual (Evident Change, formerly NCCD, for CDSS). Query to run: `California SDM risk assessment manual caregiver cooperation item`. Settling passage: an item scoring caregiver cooperation or refusal of services.
- Settling passage in any study: cooperation as a predictor of removal, with an effect size, not only as a caseworker-stated reason.

### cps R6: worker must contact the mother (implicit; drives cps `care_assigned_by_sex`)
- Current level: unverified. Readability review: cannot tell (source cell truncated).
- Source kind: empirical only. What counts: a case-file or caseworker study showing mothers are contacted and held responsible while fathers are not contacted.
- Leads:
  - Malm, Murray & Geen, "What About the Dads? Child Welfare Agencies' Efforts to Identify, Locate and Involve Nonresident Fathers" (Urban Institute for HHS/ASPE, 2006): https://aspe.hhs.gov/sites/default/files/migrated_legacy_files//41961/report.pdf . Query: `Malm Murray Geen 2006 What About the Dads`. Settling passage: share of nonresident fathers never contacted (summary: "nearly half"). US, four states (AZ, MA, MN, TN), not CA. Empirical, open PDF.
  - Strega, Fleet, Brown, Dominelli, Callahan & Walmsley, "Connecting father absence and mother blame in child welfare policies and practice", Children and Youth Services Review 30(7):705-716 (2008), doi:10.1016/j.childyouth.2007.11.012; open copy https://tru.arcabc.ca/_flysystem/repo-bin/2016-08/tru_953.pdf . Settling passage: 116 files, 60% of fathers judged a risk were not contacted; mother held responsible. Canadian. Empirical.
  - Walmsley et al., "Manufacturing ghost fathers", Child & Family Social Work 14:25-34 (2009). Secondary.
- Caveat: these show fathers *not* contacted, which supports "mother contacted (first)" only by contrast; the rule says *must* contact the mother. An implicit "must" can only ever be a reading of a pattern; say so on the row.

### cps R1: worker must investigate a report
- Current level: unverified.
- **The cited Penal Code 11165.14 looks wrong.** Search results for its text: "The appropriate local law enforcement agency shall investigate a child abuse complaint filed by a parent or guardian of a pupil ... against a school employee" (https://california.public.law/codes/ca_penal_code_section_11165.14). That is about police investigating school-site abuse, not CPS. Replace the pin.
- Leads: WIC 328 https://california.public.law/codes/ca_welf_and_inst_code_section_328 (settling passage: the social worker "shall immediately make any investigation he or she deems necessary" when there is cause to believe a child is described by s. 300; note the discretion "deems necessary", which a plain `must` drops); CDSS Manual of Policies and Procedures, Division 31, Emergency Response (31-100 series; in-person response "immediate" or within 10 days); index at https://www.cdss.ca.gov/inforesources/letters-regulations/legislation-and-regulations/child-welfare-services-regulations (not searched to text). Primary.
- The source string also says "the same worker who offers services investigates": WIC 16501(a) puts emergency response and family maintenance in the same county agency; same *worker* is a practice claim needing a secondary source. Flag on the row.

### cps R2: worker may provide services (WIC 16501)
- Current level: unverified. Lead: WIC 16501 and 16506 (family maintenance services) on california.public.law. Settling passage: definition of "child welfare services" including family maintenance. Primary. Low risk.

### cps R8: child must have appointed counsel (WIC 317)
- Current level: unverified.
- Lead: WIC 317 https://california.public.law/codes/ca_welf_and_inst_code_section_317 ; FindLaw https://codes.findlaw.com/ca/welfare-and-institutions-code/wic-sect-317/ . Settling passage: 317(c)(1) "If a child ... is not represented by counsel, the court shall appoint counsel ..., unless the court finds that the child ... would not benefit from the appointment". Primary.
- **Encoding concern:** the rule has `investigate` establish `counsel_appointed`. Counsel is appointed by the juvenile court once a dependency petition is filed, not on investigation; a report investigated and closed has no counsel. Also the "would not benefit" exception is dropped (the readability review noted it). Raise with the encoder.

### cps R11: child may petition in own name when counsel appointed (WIC 317(e))
- Current level: unverified. Readability review: cannot tell.
- **The better pin is WIC 388(a)(1)**, which (per search summary) lets "the child himself or herself" petition to change, modify or set aside an order: https://california.public.law/codes/ca_welf_and_inst_code_section_388 ; form JV-180, Cal. Rules of Court 5.570. Query: `California Welfare and Institutions Code 388 petition any parent or other person having an interest in a child`. Settling passage: the standing clause of 388(a)(1).
- **Possible condition error:** if 388 gives the child standing directly, the rule's condition "when counsel has been appointed" is narrower than the law (has_standing would not depend on counsel). Check the full standing clause (the snippet trails off at "through a ..."); it may require a guardian ad litem, which 317(c)(2) makes appointed counsel. Primary.

## 3. Kibbutz (gate (d), claim L6)

The weak point is the **sanction**, not the practice. R2's or_else R6 (committee reprimands for assigning a man) is what makes R2 a sanctioned norm; the card review judged R2 and R6 "cannot tell". The literature found so far describes the gendered *outcome* and argues about its *cause* (women's preference: Tiger & Shepher, Spiro 1979; structural pressure: Agassi, Palgi, Blumberg). None of the summaries describes a committee rule or reprimand for staffing the children's house with men. **This may mean R2's or_else is wrong, not just unsourced**: the sources may support a disability-free practice (the rota never did it) with no sanction. The third review already retreated from a disability to a sanctioned norm; an opener should look specifically for any report of sanction, and if none exists, the honest encoding is a pattern with no or_else, and the claim "a weaker encoding still passes (d)" becomes the load-bearing one.

### R6 (sanction: general assembly / public opinion as discipline)
- Current level: unverified.
- Leads:
  - Spiro, *Kibbutz: Venture in Utopia* (Harvard UP 1956; Schocken augmented ed. 1970). No archive.org copy found by search. eHRAF World Cultures holds it (culture MF01, document 014): https://ehrafworldcultures.yale.edu/cultures/mf01/documents/014 (institutional login; full text, searchable by OCM code for "sanctions" / "public opinion"). Settling passage: the chapter on social control, public opinion and the general meeting as the kibbutz's sanction. Primary ethnography.
  - Gavron, *The Kibbutz: Awakening from Utopia* (Rowman & Littlefield 2000, ISBN 9780847695263). Open Library lists Internet Archive id `kibbutzawakening0000gavr`: https://archive.org/details/kibbutzawakening0000gavr (lending, unconfirmed). Settling passage: anything on the assembly disciplining members over work. Secondary (journalistic oral history).
- Query used: `Spiro "Kibbutz: Venture in Utopia" archive.org full text general meeting public opinion sanction`; `Gavron "The Kibbutz: Awakening from Utopia" archive.org`.

### R2 (practice: no man assigned to the children's house)
- Current level: Wikipedia quote (opened 2026-11-03 per the row) for the practice; Tiger & Shepher via Kirkus only.
- Leads:
  - Tiger & Shepher, *Women in the Kibbutz* (HBJ 1975). No open copy found. Settling passage: their occupational tables showing women's share in child care / education (the row cites pp. 41, 167 via Wikipedia). Empirical (34,040 members), but frames the outcome as women's choice.
  - Spiro, *Gender and Culture: Kibbutz Women Revisited* (Duke UP 1979). No open copy found; review by Giasson, Anthropologie et Sociétés 6(1):261-265 (1982), open: https://www.erudit.org/fr/revues/as/1982-v6-n1-as497/006072ar.pdf . Settling passage: who staffed the children's houses at Kiryat Yedidim 1950-1975. Primary ethnography.
  - Agassi, "Gender equality: theoretical lessons from the Israeli kibbutz", open author copy: https://www.tau.ac.il/~agass/judith-papers/kibbutzlesson.pdf . Settling passage: any account of how work assignment put women in child care. Secondary, critical of Tiger & Shepher.
  - Palgi, Women in Judaism 1(1) (1997), open: https://epe.lac-bac.gc.ca/100/201/300/women_judaism/v01n01/v1n1palg.htm ; and Palgi, Blasi, Rosner & Safir (eds.), *Sexual Equality: The Israeli Kibbutz Tests the Theories* (1983). Settling passage: child care "remains the woman's responsibility"; any mention of men as metaplim or of the work-roster (sadran avoda) practice. Secondary/empirical.
- Query used: `Agassi ... OR Palgi "sexual division of labor" kibbutz women child care critique Tiger Shepher`.
- If any source reports men working as metaplim (even a few), R2 as an absolute `must_not` is too strong; look for it.

## 4. Footbinding and naming-convention

### Footbinding R1, R3, R5, R6, R7: Mackie 1996
- Current level: snippet (abstract read as a search-index snippet, per the rows), body recalled.
- Leads: JSTOR https://www.jstor.org/stable/2096305 (library login); ETH Zurich course copy cited elsewhere: webarchiv.ethz.ch/soms/teaching/OppFall09/MackieFootbinding.pdf (unconfirmed); USP course page https://edisciplinas.usp.br/mod/resource/view.php?id=3787562 (may be first page only). Query: `Mackie 1996 "Ending Footbinding and Infibulation: A Convention Account" pdf`. Settling passages: (R3/R5) the marriage-market mechanism, an unbound daughter is unmarriageable; (R4/R10) the two-part pledge, not to bind daughters and not to let sons marry bound women; (R7) bound or pledged as the marriage condition. Secondary (sociology, citing Chinese-history sources).
- Mackie's own informal summary, "Female Genital Cutting: The Beginning of the End" (2000), Scribd: https://www.scribd.com/document/319666376/BeginningOfEndMackie2000-pdf . Secondary.

### Footbinding R4, R10: pledge-society founding dates and membership
- Current level: recalled (Wikipedia search snippets only).
- Search found date conflicts that the row should record, not resolve:
  - Heavenly Foot Society, Xiamen: 1874 (most sources) vs 1875 (one source), meeting of 60-70 women presided over by John MacGowan.
  - Tianzu hui / Natural Foot Society, Shanghai: April 1895, Alicia Little and "more than ten Western women of different nationalities" (NCCU dissertation abstract https://ah.lib.nccu.edu.tw/handle/140.119/52093).
  - Chinese reformers: Kang Youwei's village effort 1883 (Britannica: an attempt in his own village, not a society); Wikipedia gives Nanhai 1887 (abandoned) and Canton 1895 with Kang Guangren; Hunan 1896/1897 (Wu Xinggang; Tan Sitong and Tang Caichang), Shanghai Bu chanzu hui 1897-06-30 (Liang Qichao).
  - The "~300,000 members" figure is a *claimed* aggregate for all anti-footbinding societies, unverified.
- Scholarly sources to open: Alison R. Drucker, "The Influence of Western Women on the Anti-Footbinding Movement, 1840-1911", Historical Reflections 8(3) (1981); Ono Kazuko, *Chinese Women in a Century of Revolution, 1850-1950* (Stanford 1989); Dorothy Ko, *Cinderella's Sisters: A Revisionist History of Footbinding* (UC Press 2005), ch. 1; Fan Hong, *Footbinding, Feminism and Freedom* (1997). Settling passage: founding date, founder, pledge wording, and membership figure with its source. Secondary (history). Query: `Bu chanzu hui Kang Youwei 1883 Canton anti-footbinding society Shanghai 1897 Liang Qichao membership 300,000`.
- Note for R4's row text: the 1874 society was missionary-led; Mackie's pledge mechanism (both halves, critical mass) is mainly the 1890s Chinese reformers' societies. The row's "1874 onward" is fine for the pledge; "superadditive ... critical mass" should cite the 1890s societies.

### Naming-convention (all rules, notes, `source_text`; claim T7)
- Current level: recalled (the rows say "cited from memory").
- Leads (open copies): author PDF https://www.asc.upenn.edu/sites/default/files/2021-03/Experimental%20evidence%20for%20tipping%20points%20in%20social%20convention.pdf (already linked in theory.md); accepted manuscript at City Research Online https://openaccess.city.ac.uk/id/eprint/20031/1/CM_CRO_Version.pdf . Science 360(6393):1116-1119, doi:10.1126/science.aas8827. Query: `Centola Becker Brackbill Baronchelli 2018 Science tipping points social convention 25% committed minority`. Primary.
- Settling passages: (a) design: 10 groups, 194 subjects recruited online, groups of ~20-30, paired rounds, reward on match ($0.10 per coordination reported by a critic) and penalty on mismatch; (b) minority sizes tested and outcomes: summaries disagree, 17%-31% vs 15%-35%; the entry's notes say largest failing ~21%, smallest succeeding ~25%, largest tested 31%; find the figure/table; (c) the theoretical model's predicted threshold and what it depends on (recalled: agent memory length; the 25% is the model's value at the experiment's parameters, not a universal constant). Record (c): it is the caveat T7 needs.
- Critiques (secondary, blog-level, no formal replication found): https://rufuspollock.com/Experimental+Evidence+for+Tipping+Points+in+Social+Convention ; https://jamesozden.substack.com/p/social-tipping-points-are-probably . Claim reported there: costly behaviours show thresholds of 50-65% (reusable cups). If kept in theory.md, cite the underlying study, not the blog.

## 5. docs/theory.md uncited facts

All currently uncited or web-blog-cited; no rule row, so no level beyond the claims register (`uncited`).

### Kleven adoptive-mothers finding (theory "Evidence that the role, not the body"; ectogenesis R5 leans on it)
- Citation (confirmed by search): Kleven, Landais & Søgaard, "Does Biology Drive Child Penalties? Evidence from Biological and Adoptive Families", *American Economic Review: Insights* 3(2):183-198 (2021), doi:10.1257/aeri.20200260. Open: LSE https://eprints.lse.ac.uk/107556 ; NBER WP 27130 https://nber.org/system/files/working_papers/w27130/w27130.pdf . Primary (empirical, Danish registers).
- Settling passage: abstract, "short-run penalties are modestly bigger for biological mothers, while long-run penalties ... are nearly the same" (search summary; WP appendix reportedly about -0.216 biological vs -0.182 adoptive, unweighted). theory.md's "roughly the same earnings drop" is right for the long run; add "in the long run" and "Denmark".

### "Forager societies relatively equal despite high fertility, because care was shared and little property"
- Dyble et al., "Sex equality can explain the unique social structure of hunter-gatherer bands", *Science* 348(6236):796-798 (2015), doi:10.1126/science.aaa5139; open record https://research-information.bris.ac.uk/en/publications/sex-equality-can-explain-the-unique-social-structure-of-hunter-ga/ . Primary. **Supports only equal influence over camp co-residence (Agta, BaYaka)**, not equality in general, nor shared care, nor property.
- For shared care: Hrdy, *Mothers and Others* (2009) (alloparenting). For little property / egalitarianism: Woodburn, "Egalitarian societies", *Man* 17(3):431-451 (1982); Boehm, *Hierarchy in the Forest* (1999). Recalled, not searched.
- **"Despite high fertility" is doubtful.** Bentley, Jasienska & Goldberg, "Is the fertility of agriculturalists higher than that of nonagriculturalists?", *Current Anthropology* 34(5):778-785 (1993) (open: https://goldberglab.wisc.edu/pdf/P002.pdf): foragers TFR ~5.6 vs intensive agriculturalists ~6.6 (p = 0.004); Campbell & Wood (1988) found no significant difference (5.7 / 5.9 / 6.3). Forager fertility is moderate and lower than agriculturalists'. Suggest "despite frequent births" or drop the clause.

### Mullainathan and Shafir (scarcity narrows attention)
- Mullainathan & Shafir, *Scarcity: Why Having Too Little Means So Much* (Times Books 2013); key experiment Mani, Mullainathan, Shafir & Zhao, "Poverty impedes cognitive function", *Science* 341:976-980 (2013), open via https://shafir.scholar.princeton.edu/document/9 . Primary.
- **Replication caveat:** O'Donnell et al., "Empirical audit and review and an assessment of evidentiary value in research on the psychological consequences of scarcity", PNAS (2021; correction Nov 2022) found weak evidential value in the scarcity literature; a Colombian replication (Theory and Decision, 2021) did not find the bandwidth effect; Shah, Zhao, Mullainathan & Shafir replied (2022 preprint). theory.md states the finding as settled; add "contested" or cite the audit.

### Inglehart (security shifts values toward self-expression and equality)
- Best fit for "equality": Inglehart & Norris, *Rising Tide: Gender Equality and Cultural Change Around the World* (Cambridge UP 2003). For the general mechanism: Inglehart & Welzel, *Modernization, Cultural Change, and Democracy* (2005); Inglehart, *Cultural Evolution* (2018), excerpt https://assets.cambridge.org/97811084/89317/excerpt/9781108489317_excerpt.pdf . Primary (World Values Survey). Settling passage: self-expression values "emphasize gender equality", linked to existential security.

### Whaling figures (theory "Technology is necessary, not sufficient"; claim T3)
- Currently cites a resilience.org blog. Replace with:
  - Davis, Gallman & Gleiter, *In Pursuit of Leviathan* (Chicago/NBER 1997); ch. 9 "Product Markets" open at NBER: https://www.nber.org/system/files/chapters/c8284/c8284.pdf . Settling passage: demand failure (illuminants) as the main cause of the US industry's decline. Secondary (economic history). **Note:** this supports "kerosene ended American (sperm) whaling", which cuts against the "only briefly" phrasing; the brief-cut claim needs its own source.
  - International Whaling Statistics (Norway, Statistics Norway scans): https://www.ssb.no/a/histstat/iws/iws_iii.pdf and the series index https://www.ssb.no/a/histstat/iws/ . Settling passage: the 1930/31 Antarctic catch by species (total reported 40,201 all species, the peak season). Primary (dataset). The theory's "about 30,000 blue whales by 1930" is plausible (a radio transcript says "more than 30,000" in 1930-31) but unconfirmed; the "about 6,000" baseline year is not located. Also: Rocha, Clapham & Ivashchenko, "Emptying the oceans", *Marine Fisheries Review* 76(4) (2014) (recalled).
  - Starbuck, *History of the American Whale Fishery* (1878), archive.org (recalled; primary-era compilation of voyages and catches).

### Happy the elephant (claims T4, L7)
- *Matter of Nonhuman Rights Project, Inc. v Breheny*, 38 N.Y.3d 555, 2022 NY Slip Op 03859 (N.Y. June 14, 2022), 5-2, DiFiore C.J.; affirming 189 A.D.3d 583; reargument denied 39 N.Y.3d 967. Official text: https://nycourts.gov/REPORTER/3dseries/2022/2022_03859.htm . Primary. Query: `"2022 NY Slip Op 03859" Nonhuman Rights Project Breheny`.
- Settling passages: habeas protects the liberty of human beings; personhood tied to the capacity to bear duties; extension is for the legislature. **Check theory.md's "citing destabilization and pet ownership":** the majority does warn of consequences for animal ownership and the use of animals, but find the exact passage; the LAist summary is secondary.
- Note: the handoff's "39 N.Y.3d" is the reargument-denial cite, not the decision.

### Cecilia the chimpanzee
- *Presentación efectuada por AFADA respecto del chimpancé "Cecilia" – sujeto no humano*, Expte. P-72.254/15, Tercer Juzgado de Garantías, Mendoza, Argentina, 3 Nov 2016 (Judge María Alejandra Mauricio). Text: https://www.animallaw.info/sites/default/files/16190011.pdf ; English translation (MPI) https://www.mpipriv.de/2185653/judicial_power_mendoza_argentina_re_cecilia.pdf ; case page https://www.animallaw.info/case/afada-habeas-corpus-cecilia . Primary.
- Settling passage: the dispositive part granting habeas corpus, declaring Cecilia a "sujeto de derecho no humano", and ordering transfer to the Sorocaba sanctuary (Brazil). theory.md's "won it" is right; use the court's term "non-human subject of law", not "person".

## Highest-value five

1. **cps R1 pin is wrong**: Penal Code 11165.14 is about law enforcement investigating school-site abuse. Replace with WIC 328 + CDSS MPP Div. 31; record "as he or she deems necessary". (Primary, open on california.public.law.)
2. **Drop-one ablation of the UNVERIFIED police/cps rows against gate (b)**, then open police R5's source (Penal Code 835a post-AB 392 plus a California agency's force policy that reaches 5150 custody). The declared sub-signatures read only statute-sourced rows; the ablation settles whether any UNVERIFIED row is load-bearing for L1.
3. **Kibbutz R6 / R2 or_else**: open Spiro 1956 (eHRAF MF01 doc 014) and Agassi's open PDF looking for any reported sanction for staffing the children's house with men. If none, R2's or_else is unsupported and L6 should rest on the weaker encoding.
4. **cps R5 and R6 empirical sources**: NSCAW (cooperation and removal) and Malm, Murray & Geen 2006 / Strega et al. 2008 (fathers not contacted), both with open PDFs; plus the California SDM instrument as the primary for R5.
5. **Centola 2018 from the open author PDF**: settle the tested minority sizes, the failing/succeeding band, and the model's dependence on memory length (T7's caveat); and Mackie 1996 full text for the footbinding pair.

## Findings that suggest a rule or claim is wrong, not just unsourced

- cps R1: cited Penal Code 11165.14 does not concern CPS investigation (search summary of its text).
- cps R11: WIC 388(a)(1) appears to give the child standing to petition directly, so the condition "when counsel has been appointed" may be narrower than the law; R11's 317(e) pin is the wrong section.
- cps R8: counsel is appointed by the court on a dependency petition, not by investigation; the rule's establishing action and the dropped "would not benefit" exception.
- police R8: WIC 5275's coverage of 5150 detainees may date only from AB 2275 / 2023 amendments; record `effective_date`.
- police R5: Penal Code 835a speaks of arrest for a public offense; whether it reaches 5150 custody is open.
- kibbutz R2 / R6: no source found for any sanction; the literature disputes the *cause* of the gendered staffing (preference vs structure), and Tiger & Shepher frame it as choice.
- theory.md: "despite high fertility" for foragers is contradicted by Bentley et al. 1993; Dyble 2015 supports co-residence equality, not general equality; the scarcity finding has a published replication audit; Davis, Gallman & Gleiter attribute the US whaling decline to demand collapse, which weakens "kerosene cut catches only briefly" for the sperm fishery (the theory's point holds for 20th-century rorqual whaling).
