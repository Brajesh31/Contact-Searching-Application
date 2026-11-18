# 🧪 Test Plan

| ID | Scenario | Expected result | Automated? |
|---|---|---|---|
| TP-01 | Load one valid synthetic row | Record available for search | Yes, smoke test |
| TP-02 | Add valid contact | Record inserted | Yes |
| TP-03 | Exact name search | Added contact printed | Yes |
| TP-04 | Partial-name search | Matching initial contact printed | Yes |
| TP-05 | Persistence | Both rows remain in temporary file | Yes |
| TP-06 | vCard export | Expected vCard 3.0 fields emitted | Yes |
| TP-07 | Duplicate phone on add | Duplicate message | Manual |
| TP-08 | Phone length not 10 | Invalid phone message | Manual |
| TP-09 | Delete existing contact | Contact removed | Manual |
| TP-10 | Modify existing contact | New values stored | Manual |
| TP-11 | Missing contacts.txt | Startup behavior recorded | Manual |
| TP-12 | Export path invalid | Error message and false-success behavior observed | Manual |
| TP-13 | Non-numeric menu choice | Fail-state behavior observed | Manual |
| TP-14 | Malformed CSV row | Parsing behavior recorded | Manual |

Run tests in a temporary directory with synthetic values only.
