#!/usr/bin/env python3
"""Perform basic structural checks on editable Mermaid diagram files."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
files = sorted((ROOT / "docs").rglob("*.mmd"))
errors = []
if not files:
    errors.append("No Mermaid source files found.")
for path in files:
    content = path.read_text(encoding="utf-8").strip()
    first = content.splitlines()[0].strip() if content else ""
    allowed = ("flowchart ", "graph ", "sequenceDiagram", "stateDiagram-v2", "classDiagram", "erDiagram")
    if not first.startswith(allowed):
        errors.append(f"{path.relative_to(ROOT)}: unsupported or missing Mermaid diagram declaration")
    if content.count("{") != content.count("}"):
        errors.append(f"{path.relative_to(ROOT)}: unbalanced curly braces")
if errors:
    for error in errors:
        print(f"ERROR: {error}")
    sys.exit(1)
print(f"PASS: basic structure checked for {len(files)} Mermaid sources.")
print("NOTE: this is not a full Mermaid parser or renderer.")
