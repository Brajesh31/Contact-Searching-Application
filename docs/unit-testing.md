# 🧪 Unit Testing

No isolated unit-test suite exists. Most functions are defined in main.cpp and are coupled to console input/output or global state such as contactCount.

A future unit-test harness would first need a separately authorized source-organization change. Candidate units include record parsing, duplicate detection, bucket insertion/rehash, search matching, serialization, and input validation.

Do not claim unit-test coverage from the CLI integration smoke test.
