# 📁 Project Structure

## Original application files

| Path | Purpose |
|---|---|
| main.cpp | Complete C++ command-line implementation |
| contacts.txt | Startup contact data and runtime persistence target |
| Dummy Contacts.txt | Additional sample contact rows |
| Eswar.vcf, Vignesh.vcf | Existing example vCard files |
| Contact Searching Appliaction.pptx | Existing project presentation; filename spelling is preserved |
| .vscode/c_cpp_properties.json | VS Code compiler and IntelliSense configuration |
| .vscode/settings.json | VS Code file associations |
| .idea/.gitignore | Existing IDE-specific ignore rules |
| .gitignore | Existing executable ignore rule |

## Added repository support

| Path | Responsibility |
|---|---|
| docs/ | Product, architecture, usage, development, security, accessibility, testing, operations, maintenance documentation |
| docs/architecture/ | Editable Mermaid diagrams and architecture decision record |
| docs/assets/ | Project branding and original technical diagrams |
| docs/templates/ | Reusable product and engineering templates |
| scripts/ | Documentation, asset, license, and preservation validators |
| .github/ISSUE_TEMPLATE/ | Structured issue forms |
| .github/workflows/ | Documentation validation, C++ compile, CodeQL, and retired legacy workflow notice |

## Preservation

The original C++ source, contact samples, VCF examples, PowerPoint, IDE settings, and .gitignore are preserved. Their original Git blob identifiers are checked by scripts/repository_audit.py.
