# Draft only, nothing committed. To use: copy euler/ into nothing-theorem/, insert SECTION_EULER_DRAFT.md into THEOREM.md
# as §10 (renumber "What is still missing" to §11), add the four euler/*.py scripts to SCRIPTS in run_all.py, then commit with:

Add §10: the retry rule lands on e, the 1/9-1/10 pair, and the α share

- euler/hash_retest.py: Marc's multi-round retry hash, first-wins vs both-leave,
  checked for identity on 104,334 real words (both-leave: every item finds itself).
- euler/euler_rounds.py: (1-1/k)^k -> 1/e per round; totals e/(e-1) and e; 1/A + 1/B = 1.
- euler/euler_phi_check.py: closed forms vs measured; load ln φ² gives φ (partner φ²).
- euler/alpha_inverse.py: α bracket layers as retry rounds, share solved backwards
  from CODATA 2022 / Rb 2020 / Cs 2018 with a chance estimate.
- THEOREM.md §10: STATED / PROVED / COMPUTED / KNOWN / OPEN; rule B = BBHash (2017).
