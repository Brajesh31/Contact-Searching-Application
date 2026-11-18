# 🧯 Reliability and Failure Modes

| Failure mode | Current behavior / limitation | Operational response |
|---|---|---|
| contacts.txt missing or unreadable | File-open success is not explicitly validated before reading | Confirm file and working directory |
| Malformed contact row | No dedicated row validation/reporting | Restore clean sample or prepare valid rows |
| Data write interrupted | Whole-file write is not atomic | Restore from backup |
| Export file cannot open | Export routine prints an error | Check permissions and filename |
| Invalid menu input | Default branch reports invalid choice for unsupported numeric option | Re-enter a valid option |
| Unexpected input format | Limited validation | Reproduce using synthetic data and report |

There are no service availability targets, SLOs, or monitoring services for this local CLI.
