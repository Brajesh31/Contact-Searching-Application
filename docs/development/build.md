# 🧱 Build Guide

## Compiler assumptions

The checked-in VS Code configuration declares GNU++17. main.cpp includes bits/stdc++.h, which is commonly supplied by GCC-compatible toolchains.

## Build command

~~~bash
g++ -std=gnu++17 -Wall -Wextra main.cpp -o contact-search
~~~

## Run

~~~bash
./contact-search
~~~

Run from the project root so contacts.txt resolves using the current working directory.

## Build output

The executable is generated locally and should not be committed. The CI workflow compiles the same source using a temporary runner workspace. No application build configuration is changed by repository documentation automation.
