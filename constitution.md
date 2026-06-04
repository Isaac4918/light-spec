# Team Constitution

This document defines the non-negotiable rules for Python/FastAPI software with optional AI and Azure integrations. When in doubt, prefer the simplest, safest, most maintainable, and most observable option.

## Goal

Build readable, secure, maintainable, production-ready software while avoiding implicit decisions and reducing technical risk across web, API, and AI integrations. Shared workflow details live in [workflow_rules.md](workflow_rules.md).

## Mandatory principles

1. Clarity over complexity: code must be easy to read, review, and change.
2. Strict separation of responsibilities: HTTP validates and delegates; business logic stays in services; external systems stay behind adapters or clients.
3. Explicit contracts and typing: public interfaces, request models, and response models must be clear and consistent.
4. Secure by default: never hardcode secrets or sensitive endpoints; validate input; keep client-facing errors safe.
5. Required observability: requests must be traceable, logs must be useful, and integrations must expose latency, failures, and degraded behavior.
6. AI with explicit control: AI features need defined purpose, limits, inputs, outputs, and minimum evaluation criteria.
7. Technology decisions require human approval: managed services and architecture-affecting choices need explicit confirmation.
8. Verifiable quality: every change must be checkable through tests, local validation, or clear observable criteria.

## System design rules

- APIs should use HTTP resources and verbs consistently and expose a stable, lightweight health check endpoint.
- Configuration must stay centralized and environment-driven.
- Every new dependency needs clear technical justification.
- Web frontend styling should use plain CSS unless an exception is explicitly approved.

## Rules for coding agents

- Prefer small, localized, verifiable changes.
- Do not invent requirements, folders, services, or conventions.
- Ask before making decisions that change scope, infrastructure, cost, security, or business rules.
- Preserve project structure and align with these principles before optimizing or refactoring.

## Operational definition of compliance

A change complies when it keeps API, services, and integrations separated; uses clear names and explicit contracts; avoids secrets and internals; includes reasonable error handling and observability; treats AI as a controlled, evaluable component; uses plain CSS for web frontend unless approved otherwise; and does not introduce Azure services without human approval when the decision is architectural.