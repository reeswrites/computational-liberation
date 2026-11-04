# Parked: sexuality, relationships, and the marriage bundle (handoff, received 2026-11-04)

Status: PARKED. Author: "doesn't have to be right now but something to keep in mind." Not started.

Coordinator note (2026-11-04):
- Core goal is the cleanest test of the project's thesis yet: one status gating N goods, unbundled one good at a time, tracked by the count of rules gated on marital status. Each minimal pair (good on status vs good on the person or a chosen designation) is a one-rule pair of the kind gate (c) already handles.
- `marriage-bundle` is the first entry that needs composition (docs/connections.md section 3): the SSI marriage penalty and spousal coverage are rules in other institutions whose conditions read `married`. Encode as one entry first; split into composable pieces when the composition verb exists.
- Marital rape exemption extends coverture directly (Hale's doctrine is part of the same bundle): add it as a coverture rule and an mwpa-style repeal entry; preregister with the MWPA chain conventions.
- Sodomy, adultery and bigamy statutes are "control without a care duty": a preregistered NON-match to the care+control cluster, which is a useful negative control for the iso claim in docs/connections.md.
- Relationship agreements as micro-institutions with sunset conditions, drifting into implicit rules: ties to the kibbutz finding and to layer 2 (frozen). Encode the rules; the drift test waits.
- Rules-lead-vs-trail (same-sex marriage) is a backtest in reproductive-labor-adjacent territory, which the author kept open; the freedom-vs-flourishing reading (Warner) is a disagreement row for the locator.
- The consent/sexual-violence guard note must be written before any such encoding is run, like ADR 0005.
- Sequencing: after the ablation slices; the readability process (plans/readability.md) lands first so these encodings are written as per-institution source files with plain-English lines, not generator edits.

## Handoff text, verbatim

# Handoff: Sexuality, relationships, and the marriage bundle in computational-liberation

## Context
Repos: github.com/reeswrites/computational-liberation (theory, plan,
claims register, reviews, institutions dataset) and
github.com/reeswrites/philosophy-engine (generic engine).
Related Notion note: "Reinterpreting Abolition As Unbundling"
(lineage already there: Brake/amatonormativity, Chambers "Against
Marriage", relationship anarchy).

Current repo state (checked 2026-11-04): marriage appears only as
coverture (coverture-household, the MWPA backtest entries, footbinding's
marriage sanction). No-fault divorce is named as a counter-case to
floor-first (intent.md, claims T1/T4). Nothing yet on sexuality,
queerness, non-monogamy, or marriage as a benefits bundle.

## Scope decision
Model institutions and rules only: consent law, who may partner with
whom and how many, what partnership unlocks, and relationship
agreements as micro-institutions. First-order ethics (is non-monogamy
ethical, what fidelity is owed) belongs in philosophy-engine. Handoff
point: once a view becomes an enforced norm, it is an institution.

## Core goal: show the marriage bundle can be unbundled over time
Model marriage now so the engine can show its legal effects coming off
one by one, toward Chambers' "marriage-free state" (marriage as an
optional ceremony with no legal effects).

1. Encode `marriage-bundle`: one status triggers medical proxy and
   hospital visitation, intestate inheritance, immigration sponsorship,
   joint taxes and benefits (incl. SSI marriage penalty), and spousal
   health coverage.
2. One minimal pair per good: that good attached to the person or to a
   chosen designation instead of marital status.
3. Run in sequence; track the number of rules gated on relationship
   status (not total rule count, since some goods move to new rules
   such as a designation registry).

Backtests (verify before encoding):
- Medical proxy: advance directives let any adult name anyone
- Visitation: US hospitals in Medicare/Medicaid must honor
  patient-designated visitors (HHS rule, ~2010)
- Taxes: Sweden's move to individual taxation (early 1970s)
- Health coverage: single payer ties coverage to the person (links to
  the earlier healthcare/family-abolition thread)
- Immigration sponsorship: barely unbundled anywhere; test whether the
  engine finds a workable sequence or a real blocker

Claim for the register:
"Goods tied to marital status can each be reattached to the person or
to a chosen designation without loss of the good."
Falsified if a good can't be detached without losing coverage, or if
detaching it just moves the gate (cohabitation test, family-tie test).

## Additional institutions to encode
- Multi-partner domestic partnership ordinances (Somerville, Cambridge,
  Arlington, MA, 2020–21) vs. two-person partnership: a minimal pair
  differing by one rule (cap on number of partners)
- Sodomy laws (struck down in Lawrence v. Texas, 2003), adultery and
  bigamy statutes: control without a care duty; contrast with the
  care+control cluster
- Marital rape exemption (Hale's doctrine, part of coverture) and its
  state-by-state repeal: extends the coverture encoding and MWPA
  backtests
- Affirmative consent vs. force-based definitions: one-rule minimal pair
- Relationship agreements (exclusivity, disclosure, veto) as
  micro-institutions; optionally encode with sunset conditions and test
  whether they relax as trust grows or turn into implicit rules (cf.
  kibbutz finding). Possible link to the load-audit app's agreements
  and the private `me/` family.

## Tests of existing hypotheses
- Rules lead vs. trail: same-sex marriage, where public attitudes
  shifted before law; also a strong case for the "imagination"
  mechanism
- Freedom vs. flourishing: same-sex marriage gained standing by joining
  the dyadic bundle, not breaking it. Warner (The Trouble with Normal)
  argues it strengthened the bundle; others count it a clear gain.
  The engine should be able to score both readings.
- Care outside kin: queer chosen family and care networks during the
  AIDS crisis as historical evidence for "kith not kin"

## Tasks
- [ ] Verify: MA multi-partner ordinances (dates, current status),
      HHS visitation rule, Swedish tax date, marital-rape-exemption
      repeal timeline
- [ ] Encode marriage-bundle plus one minimal pair per good
- [ ] Encode the additional institutions above
- [ ] Add the unbundling claim and the rules-lead/trail and
      freedom-vs-flourishing tests to the claims register
- [ ] Write a guard note for consent and sexual-violence encodings,
      like ADR 0005: what the engine can and can't claim, before any run
- [ ] Run council review after the batch

## Caveats
Present both sides where contested (Warner vs. marriage-equality gains;
conservative views that marriage's legal bundle supports family
stability). Don't state current policy facts without verifying.
