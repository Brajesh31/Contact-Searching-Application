# 🧩 Component Diagram

See the editable [component source](component.mmd).

~~~mermaid
flowchart TB
    Main["main()"]
    Load["File loader"]
    Menu["Menu dispatcher"]
    Insert["insertContact() / rehash()"]
    Read["Search / getContact / contactExists"]
    Mutate["modify() / deleteContact()"]
    View["display()"]
    Export["exportToVCF()"]
    Save["contacts.txt writer"]
    Main --> Load
    Main --> Menu
    Menu --> Insert
    Menu --> Read
    Menu --> Mutate
    Menu --> View
    Menu --> Export
    Menu --> Save
~~~
