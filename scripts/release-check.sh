#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

python3 scripts/check_license.py
python3 scripts/validate_docs.py
python3 scripts/validate_markdown.py
python3 scripts/validate_svg.py
python3 scripts/validate_mermaid.py
python3 scripts/verify-assets.py
python3 scripts/repository_audit.py

echo "NOTE: no semantic-version tag or formal release process is defined."
echo "NOTE: compile and run tests with scripts/test-project.sh before creating a release artifact."
