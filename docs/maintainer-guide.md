# 🧭 Maintainer Guide

## Routine maintenance

1. Review issues and proposed work for scope and privacy.
2. Keep README and technical documentation aligned with main.cpp.
3. Review GitHub Actions updates and least-privilege permissions.
4. Run documentation and asset validation.
5. Compile and execute the disposable-data CLI smoke test.
6. Review CodeQL findings and source compiler warnings.
7. Keep changelog and roadmap accurate.
8. Review tracked sample contact data before public distribution.

## Boundaries

The current repository has no release automation, service monitoring, database migration process, or hosted deployment. Avoid adding workflows that assume those systems exist.
