---
date: 2025-03-07T10:16:00
authors:
  - markbac
categories:
  - Engineering practice
slug: standardising-tools
---

# Why Standardising Tools and Processes Across Software Teams is a Bad Idea

There’s a persistent belief in many organisations that standardising tools and processes across all software teams is a good idea. The logic goes something like this: if everyone is using the same set of tools, collaboration becomes easier, onboarding new engineers is smoother, and there’s less administrative overhead.

<!-- more -->

In theory, this sounds reasonable. In practice, it’s a disaster.

Forcing every software team to use the same tools and follow the same processes creates friction and stifles innovation. It often leads to a situation where *nobody* is happy, because the chosen toolset is a compromise that suits no one properly. The reality is that **tools are just enablers**—what really matters is that teams understand *why* they are doing something, not just *how*. If they understand the fundamentals, they can pick up any tool with minimal effort.

## 1. The Tool Is Not the Process

A classic example is task management. Some teams use **Jira**, others prefer **Azure DevOps**, some like **Trello**, and a few might even be happy with a well-organised **spreadsheet** (yes, it happens). Does it matter? Not really—*as long as they understand how to manage tasks effectively*.

A well-functioning team understands:

* How to prioritise work.
* How to track progress.
* How to communicate blockers and dependencies.

If they get those fundamentals right, the tool itself is just a detail. On the other hand, if a team *doesn’t* understand task management, forcing them onto a standard tool won’t fix the problem. It will just make it harder for them to work effectively.

## 2. Different Teams Have Different Needs

Not all software teams work in the same way. Forcing them into one set of tools and processes is like making a football team, a Formula 1 team and a mountain climbing expedition share one vehicle. It’s nonsensical.

* A **DevOps-heavy team** needs deep GitOps integration, automated deployment tracking, and flexible sprint planning.
* A **UX-focused team** might need lightweight task management, tight links to customer feedback, and design review workflows.
* A **research-driven team** working on experimental algorithms might prefer a Kanban-style workflow with minimal process overhead.

Forcing all these teams into a single tool and workflow **doesn’t make things more efficient—it makes them worse** because nobody gets what they actually need. Instead, they get a “one-size-fits-all” tool that ends up being a compromise for *everyone*.

## 3. Standardisation Kills Innovation

When teams have the freedom to choose their own tools and processes, they can experiment, adapt, and refine their way of working. They can adopt new technologies and workflows that genuinely improve productivity.

But when tool selection is dictated from above, experimentation stops. Instead of focusing on *how to build better software*, teams waste time working around tool limitations, filling in unnecessary forms, and following processes that don’t actually help them.

A great example is documentation. Some teams prefer **Confluence**, others prefer **Docs-as-Code** with markdown and Git. If you force everyone onto a single documentation platform, you might be solving an imaginary consistency problem while creating a *real* productivity problem.

## 4. Cross-Team Collaboration Is a People Problem, Not a Tool Problem

One of the most common arguments for standardising tools is that it makes cross-team collaboration easier. In reality, **collaboration is about communication and alignment—not about everyone using the same tool.**

* If two teams need to share work, they can agree on a simple integration (e.g. syncing key work items between different tools).
* If leadership needs visibility, dashboards and reporting APIs can pull data from multiple sources.
* If teams understand *why* things are being tracked, they’ll work together to ensure visibility—regardless of the tool.

Instead of focusing on forcing everyone onto the same system, **organisations should focus on making sure teams talk to each other.**

## 5. The Fundamentals Matter More Than the Tools

The biggest counter-argument to “but we need everyone on the same tools” is simple: if engineers understand the fundamentals, they can pick up *any* tool quickly.

* If a developer understands what an **issue tracker** is, they can use Jira, ADO, Trello, or GitHub Issues—it doesn’t matter.
* If they understand what an **IDE** does, switching from Visual Studio to JetBrains Rider or VS Code is just a minor adjustment.
* If they understand **CI/CD concepts**, moving from Jenkins to GitHub Actions isn’t a major problem.

The real danger isn’t that people are using different tools. It’s when **people don’t understand the fundamentals of software development and need their hand held by the tool itself.**

## 6. Process Overhead Is the Real Enemy

The real risk isn’t a lack of tool standardisation—it’s *process bloat*. Standardisation often brings unnecessary overhead, where teams are forced to follow rigid workflows that don’t actually help them build better software.

Instead of dictating *how* teams should work, organisations should focus on:

* **Defining clear outcomes** (e.g. reliable delivery, quality, security).
* **Giving teams the autonomy to choose the best way to achieve those outcomes.**
* **Providing best practices as guidance, not rigid rules.**

## 7. Standardise Where It Matters, Not Everywhere

Some things *do* benefit from standardisation:

- ✔️ Security practices.
- ✔️ Compliance requirements.
- ✔️ API design principles.
- ✔️ Coding standards.

But **forcing a single set of tools and ways of working across all software teams is a mistake.**

Some teams understand the core principles of software development: good task management, effective collaboration, quality control, and reliable delivery. They should be free to use whatever tools make them most productive.

## Final Thoughts: Focus on the Right Problems

At the end of the day, **tools don’t deliver software—people do.**

Give teams the autonomy to work in the way that makes sense for them, and they’ll deliver better results. Standardisation for the sake of it is a distraction from the real goal: enabling teams to build great software, efficiently and effectively.
