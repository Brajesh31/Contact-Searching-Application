# 🔗 Software Supply-Chain Security

## Current application dependency surface

The application uses C++ standard-library facilities and the GCC convenience header bits/stdc++.h. No external C++ package manifest, vendored libraries, or package lockfile was present in the audited tree.

## Repository automation dependencies

GitHub Actions are used for checkout, Python setup, CodeQL, and workflow execution. Dependabot is configured for GitHub Actions updates.

## Controls and limits

- Review workflow changes and permissions.
- Review dependency-update pull requests.
- Keep compile and CodeQL workflows green.
- Do not invent a third-party dependency inventory where none exists.
- No SBOM artifact is currently generated; the application package inventory is limited to compiler and standard library/toolchain assumptions.
