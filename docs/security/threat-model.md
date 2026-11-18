# 🛡️ Threat Model

## System scope

The application is a local command-line process that reads contacts.txt, accepts terminal input, stores records in memory, rewrites the contact file, and writes selected VCF exports.

## Assets

- Contact names, phone numbers, and emails.
- contacts.txt and exported VCF files.
- Repository write access and project integrity.

## Trust boundaries

| Boundary | Input | Concern |
|---|---|---|
| Terminal to process | User-entered fields and menu choice | Malformed or unexpected input |
| Local file to process | contacts.txt records | Invalid delimiters or malformed rows |
| Process to filesystem | Rewritten text and VCF output | Accidental overwrite, unsafe path/name, write failure |
| Contributor to repository | Commits and issues | Accidental disclosure of real contact data |

## Threat scenarios

| Threat | Existing exposure | Defensive practice |
|---|---|---|
| Personal data disclosure | Contact rows and VCF files are plain text | Use synthetic data and keep personal files untracked |
| Corrupted contact store | Whole file is rewritten | Keep backups and use disposable test copies |
| Malformed input | Limited field validation | Validate data before use; do not assume current code rejects all malformed values |
| Unsafe export name | Output filename is derived from contact name | Review names and output path before running |
| Unauthorized repository change | Public repository contribution surface | Review changes and restrict write access in GitHub settings |

## Limitations

This threat model is a documentation-level assessment based on source inspection. It is not a penetration test or formal security assessment.
