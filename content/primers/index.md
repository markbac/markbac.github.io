---
title: Primers
author: Mark Bacon
---

# Primers

Short introductions to the topics that come up again and again in software, cloud and embedded engineering. Each primer explains what something is, why it matters and the main ideas, in a few minutes' reading, and then points to where to go deeper. They used to be called the Tech 101s.

The primers are introductions, not rules. The [Guidelines](../guidelines/index.md) and [Standards](../standards/index.md) sections say how things are done here; the [Guides](../guides/index.md) and the [Handbook](../handbook/index.md) go into depth; the [Glossary](../glossary/index.md) defines the terms.

## The areas

| Area | Covers |
| --- | --- |
| [Architecture](architecture.md) | Decision records, C4, design principles and patterns, anti-patterns, hexagonal architecture, domain-driven design, event-driven architecture, monoliths and microservices, device shadows |
| [Distributed systems](distributed-systems.md) | CAP and PACELC, consistency models and CRDTs, idempotency, sagas |
| [APIs and data](apis-and-data.md) | REST, OpenAPI and AsyncAPI, JSON, YAML, Protocol Buffers, CBOR |
| [Cloud](cloud.md) | CI/CD, infrastructure as code, serverless, Kafka, IoT on Google Cloud |
| [IoT and embedded](iot-and-embedded.md) | Embedded design, RTOS, state machines, interrupts and DMA, watchdogs, bootloaders, MQTT, CoAP, LwM2M, cellular LPWAN, firmware updates, edge computing, hardware-in-the-loop testing |
| [Security](security.md) | Cryptography, PKI, TLS and DTLS, post-quantum cryptography, secure coding, OWASP Top 10, OAuth and OpenID Connect, zero trust, ETSI EN 303 645, ISO/IEC 30141 |
| [Methods and delivery](methods-and-delivery.md) | Life cycle models, agile, Scrum and Kanban, event storming, architecture evaluations, testing, code review, technical debt, docs as code, root cause analysis |
| [Programming and tools](programming-and-tools.md) | Git, static analysis, PlantUML and Mermaid, Python, Rust, the terminal |

[[CAPTION:Table]] The primer areas.

## Suggested reading paths

If you are new to an area, these orders build on each other.

**Embedded and IoT firmware**

1. [Embedded systems design](embedded-systems-design.md)
2. [Real-time operating systems and FreeRTOS](rtos-and-freertos.md)
3. [Finite state machines](finite-state-machines.md)
4. [Interrupts and DMA](interrupts-and-dma.md)
5. [Cellular LPWAN](cellular-lpwan.md), then [CoAP](coap.md) or [MQTT](mqtt.md)
6. [CBOR and compact binary formats](cbor.md)
7. [Bootloaders](bootloaders.md) and [firmware over the air](firmware-over-the-air.md)
8. [ETSI EN 303 645](etsi-en-303-645.md)
9. [Hardware-in-the-loop testing](hardware-in-the-loop-testing.md)

**Cloud and distributed systems**

1. [Cloud primers](cloud.md) for the service models
2. [Domain-driven design](domain-driven-design.md)
3. [Modular monolith or microservices](modular-monolith-vs-microservices.md)
4. [Event-driven architecture](event-driven-architecture.md) and [Kafka](kafka-event-streaming.md)
5. [CAP and PACELC](cap-and-pacelc.md), [idempotency](idempotency.md) and [sagas](saga-pattern.md)
6. [Infrastructure as code](infrastructure-as-code.md) and [CI/CD pipelines](cicd-pipelines.md)

**Security**

1. [Cryptography basics](cryptography-basics.md)
2. [PKI and certificates](pki-and-certificates.md) and [TLS and DTLS](tls-and-dtls.md)
3. [Secure coding practices](secure-coding-practices.md) and the [OWASP Top 10](owasp-top-10.md)
4. [OAuth 2.0 and OpenID Connect](oauth-and-oidc.md)
5. [Zero trust architecture](zero-trust-architecture.md)

**Technical leadership**

1. [Agile development](agile-development.md) and [Scrum and Kanban](scrum-vs-kanban.md)
2. [Architecture decision records](architecture-decision-records.md) and [the C4 model](c4-model.md)
3. [Lightweight architecture evaluations](lightweight-architecture-evaluations.md)
4. [Technical debt](technical-debt.md) and [code review](code-review.md)
5. [Root cause analysis](root-cause-analysis.md)
6. [Docs as code](docs-as-code.md)
