#!/usr/bin/env python3
"""Offline, standard-library verification. Writes verification.json beside this file."""
from pathlib import Path
from fractions import Fraction
from decimal import Decimal, localcontext
from itertools import product
import json, math

def run():
    F=[0,1]; B=[0,1]; L=[2,1]
    for n in range(2,501):
        F.append(F[-1]+F[-2]); B.append(B[-2]-B[-1]); L.append(L[-1]+L[-2])
    out={'date':'2026-10-09','method':'Python exact integers/Fraction; Decimal 70-digit approximations; finite checks are not proofs','checks':{}}
    def record(name,detail):out['checks'][name]=detail
    for n in range(501):assert F[n]+B[n]==(2*F[n] if n%2 else 0)
    record('equilibrium',{'range':'n=0..500','passed':True})
    seeds=[(0,1),(0,7),(2,5),(-3,2),(Fraction(1,3),Fraction(-2,7))]
    for a,b in seeds:
        P=[a,b]; N=[a,b-a]
        for n in range(2,101):P.append(P[-1]+P[-2]);N.append(N[-2]-N[-1])
        for n in range(101):assert P[n]+N[n]==(F[n]*(2*b-a) if n%2 else a*L[n])
    record('generalized_equilibrium',{'seed_pairs':[list(map(str,s)) for s in seeds],'range':'n=0..100','passed':True})
    for n in range(1,500):assert L[n-1]+L[n+1]==5*F[n]
    record('five_connector',{'range':'n=1..499','passed':True})
    ratios=[]
    for n in range(1,31):
        g=L[n+1]-L[n]-1
        ratios.append({'n':n,'L':L[n],'gap':g,'ratio_left':str(Fraction(g,L[n])),'ratio_right':str(Fraction(g,L[n+1]))})
    assert Fraction(2,4)>Fraction(3,7)
    record('gap_ratios',{'rows':ratios,'counterexample_monotonicity':'n=3 → 4: 1/2 → 3/7; 2/7 → 3/11','finite_ratios_sum_at_n4':str(Fraction(3,7)+Fraction(3,11))})
    dmap={str(n):str(L[n]) for n in range(10)}
    def D(s):return ''.join(dmap[c] for c in s)
    active=set('2346789')
    for c in active:
        s=c
        for _ in range(4):s=D(s)
        assert sum(x in active for x in s)>=2
    assert D('5')=='11' and D('11')=='11'
    for k in range(1,5):
        for v in product('15',repeat=k):assert set(D(''.join(v)))=={'1'}
    record('digit_map',{'map':dmap,'settling_alphabet':'1,5','growing_alphabet':'0,2,3,4,6,7,8,9','active_lineages_double_within_four_substitutions':True,'example':'5 → 11 → 11'})
    frames=[a+'='+b for a in '><=0' for b in '><=0']
    def swap(s):return s.translate(str.maketrans('><','<>'))
    def sigma(s):return ''.join({'>' :'==0','<':'0==','=':'=','0':'0'}[c] for c in s)
    for f in frames:
        assert sigma(f)[::-1]==sigma(swap(f[::-1]))
        assert sigma(sigma(f))==sigma(f)
    images={}
    for f in frames:images.setdefault(sigma(f),[]).append(f)
    record('symbol_frames',{'frames':len(frames),'distinct_sigma_images':len(images),'collisions':{k:v for k,v in images.items() if len(v)>1},'mirror_law_passed':True,'idempotence_passed':True})
    def closed(m):
        states=[]
        for k in range(10):
            r=L[k]-1
            c,q=divmod(m,r) if r else (m,0)
            o=c%2;p=(r-q if o else q) if r else 0
            states.append((p,o));m=c
        return tuple(states)
    # Independent event-by-event recurrence, compared using positions/orientations only.
    positions=[0]*10; orientations=[0]*10
    def move(k):
        if k==10:return
        r=L[k]-1
        if r==0:orientations[k]^=1;move(k+1);return
        positions[k]+=(-1 if orientations[k] else 1)
        if positions[k] in (0,r):orientations[k]^=1;move(k+1)
    seen=set()
    for m in range(5001):
        state=tuple(zip(positions,orientations))
        assert state==closed(m)
        assert state not in seen;seen.add(state)
        move(0)
    record('terminal_counter',{'moves':'0..5000','unique_position_orientation_stacks':len(seen),'independent_incremental_matches_closed_form':True,'thresholds_L3_to_L7':[2,6,36,360,6120]})
    periods=[]
    for k in range(1,10):
        modulus=10**k; start=2*pow(5,k,modulus)%modulus;v=start;period=0
        while True:
            v=v*5%modulus;period+=1
            if v==start:break
            assert period<=128
        assert period==(1 if k<3 else 2**(k-3))
        periods.append(period)
    record('last_digit_periods',{'k':'1..9','periods':periods,'start_n':'k','passed':True})
    adjusted=[sum((2*5**n)%(10**k) for n in range(8))-1 for k in range(2,8)]
    record('unfinished_grid_extension',{'choice':'archived n0 adjustment 2 → 1; n=0..7','k':'2..7','sums':adjusted})
    mu=[1]*100002;prime=[True]*100002;prime[0]=prime[1]=False
    for p in range(2,100002):
        if prime[p]:
            for j in range(p,100002,p):mu[j]*=-1
            for j in range(p*p,100002,p):prime[j]=False
            for j in range(p*p,100002,p*p):mu[j]=0
    mertens=0;positive=negative=zeros=0;near={};first_positive=None
    for n in range(1,100002):
        mertens+=mu[n]
        if n>1 and mertens>0 and first_positive is None:first_positive=n
        if n<=100000:positive+=mertens>0;negative+=mertens<0;zeros+=mertens==0
        if n>=99994:near[n]=mertens
    assert near[100000]==-48
    record('mertens',{'near_100000':near,'first_positive_after_n1':first_positive,'positive_negative_zero_counts_to_100000':[positive,negative,zeros]})
    # Segment sets: a top, b upper right, c lower right, d bottom, e lower left, f upper left, g middle.
    segments=['abcdef','bc','abdeg','abcdg','bcfg','acdfg','acdefg','abc','abcdefg','abcdfg']
    rotate=str.maketrans('abcdefg','defabcg')
    rotated={}
    for i,s in enumerate(segments):
        target=set(s.translate(rotate));rotated[i]=next((j for j,t in enumerate(segments) if set(t)==target),None)
    assert rotated[2]==2 and rotated[5]==5 and rotated[1] is None
    record('seven_segment_rotation',rotated)
    with localcontext() as ctx:
        ctx.prec=70;one=Decimal(1);phi=(one+Decimal(5).sqrt())/2
        v0=Decimal(137)+one/28;v1=v0+one/v0/29;v2=Decimal(137)+one/(29-2/phi);final=(v1+2*v2)/3
        reference=Decimal('137.035999177')
        e6=Decimal('2.71')+one/90-Decimal(2).sqrt()/500
        record('checkpoints',{'V0':str(v0),'V1':str(v1),'V2':str(v2),'FINAL':str(final),'archive_reference_only':str(reference),'FINAL_minus_archive_reference':str(final-reference),'relative_error_percent':str((final-reference)/reference*100),'e_six_terms':str(e6),'e_error':str(e6-one.exp()),'angle_norm':str(Decimal(180)*Decimal(2).sqrt())})
    a,b=0.,1.;back_hi,back_lo=1.,0.;wall={}
    for n in range(1480):
        if n>=1474:wall[n]={'F':str(a),'backward':str(back_lo),'sum':str(a+back_lo)}
        a,b=b,a+b;back_hi,back_lo=back_lo,back_hi-back_lo
    record('binary64_wall',wall)
    out['all_assertions_passed']=True
    return out
if __name__=='__main__':
    result=run();dest=Path(__file__).with_name('verification.json');dest.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'all_assertions_passed':result['all_assertions_passed'],'check_groups':len(result['checks']),'output':str(dest),'mertens':result['checks']['mertens'],'sigma':result['checks']['symbol_frames']}))
