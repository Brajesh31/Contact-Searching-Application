# ⚠️ Project Risk Register

| ID | Risk | Likelihood | Impact | Current mitigation | Status |
|---|---|---|---|---|---|
| R-01 | Real contact details committed | Medium | High | Use synthetic examples; review staged files | Open |
| R-02 | contacts.txt overwritten unexpectedly | Medium | Medium | Back up file and test in a disposable copy | Open |
| R-03 | Malformed data row loaded | Medium | Medium | Document current format limitations | Open |
| R-04 | Partial search misunderstood as typo correction | Medium | Low | Clarify substring behavior in docs | Addressed by docs |
| R-05 | Missing automated tests | High | Medium | Manual test plan; build CI | Open |
| R-06 | Toolchain differences | Medium | Medium | Document GNU++17/GCC assumption | Open |

Qualitative ratings are initial documentation assessments, not measured risk analytics.
