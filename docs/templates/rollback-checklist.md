# ↩️ Rollback Checklist

- [ ] Stop the application.
- [ ] Preserve the current data file and logs privately.
- [ ] Identify the last known-good backup or repository commit.
- [ ] Restore contacts.txt from backup if required.
- [ ] Verify the restored file format.
- [ ] Test in a disposable directory using synthetic data.
- [ ] Confirm that generated VCF files are handled separately.
- [ ] Record recovery outcome and any data loss.

This is a local data/repository rollback checklist, not a cloud deployment procedure.
