---
date: 2025-05-15T09:14:00
authors:
  - markbac
categories:
  - Docs as Code
slug: documentation-culture
---

# Building a Documentation Culture That Lasts

Tools are easy. Culture is hard.

<!-- more -->

You can set up a Markdown repo, add a template, automate previews, and push PDFs to SharePoint. But unless your engineers see documentation as a **valuable habit**, it won’t last.

This post explores how to build a documentation culture that survives handovers, reorganisations, and delivery crunches. It's for engineering managers, team leads, and principal engineers trying to make documentation a normal, valued part of software delivery. Not a nice-to-have that dies after every sprint.

---

## Ownership Models that Work

Documentation needs owners. But not every document needs a dedicated scribe. Instead, use **structured, role-based ownership**.

### Ownership by Layer

| Layer          | Primary Owner        |
|----------------|----------------------|
| Architecture   | Principal Engineer / Architect |
| Application    | Tech Lead or Squad Lead |
| Feature-level  | Developer or Feature Owner |
| Test Artefacts | QA or Automation Engineer |
| Onboarding Docs| Team Lead / Manager |

### File-Level Ownership with Metadata

```yaml
owner: "device-team"
component: "telemetry"
status: "active"
last-reviewed: "2025-03-01"
```

Include `CODEOWNERS` or GitHub/ADO reviewers to route PRs automatically.

---

## Rituals that Reinforce

Teams that keep documentation healthy have **rituals** around it.

### Weekly: Review Rotations

Use metadata (`next-review:`) to open auto-generated tickets:

> "Review `mqtt.md` (last reviewed 2024-12-10)"

Rotate ownership across the team.

### Sprint Reviews

Include doc artefacts in the demo:
- Show new diagrams, ADRs, specs
- Link stories to updated docs

### Retrospectives

Have a “Doc Smells” section:
- What was hard to understand?
- What was outdated?
- What should we retire?

### Monthly Architecture Forum

Pick one architecture decision or interface and do a live review. Keep it informal and educational.

---

## Make Docs Part of Onboarding

Your documentation culture is only as strong as your onboarding.

### Onboarding Tasks

- Read: system overview, deployment diagram, top 5 ADRs
- Write: one bugfix doc, one onboarding tip
- Contribute: one PR to improve docs

### New Starter README Template

```markdown
# Welcome to Team API Gateway

## Start Here
- [Architecture Overview](../architecture/overview.md)
- [Interface Spec](../interfaces/http-ingestion.md)

## Week 1 Tasks
- Read ADR-010 and ADR-012
- Join intro session with Tech Lead
- Run local system with README steps
```

---

## Make Docs Part of KPIs and Progression

Engineers follow incentives. If documentation is valued, track it.

### Examples

- Promotion criteria includes: “Improves team onboarding experience”
- KPIs include: “Contributes to architectural clarity”
- Quarterly reviews ask: “Which documentation did you create or improve?”

---

## Contribution Ladder

A ladder gives people confidence about how to engage.

| Level          | Example Contribution                      |
|----------------|--------------------------------------------|
| 🔍 Reader       | Flags unclear sections via issue/comment |
| 🛠 Editor       | Fixes typos, broken links                 |
| ✍️ Author       | Writes or updates artefacts (ADR, RFC)    |
| 🧭 Maintainer   | Defines structure, review, ownership       |
| 📢 Advocate     | Trains others, improves culture           |

Use this in onboarding packs and retros.

---

## Review Flows That Work

Not every doc needs a review council. Use **lightweight peer review**.

### PR Template Snippet

```markdown
### Docs Updated

- [x] ADRs or RFCs touched
- [ ] Interface or diagrams updated
- [ ] Reviewer validated traceability

Reviewer(s): @team-architects
```

Automate notifications using GitHub Actions or Azure DevOps.

---

## Working Respectfully with Word and SharePoint

Word and SharePoint are not the enemy. But **author in Markdown, export to Word/PDF** when needed.

### Export with Pandoc

```bash
pandoc adr/014.md -o adr-014.docx
```

### SharePoint Coexistence Strategy

- Host artefacts in Git
- Use CI to export PDFs weekly
- Push to a SharePoint document library via Rclone or sync job
- Watermark with Git hash and last-reviewed date

---

## Encourage Contributions from Non-Engineers

Great systems are documented by more than just devs.

### Invite Ops, QA, PMs

- Run a “Docs Sprint” — 2 hours of pairing to clean and clarify
- Use `docs/contributions/` folders for team-specific content
- Template checklists for runbooks, playbooks, test strategies

---

## Simple Contribution Templates

### Test Strategy Template

```markdown
---
title: "Schema Validation Strategy"
owner: "qa-team"
last-reviewed: "2025-01-01"
status: "active"
---

## Scope

## Inputs

## Expected Behaviour

## Failure Conditions

## Manual vs Automated
```

### Runbook Template

```markdown
---
title: "Alert: Database Connection Failure"
owner: "oncall-team"
---

## Symptoms

## Steps to Diagnose

## Short-Term Fix

## Long-Term Resolution
```

---

## Folder Structure Example

```plaintext
docs/
├── architecture/
│   ├── overview.md
│   └── system-context.mmd
├── adr/
│   ├── 010-mqtt-decision.md
├── interfaces/
│   └── ingestion-spec.md
├── tests/
│   └── validation-strategy.md
├── runbooks/
│   └── db-connection-failure.md
├── onboarding/
│   └── new-starter-guide.md
└── contributions/
    ├── qa/
    └── ops/
```

---

## Dashboards and Visibility

Visibility drives trust.

### Dashboards To Track

- Artefacts missing owners
- Docs past `next-review` date
- Coverage of features → tests → docs
- Contributions by team

Render via a script that parses YAML frontmatter → JSON.

---

## Summary Checklist

| Habit/Pattern                        | Benefit                           |
|-------------------------------------|-----------------------------------|
| Ownership in frontmatter            | Prevents rot                      |
| Review rituals in teams             | Maintains trust                   |
| Docs in onboarding                  | Faster ramp-up                    |
| Templates and ladders               | Lowers barrier                    |
| Word/PDF as output only             | Keeps source clean                |
| QA/Ops contributions welcomed       | Improves realism                  |

---

## Final Thoughts

You can’t automate a culture. But you can scaffold it.

By making documentation normal — not heroic — you embed knowledge into your systems. You reduce team bus factor. You onboard faster. You catch bugs earlier. You scale more gracefully.

Invest in ownership, encourage small contributions, make docs part of delivery — and you’ll have a culture that sustains itself.

---

📘 Next in the series: [Templates, Starter Kits and Metadata Playbooks](2025-05-15-templates-and-playbooks.md)
