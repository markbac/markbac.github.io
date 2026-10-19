---
title: "Chapter 1: The Programme That Failed Predictably"
---

# Chapter 1: The Programme That Failed Predictably

The contract was signed on a Tuesday in October.

The client needed a complex integrated product - hardware, firmware, and software working together - delivered within fourteen months. The budget was fixed. The penalty clauses were standard. The account team had worked hard to win the business and the commercial director had committed to a date that made the business case work.

Nobody had spoken to the engineering team before the contract was signed.

That is not unusual. In most organisations, the sequence runs: bid, win, commit, then tell engineering. The assumption embedded in that sequence - that engineering will find a way to deliver whatever has been sold - is so common that most people inside those organisations no longer notice it. It feels like the natural order of things. Sales sells. Engineering delivers. The gap between what was sold and what is deliverable is a problem for later.

Later, in this case, arrived at the end of week three.

---

The engineering team spent the first three weeks doing what good engineering teams do when handed a commitment they did not make. They read the contract. They mapped the requirements. They identified the unknowns. They produced an honest assessment of what the programme would actually take.

The lead systems engineer brought the assessment to the first programme review. It contained a three-point estimate: best case twelve months, most likely seventeen months, worst case twenty-two months. Attached to the estimate was a risk register. Fourteen items. Three rated red.

The first red item was the hardware-software interface. The specification existed but contained ambiguities that would require resolution with the client before firmware development could proceed meaningfully. Until those ambiguities were resolved, any firmware written against the current specification was written against assumptions that might prove wrong.

The second red item was a third-party software component the architecture depended on. It had not been evaluated against the programme's specific requirements. The supplier had confirmed it was suitable. The engineering team had not yet been able to verify that claim independently.

The third red item was the test environment. The programme required a hardware-representative test environment to validate the integrated system. Procuring, building, and qualifying that environment would take time. Until it existed, integration testing would be delayed - and integration testing was where the real risks in this kind of programme almost always surfaced.

The lead systems engineer presented all of this clearly. The three red items were not hypothetical concerns. They were specific, named, bounded risks, each with a defined impact on the delivery estimate and a defined window within which a decision or action could prevent that impact from materialising.

The programme board noted the risks. They asked for mitigation plans. They confirmed the delivery date was unchanged.

The programme moved on to a review of task status.

---

By month four, the hardware-software interface ambiguities had not been resolved. Two rounds of correspondence with the client had produced clarifying questions rather than answers. The firmware team had made the only rational response to sustained ambiguity - they had written against their best interpretation of the specification. That interpretation would later turn out to be wrong in three places. The rework cost six weeks.

The third-party software component had been evaluated. It was not suitable as specified. It could be made suitable with modifications, but the supplier's timeline for those modifications was longer than the programme could absorb. The architecture required a redesign. The team identified a viable alternative in week eighteen. Implementing it took four weeks and required changes to elements of the system that had already been completed and tested.

The test environment was procured in month five. Qualification took longer than expected. It was available for integration testing in month seven. By that point the programme was carrying risks that had been visible since week three, accumulating since month one, and never resolved - because the decisions required to resolve them had never been made.

At month six the programme manager told the client there would be a delay. The revised delivery date was eight months beyond the original commitment. The client was not surprised. They had been watching the slow responses and the revised timelines accumulating in their inbox. They had suspected for some time that the programme was in difficulty.

The engineering team was not surprised either. They had known since week three.

The people who were surprised were the ones who had been reading the status reports.

---

The status reports had been mostly green. Task completion rates were tracking reasonably. The risk register had been mostly amber. Nothing in the formal programme reporting had indicated the scale of what was coming. The reporting had been technically accurate in a narrow sense - the tasks that were being tracked were being completed - but it had been describing a programme that existed on paper rather than the programme that existed in reality.

This is worth pausing on, because it is one of the most consistent patterns in engineering programme failure. The formal reporting system and the informal engineering reality had diverged at month one and continued to diverge throughout. Every engineer on the programme knew this. Most of the programme management layer knew it too, in the way that people know things they have chosen not to act on. Only the people at the top of the governance structure - the people with the authority to make the decisions the programme needed - were reading the green task status and the amber risk register and concluding that the programme was roughly on track.

The risk register had not lied to them. It had contained three red items since week three. But those three red items had been reviewed, noted, mitigations had been requested, and the conversation had moved on. The register had been used as a reporting artefact rather than a decision instrument. It had told the programme board what the risks were. The programme board had not treated that information as a set of decisions requiring owners, authority, and action. They had treated it as information to be noted. Noted and filed.

The window to change the outcome had been at week three. Not at month six when the delay was announced. Not at month four when the rework began. At week three, when a lead systems engineer put three specific, actionable risks in front of people who had the authority to act on them, and those people asked for mitigation plans and moved on to task status.

---

After the delay was announced, a lessons-learned exercise was commissioned.

It concluded that the programme had suffered from insufficient risk management, inadequate requirements definition, and a failure to escalate issues in a timely manner.

These conclusions were not wrong. But they were incomplete in a way that made them useless - and dangerous.

The risk register had contained three red items since week three. They had been reviewed at every programme board. They had not been acted on. That is not insufficient risk management. That is risk management that was present, visible, and systematically bypassed in favour of preserving a delivery date that had been set before anyone understood what the programme required.

The requirements had ambiguities that the engineering team had identified and flagged. The flags had been noted. The ambiguities had not been resolved. That is not inadequate requirements definition. That is a requirements problem that was known, named, and left unresolved because resolving it would have required a difficult conversation with the client at a moment when nobody wanted to have it.

The issues had been escalated. The lead systems engineer had put three red items in front of the programme board at the first review. The programme board had asked for mitigation plans, confirmed the delivery date, and moved on. That is not a failure to escalate. That is escalation that was received, acknowledged, and not acted upon.

The lessons-learned exercise produced a set of process improvements. New templates for risk registers. A revised escalation protocol. A requirement for more frequent programme reviews. These changes were implemented on the next programme.

The next programme failed in the same way.

---

What happened here was not unusual. The same sequence - honest assessment, noted risks, unchanged date, deferred decisions, accumulated failure, surprised senior management, blame distributed downward - plays out across engineering organisations in every sector, at every scale, with a consistency that suggests it is not a series of individual failures but a single systemic one.

The engineers on this programme were not incompetent. The programme manager was not negligent. The programme board members were not indifferent to the outcome. Everyone involved was doing what their system had shaped them to do. The engineers produced an honest assessment and flagged the risks because that was their job. The programme board noted the risks and moved on because that was what programme boards in their organisation did with risk registers. The commercial director held the date because dates in fixed-price contracts are not moved without significant commercial and reputational cost. The lessons-learned exercise blamed process rather than structure because blaming process produces recommendations that are easier to implement than the ones that would actually change the outcome.

Each individual in this story behaved rationally within the system they were in. The system produced a predictable failure. The failure was attributed to the individuals. The system was adjusted at the edges. The next programme began.

---

There is a variant of this pattern worth naming, because it produces an additional layer of cost that is rarely counted.

When an organisation delivers for a third party - a customer, a client under contract - the overrun carries a defined, bounded cost. Contractual penalties, reputational damage, a difficult client relationship. Real costs, but contained ones. The delivering organisation bears those costs and moves on. The failure is painful but it does not reach inside the business and damage its ability to operate.

When an organisation delivers a product or platform for its own use - building the infrastructure it needs to run as a business - the overrun hits twice. The first hit is the delivery overrun. The second is the operational consequence: every week the platform does not exist is a week the business operates on workarounds, on legacy systems, on manual processes, on capabilities it does not yet have. And when the platform eventually arrives - built under cost pressure, with risks deferred, with quality shortcuts taken to hit a date - it becomes the infrastructure the business depends on. The technical debt is not deferred to a future project. It is baked into the system that now runs the business. The cost of delivery decisions made under pressure becomes an ongoing operational cost that the project budget never captured and the lessons-learned exercise never measured.

Organisations delivering for their own use tend to feel the consequences of poor delivery more acutely for this reason. They take the full hit - delivery cost, operational lateness cost, and the long-term cost of what was built under pressure - with none of the insulation that the distance between a delivering organisation and an external client provides. That proximity to consequence can, when leadership is willing to act on it, create the conditions for more honest delivery governance. It does not always do so. The same failure patterns occur. But the cost of them is harder to ignore.

---

This book is about why programmes fail in the way this one did - and what it would take to build organisations where that failure pattern is no longer the default.

The answer is not better risk register templates. It is not more frequent programme reviews. It is not a revised escalation protocol. These are the responses of an organisation that has correctly identified the symptoms and incorrectly identified the cause.

The cause is structural. The people who made the decisions that determined the outcome of this programme were not the people who bore the consequences of those decisions. The commercial director who committed to the date did not write the firmware. The programme board members who filed the risk register did not spend six weeks on rework. The account team who won the contract did not spend month seven integrating a system in a test environment that should have been available in month two.

This separation - between the people who make delivery decisions and the people who live with the consequences of those decisions - is not an accident. It is the predictable product of how most engineering organisations are structured. Authority flows upward. Knowledge stays down. The people with the most accurate understanding of what a programme requires have the least authority to act on that understanding. The people with the most authority to act have the least visibility of what the programme actually needs.

Firmitas is built on the conviction that closing that gap - aligning the authority to make delivery decisions with the knowledge required to make them well - is the primary structural challenge of engineering programme governance. Everything else in this book follows from that conviction.

The next chapter examines the belief that most commonly prevents that gap from being closed: the assumption that engineers are being conservative, that their estimates are negotiating positions, and that pressure will extract the real number.

It is almost always wrong. Understanding why - and understanding the specific, measurable damage it causes - is where the structural argument begins.

---

*End of Chapter 1*
