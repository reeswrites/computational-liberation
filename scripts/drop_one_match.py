"""Drop-one sensitivity of gate (b), the care+control match.

Deletes each rule of coverture-household, police-crisis and cps in turn, reruns the gate
on the edited institutions copy, and prints whether criterion b still PASSes.
Default: the gate runs in-process (philengine imported) in a spawn ProcessPoolExecutor
(z3 contexts are not thread-safe); `--subprocess` restores the old `uv run phil rules gate` calls.
Usage (repo root): python scripts/drop_one_match.py [--subprocess] [--only ENTRY:RULE] <tmpdir>
See plans/sourcing.md, "Which rows the care+control match reads".
"""
import json, subprocess, sys, copy, inspect, argparse
from concurrent.futures import ProcessPoolExecutor
import multiprocessing as mp


def gate_subprocess(p):
    return subprocess.run(['uv','run','phil','rules','gate','--institutions',p,'--json'],capture_output=True,text=True).stdout


def gate_inprocess(p):
    """Mirror cli_rules.cmd_gate with only --institutions/--json set (all else default)."""
    from philengine import rules_ablate, rules_gate
    from philengine.schemas_rules import RulesLoadError, default_paths, load_institutions, load_properties
    ip, pp = default_paths()
    try:
        insts, props = load_institutions(p), load_properties(pp)
        for inst in insts:
            rules_ablate.applicable_which(inst, rules_ablate.expand_contested(props))
    except RulesLoadError as e:
        return str(e)
    kw = {}
    if 'cache' in inspect.signature(rules_gate.run_gate).parameters:
        from philengine.rules_cache import RuleCache
        kw['cache'] = RuleCache()
    rep = rules_gate.run_gate(insts, props, **kw)
    return json.dumps({"passed": rep.passed, "agreement": rep.agreement,
                       "criteria": [{"key": c.key, "status": c.status, "detail": c.detail, "lines": c.lines}
                                    for c in rep.criteria]}, indent=1)


def run(args):
    j, p, use_sub = args
    out = gate_subprocess(p) if use_sub else gate_inprocess(p)
    try:
        c = [x for x in json.loads(out)['criteria'] if x['key'] == 'b'][0]
    except Exception:
        return j, 'ERR', out[-300:]
    return j, c['status'], c['detail']


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('tmpdir'); ap.add_argument('--subprocess', action='store_true')
    ap.add_argument('--only', help='ENTRY:RULE, run just that one deletion (debug)')
    a = ap.parse_args(); S = a.tmpdir
    base = json.load(open('data/institutions/institutions.json'))
    jobs = []
    for e in base:
        if e['id'] in ('police-crisis', 'cps', 'coverture-household'):
            for r in e['rules']:
                if a.only and a.only != f"{e['id']}:{r['id']}": continue
                jobs.append((e['id'], r['id'], 'UNVERIFIED' in r.get('source', ''), r.get('implicit')))
    work = []
    for j in jobs:
        eid, rid = j[0], j[1]; d = copy.deepcopy(base)
        for e in d:
            if e['id'] == eid: e['rules'] = [r for r in e['rules'] if r['id'] != rid]
        p = f"{S}/{eid}-{rid}.json"; json.dump(d, open(p, 'w'))
        work.append((j, p, a.subprocess))
    if a.subprocess:
        from concurrent.futures import ThreadPoolExecutor
        ex = ThreadPoolExecutor(4)
    else:
        ex = ProcessPoolExecutor(4, mp_context=mp.get_context('spawn'))
    with ex:
        for j, st, det in ex.map(run, work):
            pairs = [s for s in det.split('; ') if j[0] in s and ('crisis-team' not in s and 'control)' not in s)]
            print(f"{j[0]:20} {j[1]:4} unverified={j[2]!s:5} implicit={j[3]!s:5} b={st:5} {' | '.join(p.split(': ')[1] for p in pairs if ': ' in p)}")


if __name__ == '__main__':
    main()
