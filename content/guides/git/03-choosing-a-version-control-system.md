---
title: Choosing a version control system
---

# Choosing a version control system

A version control system (VCS), like Git, is the backbone of our **Docs as Code** philosophy. When managing complex, integrated products, it's essential to consider how our VCS strategy impacts the entire team, particularly in a multi-disciplinary environment. The goal is to accommodate different paces of work while maintaining a single source of truth and clear traceability.

This guide outlines key factors to consider when designing a version control strategy, rather than dictating a single, rigid workflow.

## The Challenge of Multi-Disciplinary Repositories

In a multi-disciplinary product (software, firmware, hardware), not all teams operate at the same pace. Software and firmware can iterate rapidly, while hardware has long lead times and high iteration costs. Your branching strategy must accommodate this reality while maintaining a single source of truth and clear traceability.

## Key Considerations for Your Strategy

Instead of adopting a prescriptive workflow, it's better to design a strategy based on a few core principles. These principles will help you create a system that works for your team's unique context and constraints.

### 1. The Single Source of Truth

This is about defining a definitive reference point for the latest, validated state of the product. It’s the branch that represents what’s released to customers or ready to be built.

* **Core Principle:** Every strategy should aim to create a single, authoritative branch for the latest, validated version of the entire product. This is often a `main` or `trunk` branch that is highly protected.

* **What to Consider:** What rules need to be in place (e.g., automated checks, required reviews) to ensure only validated work is integrated into this branch? How will you handle hotfixes and urgent changes?

### 2. Decoupling Workflows

Your strategy should allow different teams to work at their own pace without blocking each other. This is about managing the inherent tension between agile, fast-paced work and structured, long-cycle work.

* **Fast-Paced Work:** For software, a lightweight branching model (like short-lived feature branches) can support rapid iteration and continuous integration. This keeps the main branch clean and makes it easy for teams to collaborate on small, incremental changes.

* **Structured Work:** For hardware, which might have longer design and manufacturing cycles, a more structured approach might be necessary. This could involve creating longer-lived branches that align with physical hardware revisions or formal releases. These branches serve as stable targets for software and firmware teams.

This hybrid approach allows teams to work in parallel. Imagine a hardware team working on `hardware-revA` while a software team iterates on new features on a `develop` branch. When a new hardware prototype is ready, the software team can easily integrate their latest code with the stable hardware branch for testing.

### 3. Traceability and Historical Context

Your VCS strategy should make it easy to understand the "why" behind every change. This is essential for debugging issues, onboarding new team members, and satisfying compliance requirements.

* **Meaningful Commits:** Require commits to be a single, logical unit of work with clear, descriptive messages. A good practice is to adopt a convention like `[Category]: [Description]` (e.g., `docs: Add ADR template` or `feat: Implement new API endpoint`). This provides context at a glance.

* **Pull Request Discipline:** Use pull requests to document the discussion, trade-offs, and approvals for every change. This provides a rich history that goes beyond just the code itself and serves as a living record of decisions.

* **Release Tagging:** Use tags to mark important milestones, such as a formal product release. This allows you to easily find the exact state of the product (code, docs, and all designs) at any point in time.

## Best Practices for All Artifacts

Regardless of your chosen strategy, these best practices apply to every type of artefact in your repository:

* **Atomic Commits:** Each commit should be a logical, indivisible unit of work. For documentation, this means a single change per commit (e.g., "docs: Add ADR template"). This makes it easy to revert changes and see the history of a document.

* **Use LFS for Large Files:** If your repository includes large files like hardware design files (CAD, PCB layouts), use a large file storage solution. This keeps the repository size manageable and prevents cloning times from becoming a bottleneck for the entire team.

* **Continuous Integration (CI):** Automate checks on every push and PR. For code, this means running linters and tests. For documentation, you can use a tool like `markdownlint` to check for formatting errors. For hardware, you could even have a CI job that validates design files against a set of rules.

* **Branch Protection:** Enforce rules to prevent direct commits to your main branches. This ensures all changes go through a proper review and validation process before being integrated. This simple rule is one of the most effective ways to maintain a clean and reliable codebase.
