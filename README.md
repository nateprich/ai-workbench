# AI Workbench

Agent skills and prompts for thinking through ideas and writing in your own voice.

This is my workbench: the tools I actually use when I work with AI, published so other people can use them too. The practice behind all of it is plain. Get clarity of perspective before the work starts, write in your own voice while the work happens, use judgment about the tools instead of accepting whatever they hand back, and edit what comes back like it matters. The tools in here support one or more of those four steps. Anything deep in a technical domain's weeds lives in its own repo, not this one, so the workbench stays useful to a general practitioner.

## What is inside

| Branch | What it holds | Who it is for |
| --- | --- | --- |
| [thought-partner](thought-partner/) | One self-contained skill for intent discovery, idea refinement, plan challenge, recurring-work thinking, and targeted decision lenses | Anyone thinking through a project, plan, article, or choice before committing to a direction |
| [anti-slop](anti-slop/) | The writing collection: prompts that build a skill file which writes in your voice, from your own sent writing | Anyone whose AI drafts sound like everyone else's |

## Installing

In a tool that supports installing agent skills, tell your agent "I want to install thought-partner from https://github.com/nateprich/ai-workbench" and have it include the complete skill folder. Ask it how to invoke the skill once installed. Installation and automatic discovery depend on your tool; see the [thought-partner instructions](thought-partner/README.md) for the folder, CLI, and migration options.

If you use the skills CLI, the same install is one command:

```text
npx skills add nateprich/ai-workbench
```

For a manual skill install, copy the complete skill folder, including its references and license files. The prompts in the anti-slop branch are individual text files you paste into a chat. Nothing in here needs a build step.

## Where the thought-partner methods come from

The thought-partner folder bundles deliberately adapted methods from original publishers, with one shared routing and interaction contract. No separate upstream installations are required:

- Matt Pocock's grill-me, for stress-testing a plan or decision, at https://github.com/mattpocock/skills
- Addy Osmani's interview-me, for extracting what you actually want one question at a time, at https://github.com/addyosmani/agent-skills

Optional lenses also draw on neurofoo, Claudio Babelis/radarist, Vladimir Kochetkov/v0lka, and sammcj, with an original short description of Gary Klein's premortem method. Exact pinned sources, modifications, and retained MIT/Apache-2.0 terms are in [the provenance record](thought-partner/PROVENANCE.md). Install the complete folder so its references and licenses travel with it.

Nate Rich
