# 🧪 Test Strategy

Use layered checks appropriate for a small command-line application.

| Layer | Current or planned coverage |
|---|---|
| Compile | Automated GNU++17 compile |
| CLI integration | One temporary-data smoke test |
| Unit | Not implemented; source functions are not separated into a testable module |
| Negative cases | Manual plan only |
| Data-format | Manual malformed-row tests not automated |
| Security | CodeQL static analysis; no penetration test |
| Accessibility | Manual review checklist; no audit run |
| Performance | No benchmark suite |
| Documentation | Link, SVG, Mermaid-structure, and repository audit scripts |

All automated behavior tests must use temporary data. They must never overwrite the tracked contacts.txt file.
