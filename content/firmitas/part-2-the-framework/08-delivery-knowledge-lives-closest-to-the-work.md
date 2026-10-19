---
title: "Chapter 8: Delivery Knowledge Lives Closest to the Work"
---

# Chapter 8: Delivery Knowledge Lives Closest to the Work

The engineers on the programme in Chapter 1 knew what was wrong. They knew it at week three. They knew which risks were real, which assumptions were unsafe, and which decisions were required to change the outcome. They put that knowledge into a risk register and presented it to the people with the authority to act on it.

The people with the authority did not have the knowledge. The people with the knowledge did not have the authority. The gap between them is where the programme failed.

This is not an unusual configuration. It is the default configuration of most engineering programme governance. Authority flows upward through the organisational hierarchy. Knowledge stays down, with the people doing the work. The further up the hierarchy a decision travels, the further it moves from the operational reality that should inform it — and the closer it moves to the commercial, political, and organisational pressures that consistently distort it.

The principle that delivery knowledge lives closest to the work is not a statement about who is more capable or more intelligent. It is a structural observation about where accurate information about risk, timescale, and technical feasibility actually resides — and what the consequences are when governance systems route decisions away from that information rather than through it.

---

## Where delivery knowledge actually lives

Delivery knowledge is the accumulated understanding of what a specific programme requires — the technical constraints, the integration dependencies, the risk landscape, the realistic timescales, the architectural assumptions that will hold and the ones that will not. It is not generic engineering knowledge, though that is part of it. It is contextual knowledge about this programme, this system, these components, and these conditions.

This knowledge is held primarily by the engineers doing the work. Not because engineers are uniquely gifted, but because proximity to the work is what produces it. The firmware engineer who has been reading the hardware specification for three weeks knows where the ambiguities are. The systems integrator who has been evaluating the third-party component knows whether the supplier's claims are credible. The test engineer who has been designing the validation approach knows how long the test environment qualification will actually take.

This knowledge is specific, current, and perishable. It is specific to the programme and cannot be reliably transferred by summary or abstraction — a risk register entry that says "hardware-software interface ambiguity" contains a fraction of the knowledge held by the engineer who identified it. It is current in the sense that it changes as the programme develops, as new information arrives, as assumptions are tested and found wanting. It is perishable in the sense that it degrades rapidly when the person who holds it leaves the programme, is moved to another team, or stops volunteering it because the system has taught them that volunteering it is not worth the effort.

The governance layers above the engineering team hold different knowledge — commercial context, portfolio priorities, client relationship intelligence, regulatory and contractual obligations. This knowledge matters. It is not the same as delivery knowledge and it does not substitute for it. A governance layer that makes delivery decisions on the basis of commercial context and portfolio priorities without adequate delivery knowledge is not making informed decisions. It is making commercially-informed decisions in a delivery vacuum — which is precisely what produced the committed date that the engineering team was handed in Chapter 1.

---

## The decision authority problem

The gap between delivery knowledge and decision authority is structural. It is produced by the way engineering organisations are designed — with authority concentrated at the top of a hierarchy and knowledge concentrated at the bottom — and it is reinforced by a set of assumptions about what governance is for that make the gap feel normal rather than dysfunctional.

The assumption that governance should reside at the top of the hierarchy rests on the idea that governance is primarily about commercial accountability, strategic alignment, and risk ownership at an organisational level. These are legitimate governance concerns. But they are not the only governance concerns on an engineering programme. Operational governance — the decisions about how delivery proceeds, which risks require urgent action, whether the plan reflects reality — requires operational knowledge that senior governance layers frequently do not have.

When operational governance decisions are made by people without operational knowledge, the results are predictable. The risk register is reviewed without the ability to assess whether the mitigation plans are credible. The programme status is evaluated without the ability to assess whether the green task completion accurately reflects programme health. The delivery date is confirmed without the ability to assess whether the conditions required to achieve it are in place.

This is not incompetence. It is a structural mismatch — the wrong type of knowledge being applied to a class of decision that requires a different type of knowledge. And the mismatch is invisible to the people making the decisions, because they do not know what they do not know. The programme board in Chapter 1 confirmed the delivery date because nothing in the information presented to them told them clearly that confirming it was the wrong decision. The information was present. The operational understanding to interpret it was not.

---

## What genuine autonomy requires

The response to the decision authority problem is not to move all decisions downward. Some decisions — commercial commitments, portfolio priorities, strategic trade-offs, regulatory obligations — genuinely belong at a governance level that has the commercial and organisational context to make them well. The goal is not to dismantle governance. It is to align decision authority with the knowledge required to exercise it well.

This alignment looks different at different levels.

At the team level, it means that engineers and architects own the day-to-day and week-to-week decisions about how delivery proceeds. How the work is sequenced. Which technical approaches are pursued. How risks within the team's scope are managed. These decisions require the contextual knowledge that the team holds. They do not require commercial or strategic input on a routine basis. Requiring teams to seek approval for decisions that are within their technical competence and their scope of ownership adds latency without improving decision quality.

At the programme level, it means that programme governance focuses on the decisions that genuinely require programme-level authority — escalated risks that require resource or client engagement, trade-off decisions that span multiple teams or systems, gate decisions that represent genuine commitment points. It does not mean reviewing task completion status or second-guessing the technical decisions that the delivery team is better placed to make.

At the senior governance level, it means that executive and portfolio governance focuses on the decisions that require strategic, commercial, and regulatory authority — portfolio prioritisation, contractual commitments, major investment decisions, regulatory strategy. It maintains visibility of programme health through the risk and issues register rather than through task status reporting. And it creates the conditions for honest information to flow upward by ensuring that the governance culture treats bad news as useful information rather than as a performance failure.

The boundary between these levels is not rigid and will vary by programme type, scale, and regulatory context. What is rigid is the principle: decision authority should sit with the people who have the knowledge to exercise it well. Where that alignment does not exist, the governance system must be designed to create the information bridges that compensate — to ensure that the people making decisions have access to the knowledge they need, and that the people with the knowledge have access to the decision-making process.

---

## No micromanagement — no second-guessing

Genuine autonomy at the team level requires two specific commitments from the governance layers above it.

The first is the absence of micromanagement. Micromanagement is the substitution of a governance layer's operational preferences for the team's operational judgement on matters within the team's authority. It takes many forms: requiring teams to seek approval for decisions they have the authority and knowledge to make independently, questioning specific task sequencing in programme reviews, requesting justification for technical approaches that have been made through legitimate engineering process, adding resource to a team without that team's input because the programme appears to be running late.

Micromanagement is not always recognisable to the person doing it. It can feel like appropriate oversight, like quality control, like the exercise of legitimate programme authority. What distinguishes it from those things is that it substitutes the judgement of a person without operational knowledge for the judgement of a person with it — and in doing so, degrades rather than improves the quality of the decision while signalling to the team that their judgement is not trusted.

The cost of that signal compounds over time. A team that has learned that its operational decisions will be second-guessed stops making them with confidence. It starts seeking approval rather than exercising judgement. It starts managing upward rather than managing delivery. The autonomy that was supposed to produce faster, better-informed decisions produces slower, more conservative ones — because the team has adapted to a governance system that does not actually trust them to decide.

The second commitment is the absence of uninformed override. When a governance layer overrides a technical decision made by the delivery team, that override must be based on information or authority that the team did not have access to — a commercial constraint, a regulatory obligation, a portfolio-level trade-off. It must not be based on the preference of someone who has not read the technical assessment, does not have the contextual knowledge to evaluate it, and is substituting their seniority for the team's expertise.

Uninformed override is one of the most damaging governance behaviours in engineering programmes. It is damaging not just because it produces worse technical decisions — though it often does — but because of what it teaches the people it is applied to. The engineer whose technically-grounded recommendation is overridden by a governance decision based on commercial preference, without engagement with the technical reasoning, has learned that technical reasoning is not what governs decisions in this organisation. They will still produce technical assessments. But the assessments will be calibrated to what the governance layer wants to hear, not to what the technical reality requires.

---

## Gates approved without knowledge

There is a specific governance failure that deserves direct treatment because it is so common and so consequential: the gate review approved by people who do not have the knowledge to evaluate what they are approving.

Gate reviews are intended to be decision points — moments at which the programme's readiness to proceed to the next phase is assessed against defined criteria, and a genuine decision is made about whether to proceed, pause, or change direction. This is governance at its most valuable: a structured moment to verify that the programme is on a sound footing before making the commitments that the next phase requires.

In practice, gate reviews in most organisations are approval ceremonies. The programme team prepares a gate pack. The gate pack is reviewed by a governance body. The governance body approves the gate. The programme proceeds.

The approval is meaningful only if the governance body has the knowledge to evaluate whether the gate criteria have genuinely been met — whether the requirements are adequately defined, whether the architecture is sound, whether the risks are understood and managed, whether the estimates are honest and achievable. If the governance body lacks that knowledge — if it is evaluating the gate pack on the basis of whether it is complete and well-presented rather than on whether the programme is genuinely ready — the gate review is not a decision point. It is a formality that creates the appearance of governance assurance while providing none.

The gate approval without knowledge transfers risk downward without transferring understanding. The programme proceeds into the next phase carrying the risks that the gate was supposed to surface. When those risks materialise, the gate review provides the governance layer with a defence — we approved this, the criteria were met — while the delivery team carries the consequences.

Firmitas requires that gate reviews are genuine decision points — that the people approving gates have either the operational knowledge to evaluate readiness themselves or have been provided with the direct engineering input necessary to form an informed view. A gate approved on the basis of a well-prepared document pack by people who have not engaged with the engineering substance of what the gate is assessing is not governance. It is compliance theatre with consequences.

---

## The authority-experience gap in this context

Chapter 2 introduced the authority-experience gap — the structural condition in which the people with the most authority over delivery decisions have the least direct experience of what delivery requires. That gap is relevant here in a specific way.

The alignment of decision authority with delivery knowledge is harder to achieve in organisations where the governance layer has not experienced the conditions under which delivery happens. Not because people without direct engineering experience cannot govern engineering programmes — they can, and many do so effectively. But because the ability to recognise when a decision requires operational knowledge that you do not have, and to create the mechanisms to access that knowledge before deciding, requires a degree of self-awareness that is only available to people who know what they do not know.

The governance layer member who has personally written firmware against an ambiguous specification knows, viscerally, what the week-three risk register item means. They know how quickly ambiguity becomes rework, how the cost compounds when assumptions prove wrong at integration, how the window for a cheap fix closes faster than the programme schedule suggests. They do not need the risk register to tell them this is urgent. They know it is urgent.

The governance layer member who has not had that experience may read the same risk register entry with appropriate concern but without the operational reference point that converts concern into urgency. The ambiguity is noted. It is on the register. There is a mitigation plan. The governance process has been followed. The programme proceeds.

This is not a reason to exclude people without direct engineering experience from governance roles. It is a reason to design governance systems that do not depend on individual experiential knowledge to function correctly. The governance system should be designed so that the urgency of a risk is visible in the system — through the structure of the risk register, through the escalation mechanism, through the explicit connection between a risk and its impact on the programme plan — rather than dependent on the individual knowledge of the people reviewing it.

That is a system design requirement. And system design, as Chapter 7 established, is a leadership responsibility.

---

## The principle in practice

The principle that delivery knowledge lives closest to the work has a set of practical implications for how programmes are governed.

Teams own the day-to-day and week-to-week management of delivery. They sequence their own work, make their own technical decisions within defined architectural boundaries, manage their own risks within their authority level, and escalate only the items that require authority or resource they do not have. They are not required to justify routine operational decisions to governance layers that are not better placed to make them.

Programme governance focuses on escalated risks and issues, not on task status. The primary governance instrument is the risk and issues register, reviewed with the intent of generating decisions on escalated items. Task completion is visible to the programme management layer and is used to identify issues that should be escalated — it is not the primary instrument of senior governance.

Gate reviews are genuine decision points with defined criteria and genuine evaluation against those criteria. The governance body either has the operational knowledge to evaluate readiness or has direct engineering input that allows it to form an informed view. Gates are not approval ceremonies. They are decisions.

Decision boundaries are explicit. Teams know what they can decide independently, what requires consultation, and what is explicitly reserved for a higher authority level. Those boundaries are stable enough to trust and clear enough to apply without seeking clarification on routine matters. Where a decision genuinely spans boundaries — where its implications are broader than a single team's scope — there is a defined mechanism for bringing the relevant parties together rather than escalating upward through a hierarchy that may lack the knowledge to resolve it well.

---

## What changes when this is done well

The change is not dramatic. It does not involve new ceremonies or complex process redesign. It involves a shift in where attention is focused and what governance systems are designed to do.

Programme boards that focus on escalated risks and decisions rather than task status spend their time on the things that only they can resolve. The conversations are harder. They require decisions rather than acknowledgements. But the decisions are the right decisions — made by the right people, at the right time, with the right information — rather than the rubber-stamped approvals and noted risk items that the wrong governance model produces.

Engineering teams that are genuinely trusted to manage their own delivery behave differently. Not because they have been motivated by empowerment rhetoric — but because the system now makes honest behaviour rational. The estimate that will be accepted rather than compressed can be honest. The risk that will generate a decision rather than a note is worth escalating. The architectural concern that will be heard rather than overridden is worth raising clearly.

This is the connection between the governance principle in this chapter and the human system principle in Chapter 5's compounding cycle. Delivery knowledge reaches decisions when the governance system is designed to receive it. When it reaches decisions, the decisions improve. When the decisions improve, the programme outcomes improve. And when programme outcomes improve in ways that are attributable to the honest information the engineering team provided, the conditions for the next programme's honest information are better than they were for this one.

That virtuous cycle is available. It requires a governance system designed to produce it.
