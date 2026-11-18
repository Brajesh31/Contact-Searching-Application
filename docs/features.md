# ✨ Feature Inventory

This is the canonical feature summary. See [product feature details](product/features.md) and [acceptance criteria](product/acceptance-criteria.md) for the complete inventory and verification map.

| Feature | Menu | Implemented behavior | Limitation |
|---|---:|---|---|
| Add contact | 1 | Reads name, phone, email; requires phone length 10 and rejects duplicate phone | Does not validate numeric-only phone or email syntax |
| Delete contact | 2 | Deletes the first exact phone match | No confirmation or undo |
| Export contact | 3 | Attempts to write vCard 3.0 named after contact | Caller prints success even if file open failed |
| Display | 4 | Sorts and prints contacts by name | No pagination |
| Exact search | 5 | Exact name or phone equality | Linear scan |
| Partial-name search | 6 | Case-insensitive substring match | Not typo-tolerant edit-distance search |
| Modify | 7 | Finds exact name or phone and prompts for replacement fields | No duplicate/phone validation after modification |
| Exit | 8 | Prints message and returns success | Process exits without explicit table deallocation |

Data is read from contacts.txt at startup and the file is rewritten after every non-exit menu iteration.
