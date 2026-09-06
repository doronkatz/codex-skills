#!/usr/bin/env python3
"""Insert or replace anchored Mermaid blocks in Markdown files."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ANCHOR_RE = re.compile(r"^[A-Za-z0-9_.-]+$")
FENCED_MERMAID_RE = re.compile(r"(?ms)```mermaid\s*\n(.*?)\n```")
COMMON_STARTS = (
    "flowchart",
    "graph",
    "sequenceDiagram",
    "classDiagram",
    "stateDiagram",
    "stateDiagram-v2",
    "erDiagram",
    "journey",
    "gantt",
    "pie",
    "gitGraph",
    "mindmap",
    "timeline",
    "quadrantChart",
    "requirementDiagram",
    "C4Context",
    "C4Container",
    "C4Component",
    "C4Dynamic",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Insert or replace an anchored Mermaid code block in Markdown."
    )
    parser.add_argument("--file", required=True, help="Markdown file to update.")
    parser.add_argument("--id", required=True, help="Stable diagram id for HTML anchors.")
    parser.add_argument("--diagram-file", required=True, help="File containing raw Mermaid.")
    parser.add_argument("--title", help="Optional Markdown heading inside the anchored block.")
    parser.add_argument("--after-heading", help="Insert below this Markdown heading if absent.")
    parser.add_argument("--before-heading", help="Insert before this Markdown heading if absent.")
    parser.add_argument("--append", action="store_true", help="Append if the block is absent.")
    parser.add_argument("--replace-only", action="store_true", help="Fail if the block is absent.")
    parser.add_argument("--create", action="store_true", help="Create the Markdown file if needed.")
    parser.add_argument("--dry-run", action="store_true", help="Print updated Markdown only.")
    parser.add_argument(
        "--strict-kind",
        action="store_true",
        help="Fail when the first Mermaid line is not a common diagram start.",
    )
    return parser.parse_args()


def normalize_lf(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n")


def detect_newline(text: str) -> str:
    return "\r\n" if "\r\n" in text else "\n"


def read_text_preserve_newlines(path: Path) -> str:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return handle.read()


def write_text_preserve_newlines(path: Path, text: str) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        handle.write(text)


def extract_mermaid(text: str) -> str:
    text = normalize_lf(text).strip()
    match = FENCED_MERMAID_RE.search(text)
    if match:
        text = match.group(1).strip()
    if "```" in text:
        raise ValueError("diagram input contains a non-Mermaid code fence")
    if not text:
        raise ValueError("diagram input is empty")
    return text


def first_mermaid_line(diagram: str) -> str:
    for line in diagram.split("\n"):
        stripped = line.strip()
        if stripped and not stripped.startswith("%%"):
            return stripped
    return ""


def is_common_mermaid_start(line: str) -> bool:
    return any(line == start or line.startswith(start + " ") for start in COMMON_STARTS)


def build_block(diagram_id: str, diagram: str, title: str | None) -> str:
    lines = [f"<!-- mermaid-diagram: {diagram_id} -->"]
    if title:
        lines.extend([f"### {title}", ""])
    lines.extend(["```mermaid", *diagram.split("\n"), "```"])
    lines.extend([f"<!-- /mermaid-diagram: {diagram_id} -->", ""])
    return "\n".join(lines)


def block_pattern(diagram_id: str) -> re.Pattern[str]:
    escaped_id = re.escape(diagram_id)
    return re.compile(
        rf"(?ms)^<!--\s*mermaid-diagram:\s*{escaped_id}\s*-->\n"
        rf".*?"
        rf"^<!--\s*/mermaid-diagram:\s*{escaped_id}\s*-->\s*(?:\n)?"
    )


def heading_matches(line: str, query: str) -> bool:
    stripped = line.strip()
    query = query.strip()
    if stripped == query:
        return True
    match = re.match(r"^#{1,6}\s+(.*?)\s*#*\s*$", stripped)
    return bool(match and match.group(1) == query)


def insert_after_heading(text: str, heading: str, block: str) -> str:
    lines = text.splitlines(keepends=True)
    position = 0
    for index, line in enumerate(lines):
        if heading_matches(line.rstrip("\n"), heading):
            position += len(line)
            next_index = index + 1
            while next_index < len(lines) and lines[next_index].strip() == "":
                position += len(lines[next_index])
                next_index += 1
            return splice_block(text, position, block)
        position += len(line)
    raise ValueError(f"heading not found: {heading}")


def insert_before_heading(text: str, heading: str, block: str) -> str:
    lines = text.splitlines(keepends=True)
    position = 0
    for line in lines:
        if heading_matches(line.rstrip("\n"), heading):
            return splice_block(text, position, block)
        position += len(line)
    raise ValueError(f"heading not found: {heading}")


def append_block(text: str, block: str) -> str:
    if not text:
        return block
    separator = "" if text.endswith("\n\n") else "\n" if text.endswith("\n") else "\n\n"
    return text + separator + block


def splice_block(text: str, position: int, block: str) -> str:
    prefix = text[:position]
    suffix = text[position:]
    before = "" if not prefix or prefix.endswith("\n\n") else "\n"
    after = "" if not suffix or suffix.startswith("\n") else "\n"
    return prefix + before + block + after + suffix


def update_text(text: str, diagram_id: str, block: str, args: argparse.Namespace) -> tuple[str, str]:
    pattern = block_pattern(diagram_id)
    matches = list(pattern.finditer(text))
    if len(matches) > 1:
        raise ValueError(f"multiple mermaid blocks found for id: {diagram_id}")
    if matches:
        return pattern.sub(block, text, count=1), "replaced"
    if args.replace_only:
        raise ValueError(f"mermaid block not found for id: {diagram_id}")
    if args.after_heading:
        return insert_after_heading(text, args.after_heading, block), "inserted"
    if args.before_heading:
        return insert_before_heading(text, args.before_heading, block), "inserted"
    return append_block(text, block), "appended"


def main() -> int:
    args = parse_args()

    placements = [bool(args.after_heading), bool(args.before_heading), bool(args.append)]
    if sum(placements) > 1:
        print("error: choose only one placement option", file=sys.stderr)
        return 2
    if not ANCHOR_RE.match(args.id):
        print("error: --id may contain only letters, digits, dot, underscore, and hyphen", file=sys.stderr)
        return 2

    target_path = Path(args.file)
    if not target_path.exists() and not args.create:
        print(f"error: file not found: {target_path}", file=sys.stderr)
        return 2

    try:
        diagram = extract_mermaid(Path(args.diagram_file).read_text(encoding="utf-8-sig"))
        first_line = first_mermaid_line(diagram)
        if first_line and not is_common_mermaid_start(first_line):
            message = f"warning: uncommon Mermaid start: {first_line}"
            if args.strict_kind:
                raise ValueError(message)
            print(message, file=sys.stderr)

        original = read_text_preserve_newlines(target_path) if target_path.exists() else ""
        newline = detect_newline(original)
        original_lf = normalize_lf(original)
        block = build_block(args.id, diagram, args.title)
        updated_lf, action = update_text(original_lf, args.id, block, args)
        updated = updated_lf.replace("\n", newline)
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if args.dry_run:
        print(updated, end="")
        return 0

    target_path.parent.mkdir(parents=True, exist_ok=True)
    write_text_preserve_newlines(target_path, updated)
    print(f"{action}: {target_path} :: {args.id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
