# 🌱 Environment Variables

## Current application behavior

The inspected C++ source does not read environment variables. There is no environment-driven configuration layer.

| Variable | Present? | Purpose |
|---|---|---|
| None | No | The application uses a fixed relative data-file path |

## Configuration instead

- Data file: contacts.txt relative to the process working directory.
- Initial bucket count: 10.
- Load-factor check: greater than 0.75 before insertion.
- Export: name-derived .vcf file in the current working directory.

An .env.example file is intentionally not added because there are no application environment variables to demonstrate.
