---
name: asc-ui-test-screenshots
description: "Capture iOS UI-testing screenshots and report them back to Linear. Use when asked to use asc for app screenshots as part of iOS UI testing, or to attach UI test evidence to a Linear issue. Important: the installed asc CLI does not capture screenshots, so this skill must route capture through the AXe simulator workflow and use $linear for issue comments and attachments."
---

# ASC UI Test Screenshots

Use this skill for iOS tester work that needs screenshot evidence on a Linear issue.

## Non-negotiables

- Treat `asc` as a naming trigger only. The installed `asc` CLI does not provide screenshot capture commands.
- For simulator automation and screenshot capture, follow the `axe` skill.
- For issue context, attachments, and comments, follow the `$linear` skill.
- Always read the Linear issue first before posting evidence so the comment matches the testing scope.
- Always attach screenshots to the issue and add a comment that explains what each screenshot proves.

## Required workflow

### Step 1: Confirm scope

Collect or infer:
- Linear issue ID
- Target simulator UDID
- App bundle ID or launch target
- The UI flow being tested
- Whether the screenshots are expected-state evidence, bug evidence, or regression evidence

If the issue ID is missing, stop and ask for it. Screenshot evidence without a target issue is not a complete workflow.

### Step 2: Read issue context with `$linear`

Use `$linear` first:
- Read the issue and recent comments.
- Check for requested coverage, acceptance criteria, and any prior screenshot evidence.
- If the issue references another parent ticket, stay scoped to the issue the tester was asked to update.

### Step 3: Capture screenshots through AXe

Use the `axe` skill for all simulator interactions.

Preferred flow:
1. Inspect the current screen with `axe describe-ui --udid <UDID>`.
2. Navigate the app with AXe commands or batch steps as needed.
3. Capture screenshots with:

```bash
mkdir -p artifacts/ui-testing/<ISSUE_ID>
axe screenshot --udid <UDID> --output artifacts/ui-testing/<ISSUE_ID>/<NAME>.png
```

Rules:
- Prefer deterministic names such as `launch.png`, `settings-screen.png`, `bug-empty-state.png`.
- Capture only the minimum set needed to prove the outcome.
- After each meaningful UI transition, verify the state before capturing.

### Step 4: Attach screenshots to the Linear issue

Use Linear attachments rather than pasting raw file paths into a comment.

For each screenshot:
1. Base64-encode the PNG locally.
2. Call the Linear attachment tool with:
   - `issue`: the Linear issue ID or identifier
   - `filename`: the screenshot filename
   - `contentType`: `image/png`
   - `title`: short evidence label
   - `subtitle`: optional note such as `iPhone 16 Pro simulator`

If the attachment response includes a URL, use it in the comment body. If it does not, still post the summary comment after uploading the files.

### Step 5: Post a high-signal comment with `$linear`

After attachments are uploaded, add one comment that includes:
- What flow was tested
- Result: pass, fail, or blocked
- Short observation for each screenshot
- Any mismatch against acceptance criteria
- Environment details: simulator, OS, app build if known

Comment template:

```markdown
UI test evidence for <flow>.

Result: <pass|fail|blocked>
Environment: <device / iOS version / build>

Screenshots:
- `<file>`: <what this screenshot proves>
- `<file>`: <what this screenshot proves>

Notes:
- <key finding or failure>
- <follow-up needed, if any>
```

If the attachments expose URLs, include them inline in the screenshot bullets.

## Tooling notes

- If you need to launch or rebuild the app before capture, use the Xcode MCP workflow already used by the iOS tester agent.
- Keep screenshots in `artifacts/ui-testing/<ISSUE_ID>/` so repeated runs stay organized.
- If the request is actually about App Store metadata screenshots, do not use this skill. Use the relevant ASC metadata workflow instead.

## Exit criteria

Before finishing:
- The Linear issue has the uploaded screenshot files.
- The issue has a comment summarizing the evidence.
- The comment clearly states whether the tested flow passed, failed, or is blocked.
