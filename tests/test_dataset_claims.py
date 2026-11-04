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
    """With `enabled` false for an action no may/must rule names, deleting police R3 (may detain) and R5 (may
    use_force) removes can_sanction: the old shape of care_and_sanction_same_role (care implies power) goes from
    holds to violated, and the current shape (no one but the carer sanctions) from a non-vacuous holds_to_k to a
    vacuous one (its antecedent, some sanction power, is unreachable)."""
    inst, props = _dataset_inst("police-crisis")
    old = Property(name="old_shape", formal="(forall ((x agent) (y agent)) (=> (and (provides_care x y t) (is_subject y t)) (can_sanction x y t)))")
    cur = props["care_and_sanction_same_role"]
    ps = {"old_shape": old, cur.name: cur}
    which = {n: ["invariant"] for n in ps}
    before = {r.property: r for r in rc.run_all(inst, ps, k=6, which=which).results}
    after = {r.property: r for r in rc.run_all(_without(inst, "R3", "R5"), ps, k=6, which=which).results}
    assert before[cur.name].verdict == "holds_to_k" and not before[cur.name].vacuous
    assert after[cur.name].verdict == "holds_to_k" and after[cur.name].vacuous and after[cur.name].antecedent_reachable is False
    assert before["old_shape"].verdict == "violated"  # power only while danger holds; care persists
    assert after["old_shape"].verdict == "violated"  # and never holds_to_k by an always-enabled unregulated action
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
