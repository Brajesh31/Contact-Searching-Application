# ⌨️ Command Reference

## Build

~~~bash
g++ -std=gnu++17 -Wall -Wextra main.cpp -o contact-search
~~~

## Run on Linux/macOS

~~~bash
./contact-search
~~~

## Run on Windows PowerShell

~~~powershell
.\contact-search.exe
~~~

## Repository checks

~~~bash
python3 scripts/validate_docs.py
python3 scripts/validate_svg.py
python3 scripts/validate_mermaid.py
python3 scripts/repository_audit.py
~~~

Repository checks inspect documentation and supporting files only. They do not mutate application data or perform application logic tests.
