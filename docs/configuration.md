# ⚙️ Configuration Reference

## Runtime configuration

The inspected source has no environment-variable configuration interface.

| Setting | Current source behavior |
|---|---|
| Contact data file | Relative path contacts.txt |
| Initial bucket count | 10 |
| Rehash threshold | Load factor greater than 0.75 |
| Phone check on add | Length must be 10 |
| Export format | vCard VERSION:3.0 |
| Export location | Current working directory |
| Export filename | Contact name with .vcf extension |

## Editor configuration

The repository includes VS Code C/C++ settings. These are existing project files and are preserved. The configured compiler path is machine-specific to a Windows MinGW installation.

## Environment variables

None are read by the current application. An .env.example file is therefore not applicable.
