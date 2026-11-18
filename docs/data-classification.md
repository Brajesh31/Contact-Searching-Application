# 🏷️ Data Classification

| Data | Classification guidance | Handling |
|---|---|---|
| Name | Personal data | Use synthetic examples publicly |
| Phone number | Personal data | Do not publish real numbers |
| Email | Personal data | Do not publish real addresses |
| contacts.txt | May contain personal records | Keep private if it contains real contacts |
| VCF export | Contains contact fields | Treat as sensitive plaintext |
| Build logs | May contain user-provided fields if echoed | Redact before sharing |

The existing tracked contact and VCF files have been preserved. This repository audit does not certify that their contents are anonymized.
