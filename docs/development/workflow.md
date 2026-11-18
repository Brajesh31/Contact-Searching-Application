# 🔁 Development Workflow

1. Inspect the existing repository and identify the specific change scope.
2. Keep application behavior, source, dependencies, and application configuration unchanged unless separately authorized.
3. Create a focused branch.
4. Update relevant docs and diagrams alongside supporting changes.
5. Run documentation, SVG, Mermaid-structure, and preservation checks.
6. For application changes separately authorized in another task, compile and test on a disposable data copy.
7. Review every changed path and ensure no personal data was added.
8. Open a focused pull request with evidence and known limitations.

GitHub Actions in this repository are designed to validate documentation and compile the current C++ source. They do not rewrite README content or push commits.
