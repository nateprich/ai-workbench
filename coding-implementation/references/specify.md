# Prepare the work

Use one preparation process to reach Ready. Clarifying, shaping, specifying, splitting, and checking readiness are techniques within it, not separate states or approval ceremonies. Reuse an adequate supplied contract. A small change can remain one compact work record; use [project setup](setup.md) when durable tracking is needed.

## Establish the completion contract

Inspect relevant code, observed behavior, and accessible facts before asking the user. Reuse settled answers. Ask only about consequential unresolved goals, preferences, scope, or tradeoffs; routine implementation choices remain delegated. A documented claim is not observed behavior when that distinction affects acceptance. Record material assumptions and their evidence or uncertainty.

An agreed output representation can still leave the source input's units, format, or conversion undefined. Ground consequential input and interface meanings in the spec, authoritative source definitions, or observable existing behavior. A prior work item's “settled” label is not evidence for missing semantics. When plausible interpretations produce materially different behavior, record the needed decision and keep affected work Needs definition. Preserve independently settled contracts and continue useful preparation.

Identify the authoritative spec version or snapshot and stable requirement/acceptance references. At the project's scale, establish:

- Intended outcome, users, observable behavior, and concrete acceptance examples.
- Scope, non-goals, rejected alternatives, relevant constraints, and deliberate limits on complexity.
- Important failure cases and test priorities; tests themselves may be written after implementation.
- The final user path from its entrypoint to the required observable effect.
- Consequential unknowns, affected work, and who can resolve them.

Keep guardrails concrete: intended environment and users, supported scale, compatibility, permitted dependencies or services, and deferred features where relevant. Show consequential approaches and tradeoffs before treating them as settled. Agreement can already exist in the request or context; drafting a spec alone does not authorize building.

## Cover the whole outcome, detail the next useful batch

Keep one authoritative project outcome and a compact map from **every required outcome → work item(s) → acceptance evidence**. Include setup, integration, and delivery when required by the spec. Keep explicit non-goals outside the map. Record missing required work rather than silently narrowing the project to the tickets already created.

For a large project, detail the next useful batch and represent later required work as Needs definition with known boundaries, unknowns, and dependencies. Routine future implementation detail need not block useful work now. An unspecified interface or consequential decision needed by the current batch does block the affected items.

Split by coherent, observable behavior when it improves execution or verification; retain one item when it can be built and checked coherently. Do not impose line counts, a ticket per edit, mandatory scaffolding, long user-story inventories, or automatic prefactoring. Inspect actual shared interfaces and write conflicts that affect the plan without requiring an all-pairs matrix for unrelated work.

Summarize parent progress from agreed outcomes, unresolved work, accepted child results, and final verification. Identify what can advance and the next action; do not apply a duplicate item-level Ready gate to the parent. All existing children being Done is insufficient if promised outcomes remain uncovered. Deferral leaves required outcomes outstanding unless the user approves the scope change.

## Give each item an executable brief

Link existing detail rather than duplicating the spec. The brief stays subordinate to its identified spec revision. Describe behavior, contracts, and bounds; code locations are navigation aids, not a prescribed edit sequence. A fresh agent needs:

```text
Item: stable ID, intended observable outcome, requirement/acceptance references
Authority: authorized next action and scope; user instruction/reference;
           execution limits and pending consequential decisions
Contract: authoritative spec version/snapshot; examples, constraints,
          non-goals, relevant interfaces, and final user-path context
Bounds: allowed changes and excluded work, including shared behavior/interfaces
Workspace: repository/location, entrypoint, setup/run pointers, write ownership
Tracking: saved configuration and exact item/evidence destination
Dependencies: required accepted results/contracts and their identities;
              what is available, what is waiting, and the clearing condition
Progress: current stage, settled decisions, artifact/checkpoint, unresolved
          questions or findings, and the actual next action
Checks and return: required checks; artifact and spec identities, changes,
                   observed results, acceptance mapping, and limitations
```

Include consequential decisions present only in conversation. Make the referenced spec, setup, and prerequisite results accessible to delegates. A thinking handoff carries goals, users, decisions, constraints, non-goals, unresolved questions, and authorized next action; prepare its executable brief only as far as the user's authority permits.

## Check readiness and preserve partial work

Ready means an actionable contract, appropriate bounds, concrete acceptance, and understood dependencies, with no consequential definition decision remaining. A settled item can be Ready while waiting for a known upstream implementation; an item whose behavior or acceptance depends on an unanswered upstream decision remains Needs definition. Build eligibility is a separate check in [coordination](coordinate.md#select-the-right-assignment).

For a substantial new decomposition, use a fresh independent readiness reviewer when supported, following the user's review requirements. Give it the spec, actionable packets, and necessary project references without the drafting conversation. Ask which unanswered questions force consequential guesses, including missing required outcomes or incompatible shared interfaces. Reuse that review across the unchanged batch rather than requesting approval for every item. If required independent review is unavailable, disclose the outstanding check and continue only work that does not depend on it.

Resolve findings by cause: recover answers already in the spec/project; settle delegated implementation choices; test a material technical premise with the smallest useful authorized investigation. Create a separate bounded investigation only when needed. Return consequential user choices, required spec redesign, or item-external implementation redesign to the user with evidence and a recommendation. Do not invent an answer to make an item appear ready.

If preparation pauses, save settled decisions, draft spec/items, unresolved questions, and the next action in the same record. For example: “Behavior and scope settled; resolve partial-import handling, then finish splitting import items.” Remain Needs definition and resume the unfinished work without repeating settled grilling. A missing command or pointer calls for context repair, not automatic reshaping.

An approved spec/interface change can invalidate affected readiness and evidence even with unchanged code; changed artifacts can do the same with an unchanged spec. Mark the affected items and checks, preserve unrelated valid work, and seek the user's decision before an overall spec redesign.
