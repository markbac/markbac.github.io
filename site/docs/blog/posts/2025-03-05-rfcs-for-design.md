---
date: 2025-03-05T09:48:00
authors:
  - markbac
categories:
  - Architecture
slug: rfcs-for-design
---

# Using RFCs to Improve Software Design and Architecture

In the fast-paced world of software engineering, making well-informed architectural decisions is critical to project success. Yet, too often, design discussions happen informally—scattered across Slack, emails, and meeting notes—leading to poor documentation, tribal knowledge, and repeated mistakes.

<!-- more -->

One effective way to bring structure and transparency to software design is by using **Request for Comments (RFCs)**. This lightweight process provides a formal yet flexible way for engineers to propose, discuss, and document changes to a system’s architecture.

In this post, I’ll break down why RFCs are useful, how they fit into a modern software development process, and how you can implement them effectively.

***

## What is an RFC?

An RFC is a structured document proposing a **technical change**, such as:

* A new feature or system component
* A major refactor or redesign
* A significant architectural decision (e.g., introducing Kafka for event-driven processing)
* Adoption of a new technology or framework

It serves as both a **proposal** and **historical record** of why a decision was made, capturing context that might otherwise be lost.

***

## Why Use RFCs?

### 1. Encourages Thoughtful Design

Writing an RFC forces engineers to **think deeply** about a proposal before jumping into code. By outlining the problem, trade-offs, and alternatives, teams can identify flaws early.

### 2. Facilitates Collaboration & Alignment

RFCs provide a **single point of discussion**. Engineers, architects, and product managers can all contribute feedback in a structured way rather than in ad-hoc conversations.

### 3. Improves Documentation & Knowledge Sharing

Over time, RFCs become a **knowledge base** of past decisions, preventing repeated discussions on already settled topics. New engineers can understand why certain choices were made without relying on oral history.

### 4. Balances Speed & Rigour

A lightweight RFC process ensures important decisions are reviewed **without introducing excessive bureaucracy**. If done well, it becomes an enabler, not a blocker.

***

## The RFC Process

### 1. Proposal (Author Drafts RFC)

An engineer or architect writes an RFC following a structured template. A typical RFC includes:

| Section            | Description                                                  |
| ------------------ | ------------------------------------------------------------ |
| **Title**          | A concise summary of the proposal                            |
| **Context**        | Background on the problem being solved                       |
| **Proposal**       | The proposed solution and technical details                  |
| **Alternatives**   | Other approaches considered and why they were rejected       |
| **Trade-offs**     | Potential downsides or risks                                 |
| **Migration Plan** | How to transition from the current state                     |
| **Impact**         | Expected impact on performance, scalability, maintainability |
| **Open Questions** | Unresolved issues requiring further discussion               |
| **Decision**       | (Added later) Final outcome and rationale                    |

***

### 2. Review & Discussion

Once drafted, the RFC is shared for feedback. This can be via:

* Pull requests (e.g., in a GitHub repo like `company/architecture-rfcs`)
* Internal wikis (e.g., Confluence, Notion)
* Emails or dedicated Slack channels

Engineers, architects, and stakeholders provide **comments, questions, and suggestions**. Constructive debate is encouraged, as this is where flaws and improvements surface.

***

### 3. Decision & Approval

After discussion, the RFC is either:

* **Accepted** (possibly with revisions)
* **Rejected** (documenting reasons for future reference)
* **Deferred** (if more information is needed)

Approved RFCs are **merged into the documentation repository**, ensuring they remain part of the organisation’s architectural history.

***

### 4. Implementation & Follow-Up

Once accepted, the RFC guides implementation. As the work progresses, the original RFC may be updated with **lessons learned** or **adjustments**.

***

## Example RFC

Let’s look at a practical example:

### Title: Move from REST to gRPC for Internal Service Communication

#### Context

Our microservices communicate over REST (JSON over HTTP). This introduces **high latency** and **verbose payloads**. We need a more efficient protocol to handle growing internal traffic.

#### Proposal

Adopt **gRPC** for inter-service communication:

* Use **Protocol Buffers** instead of JSON
* Implement bidirectional **streaming RPCs** for real-time data sync
* Deploy **Envoy** as a gRPC gateway for external clients

#### Alternatives Considered

1. **Keep REST:** Simple, but inefficient at scale.
2. **GraphQL:** More flexible but adds complexity for internal service-to-service calls.
3. **Custom WebSockets API:** Good for real-time, but lacks strong typing and tooling.

#### Trade-offs

| Factor           | REST   | gRPC                         |
| ---------------- | ------ | ---------------------------- |
| Latency          | High   | Low (binary format)          |
| Schema Evolution | Manual | Strongly typed with Protobuf |
| Streaming        | No     | Yes                          |
| Browser Support  | Native | Requires Gateway             |

#### Migration Plan

* Phase 1: Implement gRPC alongside existing REST APIs
* Phase 2: Migrate high-traffic services first
* Phase 3: Fully deprecate REST for internal calls

#### Impact

- ✅ Faster response times (\~30-50% reduction in payload size)
- ✅ Stronger type safety, reducing runtime errors
- ⚠️ Requires new client libraries & monitoring updates

#### Decision

✅ **Accepted** – Begin phased rollout in Q2

***

## Visualising RFCs

### Decision Flow for RFC Process

A simple flowchart of the RFC process:

```plaintext
[Start] --> [Draft RFC] --> [Review & Feedback] --> [Revise if needed]  
   --> [Approve?] --> (Yes) --> [Implement]  
   --> (No) --> [Document Rejection & Close]
```

***

## Best Practices for RFCs

* **Keep it lightweight** – Avoid excessive formality; focus on clarity.
* **Encourage discussion** – RFCs should invite feedback, not just approval.
* **Document rejected ideas** – Learning from past decisions is just as valuable.
* **Automate where possible** – Use templates, PR-based discussions, and tagging for tracking.

***

## Conclusion

RFCs are a simple but powerful tool for making better architectural decisions. By adopting an RFC process, teams can:

- ✅ Improve collaboration
- ✅ Reduce knowledge loss
- ✅ Make more informed, transparent decisions

If you’re not using RFCs yet, start small—documenting just a few key decisions can make a huge difference. And if you already have an RFC process, continually refine it to fit your team's needs.
