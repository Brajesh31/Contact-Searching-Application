# ✨ Feature Inventory

The following capabilities were verified against main.cpp.

| ID | Feature | Entry point | Current behavior |
|---|---|---|---|
| F-01 | Add contact | Menu 1 | Reads name, phone, and email; checks 10-character phone length and duplicate phone |
| F-02 | Delete contact | Menu 2 | Deletes by exact phone number |
| F-03 | Export contact | Menu 3 | Writes selected record as a vCard 3.0 file |
| F-04 | List contacts | Menu 4 | Prints contacts sorted by name |
| F-05 | Exact search | Menu 5 | Searches exact name or phone number |
| F-06 | Partial-name search | Menu 6 | Case-insensitive substring match |
| F-07 | Modify contact | Menu 7 | Updates fields for exact name or phone match |
| F-08 | Exit | Menu 8 | Exits the process |
| F-09 | Persistence | Startup and end of menu iteration | Loads and rewrites contacts.txt |

The partial-name search is called fuzzy search by the menu, but it does not implement edit-distance typo correction.
