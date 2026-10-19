---
title: "Chapter 28: What Firmitas Cannot Fix"
---

# Chapter 28: What Firmitas Cannot Fix

A framework that cannot tell you when it is the wrong tool is not a framework. It is a belief system — one that attributes every failure to insufficient or incorrect application rather than to the possibility that the framework itself does not fit the problem.

This chapter is the honest limits chapter. It names the conditions under which Firmitas will not work, the organisations it is not for, and the failure modes that it cannot prevent even when applied sincerely and competently. Some of these limits are about scope — the framework addresses specific problems and not others. Some are about context — the framework's assumptions do not hold in every organisational environment. And some are about the framework's own self-referential tension — the risk that a framework arguing against methodology-first thinking will itself be adopted as a methodology.

Acknowledging these limits is not a disclaimer. It is the most credible thing this book can do. And it provides the reader with the tools to assess whether Firmitas is the right instrument for their specific situation, rather than applying it universally and discovering the limits the hard way.

---

## The organisations Firmitas is not for

**The very small startup without regulatory obligations.**

A team of five to fifteen people building a product quickly, without safety-critical obligations, without a regulated compliance framework, without the integration dependencies of a multi-discipline programme, and with a direct and fast feedback loop to the customers whose behaviour will determine whether the product succeeds — this team does not need Firmitas.

The structured foundations phase, the Requirement Breakdown Structure, the Architecture Decision Records, the risk register with trigger dates and named owners, the governance model with escalation thresholds and exception management — these are instruments designed for the complexity and consequence of programmes where the cost of getting things wrong is high, where the feedback loops are long, and where the integration dependencies between disciplines make unstructured development expensive.

For a startup at early stage, the cost of those instruments exceeds the cost of the problems they prevent. The product will iterate rapidly. The requirements will change faster than a formal specification process can accommodate. The architecture will evolve faster than ADRs can capture. The risk register will lag the reality of a team that is discovering its product-market fit in weeks rather than months.

The philosophy of Firmitas applies — outcomes over outputs, delivery knowledge closest to the work, honest estimation, customer line of sight. But the framework overhead does not. Applying the full Firmitas governance model to a five-person startup is not discipline. It is the imposition of a structure designed for programmes of fifty that will slow the team down without protecting anything that needs protecting at this scale.

The practical test: does the programme involve multiple disciplines with incommensurable cadences, a regulated compliance framework, safety obligations, or integration dependencies that require coordination across organisational boundaries? If not, the philosophy applies but the framework overhead probably does not.

**Organisations where the primary obstacle is political unwillingness rather than structural ignorance.**

Firmitas can help a willing organisation build better systems. It cannot make an unwilling one want to.

The organisations where the primary obstacle to better delivery is not structural — not the governance model, not the estimation practices, not the risk management discipline — but political, are organisations where people with power benefit from the current dysfunction and have no incentive to change it.

The commercial director whose authority depends on making commitments before engineering has been consulted. The programme director whose governance role exists because decisions are centralised rather than distributed to the people with delivery knowledge. The organisational layer that exists to provide oversight of engineering teams whose performance would improve if the oversight layer's intervention were reduced.

Each of these people is behaving rationally within a system that has structured their incentives in a particular direction. Firmitas does not restructure those incentives. It assumes a leadership layer that is willing to govern differently — to accept honest estimates, to manage risks rather than note them, to attribute accountability accurately. Where that willingness does not exist at the level of authority required to make the changes the framework requires, the framework cannot achieve what it is designed for.

The practical test: do the people with the authority to change the governance behaviour have the incentive to change it? If the answer is no — if the current governance structure serves the interests of the people with the authority to change it — the framework will be adopted in form and rejected in substance, producing the cargo cult governance described in Chapter 26.

**The very large multinational with structurally separated decision authority.**

In organisations of sufficient scale and complexity, decision authority may be structurally separated from delivery knowledge in ways that no single leader within the organisation can change. Procurement frameworks that mandate specific delivery methodologies contractually. Matrix management structures that diffuse ownership so completely that no one person can be held accountable for the conditions of any specific programme. Portfolio governance imposed by a parent organisation with its own standards and incentive structures that are not aligned with the Firmitas model.

In these environments, a willing leader can apply Firmitas principles within their own sphere of authority — their team, their programme, their immediate governance perimeter. They cannot apply it systemically without organisational change that exceeds their authority. The localised application can produce localised improvement. The systemic change that would compound those improvements across the organisation may simply not be available as an option for any individual within it.

The practical test: does the leader with the authority to adopt Firmitas have the authority to change the governance structures that the framework requires? If the answer is no — if the relevant governance structures are determined by levels of the organisation above the leader's authority — the adoption will be partial at best.

**Compartmentalised environments where information flow is deliberately restricted.**

In certain defence, intelligence, and security programmes, the information flows that Firmitas depends on are deliberately constrained by security and classification requirements that are non-negotiable.

Firmitas requires that delivery knowledge reaches decision-makers. It requires that customer reality informs engineering decisions. It requires that risk information flows honestly through the governance structure. It requires that the reasoning behind architectural decisions is preserved and accessible.

In programmes where the customer's operational context is classified, where the programme's scope cannot be fully described to the people implementing parts of it, where the rationale for certain requirements cannot be documented because the rationale is itself classified, and where the psychological safety of honest risk disclosure is complicated by need-to-know cultures that treat information about problems as sensitive — the framework's information flow assumptions do not hold.

Some elements of Firmitas apply in compartmentalised environments. Delivery knowledge should still reside with the people closest to the work. Governance should still act on risks rather than note them. Quality is still a system property. But significant parts of the framework assume information availability that classified programmes cannot provide. The practitioner in a compartmentalised environment must be honest about which framework elements require information flows that their security context prevents — and must not substitute assumption for the customer and operational context the framework requires without acknowledging the substitution as a risk.

---

### The conditions under which Firmitas fails even when applied sincerely

**When the programme inherits conditions it cannot change.**

Firmitas is designed for programmes that have the authority to establish their own governance model, their own delivery structure, and their own relationship between commitment and estimation. Some programmes begin with commitments already made, architectures already designed, teams already assembled, and commercial relationships already established in ways that constrain every subsequent decision.

A programme that inherits a reverse-engineered plan, an unvalidated architecture, a contractual commitment made without honest estimation, and a client relationship that was established on expectations the programme cannot meet is starting in the failure pattern that Firmitas is designed to prevent. It cannot undo those conditions by adopting the framework. It can apply the framework's disciplines to manage the conditions it has inherited — surfacing the risks honestly, managing what can be managed, limiting the accumulation of additional debt — but it cannot retroactively correct decisions made before it existed.

The framework is most effective when applied from the beginning of a programme, before commitments are made and before the architecture is established. Applied mid-programme to a programme that has already entered the failure pattern, it provides better governance of the remaining programme but cannot recover the damage done before it arrived.

**When adoption is treated as transformation rather than evolution.**

Firmitas adopted wholesale — rolled out across all programmes simultaneously, with all governance processes changed at once, with full framework compliance expected from the first day — will fail in the ways described in Chapter 25. Not because the framework is wrong but because the organisational system cannot absorb that rate of change without collapsing into compliance theatre.

The organisations that have improved their delivery governance sustainably have done so through progressive adoption — starting where conditions are most favourable, building evidence of better outcomes, and expanding adoption as the evidence produces the trust and the political support for wider change. This is slower than wholesale adoption. It is the only adoption that produces lasting change.

The leader who adopts Firmitas as a transformation programme — who announces framework adoption, introduces all the artefacts and governance processes simultaneously, and measures adoption by compliance with the new process requirements — is applying a process-first approach to a framework that is explicitly designed to resist process-first adoption.

**When the framework is used as a substitute for judgement rather than a support for it.**

Chapter 6 established that Firmitas is a philosophy that constrains a framework that constrains process. The framework provides structure for decision-making. It does not make decisions.

The governance layer that approves a gate because the framework's gate criteria appear to have been met, without exercising the judgement to assess whether the evidence behind those criteria is credible, has used the framework as a substitute for governance. The programme board that notes an escalated risk because the risk register format requires a governance response, without the judgement to assess whether the risk is being managed or merely being documented, has used the framework as a substitute for risk management.

The framework supports judgement by providing structure — the questions to ask, the evidence to require, the decision boundaries to respect. It does not replace judgement. An organisation that has adopted the framework's artefacts and processes while losing the leadership judgement that gives them purpose has not adopted Firmitas. It has produced an elaborate compliance structure that will fail in the ways Chapter 26 described — because the artefacts exist but the decisions they are supposed to generate are not being made.

---

### The self-referential tension

Firmitas argues against methodology-first thinking. It will be adopted as a methodology by a significant proportion of the organisations that encounter it. Not because those organisations are stupid or dishonest — but because methodology adoption is the default organisational response to delivery problems, and the book will be given to a programme manager who has been told to fix delivery and will reach for it the way they reach for every other framework.

The self-referential tension is real and cannot be fully resolved. A framework that argues against frameworks will be used as a framework. The philosophy layer is supposed to prevent this — by establishing the non-negotiables that constrain the process layer and by making the purpose of each element explicit. But philosophy layers are frequently skipped. They require more effort to engage with than process layers. They do not produce artefacts. They produce understanding, which takes longer and is harder to demonstrate than the completion of a template.

The defence against this misuse is named explicitly in Chapter 26 — the earliest warning signal is the shift from "are outcomes improving?" to "are we doing this correctly?" But the defence requires leaders who are watching for it. And the leaders who are most at risk of missing it are the ones who believe they are genuinely applying the framework rather than performing it.

The practical guidance: if the framework is producing governance artefacts more reliably than it is producing governance decisions, the philosophy has been lost. If the risk register is being reviewed more consistently than it is generating decisions, the review has become the purpose rather than the instrument. If the framework is being treated as something that can be adopted completely and then maintained through compliance monitoring, it has become a methodology.

The test is always the outcomes. Not whether the artefacts are complete, not whether the processes are being followed, not whether the framework has been adopted — but whether the governance decisions are better, the programme outcomes are more predictable, and the conditions for honest information flow are stronger than they were before. Those are the only measures of whether Firmitas is being applied or merely performed.

---

### What to do when the limits apply

The limits described in this chapter do not leave practitioners without options. They define the scope within which the options available within the framework apply, and identify when a different instrument is needed.

For the small startup: the philosophy applies without the framework overhead. Outcomes over outputs. Delivery knowledge closest to the work. Honest estimation within whatever lightweight structure supports it. The discipline is appropriate to the context. The overhead is not.

For the organisation where political unwillingness is the obstacle: the entry point is evidence, not argument. A single programme governed differently, producing better outcomes, is the most powerful political argument for change that exists. The framework cannot make unwilling organisations willing. Evidence can change what unwilling organisations believe is possible — and belief about what is possible is a precursor to willingness.

For the mid-programme rescue: apply what can be applied from the current position. Surface the risks honestly. Limit the accumulation of further debt. Make the gap between the committed plan and the honest estimate visible to the governance layer and manage it explicitly rather than silently. The framework cannot undo what has already been done. It can limit the compounding of it.

For the compartmentalised environment: apply the elements that the security context allows and be explicit about which elements cannot be applied and why. A partial application that is honest about its limits is more useful than a complete application that is not.

For the self-referential tension: there is no permanent resolution. There is only the repeated practice of asking whether the framework is producing outcomes or artefacts, whether governance is generating decisions or compliance records, and whether the engineering teams who know the most about the programme's real state believe the governance process is serving them or constraining them.

---

### The final honest acknowledgement

Firmitas, applied sincerely and competently in a receptive organisation with a willing leadership layer, will improve delivery outcomes. Not perfectly. Not without setbacks. Not in a linear progression from current state to ideal state. But the specific, preventable failure patterns described in Part One — the committed date that nobody verified was achievable, the risk register filed rather than acted on, the honest estimate suppressed in favour of the commercial narrative — will become less common. And when they do occur, the organisation will be more likely to identify the real cause and less likely to compound it with the wrong lesson.

That is the claim. It is a modest one compared to the claims most frameworks make. It is an honest one. And it is the only kind worth making.
