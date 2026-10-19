---
title: "Chapter 26: Common Failure Modes and Anti-Patterns"
---

# Chapter 26: Common Failure Modes and Anti-Patterns

Frameworks fail in predictable ways. The specific failure modes of Firmitas adoption are not random — they follow from the specific mechanisms that the framework is designed to address and the specific ways in which organisations resist the changes those mechanisms require.

This chapter catalogues those failure modes. Not as warnings to be avoided through careful reading, but as diagnostic signals — specific, observable patterns that indicate the framework is being adopted in form while the underlying system remains unchanged. Each one has a symptom that is visible, a cause that is structural, and a correction that is specific.

The chapter also addresses the hardest failure mode of all: the adoption that appears successful by every formal measure while the governance behaviour that produces the outcomes the framework is supposed to prevent continues unchanged beneath the surface.

---

## The primary failure mode — philosophy discarded, process retained

Every subsequent failure mode in this chapter is a variant of this one.

Firmitas is a philosophy-led framework. The philosophy layer — the twelve principles that establish the non-negotiables — constrains the framework layer, which constrains the process layer. When the philosophy is engaged with and the framework is understood in its context, the process layer can be applied in ways that produce the governance outcomes the framework is designed for.

When the philosophy is skipped and the process layer is installed directly, the framework becomes a set of artefacts and ceremonies. The risk register exists but is still used as a reporting tool. The three-point estimate is produced but is still compressed toward the committed date. The gate review is held but still results in approval regardless of the evidence state. The ADRs are written but are still produced to satisfy a process requirement rather than to preserve reasoning. The retrospective is held but still produces a list of actions nobody has time to implement.

The observable signal of this failure mode is a specific question. Teams that have genuinely engaged with the framework ask: "are outcomes improving?" Teams that have adopted the process without the philosophy ask: "are we doing this correctly?" The shift from the first question to the second is the first sign that the philosophy has been lost and the process has become the point.

The correction is not to add more process. It is to return to the principles — to ask, for each artefact and each ceremony, what outcome it is supposed to produce and whether it is producing it. If the risk register review is not generating decisions, the question is not whether the register is in the correct format. It is why the governance culture treats the register as a reporting artefact rather than a decision instrument, and what needs to change about the governance behaviour to change that treatment.

---

## Treating the committed date as a governance anchor

The most consequential single anti-pattern in engineering programme management — and the one that most directly produces the failure in Chapter 1 — is the treatment of the committed date as the primary governance anchor against which everything else is calibrated.

When the committed date is the anchor, the estimate is expected to reach it. The risk register is expected to show that the date is achievable. The gate review is expected to confirm that the programme is on track. The status report is expected to show green. Everything is calibrated to confirm the date rather than to reveal the programme's real state.

The observable signals are consistent. Estimates that are challenged until they show the committed date as most likely. Risk registers that show amber rather than red because red would threaten the date narrative. Gate reviews that approve programmes that are not genuinely ready because readiness is assessed against the narrative rather than the evidence. Status reports that are green while the corridors contain conversations about how the programme is actually doing.

The correction is the commitment model described in Chapter 9 — separating the commercial commitment from the honest estimate, managing the gap as a programme risk, and governing the programme against the honest estimate rather than the commercial commitment. This requires the leadership behaviour change described in Chapter 24 — specifically, the willingness to accept a most likely estimate that differs from the committed date and to treat the gap as information rather than as an engineering failure.

---

## Cargo cult governance

Cargo cult governance is the adoption of governance artefacts and ceremonies without the understanding of what they are supposed to produce.

The programme has a risk register. The risk register is reviewed at every programme board. The programme board has reviewed the risk register. The programme board has performed risk management. This is cargo cult governance — the performance of the activities associated with risk management without the substance of it, in the same way that cargo cults perform the activities associated with receiving aircraft without understanding the conditions that cause aircraft to arrive.

The observable signals: risk registers that grow without items ever being retired through decision and action. Programme boards that consistently spend less than five minutes on the risk register before moving to task status. Gate reviews that approve programmes without the evidence required having been produced. ADRs that describe decisions that were made differently from how the ADR describes them. Retrospectives that end with action items nobody owns.

The correction is not to make the ceremonies more elaborate. It is to reconnect the ceremonies to their function. The risk register review is not a ceremony. It is a meeting whose purpose is to make decisions on escalated items. It ends when those decisions have been made — not when the items have been reviewed. If the programme board is spending five minutes on the risk register, the risk register is not functioning as a decision instrument. The governance structure needs to change, not the risk register format.

---

### Empowerment theatre

Empowerment theatre is the declaration of team autonomy without the structural changes that autonomy requires. Teams are told they own the delivery. They are given autonomy over their ways of working. They are empowered to make decisions.

And then the plan is changed without consultation. The architecture decision is overridden in a review the team was not invited to. The estimate is replaced by the number that makes the business case work. The risk that was escalated is noted and the conversation moves on.

The observable signals: teams that use the language of autonomy in formal settings and behave defensively in operational ones. Decision boundaries that are unclear enough that teams spend time seeking approval for decisions they should be making independently, while governance layers make operational decisions they should be deferring to teams. Engineers who route around the governance system because they have learned that engaging with it produces worse outcomes than working around it.

The correction is the decision authority alignment described in Chapter 8 — explicit decision boundaries that are clear enough for teams to operate within without seeking approval for routine decisions, and that are stable enough that teams can trust them to hold under pressure. Autonomy that disappears when the programme is under pressure was never autonomy. It was permission, granted conditionally and revoked when the conditions changed.

---

### Output obsession in outcome language

This failure mode occurs when an organisation adopts the language of outcomes — "we focus on value delivery, not feature factories" — while continuing to measure, incentivise, and govern based on outputs.

Velocity targets dressed as "delivery predictability." Feature counts reported as "value creation." OKRs defined as delivery milestones. Teams optimised for throughput in an organisation that claims to care about impact. The language has changed. The measurement has not. The behaviour that measurement produces has not changed.

The observable signals: teams that know the outcome language and use it correctly in formal settings while working in ways that optimise for the metrics they are actually measured on. Sprint reviews that report completed features without discussion of whether those features produced the customer outcomes they were supposed to produce. Portfolio reviews that assess commercial milestones without assessing customer impact.

The correction is the alignment between stated values and actual measurement described in Chapter 22. If the organisation values outcomes, the governance metrics must measure outcomes. If the metrics measure outputs while the language claims to measure outcomes, the teams will measure outcomes with the language and deliver outputs with the work.

---

### "Lightweight" becoming "no discipline"

A specific reaction to heavy governance processes — the approval gates, the documentation requirements, the formal reviews — is to eliminate them entirely in the name of agility or pragmatism. The team is "lightweight" and "pragmatic." It does not produce unnecessary documentation. It does not hold ceremonies that do not add value.

What it also does not do is document architectural decisions, maintain a live risk register, define done criteria that include quality standards, or produce the traceability that regulated compliance requires. The reaction to bureaucracy has overshot the target, eliminating the discipline as well as the unnecessary overhead.

The observable signals: decisions that are undocumented and must be reconstructed from memory when they are challenged. Risk registers that contain no risks because the team has concluded that risk management is bureaucratic overhead. Technical debt that is invisible because documenting it would take time that could be spent on delivery. Integration failures that could have been anticipated if an interface definition had been maintained.

The correction is the distinction between ceremony and discipline — between the governance activities that exist to produce records and the governance activities that exist to produce outcomes. Eliminating the ceremony while preserving the discipline requires the governance culture to be able to articulate, for each activity, what outcome it is supposed to produce and whether a lighter-weight version of the activity produces that outcome adequately. An ADR need not be long. It must record the decision and the reasoning. A risk register need not be elaborate. It must surface the decisions the programme needs to make. Lightweight governance is not the absence of discipline. It is discipline at the minimum necessary scale to produce the outcomes required.

---

### Delegating system health to teams alone

This failure mode occurs when leadership claims to have adopted the framework's philosophy — teams own their delivery, psychological safety is important, learning from failure is valued — while retaining the structural constraints that make those aspirations impossible.

Teams blamed for outcomes they cannot influence because the incentive structures, funding models, or governance constraints that produce those outcomes are unchanged. Repeated "coaching" and "culture work" at the team level while the systemic causes of poor performance remain at the leadership level. Retrospectives that surface the same issues cycle after cycle because the authority to address the structural causes resides above the team's authority level.

The observable signals: teams that have been through multiple cycles of "improvement initiatives" without sustained improvement. Retrospective action items that are team-level interventions for organisation-level problems. High team turnover in areas where the structural conditions are most misaligned with the framework's requirements.

The correction is the leadership accountability described in Chapter 7 — the recognition that system health is a leadership responsibility that cannot be delegated to the teams operating within the system. Teams can identify what is wrong. Only leadership has the authority to change it. The coaching and the culture work that does not change the structural conditions is not investment in improvement. It is the appearance of investment, producing the wrong lesson in the same way that the lessons-learned exercise in Chapter 5 produces the wrong lesson from programme failure.

---

### The meta-failure — not learning from failure

The failure mode that all the others feed into is the meta-failure: the organisation that experiences programme failures, framework adoption failures, and governance failures repeatedly without updating its understanding of why they occur.

The retrospective is held. The action items are generated. Nothing changes. The next programme fails in the same way. The same action items are generated. The cycle repeats.

The observable signals: the same failure patterns appearing across multiple programmes without the root cause being addressed. Lessons learned libraries that contain insights from programmes going back years without evidence that those insights have been incorporated into subsequent programme governance. Leaders who can describe the failure patterns accurately and in detail without connecting them to the governance decisions that produced them.

The correction is the learning system described in Chapter 5 — the governance capacity to identify failure causes accurately, to trace those causes to the governance decisions that produced them, and to change the governance behaviour that those decisions represent. This requires the diagnostic honesty that Chapter 24 described — the willingness to examine one's own governance decisions as causes of programme outcomes rather than as context within which execution fails.

A framework that is being genuinely applied produces learning. Each programme reveals something about the governance system that the previous programme did not reveal, and the governance system is adjusted accordingly. A framework that is being performed produces compliance records. Each programme produces documentation that the process was followed. The next programme begins without the governance system having changed.

The difference between these two is not the sophistication of the framework. It is the honesty of the learning.

---

### The first warning signs

The failure modes described in this chapter share a common early signal that appears before the consequences become visible: the governance layer stops asking the question that the framework is designed to answer.

The question is: are outcomes improving?

When a programme board stops asking whether the governance process is producing better decisions, and starts asking whether the governance process is being followed correctly — the philosophy has been lost. When a team stops asking whether the risk register is surfacing the decisions the programme needs, and starts asking whether the risk register format is correct — the ceremony has replaced the substance. When a leader stops asking whether the estimate reflects honest engineering assessment, and starts asking whether the estimate has been challenged sufficiently — the committed date has become the governance anchor.

Each of these shifts is visible before the consequences arrive. The shift from outcome questions to process questions is the earliest reliable signal that the framework is being adopted in form while the governance behaviour remains unchanged.

The practical response: at every governance meeting, in every framework review, the primary question is "what decisions did this produce?" Not "did this occur?" Not "was the artefact in the correct format?" Not "did the process step happen?" What decisions did this produce, and were those the right decisions?

When the answer is consistently yes — when the governance process is consistently producing informed, accountable decisions at the right level — the framework is working. When the answer is consistently "the process occurred" rather than "decisions were produced," the framework is being performed rather than applied.

That distinction is the only one that matters.
