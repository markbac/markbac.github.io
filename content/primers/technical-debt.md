---
title: Technical debt
---

# Technical debt

Technical debt is the extra cost of future change caused by shortcuts or outdated decisions in the code and design today. Ward Cunningham coined the metaphor in 1992: like financial debt, a little taken on deliberately can help you move faster, but it accrues interest. Every change to indebted code takes longer and is riskier, until the interest consumes most of the team's time.

## Kinds of debt

Martin Fowler's technical debt quadrant separates debt by whether it was deliberate and whether it was prudent:

| | Reckless | Prudent |
| --- | --- | --- |
| **Deliberate** | "We don't have time for design." | "We must ship now and will deal with the consequences." |
| **Inadvertent** | "What's layering?" | "Now we know how we should have done it." |

[[CAPTION:Table]] The technical debt quadrant.

Prudent, deliberate debt is a legitimate business decision. Inadvertent, prudent debt is unavoidable: teams learn as they build. Reckless debt is the kind to prevent.

Debt also takes many forms beyond messy code: missing tests, outdated dependencies, manual deployment steps, missing documentation, an architecture that no longer fits the product, and slow builds.

## Signs of debt

- Simple changes take surprisingly long, or keep breaking unrelated things.
- People avoid certain areas of the code.
- Estimates for work in some areas are consistently wrong.
- Bugs cluster in the same modules.
- New team members take a long time to become productive.

## Managing it

- **Make it visible**: record significant debt in the backlog with what it costs ("every change to billing needs two days of manual testing"), not just what is wrong. A debt register or labelled tickets work.
- **Prioritise by interest, not size**: fix the debt in code that changes often. Ugly code that nobody touches costs little.
- **Pay down continuously**: leave code better than you found it (the "boy scout rule"), and reserve a steady share of capacity, such as 15 to 20 %, rather than waiting for a "refactoring sprint" that never comes.
- **Prevent the reckless kind**: [code review](code-review.md), [static analysis](static-code-analysis.md), automated [tests](testing-strategies.md) and a clear definition of done.
- **Record deliberate debt** when you take it on, ideally in an [ADR](architecture-decision-records.md) with the condition for repaying it.
- **Measure what you can**: complexity, duplication, dependency age and change failure rate show trends, though no single number captures debt.

## Talking about it

Explain debt to non-technical stakeholders in terms of speed and risk. For example: "feature X will take three weeks instead of one because of Y. A week spent on Y first makes this and the next four features faster." That makes it a business decision rather than an engineering preference.

## Where next

- [Anti-patterns](anti-patterns.md) describes common forms of design debt.
- The [Guides](../guides/index.md) section covers refactoring and maintenance in more detail.
