"""Drop-one sensitivity of gate (b), the care+control match.

Deletes each rule of coverture-household, police-crisis and cps in turn, reruns
`phil rules gate --institutions <copy> --json`, and prints whether criterion b still PASSes.
Usage (repo root): uv run python scripts/drop_one_match.py <tmpdir>
See plans/sourcing.md, "Which rows the care+control match reads".
"""
import json, subprocess, sys, copy, re
from concurrent.futures import ThreadPoolExecutor
S=sys.argv[1]; base=json.load(open('data/institutions/institutions.json'))
jobs=[]
for e in base:
    if e['id'] in ('police-crisis','cps','coverture-household'):
        for r in e['rules']: jobs.append((e['id'], r['id'], 'UNVERIFIED' in r.get('source',''), r.get('implicit')))
def run(j):
    eid,rid,_,_=j; d=copy.deepcopy(base)
    for e in d:
        if e['id']==eid: e['rules']=[r for r in e['rules'] if r['id']!=rid]
    p=f"{S}/{eid}-{rid}.json"; json.dump(d,open(p,'w'))
    out=subprocess.run(['uv','run','phil','rules','gate','--institutions',p,'--json'],capture_output=True,text=True).stdout
    try:
        c=[x for x in json.loads(out)['criteria'] if x['key']=='b'][0]
    except Exception as ex: return j,'ERR',out[-300:]
    lost=[s for s in c['detail'].split('; ') if eid in s and 'partial(care+control)' not in s and 'none' not in s]
    return j,c['status'],c['detail']
with ThreadPoolExecutor(4) as ex:
    for j,st,det in ex.map(run,jobs):
        pairs=[s for s in det.split('; ') if j[0] in s and ('crisis-team' not in s and 'control)' not in s)]
        print(f"{j[0]:20} {j[1]:4} unverified={j[2]!s:5} implicit={j[3]!s:5} b={st:5} {' | '.join(p.split(': ')[1] for p in pairs if ': ' in p)}")
