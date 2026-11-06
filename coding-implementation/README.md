# Coding Implementation

One software-delivery skill for turning a raw idea, a thinking handoff, an existing spec, or a bounded work item into a verified result. It enters at the stage the task needs, keeps the spec as the completion contract, and coordinates a finite set of implementation and independent verification steps.

## Use it

Invoke `coding-implementation` or ask your skill-aware agent to use Coding Implementation. Examples:

- “Help me turn this software idea into a spec. Do not build it yet.”
- “Implement this agreed spec in this repository and verify the result.”
- “Here is a bounded work item and its execution limits. Build it and return the evidence.”
- “Resume this implementation from the spec, accepted items, and verification record.”

The skill reuses settled decisions. A small change can have a short spec, one item, and one independent pass covering both the item and the unchanged assembled result. Larger changes can use fresh builders, dependency-aware coordination, and independent checks after each item and after integration. Follow-up reviews focus on serious findings, their fixes, and consequential affected behavior.

Thought Partner is optional when material thinking remains. A thinking-only request or permission to draft a spec does not authorize building; existing execution permission carries forward. You do not need separate stage skills or any upstream framework, tracker, dashboard, or orchestration service.

## Install

Ask your skill-aware agent to install `coding-implementation` from `nateprich/ai-workbench`, including the complete folder. For a manual install, copy the complete `coding-implementation/` folder into your host's skills directory, preserving `references/` and `LICENSE`. Installation and automatic discovery depend on the host.

The [entrypoint](SKILL.md) loads the relevant internal guidance for [specifying](references/specify.md), [coordinating](references/coordinate.md), and [verifying](references/verify.md). No build step or additional package is required. Independent verification depends on the host's available capabilities and authorization; if it cannot be performed, the skill reports it as outstanding rather than claiming completion.

These original instructions synthesize practices selected in the design from [Command Center](https://github.com/nateprich-projects/command-center), [Matt Pocock's skills](https://github.com/mattpocock/skills), [Superpowers](https://github.com/obra/superpowers), [GStack](https://github.com/garrytan/gstack), and [PStack](https://github.com/cursor/plugins/tree/main/pstack). No upstream implementation is bundled or required.
