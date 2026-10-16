---
title: Pull requests and commits
---

# Pull requests and commits

A pull request and its commits are the record of why the code is the way it is. Someone reading `git log` or `git blame` in three years' time should be able to find out what changed, why, and what evidence showed that it worked.

## Pull request template

Save this as `.github/pull_request_template.md` (GitHub) or `.gitlab/merge_request_templates/Default.md` (GitLab), so every new pull request starts from it.

[[CAPTION:Figure]] Pull request template.

```markdown
## What and why

What this change does, and the problem it solves.

## Links

- Requirement:
- Ticket:
- ADR or RFC:

## Evidence

- Tests run and their results:
- Effect on size, timing, memory or power:

## Risk and rollback

What could go wrong, and how to undo the change.

## Checklist

- [ ] Commits and test names reference the requirement IDs
- [ ] Documentation updated
- [ ] Breaking change flagged in the title and the commit (`!`)
- [ ] AI assistance disclosed with an `Assisted-by:` trailer
- [ ] Safety-related, certified or regulated code touched (say which)
```

The [Definition of Done](definition-of-done.md) and the [code review checklist](code-review-checklist.md) say what the reviewer will look for.

## Commit messages

Use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/). The type at the start of the first line tells readers and release tools what kind of change it is. A changelog and the next version number can then come straight from the history.

```text
<type>[(scope)][!]: <description>

[body: what changed and why, wrapped at 72 characters]

[trailers]
```

[[CAPTION:Table]] Conventional Commits types.

| Type | Use it for |
|------|------------|
| `feat` | A new feature (a minor version) |
| `fix` | A bug fix (a patch version) |
| `perf` | A change that makes the code faster or smaller |
| `refactor` | A change that neither fixes a bug nor adds a feature |
| `test` | Adding or correcting tests |
| `docs` | Documentation only |
| `build` | The build system or dependencies |
| `ci` | The CI configuration |
| `style` | Formatting, with no change in meaning |
| `chore` | Anything else that does not touch the product code |
| `revert` | Reverting an earlier commit |

An exclamation mark before the colon, or a `BREAKING CHANGE:` trailer, marks a change that breaks compatibility (a major version).

```text
feat(telemetry): send readings as CBOR

JSON payloads were 3.1 times larger and cost too much airtime on NB-IoT.
CBOR keeps the same structure, so the cloud decoder changes but the data
model does not.

Refs: REQ-GW-0042, ADR-0007
Assisted-by: Claude
```

- Write the description in the imperative ("add", not "added"), in lower case, with no full stop, and keep the first line to 72 characters or fewer.
- Use the body to explain why. The diff already shows what.
- Put references in trailers: `Refs:` for tickets and requirements, `Assisted-by:` for AI tools, `Co-authored-by:` for people.

## Commit message hook

This Git hook rejects a commit whose first line is not a Conventional Commits header. It is a POSIX shell script, so it runs with the Git that comes with every platform, Git for Windows included. Download [`commit-msg`](https://github.com/markbac/markbac.github.io/raw/main/content/templates/files/commit-msg), then install it in the repository:

```bash
mkdir -p .githooks
cp commit-msg .githooks/
chmod +x .githooks/commit-msg
git config core.hooksPath .githooks
```

Commit the `.githooks` folder, so that everyone gets the same hook. Each person runs the `git config` line once per clone. The `COMMIT_TYPES` variable changes the allowed types, and `REQUIRE_REFS=1` makes a `Refs:` trailer compulsory.

A hook runs on the developer's machine and can be skipped, so check the same rule in CI on the pull request title or its commits.
