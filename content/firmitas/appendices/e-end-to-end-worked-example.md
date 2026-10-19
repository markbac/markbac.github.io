---
title: "Appendix E: End-to-End Worked Example"
---

# Appendix E: End-to-End Worked Example

## A Single Product Through the Full Firmitas Lifecycle

This appendix provides a **concrete, end-to-end example** of how Firmitas is applied to a single product across its full lifecycle.

The goal is not to prescribe a “correct” implementation, but to **demonstrate how philosophy, framework, and process interact** in practice, and how artefacts remain lightweight, living, and value-focused.



## E.1 Product Context

### Product Overview

**Product:** Smart Gas Metre (NB‑IoT enabled)  
**Domain:** Regulated IoT / critical national infrastructure  
**Disciplines:** Firmware, hardware, cloud software, manufacturing, operations  
**Regulatory Context:** MID, security standards, safety requirements  
**Profile Used:** Regulated Firmitas (with a Balanced delivery core)



### Business Objectives

- Enable accurate, remote gas metering
- Support prepayment and credit modes
- Reduce operational cost via remote management
- Meet regulatory, security, and safety obligations

Value is realised **only when meters operate reliably in the field over many years**, not when features are shipped.



## E.2 Philosophy in Action

From day one, leadership explicitly sets context:

- **Purpose:** Safe, reliable metering that customers trust
- **Constraints:** Regulation, security, battery life, field longevity
- **Non‑Goals:** Rapid feature churn, experimental hardware in production
- **Slack:** Explicit buffer for learning, audits, and field feedback

This context enables teams to make local decisions without constant escalation.



## E.3 Structured Foundation Phase

### E.3.1 Vision Brief

A concise Vision Brief is created:

- Problem statement
- Customer and regulator needs
- Success criteria (accuracy, uptime, audit success)
- Explicit constraints
- Known risks

This document is reviewed once, then evolves slowly.



### E.3.2 System Requirements

System-level requirements are captured:

- Functional (metering, communications, updates)
- Non-functional (battery life, latency, reliability)
- Regulatory and safety requirements

Requirements are written to **express intent**, not implementation.



### E.3.3 High-Level Architecture

Architecture work focuses on:

- System boundaries (metre, cloud, head-end)
- Key interfaces (radio, security, manufacturing)
- Failure modes and recovery paths

C4 Context and Container diagrams are created and version-controlled.



### E.3.4 Early Architectural Decisions

Key ADRs are written for:
- Communications protocol
- Security model
- Key hardware components

Each ADR captures trade-offs and future implications.



## E.4 Iterative Development Core

### E.4.1 Breaking Down Work

System requirements are decomposed into:
- Firmware features
- Hardware revisions
- Cloud services
- Manufacturing processes

A lightweight RTM links:
- Requirement → ADR → implementation → tests



### E.4.2 Firmware & Software Iterations

Development proceeds in short cycles:

- Firmware stubs against simulated hardware
- Cloud services mocked early
- Continuous integration on every change
- Automated tests executed on-host and on-target

Feedback is constant and visible.



### E.4.3 Hardware Iteration

Hardware progresses in parallel:

- Early prototypes
- Iterative PCB revisions
- Emulators used to decouple firmware from hardware delays

Hardware lead times are treated as **explicit risks**, not surprises.



### E.4.4 Managing Risk

A living risk register tracks:
- Supply chain risks
- Security risks
- Performance uncertainties

High-risk items are addressed early through spikes and prototypes.



## E.5 Validation and Verification Arm

### E.5.1 System Integration

Software, firmware, and hardware converge:

- Full system builds
- Integration testing
- Fault injection and failure testing

Integration is incremental, not a “big bang”.



### E.5.2 Formal Verification

Formal V&V includes:
- Accuracy testing
- Environmental testing
- Security penetration testing
- Compliance verification

Evidence is generated **as part of normal delivery**, not as a separate phase.



### E.5.3 Acceptance and Release

Release readiness is assessed against:
- System requirements
- Risk posture
- Operational readiness

Sign-off is based on **confidence**, not checkbox completion.



## E.6 Operational Feedback Loop

### E.6.1 Field Deployment

Once deployed:
- Telemetry feeds back into engineering
- Operational incidents are reviewed blamelessly
- Assumptions are validated or challenged

The system continues to evolve.



### E.6.2 Incident Learning

When incidents occur:
- Root causes are systemic
- ADRs are updated if assumptions change
- Architecture evolves deliberately

Failure strengthens the system.



## E.7 Artefact Summary

| Artefact | Nature |
|--|-|
| Vision Brief | Stable, concise |
| Requirements | Living, traceable |
| ADRs | Continuous |
| Architecture Diagrams | Updated as system evolves |
| Risk Register | Actively maintained |
| Test Evidence | Generated continuously |

No artefact exists without purpose.



## E.8 Profile Transitions

During early discovery:
- Minimal Firmitas applied locally

During development:
- Balanced practices dominate

For release and compliance:
- Regulated profile governs

Profile changes are explicit and communicated.



## E.9 What This Example Demonstrates

- Firmitas scales without changing philosophy
- Regulation does not require waterfall
- Slack enables learning and resilience
- Architecture is a delivery enabler
- Leadership is exercised through system design



## E.10 Key Takeaway

Firmitas works when:
- Context is explicit
- Systems are designed intentionally
- Learning is prioritised over blame
- Governance serves delivery, not the reverse

This example is representative, not exhaustive.
Its purpose is to show **how the pieces fit together in reality**.
