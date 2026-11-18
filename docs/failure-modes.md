# ⚠️ Failure Modes

| Failure | Trigger | Current behavior | Recovery guidance |
|---|---|---|---|
| Missing input file | contacts.txt absent | No explicit error check on startup stream | Confirm working directory; restore or create a valid file |
| Malformed row | Missing or extra fields | Parser has no strict row validator | Restore a known-good copy |
| Comma in field | User or file value includes comma | Fields do not round-trip safely | Avoid commas until format is improved |
| Write failure | Directory or disk unavailable | Output stream not checked | Stop using copy and restore from backup |
| Export failure | File cannot be created | Export function prints error; caller still prints success | Verify output file exists and is readable |
| Invalid numeric menu input | Letters entered at numeric prompt | Input stream fail state not reset | Restart process |
| Duplicate after modify | Update creates same phone as another record | No duplicate check in modify() | Review data file and restore if needed |

The table is descriptive; these failures are not all covered by automated tests.
