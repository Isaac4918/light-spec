---
name: explore-ideas
description: 'Explore ideas before adding a feature. Use for brainstorming, comparing options, questioning assumptions, investigating the codebase, and refining a rough idea into feature suggestions ready for approval.'
argument-hint: 'Describe the idea, problem, or area you want to explore before creating features'
user-invocable: true
---

# Explore Ideas

Explore ideas before writing to `feature_list.json`. Follow [workflow_rules.md](../../../workflow_rules.md) and use the same feature shape as [feature_template.json](../add-feature/assets/feature_template.json).

## Use it when

- the user has a rough idea and needs help shaping it;
- requirements are unclear, broad, or mixed together;
- several approaches or tradeoffs should be compared before committing;
- the codebase should be inspected to ground the discussion in reality;
- the user wants candidate features drafted for later approval.

## Sources and limits

Use the user prompt as the primary source. Read only the relevant code, backlog, specs, memory, or docs needed to clarify the discussion. Do not implement code, do not modify application files, and do not write backlog, spec, or memory artifacts during exploration.

## Prerequisites

- No artifact is required to start brainstorming.
- If `feature_list.json` exists, use it to detect overlap, duplicates, or natural increments.
- If relevant code exists, inspect only the slices that help validate assumptions or integration points.

## Flow

1. Start with an open exploratory conversation and ask only the questions needed to clarify goals, constraints, users, and success signals.
2. If the idea is broad or vague, surface multiple directions, challenge assumptions, and help the user narrow scope.
3. When useful, inspect the codebase to find existing patterns, constraints, risks, or reuse opportunities.
4. Compare options, tradeoffs, and unknowns in concise prose, tables, or ASCII diagrams when they improve clarity.
5. Keep the discussion exploratory until the idea is concrete enough to describe one or more candidate features.
6. When the idea crystallizes, suggest the identified features in chat using the same structure as `feature_template.json`, including acceptance criteria and an explicit `sdd` question when still undecided.
7. Ask the user which suggestions are worth keeping and, if they want to formalize them, direct the next step to `/add-feature`.

## Rules

- This skill is for thinking and validation, not implementation.
- Do not force a rigid questionnaire; adapt the conversation to the user's idea.
- Do not auto-create artifacts or edit `feature_list.json`.
- If several features emerge, show them separately and explain the split briefly.
- Keep suggestions actionable, bounded, and coherent with the current project and backlog.

## Final behavior

Summarize the refined idea, main tradeoffs or risks, open questions if any remain, and the candidate feature entries proposed in chat. If the user is ready to continue, recommend `/add-feature` as the next step.