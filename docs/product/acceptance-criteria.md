# ✅ Acceptance Criteria Reference

This table describes the observable behavior currently present and can be used when manually reviewing the application.

| Feature | Current acceptance observation |
|---|---|
| Startup load | Valid three-field rows are read from contacts.txt |
| Add | A phone number with length other than 10 is rejected |
| Duplicate | A matching phone number is rejected on add |
| Delete | A matching phone number is removed; missing phone reports not found |
| Exact search | Name or phone exact equality returns contact details |
| Partial search | Consecutive case-insensitive name substring returns results |
| List | All stored contacts print in ascending name order |
| Modify | An exact name or phone match prompts for replacement values |
| Export | Existing match is serialized with vCard 3.0 field labels |
| Exit | Option 8 terminates the process |

These criteria describe current behavior; they are not a claim that an automated test suite exists.
