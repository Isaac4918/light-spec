---
name: validate-feature-list
description: 'Audit feature_list.json for conflicts, weak modeling, missing gaps, and bad priority order, then apply approved corrections only.'
argument-hint: 'Optionally include domain context, priorities, or backlog constraints'
user-invocable: true
---

# Validate Feature List

Review the backlog after it already contains features. Follow [workflow_rules.md](../../../workflow_rules.md).

## Flow

1. Validate `feature_list.json`, `constitution.md`, and `code_standards.md`.
2. Read `memory/history.md` and `memory/current.md` when available.
3. Find one inconsistency at a time and explain why it matters.
4. Ask for approval before writing each correction, then apply it immediately if approved.
5. After internal inconsistencies are closed, suggest justified missing gaps and then propose a final priority order.

## Prerequisites

- A valid non-empty `feature_list.json` must exist.
- `constitution.md` and `code_standards.md` must exist.
- If memory is available, review it; if it is missing, continue the analysis without it.

## Rules

- Stop if `feature_list.json` is missing, incomplete, or empty.
- Do not suggest generic checklist features without evidence from the product, rules, or code.
- If a feature overlaps or contradicts another, propose a concrete merge, split, reopen, or rewrite.
- If `rules.require_tests_to_close` is true, include a testing acceptance criterion and name the test file.

## Final behavior

Report the inconsistencies found, which were corrected or left unchanged, any new or reopened features, and the recommended or applied backlog order.