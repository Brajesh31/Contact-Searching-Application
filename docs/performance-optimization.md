# ⚡ Performance Optimization

Current source characteristics:
- Several lookup and mutation functions scan every bucket.
- display() copies all contact records and sorts them.
- contacts.txt is rewritten in full after each non-exit menu operation.
- Rehash doubles the bucket array.
- No benchmark data exists.

Future optimization should be measured before changing the implementation. The hash-table insertion index should also be recalculated after rehash, but that is a correctness concern rather than a measured performance issue.
