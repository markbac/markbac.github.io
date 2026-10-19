---
title: Continuous integration and delivery
---

# Continuous integration and delivery

Continuous Integration (CI) and Continuous Delivery (CD) are a cornerstone of modern development. They are about automating the boring, repetitive tasks so your team can focus on what matters: delivering value. In a multi-disciplinary team, that means more than building and testing code. It means checking every artefact, from firmware to documentation, and giving it a smooth, reliable path to customers.

This guide outlines key considerations for designing a CI/CD pipeline, aligning with our core philosophy of structure without bureaucracy.

## The Challenge of a Hybrid Pipeline

Just as with version control, a CI/CD pipeline for a multi-disciplinary product must handle different types of artifacts and validation needs.

* **Software and Firmware:** Requires rapid build, lint, and unit test cycles.

* **Hardware:** Can be validated through simulations, automated tests on physical hardware (Hardware-in-the-Loop or HIL), or even formal design checks.

* **Documentation:** Should be linted, built into a website, and published automatically.

The goal is to create a single, unified pipeline that provides fast feedback to every team member, regardless of their discipline.

## Key Considerations for Your Pipeline

A good CI/CD pipeline is about enabling flow and reducing friction. Here are some key principles to guide your design.

### 1. Shift Left and Fail Fast

The best way to prevent problems is to find them as early as possible. Your pipeline should run a series of automated checks and tests at every stage, starting with the very first commit or pull request.

* **Continuous Integration (CI):** Every time a change is pushed to a feature branch, the CI pipeline should automatically build and test the code. This gives the developer immediate feedback and prevents them from introducing a bug that could block the entire team.

* **Automated Checks:** Implement checks for code style, documentation quality, and security vulnerabilities. This ensures consistency and catches common errors before they are ever reviewed by a human.

* **Decoupling Tests:** Separate your tests into different stages. A fast-running smoke test should run on every commit, while a longer, more comprehensive suite can run on merge requests or nightly builds. This gives your team fast feedback without sacrificing thoroughness.

### 2. Embrace Automation as an Enabler

Automation is a force multiplier. It saves time, reduces human error, and ensures consistency.

* **Build Automation:** Automate the entire build process, from compiling code to generating an executable or a production-ready artefact. This eliminates the "works on my machine" problem.

* **Automated Testing:** Run unit, integration, and end-to-end tests automatically. This gives you confidence that your changes haven't broken anything.

* **Automated Deployment:** Automate the process of deploying your application to a staging or production environment. This ensures a consistent, repeatable process and reduces the risk of manual errors.

### 3. Integrate All Artifacts

A CI/CD pipeline for a hybrid product should treat all artifacts as first-class citizens.

* **Docs as Code:** When a developer updates documentation, the CI pipeline should automatically build the website and publish the changes.

* **Hardware Design Checks:** For hardware, your CI pipeline could run a check that validates a PCB layout against a set of design rules. This catches errors early and prevents costly manufacturing mistakes.

* **Artefact Traceability:** Ensure that every build artefact (e.g., a software binary, a PCB gerber file) is tagged with a unique version number and a link to the commit that generated it. This provides a clear audit trail and is essential for troubleshooting and compliance.

## The Pipeline in Practice

Let's imagine a pull request for a new feature.

1. **Code Push:** A developer pushes a new commit. The CI pipeline is triggered.

2. **Lint & Test:** The pipeline runs a linter to check for code style issues and then runs the unit tests. If anything fails, the developer is notified immediately, and the pipeline stops.

3. **Peer Review:** The developer opens a pull request. A pull request is not just a code review; it's a review of the entire change, including documentation updates, architecture decisions, and tests.

4. **Merge & Build:** Once reviewed, the code is merged into the `main` branch. The pipeline is triggered again, this time running a more comprehensive suite of tests and checks.

5. **Deploy:** Once all tests pass, the artefact is automatically deployed to a staging environment for final validation.

This process provides continuous feedback and ensures that the `main` branch is always in a releasable state, making a "release" a non-event.

## Tips for Success

* **Start Small:** Don't try to automate everything at once. Start by automating your build process, then add tests, and then work on deployment.

* **Treat the Pipeline as Code:** Your CI/CD configuration should live in your repository alongside your code. This ensures it is version-controlled, auditable, and easily shared among your team.

* **Focus on the Metrics:** Measure what matters. How long does it take for a pull request to be merged? How many bugs are making it to production? Use these metrics to continuously improve your process.

* **Blameless Postmortems:** When something goes wrong in the pipeline, focus on what failed, not who. Use the failure as a learning opportunity to improve the process for everyone.
