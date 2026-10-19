---
title: Decision log
---

# Decision log

Use this template for a running list of the decisions a project makes. Significant architecture decisions still get their own [architecture decision record](adr.md); the log points to them.

## Template

```markdown
---
title: Decision Log - [Project/System/Topic Name]
status: Active / Archived
date: YYYY-MM-DD (Date of Log Creation)
owner: [Name or Role of Decision Log Owner]
version: 1.0
related_documents:
  - [Link to relevant project plan, design doc, meeting minutes, etc.]
---

# Decision Log: [Project/System/Topic Name]

This log serves as a central record for key decisions made regarding [Project/System/Topic Name]. Its purpose is to ensure that all significant choices, their justifications, and their consequences are transparently documented for current and future reference.

---

## 1. Introduction

### 1.1 Purpose

The purpose of this Decision Log is to:
* Document all significant decisions made.
* Capture the rationale and alternatives considered for each decision.
* Record the date, deciders, and any implications of the decision.
* Provide a historical context for future architectural or project evolution.
* Facilitate impact analysis when changes are proposed.
* **Where applicable, ensure decisions are linked to relevant Architecture Decision Records (ADRs).**

### 1.2 Scope

This Decision Log covers decisions related to [briefly describe the scope, e.g., "architectural choices for Product X," "project management decisions for Project Y," "design decisions for Module Z"].

## 2. Decision Log Entries

[List each decision made. For each decision, include its rationale, alternatives considered, and any agreed-upon next steps or implications. **Architectural decisions should, where applicable, link to a corresponding Architecture Decision Record (ADR) for more detailed context and justification.**]

| Decision ID | Decision (Concise) | Rationale | Alternatives Considered | Implications | Deciders | Date Made | Related ADR (if applicable) | Status | Notes |
|-------------|--------------------|-----------|-------------------------|--------------|----------|-----------|-----------------------------|--------|-------|
| **D-001** | Adopt Microservices for new backend. | Need for scalability, independent deployment, team autonomy. | Monolith, Layered Architecture. | Increased operational complexity, initial setup cost. | Lead Architect, CTO | YYYY-MM-DD | ADR-001                     | Approved |                           |
| **D-002** | Use PostgreSQL as primary database. | Strong community, ACID compliance, good tooling. | MongoDB, MySQL. | Need for relational schema design. | Lead Architect, Tech Lead | YYYY-MM-DD | ADR-005                     | Approved |                           |
| **D-003** | Defer Feature X to Phase 2. | High effort for low immediate value; focus on core MVP. | Include in MVP with reduced scope. | Feature X not available in initial release. | Product Owner, Project Manager | YYYY-MM-DD |                             | Approved | Communicated to stakeholders. |
| **D-004** | Implement OAuth 2.0 for user authentication. | Industry standard, security best practices, future extensibility. | Custom token-based auth. | Requires third-party library integration. | Security Lead, Lead Dev | YYYY-MM-DD | ADR-010                     | Approved |                           |

## 3. Usage Guidelines

* **Decision ID:** Unique identifier for the decision (e.g., D-001).
* **Decision (Concise):** A brief, clear statement of the decision made.
* **Rationale:** Explain *why* this decision was made. What factors were considered? What problem does it solve?
* **Alternatives Considered:** Briefly list other options that were evaluated and why they were rejected.
* **Implications:** Describe the direct consequences or impact of this decision (positive and negative).
* **Deciders:** List the individuals or roles who were key in making or approving the decision.
* **Date Made:** The date the decision was finalized.
* **Related ADR (if applicable):** Link to a more detailed Architecture Decision Record if the decision is architectural.
* **Status:** (e.g., Approved, Reversed, Superseded).
* **Notes:** Any additional relevant information or context.

## 4. Maintenance

This Decision Log is a living document and should be updated whenever:
* A significant decision is made.
* A previously made decision is revisited or changed.
* New information impacts the rationale or implications of a decision.

## 5. References

[List any documents, meeting minutes, or other resources that provide further context or detail for the decisions logged here.]
```
