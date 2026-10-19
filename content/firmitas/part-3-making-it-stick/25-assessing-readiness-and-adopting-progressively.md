---
title: "Chapter 25: Assessing Readiness and Adopting Progressively"
---

# Chapter 25: Assessing Readiness and Adopting Progressively

Firmitas is not installed. It is grown — incrementally, within real organisations, by real leaders who have competing priorities, imperfect information, and limited political capital. The organisations that have successfully changed their delivery governance have not done so through comprehensive framework rollouts or transformation programmes. They have done so through specific, visible changes in specific, observable behaviours, starting where the conditions for success are most favourable and building from there.

This chapter provides two instruments for that process. The Firmitas Delivery Diagnostic — twenty-six questions that assess how a real programme compares to what the framework requires — and the progressive adoption model that guides how an organisation moves from where it is to where the framework asks it to be, without collapsing under the weight of trying to change everything simultaneously.

Both instruments start from the same premise: the honest assessment of current conditions is more valuable than the aspiration toward ideal ones. An organisation that knows where it actually is has the information required to make deliberate progress. An organisation that believes it is further along than it is will make the mistakes that Chapter 5 described — drawing the wrong lessons, adding the wrong processes, and wondering why the outcomes do not improve.

---

## Assessing organisational readiness

Before attempting adoption, an organisation must honestly assess whether the conditions for adoption exist. Not whether leadership is enthusiastic — enthusiasm is a weak predictor of sustained change. Whether the systems the framework requires can be established, maintained, and protected in the organisational context that actually exists.

Firmitas readiness is assessed across six dimensions that correspond to the six system types described in Chapter 4.

**Human systems readiness.** Do people feel safe to surface honest information — about risks, about estimates, about the gap between the programme's official narrative and its operational reality? Is failure treated as learning or as blame assignment? Are engineering concerns heard and acted upon, or noted and bypassed? If the human system makes honesty expensive and comfortable reporting rational, the framework cannot function — because the framework depends on accurate information flowing to the governance layer, and that flow requires a human system that does not punish the people who produce honest information.

**Organisational systems readiness.** Does decision authority align with delivery knowledge? Are the people making programme commitments the people with enough understanding of what the programme requires to make those commitments honestly? Are incentives structured around outcomes or around outputs and appearance? Can the organisation make portfolio prioritisation decisions based on current reality rather than the inertia of a previous plan? If the organisational system rewards the appearance of delivery over its reality, the framework's governance model will be adopted superficially — the artefacts will exist, but the decisions they are supposed to generate will not be made.

**Socio-technical systems readiness.** Is the tooling capable of supporting the governance practices the framework requires? Can the risk register be maintained as a live instrument rather than a filing obligation? Can documentation be produced and maintained alongside code rather than as a separate governance exercise? Can traceability be established and maintained without requiring dedicated documentation teams? If the tools are designed to produce governance artefacts rather than to support governance decisions, the framework's documentation and traceability disciplines will produce compliance theatre rather than the living evidence the framework requires.

**Product and delivery systems readiness.** Does the delivery system have the feedback loops that the iterative development core requires? Can the organisation validate continuously rather than deferring all validation to a late phase? Are batch sizes manageable? Are handoffs between teams designed to preserve rather than destroy context? If the delivery system has been designed for sequential, batch-heavy delivery, the iterative core will require structural changes that cannot be made without disrupting the delivery of programmes already in flight.

**Technical and architectural systems readiness.** Does the existing architecture support the team autonomy and the integration cadence that the delivery model requires? Is technical debt visible and managed, or invisible and accumulating? Are architectural decisions documented and accessible? If the existing architecture enforces the coordination patterns that the framework is designed to eliminate, improving governance without addressing the architecture will produce teams that are governed better but still constrained by the structural conditions that make flow expensive.

**Economic and business systems readiness.** Are engineering programmes evaluated on outcomes or on output and activity metrics? Is the business capable of having honest conversations about what is achievable within commercial constraints, or does the commercial culture require optimistic commitments regardless of evidence? Are the funding models compatible with the delivery approach the framework requires? If the economic system rewards commercial commitments made before scope is understood and penalises the honest acknowledgement of uncertainty, the framework's commitment and estimation disciplines will be adopted in form while being violated in substance.

---

## Signals of low readiness

Some conditions indicate that adoption will fail before it has produced enough evidence to survive the first wave of organisational resistance. These are not reasons to abandon adoption — but they are reasons to address the conditions before attempting adoption, or to choose an entry point that is insulated from them.

Fear-driven cultures. When the primary motivation for producing governance artefacts is to avoid blame rather than to inform decisions, the artefacts will be designed to provide cover rather than to surface risks. The risk register will contain the risks that the governance layer is already aware of. The status report will describe the programme as it should be rather than as it is. The gate review will be prepared to pass rather than to assess readiness.

Output-heavy performance metrics. When the primary measure of engineering performance is delivery throughput — features shipped, tasks completed, milestones hit — the framework's quality and estimation disciplines will be traded for delivery pace at every point of pressure. The definition of done that includes quality standards will be quietly revised. The three-point estimate that shows a realistic most likely case will be challenged until it reaches the committed date. The technical debt that should be entered in the register will be absorbed silently to preserve the velocity metric.

Tool-led transformation narratives. When the organisational response to delivery problems is to introduce new tools — a new project management platform, a new risk register template, a new governance dashboard — without addressing the governance behaviours and cultural norms that determine how those tools are used, the new tools will be used in the same way as the old ones. The risk register will be produced in the new format and filed with the same consequences.

Zero-slack delivery expectations. When every team is at full utilisation and every hour of capacity is pre-committed to delivery activity, there is no capacity for the foundations work, the verification discipline, and the governance attention that the framework requires. Adoption cannot occur in a system that has eliminated the slack that adoption requires. Creating the conditions for adoption requires protecting capacity for it — which requires a leadership decision that something else will not be started, continued, or resourced at the level it previously was.

---

## The Firmitas Delivery Diagnostic

The diagnostic that follows is designed to be uncomfortable to answer honestly. That discomfort is the point. Easy questions produce comfortable answers that reveal nothing. The questions here require specific evidence rather than general assessment. If the evidence is not available, the answer is no.

**How to use this diagnostic**

Answer yes or no to each question. If you hesitate, the answer is no. If you answer yes, the evidence check applies. If you cannot produce the evidence in five minutes, the answer reverts to no.

Score one point for each confirmed yes with evidence. The score and the clustering of no answers will indicate both the overall readiness of the programme and which dimensions require the most urgent attention.

---

### Dimension 1 — Commitments and Planning

**Q1.** Was your current delivery date set by the people who have to meet it?

*Evidence check: Name the person who set the date and the person accountable for delivering it. If they are different people, at what point was the delivery team's honest estimate compared against the committed date — and what happened when they differed?*

**Q2.** Does your current plan include a worst case estimate with the specific risks that would cause it?

*Evidence check: Find the worst case number in your current plan. Find the named risks used to derive it. Find the owner and current mitigation status of each risk today. If the worst case exists without attached risks, or the risks exist without owners, the answer is no.*

**Q3.** When the last estimate your engineering team produced differed significantly from the committed date, was the estimate preserved in programme documentation alongside the committed date?

*Evidence check: Find that estimate. Is it still visible in programme documentation or was it replaced by the committed date? If it was replaced, the programme is running on a date, not an estimate.*

**Q4.** Has a programme gate ever stopped or fundamentally changed a programme in your organisation?

*Evidence check: Name the programme, the gate, and the decision. If every gate in your organisation's history has resulted in proceed, your gates are not functioning as decision points.*

**Q5.** When commercial or schedule pressure has been applied to your programme, has the risk register been formally updated to reflect the increased risk of the accelerated plan?

*Evidence check: Find the most recent schedule compression decision on your programme. Find the corresponding risk register update. If the schedule changed but the risks did not, the risk register is not being maintained as a live instrument.*

---

### Dimension 2 — Requirements

**Q6.** Can you trace any requirement from the customer need that generated it, through system and subsystem levels, to the test that will prove it has been met?

*Evidence check: Pick one requirement from the middle of your requirements document. Not a simple one. Not one you wrote. Trace it upward to the customer need and downward to the test case right now. If you cannot do it in five minutes the answer is no.*

**Q7.** Are your requirements granular enough that no single requirement could be satisfied by two meaningfully different implementations?

*Evidence check: Take your three highest-risk requirements. For each one, try to describe two different implementations that would both technically satisfy the requirement as written. If you can do it for any of them, those requirements are not granular enough.*

**Q8.** Are your requirements free of catch-all language that defers specification decisions to the implementer?

*Evidence check: Search your requirements document for the words "appropriate," "adequate," "as required," "suitable," "etc," "as necessary," and "to be defined." Count the occurrences. More than five per hundred requirements and the answer is no.*

**Q9.** Was every requirement written and signed off by both the stakeholder who owns the need and the engineer who will implement it?

*Evidence check: Take three requirements at random. Name the person who wrote each one. Name the stakeholder who approved it. Name the engineer who reviewed it for technical feasibility before sign-off. If you cannot name both parties for any requirement, the process was not adequate.*

**Q10.** Does every requirement in your programme have a defined, specific, testable acceptance criterion that produces an unambiguous pass or fail?

*Evidence check: Read three requirements at random. For each one, state the specific pass/fail condition right now without referring to another document. If any produce "it depends" or require interpretation, the answer is no.*

**Q11.** When requirements change on your programme, can you assess the full impact on design, dependent requirements, test cases, and delivery estimates within one working day?

*Evidence check: Take the last significant requirements change on your programme. How long did impact assessment actually take? Were gaps discovered later during implementation? If yes, the traceability was insufficient.*

---

### Dimension 3 — Knowledge, People, and Capability

**Q12.** Is the reasoning behind your three most critical architectural decisions written down and findable by someone who joined the programme in the last three months?

*Evidence check: Ask someone who joined recently to find the rationale for your most significant architectural decision without asking anyone. If it takes more than ten minutes or requires asking a person, the answer is no.*

**Q13.** Do you have a documented assessment of the capability gaps between what your programme requires and what your current team can deliver?

*Evidence check: Find that assessment. When was it last updated? What actions were taken as a result? If the assessment does not exist or has not changed a programme decision, capability gaps are being carried as invisible risk.*

**Q14.** Is your technical debt documented, risk-assessed, formally accepted by the business, and allocated budget for resolution?

*Evidence check: Find your technical debt register. For each item confirm four things — who accepted it, when, with what risk assessment, and what budget is allocated to resolve it. If you cannot answer all four for any item, it is not managed debt.*

**Q15.** If your three most experienced engineers left tomorrow, is what they know about why the system was built the way it was written down and accessible?

*Evidence check: Write down right now what would be lost. That list is your knowledge risk register. If writing it takes less than five minutes either your knowledge is well preserved or you do not know what you would lose — and those require different responses.*

**Q16.** When you last needed a capability your team did not have, was the response proportional to how critical and long-lived that need was?

*Evidence check: Name the capability gap, the response chosen, and the outcome. If the response was on-the-job upskilling under delivery pressure and the capability was critical, the gap was not adequately addressed.*

---

### Dimension 4 — Delivery and Operations

**Q17.** Was your operations team involved in design reviews and NFR definition early enough to influence what was built?

*Evidence check: Name the first design review your operations team attended. Name one NFR that exists because ops raised it. If you cannot name either, ops involvement was too late to influence the product.*

**Q18.** Could your operations team diagnose and resolve your three most likely production incidents today without involving the delivery team?

*Evidence check: Ask your operations lead to walk through the diagnosis and resolution of your three most likely incidents right now. If delivery team knowledge is required for any of them, the handover is incomplete.*

**Q19.** Do your engineers have direct, regular visibility of how end customers actually use the product they are building?

*Evidence check: Name the last time an engineer spoke directly to or observed an end customer. Name what changed in the programme as a result. If nothing changed, the visibility is not feeding back into delivery decisions.*

**Q20.** When your programme produces a workaround to meet a deadline, is that workaround formally recorded as technical debt with an owner, risk assessment, business acceptance, and resolution budget?

*Evidence check: Find the last three deadline-driven workarounds on your programme in the technical debt register. If they are not there, they are invisible risks accumulating interest.*

---

### Dimension 5 — Leadership and Governance

**Q21.** Do your engineers know without asking which decisions they are empowered to make and which require escalation?

*Evidence check: Ask three engineers independently and without warning to describe their decision authority. If their answers differ significantly or any answer is "it depends," the boundaries are not clear enough to be functional.*

**Q22.** Does your governance process improve the quality of decisions rather than primarily create a record that decisions were made?

*Evidence check: Name the last decision your governance process changed significantly — not approved, but changed. If you cannot name one, your governance is producing records, not improving decisions.*

**Q23.** Does your senior programme governance focus primarily on escalated risks and issues rather than task-level status?

*Evidence check: Find the agenda and minutes of your last senior programme review. Calculate the proportion of time spent on task status versus risks and issues requiring decisions. If task status dominated, the governance model is inverted.*

**Q24.** When your last significant programme failure occurred, did the accountability land on the person who made the decision that caused it?

*Evidence check: Name the failure. Name the decision that caused it. Name who made that decision. Name who was held accountable. If those are different people, accountability is inverted in your organisation and the conditions for the next failure are in place.*

**Q25.** When your engineering team's estimate has been challenged or compressed under commercial or schedule pressure, has the final number turned out to be more accurate than the original estimate?

*Evidence check: Name the last three instances where an estimate was challenged and a lower number was agreed under pressure. Find the actual outcome for each. If the original estimates were more accurate than the compressed ones, pressure is not extracting truth. It is suppressing it.*

---

### Dimension 6 — Culture and Psychological Safety

**Q26 — unscored.** If you answered all twenty-five of these questions honestly, wrote your answers down, and showed them to your engineering team — would they agree with what you wrote?

*Evidence check: There is no evidence check for this one. If the answer is yes, your self-assessment is probably accurate. If the answer is "I'm not sure," your self-assessment may be optimistic. If the answer is "they would disagree significantly," the gap between leadership perception and engineering reality is the most important finding of this diagnostic — and it is the gap the entire framework exists to close.*

---

## Scoring and interpretation

**Score one point for each confirmed yes with evidence.**

**22–25:** Your delivery system has genuine structural health. The nos are your improvement priorities in order of their position in the diagnostic — commitments and requirements failures compound everything else.

**17–21:** Meaningful gaps in at least two dimensions. The nos are active programme risks, not future improvements.

**12–16:** Your programme is carrying significantly more risk than your reporting shows. Start with Dimension 1 and Dimension 2 — commitment and requirements failures are the primary risk multipliers for everything downstream.

**7–11:** Your programme is being sustained by people rather than systems. That is not a performance problem. It is a structural one, and the people sustaining it will not do so indefinitely.

**0–6:** The conditions that produce programme failure are present across most dimensions. The failure may not have arrived yet. When it does, it will not be a surprise to the engineers.

---

## The clustering insight

Your score matters less than where your nos cluster.

**Nos in Dimension 1 only:** Foundations are weak but execution is sound. Fix the commitment and planning discipline before the next programme starts — it cannot be fixed mid-flight.

**Nos in Dimension 2 only:** Delivery is working but building on uncertain ground. Requirements gaps will surface as integration failures, acceptance failures, or field failures. The later they surface the more expensive they are.

**Nos in Dimension 3 only:** Systems are reasonable but knowledge is fragile. One or two key departures will expose this.

**Nos in Dimensions 1 and 2 together:** The most common high-risk pattern. Uncommitted dates and inadequate requirements are the two primary causes of the failure cycle described in Part One. If both are weak, the programme is already in the failure pattern whether or not it is visible yet.

**Nos in Dimension 6:** The formal diagnostic is unreliable. Before acting on scores in other dimensions, address the culture and psychological safety gaps — otherwise decisions are being made on information the system has filtered to be acceptable rather than accurate.

---

## Progressive adoption

The diagnostic reveals where the gaps are. The maturity model guides how to close them — not all at once, but in a sequence that builds capability and trust progressively rather than attempting a transformation that the organisation's current conditions cannot support.

### Stage 1 — Localised discipline

Firmitas principles applied within a single team or programme. The risk register is being used as a decision instrument. Estimates are three-point with conditions attached. Gates are generating decisions rather than approvals. The team is managing its own delivery with genuine autonomy within defined boundaries.

This stage builds credibility through results. It does not require organisational change. It requires a leader with the authority to govern one programme differently and the willingness to demonstrate what different governance produces.

Diagnostic score range: 7–12.

### Stage 2 — Cross-team alignment

Shared artefacts and decision logic emerge across teams. Interfaces are explicitly defined and maintained. Dependencies are managed as programme risks with trigger dates and owners. Architecture decisions are documented and accessible. The traceability spine connects requirements to evidence across team boundaries.

This stage requires the architectural and requirements disciplines described in Chapters 11 and 13. It also requires the team topology and communication disciplines described in Chapters 17 and 18 — because cross-team alignment requires that team boundaries are designed to support the integration cadence the delivery model requires.

Diagnostic score range: 12–17.

### Stage 3 — Organisational integration

Portfolio-level thinking replaces project-level optimisation. Economic trade-offs are explicit. Quality, risk, and compliance are integrated into delivery flow. Leadership behaviour starts to align with system needs — governance reviews are driven by risks and issues rather than task status, estimates are accepted with their conditions, and accountability is attributed accurately when programmes fail.

This stage is where the political obstacles described in Chapter 24 are most active. The changes required reach the governance layer, which means they require leaders who own the governance to change their own behaviour — not just to adopt new processes, but to govern differently in the specific moments when governance matters.

Diagnostic score range: 17–22.

### Stage 4 — System stewardship

Leadership actively manages system health. Slack is deliberately protected. Learning is institutionalised. The framework's disciplines are embedded in how the organisation works rather than being maintained as an explicit framework adoption. Adaptation becomes continuous rather than episodic.

At this stage, Firmitas is no longer "a framework being adopted." It is how the organisation delivers — with the principles internationalised, the governance disciplines embedded, and the continuous improvement that the learning system described in Chapter 5 produces when it is functioning correctly.

Diagnostic score range: 22–25.

---

## Avoiding the framework layering trap

The most consistent adoption failure mode is layering Firmitas on top of existing frameworks without removing or adjusting the conflicting structures. Retaining approval-heavy governance while claiming to have adopted guardrails-based governance. Introducing three-point estimation while continuing to govern programmes against the committed date. Demanding outcomes while measuring outputs.

The layering trap produces a programme with two governance systems — the formal one that was adopted and the informal one that actually governs. Teams learn quickly which one matters. They comply with the formal system when it is observed and revert to the informal system when the pressure is on.

Firmitas requires subtraction as well as addition. The governance processes that conflict with the framework's principles must be removed, not supplemented. The commitment practices that produce reverse-engineered plans must be replaced, not accompanied by a three-point estimation process that produces the honest estimate while the programme is governed against the committed date anyway.

The adoption sequence matters. The philosophy layer must be established before the framework layer. The framework layer must be established before the process layer. Changing the process without engaging with the philosophy produces compliance theatre. The artefacts exist. The governance behaviour does not change. The outcomes do not improve.

---

## What success looks like

Firmitas is never fully adopted. The framework evolves as understanding improves. The organisation changes as markets shift, programmes complete, and people move. The disciplines that are embedded today require active maintenance to remain embedded as the conditions that produced them change.

The measure of adoption is not compliance with the framework's artefact requirements. It is the quality of the governance decisions the framework produces. Can the programme board look at the risk register at week three and see the decisions it requires? Can the engineering team produce an honest three-point estimate with the confidence that it will be accepted, conditions and all? Can the leader who receives uncomfortable information treat it as the valuable signal it is rather than as the threat it used to be?

When the answer to those questions is yes — when the governance behaviour has genuinely changed, not just the governance process — the framework is working. The specific artefacts, the specific processes, the specific cadences are secondary. They are the means. The ends are decisions that are informed, accountable, and made at the right level, by the right people, with the right information.

That is what the diagnostic is measuring. That is what the maturity model is building toward. And that is what the rest of Part Three is designed to sustain.
