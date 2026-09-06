# Doron Publishing Image Style

Use this style for every image generated for a publishing social post, article promotion, or article hero unless Doron explicitly overrides it.

## Subject
- When an avatar is required, use Doron Katz as the recognizable central or anchoring subject.
- Preserve the reference identity: bald or shaved head, full dark beard with grey streaks, navy blazer over a light grey shirt, serious or neutral expression.
- Use a local or explicitly supplied avatar reference when available. Do not invent a generic substitute when likeness is required.

## Medium and visual language
- Warm cream handmade paper background with visible paper texture.
- Hand-drawn ink linework as the structural anchor.
- Rich watercolor pigment bloom, organic brush texture, and restrained editorial sophistication.
- Default accent palette: coral, teal, navy, and golden ochre. Use restraint; do not turn the image into a flat branded poster.
- Prefer a clear physical scene or editorial metaphor over a generic AI dashboard or floating icons.
- Keep the composition sparse but information-rich, with one obvious focal point and supporting artifacts tied to the post thesis.
- Avoid photorealism, glossy 3D, clean vector art, corporate-dashboard layouts, and unnecessary visual clutter.

## Brand mark
- Every publishing image must include a small handwritten `@doronkatz` watermark in the bottom-right corner.
- The watermark must be warm dark brown ink and integrated into the same hand-drawn medium, not a clean digital overlay or sticker.

## Text and QA
- No large readable text unless the brief explicitly requires it.
- No accidental logos, fake labels, prompt fragments, or gibberish.
- Before handoff, visually check avatar identity, scene relevance, watermark presence, aspect ratio, and unwanted text.
- If avatar or watermark fails, regenerate; do not paint over the generated image.

## Backend
- Publishing image generation uses `--provider codex-cli` through the logged-in ChatGPT/Codex subscription.
- Do not use OpenRouter, `OPENROUTER_API_KEY`, OpenAI Images API, or `OPENAI_API_KEY` for this publishing image path.
