# 📦 Build and Release

## Build

~~~bash
g++ -std=gnu++17 -Wall -Wextra -Wpedantic main.cpp -o contact-search
~~~

## Verification

Run tests/test_cli_smoke.py against the executable and run repository documentation checks.

## Release state

No semantic-version tags, release binary process, platform compatibility policy, signing process, or release automation was present in the audited repository. A release workflow should be added only after a versioning and artifact policy is adopted.
