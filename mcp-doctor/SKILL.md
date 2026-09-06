---
name: mcp-doctor
description: Use when diagnosing or repairing Codex MCP server startup failures, connector auth errors, missing tools, plugin cache drift, skill-loader warnings, broken skill symlinks, or config.toml syntax and path issues.
---

# MCP Doctor

Use this skill for Codex-home tool startup and connector hygiene.

## Workflow

1. Read the relevant `~/.codex/config.toml` block and the failing startup output before changing anything.
2. Classify the failure: TOML syntax, unsupported config key, missing binary, broken symlink, stale plugin cache path, auth/401, network/package fetch, initialize-response failure, or skill-loader warning.
3. Validate narrowly:
   - TOML with `tomllib`.
   - Skill frontmatter with a YAML parser.
   - Symlinks with `find skills -type l ! -exec test -e {} ; -print`.
   - Configured commands with `command -v` or explicit path checks.
4. Fix the smallest surface that explains the failure.
5. Re-run the narrow validator. If a full startup check hangs, stop it and report the hang rather than waiting indefinitely.

## Guardrails

- Do not delete unrelated MCP entries.
- Do not expose or commit secrets.
- Prefer official package paths and current configured binaries over guesses.
- Mention restart requirements when Codex needs to reload skills, plugins, or MCP registrations.
