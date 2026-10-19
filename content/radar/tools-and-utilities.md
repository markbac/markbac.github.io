---
title: Tools and Utilities
---

# Tools and Utilities

This quadrant covers development environments, diagram engines, static analysis linters, compilers, and local database engines.

## Ring: Adopt

### PlantUML
- **Status**: **Adopt**
- **Tags**: `diagrams`, `tools`, `uml`, `c4`
- **Rationale**: The standard text-based diagram generator for complex UML sequence diagrams, component diagrams, and C4 architectural models. Integrated into automated DOCX/PDF document compilation via `createdocs.py`.

### Mermaid
- **Status**: **Adopt**
- **Tags**: `diagrams`, `tools`, `markdown`, `docs-as-code`
- **Rationale**: Preferred tool for lightweight, client-side rendered flowcharts, state transitions, and sequence diagrams directly inside Markdown documentation pages.

### OpenAPI Specification (v3.1)
- **Status**: **Adopt**
- **Tags**: `api`, `tools`, `rest`, `specification`
- **Rationale**: Standard machine-readable contract format for describing RESTful HTTP APIs. Powers automated documentation generation, client SDK synthesis, and mock testing.

### SQLite
- **Status**: **Adopt**
- **Tags**: `database`, `embedded`, `sql`, `edge`
- **Rationale**: Zero-configuration, serverless, self-contained SQL database engine adopted for edge gateway local telemetry caching, desktop testing tools, and embedded data logging.

### GCC & Clang
- **Status**: **Adopt**
- **Tags**: `compilers`, `c`, `c++`, `toolchains`
- **Rationale**: Standard cross-compilers for ARM Cortex-M and embedded Linux target compilation. Enforcing strict `-Wall -Wextra -Werror` compiler hygiene in CI.

### Visual Studio Code
- **Status**: **Adopt**
- **Tags**: `ide`, `editor`, `developer-experience`
- **Rationale**: Primary cross-platform integrated development environment with extensions for C/C++, Python, Rust, Docker, PlantUML, and Markdownlint.

## Ring: Assess

### Coverity
- **Status**: **Assess**
- **Tags**: `sast`, `security`, `static-analysis`, `quality`
- **Rationale**: Evaluating enterprise-grade deep static analysis for automated detection of concurrency race conditions, memory leaks, and buffer overflows in C/C++ firmware.

### Structurizr DSL
- **Status**: **Assess**
- **Tags**: `architecture`, `c4`, `modelling`, `dsl`
- **Rationale**: Evaluating Structurizr DSL as a single-source-of-truth textual modelling tool capable of generating synchronized C4 diagrams across all abstraction levels ([GD-001](../guides/c4-model/index.md)).
