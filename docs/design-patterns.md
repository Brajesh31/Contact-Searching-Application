# 🧱 Design Patterns and Data-Structure Techniques

The implementation uses a small set of algorithmic techniques rather than a formal application framework.

| Technique | Present? | Where | Notes |
|---|---|---|---|
| Hash-table-style bucket collection | Yes | HashTable | The initial bucket is based on name length, not a general-purpose string hash |
| Linear probing | Yes | insertContact(), rehash() | Probes next bucket while occupied |
| Rehashing | Yes | rehash() | Doubles capacity and reinserts |
| Repository pattern | No | - | Storage and application logic are combined in main() |
| MVC | No | - | No separated model/view/controller layers |
| Dependency injection | No | - | Dependencies are not injected |
| Observer/event bus | No | - | No event architecture |
| Strategy pattern | No verified use | - | Do not infer from free functions |
| RAII ownership | No | - | Bucket array is allocated manually |

This is an implementation inventory, not a recommendation to refactor under the current preservation scope.
