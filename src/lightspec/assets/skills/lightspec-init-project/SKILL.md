---
name: lightspec-init-project
description: 'Initialize a new project from a short description, confirm the target architecture and rules, and create the base structure plus an empty feature_list.json.'
argument-hint: 'Describe the project and include its name if you already have one'
user-invocable: true
---

# Init Project

Initialize a new project. Follow [workflow_rules.md](../../../workflow_rules.md).

## Prerequisites

- The project name and a short functional description must be available.
- The architecture and rules must be confirmable before files are created. Propose suitable architecture options to the user (for example a single-purpose application or a multi-module platform) and let the user choose; do not assume one.
- `constitution.md` and `code_standards.md` must remain available at the workspace root, because downstream workflow skills depend on them.

## Flow

1. Ask for the name, description, architecture, and rules if anything is missing.
2. Suggest architecture options that fit the described project and confirm the chosen one with the user instead of assuming it.
3. Create the matching base structure with clear separation of responsibilities.
4. Generate an empty `feature_list.json` from the template.
5. Confirm that `constitution.md` and `code_standards.md` are still present and that the workspace is ready for the next workflow skills.
6. Validate and summarize what was created.

## Evidence it produces

- Initial `feature_list.json`.
- Base project structure.
- Captured architecture and rule decisions for the rest of the workflow.
- A workspace that remains ready for `add-feature`, `create-spec`, `implement-feature`, `validate-feature-list`, and `validate-standards`.

## Final

Report the chosen architecture, captured rules, created folders, and the path to `feature_list.json`.
