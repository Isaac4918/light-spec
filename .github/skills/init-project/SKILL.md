
---
name: init-project
description: 'Initialize a new project from a short description, validate Python 3.12+, confirm architecture and stack, and create the base structure plus an empty feature_list.json.'
argument-hint: 'Describe the project and include its name if you already have one'
user-invocable: true
---

# Init Project

Initialize a new project. Follow [workflow_rules.md](../../../workflow_rules.md).

## Prerequisites

- A valid Python environment using `conda` or `venv` with Python 3.12+ must be available.
- The project name and a short functional description must be available.
- The architecture, rules, and initial stack must be confirmable before files are created.
- `constitution.md` and `code_standards.md` must remain available at the workspace root, because downstream workflow skills depend on them.

## Flow

1. Validate the Python environment.
2. Ask for the name, description, architecture, rules, and stack if anything is missing.
3. Create the matching base structure.
4. Generate an empty `feature_list.json` from the template.
5. Confirm that `constitution.md` and `code_standards.md` are still present and that the workspace is ready for the next workflow skills.
6. Validate and summarize what was created.

## Evidence it produces

- Initial `feature_list.json`.
- Base project structure.
- Captured rules and stack decisions for the rest of the workflow.
- A workspace that remains ready for `add-feature`, `create-spec`, `implement-feature`, `validate-feature-list`, and `validate-standards`.

## Final

Report the validated Python environment, chosen architecture, stack confirmations, created folders, captured rules, and the path to `feature_list.json`.
