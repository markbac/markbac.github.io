---
title: Defect report checklist
---

# Defect report checklist

A good defect report lets someone who has never seen the problem reproduce it. A poor one starts a conversation that takes longer than the fix. Use this checklist when you raise a defect and again when you close it.

## Raising a defect

- [ ] **DC-1 Describe the environment.** Give the hardware variant and revision, the firmware or software version with its commit, and the operating system or RTOS version. Include any non-default settings, build flags or feature flags, and the state the system was in before the failure.
- [ ] **DC-2 Reproduce it.** Retest until you have the exact steps in the right order. If it is intermittent, say how often it happens, for example "3 in 100 power cycles". Narrow down which part of the system is involved, using error codes and logs.
- [ ] **DC-3 Attach the evidence.** Include console logs, traces with their correlation IDs, logic analyser or network captures, crash dumps, register state and backtraces, and screenshots or recordings.
- [ ] **DC-4 Stick to the facts.** Say what happened and what you expected. Leave out guesses about the cause, opinions and blame. Use the headings in the template below.
- [ ] **DC-5 Set the severity, and let the product owner set the priority** (see below).

## Template

```markdown
### Summary
<One line: what fails, and under what conditions.>

### Environment
- Device and revision:
- Firmware version and commit:
- Other components and versions:
- Configuration that differs from the default:

### Preconditions
1. <The state the system must be in first.>

### Steps to reproduce
1. <Step.>
2. <Step.>

### Expected result
<What should happen.>

### Actual result
<What happens instead. If it is intermittent, how often.>

### Evidence
- <Log, capture, dump or screenshot, attached or linked.>
```

## Example

```markdown
### Summary
Modem does not reconnect after deep sleep when the signal is weak (-115 dBm).

### Environment
- Device and revision: gateway, revision C
- Firmware version and commit: v2.4.1 (a3b7c89f)
- Other components and versions: modem firmware BG95M3LAR02A03, FreeRTOS 10.4.3
- Configuration that differs from the default: none

### Preconditions
1. Device provisioned with a working SIM on band 20.
2. RF attenuator set to give -115 dBm RSRP.

### Steps to reproduce
1. Put the device to sleep from the CLI: `system sleep --duration 300`.
2. Wait 300 seconds for the RTC to wake it.
3. Watch the diagnostic UART while the modem powers up.

### Expected result
The modem driver restarts, the modem registers within 45 seconds, and the
device reports that it is connected.

### Actual result
The modem powers up, but its first AT command times out after 10 seconds.
The driver then retries forever and flattens the backup battery in about
four hours. Happens every time at -115 dBm, and never at -90 dBm.

### Evidence
- console-reconnect-fail.log
- power-rail-ch1.png (oscilloscope)
- uart-at-timeout.sr (logic analyser)
```

## Severity and priority

Severity and priority are separate. Severity is how much damage the defect does, and it rarely changes. Priority is how soon it must be fixed, which is a business decision and can change from week to week. A cosmetic fault on the launch demo can be urgent, and a crash in a feature nobody uses yet can wait.

[[CAPTION:Table]] Severity levels.

| Severity | Meaning | Examples |
|----------|---------|----------|
| S1 Critical | The system stops, data is lost or corrupted, or security is broken, with no workaround | Crash or boot loop, hard fault, exploitable vulnerability, service down |
| S2 Major | A core function does not work, or works only with a lot of manual effort | Telemetry stops, partial data loss |
| S3 Moderate | A secondary function fails, and a workaround exists | Wrong LED sequence, a report that does not generate |
| S4 Minor | Little or no effect on operation | Typing error in a log message, misaligned text in a web page |

[[CAPTION:Table]] Priority levels.

| Priority | Meaning | How it ships |
|----------|---------|--------------|
| P1 Immediate | Work starts now and continues until it is fixed | A hotfix release |
| P2 High | Fixed in the current sprint | The next planned release |
| P3 Medium | Planned into an upcoming sprint | A normal release |
| P4 Low | Fixed when someone is working in that code anyway | A future release |

## Closing a defect

- [ ] **DR-1 You understand the area you changed,** not just the line that failed. The [debugging checklist](debugging-checklist.md) helps here.
- [ ] **DR-2 The defect is classified,** as a requirement, design, architecture, integration or coding defect. The class shows where the process let it through.
- [ ] **DR-3 The report says what was wrong** with the old behaviour.
- [ ] **DR-4 The report says what changed** to fix it.
- [ ] **DR-5 The report lists the tests** that show the fix works, including the new regression test.
- [ ] **DR-6 Commits and the pull request reference the defect,** so the fix can be traced both ways.
- [ ] **DR-7 S1 and S2 defects in the field get a [postmortem](postmortem.md).**
