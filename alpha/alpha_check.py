#!/usr/bin/env python3
"""Reproduce Marc's working alpha conjecture and the explored alternatives offline.

The stored experimental references are inputs, not independently verified here.
Passing checks establishes numerical consistency, not physical truth.
"""
from decimal import Decimal as D, getcontext

getcontext().prec = 70
PHI = (1 + D(5).sqrt()) / 2
L = [2, 1]
for _ in range(9):
    L.append(L[-1] + L[-2])
S = D(L[10] + 2 * L[4])
V0 = S + 1 / D(4 * L[4])
V1 = V0 + 1 / V0 / L[7]
V2 = S + 1 / (L[7] - 2 / PHI)
C = (V1 + 2 * V2) / 3
A = PHI ** -28
REFS = (
    ("CODATA 2022", D("137.035999177"), D("0.000000021")),
    ("Rb 2020", D("137.035999206"), D("0.000000011")),
    ("Cs 2018", D("137.035999046"), D("0.000000027")),
)


def candidate(r):
    return C - A / (1 - r)


def main():
    rows = [
        ("checkpoint", C),
        ("one layer", C-A),
        ("two layers, same sign", C-A-PHI**-37),
        ("two layers, alternating", C-A+PHI**-37),
        ("fixed alternating series", candidate(-PHI**-9)),
    ]
    assert (L[4], L[7], L[10], S) == (7, 29, 123, 137)
    assert abs(C-D("137.036000608393145653208386091")) < D("1e-27")
    # Compare the closed form with explicit layers, allowing a geometric tail.
    count = 12
    q = PHI**-9
    partial = C + sum((-1)**(j+1)*PHI**(-28-9*j) for j in range(count))
    tail_bound = A*q**count/(1-q)
    assert abs(partial-candidate(-q)) <= tail_bound + D("1e-60")
    print("Stored references; residuals in supplied standard uncertainties.")
    print(f"{'candidate':28} {'1/alpha':>24}  CODATA       Rb       Cs")
    for name, value in rows:
        z = " ".join(f"{(value-x)/u:+8.3f}" for _, x, u in REFS)
        print(f"{name:28} {value:24.18f} {z}")
    print(f"phi^-46 = {PHI**-46:.12E}")
    print("\nInverse signed ratios and intervals:")
    for name, x, u in REFS:
        r = 1-A/(C-x)
        lo, hi = 1-A/(C-x-u), 1-A/(C-x+u)
        assert lo < r < hi
        assert abs(candidate(r)-x) < D("1e-60")
        print(f"{name}: {r:+.8f} [{lo:+.8f}, {hi:+.8f}]")
    print("\nExplored alternatives, not replacements for the fixed conjecture:")
    e = D(1).exp()
    ratios = [("one layer", D(0)), ("phi^-9", q), ("1/10", D(1)/10),
              ("1/9", D(1)/9), ("1/e", 1/e), ("1-1/e", 1-1/e),
              ("phi^-10", PHI**-10), ("exp(-4)", D(-4).exp())]
    for label, ratio in ratios:
        for sign in (1, -1):
            value = candidate(sign*ratio)
            z = " / ".join(f"{(value-x)/u:+.4f}" for _, x, u in REFS)
            print(f"{label:10} {'same sign' if sign == 1 else 'alternating':11} "
                  f"{value:.18f}  {z}")
    print("PASS: checkpoint, series tail, and inverse round trips.")
    print("These checks do not establish the conjecture's physical identification.")


if __name__ == "__main__":
    main()
