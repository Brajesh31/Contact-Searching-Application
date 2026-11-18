# 🧑‍🔧 Developer Guide

## Source map

The complete application is in main.cpp. The architecture and module inventories are in [architecture](architecture.md) and [module documentation](module-documentation.md).

## Development baseline

- Preserve source and application behavior under repository-enhancement scope.
- Build with GNU++17.
- Use synthetic data and a temporary working directory for runtime tests.
- Run scripts/validate_docs.py, scripts/validate_svg.py, scripts/validate_mermaid.py, scripts/check_license.py, scripts/repository_audit.py.
- Run tests/test_cli_smoke.py against a compiled executable.

## Change scope

Any application-code change requires separate authorization and should carry focused tests, a clear diff, and data-safety review.
