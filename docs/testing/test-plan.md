# 🧪 Manual Test Plan

- **Status:** Proposed manual plan
- **Test data:** Synthetic only
- **Safety:** Run in a disposable copy because contacts.txt is rewritten.

| ID | Scenario | Action | Expected visible behavior |
|---|---|---|---|
| T-01 | Startup load | Launch with valid sample file | Records loaded into memory |
| T-02 | Add valid | Add 10-character phone value | Record inserted |
| T-03 | Add invalid length | Add value with another length | Invalid phone message |
| T-04 | Add duplicate | Reuse existing phone | Duplicate message |
| T-05 | Exact search | Search exact name | Matching record printed |
| T-06 | Phone search | Search exact phone | Matching record printed |
| T-07 | Partial search | Search a consecutive name substring | Matching records printed without case distinction |
| T-08 | Missing search | Search unknown value | Not-found message |
| T-09 | Delete | Delete existing phone | Deleted message |
| T-10 | List | Display all records | Alphabetical output |
| T-11 | Modify | Update a matched record | Prompts and modified message |
| T-12 | Export | Export a known contact | vCard file creation is attempted |
| T-13 | Exit | Select option 8 | Process exits |

Record compiler, OS, result, and evidence when tests are actually executed.
