---
title: Standards
author: Mark Bacon
---

# Standards

Technical standards for the code and the devices: how C and Python are written, how interfaces and identifiers are designed, and what a field-deployed connected device must do.

The [Guidelines](../guidelines/index.md) say how the engineering is run, and require a coding standard for each language ([EG-013](../guidelines/coding-standard.md)). These pages are those standards, and the device and interface standards that sit alongside them. The [Guides](../guides/index.md) go into depth, and the [Primers](../primers/index.md) introduce the topics.

## Coding

[[CAPTION:Table]] Coding standards.

| Standard | Covers |
| --- | --- |
| [C coding standard](c-coding-standard.md) | Layout, naming, declarations, statements and comments for C, with a focus on embedded firmware |
| [MISRA C](misra-c.md) | What MISRA C is, how to approach violations and deviations, and how it fits the workflow |
| [Python for supporting tools](python.md) | Style, type hints, docstrings, errors, structure and tooling for build scripts and other supporting tools |

## Design and interfaces

[[CAPTION:Table]] Design and interfaces standards.

| Standard | Covers |
| --- | --- |
| [Software architecture principles](software-architecture-principles.md) | Component, SOLID and package principles, and the simplicity principles behind them |
| [API design and error handling](api-design.md) | Resource design, status codes, problem details (RFC 9457), versioning and pagination |
| [Unique identifiers](unique-identifiers.md) | Choosing and storing UUIDs and their time-ordered alternatives, and the effect on database indexes |
| [Designing LwM2M objects and resources](lwm2m-objects.md) | Grouping data into objects, choosing resource types and access, and when to split an object |

## Connected devices

[[CAPTION:Table]] Connected devices standards.

| Standard | Covers |
| --- | --- |
| [IoT device architecture principles](iot-device-architecture-principles.md) | Principles for field-deployed devices in seven pillars, with device tiers and review checks |
| [Battery budgeting and power profiling](iot-battery-budgeting.md) | Energy budgets, low-power state machines, battery chemistry and current profiling |
| [Constrained binary payloads](constrained-binary-payloads.md) | When and how to use CBOR and Protocol Buffers on constrained networks |
| [Offline storage and synchronisation](iot-edge-offline-storage.md) | Flash storage, wear levelling, buffering and synchronising data when a device has been offline |
| [Serialisation, provisioning and factory test](device-serialisation-and-factory-test.md) | Device identities, key injection, hardware locking and automated factory test |
