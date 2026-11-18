# ADR-001: Local text-file persistence

- **Status:** Accepted as an observed implementation decision
- **Date:** 2026-11-18
- **Scope:** Documentation of existing behavior, not a new implementation decision

## Context

The current program loads comma-separated records from contacts.txt at startup and writes the current in-memory contact collection back to that file after menu operations.

## Observed implementation

The application uses C++ file streams and a simple comma-delimited three-field record. It does not use a database or separate persistence service.

## Consequences

- The application is simple to run locally.
- The data file must be available relative to the process working directory.
- Fields containing commas are not represented safely by the current format.
- Writes replace the whole file and are not transactional.
- Users should keep backups and avoid tracking real personal contact information.

## Future review

A robust format, atomic writes, and explicit persistence error handling may be evaluated in a separately authorized engineering task.
