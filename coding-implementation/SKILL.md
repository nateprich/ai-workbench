---
name: coding-implementation
description: Deliver software from a raw idea, a thinking handoff, an agreed spec, or a bounded coding work item. Clarify consequential choices, define acceptance, coordinate implementation, and independently verify real behavior. Use for coding projects and software changes; keep planning-only requests within planning and leave non-coding production to suitable capabilities.
---

# Coding Implementation

Carry a finite software task from its current state to the agreed, verified result. Use one preparation boundary: **Needs definition → Ready → Building → Verifying → Done**. Shaping, specification, and splitting happen within preparation; there is no separate Shaped checkpoint or approval between them. No upstream framework, tracker service, worktree system, or companion skill is required.

## Start at the right stage

Establish what is settled, what action the user authorized, and whether you own the project or one delegated item. Reuse accessible context and project instructions, including saved tracker setup. Do not restart discovery for an adequate spec, repeat settled questions, or rediscover setup for each item.

| Current need | Read and apply |
| --- | --- |
| Durable tracking is needed and configuration is missing or concretely stale | [Project setup](references/setup.md), using the GitHub or local template |
| Consequential behavior, acceptance, coverage, or work boundaries remain undefined | [Prepare the work](references/specify.md) |
| Work needs selection, implementation, integration, state transitions, or resumption | [Build and coordinate](references/coordinate.md) |
| An item or integrated result is ready for independent checks; findings need adjudication or follow-up | [Verify and close](references/verify.md) |

Read a stage reference before doing that stage, including when entering directly as a builder or verifier. A coordinator also reads verification guidance before commissioning a verifier. Follow the same entry rules for a direct request and a handoff.

When material thinking remains, use Thought Partner if available and suitable, honoring an explicit skill choice. Discover capabilities through the current host, load the chosen instructions, and return the thinking result to this workflow. If it is unavailable, do the necessary clarification here. Do not require installation or assume a skill name establishes its availability or ownership.

## Preserve authority and boundaries

- Carry the authorized action, scope, limits, and pending consequential decisions across every handoff. Preserve the relevant user instruction or a concise accessible reference. An agreed direction or permission to draft a spec does not by itself authorize building. Earlier execution authorization remains valid; do not add a new approval ritual.
- The authoritative spec is the completion contract; item briefs cannot silently override it. Make consequential tradeoffs visible before treating them as settled. Inspect code and facts when they can resolve uncertainty.
- Routine implementation choices, repairs to meet the spec, and verification within an item remain delegated. A spec redesign or implementation redesign beyond that item's bounds returns to the user with evidence, the smallest viable options, and a recommendation. Continue unaffected authorized work.
- Additional abstractions, infrastructure, dependencies, and refactors need an agreed requirement, a relevant regression, or a concrete consequential failure under intended use. Future scale, style preferences, and “best practice” alone do not expand scope. Leave unrelated cleanup and possible future improvements out of the active work; do not create a backlog or improve the workflow unless requested.
- Use only the access and external actions already authorized. Implementation and testing do not grant permission to install, publish, deploy, send, or change live systems beyond that scope.

## Own the finite result

Once preparation and execution authority are sufficient, the coordinator selects eligible items, manages dependencies and findings, integrates accepted results, and independently verifies the assembled user path. The coordinator owns state transitions and acceptance; builders return bounded results and evidence. Use fresh builders and separate fresh verifiers when supported and authorized.

Use a short spec and one work record for a small change. Larger work needs coverage of every agreed outcome, while later items may remain Needs definition. Parent progress is derived from that coverage and accepted results, not merely the state of existing tickets. Do not introduce portfolio scheduling, autonomous intake, dashboards, a new runtime, or automatic workflow improvement.

Completion requires accepted coverage of the spec and required checks on the current artifact and applicable contract, with no substantiated serious concerns. Builder tests, empty reviews, mocks, and structural checks cannot establish an unobserved required effect. Missing required evidence stays outstanding. Follow [verification and closure](references/verify.md), report evidence and limitations, then stop when the finite work is complete.
