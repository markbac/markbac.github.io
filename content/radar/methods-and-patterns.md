---
title: Methods and patterns
---

# Methods and patterns

This quadrant covers software architecture styles, engineering methodologies, regulatory security standards, and operational quality practices.

## Ring: Adopt

### C4 Architecture Model
- **Status**: **Adopt**
- **Tags**: `architecture`, `modelling`, `c4`, `diagrams`
- **Rationale**: The core architectural abstraction framework used across the company to model software, firmware, and connected systems across Context, Containers, Components, and Code/Deployment ([GD-001](../guides/c4-model/index.md)).

### Hexagonal Architecture (Ports and Adapters)
- **Status**: **Adopt**
- **Tags**: `architecture`, `patterns`, `clean-architecture`, `domain`
- **Rationale**: Primary structural pattern for core domain logic, decoupling business rules from external databases, UI frameworks, and network protocols.

### Modular Monolith
- **Status**: **Adopt**
- **Tags**: `architecture`, `patterns`, `monolith`, `modularity`
- **Rationale**: The default architectural pattern for new services, providing independent domain boundaries without the network complexity, eventual consistency challenges, and operational overhead of microservices.

### Microservices
- **Status**: **Adopt**
- **Tags**: `architecture`, `distributed`, `cloud`, `scaling`
- **Rationale**: Adopted selectively for large, mature domains where independent team delivery cadences and divergent scaling profiles warrant independent containerized services.

### Event-Driven Architecture (EDA)
- **Status**: **Adopt**
- **Tags**: `architecture`, `eda`, `pubsub`, `asynchronous`
- **Rationale**: Primary communication pattern for IoT telemetry processing and cross-microservice notifications, maximizing decoupling and system resilience.

### ETSI EN 303 645 & UK PSTI
- **Status**: **Adopt**
- **Tags**: `security`, `compliance`, `iot`, `regulation`
- **Rationale**: Mandatory regulatory security baseline for all connected consumer appliances, enforcing unique per-device passwords, vulnerability disclosure, and secure firmware updates.

### Documentation as Code
- **Status**: **Adopt**
- **Tags**: `documentation`, `git`, `markdown`, `docs-as-code`
- **Rationale**: Standard practice of authoring technical documentation in Markdown, storing it in Git, validating via linters in CI, and building static documentation sites ([GU-010](../guidelines/documentation-as-code.md)).

### Architecture Decision Records (ADRs)
- **Status**: **Adopt**
- **Tags**: `governance`, `architecture`, `adr`, `git`
- **Rationale**: Mandatory standard for capturing context, evaluated options, and trade-off consequences of major architectural choices ([GU-005](../guides/decision-records.md)).

### Agile (Scrum / Kanban)
- **Status**: **Adopt**
- **Tags**: `methodology`, `process`, `delivery`
- **Rationale**: Iterative software delivery methodologies with empirical feedback, clear quality gates (DoD per [GU-003](../templates/definition-of-done.md)), and collaborative retrospectives.

### MISRA C
- **Status**: **Adopt**
- **Tags**: `embedded`, `standards`, `safety-critical`, `c`
- **Rationale**: Mandatory coding standards subset for all safety-critical embedded C firmware ([GU-012](../standards/misra-c.md)).

## Ring: Assess

### CQRS and Event Sourcing
- **Status**: **Assess**
- **Tags**: `architecture`, `patterns`, `data`
- **Rationale**: Evaluating Command Query Responsibility Segregation and Event Sourcing for complex audit-sensitive domains where reconstructing historical state transitions is paramount.

### Definition of Ready (DoR)
- **Status**: **Assess**
- **Tags**: `methodology`, `process`, `agile`
- **Rationale**: Evaluating structured pre-sprint gates ([GU-004](../templates/definition-of-ready.md)) to prevent ill-defined user stories from entering active sprints.

### ISO/IEC 30141 (IoT Reference Architecture)
- **Status**: **Assess**
- **Tags**: `iot`, `standards`, `architecture`
- **Rationale**: Assessing the international reference architecture standard for industrial IoT implementations.

## Ring: Hold

### Waterfall Delivery Model
- **Status**: **Hold**
- **Tags**: `methodology`, `deprecated`
- **Rationale**: Rigid, linear, big-bang delivery models are deprecated across all engineering squads in favour of iterative, empirical Agile and Docs-as-Code practices.
