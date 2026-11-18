# 💾 Local Data Recovery Runbook

1. Stop the application before replacing its data file.
2. Preserve a copy of the current contacts.txt for diagnosis.
3. Identify the most recent known-good backup.
4. Restore the backup into the working directory.
5. Confirm each record follows the three-field comma-delimited format.
6. Run the application with synthetic validation records first.
7. Record the recovery date and whether any data was lost.

No backup scheduler or automated disaster-recovery process is implemented in the application.
