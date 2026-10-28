# tools/check_demo.py -- fixed throughout the demonstration
from pathlib import Path
import sys
import time
import unittest

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root))
suite = unittest.defaultTestLoader.discover(str(root / "tests"))
if suite.countTestCases() == 0:
    raise SystemExit("empty collection")
result = unittest.TextTestRunner(verbosity=2).run(suite)
if result.wasSuccessful() and "def label(" in (root / "demo.py").read_text():
    print("demo continuation window: 20 seconds before check completion", flush=True)
    time.sleep(20)
raise SystemExit(0 if result.wasSuccessful() else 1)
