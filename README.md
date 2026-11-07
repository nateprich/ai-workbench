# AI Workbench

Agent skills and prompts for thinking through ideas, writing in your own voice, and building software from a clear spec.

This is my workbench: the tools I actually use when I work with AI, published so other people can use them too. The practice behind all of it is plain. Get clarity of perspective before the work starts, write in your own voice while the work happens, use judgment about the tools instead of accepting whatever they hand back, and edit what comes back like it matters. The tools in here support one or more of those four steps. Anything deep in a technical domain's weeds lives in its own repo, not this one, so the workbench stays useful to a general practitioner.

## What is inside

| Branch | What it holds | Who it is for |
| --- | --- | --- |
| [thought-partner](thought-partner/) | One self-contained skill for intent discovery, idea refinement, plan challenge, recurring-work thinking, and targeted decision lenses | Anyone thinking through a project, plan, article, or choice before committing to a direction |
| [coding-implementation](coding-implementation/) | One coding workflow with saved project setup, bounded specs and work states, fresh-agent coordination, and independent verification | Anyone building software who wants strong acceptance checks without unnecessary scaffolding or endless review |
| [anti-slop](anti-slop/) | The writing collection: prompts that build a skill file which writes in your voice, from your own sent writing | Anyone whose AI drafts sound like everyone else's |

## Installing

In a tool that supports installing agent skills, tell your agent which skill you want from https://github.com/nateprich/ai-workbench and have it include the complete skill folder. Ask it how to invoke the skill once installed. Installation and automatic discovery depend on your tool; see the [Thought Partner instructions](thought-partner/README.md) or [Coding Implementation instructions](coding-implementation/README.md).

If you use the skills CLI, the same install is one command:

```text
npx skills add nateprich/ai-workbench
```

For a manual skill install, copy the complete skill folder, including its references and license files. The prompts in the anti-slop branch are individual text files you paste into a chat. Nothing in here needs a build step.

Both skills work independently. Thought Partner can offer a useful next step and route to a suitable available skill, including Coding Implementation for software work. Coding Implementation also accepts a clear spec directly. Independent agent verification requires a host that supports it; an unavailable check remains outstanding.

### ChatGPT and repository updates

The skill folders in this repository are the source of truth. Local installations can update with the skills CLI. ChatGPT account plugins are a separate distribution path: install the plugin in ChatGPT to make it available in Chat and Work, and copy updates from the repository into that existing plugin. Installing or updating a local skill does not perform that account installation or sync.

The [ChatGPT sync procedure](docs/chatgpt-skill-sync.md) describes the one-way update and verification process. It preserves the existing plugins and their presentation; there is no separately authored ChatGPT edition of either skill.

## Where the thought-partner methods come from

The thought-partner folder bundles deliberately adapted methods from original publishers, with one shared routing and interaction contract. No separate upstream installations are required:

- Matt Pocock's grill-me, for stress-testing a plan or decision, at https://github.com/mattpocock/skills
- Addy Osmani's interview-me, for extracting what you actually want one question at a time, at https://github.com/addyosmani/agent-skills

Optional lenses also draw on neurofoo, Claudio Babelis/radarist, Vladimir Kochetkov/v0lka, and sammcj, with an original short description of Gary Klein's premortem method. Exact pinned sources, modifications, and retained MIT/Apache-2.0 terms are in [the provenance record](thought-partner/PROVENANCE.md). Install the complete folder so its references and licenses travel with it.

Nate Rich
