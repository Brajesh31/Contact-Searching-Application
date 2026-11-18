# 🖥️ Environment Matrix

| Area | Observed / documented requirement | Notes |
|---|---|---|
| Source language | C++ | Single primary source file |
| Language mode | GNU++17 | Existing VS Code config |
| Compiler path | Windows MinGW path in workspace config | Machine-specific, preserved |
| Header support | GNU bits/stdc++.h | GCC-compatible environment recommended |
| Runtime | Local terminal | No web server |
| Input data | contacts.txt in current working directory | Relative path |
| Output | Console, contacts.txt, VCF files | Requires writable working directory |
| Documentation checks | Python 3 | Supporting automation only |

No macOS, Linux, or alternate compiler compatibility matrix has been independently validated.
