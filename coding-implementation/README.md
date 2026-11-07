# Coding Implementation

One software-delivery skill for turning a raw idea, a thinking handoff, an existing spec, or a bounded work item into a verified result. It enters at the stage the task needs, keeps the spec as the completion contract, and coordinates a finite set of implementation and independent verification steps.

## Use it

Invoke `coding-implementation` or ask your skill-aware agent to use Coding Implementation. Examples:

- “Help me turn this software idea into a spec. Do not build it yet.”
- “Implement this agreed spec in this repository and verify the result.”
- “Here is a bounded work item and its execution limits. Build it and return the evidence.”
- “Resume this implementation from the spec, accepted items, and verification record.”

The work-item states are **Needs definition → Ready → Building → Verifying → Done**. Preparation includes clarification, specification, splitting, and readiness review without a separate Shaped checkpoint. Blockers are recorded beside the stage. An interrupted builder resumes in Building; verification resumes in Verifying. A settled Ready item may wait for a known dependency, while an unresolved behavior decision still needs definition.

The skill reuses settled decisions. A small change can have a short spec, one item, and one independent pass covering both the item and unchanged assembled result. Larger changes keep every promised outcome represented while detailing the next useful batch. Parent progress is derived from outcome coverage and accepted results; all existing tickets being Done does not hide unfinished requirements. Follow-up reviews focus on serious findings, fixes, and consequential affected behavior, with no arbitrary cap that waives acceptance.

Thought Partner is optional when material thinking remains. A thinking-only request or permission to draft a spec does not authorize building; existing execution permission carries forward. You do not need separate stage skills or any upstream framework, tracker, dashboard, or orchestration service.

## Project setup

For work spanning items or sessions, the agent reuses existing project tracker instructions or saves them in `docs/agents/issue-tracker.md`, linked from the project's agent instructions. The record contains the exact destination, selected tool operations, state/dependency conventions, and spec/evidence locations. Setup is reused until a specific gap or failure needs repair. A one-off change can remain one compact record.

The bundled [GitHub](assets/tracker-github.md) and [local-file](assets/tracker-local.md) templates carry the same contract. GitHub uses an existing suitable Project status field or one stage-label set, plus issues and the existing spec. Local tracking uses simple item records and no extra status database. Uncertain writes are read back before retrying; an unavailable destination is reported without silently creating a shadow tracker.

Agents may help configure another tracker using the user's available tools and conventions, identifying any missing capability. **Custom tracker integrations are self-service and are not tested or supported by ai-workbench.** This limits repository support rather than the setup assistance a user may authorize.

## Install

Ask your skill-aware agent to install `coding-implementation` from `nateprich/ai-workbench`, including the complete folder. For a manual install, copy the complete `coding-implementation/` folder into your host's skills directory, preserving `references/`, `assets/`, and `LICENSE`. Installation and automatic discovery depend on the host. The repository remains the single source; use the repository's existing ChatGPT sync process to update account plugins rather than maintaining a separate edition.

The [entrypoint](SKILL.md) routes to [setup](references/setup.md), [preparation](references/specify.md), [coordination](references/coordinate.md), and [verification](references/verify.md) as needed. No build step or additional package is required. Independent verification depends on the host's available capabilities and authorization; unavailable required checks stay outstanding. Acceptance evidence identifies both the artifact and the applicable contract revision. Structural validation alone does not establish behavioral correctness.

These original instructions synthesize practices selected in the design from [Command Center](https://github.com/nateprich-projects/command-center) (whole-outcome coverage and focused review), [Matt Pocock's skills](https://github.com/mattpocock/skills) (behavioral briefs and reusable tracker setup), [Superpowers](https://github.com/obra/superpowers) (cold-start readiness and resumption), [GStack](https://github.com/garrytan/gstack) (blocker distinctions and final-effect checks), and [PStack](https://github.com/cursor/plugins/tree/main/pstack) (an initial integrated slice and consequential consumer checks). These are selective adaptations, not measured reliability claims. No upstream prose, code, implementation, or runtime is bundled or required; the skill retains its [MIT license](LICENSE).
