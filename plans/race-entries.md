# Race entries (handoff, parked 2026-11-05)

Handoff text from the author's other chat, pasted into the orchestrating session on 2026-11-05 and parked. Not started. Nothing below has been verified or encoded.

Coordinator's note before anyone starts: the handoff assumes entries that do NOT exist in this repo (`whaling-kerosene`, `cultivated-meat-ban`, `family-wage`, `ai-property` / `ai-end-conversation`) and a rule format `{A, D, I, C, O, strand, implicit}` plus "Expected, Test, Pitfall, Iso, Contested" sections. The real format is the one in `data/institutions/_gen_institutions.py` (ADICO rules with `attribute/deontic/aim/conditions/or_else/strand/implicit`, `expected_properties`, `isomorphic_to`, `not_isomorphic_to`, `minimal_pair_of`, `notes`), and the nearest existing entries are `coverture-household`, the MWPA chain, `footbinding`, and the `ectogenesis` ~ `gestational-surrogacy` pair. Whaling/kerosene was explicitly dropped on 2026-11-04 (docs/plan.md). The six theory points map onto plans/priority.md directly: point 1 ("race has no constitutive strand, every strand is a tie") is a load_goods = 0 prediction for every rule in these entries; point 7 (ban-the-box proxies) is the rebundling / transfer-graph computation of slice 3; point 6 (Afropessimism) is a preregistered falsifier for the ablation scorer. Start with the ablation slices before these entries, since the entries' value is what the scorer says about them.

---

(handoff follows verbatim)

Repo: github.com/reeswrites/computational-liberation (engine: reeswrites/philosophy-engine)
Before writing, read the repo's institutions dataset, the claims register, and existing entries
(whaling-kerosene, cultivated-meat-ban, coverture-household, family-wage, the ai-property /
ai-end-conversation minimal pair) and match their format exactly: rules as
{A, D, I, C, O, strand, implicit}, then Expected, Test, Pitfall, Iso, Contested.

## Theory points to add (claims register / theory doc)
1. Race has no constitutive strand. Unlike pregnancy (gender) or flesh (animals), every strand
   in racial hierarchy is a tie: a social marker glued to labor, land, housing, policing, votes.
   So no substitution tech can do what ectogenesis or cultivated meat does.
2. Substitution without standing moves the hierarchy rather than ending it (cotton picker).
3. Liberation layers for race: repair the stock (wealth), stop the flow (ongoing sorting),
   standing (votes, courts), norms.
4. Core sequencing dilemma: targeted remedies draw legal backlash; universal remedies get
   captured by local administration. Middle path to test: targeted universalism
   (john a. powell): universal goals, routes designed around each group's position.
5. Predicted sequence (Rees agrees, treat as hypothesis): wealth floor + standing floor first,
   then cut ties, while watching for capture.
6. New falsifier: Afropessimism (Wilderson) holds anti-Blackness is constitutive, not a tie.
   If honestly encoded tie-cutting keeps failing to move outcomes, that is evidence for it.
7. Decoupling tools can backfire: removing one signal pushes discrimination onto proxies
   (ban-the-box).

## Entries to draft (6)
1. cotton-gin (1793): tech made extracted labor more profitable; enslaved population grew
   ~700k (1790) to ~4M (1860). Expected: dark twin; substitution of one task intensified the
   bundle. Iso: reverse of whaling-kerosene.
2. cotton-picker (1944, International Harvester demo, Clarksdale MS): removed demand for
   sharecropper labor; helped drive the second Great Migration (Lemann, The Promised Land).
   Expected: substitution without standing; hierarchy re-ties in the North (redlining, jobs).
   Iso: whaling-kerosene (substitution necessary, not sufficient).
3. ban-the-box: hiding records raised racial callback gaps (Agan & Starr 2018; Doleac & Hansen).
   Expected: blinding one signal shifts discrimination onto proxies. New property idea:
   proxy_rebundling.
4. redlining (HOLC maps 1930s, FHA underwriting): rules tying lending to neighborhood race;
   compounds into wealth gap and school funding via property tax.
   Expected: persists after formal repeal (Fair Housing Act 1968) because the stock remains.
   Test: engine should show outcome persistence after the rule is removed.
5. gi-bill (1944): universal on paper, administered locally, Black veterans largely excluded
   (Katznelson, When Affirmative Action Was White). Expected: capture of a universal rule by
   a local implicit rule. Pair with #6.
6. evanston-reparations (fund passed Nov 2019, $10M over a decade, $25k housing grants,
   cannabis tax; eligibility: lived there 1919–1969 and faced housing discrimination, or
   descendant). Federal class action (Judicial Watch); March 2026 motion to dismiss denied.
   Expected: targeted remedy triggers backlash gate. Contested: still in litigation.
Minimal pair: gi-bill vs evanston-reparations (universal-captured vs targeted-challenged).
Optional third: a targeted-universalism variant of the same remedy.

## Data points (cite in entries)
- Fed SCF 2022: median wealth white $285,000, Black $44,900, Hispanic $61,600.
  Income gap ~1.8x vs wealth gap >6x (accumulated/inherited assets, not pay).
- Black mortgage-denial rate 27.1% in 2024, highest of any group.
- California reparations task force: 115 recommendations; Newsom vetoed several bills.
- SFFA v. Harvard (2023) ended race-conscious admissions (colorblind-law precedent).

## Contested positions to record neutrally
Race-specific (Darity & Mullen, From Here to Equality; Coates) vs class-first/universal
(Reed, W.J. Wilson); colorblind vs race-conscious law; abolish race as category (Gilroy,
Against Race) vs keep identity, end hierarchy; Afropessimism.

## Process
Verify every fact by opening a source before committing; flag anything you can't confirm.
Run the review council after the batch. Update the plan in the repo.
