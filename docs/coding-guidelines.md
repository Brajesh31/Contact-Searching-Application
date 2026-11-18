# 🧑‍💻 Coding Guidelines

These are guidelines for separately authorized future C++ work. They do not change the current application.

1. Keep domain logic separate from console input and file persistence.
2. Validate each input field before mutation.
3. Define an explicit record serialization format, including escaping.
4. Check every file-open, read, write, and close outcome.
5. Prefer safe value ownership over raw dynamic allocation.
6. Keep search behavior and terminology consistent.
7. Make mutation operations stop after the intended target is handled.
8. Test duplicate, malformed, missing, empty, and boundary inputs.
9. Use temporary directories for persistence tests.
10. Keep examples synthetic and redact any personal data.
