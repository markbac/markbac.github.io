---
title: "Chapter 15: Quality as a System Property"
---

# Chapter 15: Quality as a System Property

Quality failures are rarely the result of engineers who did not care about quality. In most organisations that deliver products with significant defects, the engineers knew the quality was insufficient. They knew which tests had been skipped, which requirements had been ambiguously implemented, which technical debt was accumulating in ways that would cost more to address later. They knew because they were the ones making the compromises — rationally, under pressure, in a system that made quality the most available casualty when schedule and cost were threatened.

This is the defining characteristic of quality as a system property: it is not produced by individual commitment and destroyed by individual carelessness. It is produced by systems designed to make quality the natural outcome of the way work is done, and destroyed by systems that make quality compromises the rational response to the conditions they create.

The implication for leadership is direct. Quality cannot be mandated. It cannot be inspected in at the end. It cannot be delegated to a quality function that operates separately from the delivery process. Quality is a consequence of how the system is designed — the architecture, the requirements, the feedback loops, the incentives, the verification practices, and the slack that makes doing things properly possible. Changing the quality outcomes requires changing those system properties, not issuing quality directives.

---

## Quality and the failure in Chapter 1

The programme in Chapter 1 produced poor quality outcomes not because engineers were careless but because the system produced them.

Firmware was written against an ambiguous specification. Not because the firmware engineers did not know the specification was ambiguous — they did, and they said so. But the system did not resolve the ambiguity before development began. The risk was noted, the mitigation was requested, and the development proceeded because the system had no mechanism for stopping development until the ambiguity was resolved. The quality deficit was encoded in the programme at the moment the ambiguity was left unresolved.

The third-party component was integrated without independent validation. The quality assumption — that the component would behave as specified — was never tested before the architecture was built around it. When the assumption proved wrong, the quality deficit manifested as an architectural redesign that cost weeks rather than the days a validation spike would have required.

The test environment was not available during the phases when its absence mattered most. Integration testing was deferred to the phase when the test environment became available. The defects that integration testing would have found were found instead during late-programme validation, when the cost of addressing them was substantially higher.

Each of these quality failures was systemic. Each was visible in advance. None was addressed by the system in time to prevent the cost.

---

## Built-in quality versus inspected quality

The distinction between built-in quality and inspected quality is fundamental to understanding both why quality fails and how to address it.

Inspected quality is the detection of defects after they have been created. Testing finds the bugs. Reviews find the design problems. Audits find the compliance gaps. Detection is necessary — but detection after the fact is the most expensive form of quality assurance available. The cost of a defect increases by roughly an order of magnitude for every phase boundary it crosses undetected. A requirements error found during specification costs hours to fix. Found during integration, it costs days. Found during acceptance testing, it costs weeks. Found in the field, it costs the relationship.

Built-in quality is the design of systems so that defects are prevented rather than detected — or detected as early as possible, when the cost of correction is still low. It requires that quality considerations are present at every stage of the delivery process: in how requirements are written, in how architecture is designed, in how development is conducted, in how work transitions from one team to another. Quality is not a downstream activity. It is a property of every upstream decision.

The shift from inspected to built-in quality is not the abandonment of testing. Testing remains essential. The shift is in where the emphasis lies — not on finding problems after they are embedded, but on preventing them from being embedded in the first place, and on finding them as early as possible when prevention has not been fully achieved.

---

## Quality and requirements

The quality of the delivered system is determined, more than by any other single factor, by the quality of the requirements it was built against.

A requirement that is ambiguous produces an implementation that is based on an assumption. That assumption may be correct. It may not be. When it is not, the consequence is rework — discovered at integration, at acceptance testing, or in the field, depending on when the system is first tested against a customer's actual operational expectations.

A requirement that is not testable produces an acceptance process that cannot be objective. When the acceptance criterion for a requirement is "the system shall perform adequately," the acceptance decision is a matter of interpretation rather than evidence. Interpretations differ. Disputes follow. Both parties believe they are right and both may be — because the requirement did not specify what adequate means.

A requirement that has been decomposed correctly — tracing from the customer need through system and subsystem levels to implementable leaf requirements with defined acceptance criteria — produces a programme that can verify its quality objectively at every level. Every component of the delivered system is traceable to a requirement. Every requirement has a test. Every test has a defined pass/fail condition. The quality of the system, relative to its requirements, is not a matter of judgement. It is a matter of evidence.

This connection between requirements engineering and quality is why Chapter 11 precedes this one. Requirements engineering is not a separate discipline that serves documentation purposes. It is the primary quality investment of the programme — the activity that determines the quality of everything that follows.

---

## Quality and architecture

Architecture determines quality outcomes as directly as it determines delivery performance. The two are inseparable.

A well-designed architecture makes quality achievable. Components with clear boundaries and well-defined interfaces can be tested in isolation, with confidence that the isolation faithfully represents the integration context. Changes can be made to one component without requiring system-wide regression testing of everything else. Failures can be contained and diagnosed. The system can be observed in operation in ways that produce the feedback required to maintain quality over time.

A poorly designed architecture makes quality expensive and ultimately impossible to sustain. Tightly coupled components cannot be tested meaningfully in isolation. Every change carries the risk of cascading effects that are not visible until integration. Failures propagate in ways that are difficult to diagnose. The operational system is a black box that fails in surprising ways and reveals little about why.

The architectural properties that most directly affect quality outcomes are testability, observability, and failure isolation.

Testability is the degree to which the system can be exercised in a controlled manner to confirm that it behaves as required. A testable architecture has components with defined inputs and outputs, interfaces that can be controlled and monitored, and a structure that allows the behaviour of individual parts to be verified without requiring the full system to be operational. Untestable architectures are not a testing problem. They are an architectural choice — usually made early in the programme, under schedule pressure, in the name of implementation simplicity — that will impose its cost on every test phase that follows.

Observability is the degree to which the system reveals its internal state through external signals. A system that can be monitored, that produces meaningful diagnostic output, that exposes its health and its failure modes through observable telemetry is a system that can be operated responsibly and maintained effectively. A system that fails silently, that produces unhelpful error messages, that requires specialist knowledge to diagnose is not just difficult to support. It is a quality liability — because problems that cannot be observed cannot be detected early, and problems that cannot be detected early accumulate into failures that cannot be contained cheaply.

Failure isolation is the degree to which the impact of a failure in one component is bounded — prevented from propagating to other components in ways that transform a contained problem into a system-wide incident. An architecture that isolates failures produces systems that degrade gracefully under conditions the designers did not fully anticipate. An architecture that does not isolates failures produces systems that fail catastrophically in ways that are expensive to recover from.

---

## Verification and validation

Verification and validation are frequently conflated but serve different purposes, and the distinction matters for how quality is managed throughout the delivery lifecycle.

Verification asks: did we build the system right? It confirms that the system has been implemented in accordance with its specifications — that the requirements have been met, the design has been implemented correctly, the tests pass. Verification is an internal discipline. It confirms conformance to specification.

Validation asks: did we build the right system? It confirms that the specified system, when operated in its real environment, achieves the outcomes the customer needs. Validation is an external discipline. It confirms fitness for purpose.

A system can pass all its verification tests and still fail validation — because the specification was wrong, or because the customer's real operational environment differs from the conditions under which verification was conducted, or because the customer's actual need differed from the need that was expressed in the requirements. This is the requirements failure mode that Chapter 11 described: an accurate implementation of a wrong specification.

Both verification and validation must be continuous activities, not end-stage events. Verification occurs throughout the iterative development core — every test that runs, every code review that catches a defect, every interface integration that confirms the contract is being met is an act of continuous verification. Validation begins in the foundations phase — every conversation with the customer that confirms the requirements are capturing the right need, every early prototype that tests an assumption about operational behaviour is an act of early validation.

The programme that defers all validation to the final phase is not being rigorous. It is accumulating validation risk throughout the programme and discovering it all at once, at the point when it is most expensive to address. The programme that validates continuously — that builds in regular checkpoints at which the developing system is exposed to operational reality and the gap between specification and need is measured — arrives at the validation phase with progressively higher confidence rather than with the anxiety of a system that has never been tested against the environment it must operate in.

---

## Quality in regulated and safety-critical contexts

In regulated environments — programmes operating under IEC 62304, IEC 61508, ISO 9001, DO-178C, and their sector-specific equivalents — quality is not solely an internal engineering concern. It is an external obligation with specific evidence requirements.

The evidence obligations of regulated standards are not bureaucratic impositions. They are the explicit articulation of what good quality engineering produces as a natural output: requirements that are clear and traceable, design decisions that are recorded and justified, testing that is systematic and evidence-rich, incidents that are investigated and learned from. A programme that practises quality engineering as described in this chapter will produce the evidence that regulated standards require as a by-product of doing the work well.

The failure mode in regulated programmes is not the existence of the evidence obligations. It is the treatment of evidence production as a separate activity from engineering delivery. Programmes that manage their engineering process correctly and then assemble compliance evidence retrospectively are doing two jobs: engineering the system and manufacturing the appearance of engineering discipline. The retrospective assembly is more expensive, less reliable, and less credible to auditors than evidence produced continuously as a natural output of the engineering process.

Firmitas treats compliance evidence as the output of a quality engineering system that is functioning correctly. The traceability spine described in Chapter 14 is the compliance evidence structure. The ADRs are the design justification record. The test results are the verification evidence. The risk register lifecycle is the risk management record. None of these require additional activity beyond what a well-run programme produces anyway. They require the discipline to produce them in a form that is organised, current, and navigable — which is what living documentation and docs-as-code practices, addressed in Chapter 18, provide.

---

## Quality, slack, and the system under pressure

Quality and slack are connected in the way that Chapter 12 described. A system without slack cannot maintain quality because the activities that maintain quality — proper test coverage, thorough code review, adequate investigation of defects, deliberate refactoring of accumulated debt — are the first casualties of overload.

These activities are never urgent in the sense that delivering a feature is urgent. They can always be deferred. They accumulate as a backlog of quality debt that inflates invisibly while the programme's task completion rate stays green. When the debt surfaces — in integration failures, in acceptance test failures, in field incidents — the cost is substantially higher than the cost of maintaining quality throughout would have been.

The connection between quality and slack is not just operational. It is also cultural. A team that has slack for proper code review produces better code and learns more from the review process. A team that reviews code under time pressure produces superficial reviews that miss the structural issues the review should catch. The review exists in both cases. The quality outcome is different.

The leadership responsibility is explicit: protecting the slack that makes quality sustainable is not a soft preference for comfortable working conditions. It is a structural prerequisite for the quality outcomes the programme requires. An organisation that claims to value quality while systematically eliminating the slack that quality requires is not actually valuing quality. It is valuing the appearance of delivery pace over the reality of delivery quality — and deferring the cost of that trade-off to whichever phase of the programme or product lifecycle is unfortunate enough to discover it.

---

## Quality metrics that do not corrupt behaviour

Measuring quality is necessary. Measuring it badly destroys the behaviour it is intended to encourage.

The most common quality measurement failure is the use of metrics that are easy to collect but inversely correlated with the quality they are supposed to measure. Defect counts that incentivise not finding defects. Test coverage percentages that incentivise writing tests that pass rather than tests that find problems. Story point velocity that incentivises closing tickets rather than solving problems. Each of these metrics, when used as performance measures, produces behaviour that optimises the metric at the cost of the quality it was supposed to represent.

Firmitas favours quality metrics that measure system behaviour rather than development activity. Defect escape rate — the proportion of defects that reach a later phase than the one in which they should have been detected — reveals the effectiveness of quality practices at each phase boundary. Lead time to detect — how long after a defect is introduced it is found — reveals the effectiveness of feedback loops. Rework rate — the proportion of completed work that must be revisited due to quality failures — reveals the upstream quality of requirements, design, and review practices. These metrics are harder to collect than story points. They are more meaningful. They reveal the quality of the system rather than the activity of the teams.

The governance principle for quality measurement follows from Chapter 8: metrics that senior management uses to evaluate quality should measure system health, not team activity. The governance layer that is reading defect discovery rates and rework percentages is asking the right question — is the quality system working? The governance layer that is reading test case counts and coverage percentages is asking the wrong question — are teams producing the artefacts we associate with quality work?

---

## Quality engineering as a leadership discipline

Quality is a system property. Systems are designed by leaders. Quality engineering is therefore a leadership discipline, not a technical one.

This does not mean leaders write test cases or conduct code reviews. It means they shape the conditions under which quality is either possible or impossible. They set the incentives that determine whether teams optimise for apparent velocity or for sustained quality. They protect the slack that makes quality activities possible. They establish the governance mechanisms that treat quality failures as system signals rather than execution problems. They ensure that architectural decisions are made with testability, observability, and failure isolation as first-class concerns. They create the culture in which a test failure is welcomed as early learning rather than penalised as a programme delay.

The programme board in Chapter 1 that confirmed the delivery date without addressing the unvalidated assumptions in the architecture was making a quality decision. The decision was not framed as a quality decision — it was framed as a schedule decision. But schedule decisions that require quality compromises are quality decisions. The leadership layer that makes schedule decisions without acknowledging the quality consequences they carry is not governing quality. It is generating the conditions that will produce quality failures later, at a cost that will be attributed to execution rather than to the governance decision that caused it.

Quality engineering, in the Firmitas sense, begins at the moment the programme board first reviews the programme's plan and risks, and continues throughout the programme's life. It ends when the last field incident has been resolved and the system has been retired. That scope is not a burden. It is what responsibility for outcomes actually means.
