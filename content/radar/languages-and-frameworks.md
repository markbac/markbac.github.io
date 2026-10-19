---
title: Languages and frameworks
---

# Languages and frameworks

This quadrant covers core programming languages, schema definition languages, and data serialisation formats used across our embedded firmware, edge gateways, and cloud platforms.

## Ring: Adopt

### C
- **Status**: **Adopt**
- **Tags**: `embedded`, `firmware`, `real-time`, `c99`, `misra`
- **Rationale**: C remains the unmatched industry standard for resource-constrained microcontroller development and RTOS kernel programming. With deterministic memory layout and zero runtime overhead, all bare-metal drivers and low-level task code are authored in C99/C11 conforming to [C Coding Standards](../standards/c-coding-standard.md) and [MISRA C Guidelines](../standards/misra-c.md).

### C++
- **Status**: **Adopt**
- **Tags**: `systems`, `embedded`, `c++17`, `gateways`
- **Rationale**: Used primarily on mid-tier gateways, edge computing appliances, and complex protocol decoders where object-oriented abstractions, RAII resource management, and templates provide strong type safety without sacrificing performance. Restricted to a safety-conscious subset (avoiding exceptions and heavy RTTI).

### C# (.NET)
- **Status**: **Adopt**
- **Tags**: `backend`, `cloud`, `enterprise`, `testing`
- **Rationale**: High-productivity language for enterprise services, desktop manufacturing test benches, and high-throughput cloud back-ends running on modern .NET 8+.

### Rust
- **Status**: **Adopt**
- **Tags**: `systems`, `memory-safety`, `embedded`, `cloud`
- **Rationale**: Adopted for new performance-critical cloud microservices and selected edge components requiring uncompromising memory safety without garbage collection. Its ownership model guarantees thread safety at compile time, eliminating entire classes of concurrency defects.

### Python
- **Status**: **Adopt**
- **Tags**: `scripting`, `automation`, `testing`, `data-science`
- **Rationale**: The standard language for continuous integration automation, automated hardware-in-the-loop (HIL) test suites, cloud data engineering pipelines, and rapid prototyping. Conforms to [Python Coding Standards](../standards/python.md) and PEP 8.

### Go (golang)
- **Status**: **Adopt**
- **Tags**: `cloud`, `microservices`, `concurrency`, `cli`
- **Rationale**: The preferred language for high-throughput network daemons, API gateways, and distributed cloud microservices. Its lightweight goroutines and compiled single-binary deployments provide exceptional operational simplicity.

### Protocol Buffers (Protobuf)
- **Status**: **Adopt**
- **Tags**: `serialization`, `binary`, `grpc`, `iot`
- **Rationale**: Strongly-typed, compact binary serialization format powering all internal microservice gRPC communications and constrained IoT telemetry streams. Reduces payload sizes by 60-75% compared to JSON.

### JSON
- **Status**: **Adopt**
- **Tags**: `serialization`, `web`, `rest`, `text`
- **Rationale**: The standard data interchange format for public RESTful HTTP APIs and web dashboards. Paired with RFC 9457 for structured error reporting ([GU-020](../standards/api-design.md)).

### YAML
- **Status**: **Adopt**
- **Tags**: `configuration`, `iac`, `docs-as-code`
- **Rationale**: Standard human-readable configuration language for Kubernetes manifests, GitHub Actions pipelines, and Docs-as-Code publication manifests.

### GraphQL
- **Status**: **Adopt**
- **Tags**: `api`, `frontend`, `query-language`
- **Rationale**: Adopted for customer-facing web and mobile dashboards where front-end applications require flexible, aggregated data fetching from multiple underlying microservices in a single round-trip.

## Ring: Assess

### CERT C
- **Status**: **Assess**
- **Tags**: `security`, `coding-standards`, `embedded`
- **Rationale**: Evaluating SEI CERT C coding rules to complement existing MISRA C compliance, specifically focusing on mitigating cyber-security attack surfaces and integer arithmetic vulnerabilities in connected IoT devices.

### MISRA C++
- **Status**: **Assess**
- **Tags**: `safety-critical`, `embedded`, `c++`
- **Rationale**: Evaluating MISRA C++:2023 guidelines for application in next-generation edge gateway runtimes where modern C++ features are adopted under strict safety requirements.
