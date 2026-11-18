# 📐 Code Standards

The source baseline is a single C++ file configured for GNU++17. This page complements the root [CODE_STYLE.md](../CODE_STYLE.md).

## Current standards and recommendations

- Preserve the existing source until a separate application-change task is authorized.
- Keep identifiers descriptive and consistent.
- Validate terminal input and file records at the boundary in any future approved code change.
- Check file stream state and report failures.
- Prefer explicit ownership and RAII for new code.
- Keep persistence format and parsing rules synchronized.
- Add tests for both success and failure paths.
- Avoid logging or committing personal contact data.
- Do not claim a standard or compiler portability that has not been tested.

The current source has signed/unsigned comparison warnings in several loops, and this is recorded rather than silently changed.
