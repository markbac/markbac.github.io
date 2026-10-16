# markbac.github.io

The source of two sites, built from the same Markdown with [py-doc](https://github.com/markbac/py-doc):

- **https://markbac.github.io/**: my personal home page, with every section and the blog.
- **https://tarf.co.uk/**: the same sections behind the tarf.co.uk home page.

## Layout

| Path | What it holds |
| --- | --- |
| `content/<section>/` | One py-doc document per section: guidelines, standards, handbook, primers, reference, glossary, templates and checklists |
| `site/docs/blog/` | Blog posts, for MkDocs Material's blog plugin |
| `site/mkdocs.yml` | The markbac.github.io site. py-doc writes the section pages and `py-doc-nav.yml`, which this file inherits |
| `site/mkdocs.tarf.yml` | The tarf.co.uk site: inherits `mkdocs.yml` and changes the name, address and home page |
| `site/overrides/` | Both home pages (`partials/home-personal.html`, `partials/home-tarf.html`) and their section cards |
| `py-doc.yml` | The sections, their Word and PDF outputs, lint settings and the two site targets |

## Build

```bash
pip install "py-doc @ git+https://github.com/markbac/py-doc"
py-doc tools build          # once: the tool image with pandoc, the diagram tools and MkDocs
py-doc lint content site/docs/blog
py-doc build --keep-going   # build/<section>.docx and .pdf
py-doc site build           # site/build (markbac.github.io) and site/build-tarf (tarf.co.uk)
py-doc site build --target tarf
```

To work on the site with live reload, run `py-doc site generate`, then `mkdocs serve` in `site/`
(or `mkdocs serve -f mkdocs.tarf.yml` for the tarf version).

## Publishing

`.github/workflows/site.yml` builds both sites on every push and pull request. On `main` it deploys
markbac.github.io with GitHub Pages, and pushes the tarf.co.uk build to
[markbac/web-content](https://github.com/markbac/web-content), which tarf.co.uk's host pulls by
webhook. The tarf push is off until the repository variable `TARF_DEPLOY` is `true`, and it needs a
`WEB_CONTENT_TOKEN` secret.

## Licence

MIT, unless a section's own folder says otherwise.
