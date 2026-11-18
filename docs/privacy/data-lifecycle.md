# 🔏 Data Lifecycle and Privacy

## Data lifecycle

| Stage | Current implementation |
|---|---|
| Creation | User enters contact values through terminal prompts |
| Initial storage | Rows are loaded from contacts.txt |
| In-memory use | Records are stored in HashTable buckets during the process |
| Update | Add/modify operations change in-memory fields |
| Persistence | The file is rewritten after non-exit menu operations |
| Export | A selected record may be written into a VCF file |
| Deletion | The selected in-memory record is removed and then the file is rewritten |
| Retention | No automated retention policy exists |
| Secure erasure | No secure deletion mechanism exists |

## Privacy guidance

Use synthetic data in this public repository. Keep personal contact data and backups outside version control. The application does not provide encryption, access control, consent management, or a privacy compliance feature.
