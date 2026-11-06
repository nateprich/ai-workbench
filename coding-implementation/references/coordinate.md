# Build and coordinate

An agreed spec plus execution authority starts the finite delivery workflow. Use an existing adequate work list; add only the decomposition needed for the agreed outcome. If assigned a single bounded item, implement and report that item to its coordinator.

## Keep resumable state

Use the project's existing conventions or a compact conversation record. Keep the authoritative spec, item status and dependencies, accepted artifacts, verification evidence, and unresolved blockers. Associate evidence with an unambiguous artifact revision or snapshot and the acceptance criteria it checked. A later agent must be able to tell which result passed, not just that a test once passed.

No tracker, worktree, standing service, or extra document is mandatory. Do not create further project work to occupy available agents.

## Dispatch, build, and integrate

1. Select items whose dependencies and consequential decisions are resolved. Give each fresh builder the [cold-start packet](specify.md#cold-start-work-packet), accessible project materials, and clear write ownership. Keep the packet bounded; it is not a transcript or a line-by-line coding prescription.
2. Parallelize only genuinely independent work where it helps. Sequence shared-state edits or use isolated checkouts when needed. Checkouts are an option, not a prerequisite. If builder delegation is unavailable, the coordinator may build within the same bounds.
3. The builder inspects the relevant code and affected contracts, implements the behavior, and runs proportionate direct checks plus required project checks. Add durable regression tests when useful; test-first work is optional. Report changes, artifact identity, acceptance evidence, meaningful choices, and unresolved limitations. Passing builder tests is not item acceptance.
4. Commission a fresh independent verifier using [Verify and close](verify.md). It receives the contract and actual artifact without the builder's conversation or advocacy, and selects meaningful checks from the spec before relying on builder evidence. Preserve that separation when sharing reports later. Do not substitute another pass by the builder for independence.
5. Adjudicate findings against the spec and evidence, arrange fixes within scope, and request focused independent follow-up when warranted. Accept an item only when its required checks pass on the current result and no substantiated serious concern remains. Keep blocked or unverified items visible; do not silently advance their dependents as though they passed.
6. Integrate accepted items and independently verify the assembled result through the intended entrypoint to its required observable effect. One independent pass may cover both item and final levels for a one-item change if it checks the final integrated artifact, all item criteria, and the full intended user path, with no relevant changes afterward.

The coordinator owns product changes and reconciliation; verifiers report findings and evidence. Follow-up packets identify the serious findings, fixes, current artifact, and affected behavior without coaching a desired verdict. Reuse valid prior evidence. Integration or fixes invalidate only the evidence they materially affect; broaden checks when there is a stated reason.

## Handle boundaries and blockers

Redesign inside the item can proceed when it preserves the spec and item bounds. Correcting an implementation to meet the contract is a repair, not a spec redesign. Necessary implementation details remain delegated.

For a proposed spec redesign or implementation redesign outside the item's bounds, return to the user before doing the dependent work. Present the concrete issue and evidence, the smallest viable options, and the recommended choice. Do not silently enlarge an item because the change might fit the overall project. Continue unaffected authorized items where possible.

Run verification only in authorized environments and with permitted effects. If tools, access, independence, or required final-effect evidence are unavailable, record exactly what remains unverified and the needed decision or access. When attempts repeat without useful progress or evidence cannot settle a consequential disagreement, surface that blocker. Do not relax acceptance, restart unchanged loops, or manufacture new infrastructure to avoid reporting the limit.

At completion, report what was delivered, the acceptance criteria checked, observed results, and limitations or outstanding items. Follow the closure rules in [Verify and close](verify.md); once the finite agreed work passes, end the run.
