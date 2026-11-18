# 🔬 Feature-to-Test Traceability

| Feature | Relevant test plan cases | Automated status |
|---|---|---|
| Startup loading | T-01 | Covered by CLI smoke test |
| Add and phone checks | T-02, T-03, T-04 | Add-success covered; invalid/duplicate cases manual only |
| Exact search | T-05, T-06, T-08 | Exact name search covered; phone and missing cases manual only |
| Partial-name search | T-07 | Case-insensitive substring case covered |
| Delete | T-09 | Manual only |
| Display | T-10 | Manual only |
| Modify | T-11 | Manual only |
| VCF export | T-12 | Export format and generated file covered |
| Exit | T-13 | Exercised by smoke test |

The automated test is an integration smoke check with disposable data. It is not unit-test coverage and does not imply that the untested cases have passed.
