# Shared Workflow Rules

Use this file as the compact reference for rules repeated across skills and standards.

## Cross-cutting rules
- Treat `feature_list.json` as the formal backlog and `memory/` as auxiliary context.
- Read only the code or docs strictly needed for the current task.
- Do not modify `README.md`.
- Ask for human approval before any material write, backlog change, reopening, spec update, or architectural decision.
- Keep changes small, local, and verifiable.
- If a task needs a stack choice, confirm each optional piece instead of assuming it.
- If a decision affects architecture, cost, security, data, or operations, stop and ask.
- Prefer one feature, one correction, or one work stream at a time unless the workflow explicitly allows more.

## Architecture and stack
- Option A: single-purpose application.
- Option B: multi-module platform.
- Optional stack pieces are always optional: Azure AI Foundry, Azure Cognitive Services, Azure AI Search, Azure Cosmos DB, Azure SQL, Azure Blob Storage or Azure Storage Account, and a basic HTML/CSS/JavaScript frontend with Jinja2Templates.

## Frontend
- Use plain CSS unless an exception is explicitly approved.
- Keep UI, domain logic, and integrations separated.

## Reporting
- Summaries should say what was changed, what was validated, what is blocked, and what remains pending.

## Skill prerequisites

- `init-project`: valid Python 3.12+ environment, project name, functional description, architecture choice, rules, and stack confirmations.
- `adapt-old-project`: workspace with real code and enough context to inspect the project, plus `constitution.md` and `code_standards.md`.
- `add-feature`: valid `feature_list.json` created by `init-project` or `adapt-old-project`.
- `create-spec`: valid `feature_list.json`, `constitution.md`, and `code_standards.md`, plus at least one eligible `pending` feature with `sdd: true`.
- `implement-feature`: valid `feature_list.json`, `constitution.md`, and `code_standards.md`; if the feature is `sdd: true`, its spec must already exist.
- `sync-docs`: real project code plus the formal docs and backlog artifacts needed to compare reality against them.
- `validate-feature-list`: valid non-empty `feature_list.json` plus `constitution.md` and `code_standards.md`.
- `validate-standards`: `constitution.md`, `code_standards.md`, and relevant code.