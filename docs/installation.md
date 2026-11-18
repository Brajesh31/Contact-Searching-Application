# 📥 Installation

This project is compiled from source rather than installed through a package manager.

## Requirements

- Git, if cloning.
- A GCC-compatible C++ compiler with GNU++17 support.
- A terminal or command prompt.

## Install from source

~~~bash
git clone https://github.com/Brajesh31/Contact-Searching-Application.git
cd Contact-Searching-Application
g++ -std=gnu++17 -Wall -Wextra -Wpedantic main.cpp -o contact-search
~~~

Run the executable from the repository directory so contacts.txt resolves correctly. Use a private disposable copy for tests that modify records.
