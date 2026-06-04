---
name: create-spec
description: 'Create or update concise specs for pending backlog features with sdd: true, then move complete specs to spec_ready.'
argument-hint: 'Optionally provide extra context about the features or project constraints'
user-invocable: true
---

# Create Spec

Create specs for eligible features. Follow [workflow_rules.md](../../../workflow_rules.md).

## Eligible features

- `status: pending`
- `sdd: true`

## Prerequisites

- A valid `feature_list.json` must exist.
- `constitution.md` and `code_standards.md` must exist.
- At least one eligible feature with `status: pending` and `sdd: true` must exist.
- If the feature already has a spec, the user must approve the update before writing.

## Flow

1. Validate `feature_list.json`, `constitution.md`, and `code_standards.md`.
2. Filter eligible features and read any existing spec plus relevant memory.
3. Ask only for the minimum missing details needed to write the spec.
4. If a spec already exists, ask for approval before changing it.
5. Create or update `requirements.md`, `design.md`, and `tasks.md` under `specs/<feature_name>/`.
6. If complete, set the feature status to `spec_ready`.

## Rules

- Requirements must be numbered, verifiable, and written as behavior.
- Design must explain how the feature will be built and include at least one rejected alternative.
- Tasks must be an executable checklist with code, tests, and validation.
- Do not assume unconfirmed stack pieces; ask before locking them into the design.
- Do not overwrite an existing approved spec without human approval.

## Final behavior

Report which features were processed, which were skipped and why, which spec folders changed, and which features moved to `spec_ready`.