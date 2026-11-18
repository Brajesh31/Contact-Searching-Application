# 🧪 Test Data Management

- Automated tests create their own contacts.txt in a temporary directory.
- Test values use reserved .invalid email domains and synthetic names/phone-like values.
- Tests must not execute against the tracked contacts.txt.
- Do not copy real personal contacts into fixtures, logs, screenshots, or issue reports.
- The original tracked contact and VCF files were preserved and have not been certified as anonymized by this repository audit.
- Remove temporary data at the end of the test run.
