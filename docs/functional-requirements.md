# 📋 Functional Requirements

The IDs below describe the current application behavior, not a future specification.

| ID | Requirement | Current implementation |
|---|---|---|
| FR-01 | Load persisted records | Read contacts.txt line by line at startup |
| FR-02 | Represent a contact | Three string fields: name, phoneNumber, email |
| FR-03 | Insert a record | Add through menu option 1 |
| FR-04 | Reject duplicate phone on add | contactExists() before insertion |
| FR-05 | Search exact name or phone | Search() |
| FR-06 | Search a partial name | Lowercase substring match in fuzzySearch() |
| FR-07 | Modify a record | modify() uses exact name or phone equality |
| FR-08 | Delete a record by phone | deleteContact() |
| FR-09 | List in name order | display() collects and sorts |
| FR-10 | Export one record | exportToVCF() writes vCard 3.0 |
| FR-11 | Persist current records | Rewrite contacts.txt after non-exit operations |
| FR-12 | Exit | Menu option 8 returns 0 |

The file parser expects three comma-separated fields. It does not implement quoting or escaping.
