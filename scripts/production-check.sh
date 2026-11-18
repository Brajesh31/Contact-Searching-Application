#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

bash scripts/test-project.sh
bash scripts/security-check.sh

echo "PASS: repository quality checks completed."
echo "CAUTION: this is a local repository check, not a production-readiness certification of the application."
