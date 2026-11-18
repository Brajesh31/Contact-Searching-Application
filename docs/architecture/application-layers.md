# 🧱 Application Layers

The source does not implement a strict layered architecture. The following is a conceptual grouping of responsibilities, not a claim that these are separate modules.

| Logical concern | Current location | Coupling |
|---|---|---|
| Presentation | main() prompts and display() | Mixed with orchestration |
| Application operations | Free functions in main.cpp | Operate directly on HashTable |
| Data structure | Contact and HashTable | Same source file |
| Persistence | ifstream/ofstream in main() | Directly coupled to menu flow |
| Export | exportToVCF() | Writes filesystem output directly |

Any future separation would be an application refactor and requires separate authorization.
