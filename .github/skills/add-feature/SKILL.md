---
name: add-feature
description: 'Add or update features in feature_list.json without implementing code, handling duplicates, increments, splits, and reopenings with user approval.'
argument-hint: 'Describe the feature you want to add to feature_list.json'
user-invocable: true
---

# Add Feature

Add or update features in `feature_list.json`. Use [feature_template.json](./assets/feature_template.json) as the base template and follow [workflow_rules.md](../../../workflow_rules.md).

## Use it when

- adding a new feature or reopening an existing one;
- recording an increment over an existing feature;
- deciding whether a request should be split into several features;
- checking duplicates, contradictions, or overlaps before writing.

## Prerequisites

- A valid `feature_list.json` created by `init-project` or `adapt-old-project` must exist.
- The file must contain `project`, `description`, `rules`, and `features`.
- If it is missing or incomplete, run `/init-project` or `/adapt-old-project` first.

## Flow

1. Validate `feature_list.json` and use the user prompt as the primary source.
2. Ask for the description if it is missing, decide whether the request is one feature or several, and review duplicates, increments, and contradictions.
3. If the request appears composite, explain why, propose how each resulting feature would be written using the template, show that draft in chat, and ask for approval.
4. Ask for acceptance criteria if they are missing or weak; if the feature is incomplete, suggest concrete observable criteria.
5. Always ask whether the feature will use `sdd`, and never assume `true` or `false`.
6. If tests are required by project rules, add a testing criterion and suggest `tests/test_<feature_name_snake_case>.py`.
7. Generate `title` and `name` in `kebab-case`, write the final entry with `status: pending`, or reopen a `done` feature as `pending` when that is the approved outcome.
8. Validate the JSON and summarize the result.

## Rules

- Do not implement code or modify application folders.
- Do not write if `feature_list.json` is missing or incomplete, or if a conflict, ambiguity, or reopening is still unconfirmed.
- If an existing `done` feature shares the same scope, use it as the base unless the user approves a new feature.
- If the user asks to merge features, show the proposed JSON first and ask for explicit confirmation.

## Final behavior

State whether the feature was added, updated, split, merged, reopened, or left unwritten; include `id`, `name`, `title`, whether a test criterion was added, and confirm that any new or reopened entry ended in `pending`.