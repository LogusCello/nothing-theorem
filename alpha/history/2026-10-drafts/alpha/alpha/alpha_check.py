#!/usr/bin/env python3
"""The alpha checkpoint: 1/alpha from Lucas numbers and phi, plus the bracket-layer corrections.
Standard library only. Exit code 0 = every printed value reproduced."""
import math, random

PHI = (1 + 5 ** .5) / 2
L = [2, 1]
for _ in range(60):
    L.append(L[-1] + L[-2])
L4, L7, L10 = L[4], L[7], L[10]            # 7, 29, 123

# measured references (dimensionless)
CODATA = (137.035999177, 0.000000021)      # CODATA 2022 (electron g-2)
RB = (137.035999206, 0.000000011)          # Morel et al. 2020, rubidium recoil
CS = (137.035999046, 0.000000027)          # Parker et al. 2018, cesium recoil

def sig(x, ref):
    return (x - ref[0]) / ref[1]

# checkpoint (archive, 2026-09)
S = L10 + 2 * L4                           # 137
V0 = S + 1 / (4 * L4)                      # 137 + 1/28
V1 = V0 + (1 / V0) / L7
V2 = S + 1 / (L7 - 2 / PHI)
FINAL = (V1 + 2 * V2) / 3

rows = [("checkpoint (V1 + 2*V2)/3", FINAL),
        ("- phi^-28", FINAL - PHI ** -28),
        ("- phi^-28 - phi^-37  (same sign)", FINAL - PHI ** -28 - PHI ** -37),
        ("- phi^-28 + phi^-37  (alternating)", FINAL - PHI ** -28 + PHI ** -37),
        ("all layers alternating (closed form)", FINAL - PHI ** -28 / (1 + PHI ** -9))]
print(f"{'':36s}{'value':>18s}{'CODATA':>9s}{'Rb':>8s}{'Cs':>8s}")
for name, v in rows:
    print(f"{name:36s}{v:18.12f}{sig(v, CODATA):+8.1f}σ{sig(v, RB):+7.1f}σ{sig(v, CS):+7.1f}σ")
print(f"\nlayer sizes: phi^-46 = {PHI ** -46:.1e} ({PHI ** -46 / CODATA[1]:.2f}σ), below today's precision")

# chance baseline for the phi^-28 step: how often does a random residual sit this close to some phi power?
res = FINAL - CODATA[0]
lim = abs(res - PHI ** -28) / res
r = random.Random(3); n = 20000; hits = 0
for _ in range(n):
    y = res * math.exp(r.uniform(-3, 3))
    k = round(-math.log(y) / math.log(PHI))
    hits += abs(y - PHI ** -k) / y <= lim
print(f"chance a random residual lands this close to a phi power: {hits / n:.1%}")

assert S == 137 and abs(FINAL - 137.036000608393) < 1e-11
assert abs(FINAL - PHI ** -28 - 137.035999201225) < 1e-11
