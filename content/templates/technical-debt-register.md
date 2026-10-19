---
title: Technical debt register
---

# Technical debt register

Use this template to record known technical debt, what it costs, and the plan to pay it down. Debt that is written down can be weighed against features; debt that is not just accumulates.

## Template

```markdown
---
title: Technical Debt Register / Management Plan - [System/Product/Team Name]
status: Active / Archived
date: YYYY-MM-DD
owner: [Name or Role of Technical Lead/Architect/Team]
version: 1.0
---

# Technical Debt Register / Management Plan: [System/Product/Team Name]

This document serves as a central register for identified technical debt within the [System/Product/Team Name]. It provides a structured approach to understand, prioritize, and manage the remediation of technical debt, ensuring the long-term health, maintainability, and evolvability of our systems.

---

## 1. Introduction

### 1.1 Purpose

The purpose of this Technical Debt Register and Management Plan is to:
* Provide a transparent record of identified technical debt items.
* Categorize and assess the impact and urgency of each debt.
* Facilitate informed decision-making regarding technical debt remediation.
* Assign ownership and track progress of remediation efforts.
* Ensure technical debt is managed proactively rather than accumulating uncontrollably.

### 1.2 Scope

This document covers technical debt related to [briefly describe the scope, e.g., "the software components of Product X," "the firmware for Device Y," "the entire Z System"].

### 1.3 Definitions

* **Technical Debt:** Design or implementation constructs that are expedient in the short term but set up a technical context that will cost more to change later. It's a metaphor for the trade-off between short-term gains and long-term consequences.
* **Principal:** The initial cost of the expedient solution.
* **Interest:** The ongoing cost of living with the technical debt (e.g., slower development, more bugs, higher operational costs).
* **Remediation:** The process of paying down technical debt.

### 1.4 Acronyms

[List any relevant acronyms.]

## 2. Technical Debt Register Log

This log tracks individual technical debt items.

| TD ID | Title (Brief) | Description | Category | Origin/Reason | Impact (Current) | Urgency (Current) | Owner | Status | Date Identified | Last Updated | Remediation Plan | Estimated Effort |
|-------|---------------|-------------|----------|---------------|------------------|-------------------|-------|--------|-----------------|--------------|------------------|------------------|
| **TD-001** | Hardcoded API endpoint in Frontend | Frontend API URL is hardcoded, requires manual change for environments. | Code Debt | Expedient for initial deployment. | High (deployment risk, error prone) | High (frequent deployments) | Jane Doe | Open   | YYYY-MM-DD | YYYY-MM-DD   | Externalize config to env vars. | 2 days           |
| **TD-002** | Legacy Database Schema | `users` table lacks proper indexing, slow queries. | Design Debt | Historical; pre-dates current scale. | High (performance bottleneck) | Medium (intermittent user complaints) | John Smith | Open   | YYYY-MM-DD | YYYY-MM-DD   | Add B-tree indexes to `email` and `last_login` columns. | 5 days           |
| **TD-003** | Manual Firmware Update Process | Firmware updates require manual flashing via USB. | Process Debt | Initial low volume; no automation built. | Medium (time consuming, error prone) | Low (infrequent updates) | Alice Brown | Open   | YYYY-MM-DD | YYYY-MM-DD   | Research OTA update solution. | 10 days (research) |
| **TD-004** | Outdated Library: `libxyz` | `libxyz` (v1.0) has known security vulnerabilities. | Dependency Debt | Not updated during previous release. | Critical (security risk) | High (critical vulnerability) | Bob White | Open   | YYYY-MM-DD | YYYY-MM-DD   | Upgrade `libxyz` to v2.1. | 3 days           |
| **TD-005** | Lack of Unit Tests for Payment Module | Critical payment logic has no unit test coverage. | Test Debt | Tight deadline for MVP. | High (bug risk) | Medium (critical path) | Carol Green | Open   | YYYY-MM-DD | YYYY-MM-DD   | Write unit tests for `processPayment` function. | 4 days           |

## 3. Technical Debt Categories

[Define common categories for technical debt to help with analysis and reporting.]

* **Code Debt:** Issues within the code itself (e.g., duplicated code, complex logic, poor readability, lack of comments, hardcoding).
* **Design Debt:** Suboptimal architectural or system design choices (e.g., tight coupling, poor modularity, inadequate scalability).
* **Test Debt:** Insufficient or poor quality automated tests (e.g., low coverage, brittle tests, lack of integration tests).
* **Documentation Debt:** Missing, outdated, or unclear documentation (e.g., design docs, API specs, user manuals).
* **Process Debt:** Inefficient or manual development/operations processes (e.g., manual deployments, slow build times, lack of CI/CD).
* **Dependency Debt:** Outdated or insecure third-party libraries/frameworks.
* **Knowledge Debt:** Critical knowledge residing with only a few individuals, leading to single points of failure.
* **Environmental Debt:** Issues with development, testing, or production environments (e.g., inconsistent environments, outdated tools).

## 4. Technical Debt Assessment Criteria

### 4.1 Impact Scale

[Similar to Risk Impact, but focused on the consequences of *not* addressing the debt.]

| Level | Description | Impact on Development Velocity | Impact on Quality/Bugs | Impact on Operations | Impact on Business/Risk |
|-------|-------------|--------------------------------|------------------------|----------------------|-------------------------|
| 1     | Low         | Minor slowdown                 | Infrequent minor bugs  | Negligible           | Negligible              |
| 2     | Medium      | Noticeable slowdown            | Occasional bugs        | Minor operational issues | Minor business impact   |
| 3     | High        | Significant slowdown           | Frequent bugs, critical issues | Significant operational issues | Significant business risk |

### 4.2 Urgency Scale

[How quickly does this debt need to be addressed?]

| Level | Description | Action Timeframe |
|-------|-------------|------------------|
| 1     | Low         | Long-term (next quarter/year) |
| 2     | Medium      | Mid-term (next sprint/release) |
| 3     | High        | Short-term (this sprint/hotfix) |

### 4.3 Prioritization (Optional: Urgency x Impact)

[Define how the combined Urgency and Impact determine the prioritization of debt items.]

## 5. Technical Debt Management Process

### 5.1 Identification

[How is technical debt identified? (e.g., code reviews, architectural reviews, static analysis tools, bug reports, retrospectives, developer feedback).]

### 5.2 Assessment

[How are identified debt items evaluated for category, impact, and urgency?]

### 5.3 Prioritization

[How are debt items prioritized relative to new feature development and other work?]
* **Dedicated Time:** Allocate a percentage of each sprint/iteration (e.g., 10-20%) for technical debt remediation.
* **"Fix as You Go":** Encourage developers to address minor debt in areas they are already working on.
* **Strategic Sprints/Releases:** Dedicate entire sprints or releases to major refactoring or debt payoff initiatives.
* **Product Backlog Integration:** Treat technical debt items as regular backlog items, prioritized by the Product Owner in collaboration with the engineering team.

### 5.4 Remediation Planning

[How are remediation plans developed? (e.g., specific tasks, estimated effort, dependencies).]

### 5.5 Monitoring & Reporting

[How will technical debt be continuously tracked, reviewed, and reported to stakeholders? (e.g., dashboards, regular reviews).]

## 6. Roles and Responsibilities

* **Technical Debt Owner:** Responsible for driving the remediation of specific debt items.
* **Team/Lead:** Responsible for identifying debt, contributing to remediation, and updating the register.
* **Architect/Engineering Manager:** Overall responsibility for the Technical Debt Register, facilitating prioritization discussions, and advocating for debt repayment.
* **Product Owner:** Involved in prioritizing technical debt against new features, understanding its impact on delivery velocity and product quality.

## 7. Review Schedule

[How often will the Technical Debt Register be reviewed and by whom?]

* **Frequency:** [e.g., "Bi-weekly during sprint reviews," "Monthly architectural syncs," "Quarterly strategic planning."]
* **Attendees:** [e.g., "Development team," "Technical Leads & Product Owner," "Engineering Leadership."]

## 8. References

[List any other documents (e.g., Architecture Vision, ADRs, coding standards) referenced in this document.]
```
