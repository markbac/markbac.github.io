---
title: Experiment record
---

# Experiment record

Use this template for a spike, a prototype or a piece of research. An experiment has a question, a time-box and an end. It finishes when you can answer the question or the time runs out, and either way the record says what you found.

Record negative results too. "We tried it and it does not work, for these reasons" saves the next person the same two weeks.

## Template

```markdown
---
id: EXP-0000
title: Short title
status: running          # running | stopped | extended | graduated
owner:
started: YYYY-MM-DD
time-box: YYYY-MM-DD     # the date it stops unless someone extends it
maturity: R0             # R0 idea | R1 feasible | R2 prototype | R3 ready for a product
---

# EXP-0000: Short title

## Question

What do we want to find out, and what decision depends on the answer?

## Time-box

The end date and the effort limit.

## Method

How we will answer the question, and what result would count as
success or failure. Decide this before you start.

## Setup

Hardware, software versions, configuration and where the data is kept.

## Results

What happened, with the data. Include the negative and the unexpected.

## Conclusion

The answer to the question, and how confident we are in it.

## Decision and next step

Stop, extend (and why), or graduate into a product. If it graduates,
link the requirement, ADR or RFC that follows.

## Reproduction

The commands and scripts that repeat the experiment.
```
