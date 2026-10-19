---
title: "Appendix F: Leadership and Delivery Anti-Patterns Firmitas Is Designed to Prevent"
---

# Appendix F: Leadership and Delivery Anti-Patterns Firmitas Is Designed to Prevent

This appendix documents **common leadership, architectural, and delivery anti-patterns** that repeatedly undermine engineering organisations.

Firmitas does not exist to impose a new process.
It exists to **systematically prevent these failure modes** by design.

Each anti-pattern is described with:
- What it looks like
- Why it is harmful
- How Firmitas counters it

This appendix is intentionally direct.



## F.1 Leadership Anti-Patterns

### F.1.1 Proxy Leadership

**What it looks like**  
Leadership is replaced by frameworks, tools, or roles. Decisions are deferred to process rather than owned by leaders.

**Why it is harmful**  
- Responsibility becomes diluted  
- Teams lose clarity on intent  
- Governance becomes performative

**How Firmitas counters it**  
- Makes leadership a **non-delegable systems responsibility**  
- Frames frameworks as support, not substitutes  
- Forces explicit ownership of system health



### F.1.2 Hero Leadership

**What it looks like**  
Delivery relies on a small number of individuals working excessive hours to “save” projects.

**Why it is harmful**  
- Masks systemic failures  
- Creates fragility and burnout  
- Prevents learning

**How Firmitas counters it**  
- Explicitly protects slack  
- Treats heroics as system failure signals  
- Optimises for sustainable throughput



### F.1.3 Control Through Fear

**What it looks like**  
Metrics used to punish, audits used to intimidate, escalation used as threat.

**Why it is harmful**  
- Suppresses bad news  
- Delays risk discovery  
- Encourages gaming behaviour

**How Firmitas counters it**  
- Emphasises psychological safety  
- Separates learning metrics from performance judgement  
- Uses governance to guide, not punish



## F.2 Organisational and Governance Anti-Patterns

### F.2.1 Decision Bottlenecking

**What it looks like**  
All meaningful decisions flow through a small central group.

**Why it is harmful**  
- High decision latency  
- Reduced ownership  
- Local optimisation by avoidance

**How Firmitas counters it**  
- Uses architectural guardrails instead of approvals  
- Pushes decisions to the edge  
- Makes escalation rare and explicit



### F.2.2 Governance Theatre

**What it looks like**  
Reviews, gates, and documents exist primarily to demonstrate compliance rather than reduce risk.

**Why it is harmful**  
- Adds cost without value  
- Creates false confidence  
- Encourages box-ticking

**How Firmitas counters it**  
- Requires every artefact to have a clear purpose  
- Treats evidence generation as part of delivery  
- Optimises governance for risk reduction, not optics



### F.2.3 Tool-Led Transformation

**What it looks like**  
New tools are introduced as a substitute for fixing underlying system issues.

**Why it is harmful**  
- Increases cognitive load  
- Avoids real change  
- Creates superficial progress

**How Firmitas counters it**  
- Prioritises process consistency over tool uniformity  
- Treats tooling as a socio-technical choice  
- Forces justification of tools against outcomes



## F.3 Delivery and Process Anti-Patterns

### F.3.1 Cargo-Cult Agile

**What it looks like**  
Scrum ceremonies without autonomy, iterations without learning, backlogs without outcomes.

**Why it is harmful**  
- Creates motion without progress  
- Erodes trust in agile thinking  
- Hides systemic issues

**How Firmitas counters it**  
- Separates principles from practices  
- Anchors delivery to outcomes  
- Makes learning explicit



### F.3.2 Waterfall Disguised as Agile

**What it looks like**  
Upfront design and commitment with iterative labels applied later.

**Why it is harmful**  
- Late discovery of risk  
- False sense of adaptability  
- Costly rework

**How Firmitas counters it**  
- Enforces incremental validation  
- Encourages early integration  
- Treats assumptions as revisitable



### F.3.3 Output Obsession

**What it looks like**  
Success measured by features delivered, tickets closed, or utilisation maximised.

**Why it is harmful**  
- Disconnects work from value  
- Encourages overproduction  
- Increases WIP and delays feedback

**How Firmitas counters it**  
- Shifts focus to outcomes  
- Treats WIP as a system variable  
- Measures success through value realised



## F.4 Architectural Anti-Patterns

### F.4.1 Big Design Up Front (BDUF)

**What it looks like**  
Extensive upfront design attempting to eliminate uncertainty.

**Why it is harmful**  
- Assumes stability  
- Locks in poor assumptions  
- Delays learning

**How Firmitas counters it**  
- Assumes change by default  
- Uses evolutionary architecture  
- Preserves optionality



### F.4.2 Accidental Architecture

**What it looks like**  
Architecture emerges unintentionally from local decisions.

**Why it is harmful**  
- Hidden coupling  
- Inconsistent patterns  
- Long-term fragility

**How Firmitas counters it**  
- Makes architecture a leadership concern  
- Uses ADRs to surface intent  
- Maintains architectural coherence



### F.4.3 Platform as Control

**What it looks like**  
Platforms impose constraints primarily to enforce compliance or control teams.

**Why it is harmful**  
- Increases friction  
- Reduces autonomy  
- Encourages workarounds

**How Firmitas counters it**  
- Defines platforms as enablement mechanisms  
- Measures platform success by team outcomes  
- Treats adoption as value-driven



## F.5 Quality and Risk Anti-Patterns

### F.5.1 Late Quality

**What it looks like**  
Testing and validation deferred to the end of delivery.

**Why it is harmful**  
- Amplifies cost of defects  
- Delays feedback  
- Creates blame cycles

**How Firmitas counters it**  
- Integrates V&V continuously  
- Shifts testing left  
- Treats quality as systemic



### F.5.2 Hidden Risk

**What it looks like**  
Risks known but unspoken due to fear or incentives.

**Why it is harmful**  
- Explodes late  
- Forces crisis response  
- Damages trust

**How Firmitas counters it**  
- Makes risk visibility explicit  
- Links risk to leadership responsibility  
- Normalises early escalation



### F.5.3 Zero-Slack Systems

**What it looks like**  
Teams run at full utilisation with no buffer.

**Why it is harmful**  
- Eliminates learning capacity  
- Turns small issues into crises  
- Guarantees burnout

**How Firmitas counters it**  
- Treats slack as a structural requirement  
- Plans capacity intentionally  
- Protects recovery and improvement time



## F.6 Cultural Anti-Patterns

### F.6.1 Blame-Oriented Postmortems

**What it looks like**  
Incidents framed around who failed rather than what failed.

**Why it is harmful**  
- Suppresses information  
- Prevents improvement  
- Encourages risk hiding

**How Firmitas counters it**  
- Enforces blameless reviews  
- Focuses on system conditions  
- Converts failure into learning



### F.6.2 Local Optimisation Culture

**What it looks like**  
Teams rewarded for local efficiency regardless of system impact.

**Why it is harmful**  
- Creates silos  
- Degrades end-to-end flow  
- Undermines collaboration

**How Firmitas counters it**  
- Optimises for whole-system outcomes  
- Aligns incentives to shared success  
- Makes dependencies visible



## F.7 Summary

Firmitas is intentionally designed to:
- Surface reality early
- Prevent silent failure modes
- Replace heroics with systems
- Trade false certainty for learning
- Optimise for long-term value

Anti-patterns do not disappear through good intentions.
They disappear when **systems are redesigned to make them impossible or expensive**.

That is the purpose of Firmitas.
