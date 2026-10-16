---
date: 2025-05-15T09:09:00
authors:
  - markbac
categories:
  - Docs as Code
slug: docs-in-agile
---

# Making Docs Part of Your Agile Workflow

Documentation often gets left behind in Agile workflows. Burndown charts don’t track missing architecture decisions. Velocity doesn’t drop because your API spec is a week out of date. So unless you actively build documentation into your Agile flow — it doesn’t happen.

<!-- more -->

This post shows how to make documentation a **natural part of your delivery rhythm**, not an afterthought. We’ll walk through how to connect epics and features to ADRs and RFCs, and scaffold docs from issue templates. Then we’ll add documentation reviews to CI pipelines, and even link into Confluence or SharePoint for broader visibility.

---

## Connecting Epics → Features → Artefacts → Implementation

If your Agile tool (Jira, Azure DevOps, Rally) holds your delivery backlog, it should also trace your documentation flow.

### Ideal Flow

1. **Epic**: “Add remote config support”
2. **Feature**: “Define config protocol and OTA update design”
3. **Linked Artefacts**:
    - ADR: “Select protocol for OTA updates”
    - RFC: “Proposal for update architecture”
    - Interface spec: “MQTT command structure”
    - Deployment view: “Config delivery and rollback flow”
4. **Stories**: Build firmware hook, cloud API, UI config screen

Each level references or links to the documents it depends on.

### Practical Example (Azure DevOps)

- Epic: `#123 Remote Configuration Platform`
- Feature: `#125 Protocol Architecture`
- Work item link: `ADR-007 Use MQTT for Config`
- Story: `#127 Device-side MQTT handler`

📌 Tip: Include a “Documentation” field or tag that links to `docs/adr/007-mqtt-config.md`.

---

## Scaffolding Docs from Issue Templates

We’ve all been there — a PR references an architectural decision that lives in someone’s head. Better to scaffold docs early.

### Use issue templates (Jira or ADO) to auto-generate Markdown stubs

#### Example ADO Task Template
```yaml
name: Feature Template
description: Scaffold docs-as-code items

steps:
- Create `docs/adr/adr-<num>-<topic>.md` from template
- Create `docs/rfc/rfc-<num>-<topic>.md` if needed
- Add test strategy in `docs/tests/<component>.md`
- Update `README.md` or overview index
```

#### Markdown Scaffold Example
```markdown
# ADR-008: Use LwM2M for Device Management

## Context
...

## Decision
...

## Consequences
...

## Alternatives Considered
...
```

Make this part of your sprint planning. Assign scaffolding as a task next to design and implementation.

---

## Docs in Pull Request Reviews

Don’t just review code — review the artefacts that justify and explain it.

### Setup

- Add `docs/**` as a path in codeowner or reviewer config
- Add markdownlint and link checker in your CI
- Make documentation review part of Definition of Done

#### Example GitHub CODEOWNERS
```
docs/adr/* @techleads
docs/rfc/* @architects
```

📌 Tip: Don’t let docs block merges, but make comments mandatory. “Add link to related ADR” is a valid comment.

---

## Keeping Docs in Sync via CI

You can automate a lot with minimal effort.

### Validate in CI

- All Markdown files linted
- All internal links work
- Diagrams render (optional in PR)

#### Example GitHub Action
```yaml
name: Docs Check

on: [pull_request]

jobs:
  validate-docs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - run: npm install -g markdownlint-cli
      - run: markdownlint docs/
      - run: npx markdown-link-check docs/**/*.md
```

### Bonus

- Auto-generate `docs/index.md` via script from folder content
- Flag unused or orphaned docs with a CI warning
- Extract metadata from YAML frontmatter into PR comments

---

## Linking Docs in ADO and Jira

Documentation needs to live where people work. That often means linking out of your backlog tool.

### Jira Example

- Custom field: “Related ADR”
- Add link: `https://github.com/org/repo/docs/adr/adr-008.md`
- Use smart link titles: `[ADR-008: Device Protocol Choice](...)`

### Azure DevOps

- Use "Links" tab → "External link"
- Embed markdown links in discussion or description

📌 Tip: Add README sections that mirror work items:
```markdown
## Feature: Remote Config
- [ADR-007](adr/007-protocol.md)
- [Test Strategy](tests/config-tests.md)
```

---

## Integration with Confluence and SharePoint

Sometimes your markdown needs to land where the business looks.

### Options

1. **Convert to Word or PDF** using Pandoc or `md-to-pdf`
2. **Embed GitHub markdown** via iframe widgets (for internal tools)
3. **Publish generated HTML to SharePoint Online** via scripts
4. **Use GitHub Pages** with internal DNS + a Confluence page link

### Pandoc Example
```bash
pandoc docs/adr/007-protocol.md -o Protocol-ADR.docx
```

This is especially useful for:

- Governance reviews
- Supplier integration packs
- Customer documentation requirements

📌 Tip: Maintain source of truth in Markdown, and automate the export step.

---

## Embedding Docs-as-Code into Agile Ceremonies

| Ceremony       | Docs-as-Code Integration Example                         |
|----------------|-----------------------------------------------------------|
| Sprint Planning| Assign doc scaffolding for features (ADR, canvas)         |
| Daily Standup  | “Working on RFC for messaging layer refactor”             |
| Sprint Review  | Include published site or doc links in demo notes         |
| Retrospective  | Capture lessons in `/lessons/` or add notes to an ADR     |
| Backlog Grooming | Link artefacts to features as part of triage            |

This builds habits. And once the habit is there, Docs-as-Code doesn’t feel like “extra work”.

---

## Real-World Example Workflow

**Scenario**: Refactor telemetry pipeline for observability

### Jira Setup
- Epic: `#OBS-100 Improve telemetry resilience`
- Stories:
  - Design: `#OBS-101 Define message schema (RFC)`
  - Impl: `#OBS-102 Update API ingestion`
  - QA: `#OBS-103 End-to-end validation`

### Docs Folder
```plaintext
docs/
├── rfc/
│   └── rfc-010-telemetry-schema.md
├── adr/
│   └── adr-022-use-json-schema.md
├── tests/
│   └── telemetry-validation.md
├── diagrams/
│   └── telemetry-flow.mmd
```

### Pull Request
- Implements `OBS-102`
- Links to `rfc-010` and `adr-022`
- Reviewer checks docs exist + are updated
- CI checks for link, lint, spell

---

## Definition of Done Checklist (Docs Edition)

| Check                                 | Status |
|--------------------------------------|--------|
| ✅ ADR written for architectural choice |        |
| ✅ RFC drafted (if relevant)            |        |
| ✅ Interface spec or diagram updated    |        |
| ✅ Test strategy included               |        |
| ✅ Linked in Jira/ADO                   |        |
| ✅ Lint + link checks pass              |        |

This turns documentation from a “we should write this” to “we already did”.

---

## Final Thoughts

Docs-as-Code works best when it fits into your delivery rhythm.

- Link epics to artefacts
- Scaffold docs as part of the backlog
- Review and validate docs like code
- Export where needed for visibility
- Keep the source of truth in Markdown

If you treat documentation like part of the system — not just commentary — your team’s thinking becomes traceable, transferable, and trustworthy.

---

📘 Next in the series: [Living Architecture: Keeping Documentation Relevant Over Time](2025-05-15-living-architecture.md)
