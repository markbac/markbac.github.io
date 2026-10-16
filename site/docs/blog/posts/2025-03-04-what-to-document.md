---
date: 2025-03-04T09:31:00
authors:
  - markbac
categories:
  - Documentation
slug: what-to-document
---

# What You Should Document and Why

Good documentation isn’t about writing endless pages of text. It’s about capturing the **right information** so developers can understand, maintain, and extend a system **without reverse-engineering everything from the code**.

<!-- more -->

If you’ve ever struggled to debug a system, onboard a new developer, or figure out why something was designed a certain way, chances are **critical documentation was missing**.

So, what should you document? And more importantly, *why*?

***

## 1. High-Level System Design (So No One Has to Guess How It Works)

Every system has an overall **architecture**—even if it’s not formally defined. Without documentation, developers have to **trace through code, dependencies, and configurations** to figure it out.

### What to Document

* **System architecture** – High-level diagram showing major components, services, or modules.
* **Data flow** – How information moves through the system, including storage and processing.
* **Third-party dependencies** – External APIs, libraries, and integrations.

### Why It Matters

- ✅ Helps new developers understand the system **quickly**.
- ✅ Prevents **breaking changes** by making dependencies clear.
- ✅ Reduces debugging time when troubleshooting system-wide issues.

***

## 2. Key Design Decisions (So No One Has to Re-Litigate Old Choices)

Code tells you *how* something works, but not *why* it was built that way. Without documenting key decisions, developers waste time re-evaluating past trade-offs—or worse, they **undo critical design choices without realising why they existed**.

### What to Document

* **Architecture Decision Records (ADRs)** – Short documents explaining major design choices.
* **Trade-offs and alternatives considered** – Why one approach was chosen over another.
* **Known limitations** – What the system *can’t* do, or what to watch out for.

### Why It Matters

- ✅ Avoids repeating past debates and mistakes.
- ✅ Helps developers understand **why things work the way they do**.
- ✅ Prevents unnecessary rewrites of working code.

***

## 3. State Machines & Workflow Logic (So No One Has to Reverse-Engineer Every Possible Case)

State transitions and complex workflows aren’t always obvious from code, especially when they depend on **external events, concurrency, or business rules**.

### What to Document

* **State diagrams** – Visual representation of valid transitions.
* **Event triggers** – What causes a state change?
* **Edge cases & failure modes** – What happens in unexpected situations?

### Why It Matters

- ✅ Reduces the risk of introducing **invalid state transitions**.
- ✅ Helps developers debug **edge cases** without guessing.
- ✅ Saves time when adding **new features** that interact with existing logic.

***

## 4. Concurrency & Synchronisation (So No One Introduces Subtle Race Conditions)

Multithreaded applications, real-time systems, and distributed microservices all involve **concurrent execution**. If you don’t document how tasks interact, you’re asking for **deadlocks, race conditions, and subtle timing bugs**.

### What to Document

* **Threading model** – How tasks are scheduled and synchronised.
* **Shared resources** – What’s accessed by multiple threads/processes, and how it’s protected.
* **Critical sections & locks** – Where synchronisation mechanisms (mutexes, semaphores, atomic operations) are used.

### Why It Matters

- ✅ Prevents **thread safety issues** and unexpected behaviour.
- ✅ Reduces debugging time by making **synchronisation points clear**.
- ✅ Helps developers understand how **performance and responsiveness** are affected.

***

## 5. APIs & Contracts (So No One Has to Read Through Code to Use Them)

If an application exposes an API—whether internally or externally—it needs **clear documentation**. Otherwise, consumers will either misuse it or have to **experiment to figure out how it works**.

### What to Document

* **Endpoints & request formats** – What methods exist and what data they accept.
* **Response structures & error handling** – What comes back, and what to expect when things go wrong.
* **Rate limits, authentication & security** – Who can access the API, and how.

### Why It Matters

- ✅ Enables **faster development** by making API usage clear.
- ✅ Reduces **misuse and unexpected failures**.
- ✅ Helps maintain **consistency** across multiple services.

***

## 6. Configuration, Deployment, & Infrastructure (So No One Has to Figure It Out From Scratch)

Software doesn’t just run—it needs to be **configured, deployed, and maintained**. If those steps aren’t documented, setting up a new environment becomes a nightmare.

### What to Document

* **Configuration files & environment variables** – What settings control behaviour?
* **Deployment process** – How is the system built, packaged, and deployed?
* **Infrastructure dependencies** – What databases, queues, or cloud services does it rely on?

### Why It Matters

- ✅ Reduces downtime caused by **misconfigured environments**.
- ✅ Makes onboarding **faster** for new developers.
- ✅ Prevents deployment errors that **break production**.

***

## 7. Error Handling & Debugging (So No One Has to Spend Hours Digging Through Logs)

When something goes wrong, developers need to **quickly** understand why. Without documentation on **failure modes, error codes, and logs**, debugging becomes a frustrating exercise in guesswork.

### What to Document

* **Common failure cases & expected behaviour** – How should the system react to failures?
* **Logging strategy** – What gets logged, and where?
* **Monitoring & alerts** – How to detect when something is wrong?

### Why It Matters

- ✅ Saves **hours of debugging** by making failure handling clear.
- ✅ Helps **identify and fix issues faster** in production.
- ✅ Improves system **reliability and resilience**.

***

## The Bottom Line: Good Documentation Saves Time & Prevents Mistakes

Documentation isn’t about writing **everything down**—it’s about capturing **what actually matters** so that developers can work efficiently **without unnecessary roadblocks**.

- 🔹 *If it helps someone understand the system faster, document it.*
- 🔹 *If it prevents a future mistake, document it.*
- 🔹 *If it saves hours of debugging, document it.*

The best documentation answers **why things are the way they are**—so developers don’t have to **reverse-engineer every decision from the code**.

***

### Final Thought

Bad documentation leads to wasted time, frustration, and costly mistakes. If you’ve ever spent hours figuring out something that could have been **explained in five minutes**, you already know why documentation matters.

So document the **right things**, and do it well. Future-you (and your team) will thank you.
