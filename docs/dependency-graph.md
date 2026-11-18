# 🧩 Dependency Graph

~~~mermaid
flowchart TD
    Main["main.cpp / main()"]
    Contact["Contact"]
    Table["HashTable"]
    Ops["Contact operation functions"]
    File["C++ file streams"]
    Std["C++ standard library"]
    Terminal["Terminal input/output"]

    Main --> Table
    Main --> Ops
    Ops --> Contact
    Ops --> Table
    Main --> File
    Main --> Terminal
    Contact --> Std
    Table --> Std
    Ops --> Std
~~~

No external application package or library manifest was present in the repository. The application depends on the compiler's C++ standard-library implementation and GCC-style header availability.
