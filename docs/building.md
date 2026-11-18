# 🧱 Building

The checked-in source uses bits/stdc++.h and is configured for GNU++17.

~~~bash
g++ -std=gnu++17 -Wall -Wextra -Wpedantic main.cpp -o contact-search
~~~

For a CodeQL extraction build, the workflow compiles the translation unit with GNU++17 and emits an object file. No CMake, Makefile, package manager, or custom generated build system is present.

Warnings about signed/unsigned comparisons are visible in the current source. They are reported for future code maintenance and are not silently changed here.
