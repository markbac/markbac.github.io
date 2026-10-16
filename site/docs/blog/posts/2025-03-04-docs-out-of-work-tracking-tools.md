---
date: 2025-03-04T09:17:00
authors:
  - markbac
categories:
  - Documentation
slug: docs-out-of-work-tracking-tools
---

# Why Your Software Documentation Shouldn’t Live in Work Tracking Tools

At some point, most teams have had this experience. A new developer joins, or an architect wants to understand what a system actually *does*. Someone tells them:
*"Just look in Jira."*

<!-- more -->

Or worse, a product manager asks what the **current requirements** are, and the response is,\
*"Check ADO."*

Or Confluence. Or Trello. Or Asana. Or whatever tool your team uses to track work.

This is madness. These tools are **historical records**, not authoritative documentation. They are a **swamp** of old tickets, half-baked ideas, abandoned features, and noise. Digging through them to understand what a system does is like being a history post-doc sifting through centuries of old letters and reports. You’re hoping to piece together what’s *currently true*.

## What’s Wrong with Using Work Tracking Tools as a Source of Truth?

1. **They Are Time-Sensitive Snapshots**

   * A ticket represents a moment in time: what was *planned*, *worked on*, or *completed* at a given point.
   * They *can* show whether a feature was deployed at some point, but that doesn’t mean it still exists in its original form.
   * It won’t easily tell you if another feature later changed, replaced, or removed it.

2. **They Contain Noise and Half-Truths**

   * User stories evolve. Acceptance criteria get rewritten. Bugs are fixed and reopened.
   * Sprint goals change. Requirements shift. People forget to update old tickets.
   * Non-standard workflow use might give hints about whether a feature still exists, but it’s far from reliable.

3. **They Lack Structure for Understanding the System**

   * Even well-organised backlogs don’t provide a clear, coherent view of **what the software does today**.
   * There’s no logical structure—just an ever-growing list of issues sorted by priority or date.

4. **They Mix Future Plans, Current State, and Past Decisions**

   * A ticket might describe a feature that was implemented.
   * Or one that was planned but later scrapped.
   * Or a bug that was fixed, but the feature it relates to no longer exists.

This makes it **impossible** to get a clean, authoritative view of what’s actually in production.

***

## What Should Exist Instead?

### 1. A Controlled, Structured System Document – “What the Software Does”

* This is the **single source of truth** for the current functionality.
* It should be **structured and controlled**, not an ad-hoc wiki that grows into its own chaotic mess.
* Ideal formats include **docs-as-code, structured architectural documentation (e.g., arc42, C4 models, ADRs), or controlled internal documentation systems.**
* Updates to this documentation should be treated **as critical as updates to the code itself**.
* Changes should be **reviewed in the same way as code changes**—as part of the feature development process.

### 2. Current Requirements as a Separate, Defined Document

* A structured, **up-to-date document** describing active requirements, rather than having to reverse-engineer them from ticket statuses.

* Clearly distinguishes between:

  * Features that are currently planned.
  * Features that are implemented and in use.
  * Features that are obsolete or removed.

* This document should be **actively maintained as part of the development process**.

### 3. Architectural Documentation Tied to Features

* High-level architectural documents should be **tied to features or similar groupings**, ensuring they remain relevant and actionable.
* This prevents them from becoming outdated, vague, or disconnected from real implementations.
* Whenever a feature changes in a way that impacts architecture, **the corresponding documentation must be updated alongside the code**.

### 4. Work Tracking Tools as an Archive and Work Tracker (Nothing More)

* Use Jira, ADO, or whatever tool you use for tracking work.
* Keep history, sprint plans, and prioritisation there.
* But **do not rely on it as a definitive source for what the software does**.

***

## The Bottom Line

Work tracking tools are **not** knowledge bases. They are **a swamp of past decisions and half-truths**, and no one should have to wade through them to understand what a system does.

Instead, invest in:

- ✅ A **structured, controlled system document** (what the software does).
- ✅ A **separate, structured requirements document** (what’s needed).
- ✅ **Architectural documentation that stays tied to features**.
- ✅ Treating documentation updates **as critical as code updates**, with the same level of review.
- ✅ Using Jira, ADO, and similar tools **only for work tracking** (not as documentation).

Because no one should need a PhD in backlog archaeology just to understand your software.
