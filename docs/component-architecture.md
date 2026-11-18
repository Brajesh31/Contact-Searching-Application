# 🧩 Component Architecture

The application has no separately compiled components. The following are logical responsibilities within main.cpp.

| Logical component | Source element | Responsibility | Dependencies |
|---|---|---|---|
| Data model | Contact | Stores three string fields | C++ string |
| Container | HashTable | Owns bucket array and size value | vector<Contact>, raw pointer |
| Insert/growth | insertContact(), rehash() | Adds contacts and expands buckets | HashTable, Contact |
| Lookup | contactExists(), getContact(), Search(), fuzzySearch() | Finds exact or partial matches | HashTable |
| Mutation | modify(), deleteContact() | Changes or removes entries | HashTable, console I/O |
| Presentation | main(), display() | Menu, prompts, output | iostream, algorithm |
| Persistence | main() file streams | Load and rewrite contacts.txt | fstream, stringstream |
| Export | exportToVCF() | Writes one record to VCF | ofstream |

There is no independent front-end, back-end, service, repository, or API component.
