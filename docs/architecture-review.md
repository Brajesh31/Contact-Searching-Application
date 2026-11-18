# 🏗️ Architecture Review

- **Review basis:** main.cpp and repository configuration.
- **Scope:** current local C++ CLI.
- **Application code modified:** No.

## Findings

| ID | Finding | Impact | Follow-up |
|---|---|---|---|
| AR-01 | Menu, domain operations, persistence, and presentation are in main.cpp | Tight coupling and limited isolated testing | Consider separation in a separately approved refactor |
| AR-02 | Raw dynamic allocation manages the bucket array | Manual lifetime and ownership | Evaluate RAII |
| AR-03 | Bucket index is computed before a possible rehash and not recalculated | Inconsistent post-resize placement | Add regression test and fix only in authorized code task |
| AR-04 | CSV-like storage has no quoting/escaping | Fields containing commas cannot round-trip | Design versioned serialization |
| AR-05 | File stream failures are not consistently checked | Data loss or false success may go unnoticed | Add explicit result handling |
| AR-06 | Several operations linearly scan the table | Lookup cost grows with record count | Measure before redesign |
| AR-07 | No comprehensive automated test suite | Behavior regressions may go undetected | Extend integration and unit tests |

## Review conclusion

The architecture is adequate for a small educational CLI, but it is not a production-grade address-book service. No security or reliability certification is implied.
