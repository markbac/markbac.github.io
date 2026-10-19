---
title: Documentation and modelling tools
---

# Documentation and modelling tools

A crucial part of our **Docs as Code** approach is treating documentation just like code. This means we can apply the same development principles-like version control, automated checks, and continuous delivery-to our written artifacts. The result is documentation that's always up-to-date, accurate, and easily accessible.

This guide outlines the tooling stack that makes this possible and how to integrate it into our workflows.

## The Power of Markdown

Markdown is our chosen syntax for all written documentation. It's a lightweight markup language that is both human-readable and can be converted to other formats, like HTML or PDF.

* **Simplicity and Consistency:** You can write Markdown in any text editor, making it easy for everyone on the team, regardless of their role or technical background, to contribute to and maintain our documentation. This is a huge win for collaboration.

* **Version Control:** By storing all .md files in our version control system, every change is tracked and auditable. We can see who made a change, when, and why. This is essential for traceability and compliance, especially for regulated products.

## Static Site Generators

While Markdown is great for writing, it's not ideal for browsing a large collection of documents. This is where a **Static Site Generator** comes in. Tools like **MkDocs** and **Sphinx** transform our raw Markdown files into a professional, searchable, and navigable website.

* **Automated Publishing:** Our CI/CD pipeline can automatically build and publish the updated site whenever a documentation change is merged. This ensures our documentation is always live and in sync with our codebase and hardware designs.

* **Search and Navigation:** These tools automatically create a navigation menu and a powerful search function, making it easy for anyone to find the information they need without digging through file systems. They handle the hard work of organizing content so we can focus on writing.

## Diagrams as Code

For complex systems, a picture is worth a thousand words. But a static image can quickly become outdated. Our solution is to use **diagrams as code** with tools like **Mermaid** and **PlantUML**.

* **Version-Controlled Diagrams:** These tools allow you to write simple, human-readable code that generates a diagram. The code for the diagram is stored directly in the Markdown file, meaning it's version-controlled alongside the rest of the documentation.

* **Always in Sync:** The diagram is rendered automatically when the static site is built, so it can never fall out of sync with the documentation it's describing. If a change is made to the system, the corresponding diagram code can be updated in the same pull request.

* **No Special Software:** This approach removes the need for separate diagramming software and external image files, which often leads to diagrams becoming outdated.

For example, using the **C4 model**, you can create a high-level context diagram and a detailed component diagram all within your Markdown files. This makes it easy for a new team member to understand the architecture without having to hunt for an old PowerPoint slide.

## Toolchain Integration

The power of this approach comes from seamlessly integrating these tools into our CI/CD pipeline. Here's a simplified example of how this might work for a documentation job in our pipeline:

1. **Lint Markdown:** A CI job checks all Markdown files for formatting and syntax errors, ensuring consistency and catching common mistakes before they're merged.

2. **Validate Diagrams:** The pipeline validates that the Mermaid or PlantUML code is correctly formatted. This prevents broken diagrams from being published.

3. **Build Site:** The static site generator builds the documentation site from the Markdown files and renders the diagrams.

4. **Publish:** The updated site is automatically published to a web server for everyone to access.

This process provides immediate feedback on documentation changes and ensures that our "living artifacts" are always in a pristine and usable state. It transforms documentation from a manual chore into an automated, integrated part of our delivery pipeline.
