---
title: "Appendix C: Architectural Principles for Firmitas"
---

# Appendix C: Architectural Principles for Firmitas

This appendix defines a **pragmatic, principle-led set of architectural principles** aligned to the Firmitas philosophy.
They draw inspiration from established architectural thinking (including TOGAF-style principles) but are **explicitly adapted** for modern, multi-disciplinary product development rather than enterprise IT alone.

These principles are intended to:
- Guide architectural decisions at all levels (system, solution, component)
- Act as **architectural guardrails**, not rigid rules
- Support autonomy while preserving coherence
- Optimise for long-term system health and value delivery

They should be **few, durable, and enforceable through conversation**, not bureaucracy.



## C.1 Principle Structure

Each principle is expressed using a consistent structure:

- **Statement** – The principle itself
- **Rationale** – Why this matters
- **Implications** – What this means in practice



## C.2 Foundational Architectural Principles

### AP-01: Architecture Exists to Enable Value Delivery

**Statement**  
Architecture must directly enable the delivery of customer and business value.

**Rationale**  
Architecture that optimises elegance, theoretical purity, or control at the expense of delivery speed and learning is counterproductive. Architecture is a means, not an end.

**Implications**
- Architectural work must be justified in terms of outcomes
- Architectural decisions should shorten feedback loops, not lengthen them
- “Nice to have” architectural complexity should be actively challenged



### AP-02: Optimise for Whole-System Health

**Statement**  
Architectural decisions must optimise the health of the entire system, not individual components.

**Rationale**  
Local optimisation creates systemic fragility, hidden coupling, and long-term delivery degradation.

**Implications**
- Trade-offs are evaluated across human, organisational, delivery, and technical systems
- Component efficiency may be sacrificed for system resilience
- Architectural reviews consider downstream operational impact



### AP-03: Architecture Must Assume Change

**Statement**  
All architectures must be designed with the expectation of change.

**Rationale**  
Requirements, technologies, markets, and constraints will evolve. Architectures that assume stability accumulate risk rapidly.

**Implications**
- Prefer modularity, clear interfaces, and replaceable components
- Avoid irreversible early decisions where possible
- Explicitly document assumptions and revisit them



### AP-04: Decisions Are More Important Than Diagrams

**Statement**  
The quality and clarity of architectural decisions matter more than the completeness of architectural documentation.

**Rationale**  
Unrecorded decisions decay organisational memory and force teams to re-learn context through failure.

**Implications**
- Use ADRs to capture key decisions and trade-offs
- Diagrams support understanding but do not replace decision rationale
- Architecture is judged by decision quality, not artefact volume



## C.3 Human and Organisational Alignment Principles

### AP-05: Architecture Must Reduce Cognitive Load

**Statement**  
Architecture should minimise unnecessary cognitive load on teams.

**Rationale**  
High cognitive load degrades decision quality, increases error rates, and slows learning.

**Implications**
- Prefer simple, consistent patterns
- Avoid unnecessary technology diversity
- Make ownership and responsibilities explicit



### AP-06: Conway’s Law Is a Design Constraint

**Statement**  
Architecture must acknowledge and deliberately respond to organisational communication structures.

**Rationale**  
Ignoring Conway’s Law leads to brittle architectures that conflict with how teams actually work.

**Implications**
- Team boundaries should align with architectural boundaries
- Architectural refactoring may require organisational change
- Temporary misalignment should be explicit and managed



### AP-07: Authority Must Match Responsibility

**Statement**  
Teams responsible for systems must have sufficient architectural decision authority.

**Rationale**  
Responsibility without authority creates bottlenecks, delays, and disengagement.

**Implications**
- Architectural guardrails replace centralised approval
- Escalation paths are explicit and rare
- Decisions are made as close to the work as possible



## C.4 Delivery and Evolution Principles

### AP-08: Enable Fast, Honest Feedback

**Statement**  
Architecture must support rapid feedback from real usage and failure.

**Rationale**  
Feedback is the primary mechanism for learning and improvement in complex systems.

**Implications**
- Observability is a first-class architectural concern
- Failure modes are designed, not ignored
- Testability and diagnosability influence design choices



### AP-09: Build for Incremental Validation

**Statement**  
Systems should be architected so that value and risk can be validated incrementally.

**Rationale**  
Late validation amplifies cost, risk, and rework.

**Implications**
- Support partial integration and staged releases
- Avoid designs that require “big bang” validation
- Enable prototyping and early system integration



### AP-10: Slack Is a Structural Requirement

**Statement**  
Architectures must allow slack for learning, recovery, and improvement.

**Rationale**  
Systems designed for maximum utilisation are brittle and fail catastrophically under stress.

**Implications**
- Capacity headroom is planned, not accidental
- Performance targets include resilience margins
- Teams are not architecturally forced into constant firefighting



## C.5 Governance and Risk Principles

### AP-11: Governance Through Principles, Not Permission

**Statement**  
Architectural governance should guide decisions rather than approve them.

**Rationale**  
Permission-based governance increases latency and suppresses learning.

**Implications**
- Principles are explicit and widely understood
- Exceptions are discussed, not hidden
- Governance focuses on outcomes and risks



### AP-12: Make Risk Explicit and Visible

**Statement**  
Architectural risk must be made visible and actively managed.

**Rationale**  
Hidden risk accumulates interest and surfaces late, when options are limited.

**Implications**
- High-risk decisions are addressed early
- Risk trade-offs are documented
- Technical debt is tracked as an economic concern



### AP-13: Security and Safety Are Architectural Properties

**Statement**  
Security and safety must be designed into the architecture, not added later.

**Rationale**  
Retrofitting safety or security is expensive and unreliable.

**Implications**
- Threat modelling and hazard analysis inform design
- Compliance requirements influence architectural structure
- Safety-critical paths are isolated and protected



## C.6 Technology and Platform Principles

### AP-14: Prefer Proven Before Novel

**Statement**  
Prefer proven technologies unless novelty delivers clear, justified value.

**Rationale**  
Novelty increases uncertainty, learning cost, and risk.

**Implications**
- New technology adoption requires explicit rationale
- Experiments are isolated and time-bound
- Exit strategies are defined early



### AP-15: Minimise Irreversible Decisions

**Statement**  
Architectures should delay irreversible decisions until sufficient information is available.

**Rationale**  
Early irreversible commitments amplify uncertainty and lock in poor assumptions.

**Implications**
- Use abstraction where it buys optionality
- Avoid premature standardisation
- Revisit early decisions intentionally



### AP-16: Platforms Exist to Enable Teams

**Statement**  
Platforms exist to reduce cognitive load and accelerate delivery for stream-aligned teams.

**Rationale**  
Platforms that impose friction or control undermine their own purpose.

**Implications**
- Platform teams operate as internal service providers
- Platform success is measured by team enablement
- Forced adoption without value is avoided



## C.7 Applying These Principles

These principles:
- Are **context-sensitive**, not absolute
- May occasionally conflict, requiring judgement
- Should be revisited as the organisation evolves

Their purpose is not compliance, but **better decisions, faster learning, and healthier systems**.

Architecture under Firmitas is a leadership responsibility.
These principles exist to make that responsibility explicit, shared, and actionable.
