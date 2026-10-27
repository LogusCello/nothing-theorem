#!/usr/bin/env python3
"""Exact tests of F-02 candidate notation; offline Python standard library."""
from fractions import Fraction as Q
from itertools import product,groupby
from pathlib import Path
import json
A=((0,1),(1,1));I=((1,0),(0,1));K=((-1,2),(2,1))
def mul(a,b):return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def advance(L,F):return ((L+5*F)/2,(L+F)/2)
def undo(L,F):return ((5*F-L)/2,(L-F)/2)
code={'>':'==0','<':'0==','=':'=','0':'0'}
decode={v:k for k,v in code.items()}
def enc(word):return tuple(code[c] for c in word)
def dec(groups):return ''.join(decode[g] for g in groups)
def address_enc(word):
    groups=[]
    for c,items in groupby(word):
        n=len(list(items));groups.append(c+(str(n-1) if n>1 else ''))
    return '/'.join(groups)
def address_dec(text):
    return ''.join(g[0]*(int(g[1:])+1 if len(g)>1 else 1) for g in text.split('/'))
def run():
    assert mul(K,K)==((5,0),(0,5))
    fib=[0,1];lucas=[2,1]
    for n in range(2,101):fib.append(sum(fib[-2:]));lucas.append(sum(lucas[-2:]))
    l,f=Q(2),Q(0);p=I;rows=[]
    for n in range(101):
        assert (l,f)==(lucas[n],fib[n])
        assert l*l-5*f*f==4*(-1)**n
        assert undo(*advance(l,f))==(l,f)
        for i in range(2):
            for j in range(2):assert 2*p[i][j]==l*I[i][j]+f*K[i][j]
        if n<=12:rows.append({'n':n,'L':int(l),'F':int(f),'invariant':int(l*l-5*f*f),'next_L':str((l+5*f)/2),'next_F':str((l+f)/2)})
        l,f=advance(l,f);p=mul(p,A)
    seed_count=0
    for a in range(-6,7):
        for b in range(-6,7):
            l,f=Q(a,2),Q(b,3);u,v=advance(l,f)
            assert undo(u,v)==(l,f)
            assert u*u-5*v*v==-(l*l-5*f*f)
            seed_count+=1
    words_checked=0
    for length in range(7):
        for letters in product('><=0',repeat=length):
            s=''.join(letters);assert dec(enc(s))==s;words_checked+=1
    assert ''.join(enc('>=='))==''.join(enc('==<'))
    assert enc('>==')!=enc('==<')
    frame_words=[a+'='+b for a in '><=0' for b in '><=0']
    assert len({enc(s) for s in frame_words})==16
    assert len({''.join(enc(s)) for s in frame_words})==14
    addresses=0
    for length in range(1,9):
        for letters in product('xyz',repeat=length):
            s=''.join(letters);assert address_dec(address_enc(s))==s;addresses+=1
    assert address_enc('zz')=='z1'
    return {'date':'2026-10-09','all_assertions_passed':True,'status':'conditional identities and candidate encoding, not a complete geometry model',
      'pair_recurrence':{'range':'n=0..100','ordered_seed':['L=2','F=0'],'forward':['(L+5F)/2','(L+F)/2'],'inverse':['(5F-L)/2','(L-F)/2'],'invariant':'L²−5F² = 4(−1)^n','rows':rows,'additional_rational_seed_pairs':seed_count},
      'grouped_symbols':{'words_checked':words_checked,'max_length':6,'alphabet':list(code),'frames_grouped':16,'frames_flattened':14,'collision':{'first':'>==','second':'==<','first_groups':enc('>=='),'second_groups':enc('==<'),'same_flat_string':''.join(enc('>=='))},'assumption':'explicit group boundaries are retained'},
      'coordinate_encoding':{'strings_checked':addresses,'max_length':8,'alphabet':'xyz','format':'slash-separated runs; suffix counts extra repetitions','examples':{s:address_enc(s) for s in ['x','y','z','zx','zy','zz','zzz','xyzzx']},'meaning':'reversible address spelling; dimension count not inferred'},
      'open':['exact cancellation-to-echo rewrite','a definition and transition for each zero type','cross-layer decoding/re-encoding and timing','coordinate decoding into a geometric space with independent directions','no-same-particles rule and its actual domain']}
if __name__=='__main__':
    out=run();dest=Path(__file__).with_name('symbol_layers_results.json');dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'paired_steps':101,'rational_seeds':169,'grouped_words':out['grouped_symbols']['words_checked'],'coordinate_addresses':out['coordinate_encoding']['strings_checked'],'output':str(dest)}))
