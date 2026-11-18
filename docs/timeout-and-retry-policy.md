# ⏱️ Timeout and Retry Policy

The CLI has no network requests, background jobs, retry logic, or configurable operation timeout. The automated smoke test applies a 15-second process timeout to prevent a hung CI job.

That test timeout is a CI safety bound, not an application service-level guarantee.
