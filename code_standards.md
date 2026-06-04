# Code Standards

Apply the constitution and [workflow_rules.md](workflow_rules.md).

## 1. Naming and style

- Use `snake_case` for Python functions, variables, modules, and files.
- Use `PascalCase` for classes.
- Prefer names that describe intent.
- Avoid ambiguous abbreviations unless they are domain standard.
- Do not mix naming styles without explicit reason.

## 2. Core engineering principles

- Apply YAGNI, KISS, DRY, and SOLID pragmatically: solve the current problem with the simplest clear design, avoid duplicated rules, and keep each module or service focused.
- When these principles conflict, favor clarity, maintainability, and the current project scope over theoretical purity.

## 3. Preferred base structure

- Option A for one main domain: `app/src/api/routes/`, `app/src/models/`, `app/src/services/`, `app/src/ai/`, `app/src/infrastructure/` or `app/src/clients/`, `app/src/config/`, `app/src/utils/`, `tests/`, `docs/`, `cicd/`.
- Option B for real modular platforms: `main.py` and `requirements.txt` when needed, `platform/` for shared concerns, `modules/<module>/{domain,data,web,templates}/`, `tests/`, `cicd/`.
- Use Option A for one main domain; use Option B only when the business is truly modular; do not choose Option B for speculative growth.
- If another structure is required, preserve equivalent separation of responsibilities and justify the deviation.

## 4. Boundaries

- Frontend is for presentation, interaction flow, local UI state, form handling, rendering, accessibility, and safe display of backend responses.
- Frontend must not contain authoritative business rules, persistence logic, security decisions, or direct access to protected infrastructure.
- Backend is for business rules, input validation, authorization, orchestration, persistence, integration with external systems, and final enforcement of security and data integrity.
- Client-side validation may improve usability, but backend validation stays authoritative.
- Secrets, connection details, privileged tokens, and provider credentials must stay on the backend.
- If a web UI exists, use plain CSS only.

## 5. Endpoints, models, services, and integrations

- Endpoints may validate input, call services, transform responses, and map errors, but they must not hold complex business logic or direct infrastructure access.
- Every API input and output must have an explicit model.
- Services encapsulate business rules and orchestration and must not depend on HTTP transport details.
- Wrap every external integration behind a clear client or interface.
- Integration code must handle timeouts, transient failures, and useful minimum logging.

## 6. Configuration, errors, and observability

- Centralize configuration through environment variables and typed settings.
- Never hardcode secrets, model names, keys, connection strings, index names, or sensitive endpoints.
- Map errors to the correct HTTP status codes and keep client messages safe.
- Use consistent logging; do not use `print` for diagnostics.
- Every request must be correlatable through a `request_id`, and logs should include method, route, result, and duration.

## 7. AI, Azure, tests, and security

- Every AI feature must define purpose, expected input, expected output, limits, fallback strategy, prompt versioning, and minimum evaluation.
- Treat model output as untrusted until validated against domain rules.
- Azure services are optional and require explicit confirmation before use or assumption.
- New dependencies need clear technical justification; prefer small, decoupled integrations.
- New business logic must have tests proportional to risk, and AI or external integrations should use repeatable checks or doubles where practical.
- Apply least privilege, explicit CORS, reasonable timeouts, and safe data handling.

## 8. Agent-made changes

- Keep changes small and directly justified.
- Prefer root-cause fixes over superficial patches.
- Do not create new layers, folders, or services unless the problem requires them.
- Stop and ask a human if a decision affects infrastructure, cost, security, data, or compliance.

## 9. Minimum acceptance checklist

Before closing a change, verify that responsibilities are separated, contracts are explicit, secrets and hardcoded configuration were not introduced, error handling is safe, logging or observability exists, any web frontend uses plain CSS, AI changes include control and evaluation, and any stack choice used was explicitly confirmed.