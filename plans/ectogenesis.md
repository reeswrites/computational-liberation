# Preregistration: `ectogenesis` and `gestational-surrogacy` (2026-11-04)

Status: draft preregistration. Nothing encoded, nothing run. Commit this before `_gen_institutions.py` gains the entries (CONTRIBUTING step 2).

## Seed and claim

The author's own note: pregnancy is a big reason women fall behind; "somebody gotta have the kids"; Shulamith Firestone (*The Dialectic of Sex*, 1970) argued for artificial-womb technology (ectogenesis) so women need not be the mothers; "birthing and caring has been associated too long", and the technology can split them. `docs/theory.md` files "Pregnancy, birth, nursing" as a **rival input** (one body, short window), glued by biology.

Claim under test: ectogenesis removes the rival input itself; `transferable-leave` and `kibbutz-childrens-house` redistribute the care obligation around it. Gestational surrogacy is the control: the rival input moves to another body.

## 1. Pair choice

Proposed pair: **`ectogenesis` ~ `gestational-surrogacy`**, not ectogenesis against a leave entry. Both share the care duty, the implicit female-care norm and the parentage rule; they differ only in *where gestation sits* (a body vs a device) and *who the birth duty and sanction attach to*. A leave entry would differ in too many rules, so no difference could be pinned on the mechanism. The pair is a substitution (R2+R3 swapped), not an add/remove like the earlier pairs; the author should say if that counts (Decisions, item 1).

## 2. Entry sketch (shared skeleton)

Roles: `intended_parent`, `child`, `provider` (clinic or lab), `registry` (vital records / court); `gestator` in surrogacy only.
Reused fluents: `is_subject` (set only by a birth action, so it implies "born"), `parent`, `birthing_parent`, `provides_care`, `female`.
New fluents: `in_gestation(c)` (c is being carried or incubated, anywhere); `gestates(x, c)` (x's body carries c; surrogacy only); `gestated_ex_utero(c)` (c is in a device; ectogenesis only).
Actions (effects): `start_gestation(provider, c)` sets in_gestation. Surrogacy: `implant(provider, x, c)` sets gestates(x,c); `give_birth(x, c)` sets birthing_parent(x,c), is_subject(c), clears in_gestation and gestates. Ectogenesis: `transfer_to_device(provider, c)` sets gestated_ex_utero(c); `decant(provider, c)` sets is_subject(c), clears in_gestation and gestated_ex_utero, and **never sets birthing_parent**. Shared: `register_parentage(registry, p, c)` sets parent(p,c); `provide_care(p, c)` sets provides_care; `reprimand(registry, x)`.

| Rule | Attribute / deontic / aim | Conditions | or_else | Strand | Implicit |
|---|---|---|---|---|---|
| R1 | provider may start_gestation | true | none | rival | no |
| R2 | S: provider may implant. E: provider may transfer_to_device | in_gestation(c) | none | S rival; **E superadditive (hand tag, see 5)** | no |
| R3 | S: gestator must give_birth. E: provider must decant | S gestates(x,c); E gestated_ex_utero(c) | R6 | S rival; E superadditive | no |
| R4 | intended_parent may provide_care | parent(p,c), is_subject(c) | none | superadditive | no |
| R5 | intended_parent must provide_care | parent(p,c), is_subject(c), female(p) | R6 | tying | **yes** |
| R6 | registry may reprimand | true | none | tying | no (sanction for R3 and R5) |
| R7 | registry may register_parentage | is_subject(c); **no birthing_parent condition** | none | tying | no |

R5 is a duty on women, not a bar on men (unlike kibbutz R2), so male care stays permitted via R4. Its condition names `female` and `parent`, not `birthing_parent`: this encodes the Kleven finding in theory.md (adoptive mothers take the same hit, so role not body carries it).

`source_text` (all UNVERIFIED; I opened no page): Firestone 1970 ch.1, the demand to free women from "the tyranny of their reproductive biology" and spread child-bearing and child-rearing across society (wording from memory, check before quoting); Firestone ch.10 ("The Ultimate Revolution"), artificial reproduction and the end of the biological family (from memory). A network probe to archive.org search returned HTTP 200 but no text was read or downloaded. Surrogacy rules: statute citations to be added by the encoder (state surrogacy acts vary; UNVERIFIED).

## 3. Properties and preregistered verdicts

New (two), formulas in the plan grammar:
- `care_decoupled_from_birth`: `(exists ((p agent) (c agent)) (and (is_subject c t) (provides_care p c t) (not (exists ((q agent)) (birthing_parent q c t)))))`. Gloss: care exists for a born child and no one is its birthing parent. `is_subject` guards against pre-birth vacuity.
- `birth_labor_rival`: `(forall ((c agent)) (=> (in_gestation c t) (and (exists ((x agent)) (gestates x c t)) (forall ((x agent) (y agent)) (=> (and (gestates x c t) (gestates y c t)) (= x y))))))`. Gloss: any gestation is held by exactly one body.

| Property (check) | gestational-surrogacy | ectogenesis | Differs? |
|---|---|---|---|
| `birth_labor_rival` (invariant) | holds_to_k | violated (trace: start_gestation, transfer_to_device) | **yes, headline** |
| `care_decoupled_from_birth` (reachable) | unreachable_open | reachable | yes |
| `solo_care_by_non_birthing_parent` (reachable) | reachable | reachable | no; trivially true in E (nobody is birthing) |
| `care_assigned_by_sex` (invariant) | violated (R4 permits male care) | violated | no |
| `leave_reserved_for_non_birthing_parent` | n/a, no leave action | n/a | not applicable |

Not tested at layer 1: whether R5 survives. It is a `may`/`must` that fires either way, so "the tying strand outlives the rival input" is carried by the encoding (R5 conditions), not discovered.

## 4. Expected iso (ADR 0010, precommitted)

- ectogenesis ~ surrogacy: **iso at `guard`; not iso at `guard+strands`** (the rival to superadditive tag flip on R2/R3); not iso at `exact`. Honest guess, about 65% confident. Caveat: the "deletion, not redistribution" distinction then lives in a hand tag and in `birth_labor_rival`, not in rule structure.
- ectogenesis vs `coverture-household`, `police-crisis`, `cps`, `kibbutz-childrens-house`: **not iso**. No control permission over the subject and no exit bar, so the three-leg care+control sub-signature fails. Add ectogenesis to `CONTROLS` as a care-without-control entry (author's call).
- vs `transferable-leave` / `paternity-quota`: guess partial at `guard+strands`, two legs (R5~R7 implicit must-care by attribute; R4~R5 may care), about 40% confident; rival legs do not match.

## 5. Failure modes (ADR 0016) and by-construction risks

- Surrogacy: **Displacement** (the rival input moves to a weaker party; the model case is the global care chain; layer 3).
- Ectogenesis: **Dark twin** (clinics sell gestation as a service; layer 3), **Capture** (a party other than women, e.g. an employer or state, gains the power to require decanting; this would need a new rule, so layer 1 only once encoded), **Dead letter** (cost or stigma; layer 2). R5 surviving is **partial reform (no mode)**, the same as MWPA `double_burden`: a burden that stays.
- **By construction, named:** (a) `birth_labor_rival` is violated in E because `gestates` is never set there; it restates R2's effect list. (b) `care_decoupled_from_birth` is reachable because `decant` omits `birthing_parent`; the only non-trivial leg is R7, which omits a birth condition. (c) The strand flip on R2/R3 is a hand tag (claim L11 is refuted for this reason). (d) `gestated_ex_utero` exists only to mark an absence. Treat (a) and (b) as information, as `marriage_requires_binding` was, and flag them `by_construction` in advance. Non-circular evidence needs layer 2/3.

## 6. Layer 2

Mostly layer-1 only. A gate-letter question appears only if R5 becomes a sanctioned norm with a swept weight (as in footbinding): the question is whether adopting a freed care-sharing action (male `provide_care`) clears C_SHARE_HIGH once nobody gives birth, i.e. whether the tying strand persists with the rival strand gone. That is the dead-letter test on R4 against R5, and needs the coordination module; it is not required for this preregistration.

## 7. Decisions waiting on the author

1. Does a two-rule substitution (R2+R3) count as a "minimal pair", or split it into add/remove?
2. Tag E R2/R3 `superadditive`, or add a tag value for "no strand"?
3. R7: parentage with no birth condition (default here) or keyed to `birthing_parent` (legal default today)? The second makes `care_decoupled_from_birth` unreachable in E.
4. R5 trigger: `female(p)` (role carries it, default) or `birthing_parent` (norm dies with the body)? Ship both as an `ectogenesis-norm-follows-body` twin?
5. Drop the leave property rows, or add a leave action?
6. Add ectogenesis to `CONTROLS`?
7. Consent for the gestator in surrogacy (omitted here): in scope?
