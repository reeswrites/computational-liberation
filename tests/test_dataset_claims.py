"""Dataset claims: tests about what the real institutions dataset says (gate criteria over the real institutions,
falsifier tests, round trip over the real dataset). Moved here from philosophy-engine/tests; the engine keeps
skip-when-absent copies until they are deleted there. The engine's own mechanics tests stay in the engine."""
from __future__ import annotations

import subprocess
import sys

import pytest
import z3

from philengine import rules_checks as rc
from philengine import rules_gate as rg
from philengine import rules_iso as ri
from philengine import rules_lower as rl
from philengine.rules_reference import Reference
from philengine.schemas_rules import InstitutionJSON, Property, default_paths, load_institutions, load_properties

slow = pytest.mark.slow


def _dataset_reencoded() -> bool:
    insts = load_institutions(default_paths()[0])
    return any(i.derived_fluents() for i in insts) and any(i.not_isomorphic_to_control for i in insts)


awaiting = pytest.mark.skipif(not _dataset_reencoded(), reason="awaiting dataset re-encode (ADR 0013)")


def _dataset_which(inst):
    return {n: [rc.check_for_expected(e) or "reachable"] for n, e in inst.expected_properties.items()}


def _dataset():
    ipath, ppath = default_paths()
    return load_institutions(ipath), load_properties(ppath)


def _dataset_inst(iid: str):
    ipath, ppath = default_paths()
    return next(i for i in load_institutions(ipath) if i.id == iid), load_properties(ppath)


def _without(inst: InstitutionJSON, *rids: str) -> InstitutionJSON:
    d = inst.model_dump()
    d["rules"] = [r for r in d["rules"] if r["id"] not in rids]
    return InstitutionJSON.model_validate(d)


def test_real_dataset_expectations():
    insts = {i.id: i for i in load_institutions(default_paths()[0])}
    r = ri.match(insts["companion-ownership"], insts["companion-guardian-renamed"])
    assert r.iso and r.pure_rename and r.mapping["role"]["owner"] == "guardian"
    r = ri.match(insts["companion-ownership"], insts["companion-guardianship"])
    assert not r.iso and r.rule_distance == 1 and r.unmatched_a == ["R9"] and r.unmatched_b == ["R9"]
    r = ri.match(insts["paternity-quota"], insts["transferable-leave"])
    assert not r.iso and r.rule_distance == 1 and r.unmatched_a == ["R2"] and r.unmatched_b == ["R2"]
    for other in ("coverture-household", "police-crisis", "cps"):
        assert not ri.match(insts["crisis-team"], insts[other]).iso


@awaiting
def test_gate_f_over_real_dataset():
    insts = load_institutions(default_paths()[0])
    by = {i.id: i for i in insts}
    c = rg.crit_f(by, insts)
    assert c.status == "PASS", c.detail
    assert "pure_rename=True" in c.detail and "distance=1" in c.detail
    cross = [l for l in c.lines if l.strip().startswith("cross ")]
    assert cross, "every human/non-human pair must be printed with its sub-signature"
    assert all("matched=" in l and "unmatched=" in l for l in cross)
    assert "bare iso" not in c.detail


@awaiting
def test_gate_b_c_d_over_real_dataset():
    insts = load_institutions(default_paths()[0])
    by = {i.id: i for i in insts}
    b = rg.crit_b(by)
    assert b.status == "PASS", b.detail
    assert "crisis-team: none at every level" in b.detail
    assert "(control): none@" in b.detail
    assert rg.crit_d(by).status == "deferred"


@awaiting
def test_full_gate_passes():
    insts = load_institutions(default_paths()[0])
    props = load_properties(default_paths()[1])
    rep = rg.run_gate(insts, props)
    assert rep.passed, rg.format_gate(rep, verbose=True)
    assert rep.agreement is not None and rep.agreement >= rg.AGREEMENT_MIN
    keys = [c.key for c in rep.criteria]
    assert keys == ["a", "b", "c", "d", "e", "f"]


@awaiting
def test_cli_iso_and_gate():
    out = subprocess.run([sys.executable, "-m", "philengine.cli", "rules", "iso", "--pair", "companion-ownership",
                          "companion-guardian-renamed"], capture_output=True, text=True)
    assert out.returncode == 0, out.stderr
    assert "iso=True pure_rename=True" in out.stdout
    out = subprocess.run([sys.executable, "-m", "philengine.cli", "rules", "gate"], capture_output=True, text=True)
    assert out.returncode == 0, out.stdout + out.stderr
    assert "GATE PASS" in out.stdout


def test_dataset_loads_and_grounds():
    ip, pp = default_paths()
    insts = load_institutions(ip)
    props = load_properties(pp)
    assert {i.id for i in insts} >= {"coverture-household", "police-crisis", "crisis-team"}
    for inst in insts:
        assert rl.validate_institution(inst) == [], inst.id
        G = rl.ground(inst, k=2)
        assert z3.Solver().check(G.system()) == z3.sat
        for name in inst.expected_properties:
            errs, _ = rl.validate_property(props[name], inst)
            assert errs == [], (inst.id, name, errs)


def test_dataset_loads_with_declared_init():
    ip, pp = default_paths()
    for inst in load_institutions(ip):
        G = rl.ground(inst, k=2)
        assert G.init == ("declared" if inst.declares_init() else "empty"), inst.id
        assert z3.Solver().check(G.system()) == z3.sat, inst.id


def test_coverture_dependent_cannot_exit():
    ip, pp = default_paths()
    inst = {i.id: i for i in load_institutions(ip)}["coverture-household"]
    props = load_properties(pp)
    expected = rc.normalize_expected(inst.expected_properties["dependent_cannot_exit"])
    assert expected in ("reachable", "holds_to_k")
    rep = rc.run_all(inst, props, which={"dependent_cannot_exit": [rc.check_for_expected(expected)]})
    r = rep.results[0]
    assert r.verdict == expected
    assert rep.bound_k == 6 and rep.z3_version
    if r.verdict == "reachable":
        assert any("marry(husband, wife)" in s.actions for s in r.trace)
        assert any("is_subject(wife)" in s.fluents and "can_exit(wife)" not in s.fluents for s in r.trace)


def test_deleting_police_sanction_rules_removes_the_bundled_power():
    """Police-crisis read to WIC 5150 (L1 landing 2026-11-06, plans/sourcing.md): the facility cares (R2) and may
    hold (R11); the officer may detain (R3) and use force (R5). With `enabled` false for an action no may/must rule
    names: the current shape of care_and_sanction_same_role (no one but the carer sanctions) is violated with the
    officer's powers in place, holds non-vacuously once R3 and R5 are deleted (the facility is then the only
    sanctioner and is the carer), and holds vacuously once R11 goes too (no sanction power is reachable). The old
    shape (care implies power) stays violated throughout. Updated 2026-11-06 after the run: before the landing the
    officer was the carer and the full entry held."""
    inst, props = _dataset_inst("police-crisis")
    old = Property(name="old_shape", kind="structure", formal="(forall ((x agent) (y agent)) (=> (and (provides_care x y t) (is_subject y t)) (can_sanction x y t)))")
    cur = props["care_and_sanction_same_role"]
    ps = {"old_shape": old, cur.name: cur}
    which = {n: ["invariant"] for n in ps}
    full = {r.property: r for r in rc.run_all(inst, ps, k=6, which=which).results}
    no_officer = {r.property: r for r in rc.run_all(_without(inst, "R3", "R5"), ps, k=6, which=which).results}
    none = {r.property: r for r in rc.run_all(_without(inst, "R3", "R5", "R11"), ps, k=6, which=which).results}
    assert full[cur.name].verdict == "violated" and not full[cur.name].vacuous
    assert no_officer[cur.name].verdict == "holds_to_k" and not no_officer[cur.name].vacuous
    assert none[cur.name].verdict == "holds_to_k" and none[cur.name].vacuous and none[cur.name].antecedent_reachable is False
    assert all(d["old_shape"].verdict == "violated" for d in (full, no_officer, none))
    # what violates the current shape is a non-carer holding the power while someone else cares: crisis-team's R8
    ct, _ = _dataset_inst("crisis-team")
    rep = rc.run_all(ct, {cur.name: cur}, k=6, which={cur.name: ["invariant"]})
    assert rep.results[0].verdict == "violated" and not rep.results[0].vacuous
    assert rc.run_all(_without(ct, "R8"), {cur.name: cur}, k=6, which={cur.name: ["invariant"]}).results[0].verdict == "holds_to_k"


def test_removing_guardianship_R9_restores_no_standing():
    """companion-guardianship's `no_standing_persists: fails` rests on R9 (court may reassign on best interest) alone:
    without it reassign is unregulated, hence never enabled, and the property persists as in companion-ownership."""
    inst, props = _dataset_inst("companion-guardianship")
    p = props["no_standing_persists"]
    rep = rc.run_all(inst, {p.name: p}, k=6, which={p.name: ["persists"]})
    assert rep.results[0].verdict == "fails"
    rep = rc.run_all(_without(inst, "R9"), {p.name: p}, k=6, which={p.name: ["persists"]})
    assert rep.results[0].verdict == "persists" and not rep.results[0].vacuous
    assert any("(enabled reassign ...) names an action no may/must rule regulates" in w for w in rep.warnings)


@slow
def test_round_trip_counterexample_traces():
    insts, props = _dataset()
    problems = []
    seen = 0
    for inst in insts:
        rep = rc.run_all(inst, props, k=6, which=_dataset_which(inst))
        assert rep.compliance == "strict" and rep.step_mode == "one"
        ref = Reference(inst, k=rep.bound_k, init=rep.init, step_mode=rep.step_mode)
        for r in rep.results:
            if r.verdict in ("reachable", "violated", "fails"):
                assert r.trace is not None, f"{inst.id} {r.property}/{r.check}: {r.verdict} without a trace"
                seen += 1
                bad = ref.replay(r.trace, props[r.property], r.check)
                if bad:
                    problems.append((inst.id, r.property, r.check, r.verdict, bad))
    assert seen > 0
    assert not problems, "\n".join(f"{i} {p}/{c} ({v}): {b}" for i, p, c, v, b in problems)


def test_goods_properties_have_two_encoders_and_contested():
    """Slice 2 (plans/priority-slice2.md sections 2 and 6): every goods property names two encoders and carries a
    `contested` list (empty when the encoders' formulas were logically equivalent); provided_for keeps encoder 2's
    non-equivalent formula. Revision 2 (R2.1, R2.3): every goods property has a `subject`; chosen_mutual_care added.
    Second encoder: agent, not someone living under the institution (ADR 0012)."""
    _, props = _dataset()
    goods = {n: p for n, p in props.items() if p.kind == "goods"}
    assert set(goods) == {"cared_for", "mutual_household_care", "known_carer", "child_with_family", "provided_for",
                          "chosen_mutual_care"}
    for n, p in goods.items():
        assert p.polarity == "good" and p.check == "persists" and p.encoders == ["encoder-1", "encoder-2"], n
        assert p.contested is not None and p.subject, n
    married = "(exists ((h agent) (w agent)) (married h w t))"
    assert goods["mutual_household_care"].subject == married == goods["chosen_mutual_care"].subject
    assert [a.encoder for a in goods["provided_for"].contested] == ["encoder-2"]
    assert all(goods[n].contested == [] for n in goods if n != "provided_for")


PRIMARY_MEASURES = {  # plans/priority-slice2.md revision 3, R3.1 (author decision 1, a value call): pinned verbatim
    "cared_for": ("guaranteed", "A dependent's care that the rules merely allow is not the good; the good is care that "
                                "does not lapse."),
    "provided_for": ("guaranteed", "Subsistence that is merely allowed is not secured, and the gloss asks that it be "
                                   "secured."),
    "chosen_mutual_care": ("possible", "A chosen good cannot be forced; a rule that forced it would be the imposition it "
                                       "excludes."),
    "mutual_household_care": ("possible", "Relational: mutual care that the rules force is control, not the good; what "
                                          "matters is that it is not barred."),
    "known_carer": ("possible", "Being known cannot be forced; the rules can only leave room for a continuing carer."),
    "child_with_family": ("possible", "Relational: forcing a child to stay with its family is itself control; what "
                                      "matters is that it is not barred."),
}


def test_goods_primary_measure_pinned():
    """R3.1: every goods property carries `primary_measure` and a one-line reason (at most 200 characters), and the
    mapping is the preregistered table, verbatim. No other property carries either key."""
    _, props = _dataset()
    goods = {n: p for n, p in props.items() if p.kind == "goods"}
    assert {n: (p.primary_measure, p.primary_measure_reason) for n, p in goods.items()} == PRIMARY_MEASURES
    for n, p in goods.items():
        r = p.primary_measure_reason
        assert r.strip() and "\n" not in r and len(r) <= 200, n
        assert all(a.model_dump().keys().isdisjoint({"primary_measure", "primary_measure_reason"}) for a in p.contested), n
    assert all(p.primary_measure is None and p.primary_measure_reason is None for p in props.values() if p.kind != "goods")


# R3.2 O5 (plans/priority-slice2.md revision 3): `care_obliged` pins. Two pins are written here as the preregistration
# meant them, not as it typed them (drift 10, plans/priority-slice2-results.md "Revision 3"): over every ordered pair of
# agents, `(married h w t)` is false for (wife, husband) while both duties hold, and (husband, wife) is still obliged by
# R2 once R3 is deleted. The as-typed forms are pinned too, with the verdict they get. `<=>` is written `iff` (the
# engine's grammar).
O5 = {
    "coverture-household": {
        "mutual_iff_married": ("(forall ((h agent) (w agent)) (iff (or (married h w t) (married w h t)) "
                               "(and (care_obliged h w t) (care_obliged w h t))))", "invariant", "holds_to_k"),
        "as_typed": ("(forall ((h agent) (w agent)) (iff (married h w t) (and (care_obliged h w t) "
                     "(care_obliged w h t))))", "invariant", "violated"),
        "wife_obliged": ("(care_obliged wife husband t)", "reachable", "reachable"),
    },
    "ectogenesis": {
        "iff": ("(iff (care_obliged intended_parent child t) (and (parent intended_parent child t) (is_subject child t) "
                "(female intended_parent t)))", "invariant", "holds_to_k"),
        "obliged": ("(care_obliged intended_parent child t)", "reachable", "reachable"),
    },
    "kibbutz-childrens-house": {
        "iff": ("(iff (care_obliged metapelet child t) (assigned metapelet t))", "invariant", "holds_to_k"),
        "obliged": ("(care_obliged metapelet child t)", "reachable", "reachable"),
    },
}


@pytest.mark.parametrize("iid", sorted(O5))
def test_care_obliged_pins(iid):
    inst, _ = _dataset_inst(iid)
    ps = {n: Property(name=n, kind="structure", formal=f) for n, (f, _, _) in O5[iid].items()}
    rep = rc.run_all(inst, ps, k=6, which={n: [c] for n, (_, c, _) in O5[iid].items()})
    assert {r.property: r.verdict for r in rep.results} == {n: v for n, (_, _, v) in O5[iid].items()}


def test_care_obliged_pin_coverture_without_R3():
    inst, _ = _dataset_inst("coverture-household")
    ps = {"wife_never": Property(name="wife_never", kind="structure", formal="(not (care_obliged wife husband t))"),
          "as_typed": Property(name="as_typed", kind="structure",
                               formal="(forall ((h agent) (w agent)) (not (care_obliged w h t)))"),
          "husband_still": Property(name="husband_still", kind="structure", formal="(care_obliged husband wife t)")}
    rep = rc.run_all(_without(inst, "R3"), ps, k=6, which={"wife_never": ["invariant"], "as_typed": ["invariant"],
                                                           "husband_still": ["reachable"]})
    assert {r.property: r.verdict for r in rep.results} == {"wife_never": "holds_to_k", "as_typed": "violated",
                                                            "husband_still": "reachable"}


CARE_OBLIGED_ENTRIES = {  # R3.2: every entry that declares provides_care (22; the footbinding pair declares none; drift 11)
    "coverture-household", "coverture-household-us", "coverture-floor", "mwpa-creditor-exemption", "mwpa-property",
    "mwpa-earnings", "mwpa-sole-trader", "mwpa-suit", "mwpa-property-narrowed", "police-crisis", "cps", "crisis-team",
    "airline-flight", "kibbutz-childrens-house", "kibbutz-childrens-house-no-implicit", "ectogenesis",
    "gestational-surrogacy", "companion-ownership", "companion-guardianship", "companion-guardian-renamed",
    "paternity-quota", "transferable-leave"}


def test_care_obliged_declared_where_provides_care_is():
    insts = load_institutions(default_paths()[0])
    for i in insts:
        fl = {f.name: f for f in i.fluents}
        assert ("care_obliged" in fl) == ("provides_care" in fl) == (i.id in CARE_OBLIGED_ENTRIES), i.id
        if "care_obliged" in fl:
            f = fl["care_obliged"]
            assert f.arity == 2 and f.params == ["x", "y"] and f.arg_roles == fl["provides_care"].arg_roles, i.id
            want = ("(or (obliged provides_care x y) (obliged provide_care x y))"
                    if i.id in ("ectogenesis", "gestational-surrogacy") else "(obliged provides_care x y)")
            assert f.derived == want, i.id
