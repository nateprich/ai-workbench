# Anti-Slop

The writing collection: how to use AI to write better instead of using it to produce slop faster. This branch collects the tools from the anti-slop writing posts.

Three failures produce most of the slop I see, and each one has a fix:

1. **Garbage in.** The writing starts before the thinking happens, so the AI builds structure around nothing. The fix is to be interviewed first, which is what the [interview branch](../interview/) is for.
2. **The AI voice.** The draft comes back in a generic competent voice that belongs to nobody, because the model has never been shown how you write. The fix is a voice skill, a file built from your own sent writing that teaches your tools to write like you. The prompts below build one.
3. **The skipped edit.** The draft reads well enough and ships unchecked, including the places where the AI was confidently wrong. No tool fixes this one. The tools get you about 80 percent of the way there, and the thinking before and the editing after are the 20 percent, and that part is still yours.

## The prompts

| Item | What it does | Use when |
| --- | --- | --- |
| [voice-light.md](prompts/voice-light.md) | The basic prompt: points an AI at your sent email and documents and asks it to build a profile of your writing voice and a skill file that writes in it | You want a first voice skill, or a quick one for a new tool |
| [voice-heavy.md](prompts/voice-heavy.md) | The bigger prompt: exact corpus rules (sent items only, authored only), measured mechanics instead of impressions, a fixed deliverable schema, and a calibration test that makes different tools' outputs comparable | The basic prompt came back generic, or you want to compare what different tools produce from the same writing |
| [custom-instructions.md](prompts/custom-instructions.md) | The follow-up prompt: tells the agent to preload the finished skill into the tool's custom instructions, so every chat that writes for you starts from your voice | Right after a voice skill is built, in each tool you write with |

Point either building prompt at whatever writing you have: sent email, documents, posts. Sent work only, because what you sent is what you sound like when you are being yourself on purpose. Fill in the bracketed slots in the heavy prompt (your account, your document window, a short scenario) before you run it.

A skill you have to remember to invoke is a skill you will forget under deadline, so finish with the custom-instructions prompt in every tool, not just the one that built the skill.
