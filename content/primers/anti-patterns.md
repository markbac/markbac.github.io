---
title: Anti-patterns
---

# Anti-patterns

An anti-pattern is a common response to a problem that looks reasonable at the time and turns out badly. Like a design pattern, it has a name, which makes it easier to spot and talk about in a review. Most anti-patterns are not caused by bad engineers; they are what happens to good code under deadline pressure when nobody steps back.

## Structural anti-patterns

| Anti-pattern | What it looks like | The way out |
| --- | --- | --- |
| Big ball of mud | No visible structure; everything calls everything | Find seams, draw module boundaries, enforce them with tooling |
| God object | One class or module that knows and does far too much | Split by responsibility; move behaviour to the data it uses |
| Spaghetti code | Control flow that jumps around with no clear structure | Extract functions, add tests, then restructure |
| Lava flow | Dead or half-finished code that nobody dares remove | Find out what it does, test the behaviour you need, delete the rest |
| Lava layer | Several generations of technology for the same job (three ways to access the database) | Pick one, migrate the others deliberately, finish the migration |
| Shotgun surgery | One logical change needs edits in many places | Bring the scattered knowledge into one module |

[[CAPTION:Table]] Anti-patterns in the structure of code.

## Behavioural anti-patterns

These are about how teams make decisions rather than the shape of the code.

- **Golden hammer**: using a familiar tool for everything, whether or not it fits. The cure is to state the problem before naming the tool.
- **Cargo cult programming**: copying code or practices without understanding why they work. Daily stand-ups with no shared goal, or configuration pasted from a forum, are typical. Ask what each part is for.
- **Premature optimisation**: making code faster, more complex or harder to read before measuring whether speed matters there. Measure first; optimise the hot path; keep the rest simple.
- **Not invented here**: rebuilding something that a well-maintained library already does.

## Spotting them early

Anti-patterns grow slowly, so look for the trends:

- Files or classes that appear in most changes, or that keep growing.
- Changes that need edits in many unrelated places.
- Areas that people avoid or that have no tests.
- Code that nobody can explain in a review.

Static analysis can measure some of this (size, complexity, coupling, duplication). See [static code analysis](static-code-analysis.md).

## Fixing them

Rewrites rarely work. Improve the code in small, tested steps, with each step leaving it working. Michael Feathers' *Working Effectively with Legacy Code* is the standard guide. The strangler fig approach, where new code slowly replaces old code behind a stable interface, works well for larger areas.

Record the decision to tolerate or remove an anti-pattern as [technical debt](technical-debt.md), so it is visible and scheduled rather than forgotten.

## Where next

- [Design principles](design-principles.md) and [design patterns](design-patterns.md) describe what good looks like.
- The [Guides](../guides/index.md) section covers code review and refactoring in more depth.
