#!/usr/bin/env python3
"""Check required repository support paths and protected original Git blob IDs."""
from pathlib import Path
import hashlib
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "LICENSE", "SECURITY.md", "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md", "SUPPORT.md", "CHANGELOG.md", "ROADMAP.md",
    "AUTHORS.md", "CITATION.cff", "CODEOWNERS", "GOVERNANCE.md",
    "CODE_STYLE.md", "PROJECT_STATUS.md", ".editorconfig", ".gitattributes",
    ".markdownlint-cli2.jsonc", ".yamllint", ".gitleaks.toml",
    "docs/README.md", "docs/checklist-coverage.md", "docs/cli-interface.md",
    "docs/architecture.md", "docs/architecture/README.md",
    "docs/architecture/context-diagram.md", "docs/architecture/container-diagram.md",
    "docs/architecture/component-diagram.md", "docs/architecture/data-flow.mmd",
    "docs/architecture/search-flow.mmd", "docs/architecture/test-workflow.mmd",
    "docs/product/features.md", "docs/user-guide.md", "docs/data-format.md",
    "docs/testing.md", "docs/test-strategy.md", "docs/test-plan.md",
    "docs/testing/feature-test-matrix.md", "docs/security.md",
    "docs/security-architecture.md", "docs/threat-assessment.md",
    "docs/accessibility.md", "docs/maintenance/README.md",
    "docs/templates/README.md", "docs/templates/production-readiness-template.md",
    "docs/assets/README.md", "docs/assets/branding/logo.svg",
    "docs/assets/branding/favicon.svg", "docs/assets/branding/project-banner.svg",
    "scripts/README.md", "scripts/validate_docs.py", "scripts/validate_markdown.py",
    "scripts/validate_svg.py", "scripts/validate_mermaid.py", "scripts/verify-assets.py",
    "scripts/check-env-example.py", "scripts/check_license.py",
    "scripts/check-project-structure.py", "scripts/repository_audit.py",
    "scripts/security-check.sh", "scripts/test-project.sh",
    "scripts/release-check.sh", "scripts/production-check.sh",
    "tests/README.md", "tests/test_cli_smoke.py",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/ISSUE_TEMPLATE/bug_report.yml",
    ".github/ISSUE_TEMPLATE/feature_request.yml",
    ".github/ISSUE_TEMPLATE/documentation.yml",
    ".github/ISSUE_TEMPLATE/security_report.yml",
    ".github/ISSUE_TEMPLATE/accessibility.yml",
    ".github/ISSUE_TEMPLATE/performance.yml",
    ".github/ISSUE_TEMPLATE/question.yml",
    ".github/workflows/docs-validation.yml",
    ".github/workflows/cpp-build.yml",
    ".github/workflows/codeql.yml",
    ".github/workflows/secret-scan.yml",
    ".github/dependabot.yml",
]
PROTECTED_BLOBS = {
    "main.cpp": "4d6424069d175b4c6f8f301a3e45ca62726ff6cd",
    "contacts.txt": "d0c67b2f27136b877329df9ff1b1253ea74b92b2",
    "Dummy Contacts.txt": "94a491293acf67d7b1d03a03bcf828d714a2d5db",
    "Eswar.vcf": "b47109952b8e960cde13d835aff8f429da246060",
    "Vignesh.vcf": "835fdce79b1c13e3a68caff54bbe7d007dd98954",
    "Contact Searching Appliaction.pptx": "de91b88c12608791ce2c2552950e639a253ae6de",
    ".vscode/c_cpp_properties.json": "c1afae2d97cc1df81e112c5e2b80d255308f70bd",
    ".vscode/settings.json": "fb5a06c9761e4c735f2827b15062772a77db53d6",
    ".idea/.gitignore": "13566b81b018ad684f3a35fee301741b2734c8f4",
    ".gitignore": "adb36c821965862397d65fa68e26cd2433c97140",
}

errors = []
for item in REQUIRED:
    if not (ROOT / item).is_file():
        errors.append(f"Missing required path: {item}")

for rel, expected in PROTECTED_BLOBS.items():
    path = ROOT / rel
    if not path.is_file():
        errors.append(f"Protected file missing: {rel}")
        continue
    data = path.read_bytes()
    actual = hashlib.sha1(
        b"blob " + str(len(data)).encode("ascii") + b"\0" + data
    ).hexdigest()
    if actual != expected:
        errors.append(
            f"Protected file changed: {rel} (expected {expected}, got {actual})"
        )

if errors:
    for error in errors:
        print(f"ERROR: {error}")
    sys.exit(1)

print(f"PASS: {len(REQUIRED)} required documentation/support paths exist.")
print(
    f"PASS: all {len(PROTECTED_BLOBS)} protected original files match "
    "their audited Git blob hashes."
)
