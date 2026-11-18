# 🗄️ Data Architecture

## In-memory shape

- Contact contains three strings.
- HashTable contains an integer bucket count and a dynamically allocated array of vector<Contact>.
- Insertion uses name length modulo the table size as the starting index and linear probing.
- The table grows by doubling its bucket count when the pre-insert load check exceeds 0.75.

## Persistence shape

contacts.txt stores one record per line with three comma-delimited fields in this order: name, phone number, email.

There is no escape convention for commas, no schema version, no database, and no migration layer. See [data format](../data-format.md) and [data dictionary](../data-dictionary.md).
