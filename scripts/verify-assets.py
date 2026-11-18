#!/usr/bin/env python3
"""Verify local Markdown image references and SVG accessibility metadata."""
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
DOCS = [ROOT / "README.md"] + sorted((ROOT / "docs").rglob("*.md"))
IMAGE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
errors = []
checked = 0

for doc in DOCS:
    content = doc.read_text(encoding="utf-8")
    for alt, target in IMAGE.findall(content):
        target = target.strip().split()[0].strip("<>")
        if target.startswith(("https://", "http://", "data:")):
            continue
        local = target.split("#", 1)[0]
        if not local:
            continue
        asset = (doc.parent / local).resolve()
        try:
            asset.relative_to(ROOT)
        except ValueError:
            errors.append(f"{doc.relative_to(ROOT)}: image escapes repository: {target}")
            continue
        checked += 1
        if not asset.is_file():
            errors.append(f"{doc.relative_to(ROOT)}: missing image asset: {target}")
        if not alt.strip():
            errors.append(f"{doc.relative_to(ROOT)}: image has empty alt text: {target}")

for svg in sorted((ROOT / "docs" / "assets").rglob("*.svg")):
    try:
        root = ET.parse(svg).getroot()
        tags = {element.tag.split("}")[-1] for element in root.iter()}
        if not root.tag.endswith("svg") or "title" not in tags or "desc" not in tags:
            errors.append(f"{svg.relative_to(ROOT)}: invalid SVG root or missing title/desc")
    except (OSError, ET.ParseError) as exc:
        errors.append(f"{svg.relative_to(ROOT)}: {exc}")

if errors:
    for error in errors:
        print(f"ERROR: {error}")
    sys.exit(1)
print(f"PASS: checked {checked} Markdown image references and all SVG assets.")
