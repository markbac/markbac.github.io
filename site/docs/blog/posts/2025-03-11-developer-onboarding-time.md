---
date: 2025-03-11T10:18:00
authors:
  - markbac
categories:
  - Engineering practice
  - Embedded
slug: developer-onboarding-time
---

# How Long Should It Take for a Developer to Be Productive?

Bringing a new developer onto a project—especially something as complex as an **embedded C application**—is always a balance. You want to **get them up to speed quickly** and ensure **they learn the right way to do things**. But how long should it actually take before they can **fix bugs, add features, and contribute effectively**? And if it’s taking months, what does that say about the project?

<!-- more -->

Let’s break this down.

***

## Expected Timeline for a New Developer’s Productivity

Assuming the developer has relevant experience in **C, embedded systems, and your toolchain**, a reasonable onboarding timeline should look like this:

* **Day 1-2:**

  * Setting up the development environment.
  * Getting access to repositories, build tools, debuggers.
  * Running and testing the application.

* **Week 1:**

  * Understanding the overall architecture.
  * Reading key documentation.
  * Fixing a trivial bug or tweaking a simple feature.

* **Weeks 2-4:**

  * Fixing small-to-medium issues.
  * Navigating the codebase comfortably.
  * Contributing to code reviews.
  * Becoming familiar with testing/debugging workflows.

* **Weeks 4-8:**

  * Adding minor features independently.
  * Debugging and resolving more complex issues.
  * Developing a deeper understanding of critical components.

* **2-3 Months:**

  * Capable of handling major features.
  * Able to make architectural suggestions.
  * Working independently with minimal oversight.

If a developer is still struggling after a **few months**, it’s usually a **process, documentation, or technical debt issue**, not a problem with the developer.

***

## What Should Help a Developer Get Up to Speed?

The goal should be to **enable a new developer to become productive with minimal hand-holding**. Support from experienced engineers should be reserved for **reviewing code, discussing architecture, and resolving nuanced issues**—not walking someone through setting up their dev environment.

### 1. High-Quality Documentation

New developers should be able to get the **big picture** and start solving small problems without repeatedly asking for guidance. This requires:

✅ **High-Level Architecture Docs**

* How the system is structured (**C4 model diagrams** help).
* Key components and their responsibilities.
* How data flows through the system.

✅ **Developer Guides**

* How to set up the environment **without manual intervention** (e.g., a `setup.sh` script).
* How to build and run the software.
* Debugging workflows, common pitfalls, and how to test code properly.

✅ **Codebase Overview**

* Which modules do what?
* Where to start looking for specific functionality.
* Code conventions, coding standards, and best practices.

✅ **API References & Key System Interactions**

* If the embedded application interacts with other systems (e.g., a cloud API or another device over UART/SPI/I2C), there should be **clear API documentation**.

✅ **ADR (Architecture Decision Records)**

* Why certain decisions were made—so developers don’t keep questioning past choices.

If a new developer can’t figure something out within a day by reading documentation, **it’s a failure of the documentation**.

***

### 2. Well-Defined Development Environment

A new developer should **not** spend their first few days just trying to get the system to build. The process should be **as automated as possible**:

* **A single script to set up everything** (e.g., `setup.sh` or Docker-based environments).
* Clear documentation for manual setup (if needed).
* A **working emulator or hardware access**—developers should be able to test changes **without waiting for rare, expensive hardware**.
* **Automated builds and tests**—a CI/CD pipeline should **catch common issues early** so they don’t have to waste time troubleshooting build failures.

If a developer spends more time **configuring their toolchain than writing code**, you have a process problem.

***

### 3. Clear Codebase and Modularity

A messy codebase can turn onboarding into a nightmare. A few things that help:

- ✅ **Consistent coding standards** – Everyone should follow the same style and conventions.
- ✅ **Clear separation of concerns** – Avoid spaghetti code where everything is interconnected.
- ✅ **Well-structured repository** – Clear folder structure, meaningful file names, and logical module separation.
- ✅ **Inline documentation** – Code should be self-explanatory, but **critical sections should have comments** explaining *why* something is done a certain way.

***

### 4. Structured Onboarding Tasks

Instead of throwing a new developer into the deep end, they should work through **progressively more complex tasks**:

1️⃣ **First task:** Run and debug the software. Fix a trivial bug or tweak something simple.\
2️⃣ **Next:** Fix a small but meaningful bug.\
3️⃣ **Then:** Add a minor feature, ensuring it’s tested properly.\
4️⃣ **Finally:** Handle something more complex (e.g., a non-trivial bug or refactoring task).

Each of these should be **manageable without deep system knowledge**, allowing them to get familiar with the code **without relying on experienced engineers too much**.

***

### 5. Experienced Support for Nuanced Aspects

While new developers should be **self-sufficient for basic onboarding**, experienced engineers should provide:

* **Code Reviews** – Ensuring best practices are followed and bad patterns are avoided early.
* **Guidance on Architectural Decisions** – Helping them understand the deeper trade-offs in the system.
* **Debugging Help (if truly needed)** – Some embedded issues (timing bugs, memory corruption) **aren’t obvious and need experience** to solve.

However, **mentorship should not mean babysitting**—if they can’t figure out **basic** things on their own, that suggests the documentation and onboarding process need improvement.

***

## What If It’s Taking Months for a Developer to Be Productive?

If a developer still can’t contribute after **weeks or months**, it’s usually a sign of one or more of the following:

- ❌ **Lack of good documentation** – They’re stuck constantly asking questions because nothing is written down.
- ❌ **Messy codebase with high technical debt** – If fixing small bugs requires deep tribal knowledge, that’s a sign of a **fragile, poorly-structured system**.
- ❌ **Siloed knowledge** – If only a few developers “know how things work,” it suggests **a failure in knowledge sharing**.
- ❌ **Complex, undocumented build systems** – If it takes weeks just to get the code running, it’s **not the developer’s fault**—it’s a problem with the setup process.
- ❌ **Poor onboarding process** – If new developers aren’t given structured tasks and expectations, they can’t learn effectively.

**A well-run team should have a new developer fixing small bugs within the first 1-2 weeks.** If they’re still struggling after **months**, something is broken in the **process, documentation, or system design.**

***

## Final Thoughts

Getting new developers productive quickly isn’t just about their ability—it’s about **how well the project supports onboarding**.

- ✅ **Good documentation and self-serve resources** mean they can ramp up independently.
- ✅ **A streamlined dev environment** means they aren’t wasting days fighting build issues.
- ✅ **A well-structured codebase** means they don’t need to reverse-engineer the system to make simple changes.
- ✅ **Clear onboarding tasks** mean they gradually build confidence rather than being overwhelmed.
- ✅ **Experienced engineers should help with nuanced issues, not basic setup.**

If onboarding is slow, **don’t blame the developers—fix the process.**
