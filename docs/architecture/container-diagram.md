# 📦 Container Diagram

The C4 container view collapses to one executable process and local files.

~~~mermaid
flowchart TB
    User["User"] --> Proc["C++ executable"]
    subgraph Process["Single process"]
        Menu["Menu and input"]
        Operations["Contact operations"]
        Table["HashTable / Contact records"]
        Menu --> Operations
        Operations <--> Table
    end
    Data[("contacts.txt")] <--> Proc
    Export["VCF file"] <-- Proc
~~~

No containers, microservices, databases, queues, or hosted infrastructure exist in the current project.
