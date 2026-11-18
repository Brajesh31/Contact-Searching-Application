# 🚦 Quality Gates

| Gate | Workflow/script | Required evidence |
|---|---|---|
| Documentation links | scripts/validate_docs.py | No broken local Markdown targets |
| SVG assets | scripts/validate_svg.py | XML parsed and title/desc present |
| Mermaid source | scripts/validate_mermaid.py | Diagram declaration and basic structure checked |
| License | scripts/check_license.py | MIT markers found |
| Repository audit | scripts/repository_audit.py | Required files and protected blob hashes verified |
| Application build | .github/workflows/cpp-build.yml | GNU++17 compile succeeds |
| CLI behavior smoke test | tests/test_cli_smoke.py | Temporary-data test succeeds |
| Static analysis | .github/workflows/codeql.yml | CodeQL job completes successfully |

A green quality workflow is evidence for only the checks it runs. It is not a production certification.
