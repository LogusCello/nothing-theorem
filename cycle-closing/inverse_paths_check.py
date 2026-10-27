#!/usr/bin/env python3
"""Exact, offline tests of explicit candidate readings. No physical inference."""
from pathlib import Path
from fractions import Fraction as Q
import json
I=((1,0),(0,1)); A=((0,1),(1,1)); J=((-1,1),(1,0))
def mul(a,b):return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def add(a,b):return tuple(tuple(a[i][j]+b[i][j] for j in range(2)) for i in range(2))
def trace(a):return a[0][0]+a[1][1]
def apply(a,v):return tuple(sum(a[i][j]*v[j] for j in range(2)) for i in range(2))
def prime(n):return n>=2 and all(n%d for d in range(2,int(n**.5)+1))
def run():
    assert mul(A,J)==I==mul(J,A)
    assert mul(A,A)==add(A,I)
    F=[0,1];L=[2,1]
    for n in range(2,101):F.append(sum(F[-2:]));L.append(sum(L[-2:]))
    p=q=I;rows=[]
    for n in range(101):
        assert mul(p,q)==I
        assert trace(p)==L[n]
        assert trace(q)==(-1)**n*L[n]
        assert p[0][1]==F[n]
        assert q[0][1]==(-1)**(n+1)*F[n]
        assert trace(add(p,q))==(0 if n%2 else 2*L[n])
        assert add(p,q)[0][1]==(2*F[n] if n%2 else 0)
        if n<=12:rows.append({'n':n,'forward_matrix':p,'inverse_matrix':q,'L_forward':trace(p),'L_inverse':trace(q),'L_sum':trace(add(p,q)),'F_sum':add(p,q)[0][1]})
        p=mul(p,A);q=mul(q,J)
    # A candidate signed invariant: it flips sign under either unit direction.
    def form(v):x,y=v;return x*x+x*y-y*y
    for x in range(-6,7):
        for y in range(-6,7):
            v=(Q(x,2),Q(y,3))
            assert apply(J,apply(A,v))==v
            assert form(apply(A,v))==-form(v)
            assert form(apply(J,v))==-form(v)
    # Candidate symmetric source interval. Position, sign, magnitude are separate.
    intervals=[]
    for B in [Q(1,2),Q(1),Q(2),Q(3),Q(7),Q(10)]:
        for k in range(101):
            x=B*Q(k,100);assert B-(B-x)==x
            assert (x==(B-x))==(x==B/2)
            assert x+(B-x)==B
        assert -B/2+B/2==0 and abs(-B/2)+abs(B/2)==B
        intervals.append({'source_limit':str(B),'meeting_position':str(B/2),'signed_half_sum':'0','combined_magnitude':str(B)})
    # Explicit meeting-event model: both paths persist, directions reverse together at the center.
    def event(s):phase,pair=s;return (1-phase,pair[::-1])
    s=(0,(Q(1,2),Q(-1,2)));t=event(s)
    assert s!=t and event(t)==s and sum(s[1])==sum(t[1])==0
    assert sum(map(abs,s[1]))==sum(map(abs,t[1]))==1
    # No unique next limit follows from the merge alone.
    p,c=1,2;lucas=[2]
    for _ in range(6):p,c=c,p+c;lucas.append(c)
    assert lucas==[2,3,5,8,13,21,34] # ordered adjacent seeds matter: (1,2) is NOT Lucas (2,1).
    p,c=2,1;correct=[p,c]
    for _ in range(6):p,c=c,p+c;correct.append(c)
    assert correct==[2,1,3,4,7,11,18,29]
    return {'date':'2026-10-09','status':'candidate interpretations tested; no claim of a complete formalization',
      'passed':True,'matrix_checks_n':'0..100','quadratic_form_seed_pairs':169,'reflection_points':606,
      'matrix_rows':rows,'source_interval_checks':intervals,
      'hidden_cycle':{'states':[['+1/2','-1/2'],['-1/2','+1/2']],'same_signed_sum':0,'same_magnitude':1,'period':2,'rule_status':'chosen simultaneous swap, not derived'},
      'mirror_2_to_5':{'candidate_rule':'R_B(x)=B-x','required_B':7,'fixed_point':'7/2','R_2_of_2':0,'interpretation':'a single unchanged interval of width 2 cannot implement this numerical reflection'},
      'seed_order_check':{'Lucas':[2,1,3,4,7,11,18,29],'swapped_pair_next_limits':lucas},
      'prime_check':[{'n':n,'L_n':L[n],'prime':prime(L[n])} for n in range(13)],
      'unforced_next_limit_examples':{'retain_source':[2]*6,'double_source':[2,4,8,16,32,64],'retain_two_seeds_and_recur':[2,1,3,4,7,11]},
      'not_derived':['spatial z axis','literal light or shadow dynamics','prime-only collision rule','2↔5 layer operator','unique rule for collision, delay, or next layer']}
if __name__=='__main__':
    result=run();p=Path(__file__).with_name('inverse_paths_results.json');p.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'passed':result['passed'],'n':result['matrix_checks_n'],'seed_pairs':169,'reflection_points':606,'output':str(p)}))
