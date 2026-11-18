# 🌍 Deployment Environments

| Environment | Exists? | Purpose |
|---|---|---|
| Local developer machine | Yes | Compile and run the CLI |
| GitHub Actions CI | Yes | Build, smoke test, docs validation, CodeQL |
| Staging server | No | Not applicable to the current CLI |
| Production server | No | No hosted runtime |
| Container environment | No | No Dockerfile or container workflow |

No deployment configuration, secrets, or environment matrix beyond the local toolchain is required by the current application.
