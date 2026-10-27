# Validation — 2026-10-09

- Python standard-library verification passed all assertions in 13 groups: exact recurrence identities, generalized seeds, Lucas gaps, digit-map branching, symbol substitution and collisions, reflected counter, decimal suffix periods, grid extension, Mertens sieve, glyph rotation, high-precision checkpoints, and binary64 boundary. Results and scopes are in verification.json. Finite computations are distinguished from the proofs in REVIEW.md.
- Installed Chromium headless shell: 251 arithmetic and interaction checks passed at both 1440×1100 and 390×1000. Checked tab switching, sequence steps, reset, sampling parity, play/pause controls, digit presets and invalid input, frame selection, terminal input, CSV content, and absence of horizontal overflow. No script errors were reported in the captured browser runs.
- Screenshots of equilibrium, gaps, symbols, digit mapping, overview, mobile view, and exportable SVG inspected. Test screenshots and DOM dumps remain in the VM working copy.
- Original source hashes were rechecked before delivery. No original notes or existing lab files were altered.
- Browser app has a restrictive content policy and no external resources or fetches. No intentional external network calls, searches, downloads, or installs were made. Browser validation disabled background networking, proxies, and external hostname resolution; no packet-level audit was performed.
- A first full-Chromium attempt stalled and was stopped. Validation used the already-installed Chromium headless shell. Host commands were not used.
- This is an internal review of the available notes, not an external literature, metrology, or novelty review. Historical experiments and linked spreadsheets were not certified.

## Inverse-path follow-up

- Exact candidate checks passed: forward/inverse matrix and complementary readings for n=0..100, 169 rational state pairs, and 606 reflection samples. The script also checks ordered seed consequences and separates ordinary prime values from the proposed meeting-role interpretation.
- New companion passed 105 browser arithmetic/interaction checks at desktop and mobile sizes, with no captured script errors. The updated original entry page passed its 251 mobile checks. Normal opening screenshots inspected after avoiding the test anchor’s automatic scroll.
- Raw clarifications preserved in a new Formalization note. Theorem.md received an additive link; earlier notes remain unchanged. This is the authorized follow-up to the original review’s source-preserving delivery.
- No web searches, downloads, installs, or host commands. Tests ran in the VM local copy.

## F-02 follow-up

Exact assertions passed for 101 paired recurrence steps and 169 rational seed pairs, including the inverse and L²−5F² sign flip. All 5,461 four-symbol words of lengths 0…6 round-tripped with retained groups; all 9,840 x/y/z addresses of lengths 1…8 round-tripped under the proposed repetition-count encoding. Desktop/mobile companion checks each passed 131 assertions, including the new panel updating with step selection. Normal rendered layout inspected. No web research, downloads, or host commands.

## F-03 retained-chain correction

Marc superseded the F-02 suffix/repetition-count interpretation. That historical experiment remains in the record with a correction notice; it is no longer the active visualization. New tests verify digit rotation versus reversal, a proposed reversible 20-state oriented cycle, a 1,001-state retained-history example, literal coordinate counts, and the conditional 360⁹ count. Updated companion passed 134 arithmetic/interaction checks at desktop and mobile sizes; normal screenshot inspected. The coordinate continuation remains preserved as written pending clarification. No external research or host commands.
