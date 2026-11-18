# ⚡ Performance Notes

## Current implementation

- The table starts with 10 buckets.
- An insertion checks a load factor and can trigger a doubling rehash.
- Bucket placement starts from name length modulo table size and advances with linear probing.
- Several retrieval and mutation operations scan all buckets.
- Display collects all contacts and sorts the collection by name.

## What is not known

No benchmark suite, representative data-size profile, latency target, memory budget, or performance regression threshold was present. Do not publish numeric performance claims without measurements.

## Future measurement

Any future benchmark should record compiler, platform, contact count, data shape, number of repetitions, and measurement method.
