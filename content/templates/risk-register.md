---
title: Risk register
---

# Risk register

Use this template to track a project's risks, how likely and serious each one is, who owns it and what is being done about it. Review it regularly; a register nobody reads does not reduce any risk.

## Template

```markdown
---
title: Risk Register - [Product/System/Project Name]
status: Active / Archived
date: YYYY-MM-DD
owner: [Name or Role of Risk Owner/Project Manager]
version: 1.0
---

# Risk Register: [Product/System/Project Name]

This Risk Register serves as a central repository for identified risks related to the [Product/System/Project Name]. It provides a structured way to track, assess, and manage potential issues that could impact the project's objectives, scope, schedule, budget, or quality.

---

## 1. Introduction

### 1.1 Purpose

The purpose of this Risk Register is to:
* Document all identified risks.
* Assess the likelihood and impact of each risk.
* Define clear mitigation strategies and contingency plans.
* Assign ownership for risk management activities.
* Facilitate continuous monitoring and review of risks.

### 1.2 Scope

This Risk Register covers risks associated with [briefly describe the scope, e.g., "the development and deployment of Product X," "the integration of System Y," "Project Z from inception to delivery"].

### 1.3 Definitions and Acronyms

[List any risk-specific terms, definitions, or acronyms.]

## 2. Risk Assessment Criteria

### 2.1 Likelihood Scale

| Level | Description         | Probability |
|-------|---------------------|-------------|
| 1     | Very Low / Rare     | < 10%       |
| 2     | Low / Unlikely      | 10-30%      |
| 3     | Medium / Possible   | 30-70%      |
| 4     | High / Likely       | 70-90%      |
| 5     | Very High / Almost Certain | > 90%       |

### 2.2 Impact Scale

| Level | Description | Impact on Schedule | Impact on Budget | Impact on Quality |
|-------|-------------|--------------------|------------------|-------------------|
| 1     | Very Low    | Negligible         | Negligible       | Negligible        |
| 2     | Low         | Minor delay        | Minor cost       | Minor degradation |
| 3     | Medium      | Moderate delay     | Moderate cost    | Noticeable degradation |
| 4     | High        | Significant delay  | Significant cost | Major degradation |
| 5     | Very High   | Project threatened | Project threatened | Unacceptable degradation |

### 2.3 Risk Score (Likelihood x Impact)

[Optional: Define how the risk score is calculated and what ranges mean (e.g., Low, Medium, High, Critical).]

## 3. Risk Register Log

| Risk ID | Description (Brief) | Category | Likelihood (Current) | Impact (Current) | Score (Current) | Mitigation Strategy | Contingency Plan | Owner | Status | Date Raised | Date Last Updated |
|---------|---------------------|----------|----------------------|------------------|-----------------|---------------------|------------------|-------|--------|-------------|-------------------|
| **R-001** | Delay in critical hardware component delivery. | Supply Chain | 4 (High)             | 4 (High)         | 16              | Identify alternative suppliers, pre-order long-lead items. | Use simulation/emulation for software development. | Jane Doe | Open   | YYYY-MM-DD | YYYY-MM-DD        |
| **R-002** | Unforeseen technical complexity in AI model integration. | Technical | 3 (Medium)           | 5 (Very High)    | 15              | Conduct spike/PoC, bring in external expertise. | Revert to simpler, non-AI solution. | John Smith | Open   | YYYY-MM-DD | YYYY-MM-DD        |
| **R-003** | Scope creep due to evolving stakeholder requirements. | Project | 3 (Medium)           | 3 (Medium)       | 9               | Implement strict change control process, clear scope definition. | Prioritize ruthlessly, defer non-essential features. | Alice Brown | Open   | YYYY-MM-DD | YYYY-MM-DD        |
| **R-004** | Cybersecurity vulnerability in third-party library. | Security | 2 (Low)              | 4 (High)         | 8               | Regular security audits, use trusted libraries, keep dependencies updated. | Isolate affected module, prepare emergency patch. | Bob White | Open   | YYYY-MM-DD | YYYY-MM-DD        |
| **R-005** | Key team member leaves project unexpectedly. | Resource | 2 (Low)              | 3 (Medium)       | 6               | Cross-training, comprehensive documentation. | Reallocate tasks, hire contractor. | Carol Green | Open   | YYYY-MM-DD | YYYY-MM-DD        |

## 4. Risk Categories

[Define common categories for risks to help with analysis and reporting.]

* **Technical:** (e.g., architecture, design, complexity, new technology, integration)
* **Project Management:** (e.g., schedule, budget, scope, resources, planning)
* **External:** (e.g., market changes, regulatory, supplier, economic)
* **Organisational:** (e.g., culture, stakeholder engagement, internal politics)
* **Operational:** (e.g., deployment, support, infrastructure, security)
* **Safety/Compliance:** (e.g., regulatory adherence, hazard control)

## 5. Risk Management Process

### 5.1 Identification

[How will risks be identified? (e.g., brainstorming, checklists, lessons learned, expert judgment).]

### 5.2 Analysis

[How will risks be assessed for likelihood, impact, and score?]

### 5.3 Mitigation & Response Planning

[How will strategies be developed to reduce likelihood or impact? (e.g., avoid, reduce, transfer, accept).]

### 5.4 Monitoring & Control

[How will risks be continuously tracked, reviewed, and reported? (e.g., regular risk reviews, dashboards).]

## 6. Roles and Responsibilities

* **Risk Owner:** Responsible for monitoring assigned risks, implementing mitigation strategies, and reporting status.
* **Project Manager/Lead:** Overall responsibility for the Risk Register, facilitating risk reviews, and escalating critical risks.
* **Team Members:** Responsible for identifying and reporting new risks.

## 7. Review Schedule

[How often will the Risk Register be reviewed and by whom?]

* **Frequency:** [e.g., "Weekly during team syncs," "Bi-weekly with Project Lead," "Monthly with Steering Committee."]
* **Attendees:** [e.g., "Core team," "Project Lead & Key Stakeholders."]

## 8. References

[List any other documents (e.g., project plan, requirements, ADRs) or standards referenced in this Risk Register.]
```
