# 🖥️ Platform and Toolchain Compatibility

## Verified repository configuration

The existing VS Code configuration specifies GNU++17 and a machine-specific Windows MinGW compiler path. The source includes bits/stdc++.h, a GCC-family convenience header rather than an ISO C++ header.

## Recommended build environment

A GCC-compatible compiler with GNU++17 support is the most direct choice:

~~~bash
g++ -std=gnu++17 -Wall -Wextra -Wpedantic main.cpp -o contact-search
~~~

## Compatibility status

| Environment | Status |
|---|---|
| Linux with GCC | CI compile path |
| Windows MinGW | Existing editor configuration; separate runtime validation not recorded |
| macOS Clang | Not independently validated |
| MSVC | Not supported by the bits/stdc++.h include as written |
| Other terminals | No formal terminal compatibility matrix |

A successful Ubuntu CI build does not certify every operating system.
