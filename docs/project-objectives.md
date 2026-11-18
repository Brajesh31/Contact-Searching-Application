# 🎯 Project Objectives

The implemented objective is to provide a local terminal program for basic contact-record operations.

| Objective | Existing implementation | Evidence boundary |
|---|---|---|
| Store a contact | Contact contains name, phoneNumber, email | main.cpp |
| Add a contact | Menu option 1 with simple phone-length and duplicate-phone checks | Add path only |
| Find a contact | Exact name or phone search | Search() |
| Search partial names | Case-insensitive substring search | fuzzySearch() |
| Modify a contact | Exact name or phone match, then replace fields | modify() |
| Delete a contact | Delete first phone-number match | deleteContact() |
| Display contacts | Sort by name and print | display() |
| Export | Write vCard 3.0 text | exportToVCF() |
| Persist | Load and rewrite contacts.txt | main() |

No formal market research, user interviews, business outcome targets, or product KPI commitments are present in the audited source. This page does not invent them.
