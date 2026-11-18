# 🔐 Security Architecture

The architecture has no internal identity or role system. Its security boundary is local terminal input and local filesystem access.

- Terminal values and file rows are external input.
- Contact values are plaintext in process memory.
- contacts.txt and VCF files are plaintext on disk.
- File permissions are enforced by the operating system.
- CodeQL scans C++ source in GitHub Actions.
- Gitleaks will be used for repository secret scanning.

See [security controls matrix](../security-controls-matrix.md) and [threat assessment](../threat-assessment.md). No security certification is claimed.
