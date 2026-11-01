"""Inverse solver for the alpha layers, using the retry-hash rule (each round passes a fixed share q on).
Layers: correction = -phi^-28 * (1 + s q + (s q)^2 + ...) = -phi^-28 / (1 - s q),  s = +1 same sign, -1 alternating.
Solve q from the measured value, then check named candidates.  Run: python3 alpha_inverse.py"""
import math
phi = (1 + 5 ** .5) / 2
L = [2, 1]
for _ in range(20): L.append(L[-1] + L[-2])
S = L[10] + 2 * L[4]; V0 = S + 1 / (4 * L[4]); V1 = V0 + (1 / V0) / L[7]; V2 = S + 1 / (L[7] - 2 / phi)
CP = (V1 + 2 * V2) / 3
a = phi ** -28
MEAS = {"CODATA 2022": (137.035999177, 0.000000021), "Rb 2020": (137.035999206, 0.000000011), "Cs 2018": (137.035999046, 0.000000027)}
print(f"checkpoint {CP:.12f}   first layer phi^-28 = {a:.6e}\n")
for name, (x, u) in MEAS.items():
    r = CP - x                                   # total correction needed
    sq = 1 - a / r; lo = 1 - a / (r - u); hi = 1 - a / (r + u)
    print(f"{name:12s}: needed total {r:.4e} = {r / a:.4f} x phi^-28  ->  s*q = {sq:+.4f}  (1 sigma: {lo:+.4f} .. {hi:+.4f})")
print()
cands = {"0 (one layer only)": 0, "phi^-9 (layer step 9)": phi ** -9, "1/10": 0.1, "1/9": 1 / 9, "1/e (hash leftover)": 1 / math.e,
         "1-1/e": 1 - 1 / math.e, "phi^-10": phi ** -10, "1/e^4": math.exp(-4)}
print(f"{'q':24s}{'same sign':>26s}{'alternating':>26s}   (sigma vs CODATA 2022 / Rb 2020 / Cs 2018)")
for n, q in cands.items():
    row = []
    for s in (1, -1):
        v = CP - a / (1 - s * q)
        row.append(" / ".join(f"{(v - x) / u:+.1f}" for x, u in (MEAS['CODATA 2022'], MEAS['Rb 2020'], MEAS['Cs 2018'])))
    print(f"{n:24s}{row[0]:>26s}{row[1]:>26s}")

# chance: how often does a random share q in 0..0.5 land as close to the Cs value (in its sigma) as 1/10 does?
x, u = MEAS['Cs 2018']; need = 1 - a / (CP - x); w = (1 - a / (CP - x - u)) - need
print(f"\nCs wants q = {need:.4f}; 1/10 is {abs(0.1 - need) / abs(w):.2f} sigma from it. A random q in 0..0.5 lands that close {2 * abs(0.1 - need) / 0.5:.1%} of the time;")
print("8 candidates x 3 measurements were looked at, so one such hit is not unusual (~" + f"{1 - (1 - 2 * abs(0.1 - need) / 0.5) ** 24:.0%}" + " for at least one).")
