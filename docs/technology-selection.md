# 🧰 Technology Selection and Rationale

## Observed choices

- C++ and GNU++17 for the executable.
- Standard-library strings, vectors, algorithms, and streams.
- A custom hash-table-style bucket container.
- Local text file for persistence.
- vCard 3.0 text export.

## What is not evidenced

No design proposal, technology comparison, measured selection score, framework evaluation, database evaluation, or vendor decision record was present. Do not attribute a rationale to the original author without supporting project records.

## Current recommendation

Keep the small project dependency-light. Any replacement of the persistence format, data structure, or compiler baseline should have an explicit decision record and test evidence.
