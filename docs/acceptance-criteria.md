# ✅ Acceptance Criteria

The test matrix in [testing/test-plan.md](testing/test-plan.md) contains scenario-level steps. These criteria describe current behavior and do not imply that every scenario has passed.

| Capability | Observable acceptance statement |
|---|---|
| Load | Valid three-field rows from contacts.txt are inserted during startup |
| Add | A 10-character phone value with no existing exact duplicate is accepted for insertion |
| Duplicate | An existing phone value is rejected by the add flow |
| Search | An exact name or phone match is printed |
| Partial search | A case-insensitive consecutive substring match is printed |
| Display | The visible list is in ascending name order |
| Delete | The first matching phone record is removed |
| Modify | An exact name/phone match opens replacement prompts |
| Export | A selected record is serialized using vCard 3.0 markers |
| Persistence | The process attempts to rewrite contacts.txt after non-exit menu choices |

File-open failures, invalid non-numeric menu input, malformed rows, and modification edge cases require separate negative tests.
