# Code Standards

Apply the constitution and [workflow_rules.md](workflow_rules.md).

## 1. Naming and style

- Follow the idiomatic naming and formatting conventions of the project's language and toolchain.
- Prefer names that describe intent.
- Avoid ambiguous abbreviations unless they are domain standard.
- Do not mix naming styles within the same codebase without an explicit reason.

## 2. Core engineering principles

- Apply YAGNI, KISS, DRY, and SOLID pragmatically: solve the current problem with the simplest clear design, avoid duplicated rules, and keep each module or component focused.
- When these principles conflict, favor clarity, maintainability, and the current project scope over theoretical purity.

## 3. Structure and separation of responsibilities

- Organize the code around clear separation of responsibilities: presentation, business logic, integrations with external systems, configuration, and tests.
- Keep each responsibility in its own well-bounded area so it can change independently.
- Do not fix a mandatory folder layout here. The concrete architecture is proposed to the user per project (for example a single-purpose application or a multi-module platform) and confirmed before files are created.
- Whatever structure is chosen, preserve equivalent separation of responsibilities and justify any deviation.

## 4. Boundaries

- Presentation is for interaction flow, local UI or client state, input capture, rendering, and safe display of results.
- Presentation must not contain authoritative business rules, persistence logic, security decisions, or direct access to protected infrastructure.
- Business logic is for rules, input validation, authorization, orchestration, persistence, integration with external systems, and final enforcement of security and data integrity.
- Client-side validation may improve usability, but authoritative validation stays on the trusted side.
- Secrets, connection details, privileged tokens, and credentials must stay on the trusted side, never in client-facing code.

## 5. Interfaces, models, services, and integrations

- Entry points (endpoints, handlers, commands) may validate input, call services, transform responses, and map errors, but they must not hold complex business logic or direct infrastructure access.
- Every input and output that crosses a boundary should have an explicit, well-defined shape.
- Services encapsulate business rules and orchestration and must not depend on transport or delivery details.
- Wrap every external integration behind a clear client or interface.
- Integration code must handle timeouts, transient failures, and useful minimum logging.

## 6. Configuration, errors, and observability

- Centralize configuration through environment variables and typed or validated settings.
- Never hardcode secrets, keys, connection strings, or sensitive endpoints.
- Map errors to meaningful results or status codes and keep user-facing messages safe.
- Use consistent logging; do not use ad-hoc console output for diagnostics.
- Make important operations correlatable and include enough context (operation, result, and duration) in logs.

## 7. Tests and security

- New business logic must have tests proportional to risk.
- External integrations should use repeatable checks or doubles where practical.
- New dependencies need clear technical justification; prefer small, decoupled integrations.
- Apply least privilege, reasonable timeouts, and safe data handling.

## 8. Agent-made changes

- Keep changes small and directly justified.
- Prefer root-cause fixes over superficial patches.
- Do not create new layers, folders, or services unless the problem requires them.
- Stop and ask a human if a decision affects infrastructure, cost, security, data, or compliance.

## 9. Minimum acceptance checklist

Before closing a change, verify that responsibilities are separated, contracts are explicit, secrets and hardcoded configuration were not introduced, error handling is safe, logging or observability exists, tests or observable validation cover the changed behavior, and any architecture or dependency choice used was explicitly confirmed.
