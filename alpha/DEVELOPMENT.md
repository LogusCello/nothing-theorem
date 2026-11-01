# Alpha: development history and detailed review

For the concise construction and runnable equation, start with [the alpha note](README.md). This page retains the fuller history and review.

**STATED — Marc's current idea.** The Nothing Theorem's Lucas-number and nested phi-layer structure may yield the inverse fine-structure constant through the construction below. This is a proposed route from the theorem to alpha, not a completed derivation. A *conjecture* is a statement proposed as true but not established.

This note records the idea, the numerical calculation, its development, and the missing steps together. The arithmetic can be checked independently of the proposed physical interpretation. Dates below record the supplied October 2026 development notes; the later documentation review does not establish priority or novelty.

## 1. Connection to the existing theorem

[THEOREM.md](../THEOREM.md), sections 1–3, defines the reversible Fibonacci update, its Lucas trace, and the two roots phi and psi:

`L0 = 2, L1 = 1, L(n+2) = L(n+1) + L(n)`

`phi = (1 + sqrt(5))/2`, `psi = (1 - sqrt(5))/2 = -1/phi`.

Those rules produce `L4 = 7`, `L7 = 29`, and `L10 = 123`. Their indices are three steps apart. The theorem proves identities for those sequences; it does **not yet force** the choice of these indices or the physical identification with alpha. That missing bridge is part of the conjecture.

## 2. The checkpoint

**BUILT / COMPUTED.** Define:

```text
S  = L10 + 2*L4                         = 137
V0 = S + 1/(4*L4)
V1 = V0 + (1/V0)/L7
V2 = S + 1/(L7 - 2/phi)
C  = (V1 + 2*V2)/3                      = 137.03600060839314565...
```

The quantity being proposed is **1/alpha**, not alpha itself. Alpha is dimensionless and characterizes electromagnetic coupling; the stored references below concern its low-energy value.

**STATED — readings supplied by Marc on 2026-10-29.** These explanations were written after the checkpoint was assembled, so they record its intended meaning rather than prove that it is the unique consequence of the theorem:

- **1/(4*L4):** the whole splits into two and both split again in the same moment, giving `2*2=4`, on the L4 loop. This four is a proposed computation count; it is not Lucas L0, which equals 2.
- **2/phi:** L0 supplies 2, moved one phi step back. The exact identity `2/phi = -2*psi` makes `L7-2/phi = L7+2*psi`: the Lucas loop plus twice the mirror root.
- **Weights 1:2:** when one side of the equilibrium moves, the other has to move double. Why this selects this particular weighted average remains open.
- **Three phis:** `(-phi)*(-phi)+(-phi)=1`, the reversed order also gives 1, and `1/phi-phi=-1`. These are exact algebraic identities. The interpretation is that every three layers count as a new, smaller 1.
- **25 and 2.5 loops:** a mirror around the center 5, described as “0 three times rotated, two and a half times computed.” The earlier correction divisor 25 had readings `20+5`, `16+8+1`, `22.5+2.5`, and `3^2+4^2`. Neither 25 nor 2.5 appears in the current formula. The old derivation has not been recovered.

## 3. The nested layers and the fixed candidate

**STATED.** The bracket pairing `(1...9) -> ((2...8)) -> (((3...7))) -> ...` motivates layers 28, 37, 46, nine indices apart. This notation is a proposed interpretation of the paired digits, not an established operation deriving the exponents.

The October 29 notes record two choices:

1. The checkpoint is the base layer; there is no additional phi^-19 correction.
2. Successive brackets flip sign, represented by `() -> [()] -> ([()])`. The correction starts negative and alternates thereafter.

**Working conjecture, with these choices fixed:**

```text
1/alpha = C - phi^-28 + phi^-37 - phi^-46 + ...
        = C - phi^-28/(1 + phi^-9)
        = 137.03599921949654087569...
```

**PROVED, conditional on the chosen series.** Since `0 < phi^-9 < 1`, the correction is an absolutely convergent geometric series. Its closed form follows from `sum(r^j, j>=0)=1/(1-r)` with `r=-phi^-9`. This proves the sum, not the identification with nature's alpha.

## 4. Reproducible comparisons

Run `python3 alpha/alpha_check.py` from the repository root. It uses 70-digit Decimal arithmetic, computes the Lucas numbers, checks the closed form against a finite series with a tail bound, and prints all the variants below. `python3 run_all.py` includes it.

The references are **stored inputs inherited from the draft**:

| Label | Stored 1/alpha | Stored standard uncertainty |
|---|---:|---:|
| CODATA 2022 | 137.035999177 | 0.000000021 |
| Rb 2020, attributed to Morel et al. | 137.035999206 | 0.000000011 |
| Cs 2018, attributed to Parker et al. | 137.035999046 | 0.000000027 |

Their original publications, adjustment details, and possible correlations were not independently source-verified in the October review. CODATA denotes a recommended value, not simply a separate electron g-2 measurement. The supplied uncertainties are of relative order 10^-10; printing more digits does not make them more precise.

For each row, the residual is `(candidate - reference)/reference_uncertainty`:

| Candidate for 1/alpha | Value | CODATA | Rb | Cs |
|---|---:|---:|---:|---:|
| Checkpoint C | 137.036000608393 | +68.16 | +127.49 | +57.87 |
| C - phi^-28 | 137.035999201225 | +1.15 | -0.43 | +5.75 |
| C - phi^-28 - phi^-37 | 137.035999182713 | +0.27 | -2.12 | +5.06 |
| C - phi^-28 + phi^-37 | 137.035999219737 | +2.04 | +1.25 | +6.43 |
| **Fixed alternating series** | **137.035999219497** | **+2.02** | **+1.23** | **+6.43** |

These are numerical residuals in units of the supplied uncertainty, not discovery significance levels. The stored Rb and Cs values differ by about 5.49 combined standard uncertainties if independent errors are assumed. A candidate close to one need not fit the other. The phi^-46 correction is about 2.44e-10, smaller than all three stored uncertainties; its physical value has not been independently observed.

## 5. What was known when

- **Earlier checkpoint:** C and the first phi^-28 correction were selected while the experimental target was known.
- **2026-10-29:** the session notes report that Marc named 37 and 46 before their numerical contributions were calculated. Both same-sign and alternating variants were subsequently compared with the known references.
- **Later on 2026-10-29:** alternating signs and the checkpoint as the base layer were recorded as the chosen rule.
- **2026-10-31:** an inverse calculation explored other ratios, including a same-sign 1/10 correction. This is a separate alternative, not a silent change to the October 29 candidate.

Naming the next indices before calculating them is part of the idea's history. It is not an independent experimental prediction, because the target was already available during development. A prospective test requires a fixed formula and a comparison criterion recorded before new independent data are examined.

## 6. The inverse calculation and Euler connection

For a signed ratio `r=s*q`, where `0<=q<1` and `s=+1` or `-1`, consider the family

`X = C - a/(1-r)`, with `a=phi^-28`.

Solving backwards from a target X gives `r=1-a/(C-X)`. For a target interval `X +/- u` wholly below C, the corresponding endpoints are `1-a/(C-X-u)` and `1-a/(C-X+u)`.

| Stored target | Needed r | Interval from target +/- one uncertainty |
|---|---:|---:|
| CODATA 2022 | +0.0169 | +0.0023 to +0.0311 |
| Rb 2020 | -0.0034 | -0.0113 to +0.0044 |
| Cs 2018 | +0.0994 | +0.0835 to +0.1147 |

The same-sign choice q=1/10 yields `137.035999044872704...`, about -0.0418 Cs uncertainties away, but -6.29 CODATA and -14.65 Rb uncertainties away. It is close, not exactly equal. Choosing which reference to fit after seeing the result does not validate the theory. The script retains all eight explored ratios and both signs so this selection is visible.

The shared algebra with retry rounds is the geometric series: passing a positive fraction q onward produces tail `q/(1-q)`. Thus q=1/10 gives 1/9. A signed alternating bounce instead has a different signed sum. This does not establish a physical equivalence between hash tables, the Loop Grid, and electromagnetic coupling.

For completeness, under independent uniform hashing with load `lambda = keys/slots`, the large-population slot-cost models are `A=1/(1-exp(-lambda))` for first-wins and `B=exp(lambda)/lambda` for singleton-only retries. At load 1 these are e/(e-1) and e. At load ln(phi^2), A is phi, but **B is phi^2/ln(phi^2), approximately 2.72025**, not phi^2. Empty slots are not guaranteed in finite tables. These corrected observations explain the exploratory connection; they are not another claimed physical finding.

## 7. Chance estimates and limitations

The old drafts print 7.4% for a particular log-uniform residual simulation, and about 0.3% for a uniform q in [0,0.5] landing near the Cs-fitted q. These are illustrative baselines selected after exploration. They do not cover the freedom to choose the checkpoint, coefficients, base, exponents, signs, or measurement.

The old 6% calculation treats eight candidates times three references as 24 independent identical trials. That assumption is not established; the measurements/candidates are related, both signs were inspected, and one candidate is outside the chosen q interval. It should not be quoted as a calibrated probability that the finding occurred by chance.

A separate historical search over Lucas indices for mp/me, e, pi, and a Planck/Higgs mass ratio reported no strong additional matches under its own toy baseline. That search is not evidence that this formula uniquely describes alpha, and it is not required to reproduce the present candidate.

## 8. What would complete the route

**OPEN.** Derive the choices L10, L4, L7, 1/(4*L4), 2/phi, and weights 1:2 from a sufficiently explicit theorem rule, without using the target to select them. Derive the starting exponent 28, step 9, and alternating signs from that same rule. Explain why the result represents the low-energy electromagnetic coupling. Keep the fixed candidate distinct from alternative fits and specify an empirical test that could count against it.

This is Marc's current idea of how to reach alpha from the theorem. Its calculation is reproducible; its physical identification and the missing derivation remain open.

## Historical record

The [original draft archive](history/README.md) preserves the supplied alpha and Euler drafts and scripts verbatim, including superseded statements. This page supplies the current framing and corrections. No claim is made here that an OpenAI research announcement validates this construction.
