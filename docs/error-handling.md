# 🚦 Error Handling

## Current error paths

| Failure or condition | Observed behavior |
|---|---|
| Invalid numeric menu choice | Prints Invalid choice and continues |
| Non-numeric menu input | Stream fail state is not explicitly cleared; repeated input may fail |
| Add phone length not 10 | Prints Invalid Phone Number |
| Add duplicate phone | Prints Contact already exists |
| Delete missing phone | Prints Contact not found |
| Search missing value | Prints Contact not found |
| Partial search no match | Prints No matching contacts found |
| Export file cannot open | exportToVCF() prints an error; caller still prints a success message |
| contacts.txt cannot open | Startup stream state is not checked |
| contacts.txt rewrite fails | Output stream state is not checked |

There is no centralized error type, exception policy, retry system, or structured log. These are source-level limitations, not claims of graceful recovery.
