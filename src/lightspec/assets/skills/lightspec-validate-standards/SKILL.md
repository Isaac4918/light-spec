---
name: lightspec-validate-standards
description: 'Audit the real codebase against constitution.md and code_standards.md without changing files.'
argument-hint: 'Optionally specify the module, layer, folder, or recent change you want reviewed first'
user-invocable: true
---

# Validate Standards

Compare the real codebase against the standards. Follow [workflow_rules.md](../../../workflow_rules.md).

## Flow

1. Read `constitution.md` and `code_standards.md` first.
2. Extract verifiable criteria from the standards.
3. Read only the code, tests, and config needed to check those criteria.
4. Classify findings by severity and separate confirmed violations from warnings.
5. Report aligned areas, non-aligned areas, and anything that could not be verified objectively.

## Prerequisites

- `constitution.md` and `code_standards.md` must exist.
- Relevant code must exist so compliance can be reviewed.
- If the user names a module or recent change, start there.

## Rules

- Do not modify code or documentation.
- Start with the module or recent change the user named, if any.
- If a standard is too abstract to verify, say so instead of inventing a rule.

## Final behavior

Report the standards used, the code areas reviewed, findings by severity or area, concrete recommendations, and explicitly that no code changes were made.