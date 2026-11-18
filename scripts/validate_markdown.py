#!/usr/bin/env python3
"""Perform repeatable structural checks over repository Markdown files."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
files = sorted(ROOT.glob("*.md")) + sorted((ROOT / "docs").rglob("*.md")) + sorted((ROOT / "tests").rglob("*.md"))
errors = []
checked = 0

for path in files:
    checked += 1
    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT)
    if text and not text.endswith("\n"):
        errors.append(f"{rel}: missing final newline")
    fence = None
    for number, line in enumerate(text.splitlines(), start=1):
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            marker = stripped[:3]
            if fence is None:
                fence = marker
            elif marker == fence:
                fence = None
        if line.rstrip() != line:
            errors.append(f"{rel}:{number}: trailing whitespace")
    if fence is not None:
        errors.append(f"{rel}: unclosed fenced code block")

if errors:
    for error in errors:
        print(f"ERROR: {error}")
    sys.exit(1)

print(f"PASS: checked Markdown structure in {checked} files.")
print("NOTE: this is a repository-specific structural check; markdownlint-cli2 provides the CommonMark lint.")
