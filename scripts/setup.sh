#!/usr/bin/env bash
set -euo pipefail

echo "Contact Searching Application development prerequisites"
for tool in g++ python3; do
  if ! command -v "$tool" >/dev/null 2>&1; then
    echo "ERROR: required tool not found: $tool" >&2
    exit 1
  fi
done

g++ --version | head -n 1
python3 --version
echo "PASS: required local tools are available."
echo "This script checks prerequisites; it does not install or modify system packages."
