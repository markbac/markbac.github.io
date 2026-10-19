---
title: "Appendix D: Minimal, Balanced, and Regulated Firmitas Profiles"
---

# Appendix D: Minimal, Balanced, and Regulated Firmitas Profiles

This appendix defines **three canonical Firmitas profiles**.  
They are not maturity levels and not prescriptive methodologies.  
They are **intentional configurations** of the same philosophy and framework, tuned to different organisational, product, and regulatory contexts.

Firmitas is deliberately designed to scale **both up and down** without changing its core principles.

The profiles differ in:
- Degree of formality
- Depth of artefacts
- Governance intensity
- Validation rigor
- Regulatory alignment

They do **not** differ in philosophy.



## D.1 Why Profiles Exist

A common failure mode in engineering frameworks is assuming one “correct” level of process.

Firmitas explicitly rejects this.

Instead, it recognises that:
- Over-structure kills speed and learning in small systems
- Under-structure kills safety, trust, and predictability in complex or regulated systems
- The *same organisation* may need different profiles for different products

Profiles exist to:
- Reduce cognitive overhead when tailoring
- Prevent accidental over- or under-engineering
- Make trade-offs explicit rather than implicit



## D.2 Profile Overview

| Dimension | Minimal | Balanced | Regulated |
||--|-|--|
| Primary Goal | Speed & learning | Sustainable delivery | Safety, assurance & compliance |
| Typical Context | Startups, internal tools | Scale-ups, IoT, SaaS | Medical, automotive, defence |
| Governance | Principles only | Lightweight gates | Formal gates & reviews |
| Documentation | Minimal viable | Living, structured | Comprehensive & auditable |
| Validation | Continuous, informal | Continuous + formal | Formal V&V + audits |
| Traceability | Implicit | Selective | Mandatory |
| Slack | Explicit but informal | Explicit & planned | Explicit & governed |



## D.3 Minimal Firmitas Profile

### D.3.1 Intended Context

Minimal Firmitas is appropriate where:
- Teams are small and highly collaborative
- Risk of harm is low
- Regulatory burden is minimal
- Speed of learning outweighs predictability

Typical examples:
- Early-stage startups
- Internal business tools
- Early product discovery phases
- Prototypes and pilots



### D.3.2 Core Characteristics

Minimal Firmitas emphasises:
- Fast feedback
- Low ceremony
- High trust
- Direct communication

Governance exists primarily through **shared understanding**, not artefacts.



### D.3.3 Artefact Set (Minimal)

Required:
- Vision Brief (1–2 pages)
- Lightweight backlog
- ADRs for irreversible decisions only

Optional:
- High-level architecture diagram
- Risk list (informal)
- Delivery health check (occasional)

Explicitly avoided:
- Heavy traceability matrices
- Formal stage gates
- Detailed upfront specifications



### D.3.4 Validation & Quality

- Continuous testing embedded in development
- Informal acceptance based on outcomes
- Peer review over formal sign-off
- Quality is owned by the team, not a function



### D.3.5 Risks and Failure Modes

Common risks:
- Accidental architectural drift
- Hidden technical debt
- Implicit decisions becoming permanent

Mitigations:
- Regular architectural conversations
- Periodic “decision archaeology”
- Explicit slack for refactoring and learning



## D.4 Balanced Firmitas Profile

### D.4.1 Intended Context

Balanced Firmitas is the **default profile**.

It fits contexts where:
- Products are customer-facing
- Multiple teams or disciplines are involved
- Some regulatory or contractual obligations exist
- Long-term maintainability matters

Typical examples:
- IoT platforms
- Commercial SaaS
- Embedded products
- Regulated but non-safety-critical systems



### D.4.2 Core Characteristics

Balanced Firmitas balances:
- Speed with predictability
- Autonomy with coherence
- Learning with accountability

Governance is **visible but lightweight**.



### D.4.3 Artefact Set (Balanced)

Required:
- Vision Brief
- System-level requirements
- Architecture overview (C4 context/container)
- ADRs for significant decisions
- Risk register
- Delivery health checks

Optional:
- RFCs for complex changes
- Selective traceability (RTM where it adds value)
- Formal test plans for critical paths



### D.4.4 Validation & Quality

- Continuous integration and automated testing
- Defined acceptance criteria
- Regular system-level validation
- Quality engineering embedded, not siloed



## D.4.5 Governance Model

- Lightweight transition gates at major lifecycle boundaries
- Architectural guardrails instead of approvals
- Exceptions discussed openly, not hidden



### D.4.6 Risks and Failure Modes

Common risks:
- Gradual process creep
- Tool-driven rather than outcome-driven behaviour
- Governance becoming implicit again

Mitigations:
- Periodic governance reviews
- Explicit removal of low-value artefacts
- Leadership ownership of system health



## D.5 Regulated Firmitas Profile

### D.5.1 Intended Context

Regulated Firmitas applies where:
- Failure can cause harm
- Compliance is mandatory
- External audits are expected
- Traceability is non-negotiable

Typical examples:
- Medical devices
- Automotive systems
- Aerospace and defence
- Energy and critical infrastructure



### D.5.2 Core Characteristics

Regulated Firmitas:
- Preserves learning and iteration
- Adds formality where risk demands it
- Treats compliance as a design constraint, not an afterthought

It is **not waterfall**, even when heavily governed.



### D.5.3 Artefact Set (Regulated)

Required:
- Vision Brief
- Formal system and sub-system requirements
- Full RTM
- Architecture documentation (C4 + detailed views)
- ADRs (comprehensive)
- Risk register & hazard analysis
- Formal test plans and reports
- Configuration and change records



### D.5.4 Validation & Verification

- Explicit V&V strategy
- Formal reviews and sign-offs
- Independent verification where required
- Evidence generation integrated into delivery flow



### D.5.5 Governance Model

- Defined lifecycle gates with clear entry/exit criteria
- Formal architectural and safety reviews
- Clear accountability and escalation paths

Governance is designed to:
- Reduce uncertainty
- Support audits
- Protect system integrity



### D.5.6 Slack in Regulated Systems

Slack is **mandatory**, not optional.

- Capacity reserved for defect resolution
- Time allocated for audits and reviews
- Margin built into schedules and designs

Regulated systems without slack fail catastrophically.



## D.6 Moving Between Profiles

Profiles are **not permanent**.

Products may:
- Start Minimal, then become Balanced
- Operate Balanced with Regulated subsystems
- Temporarily tighten governance after incidents

Key rule:
> Change profiles deliberately, not accidentally.



## D.7 Leadership Responsibilities Across Profiles

Leadership must:
- Select the appropriate profile consciously
- Explain *why* a profile is chosen
- Protect slack regardless of profile
- Prevent profile drift through neglect

Firmitas succeeds when **intentionality replaces habit**.



## D.8 Summary

Minimal, Balanced, and Regulated Firmitas are not different frameworks.
They are different expressions of the same philosophy.

What changes is **how much structure is required to protect system health**.

What never changes:
- Focus on outcomes
- Respect for people
- Systemic thinking
- Learning over blame
- Long-term value creation
