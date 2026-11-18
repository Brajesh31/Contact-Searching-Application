# 🧑‍💻 Use Cases

| ID | Actor | Goal | Main path |
|---|---|---|---|
| UC-01 | User | Start the application | Launch executable, load contacts file, show menu |
| UC-02 | User | Add a contact | Select 1, enter fields, pass simple phone/duplicate checks |
| UC-03 | User | Search a contact | Select 5, provide exact name or phone |
| UC-04 | User | Find a partial name | Select 6, provide substring |
| UC-05 | User | Update a contact | Select 7, identify record, enter replacement fields |
| UC-06 | User | Remove a contact | Select 2, provide phone number |
| UC-07 | User | Export a contact | Select 3, identify record, write VCF |
| UC-08 | User | Review all contacts | Select 4, display alphabetical list |
| UC-09 | User | End session | Select 8, terminate |

## Preconditions and limitations

The working directory must contain contacts.txt for startup data. The application does not authenticate users or apply role-based access. Menu input and file content should be synthetic during public demonstrations.
