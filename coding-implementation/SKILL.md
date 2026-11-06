---
name: coding-implementation
description: Deliver software from a raw idea, a thinking handoff, an agreed spec, or a bounded coding work item. Clarify consequential choices, define acceptance, coordinate implementation, and independently verify real behavior. Use for coding projects and software changes; keep planning-only requests within planning and leave non-coding production to suitable capabilities.
---

# Coding Implementation

Carry a finite software task from its current state to the agreed, verified result. Enter where useful; the user does not invoke a separate skill for each stage. No upstream framework, tracker, worktree system, or companion skill is required.

## Start at the right stage

Establish what is settled, what action the user authorized, and whether you own the project or one delegated item. Reuse accessible context and inspect the relevant repository and project instructions. Do not restart discovery for an adequate existing spec or repeat scrutiny already done.

| Current need | Read and apply |
| --- | --- |
| A material question could change the goal, behavior, scope, or tradeoff; acceptance or work boundaries are missing | [Specify and split](references/specify.md) |
| An agreed spec or bounded item is ready for authorized implementation; work needs dispatch, integration, or resumption | [Build and coordinate](references/coordinate.md) |
| An item or integrated result is ready for independent checks; findings need adjudication or follow-up | [Verify and close](references/verify.md) |

Read a stage reference before doing that stage, including when entering directly as a builder or verifier. A coordinator also reads verification guidance before commissioning a verifier. Follow the same entry rules for a direct request and a handoff.

When material thinking remains, use Thought Partner if available and suitable, honoring an explicit skill choice. Discover capabilities through the current host, load the chosen instructions, and return the thinking result to this workflow. If it is unavailable, do the necessary clarification here. Do not require installation or assume a skill name establishes its availability or ownership.

## Preserve authority and boundaries

- Carry the authorized action, scope, limits, and pending consequential decisions across every handoff. Preserve the relevant user instruction or a concise accessible reference. An agreed direction or permission to draft a spec does not by itself authorize building. Earlier execution authorization remains valid; do not add a new approval ritual.
- The spec is the completion contract. Make proposed approaches and consequential tradeoffs visible before treating them as settled. Keep questions for decisions that matter; inspect code and facts directly when they can resolve uncertainty.
- Routine implementation choices, repairs to meet the spec, and verification within an item remain delegated. A spec redesign or implementation redesign beyond that item's bounds returns to the user with evidence, the smallest viable options, and a recommendation. Continue unaffected authorized work.
- Additional abstractions, infrastructure, dependencies, and refactors need an agreed requirement, a relevant regression, or a concrete consequential failure under intended use. Future scale, style preferences, and “best practice” alone do not expand scope. Leave unrelated cleanup and possible future improvements out of the active work; do not create a backlog or improve the workflow unless requested.
- Use only the access and external actions already authorized. Implementation and testing do not grant permission to install, publish, deploy, send, or change live systems beyond that scope.

## Own the finite result

Once the spec is agreed and execution is authorized, the coordinating chat progresses through the finite work list, manages dependencies and findings, integrates accepted items, and independently verifies the assembled user path. Dispatch fresh builders and separate fresh verifiers when the host supports them. A delegated builder completes its bounded item and returns evidence to the coordinator rather than taking over unrelated work.

Use a short spec and one item for a small change when sufficient. Keep only enough state to resume and identify the exact result checked. Do not introduce scheduling, an intake funnel, a registry, a dashboard, or a new agent runtime to run the workflow.

Completion requires passing the required acceptance checks on the current result and no substantiated serious concerns. Builder tests, an empty review, mocks, and structural validation alone do not establish the actual behavior they leave unexercised. Unavailable required evidence or independent verification stays outstanding; repeated attempts without useful progress require a concrete blocker report, not a success claim or an endless loop. Follow [verification and closure](references/verify.md), report the evidence and limitations, then stop when the agreed work is complete.
