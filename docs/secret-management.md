# 🔑 Secret Management

The application does not read credentials, API keys, or environment variables. No secret store or rotation workflow exists in the application.

Repository guidance:

- Never add GitHub tokens, SSH private keys, cloud credentials, or passwords to tracked files.
- Store automation credentials only in GitHub-managed secrets when an authorized workflow genuinely needs them.
- Do not create an .env file for this application; no environment variables are currently consumed.
- If credentials are introduced by a future integration, document their owner, purpose, minimum permissions, rotation, and revocation process.

The file audit checks for protected source/data files, not a full credential scanner.
