# 🆘 Disaster Recovery

The application is a local executable and has no hosted service or automated disaster-recovery system.

## Recovery source

The only data recovery mechanism is a user-managed backup of contacts.txt. VCF exports may also exist but are not a complete replacement for the source file.

## Recovery procedure

1. Stop the application.
2. Preserve the current file separately.
3. Restore a known-good contacts.txt backup.
4. Confirm three comma-separated fields per line.
5. Test with a disposable copy and synthetic values.
6. Record whether any records were lost.

No RTO/RPO targets, scheduled backups, or successful disaster-recovery drill are established.
