# 📐 Development Conventions

## Documentation

- Prefer precise project-specific statements.
- Use tables for inventories and structured behavior.
- Include an owner/status when a procedure needs accountability.
- Mark future ideas as proposals.
- Link to diagrams' editable source.
- Do not claim audits or test results that have not been performed.

## C++ source baseline

The current project is a single main.cpp file with Contact and HashTable classes plus free functions. Do not assume a multi-layer architecture or introduce module claims not supported by the code.

## Data and privacy

Use synthetic data. Review staged files for phone numbers, email addresses, address-book exports, and credentials.

## Review

Any authorized application code change should include a focused explanation, build evidence, test scenarios, and explicit discussion of persistence/data safety implications.
