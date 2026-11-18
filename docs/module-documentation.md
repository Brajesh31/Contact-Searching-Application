# 📚 Module Documentation

All implementation currently resides in main.cpp. This module inventory maps each significant class/function to its observable responsibility.

| Element | Role | Important behavior or caveat |
|---|---|---|
| Contact | Domain record | Three public strings |
| HashTable | Bucket container | Raw pointer to vector<Contact> array |
| rehash() | Growth | Doubles bucket count, re-inserts existing contacts |
| insertContact() | Add | Index is calculated before possible rehash |
| contactExists() | Lookup predicate | Full scan for exact name or phone |
| getContact() | Retrieval | Returns an empty Contact when not found |
| deleteContact() | Delete | Removes first matching phone, decrements global count |
| exportToVCF() | Export | Returns void; caller cannot detect export success |
| display() | List | Copies all records to vector and sorts |
| Search() | Exact search | Exact name or phone comparison |
| fuzzySearch() | Partial search | Case-insensitive substring |
| modify() | Update | No phone validation or duplicate check |
| main() | Application orchestration | Input, file loading, menu, file rewrite |

No module-level ownership boundary or public library API exists.
