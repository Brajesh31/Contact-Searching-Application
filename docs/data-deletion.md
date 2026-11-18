# 🗑️ Data Deletion

Menu option 2 deletes the first in-memory contact whose phone number exactly matches the input. The program then rewrites contacts.txt after the menu operation.

Limitations:
- No confirmation step.
- No recycle bin or undo.
- No secure overwrite.
- Backups and exported VCF files are not removed.
- The file rewrite is not atomic.

Deleting a record from the application does not guarantee removal of all copies of the data.
