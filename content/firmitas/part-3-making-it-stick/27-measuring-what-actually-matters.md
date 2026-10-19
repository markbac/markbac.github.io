---
title: "Chapter 27: Measuring What Actually Matters"
---

# Chapter 27: Measuring What Actually Matters

Measurement is one of the most powerful forces in any engineering organisation. It shapes behaviour, priorities, and decision-making more strongly than stated values, framework principles, or leadership intent. What gets measured gets optimised. What gets optimised is what the measurement rewards, regardless of whether that is what the organisation intended to reward.

This creates a specific and consequential risk in framework adoption: measurement systems designed for the wrong outcomes silently undermine the framework's governance disciplines while appearing to support them. The organisation measures velocity and gets velocity — at the cost of quality. It measures milestone completion and gets milestone completion — at the cost of honest assessment. It measures defect counts and gets low defect counts — because teams stop looking for defects rather than stop creating them.

Firmitas treats measurement as a system design problem, not a reporting exercise. Poorly designed measures distort behaviour, hide risk, and erode the conditions the framework requires. Well-designed measures make reality visible, enable learning, and support the governance decisions that the framework is built around.

This chapter addresses what to measure, what to avoid measuring, and how measurement connects to the diagnostic dimensions established in Chapter 25.

---

## Measurement is never neutral

Every measure creates an incentive. Every incentive changes behaviour. The question is not whether measurement influences outcomes — it always does. The question is whether it influences them deliberately or accidentally.

The most common measurement failure in engineering programme management is the adoption of metrics that are easy to collect but inversely correlated with what they are supposed to measure. Defect counts that fall because teams stop reporting defects. Test coverage percentages that rise because tests are written to cover lines rather than to catch failures. Story point velocity that increases because the definition of done is relaxed. Feature counts that grow because features are subdivided into smaller units. Each of these metrics improves without the underlying quality improving. Each of them teaches teams what to optimise — and what to sacrifice to optimise it.

The governance layer that sees improving metrics and concludes that the programme is improving has been deceived not by the teams but by the measurement system. The teams are behaving rationally — optimising the thing they are measured on. The governance layer is drawing conclusions from the optimised measurement rather than from the operational reality it was supposed to represent. The gap between the measurement and the reality it claims to represent is the governance blindspot that allows the failure patterns of Chapter 1 to accumulate invisibly.

---

## Three categories of measurement

Firmitas distinguishes between three categories of measurement that serve different governance purposes and must not substitute for each other.

**Output measures** describe what has been produced — features delivered, tasks completed, milestones reached, documents produced, tests written. Output measures are not meaningless. They provide a view of engineering activity that can be useful for understanding capacity, identifying bottlenecks, and tracking progress against commitments. But output measures say nothing about whether the activity produced the outcomes it was supposed to produce, whether the quality of the output is adequate, or whether the delivery system is sustainable.

Output measures become damaging when they are used as success criteria. A team that is measured on feature throughput and told that throughput is the primary indicator of success will optimise for throughput — by reducing test coverage, by deferring quality work, by narrowing the definition of done, by taking the shortcuts that allow tasks to be closed faster without the work being genuinely complete. The measurement has not made the team less capable or less well-intentioned. It has made throughput the rational objective and quality the available sacrifice.

Firmitas allows output measures as local, transient signals — useful for identifying capacity constraints and understanding near-term delivery pace — but never as success criteria or primary governance instruments.

**Outcome measures** describe the effect of engineering work on the world outside the engineering system — customer adoption, operational efficiency, support burden reduction, revenue enabled, regulatory compliance achieved. Outcome measures are the primary success criteria in Firmitas. They answer the question that justifies the engineering investment: did what was built produce the value it was supposed to produce?

Outcome measures are harder to collect than output measures. They are noisier. Their attribution is less clear — many factors beyond engineering quality determine whether a product is adopted. They are often lagging — the outcome of a design decision may not be visible for months after the decision was made. These properties make them less satisfying as management instruments than output measures, which is why organisations consistently default to outputs.

But the difficulty of outcome measurement does not make it optional. The organisation that measures only outputs and claims to be delivering outcomes is measuring the wrong thing and drawing the wrong conclusions. The programme that delivers its features on time and within budget, to a specification that the customer cannot use in the way the customer needs, has produced outputs and failed to produce outcomes.

Firmitas accepts imperfect outcome measures over precise output measures. A rough measure of customer adoption is more useful than a precise measure of feature throughput — because the adoption measure is trying to answer the right question, even imperfectly, while the throughput measure is answering a question that is not the right one with apparent precision.

**System health measures** describe the capability of the engineering system to continue delivering outcomes over time — whether the conditions that make good delivery possible are present and being maintained. System health measures include defect escape rates, lead time variability, incident recurrence, technical debt trends, team cognitive load indicators, and staff retention and engagement.

System health measures are the most important class of measure for long-term programme governance and the most consistently neglected. They are neglected because they measure conditions rather than outputs — the capability to continue delivering rather than the delivery that has occurred. Their consequences appear slowly and their causes are separated from their effects by delays that make attribution difficult.

The organisation that ignores system health measures may maintain strong output metrics right up to the point at which the health of the underlying system collapses — when the technical debt accumulated over many delivery cycles makes new development prohibitively expensive, when the team that maintained the product's institutional knowledge departs, when the architecture that was never refactored becomes too brittle to change safely. The system health measures would have signalled the approaching collapse months or years earlier. The output measures would have shown green throughout.

---

## The connection to the diagnostic dimensions

The measurement framework connects directly to the six diagnostic dimensions in Chapter 25. Each dimension has a corresponding measurement focus that reveals whether the dimension is healthy or degraded.

**Dimension 1 — Commitments and planning** is measured by the accuracy of three-point estimates over time. Not whether individual estimates prove correct — that is not a useful measure. Whether the most likely case is consistently more accurate than the best case, and whether the conditions attached to estimates are consistently assessed for accuracy after programmes complete. An organisation that consistently achieves best-case outcomes has either very good fortune or a governance culture that manages the conditions the best case requires. An organisation that consistently achieves worst-case outcomes has a systematic risk management failure that the measurement should surface.

**Dimension 2 — Requirements** is measured by the phase in which requirements gaps are discovered. Requirements gaps discovered during specification cost hours to resolve. The same gaps discovered during integration cost days. Discovered during acceptance testing, they cost weeks. Discovered in the field, they cost the customer relationship. An organisation that consistently discovers requirements gaps late is investing insufficiently in specification quality. The measurement of defect escape rate by originating phase — where each defect was introduced versus where it was found — is the most revealing requirements quality measure available.

**Dimension 3 — Knowledge and capability** is measured by the rate at which the programme's performance changes when key people leave or join. A programme whose delivery performance is stable through personnel changes has institutionalised its knowledge adequately. A programme that experiences significant degradation when specific individuals leave is carrying knowledge risk that the measurement should surface as a system health signal.

**Dimension 4 — Delivery and operations** is measured by operational incident rates, mean time to recovery, and the proportion of incidents that could have been anticipated during design or development. A system that generates frequent incidents of types that should have been designed out has operational quality gaps that the measurement should surface as delivery quality signals rather than operational performance signals.

**Dimension 5 — Leadership and governance** is measured by decision latency — how long it takes for an escalated risk or issue to receive a governance decision — and by decision accuracy — whether the decisions made at governance reviews prove correct in retrospect. Decision latency measures whether the governance layer is accessible and responsive. Decision accuracy measures whether the governance layer has the information and understanding to make decisions that improve programme outcomes rather than simply confirming the programme narrative.

**Dimension 6 — Culture and psychological safety** is measured by the gap between formal and informal risk assessments. When the risk register contains risks that engineers do not regard as the programme's real risks, the measure of that gap reveals the extent to which the governance culture has made honest risk disclosure unsafe. This measure is not easily collected through dashboards. It requires deliberate leadership effort — the specific practice of asking engineers what they would say about the programme's risks if they were not being formally reported.

---

## What Firmitas explicitly does not measure

The explicit rejection of certain measurement practices is as important as the endorsement of others. Measures that consistently distort behaviour and degrade the conditions the framework requires should be named and avoided.

**Individual performance metrics for engineers.** Measuring individual engineers on defect rates, code output, feature throughput, or story points produced creates the conditions for the behaviour those metrics reward — and penalises the behaviours the framework requires. The engineer who takes time to understand a requirement properly before implementing it will appear slower than the engineer who implements immediately and fixes defects later. The engineer who surfaces a risk honestly will appear to be the source of programme problems rather than the person managing them. Individual performance metrics for engineers consistently reward the appearance of productivity over the substance of quality, and punish the honesty the framework depends on.

**Velocity as a commitment basis.** Using sprint velocity as the basis for release date commitments transforms a tool that is supposed to help teams understand their capacity into a rod for their backs. Velocity that is used for commitments will be gamed — not through dishonesty but through the rational adaptation to an environment that requires velocity to be high to avoid the consequences of low velocity. The gaming produces inflated velocity measurements that are used to generate unrealistic commitments that fail in the ways Chapter 1 describes, at the sprint level rather than the programme level.

**Utilisation rates as efficiency measures.** Chapter 12 addressed utilisation in detail. The organisation that measures team utilisation as a primary efficiency indicator will drive teams toward full utilisation — and toward the fragility, quality degradation, and learning failure that full utilisation produces. Utilisation is a local measure that, when optimised, consistently degrades global outcomes. It should not be used as a primary governance metric.

**Maturity model scores as achievement indicators.** The maturity model in Chapter 25 describes stages of adoption as a developmental framework — a way of understanding where the organisation is and what it needs to develop further. When maturity model scores become performance indicators — when teams or programmes are assessed on their maturity level — the scores will improve without the underlying capability improving. Teams will learn to answer the maturity assessment questions correctly without changing the governance behaviour the questions are supposed to reveal. The diagnostic and maturity tools become compliance exercises rather than learning instruments.

---

## Measurement review cadence

Different measures reveal different aspects of programme and organisational health and are most useful at different cadences.

**Operational reviews** are short-cadence reviews — weekly or fortnightly — focused on the leading indicators that reveal near-term risk and enable early intervention. Queue length trends. Escalated risk item counts. Blocked work items. Integration test failure rates. These are the measures that allow the programme management layer to identify emerging problems before they become governance escalations.

**Programme reviews** are medium-cadence reviews — monthly or at programme phase transitions — focused on the system health measures that reveal whether the programme is sustainable. Defect escape rates. Rework levels. Technical debt trends. Lead time variability. Capability gap status. These are the measures that allow the governance layer to assess whether the programme is maintaining the conditions for continued delivery.

**Portfolio reviews** are longer-cadence reviews — quarterly or at portfolio reprioritsation points — focused on outcome measures that reveal whether the portfolio's engineering investments are producing the business outcomes they were supposed to produce. Customer adoption rates. Operational performance improvements. Revenue enabled by delivered capability. These are the measures that allow the portfolio governance layer to assess whether the investment portfolio is aligned with the business strategy it is supposed to serve.

The governance failure is in using the wrong cadence for the wrong measure — reviewing outcome measures at operational cadence (which produces noise rather than signal, because outcomes lag activity by months), or reviewing operational measures at portfolio cadence (which misses the early signals that require immediate response).

---

## The governance principle for measurement

Measurement in Firmitas serves learning, not control.

Measures that exist to demonstrate that the programme is on track — that are designed to show green, that are reviewed by governance layers to receive reassurance that delivery is proceeding — are not learning instruments. They are comfort instruments. They produce the same governance blindspot that the programme in Chapter 1 exhibited: a governance layer reading a mostly-green status report while the programme is accumulating risk that the status report is not designed to reveal.

Measures that exist to surface the conditions the programme depends on, to reveal where the system is under stress, and to provide the early warning that allows governance decisions to be made while options still exist — these are learning instruments. They make reality visible. They create discomfort in proportion to the health problems they reveal. They generate the governance conversations that prevent the programme failures they anticipate.

The governance layer that evaluates its measurement system by whether the measures make it comfortable is not governing. It is being governed by its own comfort preferences. The governance layer that evaluates its measurement system by whether the measures reveal what it needs to know to make good decisions is governing — even when what it needs to know is uncomfortable.

Measurement is in service of governance. Governance is in service of outcomes. Outcomes are what the programme exists to produce. The measurement system that reveals whether outcomes are being produced, and what system conditions are enabling or preventing them, is the measurement system the framework requires.

Everything else is the appearance of management.
