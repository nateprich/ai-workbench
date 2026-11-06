# Changelog

## Unreleased

- Documented one-way repository-to-ChatGPT plugin sync, including complete-file comparison, guarded updates, deletion handling, and readback verification.
- Added Coding Implementation: one standalone skill for bounded software specs, automatic coordination, cold-start work items, independent acceptance tests, and focused repair loops.
- Extended Thought Partner with optional next steps and routing to suitable available skills, preserving standalone use and the user's authorization across handoffs.
- Verified installed skill discovery, planning-only handoffs, and a two-item implementation with independent defect detection, repair, and final saved-output checks.
- Rebuilt thought-partner as one self-contained skill with targeted internal methods, optional decision/challenge lenses, proportional completion, original-source attribution, and bundled licenses. Added migration guidance and isolated cold-start validation.
- Renamed the interview-first router to thought-partner and moved its folder from interview/ to thought-partner/. The upstream interview-me skill keeps its name.

## 0.1.0 - 2026-10-20

Initial contents of the workbench:

- Root README with the practice statement, the branch index, and per-tool install instructions.
- interview: the interview-first router skill, which routes between a requirements interview (interview-me, by Addy Osmani) and a plan grilling (grill-me, by Matt Pocock), with a branch README.
- anti-slop: the writing collection README with the three-failures frame, plus three prompts: voice-light (the basic voice-skill prompt), voice-heavy (the measured voice-skill prompt with corpus rules and a calibration test), and custom-instructions (the follow-up prompt that preloads a built voice skill).
- copilot: stub README marking the branch's intent. Setup and model selection material arrives with the Copilot posts.
