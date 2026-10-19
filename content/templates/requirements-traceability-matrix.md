---
title: Requirements traceability matrix
---

# Requirements traceability matrix

Use this template to trace each requirement to its design, its implementation and the tests that verify it. Generate it from your tools where you can; a matrix kept by hand goes out of date quickly.

## Template

```markdown
---
title: Requirements Traceability Matrix (RTM) - [Product/System/Component Name]
status: Draft / In Progress / Finalised
date: YYYY-MM-DD
owner: [Name or Role of QA Lead/Architect]
version: 1.0
---

# Requirements Traceability Matrix (RTM): [Product/System/Component Name]

This Requirements Traceability Matrix (RTM) provides a mapping between different levels of requirements, design elements, and test cases for the [Product/System/Component Name]. It ensures that every requirement is addressed in the design, implemented in the code, and verified through testing.

---

## 1. Introduction

### 1.1 Purpose

The purpose of this RTM is to establish and maintain traceability throughout the development lifecycle of the [Product/System/Component Name]. It helps to:
* Ensure all requirements are covered by design and testing.
* Facilitate impact analysis for changes to requirements.
* Provide evidence for compliance and quality assurance.

### 1.2 Scope

This RTM covers the traceability from [e.g., "System-Level Requirements"] to [e.g., "Detailed Requirements, Design Elements, and Test Cases"].

## 2. Traceability Matrix

This matrix links requirements to their corresponding design components, source code, and test cases.

| Requirement ID | Requirement Description (Brief) | Parent Requirement ID (if applicable) | Detailed Requirement ID(s) | Design Element ID(s) / ADR(s) | Source Code File(s) / Module(s) | Test Case ID(s) | Test Status (Latest) | Notes |
|----------------|---------------------------------|---------------------------------------|----------------------------|-------------------------------|-----------------------------------|-----------------|----------------------|-------|
| **SYS-FUN-001**| The system shall allow user login. | N/A                                   | COMP-FUN-001               | ADR-005 (Auth Mechanism)      | `auth_service.py`                 | TC-LOGIN-001    | Passed               |       |
| **SYS-FUN-002**| The system shall display product catalog. | N/A                                   | COMP-FUN-002               |                               | `catalog_module.c`                | TC-CAT-001      | Passed               |       |
| **SYS-NFR-PERF-001**| Login response time < 500ms. | N/A                                   | COMP-NFR-PERF-001          |                               | `auth_service.py`                 | TC-LOGIN-PERF-001| Passed               |       |
| **SYS-SAFE-001**| System shall prevent over-temperature. | N/A                                   | FIRM-SAFE-001, HW-SAFE-001 | ADR-010 (Thermal Mgmt)        | `temp_sensor.c`, `hw_monitor.vhd` | TC-TEMP-001     | Passed               |       |
| **COMP-FUN-001**| The authentication module shall validate credentials. | SYS-FUN-001                           | N/A                        |                               | `auth_module.c`                   | TC-AUTH-001     | Passed               |       |
| **FIRM-SAFE-001**| Firmware shall read temp sensor. | SYS-SAFE-001                          | N/A                        |                               | `firmware/sensors.c`              | TC-FIRM-TEMP-001| Passed               |       |
| **HW-SAFE-001**| Hardware shall include thermal cutoff. | SYS-SAFE-001                          | N/A                        |                               | `hardware/schematic.pdf`          | TC-HW-TEMP-001  | Passed               | Needs HW Rev 2|

## 3. Usage Guidelines

* **Requirement ID:** Unique identifier for the requirement (e.g., from System-Level Requirements or Detailed Requirements document).
* **Requirement Description (Brief):** A short summary of the requirement.
* **Parent Requirement ID:** Links to the higher-level requirement from which this one is derived.
* **Detailed Requirement ID(s):** Links to more granular requirements (if this is a high-level RTM).
* **Design Element ID(s) / ADR(s):** Links to specific design documents, components, or Architecture Decision Records that address this requirement.
* **Source Code File(s) / Module(s):** References the specific code files or modules where the requirement is implemented.
* **Test Case ID(s):** Links to the test cases designed to verify this requirement.
* **Test Status (Latest):** The current status of the associated test cases (e.g., Passed, Failed, Not Run, Blocked).
* **Notes:** Any additional relevant information or context.

## 4. Maintenance

This RTM is a living document and should be updated whenever:
* Requirements are added, modified, or removed.
* Design decisions are made or changed.
* Code is implemented or refactored.
* Test cases are created, updated, or executed.

## 5. References

* [Link to System-Level Requirements Document]
* [Link to Detailed Requirements Document(s)]
* [Link to Test Plan Document(s)]
* [Link to Architecture Decision Records (ADRs) folder]
```
