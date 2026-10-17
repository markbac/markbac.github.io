---
title: Static code analysis
---

# Static code analysis

Static code analysis examines source code without running it, looking for bugs, security weaknesses, style problems and risky constructs. Because it needs no tests or test environment, it can run on every change in seconds to minutes. It also finds problems that tests rarely cover, such as an error path that is never exercised.

## What it finds

- **Defects**: null pointer dereferences, buffer overruns, use after free, resource leaks, uninitialised variables, unreachable code, integer overflow.
- **Security weaknesses**: injection, hard-coded secrets, unsafe functions, tainted data reaching a dangerous sink.
- **Standards violations**: MISRA C, SEI CERT, or your own coding rules.
- **Maintainability problems**: high complexity, duplication, overly long functions, dependency cycles.
- **Style and formatting**, usually better handled by a formatter that fixes it automatically.

## Kinds of tool

| Kind | What it does | Examples |
| --- | --- | --- |
| Formatter | Rewrites code into one consistent style | clang-format, Black, Ruff format, rustfmt, Prettier |
| Linter | Fast checks for common mistakes and style | Ruff, ESLint, clang-tidy, Clippy, ShellCheck |
| Type checker | Checks types in dynamically typed languages | mypy, Pyright, TypeScript |
| Deep analyser | Data-flow and path analysis across functions and files | Cppcheck, the Clang Static Analyzer, Coverity, Polyspace, PVS-Studio |
| Security scanner (SAST) | Looks for vulnerability patterns and tainted data flows | Semgrep, CodeQL, Bandit, SonarQube |
| Quality platform | Tracks findings and metrics over time | SonarQube, SonarCloud |

[[CAPTION:Table]] Families of static analysis tools.

Related checks often run alongside: dependency scanning (known vulnerabilities in libraries), secret scanning, and infrastructure-as-code scanning.

## Making it useful

- **Start in the editor**: the cheapest place to fix a finding is before it is committed. Most tools have editor plug-ins and pre-commit hooks.
- **Run it in the [CI pipeline](cicd-pipelines.md)** and fail the build on new findings of agreed severity.
- **Deal with legacy findings gradually**: a baseline that hides existing findings, with a rule that new code must be clean, works better than a thousand warnings on day one.
- **Tune the rules**: switch off checks that do not fit the codebase, and document why. Too many false positives and people stop reading the results.
- **Suppress narrowly**: when a finding is wrong, suppress that one instance with a comment explaining why, not the whole rule.
- **Combine it with other checks**: static analysis complements [testing](testing-strategies.md), [code review](code-review.md) and run-time tools such as sanitisers (AddressSanitizer, UndefinedBehaviorSanitizer) and fuzzing; it does not replace them.

## For embedded C and C++

Compiler warnings are the first and cheapest analyser: build with `-Wall -Wextra` (and more) and treat warnings as errors. Add clang-tidy or Cppcheck for every change, and a deeper commercial tool or MISRA checker where the product's safety or certification needs it.

## Where next

- [Secure coding practices](secure-coding-practices.md) describes the weaknesses these tools look for.
- The [Tech Radar](../radar/index.md) lists the recommended tools, and the [Guidelines](../guidelines/index.md) set the rules they enforce.
