# GitHub tracker configuration

Copy into the project's existing configuration location or `docs/agents/issue-tracker.md`, then reference it from agent instructions. Replace project constants with observed values and retain only the selected stage/dependency routes. This is a template, not completed setup or evidence that writes have been tested. Use the available connector or CLI; if replacing the CLI recipes below, save equally concrete tool names, arguments, and readback calls.

## Destination and conventions

- Repository: `HOST/OWNER/REPO` and exact URL.
- Authoritative spec: exact path/URL and version/snapshot convention.
- Outcome coverage and derived parent progress: existing spec section or parent issue URL.
- Tool/access: selected connector or `gh` version; existing credential mechanism by reference only; supported operations and known limits.
- Evidence: item comments or an existing exact evidence location linked from each issue. Identify criterion, spec revision, artifact identity, check, expected/observed result, limitations, and passed/failed/unverified outcome.
- Work key: project-unique stable key in title/body, allocated before creation, such as `WORK-001`. Retain the resulting issue URL/number in the existing coverage record. Do not maintain a second item-status database.
- Scratch body/evidence files: actual permitted workspace path; these are write payloads, not another tracker.
- Blockers/dispositions: record reason, affected work, clearing condition, and next action in the issue. Cancelled or deferred work is never Done; reuse existing project dispositions.

## One stage source

Use an existing Project status field if it can preserve all five distinct meanings and the available tool can read/write it. Save the exact project owner, number, URL/node ID, field name/ID, and five option names/IDs. Account for existing automation that affects that field. Otherwise use one mutually exclusive label set; do not create a Project solely for this workflow or mirror stage in both representations.

| Workflow stage | Selected field option name/ID **or** exact label |
| --- | --- |
| Needs definition | Fill from existing suitable field, or `stage:needs-definition` |
| Ready | Fill from existing suitable field, or `stage:ready` |
| Building | Fill from existing suitable field, or `stage:building` |
| Verifying | Fill from existing suitable field, or `stage:verifying` |
| Done | Fill from existing suitable field, or `stage:done` |

For labels, save the actual five names and ensure they exist through authorized setup. If creation is needed, a CLI recipe is `gh label create LABEL --repo HOST/OWNER/REPO --color HEX --description DESCRIPTION`. Read back with `gh label list --repo HOST/OWNER/REPO --limit LIMIT --json name,color,description`, using a limit that covers the relevant labels. Keep unrelated labels intact.

Stage changes belong to the coordinator under the skill's assignment and acceptance rules. A closed issue, merged PR, or label alone is not accepted prerequisite evidence. Keep historical transition reasons in the issue without maintaining another current-stage field in its body.

## Selected operations

Replace `HOST/OWNER/REPO` and Project constants with configured values in these recipes. `ITEM_URL`, `ITEM_KEY`, `BODY_FILE`, `EVIDENCE_FILE`, and `DEPENDENCY_URL` are per-item inputs from the saved record or prepared payload. Quote values appropriately; write multiline bodies to files rather than interpolating them into shell commands. Read current content before updating it, preserving unrelated edits.

| Operation | CLI recipe and required result |
| --- | --- |
| Find/reconcile creation | `gh issue list --repo HOST/OWNER/REPO --state all --search 'ITEM_KEY in:title,body' --limit LIMIT --json number,url,title,body,state` and inspect the exact key. Search absence or a truncated list cannot justify retrying an uncertain create. If needed, use `gh api --hostname HOST --paginate -X GET repos/OWNER/REPO/issues -f state=all -f per_page=100` and match the exact key in returned issues; if still uncertain, leave the operation outstanding. |
| Read current item | `gh issue view ITEM_URL --repo HOST/OWNER/REPO --json number,url,title,body,state,stateReason,labels,comments,projectItems`. Read the saved dependency representation as well. |
| Create | `gh issue create --repo HOST/OWNER/REPO --title 'ITEM_KEY: TITLE' --body-file BODY_FILE`. Preserve the returned URL; read it back, then apply the selected stage route. Creation plus stage assignment is a multi-part operation. |
| Update brief/progress/blocker | `gh issue edit ITEM_URL --repo HOST/OWNER/REPO --body-file BODY_FILE`, then read the item and verify the intended change. |
| Save acceptance evidence | `gh issue comment ITEM_URL --repo HOST/OWNER/REPO --body-file EVIDENCE_FILE`. Read the comments back; use a stable evidence key to reconcile an uncertain write before posting again. |
| Finish | After acceptance, save evidence, set Done using the selected route, and `gh issue close ITEM_URL --repo HOST/OWNER/REPO --reason completed`. Read back evidence, selected stage, and issue disposition. Track any failed portion separately from product acceptance. |
| Reopen invalidated acceptance | `gh issue reopen ITEM_URL --repo HOST/OWNER/REPO`, update the reason/affected evidence, and set the appropriate stage. Read back; do not reopen merely for a cosmetic preference. |

Retain **one** stage-operation block:

- **Project field:** Save `PROJECT_OWNER`, `PROJECT_NUMBER`, `PROJECT_ID`, `FIELD_ID`, and each `OPTION_ID` once. Add a new issue with `GH_HOST=HOST gh project item-add PROJECT_NUMBER --owner PROJECT_OWNER --url ITEM_URL --format json`; retain the returned `ITEM_ID`. Set stage with `GH_HOST=HOST gh project item-edit --project-id PROJECT_ID --id ITEM_ID --field-id FIELD_ID --single-select-option-id OPTION_ID`. Read back using `GH_HOST=HOST gh project item-list PROJECT_NUMBER --owner PROJECT_OWNER --field-id FIELD_ID --format json --limit LIMIT`, matching the exact issue URL/item ID and configured field value. Ensure the listing covers that item; a truncated list is not proof of absence. Save the supported readback's field mapping during setup. Do not apply stage labels.
- **Labels:** Set the next label and remove all other labels in the configured stage set with `gh issue edit ITEM_URL --repo HOST/OWNER/REPO --add-label NEXT_LABEL --remove-label OTHER_STAGE_LABELS`. `OTHER_STAGE_LABELS` is the comma-separated set excluding the next label. Read the issue back and require exactly one configured stage label with the expected value; repair only the missing portion after partial success. Do not mirror stage to a Project field.

For Project CLI calls, `HOST` selects the configured host through `GH_HOST`; replace it alongside the exact owner/number/IDs. If using a connector, save its corresponding host and project arguments. A destination is not fully specified by a project number alone.

Retain **one** dependency-operation block:

- **Native links, when supported:** Add with `gh issue edit ITEM_URL --repo HOST/OWNER/REPO --add-blocked-by DEPENDENCY_URL`; read with `gh issue view ITEM_URL --repo HOST/OWNER/REPO --json blockedBy,blocking`. Save a supported removal operation, such as `--remove-blocked-by DEPENDENCY_URL`, for corrections. The brief identifies the required result and acceptance evidence, not only its issue URL.
- **Explicit referenced list:** In the issue body, save each dependency URL, required result/interface, and accepted artifact/evidence pointer. Update/read it using the body operations above. A checked box or closed issue cannot substitute for the required result.

If any recipe is unsupported by the selected tool, replace it with a verified available operation or record the precise missing capability. Do not leave generic commands as though setup were complete. Reuse saved configuration; repair only concretely stale portions. For timeouts or partial operations, read back first and finish only what is missing. An unavailable destination does not authorize a shadow tracker.

## Issue body

Use this compact record with the existing spec; omit unused fields rather than manufacturing detail. The chosen field/label carries current stage.

```text
Work key and outcome:
Spec revision and acceptance references:
Bounds, interfaces, non-goals:
Authority and execution limits:
Workspace, setup/entrypoint, write ownership, tracker configuration:
Dependencies and required accepted results/evidence:
Blocker or disposition: reason, affected work, clearing condition
Progress: settled decisions, current artifact/checkpoint, unresolved findings
Next action:
Evidence links: criterion + spec revision + artifact + check + expected/observed
                + passed/failed/unverified + limitations
Transition reasons and any unfinished tracker operation:
```
