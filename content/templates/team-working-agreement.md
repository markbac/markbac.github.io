---
title: Team working agreement
---

# Team working agreement

Use this template when a team forms, or changes, to agree how it works: hours, meetings, communication, reviews and how it makes decisions. The team writes it together and changes it when it stops matching what they do.

## Template

```markdown
---
title: Team Working Agreement - [Team Name]
status: Draft / Reviewed / Agreed / Evolving
date: YYYY-MM-DD
author: [Team Members' Names/Team Lead]
version: 1.0
---

# Team Working Agreement: [Team Name]

This document outlines the working agreements for the [Team Name]. It's a living document created by the team, for the team, to ensure clear communication, foster collaboration, and maintain a consistent approach to delivering value. We commit to upholding these agreements and reviewing them regularly to ensure they remain effective.

---

## 1. Introduction

### 1.1 Purpose

The purpose of this Team Working Agreement is to:
* Define our shared understanding of how we collaborate effectively.
* Establish clear criteria for when work is "ready" to be started.
* Articulate a comprehensive "Definition of Done" for our deliverables.
* Outline our expectations for user stories and other work items.
* Promote transparency, consistency, and continuous improvement within the team.

### 1.2 Scope

This agreement applies to all members of the [Team Name] and governs our daily working practices, ceremonies, and deliverable quality.

### 1.3 Review and Evolution

This is a living document. We will review this agreement [e.g., "at least quarterly," "during every retrospective"] and update it as needed to reflect our evolving practices and learnings.

## 2. Our Team Values & Principles

[Optional: Briefly state any core values or principles that guide your team's work, e.g., "Transparency," "Mutual Respect," "Continuous Learning," "Customer Focus."]

* [Value/Principle 1]
* [Value/Principle 2]

## 3. Team Collaboration & Communication

### 3.1 Synchronization & Collaboration Points

[Define the purpose, frequency, and expected participation for your team's essential synchronization and collaboration points, emphasizing flexibility over rigid ceremonies.]

* **Daily Sync / Stand-up:**
    * *Purpose:* Quick check-in to synchronize, identify immediate blockers, and align on daily priorities.
    * *Frequency:* Daily, [Time] - [Time] [Timezone] (or "as needed via chat for distributed teams").
    * *Duration:* ~15 minutes (time-boxed).
    * *Expectations:* Be concise, focus on progress, plans, and impediments.
* **Iteration Planning / Work Prioritization:**
    * *Purpose:* Align on upcoming work, clarify scope, and ensure readiness for the next iteration.
    * *Frequency:* [e.g., "Start of each iteration (e.g., bi-weekly)"]
    * *Duration:* [e.g., "Flexible, typically 1-2 hours, or broken into smaller sessions."]
    * *Expectations:* Active participation in understanding and sizing work items.
* **Review / Demo:**
    * *Purpose:* Showcase completed work to stakeholders, gather feedback, and validate value delivery.
    * *Frequency:* [e.g., "End of each iteration (e.g., bi-weekly)"]
    * *Duration:* [e.g., "Flexible, typically 30-60 minutes."]
    * *Expectations:* Prepare clear demonstrations, focus on outcomes, engage with feedback.
* **Retrospective / Continuous Improvement:**
    * *Purpose:* Reflect on our process, identify what's working well, and pinpoint areas for improvement.
    * *Frequency:* [e.g., "End of each iteration (e.g., bi-weekly)"]
    * *Duration:* [e.g., "Flexible, typically 1 hour."]
    * *Expectations:* Safe environment for honest feedback, focus on actionable improvements for our ways of working.

### 3.2 Communication Channels

[How will the team communicate for different purposes?]

* **Urgent/Blockers:** [e.g., "Dedicated Slack/Teams channel," "Direct call to relevant person."]
* **General Discussion/Questions:** [e.g., "Team Slack/Teams channel."]
* **Longer Discussions/Decisions:** [e.g., "Scheduled meeting," "Confluence/Wiki page for documentation."]
* **Documentation:** [e.g., "All significant decisions and designs documented in Markdown/Confluence."]

### 3.3 Conflict Resolution

[How will the team address disagreements or conflicts?]

* [e.g., "Address directly and respectfully with the individuals involved first."]
* [e.g., "If unresolved, escalate to the team lead/facilitator."]
* [e.g., "Use a structured discussion framework (e.g., ADRs for technical decisions)."]

## 4. Definition of Ready (DoR)

A work item (e.g., User Story, Task, Bug) is "Ready" to be pulled into a sprint/iteration when it meets the following criteria:

* **Clear Value:** The business value or problem it solves is clearly understood.
* **Well-Defined:** The scope is clear, unambiguous, and understood by the team.
* **Estimable:** The team can provide a reasonable estimate of effort.
* **Testable:** Clear acceptance criteria are defined, allowing for verification.
* **Small Enough:** It can be completed within a single sprint/iteration.
* **Dependencies Identified:** All external dependencies are known and accounted for (e.g., APIs, hardware, other teams).
* **Technical Spikes/Research Done:** Any significant technical unknowns have been explored.
* **No Obvious Blockers:** No immediate impediments prevent starting work.
* **Linked to Higher-Level Requirements:** Traceability to System-Level Requirements is established (if applicable).

## 5. Definition of Done (DoD)

A work item is "Done" when it meets *all* of the following criteria:

* **Code Complete:** All necessary code has been written.
* **Unit Tested:** All new/changed code has accompanying unit tests, and they pass.
* **Code Reviewed:** Code has been reviewed by at least one other team member and all feedback addressed.
* **Integrated:** Code has been successfully integrated into the main branch/repository.
* **Automated Tests Pass:** All relevant automated integration/system tests pass.
* **Acceptance Criteria Met:** All defined acceptance criteria for the work item have been verified (manual or automated).
* **Peer Tested / QA Approved:** (If applicable) Peer testing or formal QA sign-off has occurred.
* **Documentation Updated:**
    * Relevant design documents (e.g., SDS, C4 diagrams) updated.
    * API documentation updated.
    * User-facing documentation (if applicable) drafted/updated.
    * ADRs created for significant decisions.
* **Deployed to [Environment]:** Successfully deployed to a designated testing/staging environment.
* **Performance/Security Reviewed:** (If applicable) Basic performance and security checks passed.
* **No Known Critical Bugs:** No critical or major defects are outstanding for this feature.
* **Monitoring/Alerting Configured:** (If applicable) Necessary monitoring and alerting are in place.
* **Reviewed by Product Owner/Stakeholder:** (If applicable) Product Owner or relevant stakeholder has reviewed and accepted the work.

## 6. User Story / Work Item Requirements

When creating or refining a user story or other work item, it should ideally contain the following information:

* **Title:** Concise and descriptive.
* **Description:**
    * **As a [User Role], I want to [Action], so that [Benefit/Goal].** (for user stories)
    * Or a clear statement of the problem/task for bugs/technical tasks.
* **Acceptance Criteria:** Clear, verifiable conditions that define when the story is complete. (e.g., Gherkin format: `Given-When-Then`).
* **Dependencies:** Any internal or external dependencies.
* **Effort Estimate:** (e.g., Story Points, T-shirt size, ideal days).
* **Priority:** (e.g., MoSCoW: Must, Should, Could, Won't; or High, Medium, Low).
* **Links:** To related requirements, design documents, bugs, or other stories.
* **Assigned To:** The individual(s) responsible for the work.
* **Discussion/Comments:** Space for ongoing dialogue and clarification.

## 7. Our Definition of "Ready for Review" (Code/Design)

Before submitting code or a design for review, ensure it meets these criteria:

* [e.g., "Passes all automated tests (unit, integration)."]
* [e.g., "Adheres to coding standards/style guide."]
* [e.g., "Includes necessary comments and documentation."]
* [e.g., "No obvious compilation/build errors."]
* [e.g., "Design rationale clearly articulated (if a design review)."]

## 8. References

[List any other documents (e.g., company coding standards, architectural principles) referenced in this agreement.]
```
