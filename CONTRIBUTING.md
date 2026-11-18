# 🤝 Contributing

Thank you for considering a contribution.

## Current contribution scope

The application is treated as a complete existing project for repository-enhancement work. Preserve `main.cpp`, existing application behavior, data files, IDE settings, compiler configuration, and dependencies unless a separately authorized task explicitly requests an application change.

Documentation, diagrams, issue/PR templates, repository governance, and supporting validation scripts are appropriate contribution areas.

## Before you start

1. Read the [README](README.md) and [documentation index](docs/README.md).
2. Check open issues to avoid duplicating work.
3. For substantial changes, open an issue first to discuss scope.
4. Never use real personal contact information in examples.

## Local setup

A GNU-compatible C++17 compiler is recommended.

```bash
g++ -std=gnu++17 -Wall -Wextra main.cpp -o contact-search
```

Run from the repository root because the program opens `contacts.txt` using a relative path. Use a private disposable copy when testing operations that rewrite the contacts file.

## Contribution workflow

1. Fork the repository.
2. Create a focused branch, for example `docs/clarify-data-format`.
3. Make a narrowly scoped change.
4. Run the documentation checks when documentation or assets change:

   ```bash
   python3 scripts/validate_docs.py
   python3 scripts/repository_audit.py
   ```

5. Review the diff and confirm no protected application files changed.
6. Open a pull request using the repository template.

## Documentation standards

- Keep claims aligned with the actual implementation.
- Label planned functionality as planned, not implemented.
- Use Mermaid source for editable diagrams.
- Use descriptive alt text for meaningful visuals.
- Prefer concise, reproducible instructions.
- Do not claim test, accessibility, security, or performance results without evidence.

## Commit messages

Use clear, imperative messages, for example:

- `docs: explain contact file format`
- `docs: add architecture diagram`
- `chore: validate documentation links`

## Pull requests

Include the purpose, changed paths, evidence, validation performed, and any known limitations. State explicitly whether any application source or configuration changed. Under the current preservation policy, such changes should not be included.
