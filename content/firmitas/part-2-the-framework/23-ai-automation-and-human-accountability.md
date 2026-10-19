---
title: "Chapter 23: AI, Automation, and Human Accountability"
---

# Chapter 23: AI, Automation, and Human Accountability

Engineering work is changing. The tools available to engineers — for generating code, for producing documentation, for analysing requirements, for designing tests, for reviewing architecture — are developing at a pace that is genuinely transforming the cost of certain activities that previously consumed substantial human effort. A requirements document that took a senior engineer two weeks to produce can now be drafted in hours. Test cases that required careful manual construction can be generated against a specification automatically. Code that implemented a well-specified behaviour can be produced by a tool that did not exist three years ago.

This change is real. Its consequences for engineering delivery are significant. They are not, however, the consequences that the most enthusiastic accounts suggest. The collapse of implementation cost does not eliminate the cost of engineering. It redistributes it — from the cost of producing artefacts to the cost of specifying them correctly, verifying them rigorously, and maintaining accountability for the outcomes they produce. The engineering discipline that matters most in an AI-assisted environment is not the discipline of implementation. It is the discipline of intent, specification, and verification.

This chapter addresses AI and automation in the context of the Firmitas framework — not as a special case requiring a separate framework, but as a set of capabilities that amplify the properties of the engineering systems they operate within. AI accelerates what already works. It magnifies what is already broken. The governance implications are specific, practical, and grounded in the same principles that govern every other aspect of engineering delivery.

---

## AI as an accelerator, not a replacement

The starting position is simple and important: AI tooling is an accelerator, not a replacement for engineering judgement, engineering accountability, or the human understanding that gives engineering work its meaning and its consequences.

An AI tool that generates a requirements document has produced a hypothesis about what the system should do. The hypothesis may be well-formed. It may be coherent. It may even be largely correct. It is not a specification until a human being with the knowledge to evaluate it has reviewed it, challenged it where it is wrong, confirmed it where it is right, and accepted accountability for the claim it makes about what the system should do.

An AI tool that generates test cases has produced a set of test hypotheses against the specification it was given. Those tests may be correctly derived from the specification. They may also reflect the specification's ambiguities — testing what was written rather than what was meant. They may share the blind spots of the implementation they are testing, because both were generated from the same specification by processes that make the same assumptions. A human engineer reviewing those tests must ask not only whether they pass but whether they are asking the right questions.

An AI tool that generates code has produced an implementation of a specification. The code may be functionally correct. It may be architecturally inappropriate for the system it is being integrated into. It may violate the quality standards, the security requirements, or the performance constraints that the specification did not explicitly state but that anyone with operational knowledge of the context would have applied. A human engineer reviewing that code must bring the contextual knowledge that the tool does not have.

In each case, the AI produces the first draft. The human provides the judgement that converts the first draft into a specification, a test suite, or an implementation that the programme can build on with confidence. The AI saves the time to first draft. It does not save the time or the cognitive investment required to produce something that is genuinely fit for purpose.

---

## Where AI accelerates across the delivery lifecycle

AI tooling provides genuine acceleration at specific points in the delivery lifecycle. Understanding where the acceleration is real allows organisations to capture it. Understanding where it is illusory prevents them from accepting false confidence in its place.

**In the structured foundations phase**, AI tooling can accelerate first-draft requirements production from specification documents, standards, or customer statements of need. It can identify gaps and ambiguities in existing requirements by cross-referencing against known patterns and standards. It can generate first-draft Interface Control Documents from architectural descriptions. It can produce initial risk assessments from system descriptions.

The verification obligation at this stage is high. AI-generated requirements are hypotheses about what the system should do — and they are as good as the information they were generated from. Requirements generated from an ambiguous customer statement will be ambiguous. Requirements generated from an incomplete specification will be incomplete. The review process for AI-generated requirements must be as rigorous as the process for human-generated ones — arguably more so, because the speed of generation can create false confidence in the quality of the output.

**In the iterative development core**, AI tooling can accelerate code generation for well-specified behaviours, documentation of decisions and interfaces, generation of test cases from requirements, and analysis of change impact across requirements and architecture.

The specific risk in this phase is the AI-generated test problem. Tests generated automatically from a specification may correctly reflect the specification as written while missing the intent behind it. They may produce high code coverage with low confidence — because they test the implementation's behaviour rather than the customer's need. A test suite generated by AI should not be reviewed only for correctness against the specification. It should be reviewed for whether it is asking the questions that matter — whether the test cases that would catch the failures the customer would care about most are present and adequately specified.

**In the validation phase**, AI tooling can accelerate traceability matrix generation, test result analysis, and compliance evidence compilation. The verification obligation here is the highest in the programme — because the evidence produced in this phase is the basis for the programme's quality and compliance claims. AI-generated traceability matrices must be verified for correctness and completeness before they are used as compliance evidence. A traceability matrix that looks complete but contains incorrect or missing links is not compliance evidence. It is the appearance of compliance evidence, which is more dangerous than an acknowledged gap.

**In operations**, AI tooling can accelerate incident analysis, knowledge base generation from operational data, and documentation maintenance. The governance principle here is that operational decisions — decisions about what to do in response to an operational incident, decisions about whether a system behaviour is acceptable, decisions about whether to deploy a change — must remain in human hands. AI can surface patterns, suggest diagnoses, and recommend responses. The decision to act on those recommendations must be made by a human who accepts accountability for the outcome.

---

## Specification as the primary engineering discipline

The collapse of implementation cost has a specific implication that the Firmitas framework addresses directly: as implementation becomes cheaper and faster, specification becomes more important, not less.

When implementation is expensive, poorly specified requirements are caught relatively quickly by the cost of implementing them wrong — the developer who cannot make progress against an ambiguous requirement surfaces the ambiguity early. When implementation is cheap, poorly specified requirements are implemented rapidly and incorrectly — the AI tool fills the ambiguity with a plausible interpretation, produces an implementation, and delivers it faster than the human review process can evaluate it. The ambiguity has not been resolved. It has been embedded in a fast-delivered implementation that appears complete.

The engineering discipline that scales with AI-accelerated delivery is specification — the ability to express intent with sufficient precision, completeness, and verifiability that the tools operating on it produce what was actually needed rather than what could plausibly be inferred. Chapter 11's requirements engineering discipline becomes more critical, not less, in an AI-assisted environment. The Requirement Breakdown Structure, the properties of a well-written requirement, the testability criteria, the acceptance condition precision — these are the properties that determine whether AI-assisted delivery produces the right system or a rapidly produced version of a misunderstood specification.

The organisation that responds to AI-assisted delivery by relaxing its requirements discipline — by treating the AI's ability to fill gaps as a substitute for specifying what should be in those gaps — will discover the consequences at validation and in the field. The gaps are not filled by the AI's judgement. They are filled by the AI's most plausible inference from incomplete information. The result is a system that is implemented consistently with the inference rather than with the intent. The inference may be close. It is not the same thing.

---

## Verification must tighten as generation accelerates

The relationship between the speed of generation and the rigour of verification is inverse, not proportional. When generation is slow, verification happens continuously — the human producing the artefact is also verifying it as they produce it, catching errors as they introduce them. When generation is fast, the artefact arrives before the human reviewer is ready for it, and the social pressure to accept the output — because it looks complete and was delivered quickly — creates the conditions for superficial review.

Firmitas requires that verification depth is calibrated to consequence, not to generation speed. An AI-generated artefact that forms part of a safety case requires the same verification rigour as a human-generated one — the safety consequence is the same regardless of how the artefact was produced. An AI-generated test suite requires independent evaluation of whether it is asking the right questions, not just whether it passes. An AI-generated traceability matrix requires verification of every link, not confirmation that links exist.

The specific risk to manage is automation bias — the human tendency to trust outputs from automated systems more readily than outputs from other humans. An AI-generated requirements document that is well-formatted, comprehensive in appearance, and internally consistent will tend to pass review more quickly than a human-generated document with the same quality of underlying content, because the formatting and apparent completeness create a cognitive signal of rigour that the reviewer responds to. The review process must be designed to counteract this bias — to evaluate the substance rather than the presentation, to test the requirements against customer reality rather than against internal consistency, and to ask explicitly whether the gaps that the AI may have filled plausibly have been filled correctly.

---

## Provenance and traceability in AI-assisted delivery

When AI tools contribute to engineering artefacts — generating requirements, producing test cases, drafting design rationale, creating documentation — the provenance of those contributions must be visible. Not for blame purposes. For review purposes.

An artefact produced by a human engineer with deep domain knowledge carries different confidence than an artefact generated by an AI tool from a specification prompt. Both may be correct. The review process that is appropriate for the former may be insufficient for the latter. If the provenance is not recorded, the reviewer cannot calibrate the review depth appropriately.

In regulated programmes, the provenance question has compliance implications. The regulatory frameworks that govern safety-critical and quality-managed engineering — IEC 62304, IEC 61508, ISO 9001, DO-178C — were written before AI-generated artefacts were a practical reality. Their requirements for controlled development, documented rationale, and independent review must be interpreted in the context of AI assistance. The interpretation that best serves the standards' intent is conservative: AI-generated artefacts must be reviewed with at least the same rigour as human-generated ones, the AI's contribution must be traceable, and the human who accepts the artefact into the programme's evidence base is accountable for its correctness.

The traceability spine described in Chapter 14 applies with full force to AI-assisted delivery. Every requirement traces to its source — including whether it was generated by AI and reviewed by whom. Every test case traces to the acceptance criteria it was derived from and the method by which it was produced. Every design decision traces to the architectural reasoning that justified it and the review process that validated it. The AI acceleration does not remove the traceability obligation. It adds the requirement to record the AI's contribution as part of the traceability record.

---

## Accountability cannot be automated away

The most fundamental governance principle in AI-assisted engineering delivery is stated in Principle 5 and applies with particular force here: leadership owns the system, not the intention.

No automated system is accountable. A model does not accept responsibility for the consequences of the outputs it produces. A pipeline does not bear the cost of the defect it failed to catch. A tool does not absorb the commercial and reputational impact of the compliance failure it contributed to. All of these consequences belong to the humans who designed the system, who operated it, and who accepted the outputs it produced.

This is not a limitation of current AI capability that future AI will overcome. It is a structural property of what accountability means. Accountability is the acceptance of responsibility for outcomes — including the outcomes of decisions made under uncertainty, with incomplete information, in conditions that could not be fully anticipated. It requires a subject who can learn from failure, who can be held to the consequences of decisions, and whose future behaviour is shaped by those consequences. Accountability belongs to humans. It cannot be delegated to tools, regardless of their capability.

The practical implications are specific.

Every AI-assisted decision has a named human owner who is accountable for the outcome. Not the team that used the tool. Not the organisation that deployed it. A specific person who reviewed the AI's output, exercised judgement about its adequacy, and accepted it into the programme on behalf of the organisation. That person's name is attached to the decision in the programme's decision record.

Every automated pipeline that makes decisions without human review — that deploys code, that modifies requirements, that updates a traceability matrix, that accepts test results — has a named human owner who is accountable for the pipeline's behaviour. When the pipeline produces an incorrect output, the accountability belongs to the person who designed the pipeline, not to the pipeline itself.

Human override mechanisms are present and functional. The ability to stop an automated process, to reverse an AI-assisted decision, and to require human review at any point must be designed into the system and must be genuinely available — not technically present but practically impossible to exercise under production conditions or delivery pressure.

---

## AI governance in regulated programmes

For programmes operating in regulated environments, AI governance carries specific obligations that the framework must address.

The first is the question of qualification. Most regulated frameworks require that the tools used in safety-critical or quality-managed development are qualified — demonstrated to be fit for their intended use within the programme's defined scope. AI tools introduce new qualification challenges because their behaviour is probabilistic, context-dependent, and not fully deterministic. A tool that generates requirements correctly 95% of the time is not qualified for safety-critical requirements engineering without a rigorous process for identifying and correcting the 5% of cases where it does not.

The qualification obligation does not mean that AI tools cannot be used in regulated programmes. It means that the programmes using them must define the scope of their use, establish the verification processes that compensate for their probabilistic behaviour, and demonstrate that the combination of AI assistance and human verification produces outputs that meet the quality and safety obligations of the applicable standard.

The second is the question of training data and knowledge sources. AI tools encode their training data. A tool trained on publicly available engineering documentation may have absorbed incorrect, outdated, or context-inappropriate information that it applies to the programme's specific domain. The governance obligation is to understand what the tool knows, where its knowledge comes from, and whether the domain-specific context of the programme is adequately represented in its training — or whether the tool's outputs require supplementary review by domain experts who can identify where the tool's general knowledge does not apply correctly to the specific context.

The third is the question of auditability. Regulatory bodies increasingly expect to understand how engineering artefacts were produced. An audit trail that records what AI tools were used, what inputs they were given, what outputs they produced, and who reviewed and accepted those outputs is the minimum required for programmes in regulated environments. The audit trail for AI-assisted development is more complex than the trail for purely human development — because the trail must record not just what was done but how the AI's contribution was supervised and verified.

---

## The human skills that become more valuable

The shift in engineering work produced by AI acceleration does not diminish the value of engineering expertise. It changes which expertise matters most.

The skills that AI tools replicate most effectively are the skills of execution — producing well-formed outputs from well-specified inputs, following established patterns, generating consistent implementations of understood requirements. The skills that AI tools do not replicate are the skills of judgement — understanding which requirements matter most and why, recognising when a specification is missing something critical, evaluating whether an architecture will hold up under operational conditions the specification did not anticipate, deciding when a trade-off is acceptable and when it is not.

Specification quality — the ability to express intent precisely, completely, and verifiably — becomes more valuable as implementation becomes cheaper. The engineer who can write requirements that an AI tool can implement correctly the first time is more productive in an AI-assisted environment than the engineer who writes requirements that the AI must interpret charitably.

Systems thinking — the ability to understand how engineering decisions interact with each other and with the broader context of the programme — becomes more valuable as the volume of engineering artefacts increases. The engineer who can evaluate whether an AI-generated component fits coherently into the system architecture, whether its quality properties are consistent with the programme's requirements, and whether its assumptions are compatible with the operational environment it will enter is the engineer whose judgement the programme depends on.

Risk reasoning — the ability to identify what could go wrong, why, and what the consequences would be — becomes more valuable as the rate of change increases. The engineer who can look at an AI-generated system and identify the failure modes that the AI did not model, the edge cases that the specification did not cover, and the operational conditions that the design did not anticipate is the engineer who protects the programme from the confidence that AI-assisted delivery can inadvertently create.

These are not new skills. They are the skills that have always distinguished good engineering from mere implementation. AI assistance makes them relatively more important — because the implementation work that previously demanded a substantial portion of engineering time becomes faster, and the time freed by that acceleration is most productively invested in the specification, verification, and systems reasoning that the tools cannot replicate.

---

## What does not change

The Firmitas principles do not change in an AI-assisted environment. They become more relevant.

Principle 3 — a commitment not made by those who must keep it is a target with someone else's name on it — applies to AI-assisted programmes as directly as to any other. The AI does not make commitments. It produces artefacts. The humans who accept those artefacts and build programmes on them make the commitments and carry the accountability.

Principle 4 — delivery knowledge lives closest to the work — applies with greater force when AI tools can produce artefacts rapidly from high-level inputs. The knowledge that determines whether the AI's output is adequate, whether the specification is complete, whether the test suite is rigorous enough — that knowledge lives in the engineers who understand the domain, the operational context, and the customer need. It cannot be replaced by the tool that generates first drafts against those inputs.

Principle 9 — decisions are first-class engineering artefacts — applies to AI-assisted decisions as fully as to human ones. A decision to accept an AI-generated requirements document without substantive review is a decision with consequences. A decision to deploy AI-generated code without adequate testing is a decision with consequences. These decisions must be visible, owned, and traceable — not hidden inside the automation.

Principle 12 — your people are your most significant investment — applies with particular urgency in a period when AI-assisted delivery creates pressure to reduce headcount in the belief that tools have replaced the need for people. The tools have not replaced the need for people. They have changed which people and which skills matter most. The organisation that responds to AI acceleration by reducing the engineering investment that produces specification quality, systems thinking, and risk reasoning capability will discover, when its AI-assisted programmes fail in the ways this chapter has described, that the tools did not replace the judgement that the people they let go had been providing.
