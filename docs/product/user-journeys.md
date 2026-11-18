# 🧭 User Journeys

## First run

1. Build the executable with a GNU++17-compatible compiler.
2. Launch it from the repository root.
3. The program attempts to load contacts.txt.
4. The menu is printed.
5. The user selects an operation.

## Add and verify a contact

1. Select menu option 1.
2. Enter a name.
3. Enter a phone number.
4. The add flow checks that the phone number contains 10 characters and is not already present.
5. Enter an email.
6. The contact is inserted.
7. The current contact set is written to contacts.txt.
8. Use exact search or display to inspect the contact.

## Export a contact

1. Select menu option 3.
2. Enter the exact name or phone number.
3. The matching record is retrieved.
4. The application writes a name-derived VCF file in the current working directory.

## Safe usage

Keep a backup of contacts.txt before operations. Do not use real contact details in tracked files or public issue reports.
