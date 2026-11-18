# ⚙️ Non-Functional Requirements and Observed Constraints

No formal non-functional service targets were supplied. The table records actual constraints and unverified areas.

| Area | Observed state | Required caution |
|---|---|---|
| Platform | GNU++17-compatible compiler; bits/stdc++.h | GCC-style toolchain recommended |
| Performance | Fixed bucket array grows by doubling | No benchmark or latency target |
| Data integrity | Whole-file rewrite after each menu iteration | Writes are not atomic or transactional |
| Reliability | Basic file streams and console messages | Stream-open failures are not consistently handled |
| Security | Local plaintext storage | No encryption or authentication |
| Privacy | Names, phone numbers, emails | Keep real contact data out of public examples |
| Accessibility | Keyboard-driven text UI | No assistive-technology audit |
| Scalability | Single process and in-memory table | No multi-user or distributed scaling |
| Maintainability | Most logic in one source file | No modular library/test harness |
| Compatibility | GNU++17 configuration | Other compilers and OSes are not certified |

Do not convert these observations into numerical service-level objectives without measured evidence.
