---
title: "Chapter 10: Risk, Issues, and the Register That Actually Works"
---

# Chapter 10: Risk, Issues, and the Register That Actually Works

The risk register in Chapter 1 was not deficient. It contained the right information. The three red items were correctly identified, correctly rated, and correctly described. The engineering team had done exactly what a risk management process asks of them.

The register failed not because it was wrong but because the system it fed into was not designed to act on it. The information entered the governance process and stopped. It was noted, acknowledged, filed, and superseded by the task status review. The register had been designed to produce a document. It had not been designed to produce decisions.

This is the most common form of risk management failure in engineering programmes. Not the absence of a risk register. Not inaccurate risk identification. The presence of an accurate risk register that the governance system does not know how to use.

This chapter describes what a risk register that actually works looks like — how it is structured, how it is reviewed, how it generates decisions rather than acknowledgements, and what the governance model around it must look like for it to function as the management instrument it is supposed to be.

---

## The distinction between risks and issues

Before describing what a functional risk register looks like, it is necessary to establish a distinction that most risk registers blur and that most risk management processes treat as optional: the difference between a risk and an issue.

A risk is a condition that might occur and, if it does, would affect the programme's ability to deliver to its committed outcome. It has a probability — it may or may not materialise. It has a defined impact — if it materialises, this is what changes. And it has a window — a period within which action can prevent it from materialising or limit its impact if it does.

An issue is a condition that has already occurred and is already affecting the programme. It has no probability — it is not a future event but a present reality. It has a current impact that needs to be managed, not a potential impact that needs to be mitigated. And it has a resolution path — a set of actions that will return the programme to its intended trajectory or, if that is no longer achievable, a revised trajectory that reflects the current reality.

Confusing risks and issues produces a register that is difficult to act on. A risk that has already materialised is no longer a risk. Treating it as one — rating its probability, listing mitigation plans, keeping it in the risk register — obscures the fact that the programme is already carrying the consequence and needs a resolution response rather than a mitigation response. It also produces the specific failure pattern from Chapter 1, where risks that were never resolved gradually transitioned from potential problems to actual ones without the governance system ever formally acknowledging the transition.

Firmitas requires risks and issues to be managed as separate categories, with separate governance responses.

---

## What a risk entry must contain

A risk entry in a Firmitas risk register is not a description of something that might go wrong. It is a decision request — a structured statement of a condition that requires a governance response before a defined trigger date.

Each risk entry must contain six elements.

**A specific, named description.** Not "integration risk" or "third-party dependency risk." Those are categories, not risks. A risk entry must describe a specific condition with enough precision that someone who did not write it can understand exactly what might happen, why it would happen, and what the consequence would be. "The third-party firmware library has not been validated against the programme's NB-IoT profile requirements. If validation reveals non-compliance, the architecture will require a redesign estimated at four weeks, pushing the programme from most likely to worst case." That is a risk entry. It is specific. It is actionable. It connects directly to the programme estimate.

**A probability assessment.** Not a precise probability — engineering programmes do not admit that level of precision — but an honest characterisation of likelihood. High, medium, or low, with a brief rationale for the assessment. The rationale prevents probability ratings from drifting toward whatever makes the register look most comfortable. A risk rated low because it is genuinely unlikely is different from a risk rated low because rating it high would make a governance conversation difficult. The rationale makes the difference visible.

**An impact assessment.** What changes to the programme if this risk materialises. Specifically: what changes to the timeline, to the cost, to the scope, or to the quality of what is delivered. The impact assessment must be connected to the programme estimate — if this risk materialises, the most likely case becomes the worst case, or the best case becomes unachievable, or the delivery date moves by this many weeks for these reasons. Impact assessments that are not connected to the programme estimate are not useful for governance decisions.

**A named owner.** A specific person, not a team or a function, who is accountable for managing the risk. The owner is responsible for the mitigation actions, for monitoring the trigger conditions, and for escalating the risk when it transitions from manageable to critical. Risks without named owners are risks that nobody is managing. They persist on registers indefinitely, rated amber, until they materialise.

**A mitigation or response plan.** What actions are being taken to prevent the risk from materialising or to limit its impact if it does. The mitigation plan must be specific — named actions, named owners, defined timelines — not aspirational. "We will work closely with the supplier to ensure the component is suitable" is not a mitigation plan. "The technical lead will commission and complete an independent validation of the component against the programme's requirements by end of month two. If validation reveals non-compliance, the architecture team will begin assessment of alternative approaches immediately and present options to the programme board by end of week two of month three" is a mitigation plan.

**A trigger date or trigger condition.** The specific date or condition that will cause the risk to be escalated if it has not been resolved. The trigger date is the point at which the window for cheap resolution closes — after which either the risk has materialised or the actions required to prevent it are no longer available at the same cost. The trigger date must be connected to the programme timeline. If the third-party component validation is not complete by end of month two, the programme's ability to remain on the most likely timeline is compromised. That is the trigger date. At end of month two, if validation is not complete, the risk escalates automatically — not because the owner chooses to escalate it, but because the governance system is designed to escalate it.

---

## What an issue entry must contain

An issue entry has a different structure from a risk entry because it requires a different governance response.

An issue is a present reality, not a future possibility. It does not require mitigation — the condition has already occurred. It requires active management toward resolution.

Each issue entry must contain five elements.

**A specific description of what has occurred.** Not what might happen — what has happened, when it happened, and what its current impact on the programme is. "Software component integration testing commenced on day one of month five. Test failures have been identified in three interface behaviours that were assumed to be correctly implemented based on supplier documentation. The failures are preventing completion of integration testing and are blocking the firmware validation phase. Current impact: two weeks of delay to the integration testing schedule, with potential downstream impact on the system validation phase start date."

**The reason it occurred.** Not for blame — for learning and for informing the resolution approach. The reason the issue occurred usually reveals a gap in the programme's risk management, requirements definition, or governance that should be addressed to prevent similar issues. An issue that occurs because a risk was identified and not acted on is a different kind of issue from one that could not have been anticipated. Both require resolution. Only the first requires a governance reflection.

**A named owner with authority.** The person responsible for driving the issue to resolution. The owner must have the authority to take the actions the resolution requires — or must have an explicit escalation path to someone who does if resolution requires authority beyond their own.

**A resolution plan with actions and dates.** Specific actions, named owners for each action, and dates by which each action will be completed. The resolution plan is not a list of things that will be tried. It is a committed sequence of activities that will return the programme to its intended trajectory — or, if that is no longer achievable, will establish the revised trajectory and the governance decisions required to accept it.

**An impact statement on the programme plan.** What the issue means for the programme's delivery date, cost, and scope. The impact must be stated honestly — if the issue has moved the programme from the most likely case toward the worst case, that should be visible in the issue entry and should be reflected in a formal revision of the programme plan. Issues whose programme impact is not formally acknowledged produce the silent accumulation of delay that the programme in Chapter 1 experienced — where the formal plan remained unchanged while the real programme drifted progressively further from it.

---

## The register as a decision instrument

A risk and issues register designed as described above is a fundamentally different tool from the risk register in Chapter 1. It is not a document that records what might go wrong. It is a live management instrument that tracks the specific conditions the programme depends on and surfaces the decisions required to keep those conditions met.

For the register to function as a decision instrument, the governance process around it must be designed accordingly.

The register must be reviewed at a frequency matched to the pace of change in the programme. A monthly review of a register whose trigger dates are measured in weeks is not risk management. It is post-hoc documentation of things that have already happened. On active delivery programmes, the register should be reviewed weekly by the programme management layer and at every programme governance meeting by the governance layer. Items approaching their trigger dates should be flagged automatically — not at the next scheduled review, but when the trigger window opens.

The review must generate decisions. A risk register review that ends without decisions having been made on escalated items is not a review. It is an acknowledgement ceremony. The purpose of reviewing the register is not to confirm that the register has been updated. It is to make the decisions that the register is asking for. If a red item is in front of the programme board, the programme board meeting does not end until either a decision has been made or the decision has been explicitly deferred with a named owner, a rationale, and a date by which it will be made.

The register must be connected to the programme plan. When a risk materialises or an issue is opened, the programme plan must be updated to reflect the impact. The register and the plan are not separate documents. They are the same programme, represented at different levels of detail. A risk that has materialised and is not reflected in a revised plan is a programme that is being managed against a fiction.

---

## Management by exception — how senior management should use the register

The risk and issues register is the primary instrument through which senior management should govern a programme. Not task status. Not RAG reports. The register.

This is the governance principle that Chapter 1's programme board did not follow — and the one that would have produced a different outcome if they had.

Senior management's job is not to track task completion. Task completion is the delivery team's concern — the operational management of day-to-day and week-to-week delivery that belongs with the people who have the knowledge to manage it. Senior management's job is to manage the conditions under which tasks can be completed — to make the decisions that the delivery team cannot make within their own authority, to provide the resources and the client engagement and the cross-programme trade-offs that only the governance layer can resolve.

The risk and issues register surfaces exactly those things. Not the tasks being completed — the conditions being threatened. Not the activities in progress — the decisions required. The governance layer that reads the register correctly knows what it is being asked to do: make this decision, provide this resource, have this client conversation, resolve this dependency. The governance layer that ignores the register and reads the task status report instead knows what has been done. It has no view of what is at risk.

Management by exception means the governance layer acts on escalated items — items that have breached their trigger date without resolution, items whose impact has changed, items that require authority or resource the delivery team does not have — and trusts the delivery team to manage everything within their authority without interference.

For this to work, three things must be in place.

The exception threshold must be explicit. Teams must know which items automatically escalate to senior governance and which they own. An ambiguous threshold produces two failure modes: teams escalating everything to avoid accountability, or teams holding everything to avoid appearing incapable. Both undermine the governance model.

The governance response to escalated items must be timely. An item that escalates and sits without a governance response for two weeks is worse than one that was never escalated — it has consumed the team's attention, revealed the governance layer's inability to respond, and lost the time that a prompt decision would have preserved.

The governance layer must distinguish between escalated items and status reports. A programme review that begins with escalated risks and issues and generates decisions on each of them before moving to anything else is a functional governance meeting. A programme review that begins with a RAG dashboard and a milestone completion review and reaches the risk register as the final agenda item — if it reaches it at all — is a programme review that has been designed around the wrong information.

The principle, stated plainly: senior management governs programmes through risks and issues, not through task status. A programme review that spends more time on task status than on risks and issues has inverted its governance model. The question is not whether tasks are being done. The question is whether the conditions for doing them exist — and that question is answered by the risk register, not the Gantt chart.

---

## The software component running late

One of the most common issue types on engineering programmes is a software or firmware component that is running behind schedule. It is worth addressing directly because it illustrates how the risk and issues distinction operates in practice and what the governance response should look like.

A component running late is not a risk. By the time it is visible as a delay, it is an issue — something that has already occurred and is already affecting the programme. It must be entered as an issue, not as a risk, and it must be managed with the governance response that issues require.

What the governance layer needs to know is not that the component is late. It needs to know why it is late, what the resolution plan is, what the impact on the programme plan is, and what decisions are required from the governance layer to support the resolution.

Why it is late matters because the reason determines the response. A component running late because the requirements were ambiguous is a requirements management failure that may have implications for other components being developed against the same requirements. A component running late because an external dependency has not been resolved is a dependency management failure that requires escalation to whoever owns the dependency. A component running late because the original estimate did not adequately account for the scope requires the governance layer to review other estimates developed under similar conditions. A component running late because the engineer responsible is overloaded is a resourcing failure that requires an immediate governance decision about capacity.

Each of these causes requires a different response. The governance layer that receives "the component is two weeks late" without the reason, the resolution plan, and the impact statement cannot make the decision the situation requires. It can only express concern and request updates — which is what the programme board in Chapter 1 was reduced to, repeatedly, by a governance system that gave it insufficient information to act.

The resolution plan must be specific. Named actions, named owners, defined dates. If additional resource is needed, the request must be explicit and the governance decision to provide or decline it must be made at the governance level, not deferred back to the delivery team to resolve within their own means.

The impact on the programme plan must be stated honestly and immediately. If the component running late will push the integration phase back by three weeks, the programme plan shows that now — not at the next monthly review, not when other slippage can no longer be used to absorb the delay, now. A programme plan that does not reflect known delays is a fiction. A governance layer managing against a fiction cannot make real decisions.

---

## The register in a regulated environment

In programmes operating under formal safety or quality standards — IEC 62304, IEC 61508, ISO 9001, DO-178C, and their sector-specific equivalents — the risk register carries formal evidence obligations. Evidence of risk identification, assessment, and management is required by most safety-critical and quality management standards, and that evidence must be demonstrable to auditors and certifying bodies.

The functional risk register described in this chapter satisfies these obligations more thoroughly than a compliance-driven one, because it generates evidence naturally through its operation rather than assembling it retrospectively for audit purposes.

A risk entry with a specific description, probability and impact assessment, named owner, mitigation plan with dates, and trigger date is evidence-rich by design. When it is reviewed, the review generates a record. When a decision is made, the decision is documented. When a risk transitions to an issue, the transition and the reason are recorded. When an issue is resolved, the resolution actions and their outcomes are recorded. The register's operational lifecycle produces the audit trail that compliance requires as a natural by-product of its function.

This is the Firmitas position on compliance documentation generally: evidence should be generated by a system that is functioning correctly, not assembled by a system that is functioning incorrectly and needs to appear compliant. A risk register that generates decisions and manages programme risk will produce better compliance evidence than one that produces formatted documents for governance meetings. The compliance follows the function. It does not substitute for it.

---

## What the week-three meeting looks like with a functional register

Return to the programme board at week three in Chapter 1. The same estimate has been presented. The same three red items are on the register. The difference is that the register has been designed as a decision instrument and the governance process has been designed to use it as one.

The programme board does not note the three red items. It addresses them.

Red item one — hardware-software interface ambiguity — has a trigger date of end of week five. If the ambiguity is not resolved by then, the firmware development that has been proceeding against current assumptions will require rework, and the programme will move from the most likely timeline toward the worst case. The decision required: who will have the resolution conversation with the client, and by when? The programme director accepts ownership. The conversation will be initiated within five working days. The trigger date stands at end of week five. If resolution is not achieved, the programme board will be convened for a rebaseline review.

Red item two — third-party component validation — has a trigger date of end of month two. Independent validation must be completed by then to allow the architecture to proceed on its current assumptions. The decision required: who will commission the validation and what is the budget? The technical director accepts ownership. The budget is approved at the current meeting. The validation will be commissioned within the week. The trigger date stands at end of month two.

Red item three — test environment procurement — has a trigger date of end of week four, after which the procurement lead time will make the required availability date of month three unachievable. The decision required: who will approve early procurement and what is the budget? The procurement approval is made at the current meeting. The order will be placed within five working days.

The meeting ends. Three red items. Three decisions. Three owners. Three deadlines. Not noted. Addressed.

The programme that follows is not guaranteed to succeed. The client may not resolve the interface ambiguity quickly. The component may still prove unsuitable. But each of those outcomes will be known earlier, when the options for responding are still available at a manageable cost. And the programme will be managed against reality rather than against a plan that has already diverged from it.

That is what a risk register that actually works produces. Not certainty. The conditions under which programme governance can do its job.
