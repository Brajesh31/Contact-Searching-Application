# 🛠️ Local Development

## Working directory

The application uses a relative path named contacts.txt. Start the executable from the directory containing the intended test data.

## Build

~~~bash
g++ -std=gnu++17 -Wall -Wextra -Wpedantic main.cpp -o contact-search
~~~

## Safe test procedure

1. Create a temporary directory.
2. Copy the compiled executable into it.
3. Create a contacts.txt containing synthetic records only.
4. Run the program there.
5. Inspect the temporary contact file and any generated VCF.
6. Remove the temporary directory after preserving only non-sensitive test output.

Do not run manual tests against valuable address-book data.
