---
title: "Chapter 19: Technical Debt and Change Management"
---

# Chapter 19: Technical Debt and Change Management

Every engineering programme makes compromises. Scope is reduced to meet a timeline. An implementation shortcut is taken when the proper approach would take longer than the delivery window allows. A design decision is made on incomplete information and would be made differently if the full picture were available. A dependency is accepted because the alternative would require more time than the programme has.

These compromises are not failures of discipline or courage. They are the rational responses of engineering teams to the conditions of delivery under constraint. Complex programmes always operate under constraints. Compromises are inevitable. The question is not whether compromises will be made but whether they will be made consciously, documented honestly, and managed as the liabilities they are — or made invisibly, left undocumented, and inherited by future teams as constraints they cannot see and cannot evaluate.

Technical debt is the accumulated liability of those compromises. Change management is the discipline that governs how the programme evolves as understanding improves and conditions change. Both are addressed in this chapter because they share a common governance principle: the decisions that produce technical debt and the decisions that govern change are consequential programme decisions that require the same deliberate ownership as any other programme risk.

---

## What technical debt is and what it is not

Technical debt is a useful metaphor, introduced by Ward Cunningham, that describes the future cost of shortcuts taken in the present. Like financial debt, technical debt has a principal — the work that was deferred or done improperly — and interest — the compounding cost of carrying the debt, paid in slower development, higher defect rates, and the accumulated complexity of working around rather than through the underlying problem.

The metaphor has limits that are worth naming. Financial debt is taken on with explicit knowledge of its terms — the principal, the interest rate, the repayment schedule. Technical debt is most commonly taken on without explicit acknowledgement of its terms — without quantifying the principal, without estimating the interest rate, and without any commitment to a repayment schedule. This makes it substantially more dangerous than financial debt, because the organisation carrying it frequently does not know how much it is carrying or what it is costing.

Firmitas distinguishes between two categories of technical debt that require different governance responses.

**Deliberate debt** is a conscious, documented trade-off — a shortcut taken with full knowledge of what is being deferred, why it is being deferred, what the cost of carrying the debt will be, and when and how it will be addressed. Deliberate debt is a legitimate programme instrument. The pressure of a delivery deadline may make it rational to implement a temporary approach that will need to be replaced later. The benefit of proving a concept quickly may justify an implementation that would not survive production at scale. The cost of doing something properly before the requirements are fully understood may be higher than the cost of reworking it once the requirements are clear. In each of these cases, the deliberate acceptance of technical debt is a reasonable programme decision — but only when it is genuinely deliberate, genuinely documented, and genuinely managed.

**Accidental debt** is the accumulation of shortcuts, suboptimal decisions, and deferred work that was never explicitly acknowledged as debt — the implementation that was done quickly under pressure without recording that it needs to be revisited, the architectural decision that was made on incomplete information without flagging the assumption it rests on, the test that was not written because the sprint was ending and the ticket was almost done. Accidental debt is the dominant form of technical debt in most programmes, and it is substantially more dangerous than deliberate debt because it is invisible. It cannot be managed because it is not known. It surfaces as unexplained slowness, as defects in areas that seem unrelated to recent changes, as the discovery during a refactoring exercise that the system has dependencies that nobody documented and several people assumed did not exist.

The governance response to these two categories is different. Deliberate debt requires documentation, ownership, and a committed resolution plan. Accidental debt requires practices that prevent it from accumulating — architectural discipline, code review culture, definition of done criteria that include quality standards — and periodic investigations that surface what has already accumulated.

---

## The four conditions for legitimate debt

Deliberate technical debt is legitimate when four conditions are met. When any of them is absent, the debt is not being managed — it is being deferred with the hope that it will not surface as a problem before it can be addressed.

**Conscious.** The decision to incur the debt was made explicitly, not discovered after the fact. Someone chose this approach, understood what they were deferring, and accepted the trade-off with full knowledge of its terms. Debt that was incurred because nobody noticed, because the pressure of delivery made careful consideration impossible, or because the implications of the shortcut were not visible at the time it was taken is not conscious. It is accidental.

**Documented.** The debt exists as a named, described item in the programme's technical debt register. What was deferred. Why it was deferred. What the consequence of carrying it is. What resolving it requires. What happens if it is not resolved. Undocumented debt is invisible to anyone except the person who incurred it — and frequently to them as well after the programme has moved on. When that person leaves, the debt remains but the understanding of it is gone. The next team discovers it as a constraint they cannot explain.

**Business-accepted.** This is the condition that most treatments of technical debt omit, and its omission is one of the primary reasons that technical debt accumulates without management. The decision to carry technical debt is a business decision, not a technical one. The business is accepting a future cost — the cost of resolving the debt — and a current risk — the possibility that the debt will cause problems before it is resolved. That acceptance must be explicit. A senior engineer who accepts technical debt on behalf of the business without business sign-off has made a commitment the business did not know about. The business's subsequent surprise when the debt surfaces as a problem is not failure of awareness. It is the predictable consequence of a governance process that allowed a significant liability to be accepted without the visibility of the people who will pay for it.

**Resourced for resolution.** Future work to resolve the debt has been identified, estimated, and allocated. Not just acknowledged as something that will need to be done someday — specifically planned, with capacity allocated, within a timeframe that the programme accepts as appropriate for the level of risk the debt carries. Technical debt that is accepted without a credible resolution path is not managed debt. It is deferred failure with optimistic labelling. The backlog of debt items that has been accumulating for three years, revisited at each planning cycle, and deferred to the next cycle is not a managed debt register. It is a list of liabilities the organisation has chosen not to address while pretending to be managing them.

---

## Technical debt taxonomy

Not all technical debt is the same. Different types carry different risks, require different governance responses, and have different resolution costs. Understanding the type of debt the programme is carrying determines the urgency and approach of the resolution response.

**Strategic debt** is consciously incurred to accelerate delivery of something more valuable. The temporary integration approach used to validate a market assumption before investing in the proper architecture. The simplified implementation used to demonstrate a capability proof-of-concept before the production design is committed. Strategic debt is the most legitimate form of deliberate debt — it is incurred because the cost of doing it properly before the value is confirmed exceeds the cost of the rework when the value has been confirmed. It is legitimate when the strategic purpose is real, the debt is documented, and the rework plan exists.

**Tactical debt** is small shortcuts made under time pressure that are safe to carry for short periods. The hardcoded configuration value that needs to be externalised before scaling. The error handling that is adequate for current load but not for production volumes. The test that covers the happy path but not the edge cases that production will reveal. Tactical debt is manageable when it is tracked, when its safe carry period is understood, and when it is resolved within that period rather than deferred indefinitely.

**Systemic debt** is the most dangerous category — accumulated architectural decisions that are now constraining the system's ability to evolve. The coupling that was introduced in small increments across many deliveries until the system can no longer be changed in any part without understanding all of it. The performance bottleneck that was acceptable at the original scale and is now the primary constraint on the programme's ability to grow. The security architecture that was adequate for the original threat model and is now inadequate for the evolved one. Systemic debt is rarely visible as debt in the moment it is accumulating. It becomes visible when the programme attempts a change that the accumulated debt makes expensive or impossible.

**Inherited debt** is debt that exists in systems the current team did not build and did not choose. Every programme that builds on an existing system inherits its accumulated shortcuts, its undocumented decisions, and its architectural assumptions. Inherited debt must be assessed on arrival — not assumed to be manageable because it has been managed so far. Many programmes have failed because the inherited technical debt that was present at the start of the programme was treated as background noise rather than as a risk to be understood and managed. The assessment of inherited debt is not optional. It is a programme risk quantification exercise that determines how much of the programme's delivery capacity will be consumed by managing the legacy it has been handed.

---

## Who makes the debt call

Senior engineers must have the autonomy to identify, manage, and report technical debt. They have the technical understanding to assess what is safe to defer and what constitutes a systemic risk. They have the contextual knowledge to evaluate whether a shortcut is a considered trade-off or a structural liability. They are the people closest to the work, which is where the knowledge that determines the correct debt decision resides.

But they need two things that are often absent.

The first is the safety to surface debt honestly. In organisations where raising technical debt is treated as an admission of failure, as evidence that the team is not performing, or as a risk to the programme narrative, debt goes underground. Engineers who have raised debt concerns and watched them be ignored — or worse, used as evidence that the programme needs tighter management — stop raising them. The debt accumulates invisibly. The connection between the governance culture and the organisation's ability to manage its technical debt is direct and consequential.

The second is the authority to ensure that the business-accepted condition is genuinely met. A senior engineer who identifies a significant piece of technical debt, raises it, gets it acknowledged, and then watches it sit unresolved through three planning cycles while new features are prioritised has learned something important about the organisation's actual commitment to debt management. The next time they identify debt of similar severity, they will make a calculation about whether raising it will produce a different outcome. The resolution commitment must be real to make the identification commitment real.

---

## Change management

Change is not a failure of planning. It is the inevitable product of building complex systems in conditions of genuine uncertainty. Requirements that are specified before the system is fully understood will be revised as understanding improves. Architectural assumptions that were valid when they were made will be invalidated as the system is built and its real behaviour becomes visible. External dependencies will change in ways that affect the programme's commitments.

The question is not whether change will occur. It is whether the programme has a mechanism for managing change that preserves the integrity of its commitments, maintains the traceability of its requirements and design decisions, and ensures that the decisions about whether and how to accommodate a change are made at the appropriate level with the appropriate evidence.

Firmitas distinguishes between three classes of change that require different governance responses.

**Learning-driven change** is change that results from the programme's discovery of information that was not available when earlier decisions were made. The integration test that reveals an interface assumption was wrong. The customer feedback that reveals a requirement was misunderstood. The performance measurement that reveals an architectural assumption was invalid. Learning-driven change is expected and welcomed in a programme that is practising iterative development — it is the evidence that the feedback loops are working. The governance response is not to prevent learning-driven change but to ensure that it is incorporated systematically — updating the affected requirements, revising the affected design decisions, creating ADRs that capture the new understanding, and assessing the impact on the delivery estimate.

**Scope change** is change to the programme's committed deliverable — a new requirement added, an existing requirement revised, a feature removed. Scope change requires formal change management because it affects the programme's commitments — the delivery date, the cost, and the quality of what will be delivered. Scope change that is accepted without assessing its impact on the programme's commitments is not change management. It is the silent absorption of additional obligation into a programme that is already committed — which is how programmes accumulate the gap between their committed scope and their delivered capacity that surfaces as the surprise at month six that Chapter 1 described.

Every scope change must be evaluated against four questions: What is the impact on the delivery estimate? What is the impact on the risk register? What is the impact on the architectural decisions that have already been made? And what is the commercial and contractual implication? Only after those questions have been answered honestly can the decision about whether to accept the change be made with adequate information.

**Architectural change** is change to the fundamental decisions that shape the system's structure — the boundaries between components, the interfaces between disciplines, the patterns and principles that the development teams are building within. Architectural change carries the highest programme risk of the three classes, because its consequences are systemic. An architectural change that affects a shared interface affects every team that uses it. An architectural change that revises a fundamental pattern potentially requires every team's implementation of that pattern to be revisited.

Architectural change requires the ADR process — an explicit record of the decision, the rationale, the alternatives considered, and the assessment of impact. It requires involvement from the teams affected before the decision is finalised — because the teams building within the architecture have knowledge of its current state that the architectural decision-makers may not have. And it requires an impact assessment on the delivery estimate and the risk register before the change is accepted.

---

## The cost of thrash

Change is not free. Every change to requirements, design, or architecture carries a cost — the cost of revising the affected artefacts, updating the affected implementations, re-running the affected tests, and communicating the change to everyone who has been working on assumptions that the change invalidates.

When change is frequent, unpredictable, and poorly governed, the cost of managing change can exceed the cost of the development work itself. Teams spend more time responding to change than delivering new capability. The instability of the requirements and the architecture makes it impossible to build on previous work without the risk of being invalidated by the next change. Cognitive load increases as teams must hold increasingly complex mental models of what is current versus what has been superseded. Quality degrades because the test coverage required to validate a changing system cannot be maintained at pace with the changes.

This is the failure mode called thrash — a programme that is consuming its delivery capacity in the management of change rather than in the production of value. Thrash is not caused by change itself. It is caused by change that is poorly governed — accepted without impact assessment, incorporated without architectural discipline, and communicated without adequate time for the affected teams to update their work.

The governance response to thrash is not to prevent change. It is to ensure that change goes through the process required to assess its impact, accept it deliberately, and incorporate it without destroying the work that preceded it. Programmes that cannot change without thrashing have not been designed for change. They have been designed for stability under conditions — predetermined requirements, validated architecture, stable external dependencies — that complex programmes do not reliably provide.

---

## Knowing when not to change

One of the most important and least discussed aspects of change management is the discipline of not changing — of recognising when a proposed change would consume more delivery capacity than the value it would add, and explicitly deciding not to accept it.

Every programme receives more change requests than it can productively accommodate. The features that were not in the original scope. The requirements revisions that make previous implementations obsolete. The architectural improvements that would benefit future maintainability but at the cost of current delivery. The client requests that arise from evolving understanding of their operational needs.

All of these changes may be individually justified. Collectively, they can consume the programme's delivery capacity and prevent any of them from being delivered well. The discipline of change management includes the discipline of saying no — of applying the governance questions to each proposed change, assessing its real cost against its real benefit, and declining the changes that do not justify their delivery impact.

This requires a governance culture that can have honest conversations about what the programme can and cannot accommodate. A governance culture that cannot decline client change requests because client relationships are managed by people who lack the authority to say no to clients while having the authority to commit engineering teams is a governance culture that will absorb change until it destroys the programme it was supposed to protect.

The commercial conversation about what a programme can and cannot accommodate is a governance decision that belongs at the level where both the commercial commitment and the delivery capacity are understood. That level is not the engineering team.

---

## Technical debt and the long view

The relationship between technical debt, change management, and the long-term health of the systems the programme produces is the direct expression of Principle 10 and Principle 11 — the cost of short-term optimisation is paid by people who had no say in the decision, and optimising for long-term system health is the leadership responsibility that most directly determines whether what the programme builds will be a sustainable asset or a accumulating liability.

Programmes that manage debt deliberately — accepting it when it is genuinely justified, documenting it honestly, ensuring business acceptance, and resourcing resolution — produce systems that are sustainable. They carry known liabilities that are being managed. Future teams can understand the constraints the system operates under, evaluate which constraints are still valid, and plan their evolution accordingly.

Programmes that allow debt to accumulate invisibly — through accidental shortcuts, through the systematic treatment of quality as optional under schedule pressure, through the acceptance of change without architectural discipline — produce systems that become progressively harder and more expensive to operate and evolve. The interest on the debt compounds. The cost of each new delivery increases as the system's complexity grows. The teams maintaining the system spend an increasing proportion of their capacity managing the consequences of the decisions made under pressure in previous delivery cycles.

The technical debt that is created in a programme is not just the programme's problem. It is the inheritance of every team that will touch the system afterward — potentially for decades. Engineering stewardship, in the Firmitas sense, extends beyond initial delivery to include responsibility for the operability, maintainability, and evolvability of what is built. Accepting technical debt without managing it is not a programme delivery decision. It is an act of borrowing against the future of the people who will maintain what the programme has built.
