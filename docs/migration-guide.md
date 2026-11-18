# 🔄 Migration Guide

No versioned data schema or migration tooling exists. The current contacts.txt format is three comma-delimited values per line: name, phone number, email.

Before any manual format conversion:
- Make a private backup.
- Use synthetic test data first.
- Define escaping and encoding behavior.
- Validate record counts before and after.
- Keep the original file until the converted version is verified.

No automated migration is provided.
