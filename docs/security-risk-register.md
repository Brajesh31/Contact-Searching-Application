# ⚠️ Security Risk Register

| ID | Risk | Impact | Existing control | Residual state |
|---|---|---|---|---|
| SR-01 | Personal data in public tracked files | High | Guidance to use synthetic data | Manual data owner review required |
| SR-02 | Plaintext contact storage | High | Host filesystem permissions | No application encryption |
| SR-03 | Data file corrupted by interrupted rewrite | Medium/High | Manual backup guidance | No atomic write |
| SR-04 | Malformed input | Medium | Add path checks a limited subset | Load and modify paths remain weak |
| SR-05 | Export file path derived from name | Medium | No explicit application path sanitization | OS-specific path behavior remains |
| SR-06 | False export success message | Low/Medium | Verify output file | Caller does not inspect export status |
| SR-07 | Credential accidentally committed | High | Security policy and repository review | Full secret scan remains separate |

Review ratings with evidence before treating them as a formal security register.
