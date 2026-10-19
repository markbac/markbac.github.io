---
title: "Chapter 18: Communication, Information Flow, and Documentation"
---

# Chapter 18: Communication, Information Flow, and Documentation

The failure in Chapter 1 was, at its most fundamental level, a communication failure. Not in the interpersonal sense — the engineers communicated clearly. They produced a risk register that named three specific, actionable risks. They presented an honest three-point estimate. They described the conditions that the programme depended on. The communication was precise, timely, and accurate.

The failure was that the information did not move. It was produced, received, acknowledged, and stopped. The risk register existed in a document. The programme board had read the document. The information that the document contained — the specific decisions required, the windows within which those decisions needed to be made, the consequences of not making them — did not travel from the document into the governance process in a form that generated action.

This is the communication failure that engineering organisations most commonly experience: not the failure to produce information, but the failure to design systems in which information flows to the people who need to act on it, in a form they can act on, at a time when action is still possible.

Communication in Firmitas is a designed system, not an emergent by-product of good intentions or individual effort. How information is structured, how it is stored, how it travels between teams and governance layers, what format makes it actionable, and what cultural conditions determine whether it is received honestly — all of these are design decisions. They are as consequential as architectural decisions and as much a leadership responsibility as governance design.

---

## Communication is a system, not a skill

The most persistent misattribution in engineering programme communication is the treatment of communication failures as individual skill failures. When information does not reach the people who need it, the diagnosis is frequently "poor communication" — implying that someone did not communicate clearly enough, frequently enough, or to the right person.

This framing locates the problem in individuals and produces individual-level solutions: communication training, stakeholder management guidance, presentation skills workshops. It leaves the system that determined what information was produced, how it was structured, who it was sent to, and what happened when it arrived entirely unchanged.

People communicate as the system allows them to. If information is fragmented across disconnected tools, people share fragments. If the governance culture treats bad news as a performance failure, people share good news. If the only formal communication channel is the programme status report, people produce status reports that reflect what the programme board wants to see rather than what the programme needs them to know. If the risk register is treated as a filing obligation rather than a decision instrument, people file risks rather than surface them as urgent decisions.

The system determines what information is produced, how honestly it is presented, and whether it reaches the people who need to act on it. Changing communication outcomes requires changing the system, not coaching individuals to communicate differently within a system designed to prevent honest communication.

---

## Information that must flow

Not all information is equally important to programme outcomes. The information failures that most consistently damage programmes are failures in a specific set of information types — the ones that carry risk, drive decisions, and connect delivery reality to governance action.

**Intent and purpose.** Teams must understand why the work they are doing exists — what customer problem it solves, what business outcome it contributes to, what constraints define its boundaries. Intent is not a motivational nicety. It is the reference point that allows teams to make coherent decisions under uncertainty without escalating every question that the specification does not explicitly address. A team that understands intent can make good local decisions. A team that only understands specification cannot — because every situation the specification does not cover becomes either a blocker or an assumption.

Intent must be persistent, discoverable, and stable. Not communicated once in a project kick-off presentation that is forgotten before the second sprint. Embedded in the programme's living documentation in a form that new team members can find, existing team members can reference when priorities shift, and the programme board can use as a reference when commercial pressures create conflicting demands.

**Decisions and their rationale.** What was decided matters. Why it was decided matters more. The decision without its rationale is a constraint that cannot be evaluated — it can only be followed or violated. The decision with its rationale is a constraint that can be maintained when it is still valid and revised when it is not.

Architecture Decision Records, as described in Chapter 13, are the primary mechanism for decisions and their rationale in the technical domain. The same principle applies to programme-level decisions: the decision to accept a commercial risk, the decision to descope a feature, the decision to proceed through a gate despite an open issue. Every significant decision leaves a trace that includes not just what was decided but why, what alternatives were considered, and under what conditions the decision should be revisited.

**Risk and uncertainty.** Risk does not become dangerous when it exists. It becomes dangerous when it is hidden. The information that carries the most value in programme governance — and that the system most consistently prevents from flowing — is honest information about what the programme does not know, what assumptions it is relying on, and what could go wrong if those assumptions prove false.

The risk register, as described in Chapter 10, is the primary risk information instrument. But the risk register is only effective if the culture makes honest risk disclosure rational — if the system does not penalise the person who surfaces a risk, does not convert risks into evidence of poor performance, and does not treat the absence of visible risks as a measure of programme health. Psychological safety, addressed in Chapter 11, is the cultural condition that determines whether risk information flows honestly. Without it, the risk information that exists in engineers' heads is absent from the documents that governance relies on.

**State and reality.** The actual current state of the programme — which components are working, which are not, which integration assumptions have been validated, which remain unresolved — must be visible to the governance layer in a form that allows honest evaluation. Status reports that present the programme state optimistically, that resolve ambiguity in the direction of good news, that omit the information that would require difficult decisions, are not state information. They are programme theatre — the performance of progress rather than its reality.

Information that contradicts the plan is more valuable than information that confirms it. A system that makes contradictory information difficult to surface — because surfacing it threatens the programme narrative, creates governance conversations that nobody wants to have, or identifies the person who surfaces it with the problem they are surfacing — does not have a communication problem. It has a governance culture problem that presents as a communication problem.

---

## The story of what has been done

Chapter 4 identified organisational memory — the preservation of decisions, reasoning, and the story of why things were built as they were — as one of the most critical and most commonly lost forms of knowledge.

The story is what new team members cannot reconstruct from code and documentation alone. Not the decisions — ADRs capture those. Not the current state — the system itself captures that. The story connects the decisions and the state to the context in which they were made: the constraints that existed at the time, the alternatives that were considered, the pressures that shaped the choices, the things that were tried and did not work before the approach that was adopted.

Without the story, the next team makes decisions that appear locally rational but that repeat the reasoning of decisions already made — sometimes arriving at the same conclusion after wasted effort, sometimes arriving at a different one that violates a constraint they could not see because the story that explained it had been lost.

The story is preserved through the practices described in this chapter — the ADRs that capture not just the decision but its context, the documentation that lives alongside the code and evolves with it, the knowledge-sharing practices that distribute understanding across the team before it becomes the property of a single person. When a key person leaves, the story they carried should already be distributed. If it has not been, the programme has a knowledge risk that will surface as a cost when the next decision depends on understanding that can no longer be accessed.

---

## Asynchronous by default

Synchronous communication — meetings, calls, real-time conversations — does not scale. It requires all participants to be available simultaneously. It produces decisions and agreements that exist only in the memories of the participants unless someone records them. It creates communication dependencies that become scheduling dependencies, adding latency to the information flows that programmes depend on.

Firmitas strongly biases toward asynchronous communication, supported by living artefacts that carry the information in a form that is accessible to anyone who needs it, at the time they need it, without requiring a meeting to access it.

The preference is not absolute. Some communication genuinely requires synchronous interaction — conflict resolution, high-ambiguity alignment, incident response, the relationship repair conversations that text cannot adequately support. These are legitimate uses of synchronous communication. They are not the majority of the communication that engineering programmes require.

The majority of programme communication is informational: sharing the current state, documenting a decision, describing a technical approach, flagging a risk, explaining a constraint. All of this can be done asynchronously, in a form that is more precise, more durable, and more discoverable than the equivalent meeting. The meeting that produces a decision without a written record produces a decision that cannot be referenced, cannot be challenged, and cannot inform the next person who needs to understand the reasoning behind it.

Architecture Decision Records instead of architecture meetings. Written risk assessments instead of verbal risk discussions. Design documents reviewed through pull requests instead of design review meetings. These are not the elimination of communication. They are the substitution of communication forms that produce durable, discoverable artefacts for communication forms that produce ephemeral shared memories.

The cultural shift this requires is significant. Many organisations treat synchronous communication — meetings — as the primary evidence of communication happening. The meeting that produced no record produced communication that, for programme purposes, did not happen. Changing this norm requires leadership behaviour change as much as process change. Leaders who make decisions in meetings and do not record them are modelling the behaviour that makes asynchronous-first communication impossible.

---

## Documentation as a delivery enabler

Documentation fails in most organisations for systemic reasons, not because engineers are careless. The failures are predictable.

Documentation created to satisfy a governance gate — a gate pack, a design review document, a test plan written to pass a review — is created to satisfy the gate, not to be used. It is written for the reviewer, not the reader. By the time the programme enters the phase the document was supposed to support, the document no longer reflects the decisions that have been made since it was produced. It has drifted. Nobody updates it because the gate has been passed and the document has no further formal purpose. It becomes archaeology within months.

Large documents written upfront, assembled from the best current understanding of scope that exists before development begins, face a version of the same problem at larger scale. They reflect the programme as it was understood at the moment of their creation. The programme evolves. The documents do not evolve with it, because updating a large document requires a different workflow from the one the development team uses for everything else. It requires someone to remember that the document exists, to find it, to understand it, and to produce a revised version that does not break the references that other documents have to it. This is expensive enough that it reliably does not happen. The large document drifts from reality and eventually describes a programme that no longer exists.

Docs-as-code addresses both failure modes by treating documentation as an engineering artefact — version-controlled, reviewed through pull requests, stored alongside the code it describes, updated as part of the same workflow that updates the code. Documentation that is changed as part of the same pull request that changes the code it describes stays current without requiring a separate documentation workflow. Documentation that is reviewed through the same mechanisms as code benefits from the same review culture. Documentation that is stored in version control is traceable, attributable, and recoverable.

The core principle is not a technical one. It is a cultural one: documentation must live where the work lives. If the engineers and architects who know what decisions have been made, and why, and what the current state of the system is, do not own the documentation — if documentation is produced by a separate function, in a separate tool, on a separate workflow — the documentation will not reflect the engineers' knowledge. It will reflect a mediated version of it, filtered through the communication cost of the handoff, and drifting from reality at the rate at which the programme evolves faster than the documentation process can follow.

---

## Documentation types that matter

Firmitas deliberately limits the types of documentation it considers essential, focusing on the artefacts that carry decisions, reasoning, and state — rather than the artefacts that exist to satisfy compliance requirements that could be satisfied more efficiently by the former.

**Vision and intent.** Why the product exists, who it serves, what success looks like, and what the principal constraints are. Concise, narrative, stable. The reference point for teams making local decisions under uncertainty. Updated when the programme's fundamental purpose or constraints change, not when individual features change.

**Requirements and constraints.** The functional and non-functional requirements structured as described in Chapter 11, with traceability from customer need to acceptance criteria. Living artefacts — updated when requirements change, maintained with the same discipline as code.

**Architecture and design.** The structural shape of the system, captured through C4 diagrams at the appropriate level of abstraction, Interface Control Documents for the boundaries between components and disciplines, and Architecture Decision Records for the significant decisions that shaped the structure. Living artefacts — diagrams updated when the structure changes, ADRs written when decisions are made and superseded when they are revised.

**Verification and validation evidence.** Test plans, test results, traceability matrices, validation reports. Generated continuously through the iterative core, compiled into the formal evidence record during the validation phase. Not assembled for the audit — produced as the natural output of a quality engineering system that is functioning correctly.

**Operational documentation.** Deployment procedures, monitoring runbooks, incident response guides, support documentation. Produced with the involvement of the operations team, maintained by the teams who use them, updated when the operational reality changes. Documentation that the operations team cannot rely on is more dangerous than no documentation — it creates false confidence and is likely to fail at the moment it is most needed.

---

## Signals, noise, and information hygiene

More information is not better information. The programme that produces comprehensive status reports, detailed meeting minutes, exhaustive design documents, and complete audit trails for every decision creates an information environment in which the signals that matter are buried under the volume of information that exists because someone believed that documentation equalled governance.

Information hygiene is the practice of maintaining signal quality over volume — ensuring that the information the programme produces is meaningful, current, owned, and serves a specific purpose for a specific audience. Artefacts that no one reads should not exist. Documents that have drifted from reality should be updated or removed. Dashboards that show activity rather than health should be replaced by dashboards that show health.

The mechanisms of information hygiene are simple. Every artefact has a named owner who is responsible for its currency. Every artefact has an intended audience and a defined purpose. Every artefact that has become stale is either updated or explicitly archived. The programme review that surfaces artefacts that nobody reads is the prompt to remove them, not to continue maintaining them.

The cognitive load of navigating an information environment full of stale, redundant, and low-quality artefacts is not trivial. Engineers who cannot find the current interface specification because it exists in three versions in two tools and none of them is marked as the authoritative one spend time on archaeology rather than engineering. The cost is real. Information hygiene reduces it.

---

## Leadership's role in information flow

Leadership behaviour is the strongest determinant of whether information flows honestly in a programme. Not the documentation tools. Not the risk register format. Not the governance processes. The behaviour of the people at the top of the authority structure, and specifically how they respond when information arrives that is uncomfortable.

Leaders who punish bad news create programmes in which bad news arrives late. Not because engineers are hiding it maliciously, but because the system has taught them that the cost of surfacing bad news early — the attention, the scrutiny, the implication of failure — exceeds the cost of managing the problem quietly until it becomes unavoidable. By the time unavoidable arrives, the problem is larger, the options are fewer, and the cost of resolution is substantially higher than it would have been if the information had been surfaced at the first warning.

Leaders who reward bad news early — who treat early warning of a problem as valuable information rather than as a performance indicator, who respond to escalated risks with decisions rather than with questions about why the risk was not caught sooner — create programmes in which information flows toward the people who need to act on it. The risk register reflects the real risk landscape. The status reports describe the real programme state. The honest three-point estimate is used rather than suppressed.

This is not a management aspiration. It is a governance requirement. A programme governed on false information is not being governed at all. The governance layer that is reading a green status report and a mostly-amber risk register while the programme is carrying unresolved red items is not making informed decisions. It is making decisions in a vacuum created by the information environment the governance culture has produced.

The programme board in Chapter 1 did not lack information. It lacked the governance culture that would have treated the information it had as urgent rather than routine. That culture is a leadership product. It is designed, or it emerges by default from the behaviours that leadership models. Leadership that models the treatment of honest risk information as welcome rather than threatening produces organisations where honest information flows. Leadership that models the treatment of honest risk information as a problem to be managed produces organisations where the risk information that governs are the versions that have been sanitised to avoid uncomfortable conversations.

Communication is a system. Leadership designs the system. The system produces the information environment. The information environment determines the quality of the decisions. The quality of the decisions determines the programme's outcomes.

Design the system deliberately.
