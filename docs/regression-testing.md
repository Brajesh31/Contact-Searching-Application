# 🔁 Regression Testing

After changes to the CLI or serialization behavior, rerun:
1. GNU++17 compile.
2. tests/test_cli_smoke.py against the compiled executable.
3. Manual cases for delete, modify, invalid phone, duplicate phone, malformed rows, and file-write errors.
4. Documentation and asset validation.
5. CodeQL analysis.

The existing automated suite is not broad enough to detect all regressions. Any future source change requires an expanded test matrix.
