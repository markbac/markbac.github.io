---
title: "Chapter 20: Capability, People, and Building for the Long Term"
---

# Chapter 20: Capability, People, and Building for the Long Term

A programme can have sound architecture, honest estimates, a functional risk register, and a governance model that generates decisions rather than acknowledgements — and still fail to deliver if the people responsible for the delivery do not have the capability the work requires. Capability gaps are programme risks. They are among the most common programme risks and among the most consistently underestimated.

Underestimated because they are visible before they become problems, but the visibility does not reliably produce the response. The gap between the capability a programme needs and the capability the team has is usually identifiable during the structured foundations phase — if anyone is looking for it. It is rarely managed with the same rigour as a technical risk or an integration dependency. Instead, it is absorbed silently, managed through on-the-job learning under delivery pressure, and attributed to execution failure when the limitation it produces surfaces as a programme problem.

This chapter addresses capability as a delivery discipline — how gaps are identified, how responses are matched to the specific nature of each gap, how people are developed rather than consumed, and what the long-term stewardship of engineering capability means for organisations that want to build something sustainable rather than running their people down in service of the next deadline.

---

## Capability gaps are programme risks

The lead systems engineer on the programme in Chapter 1 identified three red risks in week three. None of them was a capability gap. That is not because capability gaps did not exist on that programme — they almost certainly did. It is because capability gaps are rarely surfaced as programme risks in the way that technical and integration risks are.

The reasons for this are structural. Technical risks are visible in the architecture and the requirements — the unvalidated interface, the unconfirmed dependency, the ambiguous specification. Capability gaps are visible in the people — in what they have and have not done before, in what skills the programme requires that the team does not currently possess. Surfacing a capability gap requires someone to look at the team as honestly as they look at the architecture, to ask what this programme needs that the team cannot yet reliably provide, and to treat the answer as programme risk rather than as an uncomfortable observation about the people involved.

This honesty is rare, for understandable reasons. Naming a capability gap feels like a criticism of the people whose gap it is. In a team that has been assembled and is working, the social cost of formally identifying gaps is high. The result is that capability gaps are managed informally — through close supervision, through pairing people who have the capability with people who are developing it, through tolerating slower delivery in the areas where the capability is weakest — without the explicit identification and resource allocation that would constitute proper risk management.

The informal management is not always wrong. Some capability gaps are appropriate to manage informally — when they are small, when the work is not on the critical path, and when the person developing the capability has adequate support and slack to do so. But when the gap is in a critical capability, on a critical path, in a team that is already at full utilisation, informal management produces the same outcome as managing any other risk informally: the risk materialises on schedule, and the consequence is attributed to execution failure rather than to the risk management failure that allowed it to materialise unmanaged.

---

## Identifying capability gaps

Capability gap identification is a structured activity that belongs in the programme's foundations phase, not a conversation that happens when a problem has already surfaced.

The identification process has two parts. The first is a clear articulation of what the programme needs — not generically, but specifically for this programme, at this point in its delivery. What technical capabilities are required? What domain knowledge? What regulatory and compliance understanding? What toolchain and process familiarity? What leadership and communication capabilities are required at the team level?

The second is an honest assessment of what the team currently has. Not a self-assessment by the team members themselves — self-assessments of capability are reliably optimistic, for the same reason that self-assessments of risk tend toward amber rather than red. A structured assessment by someone with the relevant expertise to evaluate the team's capability against the programme's requirements.

The gap between these two assessments is the capability risk. It should be entered in the risk register in the same form as any other programme risk — specific description, probability and impact assessment, named owner, mitigation plan, trigger date. The mitigation plan is the capability development response described in the next section. The trigger date is the point in the programme at which the capability will be needed at the level the programme requires — because the response to a capability gap must be initiated early enough to be effective before that point, not at the point itself.

---

## The capability decision framework

When a capability gap is identified, the response must be proportional to the criticality of the capability and the duration for which it is needed. The most common response — on-the-job upskilling with minimal support — is chosen because it is cheap and immediate, but it is appropriate only when the gap is small, the capability is not on the critical path, and adequate support and slack exist for genuine learning to occur.

Four questions determine the appropriate response.

**How critical is this capability to delivery outcomes?** If the gap is in a non-critical area, on the job learning with appropriate support is usually adequate. If the gap is in a critical path capability — the firmware architect, the safety engineer, the systems integrator, the regulatory specialist — the response must be more deliberate and better resourced. A capability gap in a critical path capability that is managed informally is not being managed. It is being deferred until it surfaces as a delivery problem.

**How long is the capability needed?** A capability needed for a specific, bounded activity in the programme — the regulatory submission phase, the performance characterisation sprint, the security review — may justify a specialist contractor or third-party engagement for the duration of that activity. A capability needed throughout the programme's life requires a different response — either recruiting someone who has it, or developing it within the team at a pace and with a resource allocation that matches the timeline on which it will be needed.

**Is there time for the person to develop the capability before it is needed?** If the answer is yes — if the capability will not be needed at full competence for several months, and if adequate support and slack exist for structured development — on-the-job development with mentoring and protected learning time is the right response. If the answer is no — if the capability is needed now, or within a window that does not allow adequate development time — bringing in external capability while developing internal capability in parallel is the honest response. Expecting someone to develop a complex capability in a compressed timeframe while delivering at full pace is not a development plan. It is a plan to fail more slowly.

**What happens if the capability gap is not filled?** If the honest answer is that an important delivery milestone will be missed, that the programme will produce something that does not meet its requirements, or that a regulatory or safety obligation will not be met, the capability gap is a programme risk that must be owned at the level that made the commitment — not absorbed silently by the team that is expected to deliver against it.

---

## The options and their honest assessment

**On-the-job upskilling with structured support** is the most common response and the most commonly misapplied one. It is appropriate when the gap is modest, the work is not on the critical path, the person has adequate cognitive slack to learn while delivering, and the support — a mentor, a pairing partner, protected learning time — is genuinely provided rather than nominally promised. It is the most likely to be applied when none of these conditions are met, because it is the cheapest option and the one that requires no difficult decisions.

The specific failure mode of on-the-job upskilling without adequate support is that the person develops the capability more slowly than the programme needs it, carries more cognitive load than is sustainable, produces work of lower quality during the development period, and ends up neither developing the capability adequately nor delivering the work effectively. The programme absorbs the cost of this through slower delivery, higher defect rates, and the programme manager's growing awareness that certain areas of the work are progressing less well than others — which is attributed to individual performance rather than to the capability response decision.

**Specialist contractor or third-party engagement** is appropriate when the capability is needed for a bounded period, the window for development does not exist, or the specialisation required is too narrow to justify a permanent hire. It is also appropriate as a bridging response while a permanent capability is being developed or recruited — providing the capability the programme needs now while building the internal capability that will sustain it over time.

The risk of specialist contractor engagement is dependency — the programme becomes reliant on knowledge that resides in an external party rather than in the organisation. Firmitas accepts this risk when it is the honest response to the capability gap, and manages it through structured knowledge transfer — ensuring that the specialist's knowledge is progressively distributed to the internal team rather than remaining concentrated in the specialist.

**Training and structured development** is appropriate for capabilities where the gap is real but the development can be done through formal training, certification, or structured learning rather than through on-the-job development alone. Regulatory knowledge. Toolchain proficiency. Quality management practices. These are capabilities that can be developed systematically through structured programmes, rather than through the unguided learning that on-the-job upskilling often provides.

**Recruitment** is appropriate when the capability is needed for the long term, when the internal development path is too slow, and when the capability is strategic enough to justify the cost and time of hiring. The lead time of recruitment — typically several months from the decision to hire to the point at which a new person is contributing at full effectiveness — must be factored into the capability timeline. Deciding to recruit when the capability is already needed does not solve the near-term problem. It creates an expectation of capability that will not be met for months, during which the programme continues to operate with the gap it has.

---

## People are not interchangeable

The governance and commercial pressure that produces the capability responses described above also produces a more fundamental misframing: the treatment of people as interchangeable units of capacity that can be swapped in and out of programmes without cost to programme outcomes or to the people themselves.

This misframing is embedded in the language of resource management. Headcount. FTEs. Resource allocation. The language treats people as fungible — one senior engineer equivalent to another, one firmware developer interchangeable with the next. The reality is the opposite.

The senior engineer who has been on a programme for twelve months carries knowledge that no new hire can replicate in a week, or a month, or possibly ever. They know which architectural decisions were made and why. They know which risks were debated and what the arguments for and against were. They know which constraints are fundamental to the system and which are historical artefacts. They know where the technical debt is and what it will cost to address. They know the client's real concerns as distinct from their stated requirements. This knowledge — the programme's accumulated understanding, distributed across the people who have been building it — is the most valuable asset the programme has. It cannot be put in a document quickly enough to be fully preserved. It is lost, partially and irreversibly, every time someone who carries it leaves the programme.

The cost of this loss does not appear on the capacity plan. It appears later — in the decisions made by incoming team members without the context to make them correctly, in the technical debt accumulated because the understanding required to manage it has been lost, in the integration failures that result from assumptions that the departing team member held and never documented, in the rework required when the system's undocumented constraints are violated by people who did not know they existed.

Principle 12 exists because this cost is real and because the treatment of people as interchangeable resources is one of the primary mechanisms by which it is incurred. Your people are your most significant investment — recruited carefully, developed over time, and irreplaceable in practice. The organisation that treats them as interchangeable will eventually have interchangeable people — not because that is who they are, but because the people with irreplaceable knowledge and the self-respect to expect to be treated accordingly have left for organisations that recognise the difference.

---

## Building capability for the long term

The argument in this chapter so far has been primarily about managing capability gaps — the immediate, programme-level responses to capability that is insufficient for current delivery needs. But capability management has a longer horizon than any single programme, and the organisations that consistently deliver well are the ones that build capability deliberately over time rather than responding to gaps reactively when programmes are already at risk.

Building capability for the long term requires three things that most organisations underinvest in.

**Deliberate development paths.** Engineers do not develop from competent to expert without deliberate exposure to progressively complex challenges, structured feedback, and protected time for the reflection that converts experience into expertise. The organisation that puts engineers in challenging positions without adequate support produces engineers who are anxious rather than developing. The organisation that provides support without challenge produces engineers who are comfortable but not growing. Deliberate development requires both — structured exposure to challenges that are at the edge of current capability, with the mentoring and slack that allow genuine learning to occur rather than mere survival.

**Knowledge transfer as a programme discipline.** The knowledge that engineers develop on programmes must be distributed before it becomes the property of individuals who can take it with them when they leave. This is not a matter of documentation alone — documentation captures explicit knowledge, not the tacit understanding that comes from experience. Distributing tacit knowledge requires practices that create the conditions for it to be shared: pair programming, design reviews that involve developing engineers as full participants rather than observers, retrospectives that examine what the team learned rather than just what happened, mentoring relationships in which the knowledge holder deliberately teaches rather than simply working alongside the learner.

**Technical career paths that do not require people to become managers.** The most technically capable engineers in most organisations face a career structure that offers two paths: become a manager, or remain in a role whose seniority and compensation plateau at a level that the organisation does not consider commensurate with real leadership. This structure consistently loses the people whose technical depth is the organisation's most valuable capability — either to management roles for which they are less suited than the technical roles they have vacated, or to other organisations that offer senior technical tracks.

The organisations that retain deep technical capability offer technical career paths that are treated as equivalent in seniority, compensation, and organisational influence to management paths. The principal engineer who influences architectural decisions across the portfolio. The technical fellow who advises on emerging technology strategy. The domain expert whose judgement is explicitly sought in governance decisions that require their knowledge. These are real leadership roles, even though they do not involve managing people. Treating them as such — with the recognition, the compensation, and the governance influence that reflects their value — is how organisations keep the capability they have invested years in building.

---

## The cost of getting this wrong

The cost of poor capability management is not visible on a delivery dashboard. It accumulates in ways that look like execution problems rather than capability problems — slower delivery in areas where the capability is weakest, higher defect rates in components built by engineers who are developing rather than competent, integration failures at the boundaries where discipline-specific knowledge should have been applied and was not.

By the time these costs become visible, the root cause has typically been obscured by months of programme narrative. The delivery problem is real. The connection to the capability gap that preceded it — the gap that was not entered in the risk register, not escalated as a programme risk, not addressed before it became a constraint on delivery — is lost.

The programme management response, when these problems surface, is typically to apply more pressure to the people experiencing the capability limitation — to manage their work more closely, to set harder deadlines for the areas that are running late, to escalate the performance of the team members in whose work the gap is most visible. This response is not only ineffective. It is the structural consequence of treating a capability risk as an execution failure.

The governance response, when a capability gap surfaces as a delivery problem, should not be pressure on the individuals affected. It should be the governance question that was not asked earlier: what capability does this programme require that the team does not have, why was this not identified and managed as a programme risk, and what needs to change to provide the programme with the capability it needs — now that the gap is visible, and in future programmes before it becomes a problem?

That question is more uncomfortable than the pressure response. It locates the cause correctly. It requires the governance layer to examine its own risk management rather than the team's delivery performance. It produces the learning that might prevent the next programme from experiencing the same gap in the same way.

That is what capability management, properly done, looks like.
