# ❓ Frequently Asked Questions

## Is this a web application?

No. The inspected project is an interactive terminal program written in C++.

## Does it use MySQL or another database?

No database server is present. Data is loaded from and saved to contacts.txt.

## Does fuzzy search correct spelling mistakes?

No. The current implementation performs case-insensitive substring matching. It does not compute edit distance.

## Why should I run it from the repository root?

The program opens contacts.txt using a relative path.

## Does the application encrypt contacts?

No. The text file and exported vCard files are plaintext.

## Is there an automated application test suite?

No checked-in unit or integration suite was found in the inspected original tree. The added GitHub build workflow compiles the program only.
