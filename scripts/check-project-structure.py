#!/usr/bin/env python3
"""Check important repository paths and documented support directories."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "main.cpp", "README.md", "LICENSE", "PROJECT_STATUS.md",
    "docs/README.md", "docs/checklist-coverage.md", "docs/cli-interface.md",
    "docs/architecture/README.md", "docs/product/README.md",
    "docs/development/README.md", "docs/testing/README.md",
    "docs/security/threat-model.md", "docs/assets/README.md",
    "docs/templates/README.md", "scripts/README.md",
    "tests/README.md", ".github/workflows/cpp-build.yml",
    ".github/workflows/docs-validation.yml", ".github/workflows/codeql.yml",
    ".github/workflows/secret-scan.yml",
]
missing = [item for item in REQUIRED if not (ROOT / item).exists()]
if missing:
    for item in missing:
        print(f"ERROR: missing required path: {item}")
    sys.exit(1)

readme = (ROOT / "README.md").read_text(encoding="utf-8")
for directory in ("docs/", "scripts/", "tests/", ".github/"):
    if directory not in readme:
        print(f"ERROR: README does not mention {directory}")
        sys.exit(1)

print(f"PASS: {len(REQUIRED)} important paths exist and README references main support directories.")
