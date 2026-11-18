# 🧪 Quality Assurance

## Quality gates currently available

1. GNU++17 compilation with warning flags.
2. CLI smoke test using temporary synthetic data.
3. Markdown local-link validation.
4. SVG XML and accessibility-title validation.
5. Mermaid source structural validation.
6. MIT license marker check.
7. Repository required-path and protected-file-hash audit.
8. CodeQL static analysis.

## Remaining coverage gaps

Delete, modify, duplicate rejection, invalid input, missing-file behavior, malformed rows, export failure, file-write failure, fuzzing, and performance remain outside the automated smoke test. See [feature-to-test matrix](testing/feature-test-matrix.md).
