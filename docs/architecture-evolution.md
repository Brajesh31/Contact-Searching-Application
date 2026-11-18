# 🧭 Architecture Evolution

Potential future evolution, only under a separately approved application-change task:

1. Separate terminal I/O, contact operations, and persistence.
2. Replace raw bucket-array ownership with standard containers and RAII.
3. Define a robust serialization format with escaping and versioning.
4. Recompute the bucket index after a table resize.
5. Add explicit error results for load, save, and export operations.
6. Add a testable application core and comprehensive regression suite.
7. Consider a database only if a real requirement warrants its operational cost.

These are recommendations, not committed milestones.
