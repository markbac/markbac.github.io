---
title: Architecture decision record
---

# Architecture decision record

An architecture decision record (ADR) captures one significant decision: the problem, the options, the choice and what follows from it. Write one when a decision is hard to reverse, affects more than one component, or will puzzle someone who joins the project later. Michael Nygard [described the idea](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) in 2011, and most ADR formats, this one included, descend from his.

- Keep each record short, usually one page, and about one decision.
- Store records in the repository beside the code, for example in `docs/adr/`, numbered in order: `0007-use-cbor-for-telemetry.md`.
- Never edit an accepted record to change the decision. Write a new one that supersedes it, and link the two.
- When a decision needs wide discussion first, write a [request for comments](rfc.md), and record the outcome as an ADR.

## Template

```markdown
---
id: ADR-0000
title: Short imperative title, for example "Use CBOR for telemetry payloads"
status: proposed        # proposed | accepted | rejected | deprecated | superseded
date: YYYY-MM-DD
deciders: [names or roles]
requirements: [REQ-...]
principles: [AP-...]
rfc:                    # RFC-0000, if one led to this decision
supersedes:             # ADR-0000
superseded-by:          # ADR-0000
---

# ADR-0000: Short imperative title

## Context

What is the problem, and why does it need a decision now? Describe the
forces at work: technical, commercial, regulatory and schedule.

## Decision drivers

- The things that matter most in choosing, for example power budget,
  team skills or time to market.

## Options considered

1. **Option A.** Summary. Pros. Cons.
2. **Option B.** Summary. Pros. Cons.
3. **Do nothing.** What happens if we do not decide.

## Decision

We will do X, because Y.

## Consequences

- Good: what becomes easier.
- Bad: what becomes harder, and what we accept as a result.
- Follow-up: actions, other decisions or documents to update.

## Verification

How we will know the decision is working, and when we will check.

## Related

Links to requirements, other ADRs, RFCs and designs.
```
