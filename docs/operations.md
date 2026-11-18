# 🧭 Operations

The current operational model is local execution and file protection.

- Launch from the directory containing contacts.txt.
- Back up the data file before running operations.
- Avoid simultaneous execution from multiple processes against the same file.
- Verify VCF output and save it only in an appropriate private location.
- If writes fail, stop using the current copy and restore from backup.
- Use synthetic records for demonstrations and troubleshooting.

There is no monitoring, alerting, scheduler, server process, or operational on-call rotation.
