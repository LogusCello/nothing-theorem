## 9 · The α checkpoint (replaces "Numerical curiosities")

The fine-structure constant α ≈ 1/137.036 sets the strength of electromagnetism. It is dimensionless, measured to 12 digits, and no accepted theory derives it. That makes it the cleanest test for any idea that claims to produce physical numbers.

**STATED** (Marc). 137 is built from the Lucas loop counts L10 = 123 and L4 = 7, and refined by the next loops. Corrections come from nested bracket layers whose outer pairs add up to 10, (1…9) → ((2…8)) → (((3…7))) → …, so the layers are 28, 37, 46 …, nine steps apart. Each layer is a smaller φ step: φ⁻²⁸, φ⁻³⁷, φ⁻⁴⁶. The 25 / 2.5-loop part of the derivation is being retraced from older notes.

**STATED: where the checkpoint's parts come from** (Marc, 2026-10-29; written after the formula, so these are readings, not a derivation that forces the formula):
- **1/(4·L4):** the 100% splits into two, and both split again in the same moment (2 × 2 = 4, the L0 count of computation steps), on the L4 loop.
- **2/φ:** the smallest step is −1, reached by moving in −φ steps. L0 = 2 is the first computed 0, so take 2 and move one φ back. **PROVED:** 2/φ = −2ψ exactly (ψ = −1/φ, the mirror rotation), so L7 − 2/φ = L7 + 2ψ is L0 times the mirror rotation added to the loop.
- **Weights 1 : 2 (V1 + 2·V2):** when one side of the equilibrium moves, the other has to move double.
- **Three φs:** ((−φ)(−φ) + (−φ)) = 1 and ((−φ) + (−φ)(−φ)) = 1 (exact, φ² − φ = 1), and 1/φ − φ = −1. Every step is built from three φs; every three layers count as a new, smaller 1.
- **25 and 2.5:** the same mirror around the center 5 ("0 three times rotated, two and a half times computed"). 25 does not appear in the current formula; it was the correction divisor in an earlier version (four derivations in the archive: 20+5, 16+8+1, 22.5+2.5, 3²+4²).

**COMPUTED** (`alpha/alpha_check.py`):

| Expression | Value | vs CODATA 2022 | vs Rb 2020 |
|---|---|---|---|
| S = L10 + 2·L4 | 137 | | |
| V0 = S + 1/(4·L4) | 137.035714286 | | |
| V1 = V0 + (1/V0)/L7 | 137.035965919 | | |
| V2 = S + 1/(L7 − 2/φ) | 137.036017953 | | |
| checkpoint = (V1 + 2·V2)/3 | 137.036000608 | +68σ | |
| − φ⁻²⁸ | 137.035999201 | +1.2σ | −0.4σ |
| − φ⁻²⁸ − φ⁻³⁷ (same sign) | 137.0359991827 | +0.3σ | −2.1σ |
| − φ⁻²⁸ + φ⁻³⁷ (alternating) | 137.0359992197 | +2.0σ | +1.2σ |
| all layers alternating: − φ⁻²⁸/(1 + φ⁻⁹) | 137.0359992195 | +2.0σ | +1.2σ |

**How to read it.**
- The checkpoint and the 28 were found while looking at the target. A random residual sits as close to some φ power 7.4% of the time.
- Layers 37 and 46 were named from the bracket rule **before** they were computed. That makes them the first prediction in this project.
- The same checkpoint rule (three Lucas slots) does **not** reproduce other constants: mp/me, e, π and Planck/Higgs all land at chance level. So far the rule is specific to α.
- φ⁻⁴⁶ ≈ 2.4×10⁻¹⁰ is about 100× below today's precision. That digit of α is a prediction for future measurements.

**OPEN.**
1. Sign rule: **alternating** (Marc, 2026-10-29: each layer is the next bracket type, () → [()] → ([()]), and each bracket flips + and −). The full series sums to checkpoint − φ⁻²⁸/(1 + φ⁻⁹).
2. Layer 1: the checkpoint itself is layer 1 (Marc, 2026-10-29: 1 sits in every layer until it attaches to 0, so 0 and 1 are the base layer and everything else layers on top). So φ⁻¹⁹ is not a correction term; corrections start at the second bracket.
3. A rule that **produces** the checkpoint's parts (1/(4·L4), 2/φ, 1 : 2, the choice of L10, L4, L7) step by step, instead of explaining them afterwards. Then the whole formula, not only the layers, is a prediction.
4. The cesium and rubidium measurements of α disagree with each other by about 5σ. The φ-layer values sit near rubidium and CODATA, not cesium.

This is not a derivation of α yet. It is a fixed, dated rule with one real prediction in it.
