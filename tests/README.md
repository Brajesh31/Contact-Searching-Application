# 🧪 Application Smoke Tests

This folder contains an automated command-line integration smoke test for the existing application.

## What is verified

The test runs the compiled executable in a temporary directory with synthetic contacts. It exercises:

- Startup parsing of a contact record.
- Adding another contact through the menu.
- Persistence of both rows to the temporary contacts.txt.
- Exact name search.
- Case-insensitive partial-name search.
- Export of a selected contact to vCard 3.0.

The test never runs against or rewrites the repository's tracked contacts.txt file.

## Run

Build the application from the repository root:

```bash
g++ -std=gnu++17 -Wall -Wextra -Wpedantic main.cpp -o contact-search
python3 tests/test_cli_smoke.py ./contact-search
```

The script uses only the Python standard library.

## Scope

This is one end-to-end CLI smoke test, not a unit-test suite, fuzz test, performance test, or security certification. It does not justify changing the application source as part of repository documentation work.
