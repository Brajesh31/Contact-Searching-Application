# 📦 Capacity Planning

No supported maximum record count, memory budget, or target workload has been defined.

## Current design implications

- Bucket count starts at 10.
- Rehash doubles the number of buckets.
- Each bucket is a vector<Contact>.
- Full scans are used for several lookup and mutation operations.
- Display makes a copy of all contacts before sorting.
- File persistence rewrites every record.

## Measurement required before setting limits

A future capacity study should vary contact count and field length, record peak memory and operation duration, include malformed and worst-case data, and identify the compiler and platform. No numerical capacity claim is made here.
