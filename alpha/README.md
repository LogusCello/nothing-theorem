# My current route to alpha

I started with the Nothing Theorem's ideas about Lucas loops, mirrored steps, and nested layers. Following those ideas led me to the expression below for **1/alpha**, the inverse fine-structure constant. This is my current working conjecture. Here are the numbers, how I reached them, and the calculation for anyone to try or correct.

## The numbers

The formula gives **137.03599921949654**.

| Reference used | Reference value for 1/alpha | Difference in standard uncertainties |
|---|---:|---:|
| CODATA 2022 | 137.035999177 ± 0.000000021 | +2.02σ |
| Rubidium 2020 | 137.035999206 ± 0.000000011 | +1.23σ |
| Cesium 2018 | 137.035999046 ± 0.000000027 | +6.43σ |

Here σ means the reference's stated uncertainty: `(formula - reference) / uncertainty`. The expression is close to the stored rubidium and CODATA values, but disagrees more strongly with cesium. These references also disagree with each other. They are the values used in my notes; their original sources were not independently rechecked for this update.

## What I did to get there

The theorem uses the Lucas sequence, starting with 2 and 1 and adding the previous two numbers to get the next. I used **L4 = 7, L7 = 29, L10 = 123**: loop indices three steps apart.

1. Build 137 as `L10 + 2*L4`.
2. Form two refinements using the L4 and L7 loops, then combine them with weights 1:2. My interpretation is a double split for the factor 4, one backward phi step for `2/phi`, and the other side moving double for the weights.
3. Add smaller, alternating corrections at exponents **28, 37, 46, …**. These come from my reading of nested bracket pairs: 19, 28, 37, 46, nine apart. I treat the checkpoint itself as the base layer, so the corrections start at 28; each next bracket flips the sign.

These are the choices and interpretations behind the construction. I have not yet shown that the theorem uniquely requires them. [The full development notes](DEVELOPMENT.md) keep the explanations, dates, alternatives, and unresolved steps.

## The equation

Let `phi = (1 + sqrt(5))/2`. Define:

```text
S  = L10 + 2*L4 = 137
V0 = S + 1/(4*L4)
V1 = V0 + 1/(V0*L7)
V2 = S + 1/(L7 - 2/phi)
C  = (V1 + 2*V2)/3
```

My proposed value is:

```text
1/alpha = C - phi^-28 + phi^-37 - phi^-46 + ...
        = C - phi^-28/(1 + phi^-9)
        ≈ 137.03599921949654
```

The series and closed form are mathematically equivalent. Whether this expression gives the physical constant is the conjecture.

| Step in the construction | Value |
|---|---:|
| Checkpoint C | 137.036000608393 |
| Subtract phi^-28 | 137.035999201225 |
| Add phi^-37 | 137.035999219737 |
| Sum all alternating layers | 137.035999219497 |

## Try it or correct it

This short Python calculation needs nothing installed beyond Python:

```python
from decimal import Decimal as D, getcontext

getcontext().prec = 50
phi = (1 + D(5).sqrt()) / 2
L4, L7, L10 = D(7), D(29), D(123)
S = L10 + 2 * L4
V0 = S + 1 / (4 * L4)
V1 = V0 + 1 / (V0 * L7)
V2 = S + 1 / (L7 - 2 / phi)
C = (V1 + 2 * V2) / 3
print(C - phi**-28 / (1 + phi**-9))
```

For the comparisons, alternative formulas, and numerical checks, run:

```bash
python3 alpha/alpha_check.py
```

The checkpoint and first correction were developed with the target known. My notes record naming 37 and 46 before calculating their contributions; the sign choices were then explored. I include that history so readers can judge the result with the same information I have.

I am an autodidact, and expressing the whole idea in mathematical notation is still difficult for me. I used Claude Opus and ChatGPT Astra to help express and check the calculations, followed by a Codex review and reproducible scripts. These are AI-assisted checks, not independent scientific validation. The idea is mine; corrections to the arithmetic, the reasoning, or the connection to measurements are welcome.

[Original drafts and scripts](history/README.md) are preserved alongside the fuller notes. This is a proposed route to alpha that others can examine, not a claim that the derivation is complete.
