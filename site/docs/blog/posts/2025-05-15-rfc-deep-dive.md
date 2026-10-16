---
date: 2025-05-15T09:17:00
authors:
  - markbac
categories:
  - Docs as Code
slug: rfc-deep-dive
---

# Deep Dive into RFCs: Capturing Collaborative Design in Docs-as-Code

RFCs — Request for Comments — are one of the most powerful tools for teams trying to make better architecture and design decisions without descending into endless meetings or tribal knowledge.

<!-- more -->

Used properly, RFCs create space for exploration, debate, feedback, and consensus across engineering. They help us decide what to build, how to build it, and most importantly — **why** we're going that way, while documenting the alternative paths we left behind.

In this deep dive, we’ll explore:

- What an RFC is and why it’s different from an ADR
- When to write one
- The anatomy of a good RFC
- Review and signoff processes that work
- Tips to integrate RFCs into your daily flow

---

## What is an RFC?

A Request for Comments is a **collaborative design artefact** that outlines a proposal for a significant technical or architectural change. It’s not a decision (yet) — it’s an open invitation to shape one.

It’s used to:

- Share context and intent
- Propose architectural options
- Invite feedback
- Document discussion history
- Guide implementation and future reference

---

## When to Use an RFC

| Trigger | Example |
|--------|---------|
| New architectural direction | Replace monolith with microservices |
| Significant refactor | Split telemetry handler from app logic |
| Cross-team dependencies | Propose shared config service |
| Ambiguity or conflict | Should we use Kafka or Redis Streams? |
| Evaluation of 3rd-party tooling | SSO with Keycloak vs Auth0 |

If the outcome has long-lasting impact, or multiple stakeholders are involved — write an RFC.

---

## Structure of a Good RFC

```markdown
---
title: "RFC-005: Redesign API Authentication"
status: "draft"
author: "team-api"
component: "auth-gateway"
created: "2025-05-01"
---

## Summary

Short and clear explanation of the problem and proposed change.

## Motivation

Why this matters. What problems are we solving?

## Detailed Proposal

- Architecture sketch
- Sequence diagrams
- Service impact
- Data model changes

## Alternatives Considered

What else did we explore and why were they rejected?

## Impact Analysis

What will change? Who needs to know? What risks exist?

## Open Questions

Things still under debate or to be validated.

## Timeline and Rollout

Rough implementation and adoption plan.

## Feedback History

Thread summaries or issue discussions linked here.
```

---

## Lifecycle of an RFC

1. **Draft**: Initial writeup with team or squad
2. **Discussion**: Shared with broader teams
3. **Updates**: Revisions made as feedback lands
4. **Approved**: Accepted and moved into roadmap
5. **Abandoned / Rejected**: Closed with explanation
6. **Archived**: Linked from ADR or historical reference

Keep this flow lightweight but visible.

---

## From RFC to ADR

Once a decision has been made, convert the RFC’s selected option into a formal ADR.

Link between them:

- From RFC: “See ADR-014 for the adopted design”
- From ADR: “Result of RFC-005”

This preserves **exploration history** without muddying the final record.

---

## Running Good RFC Reviews

### 1. Open in PR, not email

Use GitHub or Azure DevOps Pull Requests to review and comment

### 2. Use tagging

Assign reviewers by area or team

### 3. Set a deadline

Say: “Feedback closes Friday EOD”

### 4. Accept dissent

Summarise objections and why a direction was chosen anyway

### 5. Link to real tickets

Reference stories, features, tech debt cleanup

---

## Linking RFCs to Your Work

- Jira/ADO: “This story is blocked by RFC-007”
- README or repo docs: “See RFC-012 for legacy auth removal”
- Test strategy: “Covers requirements from RFC-010”

---

## RFC Template and Metadata

```yaml
---
title: "RFC-007: Unified Config Service"
author: "infra-team"
status: "proposed"
component: "config-api"
created: "2025-04-30"
tags: ["config", "microservices", "refactor"]
```

Track:

- Status: draft, discussion, accepted, rejected, superseded
- Tags: for filtering and grouping
- Created date and revision history

---

## Folder Structure Example

```plaintext
docs/
├── rfc/
│   ├── rfc-001-initial-schema.md
│   ├── rfc-007-unified-config.md
├── adr/
│   ├── adr-014-use-keycloak.md
├── diagrams/
│   ├── config-flow.mmd
```

---

## Common Pitfalls

| Pitfall | Fix |
|--------|-----|
| No one reads them | Share in syncs, channels, reviews |
| No follow-up | Assign owner to drive RFC forward |
| Too verbose | Aim for clarity over formality |
| Ends in limbo | Set review window, declare outcome |

---

## Why RFCs Help Culture

- Create a record of thoughtful engineering
- Invite multiple voices into decision-making
- Build confidence in change
- Improve trust between platform and feature teams
- Teach juniors how architectural thinking works

---

## Final Thoughts

RFCs aren’t red tape — they’re open space. They give teams the permission, format, and clarity to explore options together without endless Slack threads or whisper networks.

Use them to slow down when it matters, to show your thinking, and to future-proof your system with historical context.

Pair RFCs with ADRs, tag and trace them, and you’ll build a body of design knowledge your whole org can stand on.

---

📘 Next in the series: [Writing a Software Design Specification (SDS) Using Docs-as-Code](2025-05-15-sds-docs-as-code.md)
