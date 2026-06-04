---
name: adapt-old-project
description: 'Adapt an existing project to the workflow by mapping real capabilities, choosing the reference architecture, and creating the missing backlog, memory, and spec artifacts with approval.'
argument-hint: 'Describe the legacy project and, if known, whether to align it to Option A or B'
user-invocable: true
---

# Adapt Old Project

Adapt an existing project to the backlog/spec/memory workflow. Follow [workflow_rules.md](../../../workflow_rules.md) and the project constitution and standards.

## Use it when

- formalizing a project that already has code but no `feature_list.json`;
- creating backlog, `memory/`, and specs from an existing system;
- deciding whether the project fits Option A or Option B;
- documenting already implemented capabilities before `/implement-feature` or `/sync-docs`.

## Sources and limits

Primary sources are the whole workspace, real code, folder structure, entry points, config, tests, docs, `constitution.md`, and `code_standards.md`. Read `README.md` and `docs/` only as context. Do not modify `README.md`, do not implement new business capabilities, and do not move folders or refactor structurally without approval.

Before planning, check whether `feature_list.json`, `specs/`, `memory/`, `constitution.md`, and `code_standards.md` already exist.

## Prerequisites

- A real workspace with enough code to inspect capabilities must exist.
- `constitution.md` and `code_standards.md` must exist.
- If `feature_list.json` already exists, treat it as an adaptation base rather than an empty template.

## Required confirmations

Ask for explicit confirmation of:

- Option A or Option B from `code_standards.md`;
- preserve current structure gradually or converge more aggressively;
- approved, rejected, or pending optional stack pieces;
- whether to formalize only `done` and `in_progress` work or also new `pending` work;
- any special rule for splitting or grouping features.

## Main flow

1. Inventory the workspace and identify entry points, modules, tests, templates, assets, and docs.
2. Read `constitution.md` and `code_standards.md` to set the criteria.
3. Review enough code to identify real capabilities, partial work, and feature boundaries.
4. Ask the architecture and stack confirmations above.
5. Propose well-bounded features with `status`, `sdd`, and acceptance criteria.
6. Ask for approval before any material write.
7. Create or update `feature_list.json`, `memory/current.md`, `memory/history.md`, feature memory files, and `specs/<feature_name>/` as needed.
8. Validate consistency across architecture, backlog, memory, and specs.
9. Summarize what was adapted and what debt remains.

## Feature rules

- Build features from real capabilities, not one file per technical artifact.
- Group related code into one feature when it is one capability; split only when a capability is clearly broad.
- Use `done` for clearly implemented capabilities, `in_progress` for partial or drifting ones, `pending` for missing work, and `spec_ready` only when a non-finished feature has an approved spec.
- Do not create or update backlog, memory, or specs without human approval.

## Shared workflow reuse

Use `/add-feature` for backlog registration, `/create-spec` for missing specs, `/validate-feature-list` for backlog cleanup, and `/sync-docs` when the code already exists and the task is documentary.

## Final behavior

Report the analyzed workspace areas, chosen architecture, stack confirmation status, formalized feature statuses, files created or updated, evidence used, remaining workflow debt, and the next natural step.