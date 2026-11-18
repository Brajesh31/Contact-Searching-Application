# 🐞 Development Troubleshooting

| Symptom | Likely cause | Check |
|---|---|---|
| bits/stdc++.h not found | Compiler is not GCC-compatible | Use GCC/MinGW with GNU++17 |
| contacts not loaded | Wrong working directory or missing file | Confirm contacts.txt relative to current directory |
| Changes disappear | Output file could not be written or wrong file path used | Check directory permissions and current directory |
| Export file absent | Invalid name/path or output directory issue | Confirm file exists; caller may print success even after export failure |
| Input repeats or menu behaves unexpectedly | cin entered fail state after non-numeric menu input | Restart process |
| Link validation fails | Markdown target missing or path incorrect | Run scripts/validate_docs.py and fix target |

Use synthetic data and a disposable directory when reproducing problems.
