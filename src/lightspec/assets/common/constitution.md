# Team Constitution

This document defines the non-negotiable rules for building software in this project, independent of language, framework, or platform. When in doubt, prefer the simplest, safest, most maintainable, and most observable option.

## Goal

Build readable, secure, maintainable, production-ready software while avoiding implicit decisions and reducing technical risk. Shared workflow details live in [workflow_rules.md](workflow_rules.md).

## Mandatory principles

1. Clarity over complexity: code must be easy to read, review, and change.
2. Strict separation of responsibilities: keep presentation, business logic, and access to external systems in distinct, well-bounded layers.
3. Explicit contracts and typing: public interfaces, inputs, and outputs must be clear and consistent.
4. Secure by default: never hardcode secrets or sensitive endpoints; validate input; keep user-facing errors safe.
5. Required observability: important operations must be traceable, logs must be useful, and integrations must expose latency, failures, and degraded behavior.
6. Technology decisions require human approval: architecture, dependencies, and platform choices that affect scope, cost, or risk need explicit confirmation.
7. Verifiable quality: every change must be checkable through tests, local validation, or clear observable criteria.

## System design rules

- Keep responsibilities separated so presentation, domain logic, and integrations can evolve independently.
- Configuration must stay centralized and environment-driven.
- Every new dependency needs clear technical justification.
- Expose a stable, lightweight health or status signal for long-running services when applicable.

## Rules for coding agents

- Prefer small, localized, verifiable changes.
- Do not invent requirements, folders, services, or conventions.
- Ask before making decisions that change scope, infrastructure, cost, security, or business rules.
- Preserve project structure and align with these principles before optimizing or refactoring.

## Operational definition of compliance

A change complies when it keeps presentation, business logic, and integrations separated; uses clear names and explicit contracts; avoids exposing secrets or internal details; includes reasonable error handling and observability; is verifiable through tests or observable criteria; and does not introduce architectural, cost, or platform decisions without human approval.
