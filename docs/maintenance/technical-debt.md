# 🧱 Technical Debt Register

The following items are visible from the current implementation and should be considered before future code changes.

| ID | Observation | Potential impact | Evidence / next step |
|---|---|---|---|
| TD-01 | Comma-delimited storage has no escaping | Fields containing commas cannot round-trip | Design format and migration plan |
| TD-02 | Input validation is limited | Invalid values may enter or corrupt data | Define field validation rules |
| TD-03 | Modify path does not repeat add validation | Duplicate or malformed data can be introduced | Add focused tests before future change |
| TD-04 | Several lookups scan all buckets | Performance may degrade as data grows | Measure and review data structure |
| TD-05 | Manual dynamic allocation | Ownership/lifetime errors are possible | Review RAII in separate code task |
| TD-06 | Whole-file writes are not transactional | Interrupted writes may lose data | Evaluate atomic replacement and backup |
| TD-07 | No automated application tests | Regressions are harder to detect | Build test harness using temporary data |

These are documentation observations, not changes made in this task.
