# 🛟 Failure and Recovery Architecture

The current application has no built-in recovery subsystem.

- File-open and write failures are not consistently checked.
- contacts.txt is rewritten directly rather than through an atomic temporary-file swap.
- There is no automatic backup, transaction log, or recovery journal.
- Manual recovery uses a private copy of the last known-good contacts.txt.

See [failure modes](../failure-modes.md) and [disaster recovery](../disaster-recovery.md).
