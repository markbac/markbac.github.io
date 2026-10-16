---
date: 2025-05-15T09:16:00
authors:
  - markbac
categories:
  - Docs as Code
slug: adr-deep-dive
---

# Deep Dive into Architecture Decision Records (ADRs)

Architecture Decision Records (ADRs) are the heartbeat of traceable system design. They’re where decisions get captured, debated, and explained — not just what was chosen, but why. Without ADRs, teams rely on Slack archaeology and hearsay to understand key technical moves.

<!-- more -->

This post is a deep dive into ADRs: what they are, what makes them effective and when to write one. It also covers how to structure them and embed them in your development flow.

---

## What is an ADR?

An Architecture Decision Record is a lightweight document that captures a **single architectural decision** and its rationale.

It documents:

- A specific technical decision
- The context in which it was made
- Alternatives considered
- Trade-offs and consequences

Each ADR should stand on its own and act as a point-in-time snapshot of engineering thought.

---

## Why ADRs Matter

- Create a **shared memory** across rotating teams
- Avoid decision churn — "Why didn’t we use X?" is answered
- Improve onboarding and audits
- Support traceability for safety-critical or regulated systems

---

## When to Write an ADR

| Trigger                             | Example                                  |
|-------------------------------------|-------------------------------------------|
| Major change in interface contract  | Switch from REST to gRPC                  |
| New library or service dependency   | Adopt Redis for pub/sub                  |
| Shift in system boundaries          | Split monolith into two services         |
| Performance trade-off decision      | Choose batching over real-time events     |
| External constraint introduction    | Data retention law changes               |
| Risk or uncertainty surfaced        | Chose to postpone multi-region rollout   |

If you’re about to debate something on Slack for 20+ minutes — write the ADR.

---

## What an ADR Should Contain

### 1. Context
Lay out the business or technical background. Include constraints, goals, and why a decision is needed.

### 2. Decision
Be concise. What did you decide to do?

### 3. Consequences
What flows from this? What are the positive and negative outcomes?

### 4. Alternatives Considered
List the viable options and why they weren’t chosen.

### 5. Related Artefacts
Link to any RFCs, designs, test plans, or interface specs.

---

## ADR Markdown Template

```markdown
---
title: "ADR-017: Use Kafka for Ingestion Buffer"
owner: "platform-team"
status: "active"
component: "data-ingestion"
last-reviewed: "2025-05-01"
---

## Context

Our ingestion pipeline currently writes directly from the API gateway to S3. We're hitting throughput limits and need a decoupling layer.

## Decision

Adopt Apache Kafka as a buffered ingestion queue.

## Consequences

- Improved burst handling
- Added complexity to deploy and monitor Kafka
- Latency will slightly increase (<200ms)

## Alternatives Considered

- SQS: simpler, but less tooling for stream processing
- Redis Streams: no native durability guarantees

## Related Artefacts

- [RFC-006: Ingestion Buffer Options](../rfc/rfc-006.md)
- [Test Plan](../tests/kafka-latency-tests.md)
```

---

## What Makes a Good ADR?

| Quality           | Description                                  |
|-------------------|----------------------------------------------|
| Specific          | Focused on one decision                      |
| Neutral           | Presents pros and cons fairly                |
| Linked            | References related artefacts and code        |
| Dated             | Includes review cycle                        |
| Owned             | Owner is accountable for re-review           |

---

## ADR Lifecycle

- **Draft**: Being discussed or reviewed
- **Proposed**: Ready for wider feedback
- **Accepted**: Adopted and active
- **Deprecated**: Superseded by another ADR
- **Rejected**: Considered but not adopted

Manage state through status tags in frontmatter and folders (`adr/deprecated/`).

---

## ADRs in the Dev Workflow

1. **Open an ADR Draft in Sprint Planning**
   - Capture proposed decisions early

2. **Review in Engineering Sync**
   - Present ADR and debate

3. **Link ADR to Jira/ADO Feature**
   - Adds traceability

4. **Reference ADR in Code**
   - Add doc comments like `// See ADR-017 for context`

5. **Review Annually or After Major Refactor**
   - Update or retire

---

## Tooling to Support ADRs

- GitHub PR templates that reference ADRs
- GitHub Actions to enforce metadata
- ADR viewers (`adr-viewer`, `adr-tools`, `MkDocs` plugins)
- Frontmatter schema checkers

---

## Tips for Scaling ADRs

- Prefix titles with ADR ID: `adr-001-title.md`
- Use tags like `#performance`, `#security`, `#integration`
- Add index pages (`index.md`) with summaries
- Link ADRs to tests and interface specs
- Group by component in subfolders (`adr/ingestion/`, `adr/auth/`)

---

## Real-World Examples

### Case: Feature Toggle System

Decision: We needed runtime flags that worked across services. ADR-019 proposed LaunchDarkly over homegrown toggles, citing rollout features and risk reduction. It was referenced in onboarding guides and used in multiple future design docs.

### Case: Rejecting gRPC

We recorded ADR-021 to explain why gRPC was rejected due to ops overhead and poor browser support — saving us from re-debating it every 3 months.

---

## ADRs vs RFCs

| ADR                         | RFC                                |
|-----------------------------|-------------------------------------|
| Single decision             | Broader proposal or initiative     |
| Record of what was chosen   | Exploration of what could be done  |
| Short (~1-2 pages)          | Longer (~3-10 pages)               |
| Anchored in system need     | Anchored in roadmap discussion     |

Use RFCs when exploring; convert to ADRs once decisions land.

---

## Final Thoughts

ADRs don’t need to be long. They need to be clear, owned, and findable.

In an age of distributed teams, long-lived systems, and evolving business needs, ADRs act as the institutional memory of your architecture. They help you move faster by avoiding indecision and reinvented wheels.

Write them early, link them often, review them periodically. The cost is small — the payoff is clarity, consistency, and confidence.

---

📘 Next in the series: [Deep Dive into RFCs: Capturing Collaborative Design in Docs-as-Code](2025-05-15-rfc-deep-dive.md)
