#!/usr/bin/env python3
"""Check required docs and verify protected files retain original Git blob IDs."""
from pathlib import Path
import hashlib
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "LICENSE", "SECURITY.md", "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md", "SUPPORT.md", "CHANGELOG.md", "ROADMAP.md",
    "AUTHORS.md", "CITATION.cff", "CODEOWNERS", "GOVERNANCE.md",
    "docs/README.md", "docs/architecture.md", "docs/user-guide.md",
    "docs/testing.md", "docs/security.md", "scripts/README.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
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
    actual = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
    if actual != expected:
        errors.append(f"Protected file changed: {rel} (expected {expected}, got {actual})")
if errors:
    for error in errors:
        print(f"ERROR: {error}")
    sys.exit(1)
print(f"PASS: {len(REQUIRED)} required documentation/support files exist.")
print(f"PASS: all {len(PROTECTED_BLOBS)} protected original files match their audited Git blob hashes.")
