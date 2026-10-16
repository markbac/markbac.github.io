---
date: 2025-03-07T10:05:00
authors:
  - markbac
categories:
  - Git
slug: git-branching-and-merging
---

# Mastering Git – Part 2: Understanding Branching and Merging

Git’s true power lies in its ability to **manage multiple lines of development** through **branching**. If you’ve ever worked on a feature, bug fix, or experiment while keeping the main project stable, you’ve already used the concept of branching. Whether you realised it or not!

<!-- more -->

In this post, we'll cover:

- ✅ What branches are and why they matter
- ✅ Creating, switching, and deleting branches
- ✅ Merging changes and handling conflicts
- ✅ Best practices for working with branches

By the end, you’ll be confidently using Git branches to organise your work and collaborate effectively.

***

## What is a Branch?

A **branch** in Git is like a separate timeline of your project. You can develop features, fix bugs, or experiment without affecting the main codebase until you’re ready.

- 🔹 The **default branch** in Git is called `main` (or `master` in older projects).
- 🔹 A **new branch** is a copy of the main branch at a given point.
- 🔹 You can **switch between branches** without affecting each other.
- 🔹 Once a branch is complete, it can be **merged** back into `main`.

***

## Creating and Managing Branches

### 1. Viewing Existing Branches

To see all branches in your repository:

```sh
git branch
```

🔹 The branch you’re currently on is marked with `*`.

### 2. Creating a New Branch

To create a new branch named `feature-branch`:

```sh
git branch feature-branch
```

However, this only creates the branch—it does **not** switch to it.

### 3. Switching Between Branches

To move to your new branch:

```sh
git checkout feature-branch
```

or, in newer versions of Git (recommended):

```sh
git switch feature-branch
```

To create and switch to a branch in one command:

```sh
git checkout -b feature-branch
```

or

```sh
git switch -c feature-branch
```

### 4. Deleting a Branch

Once a branch is no longer needed, delete it with:

```sh
git branch -d feature-branch
```

🔹 If the branch hasn’t been merged yet, Git may warn you. To force delete:

```sh
git branch -D feature-branch
```

***

## Merging Branches – Combining Changes

Once your branch is ready, you’ll want to merge it back into `main`.

### 1. Merging a Branch (Fast-Forward Merge)

If no changes have been made to `main` since the branch was created, Git will perform a **fast-forward merge**, moving the `HEAD` pointer forward.

```sh
git checkout main
git merge feature-branch
```

or using `switch` (recommended):

```sh
git switch main
git merge feature-branch
```

This applies all commits from `feature-branch` into `main` without creating a separate merge commit.

### 2. Merging with Conflicts (Three-Way Merge)

If `main` has changed since the branch was created, Git creates a **merge commit** to combine both sets of changes.

```sh
git switch main
git merge feature-branch
```

If changes overlap in the same file, Git will **detect a conflict** and show:

```pgsql
CONFLICT (content): Merge conflict in file.txt
```

To resolve:\
1️⃣ Open the conflicting file and manually edit the changes.\
2️⃣ Once resolved, **stage the file** with:

```sh
git add file.txt
```

3️⃣ Complete the merge with:

```sh
git commit -m "Resolved merge conflict"
```

***

## Merge vs Rebase – What’s the Difference?

- 🔹 **Merge** keeps history as-is and creates a new merge commit.
- 🔹 **Rebase** moves your changes on top of the latest `main`, keeping a linear history.

Example of rebasing:

```sh
git switch feature-branch
git rebase main
```

Then push with:

```sh
git push --force
```

🚨 **Warning:** Never rebase a shared branch in a team unless everyone understands rebasing!

More on this in **Part 3: Merging vs Rebasing – When and Why?**

***

## Best Practices for Branching and Merging

✅ **Use descriptive branch names**\
Bad: `new-branch`\
Good: `feature/user-authentication`

✅ **Keep branches small and focused**\
Long-lived branches become hard to merge.

✅ **Regularly pull changes from `main`**\
Stay up to date to avoid big conflicts later.

✅ **Delete merged branches**\
Clean up old branches to keep your repo tidy.

✅ **Use feature branches, not `main`**\
Always develop in branches to keep `main` stable.

***

## Summary of Key Commands

| Action                   | Command                                    |
| ------------------------ | ------------------------------------------ |
| List branches            | `git branch`                               |
| Create a new branch      | `git branch branch-name`                   |
| Switch branches          | `git switch branch-name`                   |
| Create and switch        | `git switch -c branch-name`                |
| Merge branch into `main` | `git switch main && git merge branch-name` |
| Delete branch (merged)   | `git branch -d branch-name`                |
| Delete branch (force)    | `git branch -D branch-name`                |

***

## What’s Next?

Now you know how to create branches, switch between them, and merge changes. But should you always merge? What about **rebasing**?

In the next post, **we’ll explore rebase vs merge, when to use each, and how to keep a clean Git history**.

👉 Stay tuned for **Part 3: Rebasing vs Merging – When and Why?** 🚀
