---
name: implement-feature
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
4. If the feature has `sdd: true`, read its spec first; if the spec is incomplete, stop.

## Prerequisites

- A valid `feature_list.json` must exist.
- `constitution.md` and `code_standards.md` must exist.
- If the feature is `sdd: true`, its spec must already be complete and available.
- If a feature is already `in_progress`, continue that one before starting another.

## Templates

- `assets/current.template.md` for `memory/current.md`.
- `assets/feature-memory.template.md` for `memory/<feature-name>.md` per-feature implementation memory.
- `assets/history.template.md` for `memory/history.md`.

## Flow

1. Read `memory/current.md` and `memory/history.md` if they exist.
2. Mark the selected feature as `in_progress` and update `feature_list.json`.
3. Read only the code needed for the current feature plus the required memory and spec files.
4. Implement the smallest verifiable change, then validate each acceptance criterion.
5. Add or complete tests under `tests/` when appropriate and run the relevant test suite.
6. If tests pass, mark the feature as `done`, update feature memory and history, and clear `memory/current.md`.

## Rules

- Implement exactly one feature at a time.
- Do not assume optional stack pieces unless they were explicitly confirmed.
- Do not broaden scope or fix unrelated problems.
- Keep `memory/current.md` in sync with real progress.

## Final behavior

Report the feature implemented, main files changed, whether dependencies were added, which tests ran, and whether the status changed to `done`.