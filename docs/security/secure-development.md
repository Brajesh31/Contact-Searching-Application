# 🔐 Secure Development Guidance

- Use synthetic contact values in all public tests, examples, and issue reports.
- Review the complete staged diff before every commit.
- Never commit local address books or real vCard exports.
- Keep write access limited to trusted maintainers.
- Review all GitHub Actions workflow changes and keep permissions least-privilege.
- Avoid scripts that modify the application source, dependencies, or user data.
- Record security findings with evidence and impact.
- Do not claim a vulnerability scan or audit passed until its execution result is available.

This guidance does not imply that the current application has been security-hardened or independently audited.
