---
date: 2025-05-13T09:03:00
authors:
  - markbac
categories:
  - Docs as Code
slug: structuring-docs
---

# Structuring Docs for Complex Systems: Layered, Flexible, and Discoverable

The larger and more complex your systems, the more likely it is that your documentation is a mess.

<!-- more -->

I’ve seen product specs dumped in project folders, firmware architecture notes mixed with customer config guides. I’ve seen developers forced to trawl SharePoint, Confluence, and half a dozen repos to piece together how a system works.

That’s not a tooling problem — it’s a **structuring problem**.

In this post, I’ll walk through how to structure documentation for complex systems so it’s layered, flexible, and discoverable. You might have a monorepo or multi-repo setup, internal platforms or customer-specific deployments, Git or SharePoint. Either way, these principles help you create a doc setup that scales with your organisation.

---

## Why Structure Matters

Most docs fail not because they aren’t written, but because they can’t be found, understood, or trusted.

Poorly structured documentation leads to:

- **Duplication** – teams rewriting what already exists
- **Rot** – outdated or unowned docs that persist in search results
- **Frustration** – new joiners getting lost, experienced devs ignoring docs
- **Risk** – missing the one critical integration note buried in the wrong folder

Structure makes the difference between a library and a landfill.

---

## Monorepos vs Multi-Repo Setups

Start by understanding how your codebase is organised. Documentation should mirror your **code architecture**, not fight it.

### Monorepos

When all your services, firmware, or components live in one repo:

- Pros:
  - Easier cross-linking between artefacts
  - Shared CI/CD for building and publishing docs
  - One place to search

- Cons:
  - Can become bloated if not segmented
  - Confusing if product vs project docs aren't separated

📌 Tip: Use top-level folders like `/docs/product/`, `/docs/system/`, `/docs/project-abc/`

### Multi-Repo

When each component or team has its own repo:

- Pros:
  - Natural ownership and focus
  - Lightweight and decentralised
- Cons:
  - Harder to create a unified site or search
  - Cross-referencing is trickier

📌 Tip: Use a **docs-only aggregation repo** (e.g. `engineering-docs/`) that indexes and links into other repos. Use Git submodules or CI pipelines to pull in content.

---

## Shared Platform Docs vs Per-Project Overlays

In every system I’ve worked on, there are two layers of documentation:

- **Shared** (platform-level APIs, firmware behaviour, reusable components)
- **Overlays** (project-specific config, customer integration, deployment tweaks)

You have to **explicitly separate** these or you’ll end up with diagrams and specs that don’t reflect reality.

```plaintext
docs/
├── platform/
│   ├── api/
│   ├── firmware/
│   └── internal-guides/
├── overlays/
│   ├── customer-a/
│   │   ├── deployment.md
│   │   └── config-overrides.md
│   ├── customer-b/
│   └── partner-x/
```

This model has worked well for:

- Teams managing product SDKs + bespoke integrations
- Firmware platforms reused across hardware variants
- Cloud services reused across industries but configured differently

---

## Git-Based vs SharePoint-Based Content

Many organisations (especially larger or older ones) have documentation split between:

- **Git** (Markdown-based, dev-maintained, versioned)
- **SharePoint or Word** (PM-maintained, customer deliverables, compliance)

You don’t have to choose between them — just **define which content lives where**, and how it connects.

| Content Type                  | Best Fit Location        |
|------------------------------|--------------------------|
| Architecture diagrams         | Git (versioned, embedded)|
| Test strategies               | Git                      |
| Project timelines             | SharePoint               |
| Handover packs                | SharePoint               |
| Interface specs               | Git (canonical), SharePoint (formatted export) |
| Vision/strategy decks         | SharePoint               |

📌 Tip: Use Pandoc or MkDocs plugins to generate PDFs/Word exports from markdown if needed for upload to SharePoint.

---

## Ownership-Anchored Folder Structures

Structure should reflect **who owns what**. That way, you can enforce review policies, assign maintenance, and reduce orphaned docs.

Example:

```plaintext
docs/
├── platform/         # owned by product/platform team
├── system/           # owned by architects/integration team
├── project-xyz/      # owned by delivery/integration engineers
├── support/          # owned by ops/SRE
├── rfcs/             # owned by cross-functional teams
└── adr/              # owned by team leads or component owners
```

📌 Tip: Add a `README.md` or `OWNERS.md` in each folder stating purpose, owner, and review cadence.

---

## Use of Index Files, Search, and Navigation

Documentation is only discoverable if it’s navigable. This is where tools like **MkDocs**, **Docusaurus**, or **Hugo** shine.

### Use index files

Each folder should contain an `index.md` or `README.md` explaining what’s in it.

### Enable full-text search

Use static site generators with search plugins or Algolia integrations.

### Cross-link frequently

Use relative links (`../api/serial.md`) or anchors to tie docs together across folders and topics.

📌 Tip: Use [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) with features like tabs, nested nav, and instant search. It works brilliantly for large documentation portals.

---

## Diagram of a Real-World Structure

Here’s a simplified folder structure used across multiple products, system integrations, and deployments:

```plaintext
docs/
├── index.md
├── product/
│   ├── overview.md
│   ├── firmware/
│   │   ├── rtos.md
│   │   ├── comms.md
│   │   └── bootloader.md
│   └── api/
│       ├── serial.md
│       └── mqtt.md
├── system/
│   ├── context.md
│   ├── deployment.md
│   ├── integration.md
│   └── risk-register.md
├── projects/
│   ├── project-a/
│   ├── project-b/
│   └── project-c/
├── rfcs/
├── adr/
└── support/
```

This supports:

- Clean separation by scope
- Clear ownership
- Easy navigation
- Reuse of common platform docs

---

## Final Thoughts

You don’t need perfect documentation. But you do need structure.

A well-structured doc repo:

- Scales with product and system complexity
- Keeps platform docs clean and reusable
- Prevents customer-specific hacks from polluting core docs
- Enables contribution and review from the right teams
- Makes onboarding and debugging faster

It doesn’t matter if your tooling is Markdown + Git or Word + SharePoint — the same principles apply: **separation, ownership, and discoverability**.

Structure your docs like you structure your codebase — with intention, modularity, and an eye on scale.

---

📘 Next in the series: [Key Artefacts Across the Stack: What to Write and Why](2025-05-15-key-artefacts.md)
