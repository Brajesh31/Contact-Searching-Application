# 🔐 Security Policy

## Scope

This repository contains a local C++ command-line contact manager. It reads and writes contact records in `contacts.txt` and can export records to vCard files.

## Reporting a vulnerability

Please do not publish exploit details, personal contact records, or sensitive data in a public issue.

Use GitHub's **Private vulnerability reporting** feature for this repository when it is enabled. If private reporting is unavailable, contact the repository maintainer privately through the contact method listed on the maintainer's GitHub profile. Include:

- A concise description of the issue and affected file/function.
- Reproduction steps using synthetic data.
- Expected and actual impact.
- Compiler/platform information, if relevant.
- A suggested mitigation, if known.

Do not attach real phone numbers, real email addresses, or real contact exports.

## Security considerations

- Treat all contact records as personal data.
- Use synthetic data in examples, issues, demonstrations, and tests.
- Do not commit real address books, exported VCF files, or private backups.
- Keep local contact data in a private working copy and review staged changes before pushing.
- Do not put credentials or personal contact information into issue descriptions or logs.

## Supported versions

The repository currently documents the default branch. No formal release/version support schedule is published.

## Response and disclosure

The maintainer will assess reports, request clarification if needed, and coordinate a fix or mitigation before public disclosure where practical. No fixed response-time commitment is currently established.

## Security scope limitations

This policy records a reporting process. It does not claim that the application has undergone a security audit, fuzz testing, or formal privacy/compliance assessment.
