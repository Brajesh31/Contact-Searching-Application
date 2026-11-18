# 🔐 Trust Boundaries

| Boundary | Data crossing it | Current control | Residual risk |
|---|---|---|---|
| Terminal → process | Menu choice and contact fields | Limited checks in add flow | Non-numeric input and field formats are not comprehensively handled |
| Local file → process | Comma-delimited lines | Split into three values | Malformed rows and commas in data are not robustly handled |
| Process → filesystem | Rewritten contacts.txt | ofstream | Open/write state and atomicity not checked |
| Process → export file | Name, phone, email | vCard text emitted | Name-derived filename and escaping not validated |
| Repository → public | Tracked sample data and docs | Review guidance | Existing samples require owner review for privacy before public distribution |

The application provides no authentication, authorization, encryption, or sandboxing.
