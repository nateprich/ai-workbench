# Verify and close

Independent verification is actual testing against the contract, with review of consequential risks. Perform it after each item and after integration. A one-item change can use one pass for both when the verifier checks the unchanged final integrated artifact against all item criteria and the full intended user path.

## Give the verifier a clean start

Use a fresh agent separate from the builder when supported and authorized. Supply only the context it needs:

- Relevant authoritative spec snapshot, acceptance criteria, examples, scope, and guardrails.
- Actual artifact and its identity, workspace, intended environment and entrypoint, setup, and required checks.
- Authorized test actions and limits, accepted dependency contracts, and material unresolved decisions.

Exclude the builder's conversation and advocacy. The verifier first selects meaningful checks from the spec and records what observable result each should establish. It then inspects and exercises the artifact. Existing tests and builder reports can inform later investigation, but cannot replace independent test selection or execution. The verifier reports findings and evidence; the builder or coordinator makes product fixes.

If a separate verifier is unavailable, perform useful self-checks but disclose that independent verification remains outstanding. Do not relabel self-review as independent or claim full completion while a required check is unverified.

## Exercise the relevant behavior

Cover acceptance criteria, the main user path, consequential changed failure cases, and relevant regressions. Run existing required project checks. Choose a small set of checks able to expose meaningful failures, using direct execution or durable regression tests as appropriate. Test-first work can help reproduce bugs, but strict TDD, coverage quotas, exhaustive edge-case lists, and new test infrastructure are not defaults. Do not test only implementation details or whether a skill repeats particular wording.

When correctness depends on shared data, interfaces, dependencies, or lifecycle behavior, trace affected consumers beyond the immediate edit. Check the few consequential assumptions using the cheapest direct evidence. For example, a changed persisted value may affect a reader outside the edited module. This is a focused impact check, not an inventory of the entire system; required but unproven assumptions remain unverified.

For software, run the real behavior in the authorized intended environment and inspect the observable result, including required saved output or completed effects. Final verification begins at the intended entrypoint and follows the assembled user path. A successful acknowledgment is not evidence of a downstream effect. State material mocks, substitutes, and bypassed boundaries and limit conclusions to what was exercised. Missing required integration or final-effect evidence stays unverified unless the user agrees to an adequate substitute or changes the acceptance requirement. Testing grants no extra access or external-action authority.

For skills, use realistic requests with permitted raw inputs and examine actual decisions, actions, outputs, and artifacts. Metadata and reference checks are useful structural checks, not behavioral proof. Keep evaluation artifacts isolated from the product and outside its source package.

Return the artifact identity, criteria checked, actions or commands performed, expected and observed outcomes, environment limits, and findings. “Tests passed” or an empty findings list alone is insufficient evidence.

## Decide what needs another round

All required acceptance criteria remain obligations. A serious finding has a material consequence for the agreed outcome, behavior, constraints, or intended use and is supported by one of:

- A material requirement failure or missing evidence for an agreed critical acceptance check.
- A change-caused regression that materially affects intended use.
- A concrete consequential failure in intended usage, such as data loss or unauthorized access.
- Substantial unrequested scope, dependency, or architecture growth without demonstrated need.

Each serious finding names the requirement or guardrail, trigger or evidence, and consequence. The coordinator adjudicates against the contract and evidence rather than accepting every suggestion. Resolve a credible but uncertain concern with a focused check; uncertainty alone does not justify an open-ended investigation.

Minor requirement mismatches still need repair and affected checks, but do not trigger a broad review. Harmless capitalization can get a focused correction; a misleading label that causes the wrong destructive action is serious. Cosmetic preferences, equivalent alternative implementations, and speculative future problems do not expand the work. Fix small nits along the way only when safely within scope.

## Fix, recheck, and stop

Fix substantiated serious findings within scope and repeat independent review as needed. There is no fixed round cap that waives acceptance. After the initial review, follow-ups focus on unresolved serious findings, their fixes, and consequential affected behavior. Broaden only when changes or new evidence materially invalidate earlier verification, and state why. Preserve the evidence that remains valid.

Close an item or final review only when required acceptance checks pass on the current result and no substantiated serious concerns remain. After cleanup, rerun affected checks; reopen review only when a change or new evidence creates a serious concern. A resolved or dismissed finding requires new evidence or a relevant change to reopen. Nits do not start another broad search.

Repeated attempts without useful progress, unavailable required evidence, or a consequential disagreement that evidence cannot resolve call for a blocker report and the needed user decision or access. Do not silently weaken the contract, declare success, or repeat the same loop indefinitely. Report delivered behavior, checked acceptance criteria, observed results, and any limits or outstanding items. When the finite agreed work is complete, stop.
