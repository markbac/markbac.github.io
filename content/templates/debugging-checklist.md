---
title: Debugging checklist
---

# Debugging checklist

Debugging by trial and error wastes time and often adds a second bug. Use this checklist to keep an investigation methodical: form a hypothesis, test it, and only then change the code.

To report a defect, or to close one, use the [defect report checklist](defect-report-checklist.md).

## Approach

- [ ] **DBG-1 Set a time limit for quick debugging.** When it runs out, stop poking and make a plan.
- [ ] **DBG-2 Check whether someone has already found it.** Search the tracker, the knowledge base and the recent commit history.
- [ ] **DBG-3 Use every tool you have:** the debugger and debug probe, compiler warnings, static analysis, sanitisers, trace and a logic analyser.
- [ ] **DBG-4 Assume the bug is in your code** until you have evidence that it is in the compiler, the operating system or the hardware.
- [ ] **DBG-5 Do not change code you do not understand** in the hope that the problem goes away.
- [ ] **DBG-6 Use more than one technique,** such as bisection, assertions, traces and comparing a good build with a bad one.
- [ ] **DBG-7 Ask for help** when you stop making progress.
- [ ] **DBG-8 Tell people early** if the investigation will take longer than planned.
- [ ] **DBG-9 Know when to step away** and come back with fresh eyes.
- [ ] **DBG-10 Check that the fix cures the cause,** not just the symptom you saw.
- [ ] **DBG-11 Write down what you learnt,** so nobody has to find it again.

## Finding the fault

- [ ] **DBG-12 State a hypothesis** that explains what you see, before the next test run.
- [ ] **DBG-13 Shrink the test case** to the smallest set of steps that still fails.
- [ ] **DBG-14 Reproduce it in more than one way,** or under different conditions.
- [ ] **DBG-15 Gather more data** to choose between competing hypotheses: logs, registers, traces and captures.
- [ ] **DBG-16 Look at what does not fail.** It narrows the search as much as what does.
- [ ] **DBG-17 Think of other explanations** when your first idea does not hold up.
- [ ] **DBG-18 Narrow the search by halves,** with `git bisect` or by switching modules out.
- [ ] **DBG-19 Look at what changed recently** in the code, the configuration and the build.
- [ ] **DBG-20 Widen the search** when the symptom appears far from the cause, as it does with memory corruption.
- [ ] **DBG-21 Test the parts on their own,** adding them back one at a time.
- [ ] **DBG-22 Suspect the code that has had bugs before.**
- [ ] **DBG-23 Add logging and instrumentation** where a debugger would change the timing.
- [ ] **DBG-24 Check the usual suspects:** off-by-one errors, uninitialised variables, stack overflow, integer truncation and a missing `volatile`.
- [ ] **DBG-25 Explain the problem out loud,** line by line, to a colleague or a rubber duck.

## Fixing it

- [ ] **DBG-26 Understand the cause before you edit anything.**
- [ ] **DBG-27 Confirm that the diagnosis explains every symptom,** not just some of them.
- [ ] **DBG-28 Write a test that fails** because of the bug, before you fix it.
- [ ] **DBG-29 Keep the evidence:** the failing build, the logs and the captures.
- [ ] **DBG-30 Fix the cause, not the symptom.**
- [ ] **DBG-31 Make one change at a time,** and test after each one.
- [ ] **DBG-32 Check the fix against the design and the coding standards,** and make sure it does not break anything that depends on the old behaviour.
- [ ] **DBG-33 Do not rush a fix out under pressure** without testing it.
- [ ] **DBG-34 Look for the same mistake elsewhere** in the code.
- [ ] **DBG-35 Run the full regression suite** before you call it done.

**As Markdown.** To copy it into an issue, a pull request or a review record:

````markdown
## Approach
- [ ] **DBG-1 Set a time limit for quick debugging.** When it runs out, stop poking and make a plan.
- [ ] **DBG-2 Check whether someone has already found it.** Search the tracker, the knowledge base and the recent commit history.
- [ ] **DBG-3 Use every tool you have:** the debugger and debug probe, compiler warnings, static analysis, sanitisers, trace and a logic analyser.
- [ ] **DBG-4 Assume the bug is in your code** until you have evidence that it is in the compiler, the operating system or the hardware.
- [ ] **DBG-5 Do not change code you do not understand** in the hope that the problem goes away.
- [ ] **DBG-6 Use more than one technique,** such as bisection, assertions, traces and comparing a good build with a bad one.
- [ ] **DBG-7 Ask for help** when you stop making progress.
- [ ] **DBG-8 Tell people early** if the investigation will take longer than planned.
- [ ] **DBG-9 Know when to step away** and come back with fresh eyes.
- [ ] **DBG-10 Check that the fix cures the cause,** not just the symptom you saw.
- [ ] **DBG-11 Write down what you learnt,** so nobody has to find it again.

## Finding the fault
- [ ] **DBG-12 State a hypothesis** that explains what you see, before the next test run.
- [ ] **DBG-13 Shrink the test case** to the smallest set of steps that still fails.
- [ ] **DBG-14 Reproduce it in more than one way,** or under different conditions.
- [ ] **DBG-15 Gather more data** to choose between competing hypotheses: logs, registers, traces and captures.
- [ ] **DBG-16 Look at what does not fail.** It narrows the search as much as what does.
- [ ] **DBG-17 Think of other explanations** when your first idea does not hold up.
- [ ] **DBG-18 Narrow the search by halves,** with `git bisect` or by switching modules out.
- [ ] **DBG-19 Look at what changed recently** in the code, the configuration and the build.
- [ ] **DBG-20 Widen the search** when the symptom appears far from the cause, as it does with memory corruption.
- [ ] **DBG-21 Test the parts on their own,** adding them back one at a time.
- [ ] **DBG-22 Suspect the code that has had bugs before.**
- [ ] **DBG-23 Add logging and instrumentation** where a debugger would change the timing.
- [ ] **DBG-24 Check the usual suspects:** off-by-one errors, uninitialised variables, stack overflow, integer truncation and a missing `volatile`.
- [ ] **DBG-25 Explain the problem out loud,** line by line, to a colleague or a rubber duck.

## Fixing it
- [ ] **DBG-26 Understand the cause before you edit anything.**
- [ ] **DBG-27 Confirm that the diagnosis explains every symptom,** not just some of them.
- [ ] **DBG-28 Write a test that fails** because of the bug, before you fix it.
- [ ] **DBG-29 Keep the evidence:** the failing build, the logs and the captures.
- [ ] **DBG-30 Fix the cause, not the symptom.**
- [ ] **DBG-31 Make one change at a time,** and test after each one.
- [ ] **DBG-32 Check the fix against the design and the coding standards,** and make sure it does not break anything that depends on the old behaviour.
- [ ] **DBG-33 Do not rush a fix out under pressure** without testing it.
- [ ] **DBG-34 Look for the same mistake elsewhere** in the code.
- [ ] **DBG-35 Run the full regression suite** before you call it done.
````


## Further reading

This checklist follows the debugging checklist in Steve McConnell's *Code Complete* (second edition, Microsoft Press, 2004).
