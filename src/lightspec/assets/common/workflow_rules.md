# Shared Workflow Rules

Use this file as the compact reference for rules repeated across skills and standards.

## Cross-cutting rules
- Treat `feature_list.json` as the formal backlog and `memory/` as auxiliary context.
- Read only the code or docs strictly needed for the current task.
- Do not modify `README.md`.
- Ask for human approval before any material write, backlog change, reopening, spec update, or architectural decision.
- Keep changes small, local, and verifiable.
- If a task needs a technology or architecture choice, confirm it explicitly instead of assuming it.
- If a decision affects architecture, cost, security, data, or operations, stop and ask.
- Prefer one feature, one correction, or one work stream at a time unless the workflow explicitly allows more.

## Architecture
- The target architecture is proposed to the user per project and confirmed before files are created; it is not fixed here.
- Keep presentation, domain logic, and integrations separated regardless of the chosen architecture.

## Reporting
- Summaries should say what was changed, what was validated, what is blocked, and what remains pending.

## Feature state model

### Canonical states

- `pending`: approved and registered in the backlog, not currently being implemented.
- `spec_ready`: `sdd: true` feature with a complete approved spec, ready to start implementation.
- `in_progress`: the single feature currently being implemented.
- `done`: implemented and validated for closure.

### State metadata

- Blocking is metadata, not a backlog state. Use `blocked: true|false` and `blocker_reason` when needed.
- Reopen context is metadata, not a backlog state. Use `reopen_count` and `reopen_reason` when a closed feature returns to the backlog.
- Validation evidence should stay explicit through `last_validated_at` and `validation_summary`.

### Allowed transitions

- `pending -> spec_ready`: only when `sdd: true` and the spec is complete.
- `pending -> in_progress`: only when `sdd: false` and no other feature is already `in_progress`.
- `spec_ready -> in_progress`: only when `sdd: true`, the spec is still valid, and no other feature is already `in_progress`.
- `in_progress -> done`: only when acceptance coverage is complete and the required validation has passed.
- `done -> pending`: only when a human explicitly approves reopening and the reopen reason is recorded.

### Invariants

- At most one feature may be `in_progress` at any time.
- Every feature with `sdd: true` must pass through `spec_ready` before implementation.
- No feature may move directly from `pending` to `done` or from `spec_ready` to `done`.
- A blocked feature keeps its main backlog state and records the blocker separately.
- Reopening always returns the feature to `pending`; it does not restore `spec_ready` automatically.
- If `rules.require_tests_to_close` is true, a feature cannot move to `done` without passing the relevant tests.

## Skill prerequisites

- `init-project`: project name, functional description, confirmed architecture choice, and rules.
- `adapt-old-project`: workspace with real code and enough context to inspect the project, plus `constitution.md` and `code_standards.md`.
- `add-feature`: valid `feature_list.json` created by `init-project` or `adapt-old-project`.
- `create-spec`: valid `feature_list.json`, `constitution.md`, and `code_standards.md`, plus at least one eligible `pending` feature with `sdd: true`.
- `implement-feature`: valid `feature_list.json`, `constitution.md`, and `code_standards.md`; if the feature is `sdd: true`, its spec must already exist.
- `sync-docs`: real project code plus the formal docs and backlog artifacts needed to compare reality against them.
- `validate-feature-list`: valid non-empty `feature_list.json` plus `constitution.md` and `code_standards.md`.
- `validate-standards`: `constitution.md`, `code_standards.md`, and relevant code.