# 🏁 Production Setup

This project has no server-side production deployment. The relevant setup is local execution:

1. Install a GNU++17-compatible compiler.
2. Compile main.cpp.
3. Place a valid contacts.txt in the process working directory.
4. Restrict filesystem access to the address-book data.
5. Back up contacts.txt before use.
6. Verify export files before distribution.

The current application is not suitable for storing sensitive or regulated address books without further engineering work such as encryption, access control, robust validation, transactional writes, and comprehensive tests.
