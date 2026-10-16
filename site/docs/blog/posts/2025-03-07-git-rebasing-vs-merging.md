---
date: 2025-03-07T10:06:00
authors:
  - markbac
categories:
  - Git
slug: git-rebasing-vs-merging
---

# Mastering Git – Part 3: Rebasing vs Merging – When and Why?

One of the most debated topics in Git is **merge vs rebase**. Both commands achieve the same goal—integrating changes from one branch into another—but they do so in very different ways.

<!-- more -->

Used correctly, rebasing can keep your commit history **clean and linear**, while merging preserves **context and history**. But misusing either can lead to confusion, lost work, and unhappy teammates.

In this post, we'll break down:

- ✅ The difference between `merge` and `rebase`
- ✅ When to use each strategy
- ✅ How to perform safe rebasing
- ✅ Common pitfalls and best practices

By the end, you'll know exactly when to use `merge` and when to use `rebase` without breaking your repository.

***

## Merging vs Rebasing – The Key Difference

### What Happens When You Merge?

A **merge** combines two branches and creates a new **merge commit**, preserving the original branch history.

```sh
git switch main
git merge feature-branch
```

- 🔹 **Pros of Merging**:
- ✔️ Preserves history – You can see when branches were merged.
- ✔️ Safe – No history rewriting, ideal for teams.

- 🔹 **Cons of Merging**:
- ❌ Can create **messy history** if overused.
- ❌ Merge commits may clutter `git log`.

***

### What Happens When You Rebase?

A **rebase** moves all commits from your branch **on top of the latest `main`** as if they were created after the most recent `main` commit.

```sh
git switch feature-branch
git rebase main
```

- 🔹 **Pros of Rebasing**:
- ✔️ Keeps a **clean, linear history**.
- ✔️ Avoids unnecessary merge commits.

- 🔹 **Cons of Rebasing**:
- ❌ **Rewrites history**, which can be dangerous.
- ❌ Can cause conflicts that must be resolved **for each commit**.

***

## When to Use Merge vs Rebase

✅ **Use `merge` when**:

* You want to **preserve history** for clarity.
* You're working in a **team** and need to track when branches were merged.
* You’re merging a **feature branch into `main`**.

✅ **Use `rebase` when**:

* You want a **clean history** without unnecessary merge commits.
* You're working on a **personal branch** (not shared yet).
* You need to **keep up-to-date with `main`** before merging.

🚨 **Never rebase a branch that has already been pushed and shared** unless you know what you’re doing!

***

## How to Perform a Safe Rebase

### 1. Rebasing a Feature Branch onto `main`

```sh
git switch feature-branch
git rebase main
```

If there are conflicts, Git will pause the rebase and ask you to fix them manually.

1️⃣ Resolve conflicts in the affected files.\
2️⃣ Stage them with:

```sh
git add filename
```

3️⃣ Continue the rebase:

```sh
git rebase --continue
```

4️⃣ If you get stuck, **abort the rebase** with:

```sh
git rebase --abort
```

***

## Interactive Rebase – Squashing Commits

If you have **too many small commits**, you can squash them into one using **interactive rebase**.

```sh
git rebase -i HEAD~3
```

This opens an editor showing the last **3 commits**:

```sql
pick abc123 First commit
pick def456 Second commit
pick ghi789 Third commit
```

Change `pick` to `squash` (`s`) for the commits you want to merge:

```sql
pick abc123 First commit
squash def456 Second commit
squash ghi789 Third commit
```

Git will then let you edit the commit message. Once done, save and exit to complete the rebase.

✅ **Best for cleaning up unnecessary commits before pushing.**

***

## The Danger of Rebasing Shared Branches

🚨 If you **rebase a branch that has already been pushed to a shared repository**, you will **rewrite history** for everyone.

For example, if you've rebased `feature-branch` and try to push:

```sh
git push origin feature-branch
```

Git will reject it because the remote branch has different commits. To **force push** (⚠️ dangerous!):

```sh
git push --force
```

🔴 **Warning**: This will overwrite the remote branch and erase any changes made by others!

✅ Instead, use **pull with rebase** to sync your branch safely:

```sh
git pull --rebase origin main
```

***

## Merge vs Rebase – Which is Better?

| Feature                       | Merge | Rebase     |
| ----------------------------- | ----- | ---------- |
| **Preserves history**         | ✅ Yes | ❌ No       |
| **Creates merge commits**     | ✅ Yes | ❌ No       |
| **Ideal for team workflows**  | ✅ Yes | ❌ No       |
| **Keeps history clean**       | ❌ No  | ✅ Yes      |
| **Risk of rewriting history** | ❌ No  | ✅ Yes (⚠️) |

🚀 **Rule of Thumb:**

* **Use `merge`** for shared branches and team workflows.
* **Use `rebase`** for keeping your local commits clean before merging.

***

## Summary of Key Commands

| Action                                    | Command                                        |
| ----------------------------------------- | ---------------------------------------------- |
| Merge branch into `main`                  | `git switch main && git merge feature-branch`  |
| Rebase feature branch onto `main`         | `git switch feature-branch && git rebase main` |
| Continue rebase after conflict            | `git rebase --continue`                        |
| Abort rebase                              | `git rebase --abort`                           |
| Interactive rebase (e.g., last 3 commits) | `git rebase -i HEAD~3`                         |
| Pull with rebase                          | `git pull --rebase origin main`                |
| Push after rebase (⚠️ careful!)           | `git push --force`                             |

***

## What’s Next?

Now you understand the difference between merging and rebasing, but what happens when you need to **fix mistakes**?

In **Part 4: Git Reset, Revert, and Amend – Fixing Mistakes**, we’ll dive into **undoing commits, rolling back changes, and recovering lost work**!

👉 **Stay tuned!** 🚀
