# Build and coordinate

The coordinator advances the finite agreed work within existing authority. A delegated builder implements its bounded item and reports to the coordinator. Load the saved [tracker configuration](setup.md) on entry and pass its relevant instructions or an accessible pointer to delegates; reuse it throughout the run. Read live status, dependency results, and acceptance evidence whenever they affect action.

## Record the stage and the next action

The coordinator owns transitions; builder success is not independent acceptance. Keep one stage for each bounded item:

| Stage | Meaning and next action |
| --- | --- |
| Needs definition | Consequential preparation remains: clarify behavior, recover context, refine the spec, split work, or repair an unusable handoff. |
| Ready | Contract, bounds, acceptance, and dependencies are understood; no consequential definition decision remains. Select for implementation when eligible. |
| Building | Authorized implementation is underway, interrupted, or receiving bounded repairs. Preserve progress and the current artifact. |
| Verifying | A result is available for independent acceptance or verification is underway. Select checks, execute them, and adjudicate findings. |
| Done | Required acceptance passed for the identified artifact and applicable contract, with no substantiated serious concerns outstanding. |

Normal progression is Needs definition → Ready → Building → Verifying → Done. An adequate supplied item may enter Ready; an existing implementation may enter Verifying. Entry routes do not waive unmet obligations or grant authority.

Record waiting separately: blocker, affected work, and condition or action that clears it. A dependency, unanswered decision, missing access, and unavailable verification require different remedies. Cancellation and deferral preserve their reason using existing tracker dispositions and never count as Done. Parent summaries are derived from outcome coverage, child results, unresolved work, and final verification, not a second copy of item stages.

## Select the right assignment

**Initial build selection requires all of:** Ready, no active blocker, accepted prerequisite results available to the builder, appropriate workspace/write ownership, and execution authority. Inspect the required result and acceptance evidence; a closed or cancelled prerequisite issue does not prove its result exists.

Resume interrupted implementation or assign bounded repairs while the item is Building. Assign independent verification while it is Verifying. Neither requires an artificial return to Ready. For every assignment, check the relevant current contract/artifact, blockers, prerequisite results, workspace/write ownership, and authority.

Repair missing commands or pointers in context without automatically restarting preparation. A materially incomplete contract returns the affected item to Needs definition. A repair needed to meet the existing contract returns Verifying to Building; missing or invalidated evidence leaves the relevant work in Verifying. Record each reason. Reopen Done only when a relevant artifact/contract change or new evidence invalidates its acceptance. Reassess affected dependent readiness; preserve valid unrelated work.

## Dispatch, build, verify, and integrate

1. Give fresh builders the [execution brief](specify.md#give-each-item-an-executable-brief), accessible project references, accepted prerequisites, and clear write ownership. For a substantial project with a new or uncertain execution path, take the first coherent slice through build, verification, and integration before broad dispatch when this tests handoff or integration assumptions. This is ordinary project work, not a pilot state or throwaway scaffolding.
2. Parallelize genuine independent work where useful; sequence or isolate shared-state edits. Worktrees are optional. If delegation is unavailable, the coordinator may build within the same bounds but cannot call self-checks independent verification.
3. Builders inspect relevant code and affected contracts, implement, and run proportionate direct checks and required project checks. Durable regression tests are useful when they expose meaningful failures; strict TDD is not required. Return changes, artifact/spec identities, observed results, routine choices, and limitations. Preserve enough progress for a fresh agent to resume interruptions.
4. Move the returned result to Verifying and commission a fresh separate verifier using [Verify and close](verify.md). It selects checks from the contract before relying on builder tests or advocacy. Verifiers report; builders or the coordinator own product repairs.
5. Adjudicate findings against requirements and evidence. Arrange bounded repairs and focused independent follow-up; keep unverified work and blockers visible. Accept only when required checks pass on the current result and no substantiated serious concerns remain. Make the accepted result available in the form dependents need.
6. Integrate accepted results and independently verify the assembled user path through its required observable effect. For one item, one independent pass can cover item and final levels on the unchanged final artifact. Otherwise, reuse valid evidence and test the integration and consequential affected behavior.

Store checkpoints, transitions and reasons, prerequisite acceptance links, artifact and contract identities, and evidence in the configured work record. Use the exact destination and saved operations. Read back uncertain or partial tracker writes before retrying; unresolved coordination writes remain outstanding even if product checks pass. Do not create a shadow tracker when access fails.

## Handle boundaries and completion

A context omission calls for context repair. A technical failure calls for an evidence-led fix or focused investigation. A product/scope decision calls for the user. Redesign inside item bounds may proceed if it preserves the contract; proposed spec redesign or implementation redesign beyond those bounds returns to the user with evidence, smallest viable options, and a recommendation. Continue unaffected authorized work.

Do not retry an unchanged failed approach without useful new information. Repeated attempts without progress or a consequential disagreement evidence cannot settle require a concrete blocker report. Missing tools, access, independence, or final-effect evidence remain outstanding; do not relax acceptance or create new infrastructure to conceal the limit.

Project completion requires accepted coverage of every agreed outcome and independent verification of the integrated result, not merely all existing tickets being Done. Approved scope changes must be explicit; deferred required outcomes remain outstanding. Both artifact and approved spec/interface changes can invalidate acceptance, even when only one changes. Recheck only what is materially affected, under the [closure rules](verify.md#fix-recheck-and-stop). Report delivered behavior, evidence, and limitations, including unfinished tracker operations; stop when the finite agreed work is complete.
