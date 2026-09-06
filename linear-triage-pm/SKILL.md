---
name: linear-triage-pm
description: Use when triaging Linear issues in Triage status, clarifying product requirements, creating or repairing child issues, preserving parent project inheritance, and moving ready tickets to Backlog.
---

# Linear Triage PM

Use this skill for Linear triage passes where tickets must become implementation-ready.

## Workflow

1. Fetch/read the parent issue first, including state, project, projectId, labels, children, and comments.
2. Review the issue through product manager, iOS architect, iOS packager, tester, and any domain-specific roles required by the content.
3. Tighten the issue body: problem, user value, scope, non-goals, acceptance criteria, test plan, release risk, and dependencies.
4. When creating child issues, set the child `project` to match the parent exactly. If an existing child has missing or mismatched project attribution, correct it immediately.
5. Move the issue from Triage to Backlog only after the issue is clear, testable, and appropriately decomposed.

## Output

Report the triage decision, issue updates, child project inheritance status, acceptance criteria, test plan, and Backlog move or blocker.
