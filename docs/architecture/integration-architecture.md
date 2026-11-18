# 🔌 Integration Architecture

The only integrations are local operating-system interfaces:

| Interface | Direction | Purpose |
|---|---|---|
| Terminal stdin/stdout | Bidirectional | Menu input and results |
| contacts.txt | Read at startup, rewrite after menu operations | Contact persistence |
| Name-derived VCF file | Write | Export one selected contact |

No third-party API, webhook, database, queue, analytics SDK, payment provider, or cloud service is integrated.
