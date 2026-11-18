# 🧩 Architecture and Requirement Traceability

| Requirement / capability | Source area | Documentation | Verification reference |
|---|---|---|---|
| Startup load | main() file loader | data-format.md, data-flow.md | T-01 |
| Add contact | insertContact(), menu case 1 | user-guide.md, features.md | T-02 to T-04 |
| Delete contact | deleteContact(), menu case 2 | user-guide.md | T-09 |
| Exact search | Search(), menu case 5 | user-guide.md | T-05, T-06, T-08 |
| Partial-name search | fuzzySearch(), menu case 6 | user-guide.md, known-limitations.md | T-07 |
| Update | modify(), menu case 7 | user-guide.md | T-11 |
| Sorted list | display() | architecture.md | T-10 |
| vCard export | exportToVCF(), menu case 3 | data-format.md | T-12 |
| Persistence | contacts.txt input/output | data-flow.md | T-01, T-02 |
| Exit | menu case 8 | user-guide.md | T-13 |

Test references describe planned manual checks; they are not pass records.
