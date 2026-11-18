# 🛟 Resilience

The current CLI has limited resilience:
- No transactional persistence.
- No automatic recovery after a failed write.
- No backup rotation.
- No retry policy.
- No validation report for malformed startup rows.
- No multi-process file locking.

The only documented recovery path is a user-managed backup restore. No availability or resilience target is claimed.
