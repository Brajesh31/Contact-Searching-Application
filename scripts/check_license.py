#!/usr/bin/env python3
"""Check that the repository contains the declared MIT license text."""
from pathlib import Path
import sys

path = Path(__file__).resolve().parents[1] / "LICENSE"
if not path.is_file():
    print("ERROR: LICENSE is missing")
    sys.exit(1)
text = path.read_text(encoding="utf-8")
required = ("MIT License", "Copyright (c)", "Permission is hereby granted", "THE SOFTWARE IS PROVIDED")
missing = [marker for marker in required if marker not in text]
if missing:
    print("ERROR: missing license markers: " + ", ".join(missing))
    sys.exit(1)
print("PASS: LICENSE contains the expected MIT license markers.")
