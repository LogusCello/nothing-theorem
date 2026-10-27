#!/usr/bin/env python3
"""Section 1b: the mirror sum, Cassini's identity and the ratio's over/under swing share one sign, (-1)^n."""
import sys
from decimal import Decimal, getcontext

N = 500
getcontext().prec = 250
PHI = (1 + Decimal(5).sqrt()) / 2

def fib(n):
    a, b = 0, 1
    for _ in range(abs(n)):
        a, b = b, a + b
    return a if n >= 0 else (-1) ** (abs(n) + 1) * a

F = {n: fib(n) for n in range(-N - 1, N + 2)}
fails = 0
def check(ok, what):
    global fails
    if not ok:
        fails += 1
        print("FAIL", what)

prev_miss = None
for n in range(2, N + 1):
    s = (-1) ** n
    # mirror sum: 0 when s = +1 (even n), 2F(n) when s = -1 (odd n)
    check(F[n] + F[-n] == (0 if s == 1 else 2 * F[n]), f"mirror n={n}")
    # Cassini: F(n+1)F(n-1) - F(n)^2 = (-1)^n
    check(F[n + 1] * F[n - 1] - F[n] ** 2 == s, f"cassini n={n}")
    # ratio r = F(n)/F(n-1) is over phi iff a^2 - ab - b^2 > 0; exactly that quantity is -s
    a, b = F[n], F[n - 1]
    check(a * a - a * b - b * b == -s, f"over/under n={n}")
    # the miss shrinks every step
    if n <= 230:
        miss = abs(Decimal(a) / Decimal(b) - PHI)
        check(prev_miss is None or miss < prev_miss, f"shrink n={n}")
        prev_miss = miss

print("n   F(n)  F(n)/F(n-1)  vs phi   F(n)+F(-n)")
for n in range(2, 11):
    r = F[n] / F[n - 1]
    print(f"{n:<3} {F[n]:<5} {r:<12.6f} {'over ' if r > float(PHI) else 'under'}    {F[n] + F[-n]}")
print(f"\nchecked n = 2..{N} exactly: {'all hold' if not fails else f'{fails} failures'}")
sys.exit(1 if fails else 0)
