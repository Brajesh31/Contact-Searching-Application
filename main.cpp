#include<bits/stdc++.h>
using namespace std;
static int contactCount=0;
// Define a Class for contact information
class Contact {
    public:
        string name, phoneNumber, email;
};

// Define a Class for a Hash Table
class HashTable {
    public:
        int size;
        vector<Contact> *table;
};

// Rehash the Hash Table
void rehash(HashTable *ht) {
    cout << "Rehashing" << endl;
    int oldSize = ht->size;
    ht->size = 2 * oldSize;
    vector<Contact> *newTable = new vector<Contact>[ht->size]; // Allocate new table

    // Copy existing contacts to the new table
    for (int i = 0; i < oldSize; i++) {
        for (int j = 0; j < ht->table[i].size(); j++) {
            Contact c = ht->table[i][j];
            int index = c.name.length() % ht->size;
            while (newTable[index].size() != 0) {
                index = (index + 1) % ht->size;
            }
            newTable[index].push_back(c);
        }
    }
    // Delete old table and update ht->table
    delete[] ht->table;
    ht->table = newTable;
}

// Insert a contact into the hash table
void insertContact(HashTable *ht, Contact c) {
    int index = c.name.length() % ht->size;
    // Re Hash the Hash Table if more than 75% of the Hash Table is filled
    float loadFactor = (float)contactCount / (float)ht->size;
    if (loadFactor > 0.75) {
        rehash(ht);
    }
    //Collision Handling using Linear Probing
    while (ht->table[index].size() != 0) {
        index = (index + 1) % ht->size;
    }
    ht->table[index].push_back(c);
    contactCount++;
}

// Check if a contact with a given phone number already exists
bool contactExists(HashTable *ht,  string key,  string value) {
    if (key == "phoneNumber") {
        for (int i = 0; i < ht->size; ++i) {
            for (auto contact : ht->table[i]) {
                if (contact.phoneNumber == value) {
                    return true;
                }
            }
        }
    } else if (key == "name") {
        for (int i = 0; i < ht->size; ++i) {
            for (auto contact : ht->table[i]) {
                if (contact.name == value) {
                    return true;
                }
            }
        }
    }
    return false;
}

// Delete a contact for a given phone number
void deleteContact(HashTable *ht, string phoneNumber) {
    for (int i = 0; i < ht->size; ++i) {
        for (auto it = ht->table[i].begin(); it != ht->table[i].end(); it++) {
            if (it->phoneNumber == phoneNumber) {
                ht->table[i].erase(it);
                contactCount--;
                cout << "Contact deleted successfully" << endl;
                return;
            }
        }
    }
    cout << "Contact not found" << endl;
}


// Get a contact for a given phone number or name
Contact getContact(HashTable *ht,  string key,  string value) {
    Contact emptyContact;
    emptyContact.name = "";
    emptyContact.phoneNumber = "";
    emptyContact.email = "";

    if (key == "phoneNumber") {
        for (int i = 0; i < ht->size; ++i) {
            for (auto contact : ht->table[i]) {
                if (contact.phoneNumber == value) {
                    return contact;
                }
            }
        }
    } else if (key == "name") {
        for (int i = 0; i < ht->size; ++i) {
            for (auto contact : ht->table[i]) {
                if (contact.name == value) {
                    return contact;
                }
            }
        }
    }
    return emptyContact;
}

// Eport the Contact to a VCF file
void exportToVCF( Contact contact,  string filename) {
    ofstream outputFile(filename);
    if (!outputFile.is_open()) {
        cout << "Error opening file " << filename << endl;
        return;
    }
    // Write vCard format
    outputFile << "BEGIN:VCARD" << endl;
    outputFile << "VERSION:3.0" << endl;
    outputFile << "FN:" << contact.name << endl;
    outputFile << "TEL;TYPE=CELL:" << contact.phoneNumber << endl;
    outputFile << "EMAIL;TYPE=INTERNET:" << contact.email << endl;
    outputFile << "END:VCARD" << endl;

    outputFile.close();
}

// Display all the contacts in the Sorted Order according to the name
bool compareContactsByName(Contact a, Contact b) {
    return a.name < b.name;
}

void display(HashTable *ht) {
    vector<Contact> contacts;
    for (int i = 0; i < ht->size; i++) {
        for (int j = 0; j < ht->table[i].size(); j++) {
            contacts.push_back(ht->table[i][j]);
        }
    }
    sort(contacts.begin(), contacts.end(), compareContactsByName);
    for (auto contact : contacts) {
        cout << "Name: " << contact.name << ", Phone Number: " << contact.phoneNumber << ", Email: " << contact.email << endl;
    }
}

// Search for a Contact
void Search(HashTable *ht,  string key) {
    bool found = false;
    for (int i = 0; i < ht->size; i++) {
        for (int j = 0; j < ht->table[i].size(); j++) {
            if (ht->table[i][j].name == key || ht->table[i][j].phoneNumber == key) {
                cout << "Name: " << ht->table[i][j].name << ", Phone Number: " << ht->table[i][j].phoneNumber << ", Email: " << ht->table[i][j].email << endl;
                found = true;
            }
        }
    }
    if (!found) {
        cout << "Contact not found" << endl;
    }
}

// Fuzzy Search for a Contact using a partial match
void fuzzySearch(HashTable *ht, string key) {
    cout << "Fuzzy Searching for: " << key << endl;
    vector<Contact> foundContacts;
    for (int i = 0; i < ht->size; i++) {
        for (int j = 0; j < ht->table[i].size(); j++) {
            string contactName = ht->table[i][j].name;
            transform(contactName.begin(), contactName.end(), contactName.begin(), ::tolower); // Convert to lowercase
            transform(key.begin(), key.end(), key.begin(), ::tolower); // Convert search key to lowercase
            if (contactName.find(key) != string::npos) { // Check for partial match
                foundContacts.push_back(ht->table[i][j]);
            }
        }
    }
    if (!foundContacts.empty()) {
        cout << "Found contacts:" << endl;
        for (auto &contact : foundContacts) {
            cout << "Name: " << contact.name << ", Phone Number: " << contact.phoneNumber << ", Email: "
                 << contact.email << endl;
        }
    } else {
        cout << "No matching contacts found." << endl;
    }
}

// Modify a Contact
void modify(HashTable *ht, string key) {
    bool found = false;
    for (int i = 0; i < ht->size; i++) {
        for (int j = 0; j < ht->table[i].size(); j++) {
            if (ht->table[i][j].name == key || ht->table[i][j].phoneNumber == key) {
                cout << "Enter the new Name: ";
                getline(cin, ht->table[i][j].name);
                cout << "Enter the new Phone Number: ";
                getline(cin, ht->table[i][j].phoneNumber);
                cout << "Enter the new Email: ";
                cin>>ht->table[i][j].email;
                cout << "Contact modified successfully" << endl;
                found = true;
            }
        }
    }
    if (!found) {
        cout << "Contact not found" << endl;
    }
}

int main()
{
    // Create a Hash Table
    HashTable *ht = new HashTable();
    Contact c;
    ht->size = 10;
    ht->table = new vector<Contact>[ht->size];
    // Insert the Contacts in a File into the Hash Table
    ifstream file("contacts.txt");
    string line;
    while (getline(file, line)) {
        stringstream ss(line);
        getline(ss, c.name, ',');
        getline(ss, c.phoneNumber, ',');
        getline(ss, c.email, ',');
        insertContact(ht, c);
    }
    while(true){
        // Choice for the User
        int choice;
        cout << "1. Add a Contact" << endl;
        cout << "2. Delete a Contact" << endl;
        cout << "3. Export Contact to VCF" << endl;
        cout << "4. Display Contacts" << endl;
        cout << "5. Search Contact" << endl;
        cout << "6. Fuzzy Search Contact" << endl;
        cout << "7. Modify Contact" << endl;
        cout << "8. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;
        string phoneNumberOrName;
        switch(choice)
        {
            case 1:
                cout << "Enter the Name: ";
                cin.ignore();
                getline(cin, c.name);
                cout << "Enter the Phone Number: ";
                getline(cin, c.phoneNumber);
                // Check if the Phone Number is Valid
                if(c.phoneNumber.length()!=10)
                {
                    cout<<"Invalid Phone Number"<<endl;
                    break;
                }
                // Search if the Contact exist with same number
                if (contactExists(ht, "phoneNumber", c.phoneNumber)) {
                    cout << "Contact already exists" << endl;
                    break;
                }
                cout << "Enter the Email: ";
                cin>>c.email;
                insertContact(ht, c);
                break;
            case 2:
                cout << "Enter the Phone Number to delete: ";
                cin.ignore(); 
                getline(cin, phoneNumberOrName);
                deleteContact(ht, phoneNumberOrName);
                break;
            case 3:
                cout << "Enter the Phone Number or Name of the contact to export: ";
                cin.ignore();
                getline(cin, phoneNumberOrName);
                if (contactExists(ht, "phoneNumber", phoneNumberOrName) || contactExists(ht, "name", phoneNumberOrName)) {
                    Contact contactToExport = getContact(ht, "phoneNumber", phoneNumberOrName);
                    if (contactToExport.name.empty()) {
                        contactToExport = getContact(ht, "name", phoneNumberOrName);
                    }
                    exportToVCF(contactToExport, contactToExport.name + ".vcf");
                    cout << "Contact exported as "<<contactToExport.name + ".vcf"<< " successfully." << endl;
                } else {
                    cout << "Contact not found" << endl;
                }
                break;
            case 4:
                display(ht);
                break;
            case 5:
                cout<< "Enter the Phone Number or Name of the contact to search: ";
                cin.ignore();
                getline(cin, phoneNumberOrName);
                Search(ht, phoneNumberOrName);
                break;
            case 6:
                cout<< "Enter Name of the contact to Fuzzy search: ";
                cin.ignore();
                getline(cin, phoneNumberOrName);
                fuzzySearch(ht, phoneNumberOrName);
                break;
            case 7:
                cout<< "Enter the Phone Number or Name of the contact to Modify: ";
                cin.ignore();
                getline(cin, phoneNumberOrName);
                modify(ht, phoneNumberOrName);
                break;
            case 8:
                cout<<"Exiting"<<endl;
                return 0;
            default:
            cout<<"Invalid choice"<<endl;
                break;
        }

        // Store the Contacts in the Hash Table into a File
        ofstream outfile("contacts.txt");
        for (int i = 0; i < ht->size; i++) 
        {
            for (int j = 0; j < ht->table[i].size(); j++) {
                outfile << ht->table[i][j].name << "," << ht->table[i][j].phoneNumber << "," << ht->table[i][j].email << endl;
            }
        }

    }
    file.close();
    delete ht;
    return 0;
}

