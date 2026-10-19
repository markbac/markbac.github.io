"""MkDocs hook: fill blog/all-posts.md with every blog post, by category, so the list never goes stale."""
import re
from collections import defaultdict

import yaml

PAGE = "blog/all-posts.md"
MARKER = "<!-- posts-list -->"


def _post(file):
    text = file.content_string
    meta = {}
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if m:
        meta = yaml.safe_load(m.group(1)) or {}
    if meta.get("draft"):
        return None
    title = re.search(r"^# (.+)$", text, re.M)
    return {
        "title": title.group(1).strip() if title else file.name,
        "path": file.src_uri,
        "categories": meta.get("categories") or ["Other"],
    }


def on_page_markdown(markdown, page, config, files):
    if page.file.src_uri != PAGE or MARKER not in markdown:
        return markdown
    by_category = defaultdict(list)
    count = 0
    for f in files:
        if f.src_uri.startswith("blog/posts/") and f.src_uri.endswith(".md"):
            post = _post(f)
            if post:
                count += 1
                by_category[post["categories"][0]].append(post)
    out = [f"{count} posts, by category. Each post is listed under its first category.", ""]
    for category in sorted(by_category, key=str.lower):
        posts = sorted(by_category[category], key=lambda p: p["title"].lower())
        out += [f"## {category}", ""]
        out += [f"- [{p['title']}]({p['path'][len('blog/'):]})" for p in posts]
        out.append("")
    return markdown.replace(MARKER, "\n".join(out))
