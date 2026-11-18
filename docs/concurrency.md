# 🔀 Concurrency

The application is single-threaded and has no concurrency primitives, asynchronous workers, or multi-user synchronization.

Two processes writing the same contacts.txt concurrently could overwrite one another. The source does not implement file locks or conflict resolution. Avoid simultaneous writers to one data file.
