---
date: 2025-05-15T09:10:00
authors:
  - markbac
categories:
  - Docs as Code
slug: living-architecture
---

# Living Architecture: Keeping Documentation Relevant Over Time

Architectural documentation has a bad reputation. People write it, forget it, and then complain that “it’s out of date” or “no one uses it.” That’s not a failure of documentation — it’s a failure of **process and ownership**.

<!-- more -->

Documentation doesn’t have to decay. In fact, when embedded in a Docs-as-Code workflow and treated like real architecture infrastructure, it becomes one of the most powerful tools in your system. It’s a source of shared understanding, traceability, and evolution.

This post is all about **living documentation**: how to keep architecture artefacts relevant, reviewed, and useful long after the initial sprint. We'll walk through:

- Tagging schema for ownership and lifecycle
- Setting up review cadences and staleness checks
- Making diagrams diffable and reviewable
- Linking documentation changes to code and requirements
- Practical folder structures and CI policies

---

## Ownership and Lifecycle Tagging

No artefact should be anonymous. If no one owns it, no one updates it. Simple as that.

### What every document should have

- `owner`: person or team responsible
- `status`: draft, active, deprecated
- `scope`: product, system, project
- `last-reviewed` and `next-review`: timestamps
- `linked-artefacts`: references to code, tests, features

### Markdown Frontmatter Example

```yaml
title: "ADR-013: Use JSON Schema for Config Validation"
owner: "platform-team"
status: "active"
scope: "product"
last-reviewed: "2025-01-10"
next-review: "2026-01-10"
linked-artefacts:
  - feature-552-config-update
  - test-case-293-schema-validation
```

📌 Use this consistently and build linters to validate it.

---

## Review Cadences and Document Health

Not all documents need constant updates. But without **intentional review**, they quietly rot.

| Artefact Type   | Review Cadence   | Triggered By                         |
|------------------|------------------|--------------------------------------|
| ADRs             | Annually         | Major product refactor               |
| Interface Specs  | Quarterly        | New consumer or integration          |
| Context Diagrams | Bi-annually      | Product/platform scope changes       |
| Support Runbooks | Quarterly or Post-Incident | Any major outage             |
| Risk Registers   | Monthly          | Sprint retrospectives or PI reviews  |

### Review status banner in Markdown

```markdown
> 📅 Last reviewed: 2025-01-10  
> 🧯 Next review due: 2026-01-10  
> 🔗 Owner: Platform Team
```

Include this at the top of key documents like ADRs and system diagrams.

---

## Detecting Stale Documentation

Even with owners, things get missed. CI automation is your friend here.

### Simple CI check using Bash

```bash
find docs/ -name '*.md' | while read file; do
  next_review=$(grep 'next-review:' $file | cut -d ':' -f2 | tr -d ' ')
  if [[ "$(date +%Y-%m-%d)" > "$next_review" ]]; then
    echo "⚠️  Review overdue: $file (next-review: $next_review)"
  fi
done
```

Run this nightly or as part of a pre-release check. Add alerts to Slack or ADO dashboards.

---

## Diffable Diagrams in Version Control

Versioning diagrams is critical for traceability.

### Options

- **Mermaid**: Markdown-native, diffable text
- **PlantUML**: Rendered from source, readable in PRs
- **Structurizr DSL**: Best for C4 model, component views, and layering

```dsl
container delivery-api {
  technology "Go + REST"
  description "Handles telemetry ingestion"
}
```

Reviewing changes in DSL or Mermaid avoids the “who updated this PNG?” problem.

---

## Linking Doc Changes to Work Items

Documentation should evolve with features and bugs.

### Add to PR templates

```markdown
### Documentation

- [x] Relevant ADR updated
- [ ] Interface spec changed (link here)
- [x] Diagram updated and committed
```

### In Jira / Azure DevOps

- Link features directly to Markdown file paths
- Add "Related Docs" field
- Include diagrams as attachments (auto-exported if needed)

📌 Keep Markdown as the source of truth. Export only when needed.

---

## Folder Structure for Longevity

```plaintext
docs/
├── adr/
│   ├── 001-initial-design.md
│   ├── 013-json-schema.md
├── interfaces/
│   ├── mqtt-payloads.md
├── vision/
│   └── remote-update-inception.md
├── diagrams/
│   ├── container.dsl
│   ├── ingestion-sequence.mmd
├── tests/
│   └── traceability-matrix.md
├── reviews/
│   └── 2025-q1-architecture-review.md
└── retired/
    ├── 2021-old-platform.md
```

Include:
- `retired/` folder for deprecated docs
- `reviews/` for meeting summaries
- `tests/` with coverage and traceability mappings

---

## Review Checklists That Actually Work

### Inline Markdown Checklists

```markdown
## Review Checklist

- [x] Metadata updated
- [x] Linked artefacts verified
- [ ] Next-review date pushed forward
- [x] Diagram accuracy confirmed
- [ ] Risk log updated if needed
```

Use these in PRs or issue comments.

### Use CI for enforcement

Markdownlint + custom YAML checkers + GitHub Actions = no stowaway artefacts.

---

## Automating Trust

The goal of Docs-as-Code isn’t just convenience. It’s **trust**.

Automation helps you:
- Detect what’s stale
- Enforce standards
- Link docs to delivery
- Surface insights in dashboards
- Make documentation a first-class citizen in your engineering practice

---

## Final Thoughts

Architecture documentation isn’t a one-time task. It’s a continuous act of curation, communication, and alignment.

The tools are there. The habits can be built. The benefit — faster onboarding, fewer bugs, less confusion — is absolutely worth it.

Treat documentation as **code-adjacent**. Keep it versioned, reviewed, owned, and linked to real work. Let it live.

---

📘 Next in the series: [Going Beyond Markdown: Rich, Interactive, and Cross-linked Docs](2025-05-15-beyond-markdown.md)
