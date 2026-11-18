# 🌐 System Context Diagram

The terminal user is the only external actor. The program reads and writes local files through the operating system.

~~~mermaid
flowchart LR
    User["Terminal user"] --> App["Contact Searching Application"]
    App <-->|"load / save"| Data[("contacts.txt")]
    App -->|"export selected record"| VCF["Name-derived .vcf"]
    App <-->|"standard input / output"| Terminal["Operating system terminal"]
~~~

There is no remote identity provider, database server, API consumer, or external business service.
