# 📦 Deployment and Distribution

This repository produces a local C++ command-line executable. No hosted production runtime, Docker image, Kubernetes topology, cloud account, database, staging server or remote deployment exists.

## Local distribution

1. Install a GNU++17-compatible compiler.
2. Compile main.cpp using the build guide.
3. Place an intended contacts.txt in the process working directory.
4. Keep private address books outside the public repository.
5. Keep a private backup before running operations.
6. Verify any exported VCF file.

## CI/CD

GitHub Actions validates docs, compiles the executable, runs a temporary-data CLI smoke test, runs CodeQL, and scans repository history for secrets. These are CI checks, not an application deployment pipeline.

See the CI/CD architecture, GitHub Actions, and deployment-environments documents.
