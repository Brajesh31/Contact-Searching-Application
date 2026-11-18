# 📁 Project Structure

This structure reflects the tracked application and added repository-support areas. The complete per-file list is visible in GitHub's repository tree.

## Original application and data

| Path | Purpose |
|---|---|
| main.cpp | Complete C++ CLI application |
| contacts.txt | Startup data and runtime persistence target |
| Dummy Contacts.txt | Existing additional sample |
| Eswar.vcf, Vignesh.vcf | Existing vCard examples |
| Contact Searching Appliaction.pptx | Existing presentation, filename spelling preserved |
| .vscode/ | Existing compiler/editor configuration |
| .idea/.gitignore | Existing IDE ignore rules |
| .gitignore | Existing executable ignore rule |

## Repository support

| Directory/path | Responsibility |
|---|---|
| Root governance files | License, authorship, contribution, security, support, governance and status |
| .github/ISSUE_TEMPLATE/ | Bug, feature, docs, security, accessibility, performance and question forms |
| .github/workflows/ | C++ build/smoke, docs validation, CodeQL, Gitleaks |
| docs/product/ | Product overview, feature details, requirements and journeys |
| docs/architecture/ | Architecture documentation, Mermaid diagrams and ADRs |
| docs/security/, docs/privacy/ | Threats, controls, data lifecycle and recovery |
| docs/accessibility/ | Terminal accessibility review guidance |
| docs/testing/ | Manual test plan and feature-to-test mapping |
| docs/development/ | Build, debugging, tooling and workflow guidance |
| docs/deployment/, docs/operations/ | Local distribution and operating procedures |
| docs/maintenance/ | Technical debt, risks, metrics, decisions and release management |
| docs/templates/ | Reusable product and engineering templates |
| docs/assets/ | Branding, technical illustrations and workflow visuals |
| scripts/ | Repository, Markdown, asset, license, security and environment checks |
| tests/ | Disposable-data CLI integration smoke test |

## Preservation

The original C++ source, contact samples, VCF files, presentation, IDE configuration and .gitignore are checked by exact Git blob IDs in scripts/repository_audit.py.
