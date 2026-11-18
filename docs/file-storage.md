# 💾 File Storage

## Runtime files

| File | Role | Format |
|---|---|---|
| contacts.txt | Startup load and persistent current contact set | Three comma-separated fields per line |
| name-derived .vcf | Selected contact export | vCard 3.0 text |
| Other tracked examples | Existing repository assets | Preserved as supplied |

## Persistence behavior

main() opens contacts.txt for input at process startup. After each menu option other than the immediate exit path, it opens the same path for output and writes every in-memory record. This truncates and rewrites the file.

## Known limitations

- No quoting/escaping for commas.
- No schema version.
- No atomic temporary-file replacement.
- No file lock for concurrent processes.
- Input and output stream states are not consistently checked.
- The current working directory determines the resolved path.

Use backups and synthetic data. No external storage service is involved.
