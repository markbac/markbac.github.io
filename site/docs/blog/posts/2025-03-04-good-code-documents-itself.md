---
date: 2025-03-04T09:26:00
authors:
  - markbac
categories:
  - Documentation
  - Engineering practice
slug: good-code-documents-itself
---

# "Good Code Documents Itself!"—No, It Really Doesn’t

There’s a popular mantra among developers: *“Good code documents itself!”* It sounds nice, doesn’t it? A world where code is so clean, structured, and intuitive that it magically explains itself.

<!-- more -->

Except that’s not reality. In truth, this phrase is often just shorthand for *“I don’t want to write documentation.”*

***

## Why "Self-Documenting Code" is a Myth

### 1. Code Tells You *What*, Not *Why*

* Code shows *what it does*, but it rarely explains **why** it was written that way.
* Why was this algorithm chosen over another?
* Why does this function have a strange edge case?
* Why does this state transition exist?

If those answers aren’t written down somewhere, they get lost over time.

### 2. Code Doesn’t Explain System-Level Behaviour

* A function or class may be readable, but that doesn’t explain how **all the moving parts fit together**.
* APIs, modules, services, and external dependencies interact in ways that **aren’t obvious from reading the code**.
* System architecture, data flow, and error-handling strategies often need **separate documentation**.

A well-structured monolith might be easy to follow, but a **distributed cloud application** with multiple microservices? Not so much.

### 3. Concurrency, Timing, and State Are Hidden

* **Interrupt-driven** systems and **real-time tasks** introduce behaviour that isn't clear in the code.
* Race conditions, thread synchronisation, and DMA buffer access can **lead to obscure, timing-sensitive bugs**.
* A **state machine might be implemented well**, but without a diagram or description, someone has to **reverse-engineer it** to understand all the possible transitions.

If it involves concurrency, timing, or state transitions, **it needs documentation**.

### 4. Onboarding and Maintenance Become a Nightmare

* Without documentation, new developers (or even you, six months later) have to **reverse-engineer everything**.
* If debugging requires **stepping through code to understand how it all works**, that’s wasted time.
* **Edge cases, performance optimisations, and workarounds** become forgotten landmines, waiting to cause issues.

A good README, architecture diagram, or design note **saves days of effort**.

### 5. Code Evolves, but Intent Shouldn’t Be Lost

* Code changes over time, and without documentation, **decisions get lost**.
* Why was a specific trade-off made? Why was a feature implemented a certain way?
* If the original developer is gone, **who’s left to explain it?**

Without documentation, developers might **accidentally undo important design decisions**—or just break things outright.

***

## What Should You Document?

Documentation isn’t about **writing endless pages of text**—it’s about recording **what future developers need to know without reading all the code**.

### 1. Embedded & Real-Time Systems

* **Interrupts & concurrency** – Priorities, timing constraints, shared resources.
* **State machines** – Valid states, transitions, and event triggers.
* **Power management** – Sleep modes, wake-up conditions, and peripheral behaviour.

### 2. General Applications (Linux, Windows, etc.)

* **Architecture & key modules** – How components interact, dependencies.
* **Configuration & error handling** – Where settings live, failure recovery strategies.
* **Performance constraints** – Caching, threading, and known bottlenecks.

### 3. Cloud, SaaS & Microservices

* **Service boundaries & APIs** – What talks to what, and how.
* **Scaling & failure handling** – Load balancing, retry mechanisms, failure modes.
* **Security & authentication** – How access is managed, potential risks.

***

## The Real Message: Good Code *Deserves* Good Documentation

Readable code is **important**, but **self-documenting code is a myth**.

Instead of hiding behind *“the code is the documentation”*, developers should:

- ✅ Write clean, understandable code.
- ✅ Document decisions, not just syntax.
- ✅ Provide context so future developers (and themselves) aren’t left guessing.

Good code is **part of the story**—but documentation is what makes it **understandable, maintainable, and usable**.

### Final Thought

If someone tells you *“Good code documents itself!”*, ask them how long it took them to figure out the last system they worked on. If it was more than five minutes, it didn’t document itself.
