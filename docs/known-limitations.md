# ⚠️ Known Limitations

These are observations from the inspected source, not newly introduced changes.

## Input and data

- The add path checks phone-number length only.
- The modify path does not use the add path's phone validation or duplicate-phone check.
- Email input uses formatted extraction in add/modify, so whitespace-containing values are not read as a complete line.
- The comma-separated file format cannot represent commas within a field.
- File loading has no dedicated malformed-row reporting.
- The program uses a relative path for `contacts.txt`.

## Search and data structure

- The menu's fuzzy-search operation is a lowercased substring match, not edit-distance typo tolerance.
- Several operations scan all buckets.
- The table uses manual dynamic allocation and does not define a dedicated cleanup path for the allocated bucket array before process exit.
- The insertion and rehash routines should be reviewed separately before changing their behavior.

## Persistence and export

- The contact file is rewritten after menu operations rather than updated transactionally.
- The application does not implement automatic backups.
- Export filenames come directly from contact names.
- Export success is printed by the caller after invoking the exporter, while the exporter itself can report a file-open failure.

## Testing and release

- No application test suite or formal release matrix was present in the audited tree.
- No production deployment target is documented.

These limitations are recorded for transparency. They are not fixed by this documentation-only change.
