---
date: 2025-03-07T10:04:00
authors:
  - markbac
categories:
  - Git
slug: git-fundamentals
---

# Mastering Git – Part 1: Git Fundamentals – The Absolute Basics

Git is one of the most powerful and widely used version control systems, but for newcomers, it can feel overwhelming. Even experienced developers sometimes use Git without fully understanding its capabilities. This post will introduce the core concepts, set up your environment, and walk through the fundamental commands every developer should know.

<!-- more -->

By the end of this post, you'll have Git installed, understand the basic workflow, and be able to confidently track changes in your projects.

***

## What is Git? Why Should You Use It?

Git is a **distributed version control system (DVCS)** that tracks changes in files over time. It allows multiple people to work on a project without overwriting each other’s work, making it essential for collaboration.

### Why use Git?

- ✅ **Tracks history** – You can see what changed, when, and by whom.
- ✅ **Prevents data loss** – Easily revert mistakes and recover previous versions.
- ✅ **Enables collaboration** – Multiple developers can work on the same project simultaneously.
- ✅ **Works offline** – You don’t need an internet connection to commit changes.
- ✅ **Backbone of DevOps** – Integrated into modern CI/CD and automation pipelines.

***

## Installing and Setting Up Git

First, you need to install Git:

* **Windows**: Download and install Git from [git-scm.com](https://git-scm.com/downloads). During installation, choose "Git Bash" for a better terminal experience.
* **Mac**: Install via Homebrew with `brew install git`.
* **Linux**: Use your package manager (e.g., `sudo apt install git` for Debian/Ubuntu).

Once installed, configure Git with your name and email (used for commit authorship):

```sh
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Check if Git is installed correctly:

```sh
git --version
```

***

## Git’s Core Concepts

Before jumping into commands, let’s break down Git’s key components:

- 🔹 **Repository (Repo)** – A Git project containing all files and history.
- 🔹 **Commit** – A snapshot of your project at a specific point in time.
- 🔹 **Branch** – A separate line of development that can be merged later.
- 🔹 **Working Directory** – Your actual files that you edit.
- 🔹 **Staging Area** – A place where you prepare changes before committing.
- 🔹 **HEAD** – A pointer to your latest commit.

***

## Creating a New Git Repository

### 1. Initialising a Repository

To start tracking a project, navigate to its directory and run:

```sh
git init
```

This creates a hidden `.git` folder where Git stores all its data.

### 2. Cloning an Existing Repository

Instead of starting from scratch, you can copy an existing Git project using:

```sh
git clone https://github.com/user/repo.git
```

This creates a local copy of the repository on your machine.

***

## The Git Workflow: Add → Commit → Push

Once Git is tracking your project, the typical workflow involves three steps:

1️⃣ **Add changes to the staging area**\
2️⃣ **Commit the changes with a message**\
3️⃣ **Push the commit to a remote repository (e.g., GitHub, GitLab)**

### 1. Checking the Status of Your Repository

Before making changes, check what’s currently happening in your repo:

```sh
git status
```

This tells you if there are modified files, untracked files, or staged files ready to commit.

### 2. Adding Files to the Staging Area

To track changes in a file, add it to the staging area:

```sh
git add filename.txt
```

To add all modified files:

```sh
git add .
```

### 3. Committing Changes

A commit saves the current state of the staged files with a message describing the changes:

```sh
git commit -m "Added new feature"
```

### 4. Viewing Commit History

See previous commits with:

```sh
git log --oneline --graph --all
```

This gives a condensed view of the commit history.

***

## Working with Remote Repositories

To collaborate with others, you need to connect to a remote repository (like GitHub).

### 1. Adding a Remote Repository

To link your local repo to a remote server, use:

```sh
git remote add origin https://github.com/user/repo.git
```

### 2. Pushing Changes to a Remote Repository

Once you’ve committed changes, upload them with:

```sh
git push origin main
```

(Replace `main` with your branch name if different.)

### 3. Pulling the Latest Changes

To fetch updates from the remote repo and merge them into your local branch:

```sh
git pull origin main
```

***

## Undoing Mistakes – Quick Fixes

- 🔹 **Forgot to stage a file?** Run `git add` and commit again.
- 🔹 **Want to edit the last commit message?** Use `git commit --amend`.
- 🔹 **Accidentally committed too early?** Use `git reset --soft HEAD~1` to uncommit but keep changes.

***

## Summary of Key Commands

| Action              | Command                           |
| ------------------- | --------------------------------- |
| Initialise a repo   | `git init`                        |
| Clone a repo        | `git clone URL`                   |
| Check status        | `git status`                      |
| Stage a file        | `git add filename`                |
| Stage all files     | `git add .`                       |
| Commit changes      | `git commit -m "Message"`         |
| View commit history | `git log --oneline --graph --all` |
| Push changes        | `git push origin main`            |
| Pull latest changes | `git pull origin main`            |

***

## What’s Next?

Now that you know how to set up a Git repository, track changes, and push them to a remote repo, the next step is understanding **branches and merging**.

In the next post, **we'll dive into branching strategies, merging, and handling conflicts effectively**. Stay tuned! 🚀
