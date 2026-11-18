# 🔒 Data Protection

## Data handled

The program stores contact names, telephone numbers, and email addresses in plaintext. It writes local records to contacts.txt and VCF exports.

## Handling guidance

- Only use synthetic contact records in the public repository.
- Store real address books outside the checkout and outside version control.
- Do not publish unredacted console output or VCF files.
- Restrict OS-level access to local address-book files.
- Back up important local data before using operations that rewrite the file.
- Delete exported files when no longer needed, using the host operating system's normal secure-data procedures where appropriate.

## Encryption and retention

The current program does not implement encryption, retention scheduling, or secure deletion. No legal or regulatory compliance certification is claimed.
