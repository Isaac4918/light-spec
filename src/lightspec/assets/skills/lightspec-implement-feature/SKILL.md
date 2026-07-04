---
name: lightspec-implement-feature
description: 'Implement exactly one feature at a time, using specs when required, updating working memory, and closing only after tests pass.'
argument-hint: 'Optionally provide the feature id, name, or a close description, plus constraints or technical decisions'
user-invocable: true
---

# Implement Feature

Implement one feature at a time. Follow [workflow_rules.md](../../../workflow_rules.md).

## Selection

1. If a feature is already `in_progress`, continue it.
2. Otherwise choose the next implementable feature by backlog order.
3. If the user selected a feature explicitly and it is valid, honor that selection.
4. A feature is implementable only from `pending` when `sdd: false`, or from `spec_ready` when `sdd: true`.
5. If the feature has `sdd: true`, read its spec first; if the spec is incomplete or the status is not `spec_ready`, stop.

## Prerequisites

- A valid `feature_list.json` must exist.
- `constitution.md` and `code_standards.md` must exist.
- If the feature is `sdd: true`, its spec must already be complete and available.
- If the feature is `sdd: false`, it must still be `pending` before implementation starts.
- If a feature is already `in_progress`, continue that one before starting another.

## Templates

- `assets/current.template.md` for `memory/current.md`.
- `assets/feature-memory.template.md` for `memory/<feature-name>.md` per-feature implementation memory.
- `assets/history.template.md` for `memory/history.md`.

## Flow

1. Read `memory/current.md` and `memory/history.md` if they exist.
2. Validate that no other feature is already `in_progress`.
3. Mark the selected feature as `in_progress` and update `feature_list.json`.
4. Read only the code needed for the current feature plus the required memory and spec files.
5. Implement the smallest verifiable change, then map each acceptance criterion to explicit closure evidence: automated test, manual reproducible check, or both.
6. Add or complete tests under `tests/` when appropriate, preferring the narrowest test layer that gives credible coverage for the changed behavior.
7. Isolate external integrations with doubles where practical; if real integration validation is still required, keep it narrow and reproducible.
8. Run the relevant test suite and any required manual reproducible check.
9. If validation passes, mark the feature as `done`, update `last_validated_at` and `validation_summary`, update feature memory and history, and clear `memory/current.md`.

## Rules

- Implement exactly one feature at a time.
- Do not move a feature directly from `pending` to implementation when `sdd: true`; it must already be `spec_ready`.
- Do not assume optional stack pieces unless they were explicitly confirmed.
- Do not broaden scope or fix unrelated problems.
- Do not treat a vague or partial test run as sufficient closure evidence.
- Before moving to `done`, record which acceptance criteria were covered by automated tests and which were validated another way.
- If no automated test is added for changed business behavior, explain why and use a reproducible manual check instead of an implicit exception.
- Keep `memory/current.md` in sync with real progress.

## Final behavior

Report the feature implemented, the starting status, main files changed, whether dependencies were added, which tests ran, which manual checks were used if any, how acceptance coverage was demonstrated, whether validation metadata changed, and whether the status changed to `done`.