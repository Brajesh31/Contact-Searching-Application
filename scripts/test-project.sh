#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

command -v g++ >/dev/null
command -v python3 >/dev/null

BUILD_DIR="$(mktemp -d)"
trap 'rm -rf "$BUILD_DIR"' EXIT

g++ -std=gnu++17 -Wall -Wextra -Wpedantic main.cpp -o "$BUILD_DIR/contact-search"
python3 tests/test_cli_smoke.py "$BUILD_DIR/contact-search"
python3 scripts/validate_docs.py
python3 scripts/validate_markdown.py
python3 scripts/validate_svg.py
python3 scripts/validate_mermaid.py
python3 scripts/verify-assets.py
python3 scripts/check_license.py
python3 scripts/check-env-example.py
python3 scripts/check-project-structure.py
python3 scripts/repository_audit.py

echo "PASS: local build, CLI smoke test, and repository checks completed."
