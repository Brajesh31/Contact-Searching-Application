# 🗒️ Product Decisions and Observations

| ID | Decision/observation | Evidence | Status |
|---|---|---|---|
| PD-01 | Keep the program terminal-based | main.cpp uses console input/output and numbered menu | Existing behavior |
| PD-02 | Store contact fields in local text file | contacts.txt input/output in main() | Existing behavior |
| PD-03 | Use vCard 3.0 for export | exportToVCF() emits VERSION:3.0 | Existing behavior |
| PD-04 | Menu label says fuzzy search but algorithm is substring matching | fuzzySearch() uses string::find() | Terminology clarification |
| PD-05 | Treat real address-book data as sensitive | Contact records are plaintext | Repository safety guidance |
| PD-06 | Preserve application code during repository enhancement | User scope for repository tasks | Active enhancement boundary |

No undocumented product stakeholder decisions are inferred.
