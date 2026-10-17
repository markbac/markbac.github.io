---
title: Design principles
---

# Design principles

A handful of principles turn up in almost every conversation about code quality. None of them is a law. Each one is a rule of thumb that pushes against a common way for code to go wrong, and each one can be overdone.

## SOLID

Robert C. Martin gathered five principles for object-oriented design under the SOLID acronym. They apply just as well to modules and services.

| Principle | In one line | What it prevents |
| --- | --- | --- |
| Single responsibility | A module should have one reason to change | Classes that change for unrelated business reasons |
| Open/closed | Extend behaviour by adding code, not by editing working code | Every new case touching the same `switch` statement |
| Liskov substitution | A subtype must work wherever its parent type works | Subclasses that throw "not supported" or quietly change the meaning |
| Interface segregation | Many small interfaces beat one large one | Clients depending on methods they never call |
| Dependency inversion | Depend on abstractions; let the details depend on them too | Business logic that imports the database driver |

[[CAPTION:Table]] The SOLID principles.

Dependency inversion is the one with the biggest effect on architecture: it is what makes [hexagonal architecture](hexagonal-architecture.md) and easy unit testing possible.

## DRY, KISS and YAGNI

- **DRY (Don't Repeat Yourself)**: every piece of knowledge should have one authoritative home. It is about knowledge, not text. Two functions that look alike but change for different reasons are not duplication, and merging them couples things that should stay apart.
- **KISS (Keep It Simple)**: choose the simplest design that does the job. Clever code costs more to read, test and debug than it saves.
- **YAGNI (You Aren't Gonna Need It)**: do not build for requirements you only imagine. Speculative flexibility has a cost today and usually guesses the future wrong.

## Other principles worth knowing

- **Separation of concerns**: keep different kinds of work (presentation, business rules, storage) in different places.
- **High cohesion, low coupling**: things that change together live together; things that change apart talk through narrow interfaces.
- **Composition over inheritance**: build behaviour by combining small objects rather than deep class trees.
- **Least astonishment**: an interface should do what its name suggests.
- **Fail fast**: detect bad input or state at the boundary and stop, rather than carrying it deeper.

## Using them well

Principles are for judging trade-offs, not for winning arguments. A useful habit is to name the change you expect: "if we add a second payment provider, how many files change?" That question applies SOLID and DRY without anyone needing to quote them.

## Where next

- [Design patterns](design-patterns.md) and [anti-patterns](anti-patterns.md) show the principles applied and ignored.
- The [Guides](../guides/index.md) section covers coding standards in more depth.
