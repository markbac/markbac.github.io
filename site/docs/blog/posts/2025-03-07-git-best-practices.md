---
date: 2025-03-07T10:09:00
authors:
  - markbac
categories:
  - Git
slug: git-best-practices
---

# Mastering Git – Part 6: Git Best Practices – Writing Clean History

Git makes tracking changes easy, but a messy commit history can make debugging, collaboration, and project management a nightmare. Ever scrolled through a Git log full of "Fixed stuff" and "Final final version"? Yeah, we’ve all been there.

<!-- more -->

In this post, we’ll cover:

- ✅ How to structure commits properly
- ✅ Writing meaningful commit messages
- ✅ Keeping a linear history with `rebase`
- ✅ Using `.gitignore` to keep repositories clean

By the end, you’ll know how to **write clean Git history** that makes future debugging, collaboration, and project maintenance painless.

***

## 1. Why Clean Git History Matters

Messy commit history leads to:

- ❌ Hard-to-follow project evolution
- ❌ Wasted time searching for changes
- ❌ Difficult debugging and rollbacks

Clean Git history ensures:

- ✅ Easier collaboration in teams
- ✅ Clear documentation of changes
- ✅ Simpler debugging and rollback

***

## 2. Structuring Commits Properly

### A. Keep Commits Small and Focused

Each commit should represent a single, logical change.

🔴 Bad Example (one giant commit):

```css
commit abc123
Added login feature, fixed a bug, updated CSS, refactored code
```

✅ Good Example (separate commits):

```pgsql
commit xyz123
feat(auth): Added user login feature

commit def456
fix(ui): Corrected button alignment issue

commit abc789
refactor: Extracted auth logic into separate function
```

**Rule of Thumb:**

* ✅ **One feature = One commit**
* ✅ **One bug fix = One commit**
* ✅ **One refactor = One commit**

***

### B. Writing Meaningful Commit Messages

A good commit message follows this format:

```php-template
<type>(<scope>): <description>

[optional longer description]
```

🔹 **Types of commits**:

* `feat:` – New feature
* `fix:` – Bug fix
* `docs:` – Documentation changes
* `style:` – Code style (whitespace, formatting, missing semicolons)
* `refactor:` – Code change without fixing bugs or adding features
* `test:` – Adding or modifying tests
* `chore:` – Maintenance tasks

🔹 **Good Commit Examples:**

```scss
feat(auth): Add login functionality
```

```scss
fix(api): Handle 500 errors from backend properly
```

```scss
refactor(database): Optimize query performance
```

```scss
docs(readme): Update installation instructions
```

- 🚀 **Why this matters:**
- ✅ Easier to scan history with `git log`
- ✅ Helps with debugging (`git bisect`)
- ✅ Integrates well with CI/CD and release notes

***

## 3. Keeping a Linear History with Rebase

Instead of creating unnecessary merge commits, use `rebase` to keep history clean.

🔹 **Messy history (with merges):**

```sql
*   Merge branch 'feature-branch' into main
|\
| * Commit 3 from feature-branch
| * Commit 2 from feature-branch
| * Commit 1 from feature-branch
*   Previous commit in main
```

🔹 **Clean history (with rebase):**

```sql
* Commit 3 from feature-branch
* Commit 2 from feature-branch
* Commit 1 from feature-branch
* Previous commit in main
```

### Using Rebase Instead of Merge

Instead of:

```sh
git checkout main
git merge feature-branch
```

Use:

```sh
git checkout feature-branch
git rebase main
```

Then push:

```sh
git push --force
```

🚨 **Warning:** Never use `git push --force` on shared branches!

***

## 4. Using `.gitignore` to Keep Repositories Clean

Every project accumulates files that don’t belong in version control (logs, temp files, build artifacts). Git provides `.gitignore` to exclude them.

### A. Creating a `.gitignore` File

Add a `.gitignore` file to the root of your project.

Example for a Node.js project:

```bash
node_modules/
dist/
.env
.DS_Store
```

Example for a Python project:

```bash
__pycache__/
venv/
*.pyc
.env
```

### B. Checking if a File is Ignored

```sh
git check-ignore -v filename
```

### C. Applying `.gitignore` to an Existing Repo

If you've already committed ignored files, remove them:

```sh
git rm -r --cached .
git add .
git commit -m "Updated .gitignore"
```

***

## 5. Best Practices for Writing Clean Git History

✅ **Pull the latest changes before starting work**

```sh
git pull --rebase origin main
```

✅ **Use feature branches for changes**

```sh
git checkout -b feature-branch
```

✅ **Write clear commit messages following conventions**

```sh
git commit -m "feat(api): Add user authentication"
```

✅ **Use `git rebase` instead of `merge` to keep history clean**

```sh
git rebase main
```

✅ **Squash small commits before merging**

```sh
git rebase -i HEAD~3
```

✅ **Use `.gitignore` to exclude unnecessary files**

```sh
echo "node_modules/" >> .gitignore
```

✅ **Avoid unnecessary force pushes on shared branches**

🚨 **Only use `git push --force` if absolutely necessary!**

***

## 6. Summary of Key Commands

| Action                            | Command                                          |
| --------------------------------- | ------------------------------------------------ |
| View commit history               | `git log --oneline --graph --all`                |
| Amend last commit message         | `git commit --amend -m "New message"`            |
| Squash last 3 commits             | `git rebase -i HEAD~3`                           |
| Rebase feature branch onto `main` | `git checkout feature-branch && git rebase main` |
| Create a `.gitignore` file        | `touch .gitignore`                               |
| Remove ignored files from Git     | `git rm -r --cached .`                           |

***

## What’s Next?

Now that you know how to keep Git history clean, it’s time to **automate Git workflows** using hooks!

In **Part 7: Git Hooks and Automation**, we’ll cover:

- ✅ What Git hooks are and how they work
- ✅ Running automated tests before committing
- ✅ Enforcing commit message rules
- ✅ Using tools like Husky for automation
