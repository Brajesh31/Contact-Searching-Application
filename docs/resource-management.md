# 🧮 Resource Management

- Contact records are held in memory for the process lifetime.
- The bucket array is dynamically allocated with new[].
- Rehash allocates a replacement array and deletes the old array.
- display() temporarily stores a copy of every contact before sorting.
- Export and persistence use file streams.

No memory limit, maximum file size, or resource budget is defined. The main function returns directly from the exit path without explicitly releasing the HashTable allocation.
