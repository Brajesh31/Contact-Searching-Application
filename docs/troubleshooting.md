# 🛠️ Troubleshooting

## Compiler cannot find `bits/stdc++.h`

Use a GCC-compatible compiler and GNU dialect. The header is not part of the ISO C++ standard library and may be unavailable in some toolchains.

## `contacts.txt` cannot be opened

Run the executable with the repository root as the current working directory, or ensure the expected data file exists in the process working directory.

## Contact changes appear unexpected

The application rewrites `contacts.txt` after menu operations. Work on a backup copy and inspect the file after the operation.

## Search does not find a near-spelling

The current partial search requires the query characters to appear consecutively in the name after lowercasing. It is not an edit-distance or phonetic search.

## VCF file is not created

Check that the working directory is writable and that the generated filename is valid on the host operating system. The filename is derived from the contact name.

## Need more help

Open an issue with a synthetic reproduction case. See [SUPPORT.md](../SUPPORT.md).
