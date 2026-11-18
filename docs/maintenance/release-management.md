# 🚀 Release Management

## Current state

No semantic version tags, release binaries, release notes, or compatibility matrix were present in the audited tree.

## Suggested future approach

- Adopt semantic versioning only when a release policy and compatibility expectations are established.
- Keep a human-readable changelog.
- Compile the exact release commit with the supported GNU++17 toolchain.
- Record compiler version, operating system, build command, and test evidence.
- Publish source and any binary artifacts with matching version identifiers.
- Do not claim signed builds or reproducibility until verified.

No release automation is enabled because the project has no established version/tag process.
