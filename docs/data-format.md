# 🗃️ Data Format

## Contact file

The application reads `contacts.txt` line by line. Each line is split on commas into three values:

```text
name,phoneNumber,email
```

Example using synthetic data:

```text
Alex Example,5550101234,alex@example.invalid
```

## Parsing behavior

- The first field is read into `Contact.name`.
- The second field is read into `Contact.phoneNumber`.
- The third field is read into `Contact.email`.
- The delimiter is a comma.
- There is no quoting or escaping mechanism for commas inside a field.

Use simple values without commas. Blank or malformed lines are not reported through a dedicated validation mechanism in the current loader.

## Persistence

The contact file is loaded during startup. After each menu operation, the program opens `contacts.txt` for output and serializes the in-memory records as comma-separated lines.

## vCard export

The exporter writes one contact using vCard version 3.0 fields:

```text
BEGIN:VCARD
VERSION:3.0
FN:Alex Example
TEL;TYPE=CELL:5550101234
EMAIL;TYPE=INTERNET:alex@example.invalid
END:VCARD
```

The output filename is derived from the contact's name and uses the `.vcf` extension.

## Privacy

Never commit real contact information. Use reserved/example addresses and synthetic phone numbers for examples and automated validation.
