---
name: app-store-testflight-review
description: Use when preparing, reviewing, or validating iOS TestFlight or App Store release readiness, including What to Test notes, reviewer instructions, metadata, screenshots, simulator evidence, App Store Connect status, and release blockers.
---

# App Store and TestFlight Review

Use this skill for iOS release-readiness work that crosses packaging, App Store Connect, reviewer-facing copy, screenshots, and validation evidence.

## Workflow

1. Identify the release channel: internal TestFlight, external TestFlight, App Store review, metadata-only update, or screenshot/export package.
2. Reconcile current state: branch/PR, Linear workpad, build number, bundle ID, App Store Connect app/version, CI status, and pending review feedback.
3. Load the specific ASC skill needed for the channel:
   - `skills/asc-cli-usage/SKILL.md` for `asc` command conventions.
   - `skills/asc-build-lifecycle/SKILL.md` for build states and processing.
   - `skills/asc-testflight-orchestration/SKILL.md` for TestFlight groups, testers, and What to Test notes.
   - `skills/asc-release-flow/SKILL.md` for App Store submission flow.
   - `skills/asc-submission-health/SKILL.md` for review blockers and submission status.
   - `skills/asc-metadata-sync/SKILL.md` for metadata, review info, and localized copy.
4. For simulator evidence, load `skills/axe/SKILL.md`; note UDID, bundle ID, selectors, and expected path before invoking AXe commands.
5. For App Store screenshots or marketing screenshot exports, load `/Users/doronkatz/.agents/skills/app-store-screenshots/SKILL.md` if available; otherwise validate device size, localized copy, safe areas, and export filenames manually.
6. Confirm release notes and What to Test notes describe the shipped scope and user-verifiable paths.
7. Report blockers explicitly: signing, processing, missing metadata, failed tests, rejected screenshots, review feedback, unavailable credentials, or unclear release scope.

## Acceptance Bar

- Tests relevant to touched code are green, or every failure has an attached run/result path and an approved disposition.
- UI changes have screenshot or recording evidence for the affected path.
- TestFlight builds include What to Test notes for alpha/beta testers.
- App Store submissions include reviewer instructions, contact/account flow, metadata, screenshots, and compliance information as applicable.
- The handoff states one of: ready to ship, ready for human review, held for blocker, or needs product decision.
