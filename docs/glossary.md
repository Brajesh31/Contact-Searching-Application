# 📖 Glossary

| Term | Meaning in this project |
|---|---|
| Contact | A record with name, phone number, and email |
| Hash table | Bucket array used by the application to organize contacts |
| Bucket | A vector<Contact> at an index in the table |
| Linear probing | Advancing through bucket indices when an initial bucket is occupied |
| Rehash | Rebuild into a larger bucket array |
| Load factor | Contact count divided by bucket-array size in the insertion routine |
| Exact search | Equality comparison against name or phone |
| Partial-name search | Case-insensitive consecutive substring matching |
| vCard | Text-based contact interchange format; this project writes version 3.0 |
| Working directory | Process current directory used to resolve contacts.txt and output files |
