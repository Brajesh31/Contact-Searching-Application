# 🚨 Incident Response

## Example incident classes

- Accidental publication of real contact data.
- Loss or corruption of contacts.txt.
- Unexpected modification or exposure of exported VCF files.
- Suspected compromise of repository write access.

## Response procedure

1. Stop using the affected working copy if it may continue overwriting data.
2. Preserve relevant evidence without republishing personal data.
3. Restrict exposure, such as removing public access to a leaked artifact and rotating affected credentials where credentials are involved.
4. Assess which files and data were affected.
5. Restore contact information from a known backup if available.
6. Report security-sensitive events privately to the maintainer.
7. Record corrective actions without including actual contact details.

## Limitations

The application has no built-in incident telemetry, backup service, or automated recovery system. This runbook is procedural guidance, not an implemented incident-management platform.
