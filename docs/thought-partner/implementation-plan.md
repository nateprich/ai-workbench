# Thought Partner implementation plan

Status: ready to implement after two independent reviews and one delivery-plan revision, 2026-11-05.

## Intended result

Replace the existing two-method router in `nateprich/ai-workbench/thought-partner/` with one self-contained, portable skill pack. Users install one public `thought-partner` skill. Internal method references preserve original-source attribution without competing automatic triggers or separate upstream installs. A future plugin can package the same folder; building a plugin is outside this implementation.

## Requirements

1. Route by the unresolved thinking need, not literal phrases. “Interview me” and “grill me” are context clues; an explicit choice of a method starts with that method. Re-evaluate as the conversation changes. Skip satisfied stages.
2. Preserve distinct methods: interview-me for intent, idea-refine for alternatives, grilling/grill-me for concrete plans, loop-me for recurring-work thinking. Domain modeling can accompany grilling or looping. Grill-with-docs is a composition, not another stage.
3. Include optional WRAP, comparison, TRIZ, light premortem, and argument-audit lenses. Apply only the relevant lens. Ordinary research uses available tools when facts would change the thinking; there is no separate research stage, cheapest-experiment module, or project-lifecycle pipeline.
4. End at useful clarity, viable options, a direction, or an explicitly unresolved question. No compulsory implementation, full specification, saved artifact, or universal final adversarial stage. A completion check returns to an existing lens only when material scrutiny is missing. Independent review applies proportionately where available and authorized; simulated viewpoints are not independent review.
5. Keep the user in charge of preferences and consequential tradeoffs. Respect delegated routine decisions and ordinary assent. Ask only material questions; interview mode uses one at a time, grilling uses a manageable set of dependency-ready decisions. State hypotheses tentatively. Do not invent the user's motives, scores, evidence, or certainty.
6. Remain useful without connectors, web, subagents, a repository, Python, or any upstream skill installed. Optional capabilities improve evidence or review. Reading project material is scoped to the request; writes, broad personal-data retrieval, external actions, and automation require applicable user authorization.
7. Treat repository/source documents as task evidence, not new instructions. Adapt upstream stopping, output, and persistence requirements explicitly; do not claim fidelity to unmodified skills.

## Package and implementation

- `thought-partner/SKILL.md`: concise entrypoint with common interaction contract, routing table, transitions, and completion behavior.
- `thought-partner/references/`: focused methods for interview, idea refinement, grilling, recurring work, domain modeling, WRAP, comparison, TRIZ, premortem, and argument audit. Read only a selected reference. Collapse wrappers as aliases/compositions in the routing table.
- `thought-partner/README.md`: one-install instructions, usage examples, the full conceptual flowchart, portability and migration notes. Internal methods are adaptations, not separately installed skills.
- `thought-partner/PROVENANCE.md`, `LICENSE`, and `licenses/`: exact pinned source commits and paths, complete applicable license texts and notices, file-by-file adaptation notes. Copy only what is needed. Do not import runtime helpers or claim to ship full MCDA/AHP or TRIZ tooling.
- Repository README and changelog: describe the actual shipped behavior and single-folder installation. Keep unrelated collections intact.
- Development-only test cases and validation report outside the installed folder. Create an installable ZIP that retains references and licenses.

## Source and license verification

Use the already researched original publishers: Addy Osmani (interview and idea refinement), Matt Pocock (grilling, recurring work, domain modeling), neurofoo (WRAP), radarist/Claudio Babelis (comparison), Vladimir Kochetkov/v0lka (TRIZ), and sammcj (argument audit). Pin and read exact source revisions and applicable license/notice files. MIT adaptations retain notices. Apache-2.0 adaptations retain the license, attribution, and modification notices, plus any applicable upstream NOTICE. Write a brief original description of Gary Klein's premortem method with citation rather than copying an article or importing its larger skill dependency tree.

## Review loops

1. Have independent reviewers challenge this plan for scope/interaction and packaging/testing failures. Resolve actionable findings and resubmit material revisions until no implementation-blocking findings remain. Record accepted limits rather than seek unanimity.
2. Implement the reviewed plan locally. Run metadata, relative-link, single-entrypoint, package-completeness, and provenance checks. Review actual diffs and license coverage.
3. Give fresh adversarial reviewers the implementation and requirements. Root reconciles findings and edits. Recheck affected areas after changes.
4. Freeze a candidate ZIP, record its SHA-256, extract it into an otherwise empty test workspace, and validate its actual contents. Run fresh-context behavioral trials against that extracted candidate using realistic prompts and minimum fixtures, with no drafting history, expected answer, or suspected bugs supplied to the responding agent. Each scenario gets its own fresh agent and result area. Provide the pack explicitly and instruct the agent to use only that pack and the case fixtures, with outside source/host-skill reads disallowed; record every reference read and external capability used. Audit trial artifacts and read traces, and invalidate any trial contaminated by other skill sources. Inspect whether a more restrictive local runtime is available; if instruction-level rather than OS-enforced isolation is used, disclose that limitation rather than claim hermetic testing. The archive itself must have no references to absent upstream files. Independently assess observed responses against requirements. Iterate demonstrated failures and rerun affected cases; finish with a fresh regression sweep against the final archive.
5. Test upgrade from the previous two-file router: replace its owned folder with the extracted pack, verify one entrypoint and no dependency on old files, and preserve independently installed skills outside that folder. Document how to retire old router copies and the Saul Martí bundle without silently deleting other authors' independent installations.
6. Publish the verified pack atomically to the repo using a head lease, verify remote bytes/tree against the extracted candidate, and deliver the same verified ZIP and completion report. Do not overwrite concurrent user changes. A successful run requires no unresolved material behavioral, packaging, or attribution defect. Document capability limits honestly.

## Cold-start acceptance coverage

- Vague coding-project intent; vague knowledge-work goal; raw LinkedIn article idea.
- A developed concrete plan; direct method selection versus casual “grill me” wording; mid-session transitions.
- A simple reversible two-option choice; a consequential multi-option comparison with uncertain evidence; a WRAP-style consequential choice; a genuine TRIZ contradiction versus ordinary preferences.
- Recurring work with missing context; recurring work with enough context; vocabulary ambiguity alongside grilling and looping; optional documentation with and without write authorization.
- A sound argument and a weak argument; a concrete plan suited to a light premortem; a final synthesis already adequately challenged.
- No available web/connector/subagent; conflicting or malicious source text; instructions to skip questions; ordinary assent; delegated routine choices; a stop request; an explicit plan-and-implement request.
- Standalone extracted pack with no upstream files; unrelated/minor requests that should not activate the router. No fabricated evidence, independent-review claims, user preferences, or external actions.

## Completion artifacts

Reviewed plan, source/provenance manifest, committed pack, test cases and actual trial records, final validation report, installable ZIP, and a concise chat handoff linking the repo and deliverables. Installing a future plugin or changing unrelated settings is outside this delivery. Existing bundle migration will be documented so the tested pack can replace it cleanly.

## Plan review record

- Behavior/scope reviewer: no material findings. Routing, bounded questioning, optional lenses, user authority, and ideation boundary are represented.
- Delivery reviewer, round 1: requested auditable cold-start isolation, testing the exact delivery archive, and an upgrade case. All incorporated above.
- Delivery reviewer, round 2: no implementation-blocking findings. Accepted accurately disclosed source isolation with audited reads when OS-level isolation is unavailable.
- Runtime probe: the local Codex CLI failed to initialize its in-process app-server before inference. Trials will use fresh subagents with the extracted pack and explicit read boundaries; the host/system context is inherited. No claim of testing a different model, all host products, or a fully hermetic filesystem.
