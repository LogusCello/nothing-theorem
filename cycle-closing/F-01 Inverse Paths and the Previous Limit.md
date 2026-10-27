---
tags: [theorem, formalization, inverse, lucas, equilibrium, astra]
id: F-01
date: 2026-10-09
status: proposed-and-computed
---
# F-01 · Inverse paths and the previous limit

This addendum preserves Marc’s clarification after the cycle-closing review. It tests explicit candidate readings of the whole source → inverse paths → meeting → new limit construction. It does not replace his description with a claim that the candidate model is uniquely implied or physically verified.

## STATED — Marc’s clarification, verbatim

> the first 1 is odd the second 1 is even the combination 2 is the prime. as we go -1 and +1 to +-2 meaning if we treat 1 as either "+" or "-" we move say -1 as essentially "--" if 1 is - that moment or "+-" if its + as this would change if its a 1 or 11 as the second 11 must be both linked in a way so they dont repel they cant be the exact same as we can only move in inverse steps but as 2 is the result of a normal and inverse combining we end up with a 0 as L0 not a normal 0 so L0 = 2 leading to every 1 is already two things its "+-" both symbols as a symbol is "0.5" half a 1 here so just the symbol so when it adds as the 5 mirrors to the number at that position as its half of that value it has a rule implemented so the 0 acts as symbol as in the theorem 5 is the mirror of 2 and 2 is the computed L0 = 2 therefore when we cross threshold 1 to 11 to 111 when it settles it literally mirrors so it goes the other way back as it then leads to the limit being an equilibrium so 1 is +- or -+ leading to -1 and +1 while L0=+-2 asd 0 is +-0 or -+0 but we technically just added values to something that doesnt change as the 2 remains so thefirst 01 zero is L0 while the second 10 the null behind the ten so to speak would be the computed 2 so all numbers exist between 0 and 2 they just move layers as in the theorem we go L0 -> +L1-L1->2 = L2 and so on.

Marc then clarified L2, rather than adopting Astra’s suggestion that it meant a different layer notation:

> L2 = 3 relates to L0 being the base as if all numbers are inside 0 to 2 essentially L0=2 then each L1 adds to L2 so the second L1 causes the 2 to not have the loop part as its too far away as +L1 and -L1 as they are half 2 if we computed both to 1 but as they carry symbols they are 2 too much so they echoe after 2 while being on 2 as z axis to this as expansion factor like a shadow to light so if light is L0 it computes when it hits a result as +L1 and -L1 are both the paths to the computattion (where it connects to something and merges) so its computed 2 essentially the path adding up using the excess symbols to bounce the same amount as half flips so it is already stretched and if it hits an obejct the shadow is the -L1 shadow to the +L1 light of the L0 source leading to the object 2 as result so the previous limit is always the basis for the next as the shadow and the light are merged where the appear that exact point is our prime digit while L0 is even L1 is even, and 2. so if this resolves anything please do be so kind and update the theorem or test. we got about 30% context window left. so lets see what we can do here.

## STATED — connected reading, subject to Marc’s correction

The source is an enclosing limit L0=2. The plus/minus L1 paths are internal aspects of that source, not merely two unrelated scalars to add and discard. They carry orientation as well as amount. Meeting or merging produces the observed object while the path or echo relates it to the next layer. A frozen written value can hide continuing inverse movement. The previous limit becomes a basis for the next. Light/shadow and a z-direction express this relation in Marc’s account.

“Prime digit” is preserved as his name for the meeting/result role. No divisibility test has been specified. The earlier clarification attached odd/even to first/second occurrences; the latest statement also calls L1 “even.” The precise parity-bearing object remains OPEN. Numerically the established L1 is 1, which is odd. Do not silently impose integer parity on a role, or silently change 1 into an even integer.

The earlier suggestion that “L2” might mean only “layer 2” is superseded by his explicit confirmation **L2=3**. Preserve L0=2, L1=1, L2=3.

## PROPOSED — one reversible object links Fibonacci and Lucas readings

Use the two-coordinate update already underlying the archived recurrence. This is a candidate mathematical realization of the two paths, not a derivation of that recurrence from the new prose:

    A = [0  1]       A⁻¹ = [−1  1]       I = [1  0]
        [1  1]             [ 1  0]           [0  1]

    A(x,y) = (y,x+y),       A⁻¹(x,y) = (y−x,x).

The complete state is a pair. A reading of the state need not preserve all of it. There are two distinct senses of inverse here: undoing the recurrence with A⁻¹, and reversing a path’s orientation. They must not be equated without a connecting rule.

## PROVED within this candidate / COMPUTED — why 2, 1, 3 occur together

Direct multiplication gives A²=A+I. Since the trace is the sum of diagonal entries,

    tr(I)=2,    tr(A)=1,    tr(A²)=3,
    tr(Aⁿ⁺²)=tr(Aⁿ⁺¹)+tr(Aⁿ).

Thus tr(Aⁿ)=L(n), exactly. The two-coordinate identity operator supplies the base trace 2. Retaining that identity contribution gives the next trace 1+2=3. It does not count the printed plus/minus characters as extra arithmetic units. This offers a precise reading of a base structure remaining present in the next result; it does not prove that symbols create a third spatial dimension.

Induction on matrix multiplication also gives, for n≥1,

    Aⁿ = [F(n−1)   F(n)  ]
         [F(n)     F(n+1)].

A⁰=I fits the same formula when F(−1)=1. Extending the recurrence backward handles negative powers.

The Lucas and Fibonacci sequences are therefore two readings of the same reversible operator: the diagonal sum and either off-diagonal entry. They are not independent numerical patterns fitted to one another.

## PROVED within this candidate / COMPUTED — the inverse reveals complementary parity

Because det(Aⁿ)=(−1)ⁿ, the inverse formula for a 2×2 matrix gives

    tr(A⁻ⁿ) = (−1)ⁿ tr(Aⁿ) = (−1)ⁿ L(n).

The off-diagonal inverse entry is (−1)ⁿ⁺¹F(n). Consequently the same paired operator Aⁿ+A⁻ⁿ has two readings:

| Step | Off-diagonal reading, Fibonacci | Trace reading, Lucas |
|---|---|---|
| even n | 0 | 2L(n) |
| odd n | 2F(n) | 0 |

For n=0…8 the readings are:

| n | Fibonacci sum | Lucas sum |
|---|---:|---:|
| 0 | 0 | 4 |
| 1 | 2 | 0 |
| 2 | 0 | 6 |
| 3 | 4 | 0 |
| 4 | 0 | 14 |
| 5 | 10 | 0 |
| 6 | 0 | 36 |
| 7 | 26 | 0 |
| 8 | 0 | 94 |

This is a concrete connection to “when one side settles, another can still carry structure”: a zero in one reading does not make the whole paired operator zero. Neither reading requires prime classification. At n=0 the paired trace is 4 because I+I counts two operators; the source trace tr(I) is still 2. Do not silently identify those quantities.

Additional candidate invariant: Q(x,y)=x²+xy−y² satisfies Q(A(x,y))=−Q(x,y) and Q(A⁻¹(x,y))=−Q(x,y). Its absolute value is preserved while its sign alternates. This is an algebraic property, not a derived physical energy law, and it does not imply a factor of one half.

## PROPOSED / COMPUTED — source, two half-paths, meeting, retained amount

One simple whole-process witness places two paths in a source interval [0,B], moving symmetrically:

    x₊(τ)=Bτ,      x₋(τ)=B(1−τ),      0≤τ≤1/2.

Here τ is a chosen dimensionless progress parameter. The assumption of equal speeds is a modeling choice. They meet at τ=1/2, at coordinate B/2. Two signed half-contributions have sum 0 but combined magnitude B:

    (+B/2)+(−B/2)=0,
    |+B/2|+|−B/2|=B.

For B=2, that is a meeting at coordinate 1, with signed cancellation 0 and retained magnitude 2. These are three measurements, not contradictory answers to one measurement.

An explicit echo witness preserves both path identities at the meeting, swaps their directions, and lets them retrace. The full period has approaches and departures while the source size remains B. If the paths instead irreversibly merge into a single untagged object, reconstruction of the two paths needs retained information. The prose does not yet choose the collision mechanism.

A minimal hidden cycle is

    (+1/2,−1/2) ↔ (−1/2,+1/2).

Its oriented state has period 2; its signed-sum observation is permanently 0 and its magnitude observation permanently 1. This proves the possibility of a stationary reading of an alternating structured state. The simultaneous swap is an explicit proposed event rule, not something forced by the old digit substitution. A sequential half-flip would need its own intermediate-state and accounting rule.

## PROPOSED / COMPUTED — what a literal mirror can and cannot supply

For a reflected interval, R_B(x)=B−x is its own inverse and has fixed point B/2. With B=2, coordinate 1 is fixed, while all other coordinates swap in pairs. Direction can still flip at that same fixed coordinate.

This gives a precise possible meaning to “one freezes while the process reverses.” It does not produce 1→11→111 as decimal strings. Under the archived digit map, those strings remain fixed; a new layer transition must be separately defined.

Under this particular arithmetic reflection, 2↔5 would require B=7, since 7−2=5. In a single interval [0,2], R₂(2)=0, not 5. B=7 happens to be L4, but this is an algebraic condition for the proposed reflection, not evidence that Marc intended or derived that rule. A cross-layer operation, positional digit mirror, or different encoding could mean something else. Keep the 2↔5 link OPEN until that operation is fixed.

## COMPUTED — the previous limit alone does not determine the next

Symmetric halves reconstruct any positive B; that identity alone neither expands B nor determines its successor. Retaining B, doubling B, or applying a two-seed recurrence are different continuations compatible with the same half-pair bookkeeping. To get Lucas values, retain the ordered two-seed state (2,1) and the chosen update:

    (2,1) → (1,3) → (3,4) → (4,7) → …

Starting instead from (1,2) gives 3,5,8,13… . The source/current roles and order matter. In particular it is not enough to say “start with source 2 and add previous 1 forever”: after the first 3, the retained previous value must be specified correctly.

L2=3 is consistent with the archived recurrence and the matrix realization. The new account supplies an intended interpretation of that retained base, but does not yet uniquely derive the update law or its seed order.

## OPEN — primes, geometry, and the exact layer transition

The first result 2 and next Lucas value 3 are prime in ordinary arithmetic. Later Lucas values include 4,18,76,123,322. So the recurrence does not make every result prime. If “prime digit” names the origin of a merged object, it is a semantic role unless an independent divisibility claim is stated. A positional index, a numerical value, a path orientation, and a frame’s parity are separate data.

Nothing in the tested state-pair model singles out a spatial z axis, physical light, shadow, repulsion, or an expansion factor. Those descriptions remain Marc’s STATED interpretation. To turn them into a testable construction, specify:

1. What the complete state retains at a meeting (paths, orientations, previous limit, phase).
2. Whether the meeting swaps, sequentially flips, absorbs, or combines the two paths, with an exact update.
3. Which quantity becomes the next source limit, and what the 2↔5 mirror does to its layer.

These are the remaining parts of one rule, not reasons to abandon the connected source/path/meeting picture. The tests establish a consistent candidate and expose where more than one continuation remains possible.

## Reproduction and handoff

Astra’s offline deliverable contains `inverse_paths_check.py`, `inverse_paths_results.json`, and `inverse_paths.html`. Script tests use exact integers and rational arithmetic: matrix identities through n=100, 169 rational seed pairs for the reversible update and sign-flipping quadratic form, and 606 interval reflection samples. Proofs above supply the general claims; finite tests check their implementation. No literature search or physical validation was performed.

Shared package: this folder.

Related: [[00 The Foundation - Nothing is Something]] · [[Nothing Theorem Fibonacci Equilibrium]] · [[Nothing Theorem Terminal 1D]] · [[2026-10-07 The pathway of 1]].
