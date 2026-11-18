# 🧰 Repository Scripts

These scripts validate repository content or build/test the application with temporary data. They do not modify main.cpp, tracked contact fixtures, IDE configuration, dependencies or application behavior.

| Script | Purpose |
|---|---|
| setup.sh / setup.ps1 | Check local compiler and Python prerequisites |
| validate_docs.py / validate-links.py | Validate local Markdown links |
| validate_markdown.py | Check code fences, final newline and trailing whitespace |
| check-project-structure.py | Check important paths and README directory references |
| security-check.sh | Check tracked secret-like filenames and run Gitleaks when installed |
| release-check.sh | Run repository release preflight checks |
| validate_mermaid.py | Basic Mermaid source structure check, not a full renderer |
| validate_svg.py | Parse SVG and require title/description |
| check-env-example.py | Verify whether the application reads environment variables |
| verify-assets.py | Check local Markdown image references and SVG metadata |
| check_license.py | Check expected MIT license markers |
| test-project.sh | Compile app and run smoke test plus repository validators |
| production-check.sh | Run local verification and available security checks |
| repository_audit.py | Required-path audit and protected original Git blob checks |

## Example

~~~bash
bash scripts/test-project.sh
~~~

Use security-check.sh with Gitleaks installed for local content/history scanning. The GitHub Secret Scanning workflow uses Gitleaks in CI. A pass from the filename-only fallback is not a full secrets audit.
