---
name: get-api-docs
description: Use this skill when you need current documentation for a third-party library, SDK, CLI, or HTTP API before writing or reviewing code that integrates with it. Trigger on requests like "use the Stripe API", "add Anthropic SDK support", "query Pinecone", "call this vendor endpoint", or any task where accurate external API reference matters. Fetch docs with the `chub` CLI instead of relying on memory. Prefer more specialized local skills first when one exists for the same domain, such as `openai-docs` for official OpenAI documentation.
---

# Get API Docs

Use `chub` to fetch the current docs for external APIs and libraries before answering or writing integration code.

## Workflow

1. Identify the product or library you need docs for.
2. Search for the best matching Context Hub doc:

```bash
chub search "<library or API name>" --json
```

3. Pick the best `id` from the results, then fetch the relevant docs. Match `--lang` to the codebase when possible:

```bash
chub get <id> --lang py
chub get <id> --lang js
chub get <id> --lang ts
```

4. Read the returned content and use it as the source of truth for API shape, parameters, examples, and version-specific behavior.
5. If the task reveals a concise local gotcha or project-specific quirk that is not already in the doc, save it with `chub annotate`.
6. Ask the user before sending `chub feedback`.

## Rules

- Do not guess API details when `chub` can provide the docs.
- Prefer the language variant that matches the repository you are editing.
- If multiple doc IDs look plausible, inspect the closest match first and retry with a broader or more exact search term if needed.
- Keep annotations short, actionable, and limited to details future sessions would benefit from.
- Do not duplicate the doc in annotations.
- If `chub` is unavailable or returns no relevant result, say that clearly and use the next-best primary source for that vendor.

## Quick reference

```bash
chub search "stripe" --json
chub get stripe/api --lang ts
chub get anthropic/sdk --lang py -o docs.md
chub annotate stripe/api "Webhook verification requires the raw request body."
chub annotate --list
chub feedback stripe/api up
```

## Notes

- `chub search` with no query lists available docs.
- IDs use the `<author>/<name>` format.
- If a doc supports multiple languages and `--lang` is omitted, `chub` will show the available variants.
