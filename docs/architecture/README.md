# 🏗️ Architecture Reference

This folder contains editable Mermaid diagrams and architecture notes for the inspected single-process C++ command-line application.

## C4 and structure

- [Context diagram](context-diagram.md), [context source](system-context.mmd)
- [Container diagram](container-diagram.md), [container source](system-container.mmd)
- [Component diagram](component-diagram.md), [component source](component.mmd)
- [Class diagram](class-diagram.mmd)
- [Application layers](application-layers.md)
- [Dependency architecture](dependency-architecture.md), [graph](dependency-map.mmd)
- [Quality attributes](quality-attributes.md)
- [Architecture evaluation](architecture-evaluation.md)

## Runtime and data

- [System design](../system-design.md)
- [Application lifecycle](../application-lifecycle.md)
- [Contact lifecycle](contact-lifecycle.mmd)
- [User activity](user-activity.mmd)
- [User journey](user-journey.mmd)
- [Operation sequence](sequence.mmd)
- [State machine](state-machine.mmd)
- [Data architecture](data-architecture.md), [DFD](data-flow.mmd)
- [Search flow](search-flow.mmd)
- [Error handling](error-handling-flow.mmd)
- [Sequence catalog](sequence-catalog.md)

## Security and recovery

- [Security architecture](security-architecture.md)
- [Trust boundaries](../trust-boundaries.md)
- [Failure and recovery](failure-recovery.md)
- [Incident response](incident-response.mmd)
- [Backup and restore](backup-restore.mmd)

## Engineering process

- [Testing workflow](test-workflow.mmd)
- [Release workflow](release-workflow.mmd)
- [ADR index](decision-records.md)
- [ADR-001: local text-file persistence](decision-records/ADR-001-text-file-storage.md)

## Conditional diagrams

There is no frontend/backend separation, API, database, event bus, cache, network, container, or deployed service. These diagram types are not fabricated.
