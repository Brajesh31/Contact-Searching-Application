# 📋 Functional and Non-Functional Requirements

## Functional requirements

| ID | Requirement | Implementation evidence |
|---|---|---|
| FR-01 | Load contact rows when the program starts | Startup file-reading loop in main() |
| FR-02 | Store name, phone, and email | Contact class |
| FR-03 | Add a contact with duplicate phone check | Menu option 1 and contactExists() |
| FR-04 | Delete by phone number | deleteContact() |
| FR-05 | Find by exact name or phone | Search() |
| FR-06 | Search partial name text without case distinction | fuzzySearch() |
| FR-07 | Modify an exact matching record | modify() |
| FR-08 | Display alphabetically by name | display() and compareContactsByName() |
| FR-09 | Export a selected record as vCard 3.0 | exportToVCF() |
| FR-10 | Persist modified in-memory data | contacts.txt output loop |

## Non-functional observations

- **Platform:** terminal application; current editor configuration targets Windows MinGW.
- **Compiler:** GNU++17-compatible toolchain is recommended due to the source header.
- **Persistence:** local file, relative to the process working directory.
- **Privacy:** contact data should be synthetic in public repository use.
- **Reliability:** there is no transaction or backup mechanism in the current program.
- **Performance:** several lookup operations scan all buckets; measured performance is not available.
- **Accessibility:** terminal interaction depends on text output and keyboard input; no formal audit is present.

No unsupported service-level, security, scalability, or performance target is asserted.
