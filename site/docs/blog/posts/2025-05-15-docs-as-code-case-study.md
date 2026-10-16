---
date: 2025-05-15T09:13:00
authors:
  - markbac
categories:
  - Docs as Code
slug: docs-as-code-case-study
---

# Case Study: Multi-Layer Docs-as-Code in Practice

When you're building a product platform that spans firmware, application logic, cloud APIs, and customer-specific integration layers, documentation can quickly become fragmented and inconsistent.

<!-- more -->

This is the reality many engineering teams face — not a single codebase or platform, but multiple projects built on shared components, reused patterns, and evolving specs. Add regulatory pressure, onboarding demands, and the occasional SharePoint requirement, and Docs-as-Code needs to be more than just a markdown folder in Git.

This post walks through a realistic case study of how we structured documentation across multiple product layers using Docs-as-Code principles. We’ll cover:

- Realistic multi-layer folder and metadata structure
- Shared firmware and reusable application artefacts
- Per-project overlays for configuration and integration
- Markdown first with Word/PDF export for SharePoint
- CI integration for validation and publishing

---

## The Context

We were building a product platform used in multiple domains. Each deployment had:

- A shared firmware base (same bootloader, same update mechanism)
- Reusable application components (CLI, OTA updater, diagnostics)
- Project-specific configuration and deployment scripts
- System-level integration (cloud APIs, test harnesses, external partners)

Teams were distributed across embedded, cloud, QA, and DevOps — each needing to document their layer without breaking others.

---

## Folder Structure: Base + Overlay

We chose a **layered folder structure** with:

- Reusable, product-level artefacts in `/docs/core`
- Project-specific overlays in `/docs/projects/{project-name}`

### Core folder

```plaintext
docs/
├── core/
│   ├── firmware/
│   │   ├── bootloader.md
│   │   └── update-flow.mmd
│   ├── application/
│   │   ├── cli-commands.md
│   │   └── telemetry-schema.md
│   ├── adr/
│   │   └── 001-unified-updater.md
│   ├── tests/
│   │   └── firmware-traceability.md
```

### Project-specific overlays

```plaintext
docs/
├── projects/
│   ├── alpha-launch/
│   │   ├── interfaces/
│   │   │   └── mqtt-profile.md
│   │   ├── system/
│   │   │   └── end-to-end-flow.md
│   │   └── integration/
│   │       └── external-api-adapter.md
│   ├── beta-pilot/
│   │   └── interfaces/
│   │       └── rest-vs-mqtt-comparison.md
```

Each project could override, extend, or reference core content without forking it.

---

## Metadata and Ownership

Each file had consistent frontmatter:

```yaml
title: "MQTT Interface for Alpha"
owner: "integration-team"
layer: "project"
component: "mqtt-gateway"
last-reviewed: "2025-03-01"
next-review: "2026-03-01"
status: "active"
```

This allowed us to:

- Generate dashboards by layer/component/team
- Schedule reviews
- Flag undocumented interfaces or deprecated views

---

## Reuse and Inheritance

Rather than copy shared content, we linked to it explicitly:

```markdown
This project uses the shared [bootloader flow](../../core/firmware/update-flow.mmd).

Refer to [ADR-001](../../core/adr/001-unified-updater.md) for rationale behind the unified update mechanism.
```

Diagrams were embedded using Markdown extensions that rendered Mermaid or PlantUML inline.

---

## Templates for Artefact Types

To promote consistency, we scaffolded new artefacts from templates:

### ADR Template

```markdown
---
title: "ADR-XXX: Decision Title"
owner: "team-name"
status: "draft"
component: ""
linked-artefacts: []
---

## Context

## Decision

## Consequences

## Alternatives Considered
```

### Integration Spec Template

```markdown
---
title: "Integration: {partner/system}"
component: "api-adapter"
layer: "project"
owner: "integration-team"
---

## Overview

## Protocol

## Authentication

## Failure Modes

## Related Docs
```

---

## CI: Validation, Exports, Dashboards

We used GitHub Actions to:

- Run `markdownlint` on all `.md` files
- Validate frontmatter metadata with a Python script
- Generate exportable `.docx` and `.pdf` using Pandoc
- Build a `docs-dashboard.json` index for frontend rendering
- Notify on overdue reviews based on `next-review`

### Example CI snippet

```yaml
- name: Check frontmatter schema
  run: python scripts/validate_metadata.py docs/
```

### Export snippet

```bash
for file in $(find docs -name "*.md"); do
  pandoc "$file" -o "${file%.md}.pdf"
done
```

These exports were pushed to a SharePoint sync folder weekly using an Rclone job.

---

## SharePoint Coexistence

Not all stakeholders lived in Git. Some lived in SharePoint.

We supported both by:

- Keeping Markdown as the canonical source
- Exporting PDFs/docx for SharePoint
- Embedding QR codes or Git commit hashes in footer

```markdown
Generated from source at commit abc123 on 2025-03-01
```

This built confidence without compromising process.

---

## Traceability and Filtering

Using tags and consistent metadata allowed us to build traceability tools:

- List all tests linked to a feature
- Show all artefacts owned by a team
- Highlight undocumented interface endpoints

Scripts parsed metadata and rendered JSON for dashboards.

```json
{
  "component": "mqtt-gateway",
  "artefacts": [
    "mqtt-profile.md",
    "mqtt-vs-rest.md"
  ]
}
```

---

## Lessons Learned

### Start with Ownership

Every artefact must have an owner and review plan. Otherwise, it will rot.

### Avoid Forking Docs

Share core artefacts. Use overlays for per-project customisation.

### Render Everything

Don't keep diagrams as static images. Render them from `.mmd` and `.puml` every build.

### Push, Don’t Author, in SharePoint

Generate Word/PDF as output. Author in markdown.

### Use Templates and Metadata Everywhere

Consistency beats prettiness. A sparse doc with metadata is better than a shiny orphan.

---

## What Worked Well

| Practice                         | Outcome                               |
|----------------------------------|----------------------------------------|
| Layered folder structure         | Clean separation of core vs project    |
| YAML frontmatter                 | Dashboards, review alerts, filtering   |
| CI integration                   | Confidence in every PR                 |
| Export to SharePoint             | Kept wider teams in the loop           |
| Template-driven docs             | Reduced decision fatigue               |

---

## Example Project View

```plaintext
docs/
├── core/
│   ├── firmware/
│   ├── application/
│   ├── adr/
│   ├── tests/
├── projects/
│   ├── alpha-launch/
│   │   ├── interfaces/
│   │   ├── system/
│   │   └── integration/
├── scripts/
│   ├── validate_metadata.py
│   ├── export_pdfs.sh
│   └── generate_dashboard.py
└── output/
    └── sharepoint-ready/
```

---

## Final Thoughts

Docs-as-Code isn't just about Markdown. It's about **clarity, consistency, and context across teams**.

When you’re working with firmware, applications, cloud systems, and customer overlays — your documentation needs to be composable, traceable, and automatable.

This case study showed how a practical, disciplined approach to metadata, structure, templates, and CI made that possible — without overwhelming contributors or fragmenting ownership.

---

📘 Next in the series: [Building a Documentation Culture That Lasts](2025-05-15-documentation-culture.md)
