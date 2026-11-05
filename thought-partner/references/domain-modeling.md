# Domain modeling: shared meaning alongside the conversation

Use when overloaded terms, relationships, or boundaries could cause people to agree on words while imagining different things. It can accompany grilling or recurring-work thinking. A codebase alone is not a reason to run it.

Use existing relevant vocabulary documents where available. When a term conflicts with that language or carries multiple meanings, point out the concrete difference and propose a precise term. Test the distinction with a scenario or edge case. Check relevant code or documents when available; describe a mismatch as something to resolve, not proof that the user is wrong.

Keep a compact working understanding in the conversation. If persistence is requested or already authorized, follow the project's conventions, including CONTEXT.md, GLOSSARY.md, or context-specific files. Keep a glossary about domain meanings; preserve implementation tradeoffs in the project's decision records rather than smuggling them into definitions.

A decision record is useful when a genuine tradeoff is costly to reverse and would surprise a future reader without its rationale. Routine choices need no ADR. Saving documentation is an optional output governed by the shared contract; the method itself does not grant permission to write or delete files.

Adapted from Matt Pocock's repository; see [provenance](../PROVENANCE.md). Its automatic persistence and fixed document-format dependencies are replaced by optional project-native documentation.
