#!/usr/bin/env python3
"""Parse SVG assets and require accessible title and description elements."""
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
assets = sorted((ROOT / "docs" / "assets").rglob("*.svg"))
errors = []
if not assets:
    errors.append("No SVG assets found under docs/assets.")
for path in assets:
    try:
        root = ET.parse(path).getroot()
        if not root.tag.endswith("svg"):
            errors.append(f"{path.relative_to(ROOT)}: root element is not svg")
        tags = {element.tag.split("}")[-1] for element in root.iter()}
        if "title" not in tags or "desc" not in tags:
            errors.append(f"{path.relative_to(ROOT)}: add title and desc elements")
    except (ET.ParseError, OSError) as exc:
        errors.append(f"{path.relative_to(ROOT)}: {exc}")
if errors:
    for error in errors:
        print(f"ERROR: {error}")
    sys.exit(1)
print(f"PASS: parsed {len(assets)} SVG assets.")
