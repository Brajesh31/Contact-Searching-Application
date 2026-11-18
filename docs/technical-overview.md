# 🔬 Technical Overview

## Runtime path

1. main() allocates a HashTable with 10 buckets.
2. contacts.txt is opened and read line by line.
3. Each line is split on commas into three strings.
4. Each parsed record is inserted into the in-memory table.
5. A numbered menu is printed.
6. The chosen free function performs the operation.
7. After any non-exit menu choice, an ofstream rewrites contacts.txt from all buckets.
8. Option 8 returns from main().

## Implementation inventory

- Contact: simple data record.
- HashTable: table size plus pointer to an array of vectors.
- rehash(): allocate a doubled bucket array, reinsert existing records, release old bucket array.
- insertContact(): choose bucket and linearly probe.
- Search-related functions: scan all buckets.
- display(): collect and sort.
- exportToVCF(): write vCard text.
- main(): orchestration, input, persistence.

## Limits

This document describes one source file. It does not claim separate packages or modules that do not exist.
