# 🗺️ Roadmap

This roadmap separates the current implementation from possible future work. Items below are proposals, not promises or implemented functionality.

## ✅ Current repository capabilities

- [x] Terminal menu for contact operations
- [x] Add, delete, and modify contacts
- [x] Exact name and phone-number search
- [x] Case-insensitive partial-name search
- [x] Alphabetical contact display
- [x] Export a contact as vCard 3.0
- [x] Text-file persistence

## 🔭 Potential future directions

- [ ] Add automated unit and integration tests.
- [ ] Define and validate a robust contact-file format with escaping.
- [ ] Add safer import/export handling and explicit error reporting.
- [ ] Evaluate a standard container-based hash table and RAII ownership.
- [ ] Separate application operations from terminal input/output.
- [ ] Consider a true typo-tolerant search algorithm.
- [ ] Add optional data encryption or a documented secure local-storage approach.
- [ ] Add configurable data-file paths.
- [ ] Add a release and compatibility policy.

## Prioritization

Future work should first address data safety, correctness, and testability. Any implementation change requires a separate scope decision and review.
