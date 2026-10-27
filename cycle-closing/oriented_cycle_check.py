#!/usr/bin/env python3
"""F-03 explicit candidate cycle tests. No external dependencies."""
from pathlib import Path
import json
WORD='0123456789'
def rotate(s,k=1):k%=len(s);return s[k:]+s[:k]
def step(q,d):return ((q+1)%10,-d if q==9 else d)
def undo(q,d):return ((q-1)%10,-d if q==0 else d)
def run():
    assert rotate(WORD)=='1234567890'
    assert WORD[::-1]=='9876543210'
    assert rotate(WORD)!=WORD[::-1]
    assert '01'[::-1]=='10'
    for k in range(10):
        s=rotate(WORD,k)
        assert rotate(s[::-1])[::-1]==rotate(s,-1)
    for q in range(10):
        for d in (-1,1):assert undo(*step(q,d))==(q,d)
    state=(0,1);states=[];rows=[]
    for t in range(21):
        q,d=state
        if t<20:states.append(state)
        if t in (0,1,9,10,11,19,20):rows.append({'step':t,'word':rotate(WORD,q),'phase':q,'orientation':d,'oriented_zero':'+0' if d==1 else '-0'})
        state=step(*state)
    assert len(set(states))==20
    assert rows[0]['word']==rows[3]['word']==rows[-1]['word']
    assert rows[0]['orientation']==-rows[3]['orientation']==rows[-1]['orientation']
    histories=[(t%10,t//10,(-1)**(t//10)) for t in range(1001)]
    assert len(set(histories))==1001
    assert all(q+10*c==t for t,(q,c,d) in enumerate(histories))
    N=360**9
    assert N==101559956668416000000000
    raw=['xyz','zxzyzz','zzxzzyzzzx']
    return {'date':'2026-10-09','passed':True,'status':'candidate rules; not a full formalization of Marc’s geometric model',
      'digit_operations':{'initial':WORD,'left_rotation':rotate(WORD),'full_reversal':WORD[::-1],'local_pair_reversal':'01 → 10','reflection_conjugates_rotation_to_inverse':True},
      'oriented_cycle':{'rule':'increment phase modulo 10; flip orientation only on wrap','rule_status':'proposed','state_count':20,'observed_word_period':10,'complete_finite_state_period':20,'rows':rows,'inverse_checks':20},
      'retained_history':{'rule':'retain unbounded wrap counter c as additional state','tested_steps':1001,'unique_states':1001,'reconstruct_time':'t=10c+q'},
      'literal_coordinate_rows':[{'raw':s,'length':len(s),'z_count':s.count('z')} for s in raw],
      'angular_count':{'assumptions':'nine labeled independent angular slots, each with 360 discrete choices','N':str(N),'N_times_N':str(N*N),'unconstrained_N_frame_histories':'N^N','deterministic_N_frame_histories_from_N_states':'at most N','synchronized_unit_rotation_period':360,'base_360_counter_period':'360^9 (requires a carry rule)'},
      'superseded':'F-02 run-length interpretation of z1; not Marc’s intended meaning',
      'open':['coordinate token boundaries','precise retained-z-to-index rule','which variable is Fibonacci','cancellation-to-echo transition','nine-angle discretization/independence and coupling','prime role versus arithmetic primality']}
if __name__=='__main__':
    out=run();p=Path(__file__).with_name('oriented_cycle_results.json');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'cycle_states':20,'retained_history_states':1001,'angular_slots_count':out['angular_count']['N'],'output':str(p)}))
