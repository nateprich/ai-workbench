# Project setup

When work needs durable tracking across items or sessions, reuse existing project instructions or save a small configuration record. Default to `docs/agents/issue-tracker.md`, referenced from existing agent instructions; keep an established equivalent location. A small one-off change can use one compact work record without a board or extra files. Setup does not authorize implementation or external writes beyond the user's existing instructions.

## Select and record the actual route

Load saved configuration in a fresh session, then reuse it within the run. Give fresh delegates the relevant instructions or an accessible pointer. Do not rediscover project fields and conventions for every item. Revisit only on request, for required missing configuration, or after a concrete failure or changed environment shows it is stale; repair the affected part rather than repeating all setup.

Use the project's chosen tracker. If none exists, select an appropriate supported route without adding a service the task does not need:

- [GitHub template](../assets/tracker-github.md): existing authoritative spec plus linked issues. Use an existing suitable Project status field; otherwise use one mutually exclusive stage-label set. Do not mirror stage in both. Prefer native dependency links when supported; a configured explicit referenced list is acceptable.
- [Local template](../assets/tracker-local.md): existing spec and simple work records with stable IDs, stage, dependencies, and evidence. Split item files only when useful for independent work. No second status database or dashboard is required.
- A custom tracker can use available tools and project conventions. Identify missing capabilities specifically, with no universal compatibility claim or automatic integration-building task. **Custom tracker integrations are self-service and are not tested or supported by ai-workbench.** This support boundary does not prevent routine setup help authorized by the user.

Instantiate only the chosen template. Save concrete values and usable selected operations, not a list of headings for the next agent to rediscover:

- Exact destination: host/repository/project IDs, field/option or label identities as applicable, or actual file paths; authoritative spec, work record, and evidence locations.
- Available tool/CLI and access mechanism by reference, with known limits. Never copy credentials into configuration.
- The concrete calls or commands to find, create, read, update, link, and finish items, including their destination arguments and readback. Distinguish fixed project values from per-item inputs and save how the latter are obtained.
- Stage mapping, dependency representation, stable item keys and brief conventions, blocker/disposition handling, and where outcome coverage and parent progress live.

Read the destination and inspect relevant tool capabilities to establish that this route is usable. Do not claim an operation was tested if only its documentation was inspected. Any setup test writes must be within authorized destinations and effects. A configuration with required unknown fields or unavailable operations is incomplete for those operations; record the precise limitation and continue only unaffected work.

## Reconcile writes and preserve the source of truth

Use the configured destination explicitly on every operation; do not rely on a current-repository default, similarly named project, or remembered file location. Live item status, dependency results, and acceptance evidence still need reading when they affect a decision even though setup is reused.

For an uncertain or partial write, first read the exact target and reconcile what succeeded. For creation, use the stable item key to find the possible new item before retrying; an incomplete listing or delayed search result does not prove absence. Do not create a duplicate while uncertainty remains. For multi-part operations, retain successful portions and finish only missing portions after readback.

Save the unresolved operation and next action in the existing coordination record, not a parallel tracker. Report verified product behavior separately from a failed stage or evidence update. A partially finished tracking operation remains outstanding. If the destination is unavailable, report the concrete failure and affected work; do not silently switch trackers or create local replacements. Continue independent authorized work that does not depend on the failed operation.
