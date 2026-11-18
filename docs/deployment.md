# 📦 Local Deployment and Distribution

This repository builds a local command-line executable. No hosted production deployment, Docker image, or server process is implemented.

## Local installation

1. Obtain the source repository.
2. Install a GNU++17-compatible compiler.
3. Compile main.cpp using the command in [build guide](development/build.md).
4. Keep contacts.txt in the process working directory.
5. Run the executable.

## Distribution cautions

- Distribute only synthetic sample data.
- Never bundle a personal address book into a public release.
- Document compiler/OS compatibility for each binary.
- Preserve a backup before replacing local contact data.

## Deployment verification

No external production environment exists to validate. A local build is checked by the C++ workflow; runtime behavior is not represented as production-certified.
