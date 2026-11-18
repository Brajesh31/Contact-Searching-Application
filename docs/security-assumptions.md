# 🧭 Security Assumptions

- The application is run by a local operating-system user.
- The working directory is writable when contacts are modified.
- The user is responsible for protecting local contact data.
- Repository sample data must be reviewed before public reuse.
- No network attacker, multi-user access, or remote service exists in the current application boundary.
- Operating-system file permissions are outside the C++ program's control.

These assumptions may be invalid in a future hosted, multi-user, or network-enabled version and would then require a new threat model.
