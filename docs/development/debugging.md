# 🐞 Debugging Guide

## Compiler diagnostics

Compile locally with warning flags:

~~~bash
g++ -std=gnu++17 -Wall -Wextra -g main.cpp -o contact-search
~~~

Warnings are evidence for review, not proof of a specific defect.

## Runtime data

- Launch from the expected working directory.
- Confirm contacts.txt exists and contains three comma-delimited fields per record.
- Use a disposable copy, because operations rewrite the data file.
- Use synthetic contact values in logs and examples.

## Search behavior

The menu's fuzzy search is a lowercased substring comparison. A non-consecutive spelling variation will not match.

## File export

VCF output is created in the current working directory, with the filename derived from the contact name. Check directory write permission and operating-system filename rules.
