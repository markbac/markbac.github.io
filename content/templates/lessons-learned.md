---
title: Lessons learned
---

# Lessons learned

Use this template at the end of a project or phase to record what went well, what did not, and what the team will do differently. For a single incident, use the [postmortem](postmortem.md) instead.

## Template

```markdown
---
title: Lessons Learned - [Project/Initiative Name or Phase]
status: Draft / Reviewed / Finalised
date: YYYY-MM-DD (Date of Session)
project_start_date: YYYY-MM-DD
project_end_date: YYYY-MM-DD (or Current Phase End Date)
author: [Name or Role of Facilitator]
participants: [List of key participants/stakeholders]
version: 1.0
---

# Lessons Learned: [Project/Initiative Name or Phase]

This document captures the lessons learned from the [Project/Initiative Name or Phase]. The purpose of this review is to reflect on our experiences, identify what went well and what could be improved, and formulate actionable recommendations to enhance our processes, practices, and outcomes for future projects.

---

## 1. Introduction

### 1.1 Purpose

The purpose of this Lessons Learned document is to:
* Systematically collect knowledge gained from our experiences.
* Identify successful practices to be repeated and institutionalized.
* Pinpoint challenges and problems, and understand their root causes.
* Develop actionable recommendations for continuous improvement.
* Share insights across teams and the organization.

### 1.2 Context of Review

[Briefly describe the project, phase, or initiative being reviewed. What was its scope, objectives, and timeframe?]

### 1.3 Participants

[List the individuals or groups who participated in the Lessons Learned session(s).]

## 2. What Went Well? (Successes & Strengths)

[Identify and describe the aspects of the project/initiative that were successful, effective, or positive. Why were they successful?]

* **[Success 1]:** [Description, e.g., "Our cross-functional team collaboration was excellent."]
    * *Why it worked:* [e.g., "Daily syncs fostered strong communication and quick problem-solving."]
* **[Success 2]:** [Description, e.g., "Early stakeholder engagement led to clear requirements."]
    * *Why it worked:* [e.g., "Regular review sessions with product owners prevented scope creep."]
* **[Success 3]:** [Description, e.g., "The automated testing pipeline significantly reduced regression bugs."]
    * *Why it worked:* [e.g., "Investment in robust CI/CD paid off by catching issues early."]

## 3. What Could Be Improved? (Challenges, Issues & Weaknesses)

[Identify and describe the aspects that presented challenges, caused issues, or could have been handled better. What were the root causes of these difficulties?]

* **[Challenge 1]:** [Description, e.g., "Hardware delays impacted software integration schedule."]
    * *Root Cause(s):* [e.g., "Underestimated supplier lead times, lack of early prototyping."]
* **[Challenge 2]:** [Description, e.g., "Requirements changed frequently in the later stages."]
    * *Root Cause(s):* [e.g., "Insufficient initial discovery, lack of clear product vision."]
* **[Challenge 3]:** [Description, e.g., "Technical debt accumulated in the authentication module."]
    * *Root Cause(s):* [e.g., "Prioritised speed over quality in early sprints, no dedicated tech debt budget."]

## 4. What Did We Learn? (Key Insights)

[Based on the successes and challenges, what are the overarching insights or new understandings gained? These are the "lessons" themselves.]

* **[Lesson 1]:** [e.g., "Proactive engagement with external suppliers is critical for hardware-dependent projects."]
* **[Lesson 2]:** [e.g., "Robust validation of initial assumptions is key to minimizing late-stage requirement changes."]
* **[Lesson 3]:** [e.g., "Allocating regular, small amounts of time for technical debt remediation is more effective than large, infrequent efforts."]
* **[Lesson 4]:** [e.g., "The benefit of 'Docs as Code' for Living Design Documents significantly outweighs the initial setup effort."]

## 5. Recommendations & Action Items

[Based on the lessons learned, what specific, actionable recommendations and tasks should be implemented for future projects or processes? Assign owners and target dates.]

| Action Item ID | Description | Recommendation Type | Owner | Target Date | Status |
|----------------|-------------|---------------------|-------|-------------|--------|
| **LL-AI-001** | Establish a 'supplier risk assessment' checklist for new hardware projects. | Process Improvement | John Smith | YYYY-MM-DD | Open   |
| **LL-AI-002** | Incorporate a dedicated 'discovery phase' for new features before committing to development. | Process Improvement | Jane Doe | YYYY-MM-DD | Open   |
| **LL-AI-003** | Allocate 15% of sprint capacity to technical debt remediation tasks. | Policy Change | Alice Brown | YYYY-MM-DD | Open   |
| **LL-AI-004** | Develop a standard template for PoC reports to capture technical findings. | Documentation | Bob White | YYYY-MM-DD | Open   |

* **Recommendation Types:** (e.g., Process Improvement, Policy Change, Tooling Update, Training/Skill Development, Documentation, Architectural Guidance)

## 6. Communication & Sharing Plan

[How will these lessons learned be shared with relevant teams and stakeholders to ensure broader adoption of recommendations?]

* [e.g., "Present key findings in next All-Hands meeting."]
* [e.g., "Share document link in relevant Slack/Teams channels."]
* [e.g., "Integrate recommendations into updated 'Ways of Working' guidelines."]
* [e.g., "Conduct a focused workshop with other project leads on specific challenges."]

## 7. References

[List any relevant project documents, incident reports, or data used during this review.]
```
