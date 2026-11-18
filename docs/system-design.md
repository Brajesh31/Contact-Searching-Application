# 🏗️ System Design

## Design summary

The application is a single executable with in-memory contact storage. It loads a local comma-delimited text file on startup, handles menu choices, then rewrites the file after each non-exit menu iteration.

## Logical design

| Area | Implementation |
|---|---|
| User interface | Console menu and standard input |
| Domain record | Contact: name, phoneNumber, email |
| Collection | HashTable with dynamically allocated vector<Contact> buckets |
| Insertion | Initial bucket from name length modulo table size, then linear probing |
| Growth | Rehash doubles bucket-array size when the pre-insert load check exceeds 0.75 |
| Persistence | ifstream load and ofstream rewrite of contacts.txt |
| Export | vCard 3.0 text output to a name-derived filename |

## Important implementation caveat

insertContact() calculates the bucket index before checking whether rehash is required. If rehash runs, the index is not recalculated against the new table size. The inserted element still probes from that old index, but the distribution no longer follows the new name-length hash calculation.

## Missing architectural facilities

There is no separate UI/domain/storage layer, transaction boundary, database, API, authentication, cache, network client, worker queue, monitoring service, or production deployment environment.
