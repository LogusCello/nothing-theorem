# Nothing Theorem — Cycle Closing

Open **index.html** in a modern browser. It works directly from disk, offline; no installation or server is needed.

- Equilibrium: scrub n, step, play/pause, change sampling stride, export exact CSV.
- Lucas layers: inspect gap ratios and the reflected terminal counter.
- Symbol mirror: select any of the 16 frames.
- Pathway of 1: enter a decimal string and trace its Lucas substitution.
- Whole picture: read the links between the philosophical premise, proved arithmetic, built rules, and open questions.

Read **REVIEW.md** for proofs, corrections, and scope. **cycle-map.svg** is the exportable diagram. **verification.json** contains computed results; **sources.json** identifies the original notes by SHA-256.

To reproduce arithmetic checks in a local working copy: `python3 verify.py`. It uses the Python standard library and writes verification.json beside itself. Browser interaction checks are available by opening index.html with `#test` appended to its file URL.

This is a companion to the existing spiral visualizer. Original notes and existing labs remain unchanged. It does not certify physical conclusions, historical benchmarks, or novelty.

## Inverse-path clarification — 2026-10-09

Open **inverse_paths.html** for the follow-up: paired forward/inverse recurrence, complementary Fibonacci/Lucas cancellation, and a proposed source/meeting/echo model. **F-01 Inverse Paths and the Previous Limit.md** preserves Marc’s words, the candidate definitions, proofs, and unresolved layer rule. Run `python3 inverse_paths_check.py` in a local copy to reproduce exact checks.

## Grouped symbols and coordinate descriptions — F-02

The inverse_paths.html companion now also shows the exact coupled half-step for (L,F), its sign-flipping invariant, and proposed grouped-symbol and coordinate encodings. Read **F-02 Grouped Symbols and Three Descriptions.md** for Marc’s statement, derivations, and the open connection to geometry. Run `python3 symbol_layers_check.py` locally to reproduce the tests; results are in symbol_layers_results.json. Group delimiters remain a proposed convention. Marc has superseded the suffix-count interpretation; see F-03 for his retained-chain clarification.

## Retained chain and oriented return — F-03

Read **F-03 Oriented Zero and the Retained Chain.md**. The active visualization now replaces the z1 repetition-count example with a proposed cyclic-shift/oriented-return witness. It keeps the coordinate-generation rule open and explains the assumptions behind 360⁹. Reproduce checks with `python3 oriented_cycle_check.py`. Prior suffix-count tests remain historical experiments, not support for the corrected interpretation.
