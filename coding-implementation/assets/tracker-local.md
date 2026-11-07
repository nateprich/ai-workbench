# Local tracker configuration

Copy into the project's established configuration location or `docs/agents/issue-tracker.md` and reference it from agent instructions. Replace project constants with actual paths and tool names. A one-off task can keep configuration, spec, and one item in a single document; separate files are optional when they help independent work. Do not introduce a second status database or dashboard.

## Destination and conventions

- Workspace root: exact absolute path; include any workspace-specific access limits.
- Authoritative spec: exact file/section and version or snapshot convention.
- Items: exact document/section convention or directory and stable filename convention, such as `docs/agents/work/WORK-001.md` resolved against the recorded workspace.
- Outcome coverage and derived parent progress: existing spec/work-record section mapping every required outcome to items and evidence. Summarize accepted/unresolved outcomes and next action; do not copy item stages into a separate database.
- Evidence: exact existing document/section or directory; accessible to fresh delegates.
- Selected tools: actual host read, search, and edit tool names, supported operations, and limitations. Reference existing access mechanisms without copying credentials.
- Dependencies: stable item IDs with paths/anchors, required result/interface, and accepted artifact/evidence references. A reference or a Done label alone is not proof of the required result.
- Stages: `Needs definition`, `Ready`, `Building`, `Verifying`, `Done`. The coordinator edits the single `Stage` field under the skill's assignment and acceptance rules. Keep blockers, cancellation, and deferral separate with their reasons; neither disposition counts as Done.

## Selected operations

The following is a concrete shell + patch recipe. Save the available host's exact tool names and replace `WORKSPACE`, `ITEMS`, `ITEM_FILE`, and `RECORD_FILE` with actual configured paths or the saved per-item path rule. If the host uses another file editor, replace these with its concrete calls and readback. A list of required capabilities without selected operations is incomplete setup.

| Operation | Selected recipe and readback |
| --- | --- |
| Find/reconcile creation | Run `rg --files 'ITEMS'` and `rg -n -F 'WORK-001' 'RECORD_FILE' 'ITEMS'` through the selected shell tool. In a one-document layout, search only that exact document. Check the stable ID and actual target path before creating; an unreadable target does not prove absence. |
| Read | Run `cat 'ITEM_FILE'` or `cat 'RECORD_FILE'` with the selected shell tool. Read the referenced spec revision and relevant live dependency/evidence records as needed. |
| Create | Use the selected patch tool's Add File operation on the exact new item path with its allocated stable ID and record below; for one-document tracking, insert the item at its configured anchor. First check that the ID/path does not already exist; never overwrite an existing item as “creation.” Read back the exact target. |
| Update stage/brief/progress | Use the selected patch tool's Update File operation, matching current content and replacing only the affected fields/section. Re-read if context no longer matches; preserve unrelated edits. Read back the target and verify the single stage and intended changes. |
| Link dependency | Patch the item's Dependencies field with the prerequisite's ID/path/anchor, required result, and accepted artifact/evidence pointer. Read both records and inspect the required accepted result before it unblocks work. |
| Save evidence | Patch the configured evidence section/file with a stable evidence key and the record below. Read back the exact section; reconcile an uncertain write by its key before adding it again. |
| Finish | After independent acceptance, save evidence and accepted-result location, then patch Stage to Done. Read back stage, evidence, artifact/spec identities, and result availability. If a portion failed, retain an outstanding coordination operation rather than claiming the workflow finished. |
| Reopen invalidated acceptance | Patch the appropriate stage and reason, mark only affected evidence invalid, and update the actual next action. Read back; keep valid unrelated evidence. |

For example, with `apply_patch` selected, an item transition uses its actual path and observed prior value:

```diff
*** Begin Patch
*** Update File: /absolute/workspace/docs/agents/work/WORK-001.md
@@
-Stage: Ready
+Stage: Building
*** End Patch
```

The path above is illustrative; save actual project paths and the selected tool call in setup. Per-item arguments come from the allocated ID and saved path convention. The patch is an operation format, not permission to make that transition. For shared records, the coordinator sequences edits or assigns non-conflicting ownership. Do not overwrite from a stale full-file snapshot.

Reuse this setup until a specific gap/failure shows it is stale. After a timeout or partial write, read the existing target and finish only missing portions; never create another item to bypass uncertainty. Record unresolved operations and next action in the existing work record. Report product evidence separately from failed tracking updates, and do not move to a shadow tracker if the configured location is unavailable.

## Work-item record

```text
ID: WORK-001
Outcome and acceptance references:
Stage: Needs definition
Spec/contract revision or snapshot:
Bounds, interfaces, non-goals:
Authority and execution limits:
Workspace, setup/entrypoint, write ownership, tracker configuration:
Dependencies: ID/path/anchor + required result + accepted artifact/evidence
Blocker/disposition: reason, affected work, clearing condition (or none)
Progress: settled decisions, current artifact/checkpoint, unresolved questions
          or findings, and transition reasons
Next action:
Accepted result location:
Evidence: key; criterion; spec/contract revision; artifact revision/snapshot;
          action/check; expected outcome; observed outcome;
          passed/failed/unverified; material limitations
Unfinished tracker operation and next reconciliation action:
```

Keep only useful fields; existing equivalent records need not be reformatted. Partial preparation remains Needs definition with settled answers preserved. Resume interrupted Building work or Verifying checks in place. Ready can wait for a known implementation dependency, but a contract dependent on an unanswered consequential decision still needs definition.
