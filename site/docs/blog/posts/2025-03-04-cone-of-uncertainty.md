---
date: 2025-03-04T09:43:00
authors:
  - markbac
categories:
  - Engineering practice
slug: cone-of-uncertainty
---

# The Cone of Uncertainty: Why Your Estimates Are Always Wrong (And That’s Okay)

If you’ve ever been asked, *“How long will this take?”* and immediately felt a wave of dread, you’re not alone. Estimating software projects—or any complex endeavor—is notoriously difficult. The reason? A concept called **The Cone of Uncertainty**.

<!-- more -->

In this post, I’ll break down:

* What the Cone of Uncertainty is and where it came from
* Why early estimates are *always* wrong (and that’s fine)
* How to manage uncertainty instead of being blindsided by it

Let’s dive in.

***

## What Is the Cone of Uncertainty?

The **Cone of Uncertainty** describes how the accuracy of estimates improves over time as more information becomes available. Early on, estimates can be off by as much as **4× higher or lower than reality**. But as a project progresses, new insights reduce uncertainty, making estimates more reliable.

This concept was **first introduced by Barry Boehm in the 1980s** as part of his work on software engineering economics. It was later **popularized by Steve McConnell** in *Software Estimation: Demystifying the Black Art*. Since then, it’s become a fundamental part of how we understand software estimation.

### Visualizing the Cone

Construx, Steve McConnell’s company, publishes a common [diagram of the cone](https://www.construx.com/uploadedImages/Construx/Construx_Content/Resources/Books/Cone01.jpg).

At the **beginning of a project**, estimates are rough—sometimes *comically* so. As you gain insights, uncertainties reduce, and your estimates become more reliable.

- 🔹 **Project start:** Estimates can be **4× too high or 4× too low**.
- 🔹 **Midway through:** Refinements reduce uncertainty, but there’s still a margin of error.
- 🔹 **Near the end:** Estimates are much more reliable—though never perfect!

### The Role of Unknown Unknowns

<!-- vale PyDoc.Spelling = NO -->

A big reason for early uncertainty is what former U.S. Secretary of Defense **Donald Rumsfeld** famously described:

<!-- vale PyDoc.Spelling = YES -->

> *“…there are also unknown unknowns—there are things we do not know we don’t know.”*
>
> Donald Rumsfeld, news briefing, 12 February 2002

At the start of a project, you’re often dealing with **unknown unknowns**—things you aren’t even aware will be a problem. As the project progresses, these unknowns gradually turn into **known unknowns** (risks you can account for) and then **known knowns** (things you fully understand).

This transition is what shrinks the Cone of Uncertainty.

***

## Why Are We So Bad at Estimating?

Even the best engineers, project managers, and teams struggle with estimation. Why? Because at the beginning:

1️⃣ **Unknown Unknowns Dominate** – As discussed above, you don’t know what you don’t know.\
2️⃣ **Optimism Bias** – People (especially stakeholders) prefer best-case scenarios.\
3️⃣ **Requirements Change** – The project rarely stays exactly as envisioned.\
4️⃣ **Complexity and Dependencies** – One “small” issue can cascade into massive delays.\
5️⃣ **Pressure to Commit** – Once an estimate is given, it often gets treated as a deadline.

This is why so many software projects are late, over budget, or need to be drastically re-scoped.

***

## How to Work With (Not Against) the Cone

Instead of resisting the Cone of Uncertainty, **embrace it**. Here’s how:

✅ **Use Ranges, Not Absolutes** – Instead of saying “This will take 3 months,” say “This will take between 2 and 6 months.” Acknowledge the uncertainty upfront.

✅ **Reassess and Refine Estimates** – As more information becomes available, refine your forecasts. Don’t let an early wild guess dictate later decisions.

✅ **Communicate Uncertainty Clearly** – Stakeholders need to understand that early estimates are just that—**early**. Help them see how uncertainty reduces over time.

✅ **Break Down Work into Smaller Chunks** – The smaller the task, the easier it is to estimate accurately. Use Agile methodologies to reduce estimation risk.

✅ **Track and Learn from Past Projects** – Keep historical data on how past estimates compared to actuals. Over time, this helps improve forecasting.

***

## Final Thoughts

The **Cone of Uncertainty is inevitable** in software development (and beyond). The key isn’t to eliminate uncertainty (that’s impossible), but to manage it **realistically**.

So next time someone asks, *“How long will this take?”*—instead of giving a false sense of certainty, remind them:

*"At this stage, we’re somewhere between a best guess and complete fantasy—but we’ll get better over time!"* 😄
