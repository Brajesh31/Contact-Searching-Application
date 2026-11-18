# 📇 Product Overview

## Purpose

Contact Searching Application is a local command-line address book implemented in C++. It provides a small set of contact-management operations and demonstrates a custom hash-table-based storage structure.

## Contact record

Each in-memory `Contact` has three string fields: `name`, `phoneNumber`, and `email`.

## User capabilities

The menu supports adding, deleting, exporting, listing, exact searching, partial-name searching, modifying, and exiting.

## Runtime model

At startup, the application reads `contacts.txt`. It keeps records in an in-memory bucket array during the session and serializes the full collection back to the same file after each menu iteration.

## Intended environment

The project is a terminal program. The checked-in VS Code configuration declares GNU++17 and a Windows MinGW compiler path. The source includes `<bits/stdc++.h>`, making a GCC-compatible compiler the expected toolchain.

## Out of scope in the current implementation

There is no browser UI, network service, authentication system, multi-user synchronization, database server, or cloud deployment configuration in the inspected source.
