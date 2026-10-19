---
title: Code review checklist
---

# Code review checklist

Use this checklist when you review a pull request. It is a prompt, not a script: skip the sections that do not apply to the change, and spend the time on the ones that do. The sections on timing, memory and hardware are for embedded code.

Let the tools do what tools do well. Formatting, warnings and most coding-standard rules belong in CI, so a reviewer can spend their attention on design, behaviour and risk.

## Before you start

- [ ] **R-1 The pull request says what changed and why,** and links the requirement or ticket.
- [ ] **R-2 CI has passed:** build, static analysis and tests.
- [ ] **R-3 The change is small enough to review properly.** If it is not, ask for it to be split.

## Behaviour

- [ ] **F-1 The code matches the design and the requirements.**
- [ ] **F-2 It does what it should,** including at the edges: empty inputs, maximum sizes, the first and last items.
- [ ] **F-3 It does nothing it should not,** with no hidden side effects and no extra features.
- [ ] **F-4 It is as simple as it can be** while still doing the job.
- [ ] **F-5 It uses what already exists:** standard library functions, real-time operating system (RTOS) primitives, shared utilities, proven algorithms.
- [ ] **F-6 It uses sound patterns,** such as an explicit state machine instead of a tangle of flags, and no copied and pasted blocks.
- [ ] **F-7 Each function does one thing.**
- [ ] **F-8 Every variable is initialised before use,** and there are no unused variables or dead assignments.
- [ ] **F-9 Functions have a single exit** where the coding standard requires it, as MISRA C does.

## Readability

- [ ] **S-1 It follows the team's style guide.**
- [ ] **S-2 Names say what things are,** and follow one convention.
- [ ] **S-3 File and function headers describe the intent,** not just the signature.
- [ ] **S-4 Comments explain why, not what.** Workarounds and temporary fixes say so and link a ticket.
- [ ] **S-5 There are no magic numbers.** Named constants, enumerations or configuration values replace them.
- [ ] **S-6 There is no dead code,** whether commented out or unreachable.
- [ ] **S-7 You could follow it without asking the author.** If you had to ask, the answer belongs in the code or a comment.
- [ ] **S-8 Readability has not been traded for an optimisation nobody measured.**

## Structure

- [ ] **A-1 Functions are short** enough to read without scrolling back and forth.
- [ ] **A-2 Logic is reused, not duplicated.**
- [ ] **A-3 Global variables are avoided,** and every variable has the smallest scope it can.
- [ ] **A-4 Related code is grouped together,** in the same module or class.
- [ ] **A-5 Types are explicit and portable,** such as `int32_t` instead of `long`, and unsigned where a value cannot be negative.
- [ ] **A-6 Nesting is shallow.** There are no `if` statements nested more than two deep, and no `switch` inside a `switch`.
- [ ] **A-7 Values that might change are configuration,** not hard-coded.

## Errors and defensive coding

- [ ] **E-1 Inputs are checked** for range, length, null and sign before use.
- [ ] **E-2 Errors are returned to the caller, and the caller handles them.** No error code is silently dropped.
- [ ] **E-3 Every `switch` has a `default`** that catches the unexpected.
- [ ] **E-4 Array indexes and pointers are bounds-checked.**
- [ ] **E-5 Arithmetic cannot overflow, underflow or truncate** without the code noticing.
- [ ] **E-6 Resources are released on every path,** including error paths: memory, locks, file handles and sockets.
- [ ] **E-7 It copes with failure around it:** a service that is down, a database write that fails, malformed data, a full queue.
- [ ] **E-8 Operations that may be retried are safe to retry.**
- [ ] **E-9 It behaves under load,** or the limits are stated.

## Security

- [ ] **SEC-1 External input is validated,** from a serial port, a bus, Bluetooth, the network or a user, including its length.
- [ ] **SEC-2 Memory access is safe,** with no buffer overflows and no unchecked copies.
- [ ] **SEC-3 Injection is not possible,** for example database query injection, command injection or cross-site scripting.
- [ ] **SEC-4 Secrets are not in the code or the logs.**
- [ ] **SEC-5 Debug interfaces are disabled or protected in release builds,** such as debug probe ports and debug serial consoles.

## Memory

- [ ] **M-1 Dynamic allocation is avoided,** or it is bounded and predictable.
- [ ] **M-2 Every allocation is checked for failure.**
- [ ] **M-3 Stack use is analysed,** and the worst case is recorded, especially in interrupts and any recursion.
- [ ] **M-4 Pointers are initialised and checked before use.**

## Timing and concurrency

- [ ] **T-1 Worst-case timing is bounded.** There are no unbounded loops or recursion.
- [ ] **T-2 There are no race conditions.** Variables shared with an interrupt are `volatile`, and multi-byte values are read and written atomically.
- [ ] **T-3 Code called from more than one context is re-entrant and thread-safe.**
- [ ] **T-4 Interrupt handlers are short and never block,** and interrupts are not masked for long.
- [ ] **T-5 Interrupts pass work to tasks safely,** through queues, flags or notifications.
- [ ] **T-6 Shared resources are protected** by a mutex or semaphore, and priority inversion is avoided or handled.
- [ ] **T-7 Task priorities match how critical each task is.**
- [ ] **T-8 The watchdog is kicked only when every task is making progress,** not from a timer that runs whatever happens.

## Hardware

- [ ] **H-1 Input and output operations leave the hardware in the right state.**
- [ ] **H-2 The interface timing meets the datasheet,** including setup, hold and minimum delays.
- [ ] **H-3 Multi-byte hardware registers cannot change while they are read or written.**
- [ ] **H-4 A reset puts the system in a known state.**
- [ ] **H-5 Brown-out and power loss are handled.**
- [ ] **H-6 Entering and leaving sleep is correct,** with timers and peripherals reconfigured.
- [ ] **H-7 Unused interrupt vectors go to an error handler.**
- [ ] **H-8 Non-volatile writes survive power loss,** for example by keeping two copies of each record in EEPROM (electrically erasable programmable read-only memory) or flash.

## Logging

- [ ] **L-1 Logs record what someone will need to diagnose a problem,** including the values that matter.
- [ ] **L-2 Each message has the right level:** debug, info, warning or error.
- [ ] **L-3 A message makes sense on its own,** without the source code open beside it.
- [ ] **L-4 Logging is not excessive,** and nothing sensitive is logged.

## Tests and tools

- [ ] **TST-1 New behaviour has tests,** and bug fixes have a test that failed before the fix.
- [ ] **TST-2 Modules can be tested on their own,** with hardware access and delays behind an interface that a test can replace.
- [ ] **TST-3 Coverage has been checked** for the changed code.
- [ ] **TST-4 Static analysis is clean,** or each finding it suppresses has a reason, against MISRA C, cppcheck or the team's ruleset.
- [ ] **TST-5 The build has no warnings,** with warnings enabled, and informational messages have been read.

## Commits

- [ ] **C-1 Each commit message says what changed and why.** It follows the [commit conventions](pull-request-and-commits.md).
- [ ] **C-2 Commits reference the ticket or requirement.**
- [ ] **C-3 The pull request makes one change.** Unrelated fixes go in their own pull request.

**As Markdown.** To copy it into an issue, a pull request or a review record:

````markdown
## Before you start
- [ ] **R-1 The pull request says what changed and why,** and links the requirement or ticket.
- [ ] **R-2 CI has passed:** build, static analysis and tests.
- [ ] **R-3 The change is small enough to review properly.** If it is not, ask for it to be split.

## Behaviour
- [ ] **F-1 The code matches the design and the requirements.**
- [ ] **F-2 It does what it should,** including at the edges: empty inputs, maximum sizes, the first and last items.
- [ ] **F-3 It does nothing it should not,** with no hidden side effects and no extra features.
- [ ] **F-4 It is as simple as it can be** while still doing the job.
- [ ] **F-5 It uses what already exists:** standard library functions, real-time operating system (RTOS) primitives, shared utilities, proven algorithms.
- [ ] **F-6 It uses sound patterns,** such as an explicit state machine instead of a tangle of flags, and no copied and pasted blocks.
- [ ] **F-7 Each function does one thing.**
- [ ] **F-8 Every variable is initialised before use,** and there are no unused variables or dead assignments.
- [ ] **F-9 Functions have a single exit** where the coding standard requires it, as MISRA C does.

## Readability
- [ ] **S-1 It follows the team's style guide.**
- [ ] **S-2 Names say what things are,** and follow one convention.
- [ ] **S-3 File and function headers describe the intent,** not just the signature.
- [ ] **S-4 Comments explain why, not what.** Workarounds and temporary fixes say so and link a ticket.
- [ ] **S-5 There are no magic numbers.** Named constants, enumerations or configuration values replace them.
- [ ] **S-6 There is no dead code,** whether commented out or unreachable.
- [ ] **S-7 You could follow it without asking the author.** If you had to ask, the answer belongs in the code or a comment.
- [ ] **S-8 Readability has not been traded for an optimisation nobody measured.**

## Structure
- [ ] **A-1 Functions are short** enough to read without scrolling back and forth.
- [ ] **A-2 Logic is reused, not duplicated.**
- [ ] **A-3 Global variables are avoided,** and every variable has the smallest scope it can.
- [ ] **A-4 Related code is grouped together,** in the same module or class.
- [ ] **A-5 Types are explicit and portable,** such as `int32_t` instead of `long`, and unsigned where a value cannot be negative.
- [ ] **A-6 Nesting is shallow.** There are no `if` statements nested more than two deep, and no `switch` inside a `switch`.
- [ ] **A-7 Values that might change are configuration,** not hard-coded.

## Errors and defensive coding
- [ ] **E-1 Inputs are checked** for range, length, null and sign before use.
- [ ] **E-2 Errors are returned to the caller, and the caller handles them.** No error code is silently dropped.
- [ ] **E-3 Every `switch` has a `default`** that catches the unexpected.
- [ ] **E-4 Array indexes and pointers are bounds-checked.**
- [ ] **E-5 Arithmetic cannot overflow, underflow or truncate** without the code noticing.
- [ ] **E-6 Resources are released on every path,** including error paths: memory, locks, file handles and sockets.
- [ ] **E-7 It copes with failure around it:** a service that is down, a database write that fails, malformed data, a full queue.
- [ ] **E-8 Operations that may be retried are safe to retry.**
- [ ] **E-9 It behaves under load,** or the limits are stated.

## Security
- [ ] **SEC-1 External input is validated,** from a serial port, a bus, Bluetooth, the network or a user, including its length.
- [ ] **SEC-2 Memory access is safe,** with no buffer overflows and no unchecked copies.
- [ ] **SEC-3 Injection is not possible,** for example database query injection, command injection or cross-site scripting.
- [ ] **SEC-4 Secrets are not in the code or the logs.**
- [ ] **SEC-5 Debug interfaces are disabled or protected in release builds,** such as debug probe ports and debug serial consoles.

## Memory
- [ ] **M-1 Dynamic allocation is avoided,** or it is bounded and predictable.
- [ ] **M-2 Every allocation is checked for failure.**
- [ ] **M-3 Stack use is analysed,** and the worst case is recorded, especially in interrupts and any recursion.
- [ ] **M-4 Pointers are initialised and checked before use.**

## Timing and concurrency
- [ ] **T-1 Worst-case timing is bounded.** There are no unbounded loops or recursion.
- [ ] **T-2 There are no race conditions.** Variables shared with an interrupt are `volatile`, and multi-byte values are read and written atomically.
- [ ] **T-3 Code called from more than one context is re-entrant and thread-safe.**
- [ ] **T-4 Interrupt handlers are short and never block,** and interrupts are not masked for long.
- [ ] **T-5 Interrupts pass work to tasks safely,** through queues, flags or notifications.
- [ ] **T-6 Shared resources are protected** by a mutex or semaphore, and priority inversion is avoided or handled.
- [ ] **T-7 Task priorities match how critical each task is.**
- [ ] **T-8 The watchdog is kicked only when every task is making progress,** not from a timer that runs whatever happens.

## Hardware
- [ ] **H-1 Input and output operations leave the hardware in the right state.**
- [ ] **H-2 The interface timing meets the datasheet,** including setup, hold and minimum delays.
- [ ] **H-3 Multi-byte hardware registers cannot change while they are read or written.**
- [ ] **H-4 A reset puts the system in a known state.**
- [ ] **H-5 Brown-out and power loss are handled.**
- [ ] **H-6 Entering and leaving sleep is correct,** with timers and peripherals reconfigured.
- [ ] **H-7 Unused interrupt vectors go to an error handler.**
- [ ] **H-8 Non-volatile writes survive power loss,** for example by keeping two copies of each record in EEPROM (electrically erasable programmable read-only memory) or flash.

## Logging
- [ ] **L-1 Logs record what someone will need to diagnose a problem,** including the values that matter.
- [ ] **L-2 Each message has the right level:** debug, info, warning or error.
- [ ] **L-3 A message makes sense on its own,** without the source code open beside it.
- [ ] **L-4 Logging is not excessive,** and nothing sensitive is logged.

## Tests and tools
- [ ] **TST-1 New behaviour has tests,** and bug fixes have a test that failed before the fix.
- [ ] **TST-2 Modules can be tested on their own,** with hardware access and delays behind an interface that a test can replace.
- [ ] **TST-3 Coverage has been checked** for the changed code.
- [ ] **TST-4 Static analysis is clean,** or each finding it suppresses has a reason, against MISRA C, cppcheck or the team's ruleset.
- [ ] **TST-5 The build has no warnings,** with warnings enabled, and informational messages have been read.

## Commits
- [ ] **C-1 Each commit message says what changed and why.** It follows the [commit conventions](pull-request-and-commits.md).
- [ ] **C-2 Commits reference the ticket or requirement.**
- [ ] **C-3 The pull request makes one change.** Unrelated fixes go in their own pull request.
````


## Further reading

Many of the embedded items follow the peer review checklist in Philip Koopman's *Better Embedded System Software* (Drumnadrochit Education, 2010).
