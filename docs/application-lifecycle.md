# 🔁 Application Lifecycle

~~~mermaid
flowchart TD
    A([Process starts]) --> B[Allocate 10-bucket table]
    B --> C[Attempt to open contacts.txt]
    C --> D[Read and split rows]
    D --> E[Insert records]
    E --> F[Print menu]
    F --> G{Menu choice}
    G -->|1 to 7 or invalid| H[Execute branch]
    H --> I[Attempt full contacts.txt rewrite]
    I --> F
    G -->|8| J([Return 0])
~~~

The source does not explicitly validate that the input or output streams opened successfully. The exit path returns before the file rewrite for that iteration.
