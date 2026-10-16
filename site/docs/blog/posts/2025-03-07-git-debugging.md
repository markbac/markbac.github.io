---
date: 2025-03-07T10:12:00
authors:
  - markbac
categories:
  - Git
slug: git-debugging
---

# Mastering Git – Part 9: Debugging and Resolving Git Issues

Git is an incredibly powerful tool, but even experienced developers **get stuck** at times. Whether it’s **lost commits, merge conflicts, or detached HEAD states**, Git provides several ways to recover.

<!-- more -->

In this post, we’ll cover:

- ✅ How to **recover lost commits** using `git reflog`
- ✅ **Fixing merge conflicts** efficiently
- ✅ **Dealing with detached HEAD states**
- ✅ **Rolling back to a previous commit**
- ✅ How to **undo pushed commits safely**

By the end, you’ll be able to **debug Git issues confidently** and recover from mistakes like a pro. 🚀

***

## 1. Recovering Lost Commits (`git reflog` to the Rescue!)

### A. What is `git reflog`?

`git reflog` **tracks every action you perform** in Git, even deleted commits.

```sh
git reflog
```

🔹 Example output:

```pgsql
abc123 HEAD@{0}: reset: moving to HEAD~1
def456 HEAD@{1}: commit: Fixed API bug
ghi789 HEAD@{2}: commit: Added login feature
```

If you **accidentally deleted a commit**, you can recover it!

### B. Recovering a Lost Commit

1️⃣ Find the commit hash in `git reflog`\
2️⃣ Reset your branch to that commit:

```sh
git reset --hard abc123
```

✅ **Use case:** You did a **hard reset** and need to recover changes.

***

## 2. Fixing Merge Conflicts

Merge conflicts happen when two branches modify the same file in different ways.

### A. What a Merge Conflict Looks Like

If Git can’t merge automatically, the conflicting file will look like this:

```diff
<<<<<<< HEAD
Your changes here
=======
Their changes here
>>>>>>> feature-branch
```

### B. Resolving a Merge Conflict

1️⃣ Open the file and **manually edit** the conflicting sections.\
2️⃣ **Stage the resolved file** with:

```sh
git add filename.txt
```

3️⃣ **Complete the merge** with:

```sh
git commit -m "Resolved merge conflict"
```

✅ **Use case:** Two people edit the same file, causing a conflict.

***

## 3. Dealing with Detached HEAD State

### A. What is a Detached HEAD?

Detached HEAD happens when you check out a commit instead of a branch.

```sh
git checkout abc123
```

Instead of being on a branch, you’re now on a specific commit. If you make changes, they **won’t be linked to any branch**.

### B. Fixing a Detached HEAD

1️⃣ If you want to **keep your changes**, create a new branch:

```sh
git checkout -b my-recovered-branch
```

2️⃣ If you don’t need the changes, just switch back to `main`:

```sh
git switch main
```

✅ **Use case:** You checked out a commit to inspect something and forgot to switch back.

***

## 4. Rolling Back to a Previous Commit

### A. Reset to an Earlier Commit (Local Only)

1️⃣ Find the commit hash:

```sh
git log --oneline
```

2️⃣ Reset to that commit:

```sh
git reset --hard abc123
```

🚨 **Warning:** This will delete all changes after `abc123`!

✅ **Use case:** You committed something you want to completely discard.

***

### B. Undo a Commit Without Losing Changes

If you just want to **move the branch pointer back** but keep your work:

```sh
git reset --soft HEAD~1
```

✅ **Use case:** You committed too soon and want to edit your changes.

***

### C. Revert a Commit (Safe for Shared Branches)

If you **already pushed the commit**, **do not use reset**—instead, use `revert`:

```sh
git revert abc123
```

✅ **Use case:** You need to undo a commit **without rewriting history**.

***

## 5. Undoing Pushed Commits Safely

### A. Undo the Last Push (Local Branch)

1️⃣ If you **haven’t shared** your changes yet, reset the branch:

```sh
git reset --hard HEAD~1
```

2️⃣ Force push (⚠️ **dangerous, use with caution!**):

```sh
git push --force
```

🚨 **Warning:** This rewrites history—only use on personal branches.

✅ **Use case:** You pushed something by mistake and need to undo it.

***

### B. Undo a Commit That Was Already Pushed (Safe Method)

If the commit was **already shared**, use `git revert` instead of `reset`:

```sh
git revert abc123
git push origin main
```

✅ **Use case:** Undo a pushed commit without breaking the remote history.

***

## 6. Summary of Key Commands

### Recovering Lost Commits

| Action                | Command                          |
| --------------------- | -------------------------------- |
| View Git history      | `git log --oneline`              |
| View all Git actions  | `git reflog`                     |
| Restore a lost commit | `git reset --hard <commit-hash>` |

***

### Fixing Merge Conflicts

| Action                     | Command                             |
| -------------------------- | ----------------------------------- |
| Show conflicts             | `git status`                        |
| Resolve conflict and stage | `git add filename.txt`              |
| Complete the merge         | `git commit -m "Resolved conflict"` |

***

### Fixing Detached HEAD

| Action                                 | Command                               |
| -------------------------------------- | ------------------------------------- |
| Create a new branch from detached HEAD | `git checkout -b my-recovered-branch` |
| Return to main branch                  | `git switch main`                     |

***

### Rolling Back Changes

| Action                                                 | Command                          |
| ------------------------------------------------------ | -------------------------------- |
| Hard reset to an old commit (⚠️ deletes later commits) | `git reset --hard <commit-hash>` |
| Soft reset to an old commit (keeps changes)            | `git reset --soft <commit-hash>` |
| Revert a commit (safe for shared branches)             | `git revert <commit-hash>`       |

***

### Undoing Pushed Commits

| Action                                  | Command                                       |
| --------------------------------------- | --------------------------------------------- |
| Undo last push (⚠️ force push required) | `git reset --hard HEAD~1 && git push --force` |
| Revert a pushed commit safely           | `git revert <commit-hash> && git push`        |

***

## What’s Next?

Now that you know how to **debug and recover from Git issues**, it's time to explore how **Git fits into large-scale development, CI/CD, and DevOps workflows.**

In **Part 10: Git in CI/CD and Large-Scale Development**, we’ll cover:

- ✅ Using Git in **CI/CD pipelines**
- ✅ Managing **large repositories** efficiently
- ✅ Security best practices (`signed commits`, `GPG keys`)
- ✅ GitOps and infrastructure as code
