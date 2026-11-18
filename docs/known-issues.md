# 🐛 Known Issues and Limitations

The following source-observed issues remain:

1. contacts.txt parsing has no strict malformed-row validation.
2. Fields containing commas are not safely represented.
3. File stream open/write states are not consistently checked.
4. Whole-file persistence is not atomic.
5. Export caller may print success after exportToVCF() reports an open failure.
6. The insertion index is calculated before possible rehash and not recalculated.
7. modify() does not apply add-path phone or duplicate checks.
8. Partial search uses substring matching rather than typo correction.
9. Non-numeric menu input can leave cin in a failed state.
10. Raw dynamic allocation and single-file organization limit maintainability.

No application source has been changed as part of this repository work.
