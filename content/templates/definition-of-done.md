---
title: Definition of Done
---

# Definition of Done

A work item is done when it could be released without anyone doing anything more to it. This applies to stories, bug fixes, features and technical tasks alike. The list sets the minimum quality bar for the team.

"Merged" is not the same as "done". Work that still needs testing, documentation or a release note is not finished.

## Checklist

- [ ] **DoD-1 The code builds without warnings** on every target, with warnings enabled.
- [ ] **DoD-2 The developer has tested it.** Unit tests cover the change, including edge cases and error paths, and it has been run locally or on target.
- [ ] **DoD-3 It meets the acceptance criteria.** Someone other than the author has checked it against them and against the test scenarios.
- [ ] **DoD-4 It has been reviewed.** A peer has reviewed the change against the [code review checklist](code-review-checklist.md), and the comments are resolved.
- [ ] **DoD-5 It follows the coding standards** for formatting, naming and structure.
- [ ] **DoD-6 The CI pipeline passed.** The build, static analysis and automated tests all pass in CI, not just on a laptop.
- [ ] **DoD-7 The documentation is updated.** Design notes, interface specifications, user help and release notes match the change.
- [ ] **DoD-8 Technical debt is recorded.** Any shortcut or known problem has a ticket, or a note on the story that points to one.

## Extra items to consider

Add these when your product, domain or regulator needs them:

- [ ] A security review is complete.
- [ ] Performance, memory or power measurements are within budget.
- [ ] Code coverage meets the agreed threshold.
- [ ] The customer or user has accepted the change.
- [ ] New behaviour sits behind a feature flag, with a plan to remove the flag.

**As Markdown.** To copy it into an issue, a pull request or a review record:

````markdown
## Checklist
- [ ] **DoD-1 The code builds without warnings** on every target, with warnings enabled.
- [ ] **DoD-2 The developer has tested it.** Unit tests cover the change, including edge cases and error paths, and it has been run locally or on target.
- [ ] **DoD-3 It meets the acceptance criteria.** Someone other than the author has checked it against them and against the test scenarios.
- [ ] **DoD-4 It has been reviewed.** A peer has reviewed the change against the [code review checklist](code-review-checklist.md), and the comments are resolved.
- [ ] **DoD-5 It follows the coding standards** for formatting, naming and structure.
- [ ] **DoD-6 The CI pipeline passed.** The build, static analysis and automated tests all pass in CI, not just on a laptop.
- [ ] **DoD-7 The documentation is updated.** Design notes, interface specifications, user help and release notes match the change.
- [ ] **DoD-8 Technical debt is recorded.** Any shortcut or known problem has a ticket, or a note on the story that points to one.

## Extra items to consider
- [ ] A security review is complete.
- [ ] Performance, memory or power measurements are within budget.
- [ ] Code coverage meets the agreed threshold.
- [ ] The customer or user has accepted the change.
- [ ] New behaviour sits behind a feature flag, with a plan to remove the flag.
````


## Where to use it

- In the pull request template, as the checklist the author ticks (see the [pull request template](pull-request-and-commits.md)).
- As a checklist on the ticket in your tracker.
- As a gate in the CI pipeline, for the items a machine can check.
- In sprint reviews and retrospectives, when the team discusses what slipped through.

## Common problems

- Treating "merged" as "done", so testing and documentation drift into the next sprint.
- Pushing unreviewed code to meet a deadline.
- Relying on manual testing where an automated test would do the job every time.

Review the list every few months, or when a retrospective shows it missed something. Pair it with the [Definition of Ready](definition-of-ready.md).
