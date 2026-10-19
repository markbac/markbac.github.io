---
title: Definition of Ready
---

# Definition of Ready

A backlog item is ready when the team can start it on the first day of the sprint without going back to ask what it means. Use this list in backlog refinement. An item that fails any line stays in the backlog until it passes.

The Definition of Ready is a gate, not a form to fill in. If the team keeps waving items through that fail it, change the list or change the refinement, but do not keep both.

## Checklist

- [ ] **DoR-1 The story is clear.** It says who wants what and why, in a sentence or two. "As a ... I want ... so that ..." is a good default.
- [ ] **DoR-2 Acceptance criteria are written and agreed.** Each one is a concrete pass or fail check, agreed by the product owner and the people who will build and test it.
- [ ] **DoR-3 The design is understood.** Where the item needs design work, the approach has been discussed and either written down or understood well enough to start.
- [ ] **DoR-4 The architecture is understood.** The services, interfaces, environments and decisions the item depends on are known, and it fits the system as it stands.
- [ ] **DoR-5 Non-functional requirements are stated.** Performance, security, reliability, power and compliance needs are written down where they apply.
- [ ] **DoR-6 Dependencies are resolved or planned.** Nothing outside the team blocks the item, or the blocker has an owner and a date.
- [ ] **DoR-7 The story is Independent, Negotiable, Valuable, Estimable, Small and Testable (INVEST).** The table below explains each letter.

**As Markdown.** To copy it into an issue, a pull request or a review record:

```markdown
- [ ] **DoR-1 The story is clear.** It says who wants what and why, in a sentence or two. "As a ... I want ... so that ..." is a good default.
- [ ] **DoR-2 Acceptance criteria are written and agreed.** Each one is a concrete pass or fail check, agreed by the product owner and the people who will build and test it.
- [ ] **DoR-3 The design is understood.** Where the item needs design work, the approach has been discussed and either written down or understood well enough to start.
- [ ] **DoR-4 The architecture is understood.** The services, interfaces, environments and decisions the item depends on are known, and it fits the system as it stands.
- [ ] **DoR-5 Non-functional requirements are stated.** Performance, security, reliability, power and compliance needs are written down where they apply.
- [ ] **DoR-6 Dependencies are resolved or planned.** Nothing outside the team blocks the item, or the blocker has an owner and a date.
- [ ] **DoR-7 The story is Independent, Negotiable, Valuable, Estimable, Small and Testable (INVEST).** The table below explains each letter.
```


## The INVEST test

INVEST is a quick test of whether a user story is well formed.

[[CAPTION:Table]] The INVEST criteria.

| ID | Letter | The story is ready when |
|----|--------|-------------------------|
| I-1 | Independent | It can be built, tested and delivered without waiting for other work in progress |
| I-2 | Negotiable | The detail is open to discussion between the team and the product owner, and it is not a fixed contract |
| I-3 | Valuable | It delivers something a customer, stakeholder or downstream system can see |
| I-4 | Estimable | The team understands the scope and approach well enough to size it |
| I-5 | Small | It fits comfortably in one sprint, typically two to four engineering days |
| I-6 | Testable | Its acceptance criteria give a clear pass or fail |

## Common problems

- Epics pulled into a sprint whole, instead of being split first.
- Acceptance criteria that cannot fail, such as "works well" or "is fast".
- Integrations and hardware constraints that nobody mentioned until the work started.
- Security and performance needs left out because they were not in the story text.

Pair this list with the [Definition of Done](definition-of-done.md): one controls what goes into a sprint and the other controls what comes out.
