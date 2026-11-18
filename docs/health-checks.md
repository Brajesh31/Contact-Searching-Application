# 🩺 Health Checks

The application is a short-lived local CLI process. It does not expose a health endpoint, readiness endpoint, liveness probe, status API, or monitoring heartbeat.

Operational checks are manual: executable starts, menu appears, test data loads, and a disposable smoke test succeeds. These checks do not represent a hosted-service health model.
