# 🔁 CI/CD Architecture

The repository uses GitHub Actions for quality checks. It does not deploy a service.

| Workflow | Trigger | Action |
|---|---|---|
| Documentation Validation | Docs, scripts, and workflow changes | Links, SVG, Mermaid structure, license, and repository audit |
| C++ Build and CLI Smoke Test | C++ source, tests, or test docs changes | Compile and run disposable-data CLI integration smoke test |
| CodeQL | Push, pull request, weekly schedule | C++ static analysis |

There is no automated binary publishing, container publishing, staging deployment, production deployment, or rollback deployment. The current process is CI, not a full continuous-delivery pipeline.
