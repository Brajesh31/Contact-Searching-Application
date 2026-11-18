# 🧭 Feature Prioritization

No formal backlog scoring model or approved milestone plan was found. This priority view is a technical recommendation based on source-observed risks.

| Priority | Area | Reason | Status |
|---|---|---|---|
| P0 | Protect contact data from accidental overwrite | Whole-file write is not atomic and file errors are unchecked | Recommendation only |
| P1 | Add automated negative tests | Invalid input, duplicate add, delete, modify, and write failures lack automated coverage | One happy-path smoke test exists |
| P1 | Improve serialization | CSV fields have no escape strategy | Current format unchanged |
| P2 | Improve input/error handling | Stream state and field validation are limited | Current behavior documented |
| P2 | Simplify memory ownership | Raw dynamic array and pointer ownership | Current source preserved |
| P3 | Expand usability | Optional command-line arguments or configurable data path | Not implemented |

This is not a commitment to implement the items.
