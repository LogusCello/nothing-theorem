"""Re-test of Marc's multi-round retry hash (2026-10-31), now WITH identity resolution.
A = as recorded in Sept: first key in a slot keeps it, the rest retry next round (occupancy only).
B = same rounds, but a slot hit by 2+ keys is left empty and ALL of them retry (so lookup knows who owns a slot).
Lookup for both: go round by round, the first round whose slot is set is the answer. Then we check every key.
Run: python3 -I hash_retest.py [wordlist]"""
import math, sys, random
M64 = (1 << 64) - 1
def fnv(s, seed):
    h = (0xcbf29ce484222325 ^ (seed * 0x9E3779B97F4A7C15)) & M64
    for b in s.encode(): h = ((h ^ b) * 0x100000001b3) & M64
    h ^= h >> 33; h = (h * 0xff51afd7ed558ccd) & M64; h ^= h >> 33
    return h
def build(keys, gamma, both_leave):
    rounds, left, seed = [], list(keys), 0
    while left and seed < 200:
        size = max(1, math.ceil(len(left) * gamma)); hits = {}
        for k in left: hits.setdefault(fnv(k, seed) % size, []).append(k)
        bits, nxt = set(), []
        for s, ks in hits.items():
            if len(ks) == 1 or not both_leave: bits.add(s); nxt += ks[1:]
            else: nxt += ks
        rounds.append((size, bits, seed)); left, seed = nxt, seed + 1
    return rounds, left
def lookup(rounds, k):
    off = 0
    for size, bits, seed in rounds:
        s = fnv(k, seed) % size
        if s in bits: return off + sorted(bits).index(s) if False else (off, s)
        off += size
    return None
def test(keys, gamma, both_leave):
    rounds, left = build(keys, gamma, both_leave)
    slots = sum(r[0] for r in rounds)
    owner = {}
    for size, bits, seed in rounds: pass
    # who does lookup point each key to, and is that slot really the key's?
    got, wrong = {}, 0
    for k in keys:
        p = lookup(rounds, k)
        if p in got: wrong += 1
        got.setdefault(p, k)
    ok = len(got) == len(keys) and None not in got
    rank = slots / 512 * 64          # rank table so a slot turns into its index 0..N-1 (64 bits per 512)
    return dict(rounds=len(rounds), bits_per_key=slots / len(keys), with_rank=(slots + rank) / len(keys),
                shared_lookups=len(keys) - len(got), correct=ok and not left)
def load_words(path='/usr/share/dict/american-english'):
    try: return sorted({w.strip() for w in open(path, encoding='utf-8', errors='replace') if w.strip()})
    except OSError:                       # no word list on this machine: same test on 100,000 synthetic keys
        return [f"key{i:06d}" for i in range(100000)]
words = load_words(*sys.argv[1:2])
random.seed(1)
print(f"unique words: {len(words)}   lower bound for ANY minimal perfect hash: log2(e) = {math.log2(math.e):.4f} bits/key\n")
for N in (2000, 8000, len(words)):
    keys = words if N == len(words) else random.sample(words, N)
    for g in (1.0, 1.5, 2.0):
        for name, bl in (("A first-wins ", False), ("B both-leave ", True)):
            r = test(keys, g, bl)
            print(f"N={N:6d} load {1/g:.2f} {name}: rounds {r['rounds']:2d}  {r['bits_per_key']:.3f} bits/key"
                  f" (+rank {r['with_rank']:.3f})  keys sent to someone else's slot: {r['shared_lookups']:6d}  every key found itself: {r['correct']}")
    print()
