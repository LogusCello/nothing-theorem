#!/usr/bin/env python3
"""Rerun every check in this repository and report pass/fail."""
import subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SCRIPTS = ["cycle-closing/verify.py", "cycle-closing/cassini_check.py",
           "cycle-closing/inverse_paths_check.py",
           "cycle-closing/symbol_layers_check.py", "cycle-closing/oriented_cycle_check.py",
           "box-rule/box_rule.py", "alpha/alpha_check.py"]

failed = 0
for s in SCRIPTS:
    r = subprocess.run([sys.executable, "-I", str(ROOT / s)], capture_output=True, text=True)
    ok = r.returncode == 0
    failed += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {s}")
    if not ok:
        print(r.stderr[-2000:])
print(f"\n{len(SCRIPTS) - failed}/{len(SCRIPTS)} passed")
sys.exit(1 if failed else 0)
