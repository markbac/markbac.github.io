---
title: "Appendix B: Firmitas Templates"
---

# Appendix B: Firmitas Templates

This appendix provides a **canonical set of lightweight, pragmatic templates** used throughout Firmitas.  
They are intentionally minimal, text-first, and compatible with a Docs-as-Code approach.

These templates are **not mandatory artefacts**.  
They exist to reduce cognitive load, improve consistency, and preserve decision context where it matters.

Teams should tailor them, but **not dilute their intent**.



## B.1 Vision Brief Template

**Purpose:**  
Establish shared understanding of *why* the product exists and *what problem it serves*.

```markdown
# Vision Brief – <Product / Initiative Name>

## Purpose
Why does this product exist?
What customer problem or opportunity does it address?

## Target Users / Customers
Who is this for?
What context do they operate in?

## Value Proposition
What meaningful value does this deliver to the customer?
Why is this valuable to the business?

## Success Criteria (Outcomes)
How will we know this is successful?
Focus on outcomes, not outputs.

## Constraints
Known constraints (regulatory, technical, commercial, time).

## Strategic Risks
Key risks that could invalidate the vision.

## Non-Goals
Explicitly state what this product is *not* trying to do.
```



## B.2 Architecture Decision Record (ADR) Template

**Purpose:**  
Capture **why** a significant decision was made, not just what was chosen.

```markdown
# ADR-<ID>: <Decision Title>

## Status
Proposed | Accepted | Superseded | Deprecated

## Context
What problem are we solving?
What forces, constraints, or trade-offs exist?

## Decision
What decision has been made?

## Rationale
Why this option over alternatives?
What trade-offs were accepted?

## Consequences
Positive and negative consequences.
What does this enable or constrain?

## Alternatives Considered
Briefly list rejected options and why.

## Follow-Ups
Actions, reviews, or revisit conditions.
```



## B.3 Request for Comment (RFC) / Design Proposal Template

**Purpose:**  
Enable **collaborative design thinking** before commitment.

```markdown
# RFC: <Title>

## Problem Statement
What problem are we trying to solve?
Why now?

## Proposed Approach
High-level description of the proposal.

## Impacted Systems
What systems, teams, or interfaces are affected?

## Trade-Offs
What do we gain?
What do we give up?

## Risks & Unknowns
Key uncertainties or assumptions.

## Open Questions
What feedback or decisions are needed?

## Decision Owner
Who will decide and by when?
```



## B.4 Requirements Template (System / Product Level)

**Purpose:**  
Define intent clearly without over-specification.

```markdown
# Requirements – <System / Product Name>

## Scope
What is in scope?
What is explicitly out of scope?

## Functional Requirements
- FR-001: <Statement>
- FR-002: <Statement>

## Non-Functional Requirements
Performance, reliability, security, safety, usability, etc.

## Regulatory / Compliance Requirements
Standards, certifications, legal obligations.

## Assumptions
Key assumptions that influence design.

## Acceptance Criteria
How will these requirements be verified?
```



## B.5 Requirements Traceability Matrix (RTM) – Lightweight Form

```markdown
| Requirement ID | Design Ref | Implementation Ref | Test Ref | Status |
|-||--|-|--|
| FR-001         | ADR-004    | Repo:module-x      | TC-012   | Done   |
```



## B.6 Risk Register Template

```markdown
# Risk Register – <Product / Programme>

| Risk ID | Description | Likelihood | Impact | Mitigation | Owner | Status |
|--|-||--||-|--|
| R-001  | Component lead time | High | High | Alternate supplier | Ops | Open |
```



## B.7 Incident Review / Postmortem Template

```markdown
# Incident Review – <ID / Date>

## Summary
What happened?

## Impact
Who was affected and how?

## Timeline
Key events in chronological order.

## Root Causes (Systemic)
What system conditions enabled this?

## What Went Well
What helped contain or resolve the issue?

## What Didn’t Go Well
Where did the system fail?

## Actions
Concrete improvements to prevent recurrence.

## Learning Captured
What should we remember next time?
```



## B.8 C4 Architecture Diagram Index Template

```markdown
# Architecture Overview – <System Name>

## Context Diagram
Link or embed diagram.

## Container Diagrams
- Container A – Purpose
- Container B – Purpose

## Component Diagrams
Links to detailed views.

## Key Architectural Principles
Non-negotiable design principles.

## Known Constraints
Technical or organisational constraints.
```



## B.9 Delivery Health Check Template

```markdown
# Delivery Health Check – <Team / Product>

## Flow
Is work flowing predictably?

## Feedback
How fast do we learn from customers and failures?

## Quality
Are defects escaping into production?

## Sustainability
Is pace sustainable?
Is slack present?

## Risks
What keeps us awake at night?

## Actions
What system adjustments are needed?
```



## B.10 Adoption & Tailoring Checklist

```markdown
# Firmitas Adoption Checklist

- Philosophy understood and agreed
- Leadership responsibilities explicit
- Guardrails defined
- Core artefacts selected
- Slack explicitly protected
- Feedback loops established
- Risk visibility in place
- Governance lightweight and intentional
```



## B.11 Template Usage Guidance

- Templates are **starting points**, not contracts.
- Prefer clarity over completeness.
- Text-first beats tools-first.
- Review templates periodically and retire those that no longer add value.
- Treat templates as **system components**, subject to evolution.
