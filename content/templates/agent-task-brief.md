---
title: Task brief for an AI agent
---

# Task brief for an AI agent

An AI coding agent does better work with a short, specific brief than with a long conversation. The brief below gives it a goal, the boundaries, a definition of done and the points where it must stop and ask. It also says what to report, so a person can review the result quickly.

Standing rules, such as build commands, folders it must not touch and coding conventions, belong in the repository's `AGENTS.md` (or the agent's own instruction file). The brief covers only this task.

## Template

```markdown
# Task: short title

## Goal

One or two sentences: the outcome wanted, and why.

## Requirement and context

- Requirement IDs: REQ-...
- Related ADRs: ADR-...
- Files or areas in scope:

## Constraints

- Do not touch (as well as the boundaries in AGENTS.md):
- Keep the change as small as it can be. Do not refactor beyond the task.
- Prefer the simple solution. State any assumption rather than guess.

## Definition of done

- Build, tests and lint pass locally, using the commands in AGENTS.md.
- Tests added or updated, and named after the requirement IDs.
- Documentation updated.
- Commits and pull request follow the conventions, with `Refs:` and
  `Assisted-by:` trailers.

## Ask first if

- The change needs a new dependency, an interface change or an ADR.
- A requirement is missing, unclear or contradicts another.
- Anything touches a boundary listed in AGENTS.md.

## Report back

- What you did and why.
- Assumptions you made.
- Risks and anything left undone.
- Evidence: test and analysis output.
```

Review the agent's work as you would a colleague's: against the [code review checklist](code-review-checklist.md), with the same bar for tests and evidence.
