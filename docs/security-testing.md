# 🧪 Security Testing

## Current automated checks

- CodeQL analysis for C++ is configured in .github/workflows/codeql.yml.
- The compiler is run with warning flags in the C++ CI workflow.
- The repository audit checks protected original-file hashes and required support paths.

## Not performed

No penetration test, fuzz test, formal threat-model workshop, dynamic application scan, cryptographic assessment, or external security audit is claimed.

## Manual review scenarios

- [ ] Confirm public tracked contact files contain no information that must remain private.
- [ ] Test malformed contacts.txt rows in a disposable directory.
- [ ] Test file-write permission failures in a temporary location.
- [ ] Test export names containing operating-system reserved characters.
- [ ] Confirm issues and logs do not contain personal contact values.
