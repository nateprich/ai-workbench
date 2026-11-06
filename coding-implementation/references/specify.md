# Specify and split

Use this stage only to fill consequential gaps. A ready spec or bounded item can enter implementation directly. Keep existing project document and task conventions; a small change may need only a short contract in the conversation and one item.

## Resolve the questions that change the work

Inspect relevant code, behavior, and accessible facts before asking the user to supply them. Ask about unresolved goals, preferences, scope, or consequential tradeoffs. Use available thinking support when useful; return its decisions and uncertainties to this workflow. Do not grill settled answers again or ask merely to fill a template.

Show the proposed approach and consequential tradeoffs. Distinguish delegated implementation choices from decisions the user still owns. Agreement can already exist in the supplied request or context; use it. If agreement on a material decision is missing, resolve that decision before dependent work. Drafting a spec remains separate from authorization to execute it.

## Establish the completion contract

Use stable references for requirements, acceptance criteria, and items, so builders and verifiers can identify the same obligations. Record the authoritative spec version or snapshot. Make these clear at the project's scale:

- Intended outcome, users, and observable behavior, with concrete acceptance examples.
- In-scope work, explicit non-goals, existing-system constraints, and deliberate limits on complexity.
- Important failure cases, acceptance checks, and test priorities selected before implementation. The tests themselves may be written later.
- Bounded items, dependencies, and the final assembled path from the intended entrypoint to its observable effect.
- Unresolved decisions that could change the work, their consequences, and which work depends on them.

Include only relevant guardrails, stated concretely: intended environment, supported users and scale, permitted dependencies or services, compatibility expectations, deferred features, and complexity that would be unjustified here. Builders and reviewers share these boundaries. Avoid vague “production-ready” or “scalable” goals when the actual requirement can be stated.

## Choose useful work items

Prefer a complete observable behavior slice. Split when dependencies, execution, or review become clearer, not to satisfy a line count, a time box, or a ticket-per-edit rule. One item is enough when it can be built and verified as a coherent change. Identify shared files, data, and interfaces whose concurrent modification would be unsafe; the coordinator chooses sequencing or isolation as needed.

Describe what each item may change, including shared behavior and interfaces. Link earlier accepted artifacts or contracts needed by dependent items. Do not turn an implementation guess into a prescribed sequence of edits: a builder must inspect the code and can redesign within the item's bounds while preserving the spec.

## Cold-start work packet

Provide a short self-contained brief for a new builder or chat. Use accessible references for existing details, but include any consequential decision otherwise present only in the conversation. Adapt this format rather than creating empty fields or a new file for every handoff:

```text
Item: stable identifier and intended observable outcome
Authority: authorized next action and scope; relevant user instruction/reference;
           execution limits; decisions still awaiting the user
Contract: authoritative spec version/snapshot and acceptance references;
          relevant examples, guardrails, non-goals, and final user-path context
Bounds: allowed changes, including shared behavior/interfaces; excluded work
Workspace: repository/location, relevant entrypoints, setup/run instructions
Dependencies: accepted prerequisite artifacts/interfaces and their identities
Uncertainty: known constraints, material unknowns, and blocked decisions
Checks and return: required checks; artifact identity, changes, observed results,
                   acceptance mapping, limitations, and unresolved issues
```

The receiving agent must be able to find the contract and artifacts without the prior chat. Check access and missing authority before dispatch rather than letting a fresh agent invent them. A thinking handoff carries goal, users, decisions, constraints, non-goals, unresolved questions, and the authorized next action; convert it into a work packet only if implementation is authorized and the contract is ready.
