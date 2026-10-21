# Interview

The systemic step before engaging any serious project with AI: get your own perspective clear before the work goes forward. An AI handed a thin prompt will build structure and confidence around nothing. An AI that has interviewed you first builds on what you actually think.

This branch holds one skill of mine and points at two of other people's. Mine is the router: it looks at what you brought, picks the interview that fits, and runs it.

## What is in here

| Item | What it does | Use when |
| --- | --- | --- |
| [interview-first](SKILL.md) (this branch) | Routes between a requirements interview and a plan grilling based on the shape of what you brought, then runs the chosen interview | Before any serious AI-assisted work, when you want clarity before the first draft |
| grill-me (upstream) | Grills a concrete plan or decision as a decision tree, frontier questions with recommended answers, until nothing is left silently assumed | You have a plan, a design, or a decision and want it stress-tested before you commit |
| interview-me (upstream) | Extracts what you actually want, one question at a time with a best guess attached, until your intent can be restated at about 95 percent confidence | Your ask is vague, or you suspect you are asking for the conventional thing instead of the thing you want |

The upstream skills live in their authors' repos and are linked, not copied: grill-me is by Matt Pocock, at https://github.com/mattpocock/skills, and interview-me is by Addy Osmani, at https://github.com/addyosmani/agent-skills. Both are MIT licensed.

## Installing

Tell your agent "I want to install the skills at https://github.com/nateprich/ai-workbench" and it should handle the rest, or use the skills CLI:

```text
npx skills add nateprich/ai-workbench
```

Install the two upstream skills from their repos as well; the router calls them by name. If you only ever use one mode, install that mode's skill and skip the router.
