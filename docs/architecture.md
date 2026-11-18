# 🏗️ Architecture

## System shape

The inspected application is a single-process C++ command-line program. Its primary implementation is main.cpp. It has no network or database layer.

![System architecture](assets/architecture/system-architecture.svg)

Editable sources: [system-architecture.mmd](architecture/system-architecture.mmd), [system-context.mmd](architecture/system-context.mmd), [container view](architecture/system-container.mmd), [component view](architecture/component.mmd), [sequence diagram](architecture/sequence.mmd), [state diagram](architecture/state-machine.mmd), and [class diagram](architecture/class-diagram.mmd).

## Runtime components

| Component | Implementation | Responsibility |
|---|---|---|
| Contact model | Contact | Three string properties |
| Table container | HashTable | Bucket count and dynamically allocated bucket array |
| Bucket | vector<Contact> | Stores contact records in a bucket |
| Input/menu | main() | Reads menu choices and fields |
| Persistence | ifstream / ofstream | Loads and rewrites contacts.txt |
| Search/operations | Free functions | Add, find, update, delete, list, and export |
| VCF exporter | exportToVCF() | Emits vCard 3.0 text |

## Data structure and insertion

The table begins with 10 buckets. Insertion derives an initial index from the contact name length modulo the table size. If that bucket is occupied, it advances through buckets using linear probing. Each bucket itself is a vector.

When the calculated load factor exceeds 0.75, the rehash routine doubles the table size and reinserts records.

## Search characteristics

Exact search, contact existence checks, retrieval, deletion, display, and partial-name search scan across buckets. Do not infer constant-time behavior for every operation from the presence of a hash table.

## Persistence boundary

The in-memory table is initialized from contacts.txt. The application rewrites the file after processing each non-exit menu choice. There is no separate database abstraction, transaction system, or backup mechanism in the current source.

## Trust boundaries

Terminal input and file contents should be treated as untrusted. Current validation is limited. This document does not certify that all trust boundaries are enforced.
