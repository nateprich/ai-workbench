# AI Workbench

Agent skills, prompts, and setups for deliberate AI-assisted knowledge work: interview-first drafting, writing in your own voice, and Copilot configuration. For Copilot, ChatGPT, and Claude.

This is my workbench: the tools I actually use when I work with AI, published so other people can use them too. The practice behind all of it is plain. Get clarity of perspective before the work starts, write in your own voice while the work happens, use judgment about the tools instead of accepting whatever they hand back, and edit what comes back like it matters. The tools in here support one or more of those four steps. Anything deep in a technical domain's weeds lives in its own repo, not this one, so the workbench stays useful to a general practitioner.

## What is inside

| Branch | What it holds | Who it is for |
| --- | --- | --- |
| [interview](interview/) | The interview-first router skill, which picks between a requirements interview and a plan grilling based on what you brought | Anyone starting serious work with an AI who wants their own thinking clear before the first draft exists |
| [anti-slop](anti-slop/) | The writing collection: prompts that build a skill file which writes in your voice, from your own sent writing | Anyone whose AI drafts sound like everyone else's |
| [copilot](copilot/) | Copilot-specific tools, including setup and model selection material | Reserved for now; the branch fills in as the posts that produce it are published |

## Installing

If you have never installed a skill before, the easy path works in Copilot, ChatGPT, and Claude alike: tell your agent "I want to install the skills at https://github.com/nateprich/ai-workbench" and the agent should handle the rest. Ask it how to use the skill once it is installed if this is your first time; it is very easy, I promise.

If you use the skills CLI, the same install is one command:

```text
npx skills add nateprich/ai-workbench
```

You can also copy any single file by hand. The skills are plain Markdown with a name and a description at the top, and the prompts in the anti-slop branch are plain text you paste into a chat. Nothing in here needs a build step.

## Where the interview modes come from

The interview branch routes between two upstream skills, and both are worth installing on their own:

- Matt Pocock's grill-me, for stress-testing a plan or decision, at https://github.com/mattpocock/skills
- Addy Osmani's interview-me, for extracting what you actually want one question at a time, at https://github.com/addyosmani/agent-skills

Both repos are MIT licensed, and this repo is MIT licensed as well. The router here links to the upstreams rather than copying them, so install theirs from their repos and this one for the routing.

Nate Rich
