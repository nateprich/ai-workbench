# Grilling / grill-me: challenge a concrete plan

Map the important decisions and their dependencies. Separate established facts, testable assumptions, user choices, and choices already delegated to the assistant. Focus on decisions that could materially change the plan; exhaustive traversal of hypothetical branches is unnecessary.

Ask the decisions whose prerequisites are settled. A manageable set of independent questions can share a round, each with a recommended answer and its rationale. If the user prefers one at a time, honor that. Wait for answers before asking questions that depend on them. Resolve relevant accessible facts with ordinary tools rather than sending lookup work to the user.

After each answer or discovery, revise the dependency picture. Challenge unsupported premises, incompatible constraints, and the strongest credible alternative. Explain what consequence makes a question worth asking. Accept routine delegated decisions; preserve genuine consequential preferences for the user. If the user's goal itself becomes unclear, return to intent discovery.

Finish when the consequential branches are understood sufficiently for the intended decision, with assumptions and residual uncertainties visible. “No more conceivable questions” is not the standard. Count challenge already performed when the router checks readiness.

For grill-with-docs, combine this with [domain modeling](domain-modeling.md). Use that same overlay for recurring-work discussions when vocabulary is causing ambiguity. Persistent documentation follows the shared authorization rules.

Adapted from Matt Pocock's repository; see [provenance](../PROVENANCE.md). The public grill-me wrapper is collapsed into this internal method.
