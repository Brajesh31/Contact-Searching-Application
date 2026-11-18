<div align="center">

  <img src="docs/assets/branding/logo.svg" alt="Contact Searching Application logo" width="112" />

  # 📇 Contact Searching Application

  **A C++ command-line contact manager built around a custom hash-table implementation.**

  Manage contacts, search by name or phone number, find partial name matches, update records, and export individual contacts as vCard files.

  ![Language](https://img.shields.io/badge/C%2B%2B-17%20compatible-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
  ![Interface](https://img.shields.io/badge/interface-CLI-1F6FEB?style=for-the-badge)
  ![Storage](https://img.shields.io/badge/storage-local%20text%20file-2DA44E?style=for-the-badge)
  ![License](https://img.shields.io/badge/license-MIT-8A2BE2?style=for-the-badge)

  [📖 Documentation](docs/README.md) · [🐛 Report a bug](https://github.com/Brajesh31/Contact-Searching-Application/issues/new?template=bug_report.yml) · [💡 Request a feature](https://github.com/Brajesh31/Contact-Searching-Application/issues/new?template=feature_request.yml)

</div>

---

## ✨ Overview

Contact Searching Application is a terminal-based address-book program written in C++. It loads comma-separated contact records from `contacts.txt` into an in-memory custom hash-table structure and provides a menu for maintaining and searching those records.

The repository is intentionally documented as the implementation currently exists. It is not a web application, does not expose an HTTP API, and does not use a database server.

## 🖼️ Project preview

![Project banner](docs/assets/branding/project-banner.svg)

The application is interactive in a terminal. The menu and operations are described in the [user guide](docs/user-guide.md). No fabricated application screenshots are used.

## 🚀 Features

| Capability | Current behavior |
|---|---|
| ➕ Add | Prompts for name, 10-character phone number, and email; checks duplicate phone numbers |
| 🔎 Exact search | Scans contacts for an exact name or phone-number match |
| 🔤 Partial-name search | Case-insensitive substring matching against names |
| 📝 Modify | Finds by exact name or phone number, then prompts for replacement fields |
| 🗑️ Delete | Deletes the first matching phone number |
| 📋 List | Displays all contacts sorted by name |
| 📤 Export | Writes one selected contact as a vCard 3.0 `.vcf` file |
| 💾 Persistence | Rewrites `contacts.txt` after each completed menu operation |

> **Search terminology:** the current “Fuzzy Search” menu option is a case-insensitive substring search. It does not calculate edit distance or correct arbitrary spelling mistakes.

## 🧰 Technology

- **Language:** C++
- **Standard/library usage:** standard C++ facilities, included through `<bits/stdc++.h>`
- **Data structure:** custom hash-table wrapper whose buckets are `vector<Contact>`
- **Collision handling:** linear probing across buckets
- **Growth:** rehash routine doubles the bucket-array size after the load-factor check
- **Persistence:** comma-separated text file, `contacts.txt`
- **Contact export:** vCard 3.0 text format
- **Editor configurations present:** Visual Studio Code and JetBrains project metadata

The existing VS Code configuration declares GNU++17. The source uses the GNU convenience header `<bits/stdc++.h>`, so a GCC-compatible toolchain is the most direct build environment.

## 🏗️ Architecture

![Architecture overview](docs/assets/architecture/system-architecture.svg)

At startup, `main()` allocates the hash table and reads `contacts.txt`. The menu dispatches user requests to the contact operations. Most operations work on the in-memory table. At the end of each menu iteration, the program rewrites the contact file from the table.

### Main source responsibilities

| Source element | Responsibility |
|---|---|
| `Contact` | Holds a name, phone number, and email |
| `HashTable` | Holds the bucket count and dynamically allocated bucket array |
| `insertContact()` | Inserts a contact, checks load factor, and may trigger rehashing |
| `rehash()` | Allocates a larger bucket array and reinserts existing entries |
| `contactExists()` | Checks an exact name or phone-number match |
| `getContact()` | Returns a matching contact or an empty contact |
| `deleteContact()` | Removes a contact by phone number |
| `Search()` | Prints exact name or phone-number matches |
| `fuzzySearch()` | Performs case-insensitive substring matching on names |
| `modify()` | Updates fields for a matching contact |
| `display()` | Collects and sorts contacts by name before printing |
| `exportToVCF()` | Writes a vCard 3.0 file |
| `main()` | Initializes storage, loads data, dispatches the menu, and persists records |

## 📂 Repository structure

```text
Contact-Searching-Application/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── workflows/
│   └── PULL_REQUEST_TEMPLATE.md
├── docs/
│   ├── architecture/
│   ├── assets/
│   │   ├── architecture/
│   │   ├── branding/
│   │   └── workflows/
│   ├── templates/
│   └── ...
├── scripts/
├── .gitignore
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── MAINTAINERS.md
├── README.md
├── ROADMAP.md
├── SECURITY.md
├── SUPPORT.md
├── main.cpp
├── contacts.txt
├── Dummy Contacts.txt
└── ...
```

The tree above focuses on the maintained documentation and key application files. See [project structure](docs/project-structure.md) for the complete audited inventory.

## ⚙️ Getting started

### Prerequisites

- A C++ compiler with GNU C++17 support, such as GCC.
- A terminal or command prompt.
- Git, if cloning the repository.

### 1. Clone

```bash
git clone https://github.com/Brajesh31/Contact-Searching-Application.git
cd Contact-Searching-Application
```

### 2. Compile

```bash
g++ -std=gnu++17 -Wall -Wextra main.cpp -o contact-search
```

### 3. Run

Linux/macOS:

```bash
./contact-search
```

Windows:

```powershell
.\contact-search.exe
```

Run the executable from the repository directory so the relative `contacts.txt` path resolves to the tracked sample data file.

## 🕹️ Menu

| Choice | Operation |
|---:|---|
| 1 | Add a contact |
| 2 | Delete a contact |
| 3 | Export contact to VCF |
| 4 | Display contacts |
| 5 | Search contact |
| 6 | Fuzzy/partial-name search |
| 7 | Modify contact |
| 8 | Exit |

See [User Guide](docs/user-guide.md) for operation details and the data-file format.

## 🧪 Validation and testing

This repository enhancement adds documentation and repository-integrity checks only. It does not change or claim to test the application logic. A manual smoke test can be performed by compiling with the command above and running the menu using disposable contact data.

```bash
python3 scripts/repository_audit.py
python3 scripts/validate_docs.py
```

The checks validate repository documentation and supporting assets; they are not unit tests for `main.cpp`.

## ⚠️ Known limitations documented from the current source

- The application expects `contacts.txt` in its current working directory.
- The contact file is comma-separated and has no escaping mechanism for commas in fields.
- The checked-in samples are test data. Do not store real personal contact details in a public repository.
- Phone-number validation on the add path checks length only.
- Partial search is not edit-distance fuzzy matching.
- Some operations scan every bucket, so lookup is not consistently constant-time despite the hash-table data structure.
- The hash-table memory allocation and lifetime management are manual.
- The source does not provide a dedicated test suite or a documented production deployment target.
- The program writes the contact file after each menu iteration; use a copy of the sample data for experiments.

These observations are documentation findings, not code changes.

## 🗺️ Roadmap

See [ROADMAP.md](ROADMAP.md). Roadmap items are proposals and must not be read as currently implemented features.

## 🔐 Security and privacy

This application handles personal contact information. Use synthetic records for demonstrations, keep personal contact files outside public repositories, and review [SECURITY.md](SECURITY.md) before reporting vulnerabilities.

## 🤝 Contributing

Contributions to documentation, issue reports, and proposed improvements are welcome. The existing application source is being preserved as-is under this repository enhancement scope. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## 📚 Documentation

- [Documentation index](docs/README.md)
- [Product overview](docs/product-overview.md)
- [Getting started](docs/getting-started.md)
- [User guide](docs/user-guide.md)
- [Architecture](docs/architecture.md)
- [Data flow](docs/data-flow.md)
- [Data format](docs/data-format.md)
- [Project structure](docs/project-structure.md)
- [Known limitations](docs/known-limitations.md)
- [Security and privacy](docs/security.md)
- [Testing strategy](docs/testing.md)
- [Troubleshooting](docs/troubleshooting.md)
- [Changelog](CHANGELOG.md)
- [Roadmap](ROADMAP.md)

---

<div align="center">

  **Built with C++ for learning contact management and hash-table concepts.**

  [Back to top](#-contact-searching-application)

</div>
