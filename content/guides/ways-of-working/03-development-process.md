---
title: The development process, end to end
---

# The development process, end to end

This document describes an end-to-end process flow for a software development team.  
It covers **requirements definition**, **feature creation**, **sprint development**, **code quality gates**, **test & verification**, and **system integration testing** — with **feedback loops at every stage**.

---

## Process Overview

The overall process follows these steps:
1. **Requirements** are created by the Product Manager and reviewed.
2. **Features** are defined by the Architect, reviewed by the team, and accepted.
3. The software team refines features into **user stories**.
4. Delivery happens in **3-week sprints** using feature branches.
5. Before merging a feature branch:
   - All stories must be complete.
   - The build must compile and pass unit tests and static analysis.
   - Code review must be approved.
6. Once merged, a **build is created for T&V**.
7. **Test & Verification (T&V)** and **System Integration Testing (SIT)** provide structured feedback loops.
8. Rework can happen **at any stage** based on review findings, bugs, or changes in upstream requirements.

---

## High-level Flow (Mermaid)

```mermaid
flowchart TD
    PM[Product Manager creates or updates requirements] --> RvwReq[Requirements review]
    RvwReq -->|Accepted| Arch[Architect defines features]
    RvwReq -->|Changes needed| PM

    Arch --> RvwFeat[Feature refinement & acceptance]
    RvwFeat -->|Accepted| Refine[SW team refines features into user stories]
    RvwFeat -->|Rework| Arch

    Refine --> Sprint["Sprint cycles (3 weeks)"]
    Sprint --> Dev[Develop on feature branches]
    Dev --> Gate{Feature merge gate\n- All stories complete\n- Build compiles\n- Tests pass\n- Static analysis clean\n- Code review OK}
    Gate -->|Pass| Merge[Merge to main]
    Gate -->|Fail| Rework1[Rework dev or tests]
    Merge --> Build[Create build for Test & Verification]
    Build --> TnV[Test & Verification]
    TnV -->|Bugs found| Rework2[Defect fix & retest]
    TnV -->|Pass| SIT[System Integration Testing]
    SIT -->|Bugs found| Rework3[Fix SIT issues & retest]
    SIT -->|Pass| Done[Feature accepted / ready for release]

    Rework1 --> Sprint
    Rework2 --> Sprint
    Rework3 --> Sprint
```

---

## Responsibilities & Hand-offs (PlantUML Activity)

```mermaid
flowchart TD

  %% ===== Nodes =====
  pm_create["PM: Create or update requirements"]
  pm_submit["PM: Submit for review"]

  arch_review["Architect: Review requirements"]
  arch_clear{"Architect: Requirements clear & acceptable?"}
  pm_revise["PM: Revise requirements"]
  pm_signoff["PM: Sign-off requirements"]

  arch_define["Architect: Define features from signed-off requirements"]
  pm_feat_review["PM: Review feature"]
  sw_feat_review["SW Team: Review feature (Developers)"]
  feat_ok{"SW Team: Feature accepted?"}
  arch_rework_feat["Architect: Rework feature definition"]

  dev_create_us["Developer: Create user stories for feature"]
  sw_sprint["SW Team: Sprint planning (3-week)"]
  sw_execute["SW Team: Execute sprint(s) to complete user stories"]
  dev_develop["Developer: Develop on feature branches"]
  dev_local_tests["Developer: Run unit tests + static analysis"]
  ci_build["CI: Build & automated checks"]
  stories_ci{"CI: Stories complete & CI pass?"}
  dev_fix_ci["Developer: Rework to fix CI failures or incomplete stories"]

  rev_review["Reviewer: Code review"]
  approved{"Reviewer: Approved?"}
  dev_addr_comments["Developer: Address review comments"]

  ci_final["CI: Final CI build & checks"]
  ci_pass{"CI: CI passes?"}
  dev_merge["Developer: Merge to main"]
  ci_tv_build["CI: Create T&V build"]

  tv_run["T&V: Execute Test & Verification"]
  tv_bugs{"T&V: Bugs found?"}
  sw_log_defects["SW Team: Log defects"]
  dev_fix_tv["Developer: Fix defects from T&V"]

  sit_run["SIT: System Integration Testing"]
  sit_issues{"SIT: SIT issues found?"}
  dev_fix_sit["Developer: Fix SIT issues"]

  rel_ready["Release Manager: Feature accepted / ready for release"]
  arch_close_feat["Architect: Mark Feature CLOSED"]
  arch_req_all_closed{"Architect: All Features for the Requirement CLOSED?"}
  arch_close_req["Architect: Mark Requirement CLOSED"]

  %% ===== Flow =====
  pm_create --> pm_submit --> arch_review
  arch_review --> arch_clear
  arch_clear -- "no" --> pm_revise --> arch_review
  arch_clear -- "yes" --> pm_signoff --> arch_define

  arch_define --> pm_feat_review --> sw_feat_review --> feat_ok
  feat_ok -- "no" --> arch_rework_feat --> pm_feat_review
  feat_ok -- "yes" --> dev_create_us --> sw_sprint --> sw_execute

  sw_execute --> dev_develop --> dev_local_tests --> ci_build --> stories_ci
  stories_ci -- "no" --> dev_fix_ci --> dev_develop
  stories_ci -- "yes" --> rev_review --> approved
  approved -- "no" --> dev_addr_comments --> rev_review
  approved -- "yes" --> ci_final --> ci_pass
  ci_pass -- "no" --> dev_fix_ci --> dev_develop
  ci_pass -- "yes" --> dev_merge --> ci_tv_build --> tv_run --> tv_bugs

  tv_bugs -- "yes" --> sw_log_defects --> dev_fix_tv --> ci_build --> tv_run
  tv_bugs -- "no" --> sit_run --> sit_issues
  sit_issues -- "yes" --> dev_fix_sit --> ci_build --> sit_run
  sit_issues -- "no" --> rel_ready --> arch_close_feat --> arch_req_all_closed
  arch_req_all_closed -- "yes" --> arch_close_req
  arch_req_all_closed -- "no" --> arch_define


```

---

## Feature & Requirement Lifecycle (PlantUML State)

```plantuml
@startuml
[*] --> ReqDraft : Requirement created
ReqDraft --> ReqReview : In review
ReqReview --> ReqUpdate : Changes requested
ReqUpdate --> ReqReview
ReqReview --> ReqAccepted : Approved

ReqAccepted --> FeatureDraft : Feature defined
FeatureDraft --> FeatureReview : In review
FeatureReview --> FeatureUpdate : Changes requested
FeatureUpdate --> FeatureReview
FeatureReview --> FeatureAccepted : Approved

FeatureAccepted --> InRefinement : User stories created
InRefinement --> InSprint : Committed to sprint
InSprint --> DevComplete : Stories implemented
DevComplete --> ChecksGreen : Build+Tests+Static OK
ChecksGreen --> InReview : Code review
InReview --> ChangesRequested : Reviewer requests changes
ChangesRequested --> InSprint
InReview --> ReadyToMerge : Review approved
ReadyToMerge --> Merged
Merged --> ForTnV : Build for Test & Verification
ForTnV --> TnVFailed : Bugs found
TnVFailed --> InSprint
ForTnV --> ForSIT : T&V passed
ForSIT --> SITFailed : Integration issues found
SITFailed --> InSprint
ForSIT --> Done : Feature accepted
Done --> [*]
@enduml
```

---

## CI, T&V and SIT Feedback Loops (Mermaid Sequence)

```mermaid
sequenceDiagram
    participant PM as Product Manager
    participant Arch as Architect
    participant Dev as Developer
    participant Rev as Reviewer
    participant CI as CI Pipeline
    participant TnV as Test & Verification
    participant SIT as System Integration
    participant RM as Release Manager

    %% --- Requirement loop ---
    loop Until all Features for Requirement are closed
        PM->>Arch: Submit requirement for review
        Arch-->>PM: Approve & sign-off

        %% --- Multiple features per requirement ---
        par One or more Features
            Arch->>Arch: Define Feature
            Arch->>Dev: Provide feature spec
            Arch->>Arch: T-shirt size feature

            %% --- User story loop for this feature ---
            loop Until all User Stories for Feature are complete
                Dev->>Dev: Create user story
                Dev->>Arch: Submit for review
                Arch-->>Dev: Approve or request changes
                Dev->>Dev: Implement & test
                Dev->>CI: Push for CI
                CI-->>Dev: Results (pass/fail)
            end

            Dev->>Rev: Submit Feature PR for review
            loop Until approved
                Rev-->>Dev: Review comments / fixes
            end
            Rev-->>CI: Approve → trigger final CI build
            CI-->>TnV: Build for T&V
            TnV-->>TnV: Execute verification
            alt Bugs found
                TnV-->>Dev: Defect tickets
                loop Until passed
                    Dev->>CI: Fix & rebuild
                    CI->>TnV: Retest
                end
            end
            TnV-->>SIT: Promote to SIT
            SIT-->>SIT: Integration testing
            alt SIT issues found
                SIT-->>Dev: SIT defects
                loop Until SIT passes
                    Dev->>CI: Fix & rebuild
                    CI->>SIT: Retest
                end
            end
            SIT-->>RM: Feature accepted
            Arch->>Arch: Mark Feature closed
        and Another feature (parallel)
            Arch->>Arch: Define additional Feature
            note right of Arch: Same process repeats for each Feature<br>until all are complete
        end
    end

    %% --- Requirement closure ---
    Arch->>Arch: All Features closed → Requirement closed ✅

```

```mermaid
sequenceDiagram
    participant PM as Product Manager
    participant Arch as Architect
    participant Dev as Developer
    participant Rev as Reviewer
    participant VCS as Git Host
    participant CI as CI Pipeline
    participant TnV as Test & Verification
    participant SIT as System Integration
    participant RM as Release Manager

    %% Requirements loop
    loop Until requirement is accepted
        PM->>Arch: Submit requirement for review
        alt Needs changes
            Arch-->>PM: Feedback / requested changes
            PM->>Arch: Revise and resubmit
        else Acceptable
            Arch-->>PM: Recommend sign-off
        end
    end
    PM->>PM: Requirement SIGN-OFF

    %% Feature definition & review loop
    Arch->>Arch: Define features from signed-off requirement
    loop Feature review until accepted
      PM-->>Arch: PM feature review feedback
      Dev-->>Arch: Dev feasibility feedback
      alt Rework needed
        Arch->>Arch: Rework feature definition
      else Accepted
        Arch-->>Dev: Approved feature for implementation
      end
    end

    %% Story creation and sprinting (drop-in)
    Arch->>Arch: T-shirt size features
    Dev->>Dev: Create user stories for feature

    %% Architect review of user stories
    loop Until user stories accepted
      Dev->>Arch: Submit user stories for review
      alt Changes required
        Arch-->>Dev: Feedback / requested changes
        Dev->>Dev: Update user stories
      else Accepted
        Arch-->>Dev: Approve user stories
      end
    end

    Dev->>Dev: Size user stories (days)

    %% 3-week sprint loop
    loop 3-week sprints until all user stories complete
      Dev->>Dev: Sprint planning (select stories)
      loop During sprint
        Dev->>Dev: Design and document
        Dev->>Dev: Implement design
        Dev->>Dev: Create and run unit tests
        Dev->>VCS: Push commits to feature branch
        VCS-->>CI: Trigger CI
        CI->>CI: Compile + unit tests + static analysis
        CI-->>Dev: Results (pass/fail)
        alt CI fails
          Dev->>Dev: Fix & re-push
        end
      end
      Dev->>Dev: Sprint review & close
    end

    %% Review + merge gates (after all user stories complete for the feature)
    Dev->>Dev: All user stories for feature complete ✅

    Dev->>VCS: Open pull request
    VCS-->>Rev: Notify for code review

    %% Review loop
    loop Until approved
      Rev-->>Dev: Review comments / requests
      Dev->>VCS: Address comments (push updates)
    end

    Rev-->>VCS: Approve
    VCS-->>CI: Final pre-merge checks

    %% Pre-merge CI gate
    alt Checks pass
      Dev->>VCS: Merge to main
    else Checks fail
      CI-->>Dev: Fix required
      Dev->>VCS: Push fixes
      VCS-->>CI: Re-run checks
      Dev->>VCS: Merge to main
    end
    %% T&V loop
    VCS-->>CI: Create T&V build
    CI->>TnV: Deliver build
    TnV-->>TnV: Execute tests
    alt Bugs found
      TnV-->>Dev: Defect tickets
      loop Until T&V passes
        Dev->>VCS: Fix & push
        VCS-->>CI: Rebuild
        CI->>TnV: Retest
      end
    end

    %% SIT loop
    TnV-->>SIT: Promote build to SIT
    SIT-->>SIT: Integration testing
    alt SIT issues found
      SIT-->>Dev: SIT defects
      loop Until SIT passes
        Dev->>VCS: Fix & push
        VCS-->>CI: Rebuild
        CI->>SIT: Retest
      end
    end

    %% Acceptance and closure
    SIT-->>RM: Feature accepted / ready for release
    Arch->>Arch: Close Feature
    Arch->>Arch: If all features for requirement closed ⇒ Close Requirement

```

---

## Commentary & Rationale

- **Feedback loops** are intentionally present in *every phase*, not just testing.  
- **Requirements & features** have review cycles to ensure downstream teams work with clarity and stable inputs.  
- **Feature gates** before merge protect `main` and keep builds stable.
- **T&V** and **SIT** are treated as structured gates, not chaotic bug hunts.
- **Rework is planned**, not a surprise — stories or tasks can be created from findings and re-run through the process.
- This model aligns well with ADO/Jira workflows, CI/CD pipelines, and regulated development environments.

---

## Suggested Practice

| Stage | Trigger | Feedback Loop |
|-------|---------|---------------|
| Requirement | Ambiguity, scope, missing acceptance | Back to PM for revision |
| Feature | Technical feasibility or unclear scope | Back to Architect |
| Dev | Build, static analysis, unit test failure | Developer fixes before merge |
| Code Review | Review comments | Developer updates |
| T&V | Defects found | Rework through sprint |
| SIT | Integration issues | Rework through sprint |

---

**Author:** Internal Engineering Team  
**Version:** 1.0  
**Date:** October 2025


```mermaid
sequenceDiagram
    participant PM as Product Manager
    participant Arch as Architect
    participant Dev as Developer
    participant Rev as Reviewer
    participant VCS as Git Host
    participant CI as CI Pipeline
    participant TnV as Test & Verification
    participant SIT as System Integration
    participant RM as Release Manager

    %% === Requirement lifecycle ===
    loop Until all Features for Requirement are closed
        PM->>Arch: Submit requirement for review
        loop Until requirement accepted
            alt Needs changes
                Arch-->>PM: Feedback / requested changes
                PM->>Arch: Revise and resubmit
            else Acceptable
                Arch-->>PM: Recommend sign-off
            end
        end
        PM->>PM: Requirement SIGN-OFF ✅

        %% === Feature lifecycle ===
        par One or more Features
            Arch->>Arch: Define Feature
            Arch->>Arch: T-shirt size Feature
            Arch->>Dev: Provide feature specification

            %% === User story development ===
            loop Until all User Stories for Feature are complete
                par Parallel user stories
                    Dev->>Dev: Create user story
                    Dev->>Arch: Submit user story for review
                    alt Changes required
                        Arch-->>Dev: Feedback / rework
                        Dev->>Arch: Resubmit user story
                    else Accepted
                        Arch-->>Dev: Approve user story
                    end
                    Dev->>Dev: Implement story (develop, unit test, static analysis)
                    Dev->>VCS: Push to feature branch
                    VCS-->>CI: Trigger CI build & checks
                    CI->>CI: Compile + run unit tests + static analysis
                    CI-->>Dev: Results (pass/fail)
                    alt CI fails
                        Dev->>Dev: Fix and re-push
                    else Pass
                        Dev-->>Rev: Ready for PR inclusion
                    end
                and Another user story
                    note right of Dev: Stories can be implemented<br>in parallel during sprints
                end
            end

            Dev->>Dev: All user stories for feature complete ✅

            %% === Review and merge ===
            Dev->>VCS: Open pull request (feature)
            VCS-->>Rev: Notify for code review
            loop Until approved
                Rev-->>Dev: Review comments / changes
                Dev->>Rev: Push updates
            end
            Rev-->>CI: Approve → trigger pre-merge CI checks
            alt Checks pass
                Dev->>VCS: Merge to main
            else Checks fail
                CI-->>Dev: Fix required → re-push
                Dev->>VCS: Push fixes
                VCS-->>CI: Re-run checks
                Dev->>VCS: Merge to main
            end

            %% === Test & Verification stage ===
            VCS-->>CI: Create T&V build
            CI->>TnV: Deliver build for testing
            TnV-->>TnV: Execute T&V tests
            alt Bugs found
                TnV-->>Dev: Raise defect tickets
                loop Until T&V passes
                    Dev->>Dev: Diagnose and implement fix
                    Dev->>VCS: Push fix to feature branch
                    VCS-->>CI: Trigger CI build & checks
                    CI->>CI: Compile + unit tests + static analysis
                    CI-->>Dev: Results (pass/fail)
                    alt CI fails
                        Dev->>Dev: Correct issue & re-push
                    else Pass
                        Dev->>Rev: Request review for fix
                        loop Until approved
                            Rev-->>Dev: Review comments / changes
                            Dev->>Rev: Push updates
                        end
                        Rev-->>CI: Approve → trigger pre-merge checks
                        CI-->>Dev: Verify checks passed
                        Dev->>VCS: Merge fix to main
                    end
                    VCS-->>CI: Rebuild main
                    CI->>TnV: Deliver build for retest
                    TnV-->>TnV: Execute regression tests
                end
            end

            %% === SIT stage ===
            TnV-->>SIT: Promote build to SIT
            SIT-->>SIT: Execute integration testing
            alt SIT issues found
                SIT-->>Dev: Raise SIT defect tickets
                loop Until SIT passes
                    Dev->>Dev: Diagnose and implement fix
                    Dev->>VCS: Push fix to feature branch
                    VCS-->>CI: Trigger CI build & checks
                    CI->>CI: Compile + unit tests + static analysis
                    CI-->>Dev: Results (pass/fail)
                    alt CI fails
                        Dev->>Dev: Correct issue & re-push
                    else Pass
                        Dev->>Rev: Request review for fix
                        loop Until approved
                            Rev-->>Dev: Review comments / changes
                            Dev->>Rev: Push updates
                        end
                        Rev-->>CI: Approve → trigger pre-merge checks
                        CI-->>Dev: Verify checks passed
                        Dev->>VCS: Merge fix to main
                    end
                    VCS-->>CI: Rebuild main
                    CI->>SIT: Deliver build for retest
                    SIT-->>SIT: Execute regression tests
                end
            end

            SIT-->>RM: Feature accepted / ready for release
            Arch->>Arch: Mark Feature closed
        and Another feature
            note right of Arch: Requirements may have<br>multiple features progressing<br>in parallel
        end
    end

    %% === Requirement closure ===
    Arch->>Arch: All Features closed → Requirement closed ✅

```
