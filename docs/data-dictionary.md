# 📚 Data Dictionary

## Contact record

| Field | C++ type | Source field | Meaning |
|---|---|---|---|
| name | string | First comma-delimited value | Contact display name |
| phoneNumber | string | Second comma-delimited value | Phone identifier |
| email | string | Third comma-delimited value | Email address |

## Runtime storage

The HashTable class holds an integer bucket count and a dynamically allocated array of vector<Contact> buckets.

## File representation

The text file uses name,phoneNumber,email ordering. There is no escape convention for commas inside values.
