#!/usr/bin/env python3
"""The box rule (2026-10-15): a small, runnable reading of Marc's equilibrium-box idea.

Marc's words, compressed:
  * The core only does `><` (hot side first) and `<>` (cold side first).
    Call them + and -.
  * Two cores meet: same orientation -> they cannot connect.
    Inverse orientation -> they stick, and the equilibrium "=" forms a box
    around both. Written in 1D: =<=>=  (each core owns half the box).
  * Counted by size: a box holds |+1| + |-1| = 2  (= L0).
  * Growth: what goes out goes out two ways ("computed 2"), and the result
    grows as a "division" of the previous box.
  * Timing: "+L1 - L1 in two frames" (add in one frame, remove in the next)
    instead of "+L1/-L1 in the same frame".

The rule is only partly specified, so this script tests three things and
reports what happens. It does not tune anything to hit a target number.

  Part 1  Binding:  does "inverse sticks, same rejects" give one answer per
          chain, or does it depend on where you start?
  Part 2  Growth:   same-frame division vs two-frame division.
  Part 3  Box -> pi: split the box's sides again and again (Archimedes).

Standard library only.  Run:  python3 box_rule.py
"""
from itertools import product
from math import pi, sin, sqrt
import json
import os

PHI = (1 + sqrt(5)) / 2
GLYPH = {+1: "><", -1: "<>"}


# ---------------------------------------------------------------- Part 1
def bind(chain, from_right=False):
    """Greedy pairing: walk the chain, an unpaired core sticks to its
    neighbour if (and only if) the neighbour has the inverse orientation."""
    idx = list(range(len(chain)))
    if from_right:
        idx.reverse()
    paired = [False] * len(chain)
    boxes = []
    for a, b in zip(idx, idx[1:]):
        if not paired[a] and not paired[b] and chain[a] == -chain[b]:
            paired[a] = paired[b] = True
            boxes.append(tuple(sorted((a, b))))
    return sorted(boxes)


def render(chain, boxes):
    """1D writing: a stuck pair becomes =<=>= style, a lone core stays bare."""
    starts = {a: b for a, b in boxes}
    out, i = [], 0
    while i < len(chain):
        if i in starts:
            out.append("=" + GLYPH[chain[i]] + "=" + GLYPH[chain[i + 1]] + "=")
            i += 2
        else:
            out.append(GLYPH[chain[i]])
            i += 1
    return " ".join(out)


def part1(max_len=12):
    rows = []
    for n in range(1, max_len + 1):
        total = order_matters = all_bound = 0
        example = None
        for chain in product((+1, -1), repeat=n):
            total += 1
            left, right = bind(chain), bind(chain, from_right=True)
            if left != right:
                order_matters += 1
                if example is None:
                    example = chain
            if 2 * len(left) == n:
                all_bound += 1
            # mirror check: swapping hot/cold everywhere must not change who binds
            assert bind(tuple(-c for c in chain)) == left
        rows.append({"length": n, "chains": total,
                     "start_side_changes_result": order_matters,
                     "fully_boxed": all_bound,
                     "example": None if example is None else {
                         "from_left": render(example, bind(example)),
                         "from_right": render(example, bind(example, True))}})
    return rows


# ---------------------------------------------------------------- Part 2
def grow(frames, two_frame):
    """Tokens: ('B', o) = a box led by orientation o, ('F', o) = a free core.

    same frame (+L1/-L1):  B(o) -> B(o) B(-o)      the pushed-out half is boxed at once
    two frames (+L1, -L1): B(o) -> B(o) F(-o)      frame 1: the half goes out (+L1)
                           F(o) -> B(o)            frame 2: it finds its inverse (-L1)
    The pushed-out half is always the inverse, because only the inverse can connect.
    """
    state = [("B", +1)]
    history = []
    for _ in range(frames + 1):
        boxes = sum(1 for t, _ in state if t == "B")
        free = len(state) - boxes
        same_neighbours = sum(1 for (_, a), (_, b) in zip(state, state[1:]) if a == b)
        history.append({"boxes": boxes, "free": free,
                        "size": 2 * boxes + free,
                        "same_orientation_neighbours": same_neighbours,
                        "string": "".join(("[" + GLYPH[o] + "]") if t == "B" else GLYPH[o]
                                          for t, o in state) if len(state) <= 13 else None})
        nxt = []
        for t, o in state:
            if t == "B":
                nxt += [("B", o), ("B", -o)] if not two_frame else [("B", o), ("F", -o)]
            else:
                nxt.append(("B", o))
        state = nxt
    return history


def part2(frames=20):
    out = {}
    for name, two in (("same_frame", False), ("two_frames", True)):
        h = grow(frames, two)
        ratios = [h[i + 1]["size"] / h[i]["size"] for i in range(len(h) - 1)]
        out[name] = {"history": h, "last_size_ratio": ratios[-1]}
    fib = [1, 1]
    while len(fib) < frames + 3:
        fib.append(fib[-1] + fib[-2])
    # two-frame sizes should be Fibonacci numbers, size counted by |+1|+|-1|
    out["two_frames"]["sizes_are_fibonacci_x2_shift"] = all(
        row["boxes"] == fib[i] for i, row in enumerate(out["two_frames"]["history"]))
    out["phi"] = PHI
    return out


# ---------------------------------------------------------------- Part 3
def part3(splits=12):
    rows = []
    for k in range(splits + 1):
        sides = 4 * 2 ** k
        perim = sides * sin(pi / sides)          # polygon in a circle of diameter 1
        rows.append({"sides": sides, "perimeter": perim, "gap_to_pi": pi - perim})
    # each split shrinks the gap to about 1/4: the gap ratio tends to 1/4
    tail = rows[-1]["gap_to_pi"] / rows[-2]["gap_to_pi"]
    return {"rows": rows, "gap_shrink_per_split": tail}


def main():
    p1, p2, p3 = part1(), part2(), part3()
    results = {"part1_binding": p1, "part2_growth": p2, "part3_box_to_pi": p3}
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "box_rule_results.json"), "w") as f:
        json.dump(results, f, indent=1)

    print("Part 1  binding (inverse sticks, same rejects)")
    for r in p1:
        print(f"  length {r['length']:2d}: {r['chains']:5d} chains, "
              f"start side changes the result in {r['start_side_changes_result']:4d}, "
              f"fully boxed {r['fully_boxed']:3d}")
    ex = p1[2]["example"]
    print(f"  e.g. from the left : {ex['from_left']}\n       from the right: {ex['from_right']}")

    print("\nPart 2  growth")
    for name in ("same_frame", "two_frames"):
        h = p2[name]["history"]
        print(f"  {name:10s} boxes: {[r['boxes'] for r in h[:12]]}  "
              f"size ratio -> {p2[name]['last_size_ratio']:.9f}")
        for r in h[:5]:
            print(f"      {r['string']}")
        print(f"      same-orientation neighbours at frame 20: "
              f"{h[-1]['same_orientation_neighbours']} of {h[-1]['boxes'] + h[-1]['free'] - 1}")
    print(f"  phi = {PHI:.9f};  two-frame boxes are Fibonacci: "
          f"{p2['two_frames']['sizes_are_fibonacci_x2_shift']}")

    print("\nPart 3  box -> pi (split every side in two)")
    for r in p3["rows"][:8]:
        print(f"  {r['sides']:5d} sides  perimeter {r['perimeter']:.6f}")
    print(f"  gap to pi shrinks by x{p3['gap_shrink_per_split']:.4f} per split")


if __name__ == "__main__":
    main()
