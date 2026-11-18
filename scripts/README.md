# 🧰 Repository Validation Scripts

These Python scripts use the standard library and validate repository documentation and supporting files. They do not alter application source, runtime data, dependencies, or application configuration.

## Commands

~~~bash
python3 scripts/validate_docs.py
python3 scripts/validate_svg.py
python3 scripts/validate_mermaid.py
python3 scripts/check_license.py
python3 scripts/repository_audit.py
~~~

## Checks

| Script | Checks |
|---|---|
| validate_docs.py | Local Markdown file links and image references |
| validate_svg.py | SVG XML structure and required accessible title/description |
| validate_mermaid.py | Mermaid source presence and basic structural sanity |
| check_license.py | Presence and basic MIT license markers |
| repository_audit.py | Required documentation plus exact Git blob hashes for protected original files |

These checks do not replace a full Markdown renderer, Mermaid compiler, compiler test, security audit, or accessibility audit.
