# ↩️ Rollback and Recovery

There is no hosted deployment to roll back. The only operational rollback is restoration of the local data file from a known-good backup.

1. Stop the process.
2. Preserve the current file.
3. Restore the backup copy of contacts.txt.
4. Validate the three-field structure.
5. Test with a disposable copy before resuming use.

For repository changes, use normal Git history and review the exact commit diff before reverting. Do not overwrite application source or user data as part of an automated rollback.
