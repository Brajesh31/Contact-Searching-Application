#!/usr/bin/env python3
"""Run the canonical repository-local Markdown link validator."""
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
validator = root / "scripts" / "validate_docs.py"
result = subprocess.run([sys.executable, str(validator)], cwd=root, check=False)
raise SystemExit(result.returncode)
