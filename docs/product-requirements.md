# 🧩 Product Requirements

## Product boundary

The current product is a local CLI address-book demonstration. It provides record entry, lookup, partial-name search, modification, deletion, listing, and vCard export.

## User-visible requirements

- The user can select operations from a numbered terminal menu.
- Contact fields are name, phone number, and email.
- Add rejects phone values whose string length is not 10 and rejects duplicate phone values.
- Exact search matches name or phone.
- Partial search matches a consecutive case-insensitive substring within name.
- Listing is sorted by name.
- The application attempts to persist records to contacts.txt after non-exit menu operations.
- A matching record can be exported as a vCard 3.0 file.

## Explicit non-goals in the current implementation

No browser UI, mobile app, online synchronization, authentication, database, HTTP API, cloud backup, encryption, payment integration, notification service, analytics, or multi-user support is implemented.
