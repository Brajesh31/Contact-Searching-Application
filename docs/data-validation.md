# ✅ Data Validation

## Add path

- Name is read as a line.
- Phone number is read as a line.
- The only phone rule is string length equals 10.
- Duplicate phone values are rejected.
- Email is read using formatted extraction, so whitespace ends the value.

## Load path

Rows are split on commas. There is no row-count validation, escaping, type validation, normalization, or duplicate check during file loading.

## Modify path

A contact is found by exact name or phone. Replacement values are read, but the add path's phone-length and duplicate-phone checks are not reused.

## Search path

Exact search compares strings. Partial search lowercases the name and query and performs substring matching.

The actual implementation is less strict than a validated contact-data schema. No email or phone standards compliance is claimed.
