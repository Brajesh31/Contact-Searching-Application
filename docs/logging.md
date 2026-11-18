# 📝 Logging and Diagnostics

The application uses console output through cout. It does not implement structured logging, log levels, log files, telemetry, or a diagnostic event store.

## Output conventions currently observed

- Menu and prompts are written to standard output.
- Success and not-found messages are written to standard output.
- File-open error from exportToVCF() is also written to standard output.
- No sensitive-data redaction layer exists.

## Safety

Do not copy real contact records into public logs or bug reports. Future diagnostic improvements should report operation context and file errors without printing actual contact fields.
