# ⌨️ Commands and Menu Reference

The program does not expose command-line flags or subcommands. It starts an interactive menu.

| Menu choice | Prompt/behavior | Notes |
|---:|---|---|
| 1 | Name, phone, email | Phone length must be 10; duplicate phone rejected |
| 2 | Phone number to delete | Deletes first exact match |
| 3 | Phone or name to export | Attempts name-derived VCF output |
| 4 | Display contacts | Sorts by name |
| 5 | Phone or name to search | Exact equality |
| 6 | Name substring | Case-insensitive consecutive substring |
| 7 | Phone or name to modify | No duplicate or phone validation on replacement |
| 8 | Exit | Returns 0 |

There are no command-line arguments, configurable paths, help switch, or documented non-zero exit codes for application errors.
