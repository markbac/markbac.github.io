---
title: Design review checklist
---

# Design review checklist

Use this checklist to review the detailed design of a software component or firmware module before it is coded. It checks that the design is sound, consistent with the architecture above it, and complete enough to build and test from.

For a whole system or a high-level design, use the [architecture review checklist](architecture-review-checklist.md) instead. Keep the completed checklist with the design, and go through it again at each design review or stage gate.

## Checklist

### General

- [ ] **SD-1 Each part of the design meets its own checklist.** Diagrams, models and descriptions are clear, accurate and use their notation correctly.
- [ ] **SD-2 It supports both the product goals and the project goals,** such as the commercial aim and the delivery date.
- [ ] **SD-3 It is feasible** with the technology, budget, schedule and skills available.
- [ ] **SD-4 Known risks are recorded,** technical and delivery risks alike, each with a mitigation or a plan.
- [ ] **SD-5 The notation suits the job,** for example sequence diagrams for interactions and state charts for modes.
- [ ] **SD-6 The formality matches the work.** A safety function needs more rigour than a test utility.
- [ ] **SD-7 Prototypes and earlier phases have fed back into the design.**
- [ ] **SD-8 Proven designs are reused** where they fit, such as existing drivers and frameworks.
- [ ] **SD-9 It is complete enough to start implementation** with confidence.

### Design quality

- [ ] **SD-10 It has conceptual integrity.** The parts follow one set of ideas and fit together.
- [ ] **SD-11 It fits the target.** It works within the memory, CPU, hardware and environmental limits.
- [ ] **SD-12 It uses well-known techniques.** Anything unusual is there for a stated reason.
- [ ] **SD-13 It prefers simple to clever.**
- [ ] **SD-14 It is as simple as it can be while still doing the job.**
- [ ] **SD-15 It is lean.** Every part is needed, and nothing is there "just in case".
- [ ] **SD-16 The parts most likely to change are easy to change,** through low coupling, clear interfaces and modularity.
- [ ] **SD-17 Reusable parts are abstracted properly,** for example a hardware abstraction layer, a driver or a shared service.
- [ ] **SD-18 It could move to another platform** with reasonable effort, where that matters.
- [ ] **SD-19 Complexity is kept low,** for example the cyclomatic complexity of each module and function.
- [ ] **SD-20 Another engineer can hold it in their head.**
- [ ] **SD-21 It is robust** against bad inputs, timing variations and unexpected resets.

### Traceability

- [ ] **SD-22 Every functional and non-functional requirement is addressed,** and each part of the design traces back to a requirement.
- [ ] **SD-23 There is no scope creep.** The design adds no features the requirements do not ask for.
- [ ] **SD-24 Requirement coverage is recorded,** in a traceability matrix where the project needs one.

### Level of detail

- [ ] **SD-25 There is enough detail to hand over** for coding and for writing the test plan.
- [ ] **SD-26 Sequence diagrams, state machines and flowcharts are clear and complete.**

### Completeness

- [ ] **SD-27 Assumptions, constraints, decisions and dependencies are all written down.**
- [ ] **SD-28 The uncertain or high-risk parts are called out,** each with a fallback or mitigation.
- [ ] **SD-29 Gaps and open points are visible,** with a reason and an owner for each.
- [ ] **SD-30 Reasonable alternatives were considered,** including not solving the problem in software at all.
- [ ] **SD-31 Trade-offs are explained,** such as performance against power, or memory against speed.

### Consistency

- [ ] **SD-32 It matches the architecture above it** and what the modules around it expect.
- [ ] **SD-33 Issues deferred from earlier phases are dealt with.**
- [ ] **SD-34 Open points in the upstream requirements have been assessed.**
- [ ] **SD-35 It makes sense from the top down and from the bottom up.**
- [ ] **SD-36 It is consistent with similar modules,** for example those sharing a driver or a protocol.
- [ ] **SD-37 It works with the build, CI, test and deployment environments.**

### Performance

- [ ] **SD-38 Timing, memory and throughput assumptions are written down.**
- [ ] **SD-39 The performance-critical paths have evidence behind them,** from a prototype, a benchmark or a design already proven in the same setting.

### Maintainability

- [ ] **SD-40 Someone else could maintain it.** A new engineer could understand and change it without the author.
- [ ] **SD-41 Reused components are documented,** along with their effect on the design and on integration.
- [ ] **SD-42 Extension points are identified,** such as hooks and interfaces for likely additions.
- [ ] **SD-43 It will not decay quickly.** Tightly coupled areas, which tend to get worse with each change, are kept to a minimum.

### Compliance, safety and testability

- [ ] **SD-44 It follows the standards that apply,** such as MISRA C, IEC 61508, ISO 26262 or the platform's own rules.
- [ ] **SD-45 Fault behaviour is designed.** Watchdog, brown-out, reset and fault modes are described.
- [ ] **SD-46 It is testable.** It has seams for stubs, test points and logging.
- [ ] **SD-47 Static analysis and any code generation are part of the plan,** with traceability through the lifecycle.

**As Markdown.** To copy it into an issue, a pull request or a review record:

```markdown
### General
- [ ] **SD-1 Each part of the design meets its own checklist.** Diagrams, models and descriptions are clear, accurate and use their notation correctly.
- [ ] **SD-2 It supports both the product goals and the project goals,** such as the commercial aim and the delivery date.
- [ ] **SD-3 It is feasible** with the technology, budget, schedule and skills available.
- [ ] **SD-4 Known risks are recorded,** technical and delivery risks alike, each with a mitigation or a plan.
- [ ] **SD-5 The notation suits the job,** for example sequence diagrams for interactions and state charts for modes.
- [ ] **SD-6 The formality matches the work.** A safety function needs more rigour than a test utility.
- [ ] **SD-7 Prototypes and earlier phases have fed back into the design.**
- [ ] **SD-8 Proven designs are reused** where they fit, such as existing drivers and frameworks.
- [ ] **SD-9 It is complete enough to start implementation** with confidence.

### Design quality
- [ ] **SD-10 It has conceptual integrity.** The parts follow one set of ideas and fit together.
- [ ] **SD-11 It fits the target.** It works within the memory, CPU, hardware and environmental limits.
- [ ] **SD-12 It uses well-known techniques.** Anything unusual is there for a stated reason.
- [ ] **SD-13 It prefers simple to clever.**
- [ ] **SD-14 It is as simple as it can be while still doing the job.**
- [ ] **SD-15 It is lean.** Every part is needed, and nothing is there "just in case".
- [ ] **SD-16 The parts most likely to change are easy to change,** through low coupling, clear interfaces and modularity.
- [ ] **SD-17 Reusable parts are abstracted properly,** for example a hardware abstraction layer, a driver or a shared service.
- [ ] **SD-18 It could move to another platform** with reasonable effort, where that matters.
- [ ] **SD-19 Complexity is kept low,** for example the cyclomatic complexity of each module and function.
- [ ] **SD-20 Another engineer can hold it in their head.**
- [ ] **SD-21 It is robust** against bad inputs, timing variations and unexpected resets.

### Traceability
- [ ] **SD-22 Every functional and non-functional requirement is addressed,** and each part of the design traces back to a requirement.
- [ ] **SD-23 There is no scope creep.** The design adds no features the requirements do not ask for.
- [ ] **SD-24 Requirement coverage is recorded,** in a traceability matrix where the project needs one.

### Level of detail
- [ ] **SD-25 There is enough detail to hand over** for coding and for writing the test plan.
- [ ] **SD-26 Sequence diagrams, state machines and flowcharts are clear and complete.**

### Completeness
- [ ] **SD-27 Assumptions, constraints, decisions and dependencies are all written down.**
- [ ] **SD-28 The uncertain or high-risk parts are called out,** each with a fallback or mitigation.
- [ ] **SD-29 Gaps and open points are visible,** with a reason and an owner for each.
- [ ] **SD-30 Reasonable alternatives were considered,** including not solving the problem in software at all.
- [ ] **SD-31 Trade-offs are explained,** such as performance against power, or memory against speed.

### Consistency
- [ ] **SD-32 It matches the architecture above it** and what the modules around it expect.
- [ ] **SD-33 Issues deferred from earlier phases are dealt with.**
- [ ] **SD-34 Open points in the upstream requirements have been assessed.**
- [ ] **SD-35 It makes sense from the top down and from the bottom up.**
- [ ] **SD-36 It is consistent with similar modules,** for example those sharing a driver or a protocol.
- [ ] **SD-37 It works with the build, CI, test and deployment environments.**

### Performance
- [ ] **SD-38 Timing, memory and throughput assumptions are written down.**
- [ ] **SD-39 The performance-critical paths have evidence behind them,** from a prototype, a benchmark or a design already proven in the same setting.

### Maintainability
- [ ] **SD-40 Someone else could maintain it.** A new engineer could understand and change it without the author.
- [ ] **SD-41 Reused components are documented,** along with their effect on the design and on integration.
- [ ] **SD-42 Extension points are identified,** such as hooks and interfaces for likely additions.
- [ ] **SD-43 It will not decay quickly.** Tightly coupled areas, which tend to get worse with each change, are kept to a minimum.

### Compliance, safety and testability
- [ ] **SD-44 It follows the standards that apply,** such as MISRA C, IEC 61508, ISO 26262 or the platform's own rules.
- [ ] **SD-45 Fault behaviour is designed.** Watchdog, brown-out, reset and fault modes are described.
- [ ] **SD-46 It is testable.** It has seams for stubs, test points and logging.
- [ ] **SD-47 Static analysis and any code generation are part of the plan,** with traceability through the lifecycle.
```


## Further reading

The structure of this checklist follows the design checklists in Steve McConnell's *Code Complete* (second edition, Microsoft Press, 2004), extended for embedded systems.
