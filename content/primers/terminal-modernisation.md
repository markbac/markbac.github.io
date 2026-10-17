---
title: A modern terminal
---

# A modern terminal

Engineers spend hours a day at a command line. A few tools make that time faster and less error-prone. A good prompt shows the Git branch and whether the last command failed; suggestions come from history as you type; syntax highlighting shows a mistyped command before you run it. Oh My Zsh and Oh My Posh are the two most popular ways to get there.

## Oh My Zsh

Oh My Zsh is a community framework for configuring Zsh, the default shell on macOS and widely used on Linux. It bundles hundreds of plugins and themes behind a single `~/.zshrc`.

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

Read any script before piping it into a shell; the installer is short and worth a look.

Useful plugins, enabled in `~/.zshrc` with `plugins=(git z docker zsh-autosuggestions zsh-syntax-highlighting)`:

- **git**: dozens of short aliases (`gst` for `git status`, `gco` for `git checkout`).
- **z** or **zoxide**: jump to frequently used directories by part of their name.
- **zsh-autosuggestions** and **zsh-syntax-highlighting**: separate projects, installed into Oh My Zsh's custom plug-ins folder, that suggest commands from history and colour commands as you type.
- **history-substring-search**: search history by any part of a command.

## Oh My Posh

Oh My Posh is a prompt engine, not a shell framework. It works with PowerShell, Bash, Zsh, Fish, Nushell and cmd (through Clink), on Windows, macOS and Linux, so one prompt configuration can follow you everywhere. Themes are JSON, YAML or TOML files.

```powershell
winget install JanDeDobbeleer.OhMyPosh
oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH/paradox.omp.json" | Invoke-Expression
```

Put the second line in your PowerShell profile to load it every time. On macOS and Linux, install it with Homebrew or the install script and add the matching `init` line for your shell.

## Prompt themes

A good prompt shows the current directory, Git branch and status, the exit status of the last command and the duration of slow commands. It also shows anything that changes how commands behave, such as a Python virtual environment, a Kubernetes context or an SSH session.

- **Powerlevel10k** is a fast, very configurable Zsh theme with a setup wizard (`p10k configure`). Its author has said it will receive only limited maintenance from now on, so consider an alternative for new set-ups.
- **Starship** is a fast, cross-shell prompt written in Rust and configured in TOML, similar in scope to Oh My Posh.
- Oh My Posh ships with many themes, including a Powerlevel10k look-alike.

Most themes need a **Nerd Font** (a programming font patched with icons, such as MesloLGS NF or FiraCode Nerd Font) set in the terminal.

## Which to use

| | Oh My Zsh | Oh My Posh |
| --- | --- | --- |
| What it is | Zsh configuration framework: plugins, aliases, themes | Prompt engine only |
| Shells | Zsh | PowerShell, Bash, Zsh, Fish, Nushell, cmd |
| Platforms | macOS, Linux, WSL | Windows, macOS, Linux |
| Best for | Zsh users who want plugins as well as a prompt | Windows users, or one prompt across several shells |

[[CAPTION:Table]] Oh My Zsh and Oh My Posh compared.

They work together: Oh My Zsh for plugins, with Oh My Posh or Starship drawing the prompt.

## Keep it fast

Each plugin adds start-up time. If a new terminal takes more than half a second to appear, remove plugins you do not use. On Windows, a modern terminal application (Windows Terminal, WezTerm or Alacritty) makes a bigger difference than any prompt.

## Where next

- [Git practices](git-best-practices.md) pairs well with a Git-aware prompt.
- The project sites are [ohmyz.sh](https://ohmyz.sh/), [ohmyposh.dev](https://ohmyposh.dev/) and [starship.rs](https://starship.rs/).
