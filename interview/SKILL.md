---
name: interview-first
description: Routes to the right pre-work interview before any serious AI-assisted work begins, then runs it. Use when an ask is underspecified (missing who it is for, why it matters, what success looks like, or the binding constraint), when the user brings a concrete plan, decision, or design that needs stress-testing before work starts, or when the user says "interview me", "grill me", "help me think through this", or "are we sure?" Picks interview-me for extracting intent one question at a time, and grill-me for grilling a plan as a decision tree. The point is clarity of perspective before the work goes forward, so the AI builds on what the user actually thinks instead of on a thin prompt.
---

# Interview First

Most AI work goes wrong before the first draft exists. A thin prompt with no real point behind it gets structure and confidence built around nothing, and the fix is to make the thinking happen first. This skill is the step I take before engaging any serious project with AI: an interview that gets my perspective clear before the work goes forward. It routes between two upstream skills, because the right interview depends on what you brought.

## Route first

Decide which shape you are holding, and run that interview without announcing the choice:

- **The ask is vague.** Who it is for, why it matters, what success looks like, or what constraint binds it is missing or fuzzy. Run interview-me: one question at a time, each with your best guess and the reasoning behind it attached, until you can restate the intent in the user's own words (outcome, who benefits, why now, success, binding constraint, what is out of scope) with about 95 percent confidence.
- **There is a concrete plan, decision, or design.** Run grill-me: map the decision as a tree, ask the whole frontier of open questions in one round with your recommended answer attached to each, then recompute the frontier from the answers and go again. End when the frontier is empty and nothing is left silently assumed.
- **There is a raw idea, not yet an ask or a plan.** Start with interview-me to extract the intent, then, once the idea has a shape, finish with one grilling round on the shape itself. The interview finds what the user wants; the grilling checks whether the plan for getting it holds up.

Switch modes silently if the shape changes mid-conversation. A grilling that exposes missing intent goes back to the interview. An interview that produces a concrete plan earns a grilling round before anyone builds anything.

## Run it well

- Give the interviewing agent your own context to work from first: your email, your messages, your files. Questions about your material produce clarity. Generic questions produce generic answers.
- In interview mode, ask one question at a time and wait. A list of ten questions gets skimmed; one question gets answered.
- Attach your guess to every question. Reacting to a concrete proposal is faster and sharper than answering in a vacuum, and the user correcting your guess is itself information.
- Push on answers that sound like convention or best-practice talk. Ask what the user would actually want if they did not have to justify it to anyone.
- Treat only an explicit yes as confirmation of the restated intent or the grilling's conclusions.
- Stop when you can predict the user's reaction to the next three questions you would ask, and say so plainly. Do not start the work itself in the same motion; the interview ends with the shared understanding stated, and the work starts after the user confirms it.

## Install the upstream skills

This router is a routing layer over two skills by other people, and it needs them installed to run the interviews at full strength:

- interview-me, by Addy Osmani, in https://github.com/addyosmani/agent-skills
- grill-me and the grilling method behind it, by Matt Pocock, in https://github.com/mattpocock/skills

Both are MIT licensed. Install them from their repos; they are linked, not copied, so their authors keep the maintenance and the credit.
