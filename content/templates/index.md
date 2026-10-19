---
title: Templates & Checklists
author: Mark Bacon
description: Checklists for reviews and quality gates, and templates for engineering records, for embedded and connected-product teams.
---

# Templates & Checklists

Checklists for the reviews and quality gates in a software or firmware project, and templates for the records a team keeps along the way. They are written for embedded and connected products, but most of them work for any software team.

Copy them into your own repository, tracker or wiki and change them to suit. A checklist nobody adapts tends to become a checklist nobody reads.

## Checklists

Each checklist is a task list, so it can go straight into a pull request, an issue or a review record. Every item has an ID, so review comments and records can refer to it.

[[CAPTION:Table]] The checklists.

| Checklist | Use it when |
|-----------|-------------|
| [Definition of Ready](definition-of-ready.md) | Deciding whether a backlog item can go into a sprint |
| [Definition of Done](definition-of-done.md) | Deciding whether a work item is finished |
| [Architecture review](architecture-review-checklist.md) | Reviewing a system architecture or high-level design |
| [Design review](design-review-checklist.md) | Reviewing the detailed design of a component or module |
| [Code review](code-review-checklist.md) | Reviewing a pull request |
| [Debugging](debugging-checklist.md) | Investigating and fixing a fault |
| [Defect report](defect-report-checklist.md) | Raising a defect, setting its severity, and closing it |

## Templates

Grouped by when in a project you are likely to need them.

[[CAPTION:Table]] Templates for vision and architecture.

| Template | Use it for |
|----------|------------|
| [Project vision](project-vision.md) | Agreeing why a project exists, who it is for and what success looks like |
| [Architecture vision](architecture-vision.md) | Describing where a system's architecture is heading, and why |
| [Architecture principles](architecture-principles.md) | Recording the principles a product or team has agreed |
| [Architecture document](architecture-document.md) | Describing a system's architecture, with C4 diagram starters |
| [Architecture canvases](architecture-canvases.md) | Starting or explaining an architecture on one page |
| [Crosscutting concerns](crosscutting-concerns.md) | Security, logging, errors and configuration across a whole system |
| [Architecture decision record](adr.md) | Recording one significant decision |
| [Request for comments](rfc.md) | Proposing a change and gathering views before deciding |

[[CAPTION:Table]] Templates for requirements, design and testing.

| Template | Use it for |
|----------|------------|
| [Requirements and quality scenarios](requirements.md) | Writing requirements that can be traced and tested |
| [NFR scenario](nfr-scenario.md) | Writing one non-functional requirement as a testable scenario |
| [Requirements traceability matrix](requirements-traceability-matrix.md) | Tracing requirements to design, code and tests |
| [Interface specification](interface-specification.md) | Describing an interface between components or systems |
| [Software design specification](software-design-specification.md) | The detailed design of a system or module |
| [Experiment record](experiment-record.md) | Running a spike, prototype or piece of research |
| [Test plan](test-plan.md) | Planning how a product, system or component is tested |

[[CAPTION:Table]] Templates for delivery and operations.

| Template | Use it for |
|----------|------------|
| [Systems engineering management plan](systems-engineering-management-plan.md) | Running the engineering of a larger multi-discipline project |
| [Team working agreement](team-working-agreement.md) | Agreeing how a team works together |
| [Meeting minutes](meeting-minutes.md) | Recording a meeting's decisions and actions |
| [Decision log](decision-log.md) | A running list of a project's decisions |
| [Risk register](risk-register.md) | Tracking risks, their owners and what is being done about them |
| [Technical debt register](technical-debt-register.md) | Recording technical debt and the plan to pay it down |
| [Release plan](release-plan.md) | Planning a release or deployment, including the rollback |
| [Software bill of materials](sbom.md) | Summarising the components a product is built from |
| [Pull requests and commits](pull-request-and-commits.md) | Pull request descriptions, commit messages and a commit message hook |
| [Postmortem](postmortem.md) | Learning from an incident or a defect found in the field |
| [Lessons learned](lessons-learned.md) | Looking back at the end of a project or phase |
| [Task brief for an AI agent](agent-task-brief.md) | Handing a coding task to an AI agent |
| [Conformance profile and component register](product-conformance-profile.md) | Tailoring guidelines to a product, and listing its components |

## Files to download

The templates that tools read are also available as files.

[[CAPTION:Table]] Template files.

| File | What it is |
|------|------------|
| [`requirement.yaml`](https://github.com/markbac/markbac.github.io/raw/main/content/templates/files/requirement.yaml) | A requirement record |
| [`component-register.yaml`](https://github.com/markbac/markbac.github.io/raw/main/content/templates/files/component-register.yaml) | A component register |
| [`c4-workspace.dsl`](https://github.com/markbac/markbac.github.io/raw/main/content/templates/files/c4-workspace.dsl) | A starter Structurizr workspace |
| [`commit-msg`](https://github.com/markbac/markbac.github.io/raw/main/content/templates/files/commit-msg) | A Git hook that checks commit messages |
| [Architecture Inception Canvas, draw.io](https://github.com/markbac/markbac.github.io/raw/main/content/templates/files/architecture-inception-canvas.drawio) | The inception canvas, to edit in draw.io |
| [Architecture Inception Canvas, PowerPoint](https://github.com/markbac/markbac.github.io/raw/main/content/templates/files/architecture-inception-canvas.pptx) | The inception canvas, as slides |
| [Architecture Communication Canvas, draw.io](https://github.com/markbac/markbac.github.io/raw/main/content/templates/files/architecture-communication-canvas.drawio) | The communication canvas, to edit in draw.io |
| [Architecture Communication Canvas, PowerPoint](https://github.com/markbac/markbac.github.io/raw/main/content/templates/files/architecture-communication-canvas.pptx) | The communication canvas, as slides |

The canvases are by Gernot Starke, Patrick Roos, Ben Wolf and the arc42 contributors, under a Creative Commons Attribution-ShareAlike licence (see [Architecture canvases](architecture-canvases.md)).
