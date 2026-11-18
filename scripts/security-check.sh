#!/usr/bin/env bash
set -euo pipefail

if ! command -v git >/dev/null 2>&1; then
  echo "ERROR: git is required to enumerate tracked files." >&2
  exit 2
fi

tracked="$(git ls-files)"
sensitive_paths="$(printf '%s\n' "$tracked" | grep -E '(^|/)(\.env($|\.)|id_rsa$|id_ed25519$)|\.(pem|p12|pfx|key)$' | grep -vE '(^|/)\.env\.example$' || true)"
if [[ -n "$sensitive_paths" ]]; then
  echo "ERROR: tracked paths resemble local secret or private-key files:"
  printf '%s\n' "$sensitive_paths"
  exit 1
fi

if command -v gitleaks >/dev/null 2>&1; then
  gitleaks detect --source . --redact --no-banner
else
  echo "WARNING: gitleaks is not installed; filename checks passed, but content/history scanning was not performed."
  echo "Run the GitHub Secret Scanning workflow for the full Gitleaks scan."
fi

echo "PASS: tracked filename safety check completed."
