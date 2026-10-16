---
date: 2025-03-10T10:17:00
authors:
  - markbac
categories:
  - Git
slug: git-tricks
---

# 10 Git Tricks You Wish You Knew Earlier

This isn’t another **"Git basics"** article listing commands you already use daily. Instead, this post covers **lesser-known Git commands and configurations** that can dramatically improve your workflow. These are the **hidden gems** I wish I knew when I first started using Git. Every time I show someone one of these tricks, I get a **"🤯 why did no one tell me this sooner?"** reaction.

<!-- more -->

These will help you:

- ✅ **Rapidly navigate between branches**
- ✅ **Find the exact commit that introduced a bug**
- ✅ **Trace the history of a function or variable over time**
- ✅ **Speed up Git commands with performance optimisations**

Let's dive in!

***

## 1⃣ Instantly Switch to Your Previous Branch

```sh
git checkout -
```

This command **switches you back to your previous branch**. Instead of typing long branch names, just use `-`.

### Example Usage

```sh
git checkout feature-login  
# Now you need to switch back  
git checkout -  # Instantly returns to the last branch  
```

It also works in **merging**:

```sh
git merge -  # Merges the previous branch into your current one  
```

💡 **Bonus:** This pattern exists in other commands:

* `cd -` switches to your previous directory
* `git merge -` merges the last branch you were on

***

## 2⃣ Find the Exact Commit That Introduced a Bug (`git bisect`)

Finding **which commit introduced a bug** can be painful. `git bisect` **automates the process** using **binary search**, letting you find the bad commit in just a few steps.

### How to Use `git bisect`

1️⃣ Start bisecting:

```sh
git bisect start
```

2️⃣ Mark the **bad commit** (where the bug exists):

```sh
git bisect bad HEAD
```

3️⃣ Mark a **good commit** (where things worked fine):

```sh
git bisect good abc123  # Replace abc123 with a known good commit  
```

4️⃣ Git will **automatically check out a middle commit**. Test your app and mark it:

```sh
git bisect good   # If the bug isn't present  
git bisect bad    # If the bug still exists  
```

5️⃣ Repeat the process until Git finds **the exact commit** that introduced the bug!

🚀 **Bonus:** Automate this process with tests:

```sh
git bisect run npm test
```

This will **automatically run your test suite** on each commit to find the bad one—perfect for CI/CD!

***

## 3⃣ Search Git History for Code Changes (`git log -G "pattern"`)

Want to find **when a specific function, variable, or string changed**? Use:

```sh
git log -G "functionName"
```

This finds **any commit where "functionName" appeared in a change**.

💡 **Bonus:** If you want to find commits where the number of occurrences changed (e.g., a line was added or removed), use `-S`:

```sh
git log -S "config.enableAuth"
```

✅ **Use Case:** Quickly track down when a config flag was added or removed.

***

## 4⃣ Automatically Resolve Merge Conflicts (`git merge -X theirs`)

Merging branches and dealing with conflicts is **annoying**. If you already know **which branch should win**, you can use these flags:

* **Let the incoming branch win:**

  ```sh
  git merge branch-A -X theirs
  ```

* **Keep the current branch’s version in conflicts:**

  ```sh
  git merge branch-A -X ours
  ```

💡 **Use case:** When merging **long-lived branches** and you want to avoid manually resolving conflicts.

***

## 5⃣ Speed Up Git with Performance Tweaks

By default, Git checks **every file** to see if it has changed, which can be **slow in large repositories**. Speed it up with these settings:

```sh
git config core.fsmonitor true  
git config core.untrackedcache true  
```

These cache file changes to make commands like `git status` significantly faster.

🚀 **Bonus:** Make `git branch` sort branches by last commit instead of alphabetically:

```sh
git config --global branch.sort -committerdate
```

***

## 6⃣ Automatically Set Up Remote When Pushing (`git push autosetupremote`)

By default, when you create a new branch, you have to do:

```sh
git push -u origin my-branch
```

To **automatically set up tracking branches**, run:

```sh
git config --global push.autosetupremote true
```

Now you can just:

```sh
git push
```

And Git will **automatically link your local branch to the remote**.

***

## 7⃣ Improve `git diff` Output (`histogram` algorithm)

The default Git diff algorithm **isn't always the best**. Switch to `histogram` for **better change tracking**:

```sh
git config --global diff.algorithm histogram
```

This **groups similar changes together** and makes diffs **much more readable**.

***

## 8⃣ Quickly Go Back in Time (`HEAD@{1.week.ago}`)

You can check out a commit from **a specific time in the past** using:

```sh
git checkout HEAD@{1.week.ago}
```

This lets you quickly test **if a bug was present at that time** without manually finding a commit hash.

💡 **Other formats:**

```sh
git checkout HEAD@{2.days.ago}
git checkout HEAD@{3.months.ago}
```

***

## 9⃣ View a Summary of What Changed (`git shortlog`)

Instead of seeing **every commit**, view a **grouped summary by author**:

```sh
git shortlog -s -n
```

- 🔹 `-s`: Shows just the number of commits
- 🔹 `-n`: Sorts by number of commits

Example output:

```
50  Alice  
35  Bob  
20  Charlie  
```

✅ **Use case:** See who contributed the most to a project!

***

## List All Branches Ordered by Recent Activity

Want to see **branches sorted by last commit** instead of alphabetical order? Use:

```sh
git for-each-ref --sort=-committerdate --format='%(committerdate:relative) %(refname:short)' refs/heads/
```

Example output:

```css
2 hours ago  feature-xyz  
1 day ago    fix-login  
3 days ago   main  
```

💡 **Shortcut:** Set this as an alias in `~/.gitconfig`:

```sh
[alias]
    recent = for-each-ref --sort=-committerdate --format='%(committerdate:relative) %(refname:short)' refs/heads/
```

Now, just run:

```sh
git recent
```

***

## Final Thoughts – Unlocking Git Superpowers

Mastering these **lesser-known Git tricks** will **save you hours** of frustration and manual work.

### Quick Recap of Key Commands

- ✅ **Switch to the last branch:** `git checkout -`
- ✅ **Find a commit that introduced a bug:** `git bisect`
- ✅ **Search history for a function/variable:** `git log -G "pattern"`
- ✅ **Automatically resolve merge conflicts:** `git merge -X theirs`
- ✅ **Speed up Git commands:** `git config core.fsmonitor true`
- ✅ **Go back in time:** `git checkout HEAD@{1.week.ago}`
- ✅ **List branches by recent activity:** `git for-each-ref --sort=-committerdate`
