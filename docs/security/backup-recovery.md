# 💾 Backup and Recovery

## Current behavior

The application rewrites contacts.txt after non-exit menu operations. It has no built-in backup rotation or transactional write mechanism.

## Safe manual backup

Before a session, copy contacts.txt to a private backup location outside the public repository. Do not commit backups.

## Recovery

1. Stop the application.
2. Preserve the current file for diagnosis if needed.
3. Restore the last known good copy of contacts.txt.
4. Confirm the restored file contains the expected three comma-separated fields per line.
5. Relaunch from the repository directory.
6. Validate with synthetic records where possible.

## Recovery testing

No automated disaster-recovery drill has been performed. Record actual restore tests and dates before claiming that recovery objectives have been met.
