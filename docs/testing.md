# 🧪 Testing Strategy

## Current repository state

The original application tree did not contain an automated test suite. Repository enhancement now adds one standard-library Python CLI integration smoke test. There are still no unit tests, fuzz tests, or performance benchmarks.

## Build check

```bash
g++ -std=gnu++17 -Wall -Wextra -Wpedantic main.cpp -o contact-search
```

The GitHub Actions build job executes this compiler command and then runs the CLI smoke test.

## Automated CLI smoke test

```bash
python3 tests/test_cli_smoke.py ./contact-search
```

The test launches the real executable in a temporary directory using synthetic records. It verifies startup loading, adding a contact, exact search, case-insensitive partial-name search, persistence to the temporary data file, and vCard 3.0 export. The test does not read or overwrite the tracked contacts.txt file.

See [tests/README.md](../tests/README.md) and [feature-to-test matrix](testing/feature-test-matrix.md).

## Manual smoke-test scenarios

Use a disposable working copy and synthetic data.

| Scenario | Expected observable behavior |
|---|---|
| Start with sample file | Existing valid rows are loaded |
| Add a 10-character number | New contact is inserted unless duplicate |
| Add an existing phone | Duplicate warning |
| Add a number of another length | Invalid phone warning |
| Search exact name | Matching record is printed |
| Search exact phone | Matching record is printed |
| Partial name query | Names containing the query case-insensitively are printed |
| Display | Entries print in name order |
| Delete existing phone | Success message |
| Delete unknown phone | Not-found message |
| Export a matching contact | A vCard file is attempted |
| Modify an existing contact | Prompts for replacement fields |
| Exit | Process terminates |

## Documentation validation

```bash
python3 scripts/validate_docs.py
python3 scripts/validate_svg.py
python3 scripts/validate_mermaid.py
python3 scripts/check_license.py
python3 scripts/repository_audit.py
```

These checks validate documentation, supporting assets, licensing markers, and the preservation boundary. They do not prove every application behavior.

## Not yet available

No automated unit-test suite, fuzzing, load/performance testing, accessibility audit, or security certification is claimed.
