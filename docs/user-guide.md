# 🕹️ User Guide

The program prints a numbered menu in the terminal.

## Menu options

### 1. Add a contact

Prompts for a name, phone number, and email. The add path rejects a phone number whose length is not exactly 10 characters and rejects a phone number already present in the table. The source does not perform comprehensive phone or email validation.

### 2. Delete a contact

Prompts for a phone number and removes the first matching record. A message is printed when the contact is deleted or not found.

### 3. Export contact to VCF

Prompts for a name or phone number. If the contact is found, the program attempts to write a file named after the contact's name in vCard 3.0 format in the current working directory. The export routine can report a file-open failure; the calling menu code may still print its success message, so verify that the file exists.

### 4. Display contacts

Collects records from the hash-table buckets, sorts them by name, and prints name, phone number, and email.

### 5. Search contact

Searches for an exact name or exact phone-number match and prints matching records.

### 6. Fuzzy search contact

Performs a case-insensitive substring search on contact names. For example, a query of `"ann"` can match a name containing those consecutive characters. This is not edit-distance matching and does not guarantee typo correction.

### 7. Modify contact

Searches for an exact name or phone-number match, then prompts for a new name, phone number, and email. The current implementation does not repeat the add operation's validation and duplicate check during modification.

### 8. Exit

Prints an exit message and terminates the process.

## Data is written after a menu iteration

After processing a menu option other than the immediate exit path, the application opens `contacts.txt` for output and writes the current records. This rewrites the file. Keep backups and test with disposable data.

## Practical safety

Never test with a real address book in a public checkout. Use synthetic sample data and a copy of the repository.
