# Contact Searching Application 📇

## Description
This command-line application enables users to efficiently manage and search through their contacts. It offers functionalities such as adding, searching, updating, deleting contacts, as well as exporting contacts to VCF files, modifying contacts, and performing fuzzy search.

## Features

1. ✏️ **Add Contacts:** Users can add new contacts with details such as name, phone number, and email. Duplicate contacts with the same phone number are handled gracefully.

2. 🔍 **Search Contacts:** Efficient search functionality is implemented to find contacts based on name or phone number.

3. ❌ **Delete Contacts:** Users can delete contacts from their list by providing the phone number.

4. 🔄 **Update Contacts:** Contacts' information can be updated by providing the phone number or name of the contact.

5. 💾 **Export Contacts:** Contacts can be exported to VCF (vCard) files for backup or sharing purposes.

6. 📋 **Display Contacts:** Provides an option to display all contacts in the address book in alphabetical order of names.

7. 🛠️ **Modify Contacts:** Users can modify contact information including name, phone number, and email.

8. 🔍🔤 **Fuzzy Search:** Implemented fuzzy search functionality to allow users to find contacts even with minor typos or variations in the search query.

## Implementation

### Data Structures
- 🗄️ **Hash Table:** Contacts are stored in a hash table for fast retrieval. Hashing is based on the first few characters of the contact's name.

### Search Algorithms
- 🕵️‍♂️ **Hashing:** A hash function is utilized to quickly locate contacts based on their attributes.

### User Interface
- 💻 **Simple Command-Line Interface (CLI):** The application provides a CLI for users to interact with. Clear instructions and menu options guide users through various operations.

### Error Handling
- ⚠️ **Duplicate Contacts:** The system handles cases where duplicate contacts with the same phone number are attempted to be added.
- ❌ **Invalid Input:** Input validation is performed for phone numbers to ensure they have the correct format.
- 🚫 **Contact Not Found:** Error messages are displayed if a contact is not found during deletion, updating, or searching operations.

## Technologies

- 💻 **Language:** The core implementation is done in C++.
- 📚 **Libraries:** Standard C++ libraries are used for data structures and algorithms.

## Conclusion
This contact searching application provides practical experience in implementing data structures like hash tables and search algorithms for efficient contact management. The additional features such as contact exporting, modifying contacts, and fuzzy search enhance its usability and functionality, making it a comprehensive solution for contact management tasks.
