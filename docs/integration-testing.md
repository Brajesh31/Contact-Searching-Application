# 🔗 Integration Testing

The repository includes one CLI integration smoke test in tests/test_cli_smoke.py. It compiles the actual application in CI and runs it from a temporary directory containing synthetic contact data.

The test exercises startup loading, add, exact search, partial-name search, file persistence, and VCF export. It verifies that tracked repository data is not used by the test.

Additional cases remain in docs/test-plan.md and are not currently automated.
