---
title: Request for comments
---

# Request for comments

A request for comments (RFC) proposes a significant change and asks the people it affects for their views before anyone commits to it. Use one for a change that crosses teams or sites, changes a shared interface or process, or costs enough that a wrong call would hurt.

An RFC is a discussion and an [architecture decision record](adr.md) is its result. When the RFC closes, the sponsor records the outcome below, and each decision it produced gets its own ADR.

- Set a comment period, usually one to two weeks, and keep to it.
- Name a sponsor who will make the call at the end, so the RFC does not stay open for ever.
- Keep the problem statement separate from the proposal. Reviewers often agree on one and not the other.

## Template

```markdown
---
id: RFC-0000
title: Short title
status: draft            # draft | in-review | accepted | rejected | withdrawn
author:
sponsor:                 # who decides when the comment period ends
affected: [teams or sites]
comment-period-ends: YYYY-MM-DD
decision-date: YYYY-MM-DD
---

# RFC-0000: Short title

## Summary

Two or three sentences: what you propose and why.

## Problem

What problem are we solving, for whom, and what does it cost us today?

## Goals and non-goals

- Goals:
- Non-goals:

## Proposal

The design in enough detail for reviewers to judge it: interfaces,
data, behaviour, and diagrams where they help.

## Alternatives considered

Each alternative, and why it is not the proposal. Include doing nothing.

## Impact

Who and what it affects: teams, sites, products, cost, schedule.

## Migration

How we get from here to there, and how we roll back if it goes wrong.

## Risks

What could go wrong, and how we reduce each risk.

## Open questions

- Questions the author wants reviewers to answer.

## Outcome

Completed by the sponsor at the end of the comment period.

- Decision: accepted | rejected | withdrawn
- Reason:
- Objections not resolved:
- Resulting ADRs and guideline changes:

## Change log

- YYYY-MM-DD: First draft.
```
