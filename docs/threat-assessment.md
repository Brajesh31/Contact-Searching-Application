# 🧨 Threat Assessment

This is a source-based assessment, not a penetration test.

| Scenario | Asset | Exposure | Current mitigation | Status |
|---|---|---|---|---|
| Real contacts committed | Contact data | Tracked text and VCF files are public repository content | Owner review and synthetic test data guidance | Needs manual owner review |
| Malformed text row | In-memory records | Startup parser accepts comma-separated rows without strict validation | Documented file format | Open |
| Data loss during write | contacts.txt | Whole-file rewrite, no atomic replacement | Manual backup guidance | Open |
| False export success | VCF output | Caller message does not reflect exporter file-open result | Verify file after export | Open |
| Unexpected filename | Export path | Filename derives from contact name | Operating-system file handling only | Open |
| Invalid menu input | Process state | Stream fail state is not reset | Restart process | Open |
| Repository token exposure | GitHub access | Maintainer credentials | GitHub account controls and secret scanning | Outside application controls |

No severity rating is assigned without a defined threat likelihood and impact model.
