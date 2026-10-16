---
date: 2025-03-07T10:07:00
authors:
  - markbac
categories:
  - Git
slug: git-fixing-mistakes
---

# Mastering Git – Part 4: Git Reset, Revert, and Amend – Fixing Mistakes

Mistakes happen. Maybe you committed the wrong file, pushed a broken change, or need to undo something you did earlier. The good news? Git makes it easy to recover.

<!-- more -->

In this post, we’ll cover:

- ✅ The difference between `reset`, `revert`, and `amend`
- ✅ Undoing commits without losing work
- ✅ Rolling back changes safely
- ✅ Recovering deleted commits

By the end, you’ll know exactly how to fix mistakes in Git **without panicking**.

***

## 1. Understanding `reset`, `revert`, and `amend`

Before diving in, let’s clarify the differences:

- 🔹 **`git reset`** – Moves the branch pointer backwards, **erasing commits from history**.
- 🔹 **`git revert`** – Creates a new commit that undoes changes from a previous commit.
- 🔹 **`git commit --amend`** – Edits the last commit (message or files).

- ✅ **Use `reset`** when you want to **undo commits** (local history rewrite).
- ✅ **Use `revert`** when you need to **undo changes safely** (for shared branches).
- ✅ **Use `amend`** when you want to **edit the last commit** without making a new one.

***

## 2. Undoing the Last Commit

### A. Soft Reset – Keep Changes in Staging Area

If you committed too soon but want to **keep your changes staged**:

```sh
git reset --soft HEAD~1
```

- ✅ Moves the branch back **one commit** but **keeps your changes** staged.
- ✅ Allows you to commit again with a better message.

***

### B. Mixed Reset – Keep Changes in Working Directory

If you committed too soon but **don’t want changes staged**:

```sh
git reset --mixed HEAD~1
```

- ✅ Moves the branch back **one commit** and **unstages files**.
- ✅ Changes remain in the working directory but are not staged.

***

### C. Hard Reset – Erase Everything ( Dangerous!)

If you want to **completely erase the last commit and its changes**:

```sh
git reset --hard HEAD~1
```

❌ **Warning:** This **deletes** the commit and **all changes**. Use with caution!

***

## 3. Reverting a Commit (Safe for Shared Branches)

Unlike `reset`, which erases history, `revert` creates a **new commit** that undoes changes from a previous commit.

```sh
git revert HEAD
```

- ✅ **Use when working in teams** to undo a commit safely.
- ✅ Keeps history **intact** while reversing changes.

To revert a specific commit (not the latest):

```sh
git revert <commit-hash>
```

🔹 **Example:** If commit `abc123` introduced a bug, undo it with:

```sh
git revert abc123
```

***

## 4. Amending the Last Commit

If you made a typo in a commit message or forgot to include a file, you can **edit the last commit** instead of making a new one.

### A. Changing the Commit Message

```sh
git commit --amend -m "New commit message"
```

✅ Replaces the previous commit message with a new one.

***

### B. Adding More Files to the Last Commit

If you forgot to include a file in the last commit:

```sh
git add forgotten-file.txt
git commit --amend --no-edit
```

✅ Updates the last commit **without changing the message**.

🚨 **Warning:** If you already pushed the commit, amending will rewrite history!

Push with **force** if necessary (⚠️ Be careful!):

```sh
git push --force
```

***

## 5. Recovering Lost Commits (`reflog` to the Rescue!)

If you **accidentally reset or deleted commits**, they might still be recoverable using `git reflog`.

```sh
git reflog
```

This shows **all recent actions**, including resets and hard resets.

🔹 Example output:

```pgsql
abc123 HEAD@{0}: reset: moving to HEAD~1
def456 HEAD@{1}: commit: Added new feature
ghi789 HEAD@{2}: commit: Fixed bug
```

To restore a lost commit:

```sh
git reset --hard <commit-hash>
```

✅ Works even after a **hard reset**!

***

## 6. Resetting a Single File Instead of the Whole Commit

If you staged a file but haven’t committed yet:

```sh
git reset filename.txt
```

✅ Unstages the file while keeping your changes.

If you **want to discard changes** completely (⚠️ cannot be undone!):

```sh
git checkout -- filename.txt
```

✅ Resets the file to the last committed version.

***

## 7. Reset vs Revert – Which One to Use?

| Action                           | `reset`           | `revert` |
| -------------------------------- | ----------------- | -------- |
| **Removes commit from history?** | ✅ Yes             | ❌ No     |
| **Erases changes?**              | ✅ Hard reset only | ❌ No     |
| **Creates a new commit?**        | ❌ No              | ✅ Yes    |
| **Safe for shared branches?**    | ❌ No              | ✅ Yes    |

🚀 **Rule of Thumb:**

* **Use `reset`** for local history cleanups.
* **Use `revert`** when working in a team.

***

## Summary of Key Commands

| Action                                    | Command                                            |
| ----------------------------------------- | -------------------------------------------------- |
| Undo last commit (keep changes staged)    | `git reset --soft HEAD~1`                          |
| Undo last commit (keep changes, unstaged) | `git reset --mixed HEAD~1`                         |
| Undo last commit (delete changes)         | `git reset --hard HEAD~1`                          |
| Revert a commit (safe for teams)          | `git revert <commit-hash>`                         |
| Amend last commit message                 | `git commit --amend -m "New message"`              |
| Add files to last commit                  | `git add file.txt && git commit --amend --no-edit` |
| Recover deleted commits                   | `git reflog && git reset --hard <commit-hash>`     |

***

## What’s Next?

Now you know how to **undo mistakes, edit commits, and recover lost work**. But what about working with **remote repositories and teams**?

In **Part 5: Remote Repositories and Working with Teams**, we’ll cover:

- ✅ `git push` vs `git pull`
- ✅ Handling remote conflicts
- ✅ Forking vs cloning
- ✅ Team collaboration workflows
