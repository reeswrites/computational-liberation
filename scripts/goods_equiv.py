"""z3 validity of A <-> B for each good, fluents uninterpreted (first order, sorts agent and step, t free)."""
import sys, yaml, z3
from philengine import sexpr as sx
import os
D=os.environ.get('GOODS_DIR','data/institutions/goods-encoding')
A={g['id']:g for g in yaml.safe_load(open(f'{D}/encoder-1.yaml'))['goods']}
B={g['id']:g for g in yaml.safe_load(open(f'{D}/encoder-2.yaml'))['goods']}
Agent=z3.DeclareSort('agent'); Step=z3.DeclareSort('step'); S={'agent':Agent,'step':Step}
F={}
def fl(name,args):
    k=(name,len(args))
    if k not in F: F[k]=z3.Function(name,*[a.sort() for a in args],z3.BoolSort())
    return F[k](*args)
T=z3.Const('t',Step)
def tr(e,env):
    if isinstance(e,sx.Sym):
        if e.name in env: return env[e.name]
        if e.name=='true': return z3.BoolVal(True)
        if e.name=='false': return z3.BoolVal(False)
        return z3.Const(e.name,Agent)  # role literal
    if isinstance(e,sx.Quant):
        vs=[z3.Const(n,S[srt]) for n,srt in e.vars]; env2=dict(env); env2.update({str(v):v for v in vs})
        return (z3.ForAll if e.kind=='forall' else z3.Exists)(vs,tr(e.body,env2))
    if isinstance(e,sx.And): return z3.And(*[tr(x,env) for x in e.args])
    if isinstance(e,sx.Or): return z3.Or(*[tr(x,env) for x in e.args])
    if isinstance(e,sx.Not): return z3.Not(tr(e.arg,env))
    if isinstance(e,sx.Implies): return z3.Implies(tr(e.left,env),tr(e.right,env))
    if isinstance(e,sx.Iff): return tr(e.left,env)==tr(e.right,env)
    if isinstance(e,sx.Eq): return tr(e.left,env)==tr(e.right,env)
    if isinstance(e,sx.App): return fl(e.pred,[tr(x,env) for x in e.args])
    raise TypeError(type(e))
for k in A:
    a=tr(sx.parse(A[k]['formal']),{'t':T}); b=tr(sx.parse(B[k]['formal']),{'t':T})
    s=z3.Solver(); s.add(z3.Not(a==b)); r=s.check()
    print(f"{k:24} {'EQUIVALENT' if r==z3.unsat else ('DIFFERENT' if r==z3.sat else 'UNKNOWN')}")
    if r==z3.sat:
        m=s.model(); print('   counterexample (agents, step relations):'); [print('    ',d,'=',m[d]) for d in m.decls() if d.arity()>0 or d.name()=='t']
