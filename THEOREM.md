# The Nothing Theorem: formal write-up

This is a thought experiment that turned into a small, checkable piece of mathematics. It starts from a sentence about nothing. From there it builds a reversible two-path process (Fibonacci/Lucas), a mirror alphabet of `>`, `=`, `<`, and a box rule for how hot and cold sides pair up. Everything below is labelled honestly:

| Label | Meaning |
|---|---|
| **STATED** | the author's idea in his framing (see [IN_MY_WORDS.md](IN_MY_WORDS.md)) |
| **PROVED** | a mathematical argument is given (here or in `cycle-closing/REVIEW.md`) |
| **COMPUTED** | rerun by a script in this repo; `python3 run_all.py` reproduces it |
| **BUILT** | a modelling choice made to turn an idea into a runnable rule |
| **OPEN** | not settled yet |

None of this claims to derive physics. The claims are about the stated rules and nothing more.

Notation: F(n) is Fibonacci (F0=0, F1=1), L(n) is Lucas (L0=2, L1=1, L2=3), φ = (1+√5)/2 ≈ 1.618, and ψ = (1−√5)/2 = −1/φ ≈ −0.618.

---

## 0 · Foundation

**STATED.** *"Nothing is not Nothing, and Nothing is not Everything. Nothing is Something which is neither Nothing nor Everything, but it might also be both at the same time."*

The project takes this as a design brief rather than an axiom to prove: build a process where the *state* is never empty, yet some *reading* of it comes out as exactly 0. Sections 1–3 make that precise.

**OPEN.** "Nothing" is used in several senses (zero, the empty set, an unobserved state, a boundary). A full formalization must pick one domain. Four-valued logic (true/false/neither/both) and the von Neumann step ∅ → {∅} are candidate readings.

## 1 · The mirror equilibrium: a full state that reads as zero

Run the Fibonacci rule forwards and backwards from the same seed. Reversing F(n+1)=F(n)+F(n−1) gives F(−1)=1, F(−2)=−1, F(−3)=2, …

**PROVED.** F(−n) = (−1)^(n+1)·F(n). Therefore

    F(n) + F(−n) = 0        for even n
                 = 2·F(n)   for odd n

**PROVED.** The state update (u,v) → (v,u+v) is reversible, with inverse (u,v) → (v−u,u). So the pair *never loses information*, while the reading n ↦ F(n)+F(−n) returns to 0 on every second step. That is the theorem's "nothing that is something": **a zero reading of a non-empty state.**

**PROVED (generalized seeds).** With G(0)=a, G(1)=b: G(n)+G(−n) = a·L(n) for even n and (2b−a)·F(n) for odd n. Every seed with a=0 cancels on all even steps.

**COMPUTED** for n = 0…500 with exact integers (`cycle-closing/verify.py`).

### 1b · One sign behind it: Cassini's (−1)ⁿ (added 2026-10-27)

**PROVED (classical).** Cassini's identity: F(n+1)·F(n−1) − F(n)² = (−1)ⁿ.

The same sign runs three things at once:

| n | F(n)+F(−n) | F(n)/F(n−1) vs φ |
|---|---|---|
| even, (−1)ⁿ = +1 | 0 | under φ |
| odd, (−1)ⁿ = −1 | 2·F(n) | over φ |

The growth rate is fixed: F(n)/F(n−1) → φ, so F(n) ≈ φⁿ/√5 grows exponentially. What alternates is the approach. Each step overshoots or undershoots φ in strict turn, and the miss shrinks every step. The reason is exact: with a = F(n), b = F(n−1), the ratio is over φ iff a² − ab − b² > 0, and that quantity equals −(−1)ⁿ (Cassini, rewritten). So the mirror equilibrium of section 1 and the over/under swing are two readings of one sign term.

**COMPUTED** for n = 2…500 with exact integers (`cycle-closing/cassini_check.py`).

**OPEN.** Marc's reading: parity as the "cut frequency". Even n = the clean cut that splits into two equilibriums; odd n = the overflowing doubling. Test: do the archive moments marked "clean equilibrium" fall on the +1 side, and the "didn't close" moments on the −1 side?

## 2 · One operator, two readings: why 2, 1, 3

**BUILT.** Use the matrix A = [[0,1],[1,1]], so that A(x,y) = (y, x+y).

**PROVED.**
- A² = A + I.
- The trace of Aⁿ is L(n): tr I = **2**, tr A = **1**, tr A² = **3**, and so on.
- The off-diagonal entry of Aⁿ is F(n).

Lucas and Fibonacci are two readings of **one** reversible operator, not two patterns fitted to each other. The identity matrix I contributes the "2" that the foundation starts from (L0 = 2).

**PROVED.** Since det A = −1, Aⁿ + A⁻ⁿ reads:

| | off-diagonal (Fibonacci) | trace (Lucas) |
|---|---|---|
| even n | 0 | 2·L(n) |
| odd n | 2·F(n) | 0 |

Forward and inverse paths cancel in **complementary** places: when one reading is nothing, the other is something.

**PROVED.** L(n) = φⁿ + ψⁿ and F(n) = (φⁿ − ψⁿ)/√5. In the theorem's language these are two opposite rotations, φ and its mirror ψ. Their sum is φ + ψ = 1 = L1, their product is φ·ψ = −1, and the square of their difference is (φ − ψ)² = 5. L0 = φ⁰ + ψ⁰ = 1 + 1 = 2: both rotations at their starting "1", at the same moment.

## 3 · The paired half-step and the invariant 4

**PROVED.**

    L(n+1) = (L(n) + 5·F(n)) / 2
    F(n+1) = (L(n) +   F(n)) / 2

    L(n)² − 5·F(n)² = 4·(−1)ⁿ

The two readings carry each other forward, and one exact quantity keeps its size 4 while flipping sign every step.

**COMPUTED.** 101 paired steps and 169 rational seed pairs (`cycle-closing/symbol_layers_check.py`).

## 4 · Gaps between Lucas numbers tend to 1/φ

Let g(n) be the number of integers strictly between L(n) and L(n+1).

**PROVED.**
- g(n) = L(n−1) − 1.
- g(n)/L(n) → 1/φ and g(n)/L(n+1) → 1/φ².
- The two limits add up to exactly 1.
- L(n−1) + L(n+1) = 5·F(n).

**Correction kept on record.** Convergence is *not* monotone at the start (n=1 overshoots).

## 5 · The pathway of 1

**BUILT.** Replace every decimal digit d with the digits of L(d):

    0→2  1→1  2→3  3→4  4→7  5→11  6→18  7→29  8→47  9→76

**PROVED.**
- The only fixed strings are strings of 1s.
- Strings made only of 1s and 5s reach that fixed state in at most one step.
- Any other digit grows without bound.

So **1 is the only digit that passes through unchanged**, a precise version of "a pathway of 1 through everything".

**OPEN.** What the path runs through (objects, distances, update rule) is not defined yet.

## 6 · The mirror alphabet `>` `=` `<` `0`

**BUILT.** Define the mirror M (swaps `>` and `<`), the reversal R (reads the string backwards), and the substitution σ: `>` ↦ `==0`, `<` ↦ `0==`, `=` ↦ `=`, `0` ↦ `0`.

**PROVED.** R·σ(x) = σ·M·R(x) for every string. Mirroring turns into reading backwards: "the mirror changes its language". The two binding frames become palindromes:

    σ(>=<) = ==0=0==        σ(<=>) = 0=====0

**PROVED.** σ² = σ, so this substitution stops after one layer. The 16 three-symbol frames have only 14 distinct images, so the substitution is not lossless unless groups are kept. **OPEN:** the rule that would build a *next* layer.

## 7 · Oriented zero

**BUILT.** The state is (q, d): q is a phase from 0 to 9 and d = ±1 is an orientation. Each step advances q, and d flips each time the phase wraps from 9 back to 0.

**COMPUTED.**
- The visible digit word repeats every 10 steps.
- The full state repeats only every 20 steps.
- Positions 0, 10 and 20 look the same but carry +0, −0, +0.

**PROVED.** With R the reversal and T the cyclic shift, R·T·R = T⁻¹: reversing the viewpoint swaps forward and backward motion.

**Conditional count.** Nine independent angular slots with 360 settings each give 360⁹ = 101,559,956,668,416,000,000,000 configurations.

## 8 · The box rule (new, 2026-10-15)

**STATED** (the hand sketches are in `box-rule/sketches/`).
- The core only does `><` (hot first) or `<>` (cold first).
- When two cores meet, the same orientation **cannot** connect, and the inverse **sticks**. The equilibrium `=` then forms a box around both: `=<=>=`, and each core owns half the box.
- The box holds |+1| + |−1| = 2 = L0, counted by size.
- Growth is a "division": what goes out goes out two ways.
- Timing: *"+L1 − L1 in two frames"*, i.e. add in one frame and remove in the next, instead of `+L1/−L1` in a single frame.
- φ is the rotation, and the boxes, splitting again and again, close in on π.

**BUILT / COMPUTED** (`box-rule/box_rule.py`, exhaustive up to length 12, growth to 20 frames):

**8a · Binding needs a starting point.**
- Pair every core with an inverse neighbour, going left to right. The result depends on which end you start from in 2,820 of the 4,096 chains of length 12. Example: `><` `<>` `><` boxes as `=><=<>= ><` from the left and `>< =<>=><=` from the right.
- Mirroring all orientations never changes the result.
- Odd-length chains always keep exactly one core unboxed. A chain is fully boxed only when it is built from inverse pairs (2^(n/2) chains).

Reading: the rule needs a **"first particle"** to be well defined, which is the author's own phrase.

**8b · The timing decides between 2 and φ.**

| Division | Rule | Boxes per frame | Growth ratio |
|---|---|---|---|
| same frame (`+L1/−L1`) | box → box + box | 1, 2, 4, 8, 16, … | **2** |
| two frames (`+L1`, then `−L1`) | box → box + free core; free core → box (finds its inverse) | 1, 1, 2, 3, 5, 8, 13, … | **φ = 1.6180339…** |

Pushing out a core and letting it find its inverse one frame later gives exactly the Fibonacci numbers, so the growth ratio tends to φ. Squeezing both into one frame gives plain doubling. The size per box stays |+1| + |−1| = 2 throughout.

*Honest note:* the two-frame rule is the same counting structure as Fibonacci's rabbits, so φ here is a known result, not a new one. The STATED part is that the author's own timing distinction is exactly what separates "computed 2" from φ.

**8c · Neighbours break the "inverse only" rule.** In the grown chains, adjacent boxes share an orientation about 45% of the time (two-frame rule, frame 20). **OPEN:** are neighbouring boxes on different layers, so that the rule does not apply between them?

**8d · Box → π. COMPUTED.** Put a square inside a circle of diameter 1 and keep splitting every side in two (Archimedes' method). The perimeter goes 2.828 → 3.061 → 3.121 → 3.137 → 3.1403 → … → π. The remaining gap shrinks by a factor of 4 with each split, and π is never reached.

**OPEN.**
- Does φ "shift between two layers" as the ratio of inner box to outer box?
- Does the box keep 4 sides, or gain sides as it closes in?
- How fast do `>=<` ↔ `<=>` swaps happen? That swap frequency is the proposed z-axis, read as **sound**.

## 9 · Numerical curiosities (approximations, not identities)

**COMPUTED.**
- 137 + 1/28, refined with φ terms, gives 137.0360006…, which is 1.4×10⁻⁶ away from the stored fine-structure reference 137.035999177.
- A six-term expression simplifies to 2.71 + 1/90 − √2/500, which is 8.6×10⁻⁷ away from e.

These are tight approximations. They are **not** derivations: a formula can be selected after looking at the target. They are kept as curiosities, and a prediction fixed in advance would be the real test.

## 10 · What is still missing

1. The bridge from the foundation sentence to the two seeds and the update rule. At the moment these are chosen, not forced.
2. Units: nothing here maps a step to physical time, length or energy.
3. A rule for the next layer of symbols (σ stops after one layer).
4. A full state-transition for the box rule: the start side, how neighbours relate across layers, and when a box breaks.
5. A prediction made *before* comparing with anything.

## Credits

- **Idea, sketches, and all STATED material:** Marc.
- **Cycle-closing review, proofs in sections 1–7 and 9, and the offline labs:** Astra (AI assistant), 2026-10-09. See `cycle-closing/REVIEW.md`.
- **Box-rule test (section 8) and this write-up:** Claude (Anthropic), 2026-10-15.
