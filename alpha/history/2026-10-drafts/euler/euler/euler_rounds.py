"""Where e comes from in the retry hash: round by round, real words, load 1.  Run: python3 -I euler_rounds.py"""
import math
src = open(__file__.replace("euler_rounds.py", "hash_retest.py")).read().split("words = load_words")[0]; ns = {}; exec(src, ns)
words = ns['load_words']()
e = math.e
print("(1-1/m)^m for m = 10, 100, 1000, 10^6:", [round((1-1/m)**m, 6) for m in (10, 100, 1000, 10**6)], " 1/e =", round(1/e, 6))
for name, bl in (("A first-wins", False), ("B both-leave", True)):
    rounds, _ = ns['build'](words, 1.0, bl)
    print(f"\n{name}: round  keys_in  placed  kept_share  left_share")
    k = len(words)
    for i, (size, bits, seed) in enumerate(rounds[:6]):
        print(f"   {i:2d}  {k:7d}  {len(bits):7d}   {len(bits)/k:.4f}     {1-len(bits)/k:.4f}")
        k -= len(bits)
print(f"\ntheory: A keeps 1-1/e = {1-1/e:.4f}, leaves 1/e = {1/e:.4f};  B keeps 1/e, leaves 1-1/e (mirror)")
A, B = e/(e-1), e
print(f"A = 1/(1-1/e) = {A:.5f}   B = 1/(1/e) = {B:.5f}   1/A + 1/B = {1/A + 1/B:.12f}")
phi = (1+5**.5)/2
print(f"phi pair: 1/phi + 1/phi^2 = {1/phi + 1/phi**2:.12f}   (A at load ln phi^2 = phi, its partner e^load = {math.exp(2*math.log(phi)):.5f} = phi^2)")
