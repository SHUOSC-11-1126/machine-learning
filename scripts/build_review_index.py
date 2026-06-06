#!/usr/bin/env python3
"""Build review indexes from the teacher-maintained course submodule."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEACHER = ROOT / "files-from-teacher"
REVIEW = ROOT / "review"

MAIN_SESSIONS = [1, 2, 3, 4, 5, 6, 7]
EXTRA_PREFIXES = [
    "session-102",
    "session-104",
    "session-105",
    "session-200",
    "session-201",
    "session-202",
    "session-203",
    "session-204",
    "session-205",
    "session-208",
    "session-211",
    "session-212",
    "session-223",
    "session-400",
    "session-402",
    "session-403",
    "session-404",
    "session-405",
    "session-406",
    "session-501",
]


@dataclass(frozen=True)
class MarkdownFile:
    path: Path
    title: str
    headings: tuple[str, ...]


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def first_title(text: str, fallback: str) -> str:
    for line in text.splitlines():
        match = re.match(r"^#\s+(.+?)\s*$", line)
        if match:
            return match.group(1)
        match = re.match(r"^## Question:\s+(.+?)\s*$", line)
        if match:
            return match.group(1)
    return fallback


def headings(text: str, limit: int = 8) -> tuple[str, ...]:
    values: list[str] = []
    for line in text.splitlines():
        match = re.match(r"^(#{1,3})\s+(.+?)\s*$", line)
        if match:
            values.append(match.group(2).strip())
        if len(values) >= limit:
            break
    return tuple(values)


def markdown_file(path: Path) -> MarkdownFile:
    text = read_text(path)
    return MarkdownFile(path=path, title=first_title(text, path.stem), headings=headings(text))


def question_titles(path: Path) -> list[str]:
    text = read_text(path)
    titles = re.findall(r"^## Question:\s+(.+?)\s*$", text, re.MULTILINE)
    return titles or [first_title(text, path.stem)]


def session_markdown_files(session: int) -> list[MarkdownFile]:
    directory = TEACHER / f"session-{session}"
    return [markdown_file(path) for path in sorted(directory.glob("*.md"))]


def extra_markdown_files() -> dict[str, list[MarkdownFile]]:
    result: dict[str, list[MarkdownFile]] = {}
    for directory in sorted(TEACHER.iterdir()):
        if not directory.is_dir():
            continue
        if not any(directory.name.startswith(prefix) for prefix in EXTRA_PREFIXES):
            continue
        files = [markdown_file(path) for path in sorted(directory.glob("*.md"))]
        if files:
            result[directory.name] = files
    return result


def bag_questions() -> dict[str, list[tuple[Path, list[str]]]]:
    result: dict[str, list[tuple[Path, list[str]]]] = {}
    directory = TEACHER / "BagOfQuestions"
    for path in sorted(directory.glob("BagOfQuestions-session-*.md")):
        match = re.search(r"session-(\d+)-", path.name)
        if not match:
            continue
        result.setdefault(f"session-{match.group(1)}", []).append((path, question_titles(path)))
    return result


def write_source_index() -> None:
    REVIEW.mkdir(parents=True, exist_ok=True)
    questions = bag_questions()
    extras = extra_markdown_files()

    lines: list[str] = [
        "# 机器学习复习资料索引",
        "",
        "本索引从 `files-from-teacher/` 子模块生成。该子模块由老师维护，是考试复习的唯一最高优先级资料。",
        "",
        "## Exam Signal From Readme",
        "",
        "- Final score = `0.7 * T + 0.3 * P`.",
        "- Final exam: about 70% from main sessions 1-7.",
        "- Some exam questions will come from `files-from-teacher/BagOfQuestions/`.",
        "- About 30% from extra sessions, described as easier questions.",
        "- Closed-book exam: no books, sheets, or other materials.",
        "",
        "## Priority Order",
        "",
        "1. `files-from-teacher/Readme.md` exam rules.",
        "2. `files-from-teacher/BagOfQuestions/` question source.",
        "3. `files-from-teacher/session-1` to `session-7` lecture and code materials.",
        "4. Extra session materials under `files-from-teacher/session-*` beyond 1-7.",
        "",
        "## Main Sessions",
        "",
    ]

    for session in MAIN_SESSIONS:
        files = session_markdown_files(session)
        qfiles = questions.get(f"session-{session}", [])
        lines.extend([f"### Session {session}", ""])
        lines.append(f"- BagOfQuestions files: {len(qfiles)}")
        for path, titles in qfiles:
            joined = "; ".join(titles)
            lines.append(f"  - `{rel(path)}`: {joined}")
        lines.append(f"- Markdown materials: {len(files)}")
        for item in files:
            if item.path.name.startswith("practice-") or "practice" in item.path.name:
                kind = "practice"
            elif item.path.name.startswith("code-"):
                kind = "code"
            elif item.path.name.startswith("lecture-"):
                kind = "lecture"
            elif item.path.name.startswith("reading-"):
                kind = "reading"
            else:
                kind = "other"
            lines.append(f"  - `{rel(item.path)}` ({kind}): {item.title}")
        lines.append("")

    lines.extend(["## Extra Sessions", ""])
    for name, files in extras.items():
        lines.extend([f"### {name}", ""])
        for item in files[:12]:
            lines.append(f"- `{rel(item.path)}`: {item.title}")
        if len(files) > 12:
            lines.append(f"- ... {len(files) - 12} more markdown files")
        lines.append("")

    (REVIEW / "source-index.md").write_text("\n".join(lines), encoding="utf-8")

def main() -> int:
    if not TEACHER.exists():
        raise SystemExit("Missing files-from-teacher submodule")
    write_source_index()
    print("generated review/source-index.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
