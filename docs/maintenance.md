# 🔧 Maintenance Plan

| Activity | Trigger | Evidence |
|---|---|---|
| Review docs against source | Any source behavior change | Updated documentation and source references |
| Run docs validators | Docs/assets/workflow change | GitHub Actions result |
| Run C++ build and CLI smoke test | Source/test changes | GitHub Actions result |
| Review CodeQL | Push and scheduled scan | CodeQL workflow result |
| Review GitHub Actions dependencies | Dependabot PR | Workflow version and changelog review |
| Review privacy of tracked data | Before public distribution | Human review record |
| Review technical debt | Before an application refactor | Approved issue/ADR and tests |

No calendar-based maintenance SLA or release cadence is established.
