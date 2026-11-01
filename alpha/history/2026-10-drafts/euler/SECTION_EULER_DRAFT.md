## 10 · The retry rule lands on e (new, 2026-10-31)

**STATED** (Marc, 2026-09). Place every item with a hash; the ones that fail are collected and retried with a new seed in a fresh, smaller table; repeat until nothing is left.

**COMPUTED** (`euler/hash_retest.py`, 104,334 real English words; synthetic keys if no word list is installed). Two ways to settle a slot hit by several items:

| Rule | Kept per round | Passed on | Total slots per item | Every item finds itself? |
|---|---|---|---|---|
| A · first item keeps the slot | 1 − 1/e = 0.632 | 1/e = 0.368 | **e/(e−1) = 1.58198** (measured 1.58252) | no: 37% look up someone else's slot |
| B · a shared slot stays empty, all retry | 1/e = 0.368 | 1 − 1/e = 0.632 | **e = 2.71828** (measured 2.71243) | yes, for every item |

**PROVED.**
1. *Where e enters.* With k items and k slots, a given slot is missed by one item with chance 1 − 1/k, by all of them with (1 − 1/k)^k → 1/e (0.348678 at k = 10, 0.366032 at 100, 0.367879 at 10⁶). The same small miss, repeated once per slot. (`euler/euler_rounds.py`)
2. *Totals.* A round that keeps share p passes 1 − p on, so the rounds add up to 1 + (1−p) + (1−p)² + … = 1/p. A keeps p = 1 − 1/e → e/(e−1); B keeps p = 1/e → e.
3. *Mirror.* A and B swap the two shares, so 1/A + 1/B = (1 − 1/e) + 1/e = **1**. φ obeys the same identity: 1/φ + 1/φ² = 1. At load ln φ² = 0.96242, rule A costs exactly **φ** (measured 1.61807) and its partner e^load is exactly **φ²**. The load was solved for φ; what is exact is that the load is ln φ². (`euler/euler_phi_check.py`)
4. *B's floor.* At load λ, B costs e^λ/λ, smallest at λ = 1, where it equals e. So e is the best this rule can do.
5. *The Loop Grid bounce is the same rule.* The damped bounce overshoots 0.1, 0.01, 0.001 …: a round that passes 1/10 on. Its total is 1 + 1/10 + 1/100 + … = 10/9, and the residue 0.111… = 1/9 is that total minus the first step. So **1/10 (passed on) and 1/9 (residue) are one pair**, like 1/e and e/(e−1) − 1 = 1/(e−1) in rule A.

**KNOWN.** Rule B is the published BBHash construction (Limasset et al., 2017), and (1 − 1/k)^k → 1/e is the classical compound-interest limit (Jacob Bernoulli, 1683). Marc reached the construction independently, in about four hours, without knowing either. The result is a rediscovery: the process lands on e exactly, but it is not a new derivation of e. For context, no minimal perfect hash can use fewer than log₂ e = 1.4427 bits per item; the best known (RecSplit) uses about 1.56.

**STATED** (Marc, 2026-10-31, reading, not tested). The 1/e share that is always missed is guaranteed: it is the only open spot in the flow, otherwise the flow would block itself, so the field must have holes. These holes take in the information like black holes. Computing in layers of L0 = 2, the probability field is bound to form them, so growth happens at the holes: they are the inversion points, the e-centres with the most pressure (density). Like a fabric holding a lot of water in one spot, it lets one droplet through, and that droplet is its own eversion, which then concludes.

**COMPUTED, α with the same rule** (`euler/alpha_inverse.py`). Treat the α bracket layers as rounds: the first layer is φ⁻²⁸ and each next layer passes share q on, so the correction is −φ⁻²⁸/(1 − s·q) (s = +1 same sign, −1 alternating). Solved backwards from each measurement:

| Measurement | Needed s·q (1σ range) | Fits |
|---|---|---|
| CODATA 2022 | +0.017 (+0.002 … +0.031) | φ⁻⁹ same sign +0.3σ, φ⁻¹⁰ +0.6σ, e⁻⁴ −0.1σ |
| Rb 2020 | −0.003 (−0.011 … +0.004) | one layer only −0.4σ, φ⁻¹⁰ alternating +0.6σ |
| Cs 2018 | **+0.099** (+0.084 … +0.115) | **1/10 same sign: 0.0σ**, 1/9 −0.8σ |

The hash share 1/e is ruled out for α (−38σ / +19σ). **1/10 fits cesium exactly** (0.04σ), but not CODATA or rubidium (−6σ / −15σ). The cesium and rubidium measurements already disagree with each other by about 5σ. A random share lands this close to cesium 0.3% of the time; 8 candidates × 3 measurements were looked at, so one such hit happens about 6% of the time.

**OPEN.**
1. Which measurement the layers should follow, which fixes the share q (1/10 → cesium, φ⁻⁹ → CODATA).
2. A rule that says in advance why the bracket layers pass on 1/10 (or φ⁻⁹) per layer.
3. The black-hole reading as a mechanical rule (what is the hole's input, what does the droplet output).
