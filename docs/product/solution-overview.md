# 🧩 Solution Overview

The application uses a local C++ process.

1. Load rows from contacts.txt during startup.
2. Parse each row into name, phone number, and email fields.
3. Insert records into the in-memory hash-table structure.
4. Accept an operation through the terminal menu.
5. Run the corresponding contact function.
6. Rewrite contacts.txt after the operation unless the user exits.
7. For export, write a separate vCard 3.0 file.

The implementation and current limitations are described in the architecture, user guide, and data format pages.
