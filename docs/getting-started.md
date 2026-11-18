# 🚀 Getting Started

## Requirements

- Git, when cloning from GitHub.
- GCC or another compiler supporting the GNU `<bits/stdc++.h>` header.
- GNU++17-compatible compilation.
- A terminal.

## Clone

```bash
git clone https://github.com/Brajesh31/Contact-Searching-Application.git
cd Contact-Searching-Application
```

## Compile

```bash
g++ -std=gnu++17 -Wall -Wextra main.cpp -o contact-search
```

## Launch

```bash
./contact-search
```

On Windows PowerShell:

```powershell
.\contact-search.exe
```

## Working directory

Run from the repository root. The program opens `contacts.txt` using a relative path and writes the file after each menu iteration.

## Safe first run

Make a copy of the repository or back up `contacts.txt` before testing. Use synthetic contact records only. The current data file is modified by normal operations.

## First operation

Choose a number from the printed menu and follow the prompts. The [user guide](user-guide.md) explains each menu item.
