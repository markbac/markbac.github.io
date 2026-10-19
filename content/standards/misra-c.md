---
title: MISRA C
---

# MISRA C

*A practical introduction to MISRA C and safe embedded software development*

## What is MISRA?

**MISRA C** is a set of **coding guidelines for the C language**, created to reduce defects in **safety-critical and high-reliability embedded systems**.

It originated from the **Motor Industry Software Reliability Association (MISRA)** in the 1990s, when automotive systems started relying heavily on embedded software for safety.

Since then, MISRA C has become the **de facto standard** for safe C in industries such as:

- automotive
- industrial control
- aerospace
- medical
- defence
- energy metering
- telecoms
- marine/offshore

Wherever **failure matters**, MISRA is commonly used.

## MISRA is Not a Style Guide

A common misconception is that MISRA is about:

- formatting
- naming conventions
- code beauty
- personal preferences

It isn’t.

> **MISRA is a risk-reduction strategy**, not a style guide.

Every rule in MISRA exists because a **pattern of real-world failures** caused injuries, field recalls, safety hazards, or extremely expensive field fixes.

MISRA rules force developers to avoid **dangerous parts of C** — sharp edges in the language that are legal, but unsafe.

Think of MISRA as a **map of known landmines** in C, based on decades of painful history.

## Why We Use MISRA

We use MISRA to:

### Reduce Defects Early

MISRA helps prevent bugs **before they reach production** by limiting:

- undefined behaviour
- implementation-defined behaviour
- poorly-specified type conversions
- dangerous pointer use
- unbounded operations

C gives you a **loaded gun**.\
MISRA makes you **check where it’s pointing**.

### Improve Maintainability

Embedded code outlives the original authors.\
MISRA encourages patterns that are **easy to understand**, so others can safely modify the code without triggering regressions.

### Improve Portability

C behaves differently on different compilers and architectures.\
MISRA avoids features that depend on compiler-specific behaviour, so code works reliably on:

- different MCUs
- different compilers
- different optimisation levels

### Support Certification and Audit

For any regulated or quality-critical product, MISRA is accepted as **evidence** that the development team:

- uses industry best practice
- applies static analysis
- controls risk in software design

It provides a **defensible engineering position**.

## What MISRA Covers (High Level)

MISRA C focusses on **dangerous or ambiguous aspects of C**, for example:

- implicit type conversions
- signed/unsigned arithmetic
- pointer aliasing
- volatile access
- use of dynamic memory
- unreachable code
- data race risks
- unsafe casts
- recursion
- uninitialised variables
- hidden side-effects
- multiple exit points
- direct hardware access without structure

It defines rules like:

- “Do not cast away const”
- “No implicit arithmetic promotion”
- “Use explicit types for width”
- “No hidden side-effects in macros”

You don’t need to memorise every rule.\
You need to understand **why the rule exists**.

## The Most Important Mindset

### Fix the Cause, Not the Warning

When a MISRA rule is broken, the question is not:

> “How do I silence the violation?”

It is:

> **“What risk is this warning signalling?”**

MISRA violations are often **symptoms** of deeper design issues:

- wrong types
- wrong ownership model
- wrong interface contract
- pointer lifetime issues
- unsafe implicit conversion
- silent truncation / overflow
- race condition between ISR and task

A **cast** or **suppression** may hide the violation, but it also hides the **actual safety problem**.

#### Example Anti-Pattern

**Bad “fix”:**

```ini
value = (uint16_t)data;   // cast added to silence MISRA
```

Underlying problem:\
`data` is a 32-bit value that may overflow `uint16_t`.

A cast doesn’t fix it — it hides it.

**Good fix:**\
Define the right type:

```cpp
uint16_t value = clamp_value(data, UINT16_MAX);
```

Or fix the interface so the API returns the correct width.

## How to Approach MISRA Violations

Every MISRA violation fits one of **three categories**:

### Real Defect

MISRA highlights an actual bug:

- uninitialised variable
- out-of-bounds write
- incorrect signedness
- potential overflow

**Fix the bug.**

### Design Problem

MISRA exposes a **design flaw**:

- wrong type design
- unclear ownership
- unsafe pointer hand-off
- duplicated logic in different modules
- implicit dependency on optimisation level

**Fix the design**, not the line.

### Acceptable Deviation

Sometimes the **pattern is valid** in embedded work:

- hardware register access
- memory-mapped IO
- controlled interrupt behaviour
- vendor HAL abstractions
- toolchain limitations

In these cases:

- use a **local deviation** with explanation
- clearly document the **technical rationale**
- keep it **visible**, not hidden

## Deviations (When You Must Break a Rule)

MISRA does **not** expect zero violations.\
It expects:

- violations are **known**
- violations are **justified**
- violations are **local**
- violations are **documented**
- violations do **not hide risk**

Example good deviation note:

> **Deviation — MISRA Rule 11.3**\
> `uint8_t*` cast to `volatile uint8_t*` for direct hardware register access.\
> Access is atomic. No aliasing.\
> Required due to vendor register model.

This gives **context for the next developer**.

Avoid suppression like:

```cpp
/* MISRA ignore */
```

That helps nobody.

## Practical Tips for Developers

### Understand the Tool Output

Static analysis tools report:

- the **rule violated**
- the **reason**
- the **code location**

Always read **the rationale**, not just the rule title.\
MISRA includes **why the rule exists**.

### Fix Types, Not Call Sites

If you see repeated casts, clamps, or masks:

- the **API is wrong**

Example:

Instead of casting 100 times:

```scss
send((uint8_t)value);
```

Fix the interface **once**:

```cpp
void send(uint8_t value) { … }
```

This reduces **both safety risk and static analysis noise**.

### Respect Hardware

In embedded software, violations often link to hardware behaviour:

- `volatile` is required
- memory is not flat
- registers are not normal variables

Sometimes MISRA **must be deviated** to express hardware behaviour correctly — but document it.

### Learn the Common Patterns

A few patterns reoccur constantly:

- Table-driven state machines\
  (instead of scattered logic)

- Fixed-width integer types\
  (`uint16_t`, `uint32_t`)

- Avoid dynamic memory\
  (prefer static allocation)

- Avoid side-effects in macros
- Single responsibility functions

These patterns tend to be **MISRA-friendly** naturally.

## What MISRA Does *Not* Solve

MISRA reduces risk, but it does not guarantee:

- correctness of logic
- performance
- that your design is good
- that someone won’t misuse the API
- that a race condition won’t slip through
- that all edge cases are tested

MISRA + **strong reviews** + **testing discipline** is the correct combination.

## Responsibilities During Code Review

When reviewing MISRA findings:

A reviewer should ask:

- What risk is MISRA pointing to?
- Is there a better design?
- Does the change introduce future technical debt?
- Is the suppression safe and justified?
- Why does the current interface require a cast?
- Does this break blocking or timing?

Approach the issue with **curiosity**, not accusation.

## MISRA in Our Workflow

In a modern embedded pipeline:

- MISRA is run **automatically** in CI
- MISRA is run **locally** before PR
- MISRA must be **green** for merge
- Deviations must be **documented**
- Static analysis reports are **stored**
- New warnings are **blocked**

The CI pipeline is **evidence** for requirement closure.

## Learning MISRA Quickly

You do **not** need to memorise every rule.\
Focus on:

- the **common patterns**
- why the rules exist
- what risks they address

Over time:

- you will naturally write MISRA-clean code
- the mindset becomes automatic

The best MISRA developers rarely talk about “MISRA rules”, they talk about **safe C**.

## Short Summary (For Your Desk)

**MISRA is:**

- a **safety strategy**, not a style guide
- a **map of how C has failed in practice**
- a way to **prevent bugs before they happen**
- a method to create **evidence for testing**
- a tool to support **maintainability**

**When MISRA fails:**

- fix the cause, not the warning
- redesign the **interface**, not the call-site
- deviations must be **justified**, not hidden
- keep violations **local and visible**

## Recommended Reading (Optional)

If you want to dive deeper:

- *MISRA C:2012 Guidelines* (official)
- *Beyond MISRA: Designing Safe C Interfaces* (Barr Group webinars)
- *Effective C* — Robert Seacord
- *Best Kept Secrets of Peer Code Review* — SmartBear
- *Clean Code* — Robert Martin (concepts only)
- *Code Complete* — Steve McConnell

And for deeper safety context:

- ISO 26262-6 (Embedded Software)
- IEC 61508-3
- CERT C Secure Coding Standard

## Final Thought

> **Writing MISRA-compliant code is less about following rules and more about thinking clearly.**\
> If you understand **why** a rule exists, you’ll follow it naturally.

MISRA is not the goal — **reliable, safe software** is the goal.
