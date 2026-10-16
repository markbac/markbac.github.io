---
date: 2025-03-07T10:11:00
authors:
  - markbac
categories:
  - Git
slug: advanced-git
---

# Mastering Git – Part 8: Advanced Git – Stashing, Cherry-Picking, and Submodules

As you get more comfortable with Git, you’ll encounter situations where you need to:

- ✅ **Temporarily save changes without committing** (stashing)
- ✅ **Apply a specific commit from another branch** (cherry-picking)
- ✅ **Manage external dependencies inside a Git repo** (submodules)

<!-- more -->

These are advanced but **incredibly useful** Git features that can make your workflow smoother and more efficient.

In this post, we’ll cover:

- 🔹 How to use **`git stash`** to temporarily save and restore work
- 🔹 How to **cherry-pick specific commits** into another branch
- 🔹 How to **work with Git submodules** for managing dependencies

By the end, you’ll be able to **handle complex Git scenarios with ease**! 🚀

***

## 1. Stashing Changes – Saving Work for Later

Imagine you're working on a feature, but suddenly need to switch branches. You don’t want to commit half-finished work, so you **stash it** instead.

### A. Saving Work with `git stash`

```sh
git stash
```

- ✅ **Saves all modified and staged files without committing**
- ✅ **Lets you switch branches without losing progress**

***

### B. Viewing Stashed Changes

To see a list of all stashed changes:

```sh
git stash list
```

🔹 Example output:

```less
stash@{0}: WIP on feature-branch: abc123 Fix login bug
stash@{1}: WIP on main: def456 Updated README
```

***

### C. Restoring Stashed Work

1️⃣ **Apply the last stash (keeps it in stash list)**

```sh
git stash apply
```

2️⃣ **Apply and remove the last stash**

```sh
git stash pop
```

3️⃣ **Apply a specific stash**

```sh
git stash apply stash@{1}
```

4️⃣ **Remove a stash without applying it**

```sh
git stash drop stash@{0}
```

5️⃣ **Clear all stashed changes**

```sh
git stash clear
```

🚀 **Use case:** Stash unfinished work when switching branches.

***

## 2. Cherry-Picking – Selecting Specific Commits

Sometimes, you need a commit from another branch without merging the whole branch. **Cherry-picking** lets you do exactly that.

### A. How to Cherry-Pick a Commit

1️⃣ Find the commit hash you need:

```sh
git log --oneline
```

Example output:

```pgsql
abc123 Fix login bug
def456 Improve UI design
ghi789 Add API endpoint
```

2️⃣ Cherry-pick the commit into your branch:

```sh
git cherry-pick abc123
```

✅ This applies **only the selected commit** to the current branch.

***

### B. Cherry-Picking Multiple Commits

```sh
git cherry-pick abc123 def456
```

***

### C. Handling Cherry-Pick Conflicts

If conflicts occur, resolve them manually, then:

```sh
git cherry-pick --continue
```

To abort the cherry-pick:

```sh
git cherry-pick --abort
```

🚀 **Use case:** Apply a critical bug fix from another branch without merging unwanted changes.

***

## 3. Git Submodules – Managing External Dependencies

Sometimes, your project depends on another repository. Instead of copying files manually, **Git submodules** let you include another repository inside your project.

### A. Adding a Submodule

```sh
git submodule add https://github.com/user/library.git external-library
```

✅ This adds `library.git` inside the `external-library` folder.

***

### B. Cloning a Repository with Submodules

If a repo has submodules, clone it with:

```sh
git clone --recurse-submodules https://github.com/user/project.git
```

If you already cloned without submodules, run:

```sh
git submodule update --init --recursive
```

***

### C. Updating Submodules

To fetch the latest updates from a submodule:

```sh
git submodule update --remote
```

***

### D. Removing a Submodule

1️⃣ Untrack the submodule:

```sh
git submodule deinit external-library
```

2️⃣ Remove its entry from `.gitmodules`:

```sh
rm -rf .git/modules/external-library
```

3️⃣ Remove the submodule directory:

```sh
rm -rf external-library
```

🚀 **Use case:** When working with shared dependencies across multiple projects.

***

## 4. Summary of Key Commands

### Stashing Work

| Action                      | Command                     |
| --------------------------- | --------------------------- |
| Stash changes               | `git stash`                 |
| View stashed changes        | `git stash list`            |
| Apply last stash            | `git stash apply`           |
| Apply and remove last stash | `git stash pop`             |
| Apply a specific stash      | `git stash apply stash@{1}` |
| Remove a stash              | `git stash drop stash@{0}`  |
| Clear all stashes           | `git stash clear`           |

***

### Cherry-Picking Commits

| Action                             | Command                               |
| ---------------------------------- | ------------------------------------- |
| Cherry-pick a commit               | `git cherry-pick <commit-hash>`       |
| Cherry-pick multiple commits       | `git cherry-pick <commit1> <commit2>` |
| Continue after resolving conflicts | `git cherry-pick --continue`          |
| Abort cherry-pick                  | `git cherry-pick --abort`             |

***

### Working with Submodules

| Action                       | Command                                     |
| ---------------------------- | ------------------------------------------- |
| Add a submodule              | `git submodule add <repo-url> <path>`       |
| Clone a repo with submodules | `git clone --recurse-submodules <repo-url>` |
| Init and update submodules   | `git submodule update --init --recursive`   |
| Update submodules to latest  | `git submodule update --remote`             |
| Remove a submodule           | `git submodule deinit <path>`               |

***

## What’s Next?

Now that you’ve mastered advanced Git features, it’s time to **debug and fix Git issues like a pro!**

In **Part 9: Debugging and Resolving Git Issues**, we’ll cover:

- ✅ Recovering lost commits (`git reflog`)
- ✅ Fixing merge conflicts efficiently
- ✅ Dealing with detached HEAD state
- ✅ Rolling back to a previous state
