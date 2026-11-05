# Thought Partner validation

These are development checks, not dependencies of the installed skill. Python 3.9+ is needed only for these helpers. The pack itself is Markdown.

Run structural checks from the repository root:

```text
python3 tests/thought-partner/validate.py thought-partner
```

Use `--archive PATH --extract NEW_DIRECTORY` to freeze a deterministic ZIP, validate CRC/path safety, extract it, and compare every byte. Optional `--before OLD_REPOSITORY --migration NEW_DIRECTORY` tests replacement of both the old `interview/interview-first` and renamed two-file router, with backups outside the active catalog and an unrelated skill preserved. `licenses.json` locks the six full upstream license texts inspected at the revisions recorded in the pack's provenance.

Prepare source-isolated behavioral trials from that exact ZIP:

```text
python3 tests/thought-partner/prepare_trials.py thought-partner.zip trial-workspaces
```

For each case, give a fresh agent only that case root and its `harness.md`. The preparer uses neutral numbered directory names and keeps descriptive assessment IDs in `selections.json`, outside responders' allowed reads. The harness reads the entrypoint and selected references through an audited helper, supplies the realistic user prompt and minimum fixtures, and captures an actual response. Keep `cases.json`, assessment criteria, and any labels implying expected verdicts away from responding agents. For case 27, after the first response, supply the listed follow-up in the same simulated conversation and preserve both responses. Expected criteria guide independent assessment, not generated wording.

Audit archive identity, read hashes, unchanged package bytes, and fixture-edit scope:

```text
python3 tests/thought-partner/audit_trials.py thought-partner.zip trial-workspaces
```

An evidence-valid trial is not automatically a behavioral pass. Independently assess the actual responses, edits, and read paths against the case criteria. Material failures require a focused correction and a fresh replay, then regression coverage. Preserve invalid trials; put fresh replays in `_retries/` under the trial root and record a `selections.json` mapping case IDs to their selected relative replay paths. The auditor honors those selections while retaining original evidence. Do not score verbosity or exact phrasing as correctness when the behavior is sound.

Isolation is explicit and auditable at the source level, not an OS security boundary: fresh subagents can inherit host/system instructions and permissions. The allowed-read helper records the content actually read through it; `audit.json` discloses additional reads/capabilities and is self-reported. Discard contaminated trials. These checks do not prove behavior across all models or products, native slash-menu discovery, or network installer execution. Standalone archive extraction and migration are tested separately from conversational behavior.

A directory/filename inventory is metadata, not a content read. If a responder reports such an inventory in `additional_reads`, inspect the record and preserve an explicit `adjudications.json` entry with `disposition: metadata-only`, the SHA-256 of the exact audit file, and a reason. The auditor permits only that reviewed evidence exception; additional source-content reads require a fresh replay. Do not rewrite a responder's audit to make it pass.
