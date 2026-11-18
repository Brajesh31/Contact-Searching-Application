#!/usr/bin/env python3
"""Validate local links in repository Markdown without changing files."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DOCS = [ROOT / "README.md", ROOT / "CONTRIBUTING.md", ROOT / "SECURITY.md"]
DOCS += sorted((ROOT / "docs").rglob("*.md"))
LINK_RE = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")
errors = []
checked = 0

for doc in DOCS:
    if not doc.is_file():
        errors.append(f"Missing documentation file: {doc.relative_to(ROOT)}")
        continue
    text = doc.read_text(encoding="utf-8")
    for raw in LINK_RE.findall(text):
        target = raw.strip().split()[0].strip("<>")
        if not target or target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = target.split("#", 1)[0]
        if not target:
            continue
        candidate = (doc.parent / target).resolve()
        try:
            candidate.relative_to(ROOT)
        except ValueError:
            errors.append(f"{doc.relative_to(ROOT)}: link escapes repository: {target}")
            continue
        checked += 1
        if not candidate.exists():
            errors.append(f"{doc.relative_to(ROOT)}: missing local target: {target}")

if errors:
    for error in errors:
        print(f"ERROR: {error}")
    sys.exit(1)
print(f"PASS: checked {len(DOCS)} documentation files and {checked} local links.")
