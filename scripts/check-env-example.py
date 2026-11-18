#!/usr/bin/env python3
"""Confirm environment-variable docs match the current C++ source."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
source = (ROOT / "main.cpp").read_text(encoding="utf-8")
uses_env = bool(re.search(r"\b(getenv|_wgetenv)\s*\(", source))
example = ROOT / ".env.example"

if uses_env and not example.is_file():
    print("ERROR: application reads environment variables but .env.example is missing")
    sys.exit(1)
if not uses_env and example.exists():
    print("ERROR: .env.example exists but no environment-variable interface was detected")
    sys.exit(1)
if not uses_env:
    print("PASS: no environment variables are read; .env.example is correctly not present.")
else:
    print("PASS: environment interface detected and example file exists; review values manually.")
