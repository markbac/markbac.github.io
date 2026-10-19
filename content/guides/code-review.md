---
title: Reviewing code
---

# Reviewing code

**How to think about code, how to read it, and how to give feedback that makes the code and the team better**

> [!NOTE] Companion Checklist
> This document teaches the **Philosophy, Mindset, and Reading Technique** for peer review. For the concrete, itemised checklist to verify pull requests against (Functionality, Style, Architecture, Concurrency, Safety), see the companion [GU-002: Code Review Checklist](../templates/code-review-checklist.md).

## Roles and responsibilities

### Author (PR owner)
You own:
- Scope and clarity of the PR
- Tests and evidence
- Addressing comments (or explicitly disagreeing with a reason)
- Keeping it small enough to review

### Reviewer
You own:
- Reading it properly (not rubber-stamping)
- Identifying risk and asking the right questions
- Being specific and constructive
- Replying promptly (or saying when you can’t)

### Maintainer / Approver (if different)
You own:
- Merge decisions
- Enforcing repo quality gates
- Making sure the change fits the roadmap/architecture

## A Code Review is Not a Hunt for Faults

Bad reviews are driven by:

> “I am here to point out mistakes.”

Good reviews start from:

> “I’m here to understand the intent, help improve the design, and make the product safer.”

**You are reviewing *with* the author**, not *against* them.\
Think “pair-design-audit”, not “police investigation”.

A code review has three goals:

1. Correctness: does it do what was intended?
1. Maintainability: can someone else understand and change it safely later?
1. Risk reduction: are we introducing hidden technical debt, regressions, timing issues?

Note: **you are not judging the developer**, you are judging the **future cost** of the change.

The best reviewers are calm, curious, and collaborative.

## Don’t Read Code — Understand It

We are all taught to **read code line by line**.\
This is the slowest and least effective way to review.

Great reviewers **start at the top**:

### Start with Context

Before looking at the first line, ask:

- What is the problem being solved?
- What requirement or bug is this linked to?
- What is the design intent?
- Where does this fit in the architecture?
- Is this a new behaviour, a change, or a refactor?

If you cannot answer those **without opening the diff**, the PR isn’t ready.

A clear PR description saves hours:

- Why this change exists
- What the solution approach is
- What was considered and rejected
- Any known limitations
- What needs special attention

> **Tip:** If you don’t understand the intent after reading the PR description, stop. The review isn’t a guessing game.

## Read the Code as a Story, Not as Text

Good reviewers read code **in layers**:

### Layer 1 — High-Level Design

Look at:

- the data flow
- the abstractions
- module boundaries
- the decisions in the PR description

Ask:

- Is this solution **simple and obvious**, or **clever and mysterious**?
- Are there obvious alternative shapes that are more readable?

If you disagree with the **shape**, don’t bother nitpicking variable names — fix the foundation first.

### Layer 2 — Interfaces and Contracts

Check **function boundaries**, not internals:

- What goes in?
- What comes out?
- What is guaranteed?
- What happens in errors?
- How are side effects handled?

**Great design is visible at the interfaces.**

### Layer 3 — Internal Logic

Only **after** you understand the shape, examine key branches:

- difficult logic
- multi-step algorithms
- error paths
- concurrency primitives

This is where bugs hide.

Avoid reading **every line** unless the change is tiny.

> **Practitioner rule:** You don’t need to read everything — you need to read the **right 15%**.

## Mindset: Curious, Not Cynical

Poor reviews are full of statements:

> “This is wrong.”\
> “Why did you do it like this?”

Good reviews ask:

> “What trade-off made this the right solution?”\
> “Help me understand why we avoid approach X?”\
> “Is there a simpler way?”

Assume the author did the **best they could** with the information at the time.

Treat the review like a **joint investigation**, not an exam.

## The Soft Skills Matter More Than the Code

The **best reviewers**:

- ask questions
- explain reasoning
- avoid sarcasm or power plays
- propose alternatives
- leave final editorial decisions to the owner (unless safety is involved)

Example good phrasing:

- “Would we gain clarity if we extracted this loop?”
- “This reminds me of pattern X — could we use it?”
- “If we hit error here, does it leak resources?”
- “I don’t fully understand the boundary conditions — can we add one more test?”

Example bad phrasing:

- “This is wrong.”
- “Why didn’t you use pattern X? Everyone knows that.”
- “Looks ugly.”

Feedback is **instruction + reasoning**, not judgement.

## Think in Terms of Risk

A big mistake in reviews is treating everything as equal.

Not all lines carry the same risk.

Ask yourself:

- Could this cause a crash?
- Could this silently corrupt data?
- Could this break timing or deadlines?
- Could this cause a security issue?
- Could this cause later maintenance pain?

Review time is **finite**. You must **spend it where risk matters**.

Examples of **high-risk areas**:

- cryptography
- error paths
- time-critical code
- concurrency primitives
- memory allocation
- FOTA upgrade logic
- state machines
- hardware register access
- untested legacy paths
- safety logic

Examples of **low-risk**:

- formatting
- naming style
- unimportant internal helper changes

Correctness > Maintainability > Cleanliness.

Fix **critical things** first.

## Know Your Cognitive Limits

Your brain tires quickly doing deep code analysis.\
Most people can review **60–90 minutes total per day** before quality drops.

SmartBear’s research shows:

- defect discovery rate falls sharply after \~500 LOC per review session
- small reviews catch more serious bugs

So:

- prefer small PRs
- review in short bursts
- never push through fatigue

If a PR is **too big** to understand comfortably, that’s a **process failure**, not a reviewer failure.

## Avoid Reading the Code in Diff Mode First

Diffs ruin your brain.\
They show changes **out of context**, and your eyes chase **red/green noise**.

Ideal order:

1. PR description
1. Design/architecture doc snippet (if provided)
1. Browse whole files (understand shape)
1. Only then read the diff

You are here to **understand**, not mechanically inspect edits.

## Look for Intent Signals

In good code, you can answer:

- What is this doing?
- Why is it this shape?
- What are the trade-offs?
- What if it fails halfway?

Look for signals of intention:

- clear names
- limits checked
- error paths defined
- tests that show prescribed behaviour

If intention is unclear, request a comment that explains **why**, not **what**.

Example good comment:

> “We use polling here instead of interrupts because the hardware module is unstable during self-test.”

## Embed Test Thinking

When you read code, **imagine how you would break it**:

- what if input is zero?
- what if message arrives out of order?
- what if timer triggers early?
- what if the UART drops bytes?
- what if pointer is NULL?
- what if config is wrong?
- what if battery drops during FOTA?

If the author hasn’t tested these scenarios, note it.

Great review feedback:

> “Can we add a test for when the sensor returns invalid data?”

Not:

> “Your code doesn’t handle invalid data.”

(Same point, very different reception.)

## Separate Design Feedback from Style Feedback

If you mix:

- architectural critique and
- formatting nitpicks

in the same message stream, the important stuff gets lost.

Order your feedback:

1. design issues
1. correctness issues
1. edge cases
1. style and clarity

If you start with “spacing”, your mindset is in the wrong place.

## Favour Simplicity Over Cleverness

If you see clever patterns that save 4 lines but add 4 hours of future debugging, change them.

The reviewer’s job is to represent the **future reader**, not the current author.

Quote from *Clean Code*:

> “Always code as if the person who ends up maintaining your code is a violent psychopath who knows where you live.”

Funny, but true — in embedded work, somebody will debug your code in 2 years under pressure with poor tools.

Make it easy for them.

## Don’t Force Your Preferences

You will see code that **isn’t how you would write it**, but is still correct, clear, and safe.

If it’s **different, but good enough**, let it go.

Reserve push-back for:

- correctness
- clarity
- maintainability
- risk
- safety

Not personal taste.

Good review comment:

> “I prefer A, but B is fine and safe — no change required.”

## Ask for Tests When They Matter

When reading tricky logic, ask:

- Where is the test for the pathological case?
- Where is the test for invalid input?
- Where is the test for low battery?
- Where is the test for overflow?

In embedded projects, **unit tests cannot cover everything**, but they must cover **logic**, not **hardware access**.

Encourage **state-based tests**, **table-based tests**, and **simplifying flags** that drive behaviour.

## Use the Checklist as a Safety Net

Once you’ve done the **thinking part**, use your checklist to check you haven’t missed subtle issues.

Your checklist is excellent for this purpose.\
(Referencing the user’s checklist here)\
The checklist gives the **mechanical completeness check**, not the **thinking**.

Example:\
**Did we check that every input is validated?**\
→ Checklist confirms.

But the **insight** comes from the reviewer’s **mental model**.

Checklist is the **seatbelt**, not the **driver**.\
GU-002-code\_review\_checklist

## Adopt a Review Routine

Here’s a **5-step routine** that builds skill:

1. Read the PR description
1. Trace the feature from requirement → code\
   understand intent

1. Review high-level design
1. Drill into key logic paths
1. Run the checklist pass

This **separates thinking from checking**.

## Recognise When to Stop

If design is wrong at the architectural level:

- stop reviewing line-by-line
- request design update first

Example:\
re-implementing a state machine in multiple places.\
No amount of formatting will save that.

## Your Role is to Raise Awareness, Not Demand Perfection

Sometimes you find an issue that **could** be improved, but does not block correctness, safety, or clarity.

In those cases:

- raise it
- explain your reasoning
- leave decision to author

This builds trust and encourages review participation.

## Build a Positive Culture

Good review habits in teams:

- thank people for thoughtful feedback
- praise good patterns explicitly
- acknowledge improvements
- model behaviour for juniors
- ask questions more than give orders
- treat review as **mentoring**, not policing

Review should feel like **a technical conversation**, not an interrogation.

## Conclusion – The Reviewer’s Mindset

At the end of a review, ask yourself:

- Do I understand what this code does?
- Do I understand why it is shaped this way?
- Would I be comfortable owning this code?
- If I modify this in six months, would I be safe?
- Would I bet the product on this behaviour?

If the answer is yes on all, approve.

If the answer is no:

- help the author close the gap.

## Practical Advice Summary

- Start at the **design**, not the diff
- Understand **intent** before nitpicking
- Review in **layers**
- Think **risk-based**
- Work in **short sessions**
- Use the **checklist last**
- Ask questions instead of accusing
- Optimise for **future readability**
- Keep **personal style** separate from quality
- Encourage **tests where logic demands it**
- Focus feedback on **behaviour**, not **style**

## Pull request descriptions

Give reviewers the context before they read a line of code. Use the [pull request template](../templates/pull-request-and-commits.md) in the Templates section, and keep it in the repository as `.github/pull_request_template.md` or your host's equivalent.

## Example Comments (Good vs Bad)

This teaches the **tone** and **behaviour** expected.

### Bad Comments

Author will feel judged, not supported:

- “This is wrong.”
- “Why didn’t you just follow X pattern?”
- “This makes no sense.”
- “Fix your formatting.”
- “We always use approach Y.”
- “You don’t understand state machines.”

### Good Comments

Same outcome, better communication:

- “Could you explain why this approach was chosen over X?”
- “I’m unsure what happens on the error path if the pointer is null — could we clarify it?”
- “Would extracting this loop into `process_message()` make sequencing clearer?”
- “If `returnCode != 0`, do we leak resources here?”
- “If we follow the existing state machine pattern, this might be simpler — thoughts?”
- “Could we add one test for the negative path? I think it would protect against regression.”

### Excellent Comments (Mentoring tone)

You are teaching **thinking**:

- “This looks like the same pattern we used in `module_x`. If we reuse it, we gain consistency and reduce risk.”
- “This logic is clever but hard to read. Could simplicity help here even if it costs a few lines?”
- “If this value crosses ISR boundary, we may need atomic access — what do you think?”
- “This approach is good. In a future refactor, we might consider extracting a table-driven state machine — not blocking now.”

## One-Page Training Card (Printable)

**Title:** *How to Review Code (Embedded Systems & MISRA)*

### Mindset

- You review **intent**, not just syntax
- Assume **competent author**
- Ask questions, don’t attack
- Aim for **safer**, **simpler**, **clearer**

### Review in Layers

1. Why does this change exist?\
   (read PR description)

1. What is the design shape?\
   (read high-level diff)

1. Where are the risks?\
   (timing, memory, state)

1. Check logic paths\
   (especially error handling)

1. Run checklist pass\
   (MISRA, boundary conditions)

### What Matters

- Correctness
- Safety
- Maintainability
- Simplicity
- Risk reduction

**NOT**:

- personal taste
- stylistic details first

### Ask Yourself

- Would I be comfortable owning this?
- Is behaviour obvious from reading it?
- Are failure paths safe?
- Does it follow existing patterns?
- Could this crash in production?

### Common Traps

- Reviewing everything equally
- Reading diff first
- 2-hour review sessions
- Fighting style wars
- Ignoring error paths
- Cleverness over clarity

### Embedded Safety Focus

- Atomic access (interrupts)
- Overflow and wrap behaviour
- State machine consistency
- Hardware side-effects
- Memory budgets
- FOTA stability path
- Watchdog handling

### Quality Principle

> *Simple code is safer.*

## Team Rules for Review Etiquette

These are **team agreements** — not optional.

### We agree that

1. Reviews are collaborative, not confrontational
1. Feedback is **specific**, **actionable**, and **reasoned**
1. Ask questions instead of issuing commands
1. Avoid **tone policing** or sarcasm
1. Highlight **positive choices**
1. If design shape is wrong, **stop**, don’t nitpick
1. Split large PRs — **small units** are safer
1. Everyone is **teaching and learning**
1. Decisions are recorded in **PR discussion**, not lost in chat
1. Respect **DoR — Ready for Review gate**
1. Code must meet **minimum safety gates**, not personal taste
1. If discussion is stuck, **pair-review** the solution
1. The reviewer must imagine **future cost**, not current ease

## Bibliography / Recommended Reading

A curated list relevant to **embedded, safety, and review technique**.

### Books

- Best Kept Secrets of Peer Code Review — SmartBear (Rigby & Bird)\
  Practical, research-based, not fluff.

- Code Complete — Steve McConnell\
  Still the best general text on how to reason about code.

- Clean Code — Robert C. Martin\
  Opinionated, but useful for readability thinking.

- Clean Architecture — Martin\
  Good for thinking about module boundaries.

- Rapid Development — Steve McConnell\
  Project perspective; risk thinking.

- Peopleware — DeMarco & Lister\
  Culture and psychology.

- Software Engineering at Google — Winters, Manshreck, Wright\
  Modern review culture and tooling thinking.

- Effective C — Robert Seacord\
  Better C habits; relevant for embedded.

- Embedded C Coding Standards — Michael Barr / Netrino\
  Good alignment with MISRA thinking.

### Papers / Short Material

- “Modern Code Review: A Case Study at Microsoft” — Rigby, Bird
- “Best Kept Secrets of Peer Code Review” (SmartBear research summaries)
- Fagan Inspection Process — original IBM research
- SEI material on inspections and defect removal efficiency

### Standards / Guidelines

- MISRA C:2012 + Amendments\
  Not just rules, but rationale.

- ISO 26262-6 (Software)\
  Functional safety thinking.

- IEC 61508-3\
  General industrial functional safety.

- EN 50128\
  Railway safety software (good patterns).

- Barr Embedded C Rules

### Web Resources

- NASA Coding Guidelines
- CERT Secure Coding Guidelines for C
- Barr Group webinars (state machines, safety patterns)
