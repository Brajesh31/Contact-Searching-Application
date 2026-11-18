# 🧪 Testing Strategy

## Current repository state

The audited application tree does not contain an automated unit or integration test suite. This page defines safe manual checks and separates them from tests that have not yet been implemented.

## Build check

```bash
g++ -std=gnu++17 -Wall -Wextra main.cpp -o contact-search
```

This command is a suggested local compiler invocation, not a recorded successful CI run.

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
python3 scripts/repository_audit.py
```

These scripts validate documentation and the preservation boundary only. They do not execute or prove application correctness.

## Not yet available

No automated unit, integration, fuzz, performance, accessibility, or security test suite is claimed.
