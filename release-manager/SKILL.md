---
name: release-manager
description: Use when coordinating final release readiness for a PR, CI run, TestFlight build, App Store submission, release notes, review comments, or Human Review handoff.
---

# Release Manager

Use this skill to move completed implementation work through the final release gate without losing evidence or review obligations.

## Workflow

1. Reconcile current state: branch, dirty files, PR, CI checks, issue/workpad, review comments, and release target.
2. Confirm required validation for the change. Minimum: relevant unit tests. For iOS app code, include simulator or device validation when practical.
3. Sweep blocking feedback: PR review comments, inline comments, failed checks, merge conflicts, stale branch-state claims, and requested visual proof.
4. For TestFlight or App Store work, load `skills/app-store-testflight-review/SKILL.md`.
5. Prepare release notes, What to Test notes, screenshots/recordings, and known-risk notes when the channel requires them.
6. Handoff only when status is clear: ship, hold, blocked, or needs product decision.

## Output

Report the exact release state, validation evidence, remaining blockers, and the next owner. Keep summaries short and proof-first.
