"""Closed forms for both hash versions vs measured, and where phi sits.  Run: python3 -I euler_phi_check.py"""
import math, random, importlib.util, sys
spec = importlib.util.spec_from_file_location("h", __file__.replace("euler_phi_check.py", "hash_retest.py"))
sys.argv = [sys.argv[0]]; src = open(spec.origin).read().split("words = load_words")[0]; ns = {}; exec(src, ns)
words = ns['load_words']()
e, phi = math.e, (1 + 5**.5) / 2
A = lambda load: 1 / (1 - math.exp(-load))          # first-wins: total slots per key
B = lambda load: math.exp(load) / load              # both-leave: total slots per key
def meas(load, bl):
    r = ns['test'](words, 1/load, bl); return r['bits_per_key']
print(f"A first-wins, load 1:   formula e/(e-1) = {A(1):.5f}   measured {meas(1, False):.5f}")
print(f"B both-leave, load 1:   formula e       = {B(1):.5f}   measured {meas(1, True):.5f}")
best = min((B(l/1000), l/1000) for l in range(100, 3000))
print(f"B best load = {best[1]:.3f} -> {best[0]:.5f} bits/key (= e, its floor)")
lphi = 2 * math.log(phi)
print(f"A at load 2*ln(phi) = ln(phi^2) = {lphi:.5f}: formula {A(lphi):.5f} (phi = {phi:.5f})   measured {meas(lphi, False):.5f}")
print(f"gap A(1) to phi: {phi - A(1):.5f} ({(phi - A(1))/phi*100:.2f}% under)")
print(f"floor for any MPHF log2(e) = {math.log2(e):.5f};  RecSplit ~1.56;  phi = {phi:.5f}")
