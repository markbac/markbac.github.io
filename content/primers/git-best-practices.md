---
title: Git practices
---

# Git practices

Git is the version control system almost everyone uses. Its basics take an afternoon to learn; using it so that the history is genuinely useful takes a few habits. A good history answers "what changed, when and why?" years later. A bad one is a list of commits called "fix" and "wip".

## Commits

- **One logical change per commit**. A commit should build and pass tests on its own, so `git bisect` can find the change that introduced a bug.
- **Write useful messages**: a short summary line (around 50 characters, imperative mood: "Add retry to modem attach"), a blank line, then a body explaining why the change was needed and anything surprising. The diff already shows what changed.
- **Conventional Commits** (`feat:`, `fix:`, `docs:` and so on) add a machine-readable type, which tools can use to generate changelogs and version numbers.
- **Commit often locally, tidy before sharing**: `git commit --fixup` and `git rebase --autosquash` let you clean up a branch before review.
- **Never commit secrets**. Use `.gitignore`, a pre-commit hook and secret scanning in CI. If a secret is committed, rotate it; removing it from history is not enough.

## Branching

| Strategy | How it works | Good for |
| --- | --- | --- |
| Trunk-based development | Everyone merges small changes to `main` at least daily; short-lived branches, feature flags for unfinished work | Teams with good automated tests and [CI/CD](cicd-pipelines.md); fastest feedback |
| GitHub flow | A branch per change, a pull request, review, merge to `main`, deploy | Most web services and libraries |
| Git flow | Long-lived `develop` and `main`, plus feature, release and hotfix branches | Products with scheduled releases and several supported versions; adds overhead |
| Release branches | Trunk-based development, with a branch cut for each release and fixes cherry-picked to it | Firmware and products that need to maintain released versions |

[[CAPTION:Table]] Common branching strategies.

Whatever the strategy, keep branches short-lived. A branch that lives for weeks means a painful merge and late feedback.

## Merging

- **Merge commit**: keeps the branch's commits and records the merge. Full history, but noisy.
- **Squash merge**: the whole branch becomes one commit on `main`. Clean, but loses the individual steps.
- **Rebase and merge**: replays the commits on top of `main` for a linear history.

Pick one per repository and use it consistently. Do not rewrite history that others have already pulled; `git push --force-with-lease` is safer than `--force` on your own branches.

## Useful habits

- **Protect `main`**: require pull requests, reviews and passing checks.
- **Tag releases** with annotated, ideally signed, tags following semantic versioning (`v2.4.1`).
- **Sign commits** where provenance matters, with GPG, SSH or Sigstore keys.
- **Use hooks** (with a tool such as pre-commit) for formatting and quick checks before code leaves your machine.
- **Learn a few power tools**: `git bisect` to find a breaking commit, `git blame` (or better, `git log -L`) to find why a line changed, `git reflog` to recover lost work, `git worktree` to work on two branches at once.
- **Large binary files** belong in Git LFS or an artefact store, not in the repository.

## Where next

- [CI/CD pipelines](cicd-pipelines.md) builds on these habits.
- The [Templates](../templates/index.md) section has a pull-request template and a commit-message hook.
- *Pro Git* by Scott Chacon and Ben Straub is free at [git-scm.com/book](https://git-scm.com/book).
