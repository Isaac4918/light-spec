---
name: sync-docs
description: 'Synchronize backlog, specs, memory, and allowed docs with the real codebase without changing source code.'
argument-hint: 'Optionally specify the project area, module, or documentation scope to reconcile first'
user-invocable: true
---

# Sync Docs

Synchronize documentation with the real implementation. Follow [workflow_rules.md](../../../workflow_rules.md).

## Flow

1. Identify which documentation artifacts exist and read `feature_list.json`, `memory/`, `README.md`, `docs/`, and `specs/` when present.
2. Read only the code needed to confirm the real state.
3. Detect divergences between code, backlog, specs, memory, and general docs.
4. Propose documentation-only fixes and ask for approval before writing.
5. If the code contains undocumented features, ask whether the user wants to formalize them through the workflow.
6. If the user approves formalization, ask permission to run `/add-feature` first, then `/validate-feature-list` if backlog cleanup is needed, then `/create-spec` when the feature should use `sdd: true`.
7. Update allowed documentation and memory after the approved workflow steps complete.

## Prerequisites

- Real project code must exist so documentation can be compared against implementation.
- The relevant formal artifacts must exist or at least be verifiable: `feature_list.json`, `specs/`, `memory/`, `constitution.md`, `code_standards.md`, and any general documentation that is present.
- If `feature_list.json` is missing, this skill does not invent it; it only reports the absence and routes the user to the appropriate workflow.

## Rules

- Do not modify source code or `README.md`.
- Respect existing specs as controlled artifacts and do not silently rewrite them.
- If the user approves formalization of undocumented code, ask permission before each workflow skill you run.

## Final behavior

Report which artifacts were reviewed, which divergences were found, which files were synchronized, which skills were executed or left pending, and what remains misaligned.