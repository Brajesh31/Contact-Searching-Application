# 📈 Scalability Considerations

The current application is designed for a small local contact list, not distributed or multi-user use.

- All records are held in process memory.
- The table starts at 10 buckets and may double when the insertion load check exceeds 0.75.
- Several operations scan every bucket.
- Display copies all records and sorts them.
- Persistence rewrites the complete contact file.
- There is no concurrent access control, network synchronization, or service process.

No maximum supported contact count or scaling benchmark has been established. Avoid publishing scalability claims without tests.
