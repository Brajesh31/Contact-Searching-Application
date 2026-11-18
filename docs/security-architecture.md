# 🔐 Security Architecture

## Current security boundary

The application is a local process with terminal input, a local contacts.txt file, in-memory contact values, and name-derived VCF output. It does not implement a login system, roles, network listeners, API authentication, or encryption.

## Assets

- Contact names, phone numbers, and emails.
- The tracked contact file and local backups.
- Exported vCard files.
- Repository integrity and GitHub credentials used by maintainers.

## Controls currently present

| Control | Current implementation |
|---|---|
| Duplicate phone check | Add flow only |
| Phone length check | Add flow only |
| Local filesystem permissions | Delegated to operating system |
| Source analysis | CodeQL workflow |
| Build validation | GNU++17 compile workflow |
| Personal-data guidance | SECURITY.md and privacy documentation |

## Important limitations

No access control, encrypted storage, secure deletion, formal audit logging, input sanitization framework, transactional save, or independent security audit is implemented. See [threat model](security/threat-model.md).
