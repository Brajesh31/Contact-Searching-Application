# 🧹 Code Style and Engineering Guidelines

This document describes conventions for future work. It does not reformat or modify the existing application source.

## Observed baseline

- The application is written in C++.
- The VS Code configuration declares GNU++17.
- The source uses the GNU convenience header <bits/stdc++.h>.
- Most application behavior currently resides in main.cpp as free functions and two simple classes.

## Recommended conventions for future authorized code changes

| Area | Guideline |
|---|---|
| Naming | Use consistent descriptive names; preserve existing names when documenting current code |
| Types | Prefer explicit types that communicate intent |
| Ownership | Make dynamic ownership and lifetime explicit |
| Input | Validate all user-provided fields at the point they enter the program |
| Errors | Check file-open and write operations and report actionable errors |
| Functions | Keep each operation focused and document side effects |
| Data | Define a documented escaping/serialization strategy before extending the CSV-like format |
| Tests | Add tests for success paths, malformed input, and persistence failures |
| Privacy | Never log or commit real contact details |

## Preservation notice

These are recommendations, not authorization to alter the current C++ source, compiler flags, or IDE configurations.
