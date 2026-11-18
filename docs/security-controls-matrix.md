# 🧱 Security Controls Matrix

| Control area | Expected control | Current state | Evidence |
|---|---|---|---|
| Authentication | User identity verification | Not implemented | No login code |
| Authorization | Role or permission checks | Not implemented | Local single-user process |
| Input validation | Validate all external data | Partial | Add path only validates phone length and duplicate phone |
| Data at rest | Encryption | Not implemented | Plaintext file format |
| File integrity | Atomic writes or integrity check | Not implemented | Direct full-file rewrite |
| Audit logging | Security event log | Not implemented | Console output only |
| Vulnerability analysis | Static analysis | Configured | CodeQL workflow |
| Secret handling | No hard-coded credentials | No app secrets used | No environment variable interface |
| Privacy | Minimize tracked personal data | Guidance only | SECURITY.md and data-protection documentation |
| Recovery | Backup and restore | Manual guidance | disaster-recovery.md |

This matrix does not represent a compliance framework certification.
