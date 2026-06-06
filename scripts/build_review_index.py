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
        "本索引从 `files-from-teacher/` 子模块生成。该子模块由老师维护，是考试复习的唯一最高优先级资料。本仓库自己的历史作业、任务列表和群聊记录不用于决定考试重点。",
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
        "5. Archived homework experience only after a teacher-source topic has already been identified; it must never override `files-from-teacher/`.",
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


def write_homework_assets() -> None:
    REVIEW.mkdir(parents=True, exist_ok=True)
    lines: list[str] = [
        "# 本仓库历史作业资产索引",
        "",
        "本仓库历史作业和任务管理文件已从复习仓库移除，并推送到 `https://github.com/ceilf6/machine-learning-tasks`。它们不能决定考试范围，也不能覆盖老师资料；只有当 `files-from-teacher/` 已经确认某个考点后，才可以把历史作业经验当作个人练习补充。",
        "",
        "## 已清理噪音类型",
        "",
        "- 历史任务列表：提交、微信群、URL、待完成状态等管理信息。",
        "- 历史作业目录：CV、CI/CD、项目提交、实验脚本和中间数据。",
        "- 群聊记录与截图：只服务任务确认，不作为考试复习来源。",
        "- 旧 GitHub Actions：服务作业提交，不服务复习。",
        "",
        "## 可沉淀的低优先级复习经验",
        "",
        "- 情感分类模型评估：可复习 `pipeline`、标签映射、accuracy 计算、模型与数据集匹配；具体模型排名不视为考试范围。",
        "- 线性模型训练脚本：可复习 `fit`、模型参数、保存模型和最小训练流程；CI/CD 发布流程不作为复习重点。",
        "- GloVe/embedding 小实验：可辅助理解词向量、相似度、下游分类；考试重点仍以 BagOfQuestions 和老师 session 资料为准。",
        "- 个人作业踩坑：只在老师题目已经定位到同一知识点时用于提醒易错点。",
        "",
        "## 使用规则",
        "",
        "1. 先查 `files-from-teacher/Readme.md`、`files-from-teacher/BagOfQuestions/` 和主 session 资料。",
        "2. 只有老师资料已经确认某个知识点后，才允许回忆历史作业经验。",
        "3. 如果历史作业经验与老师资料冲突，丢弃历史作业经验。",
        "4. 如果需要查看已备份原始作业文件，先向用户确认，不要自行把备份复制回仓库。",
    ]
    (REVIEW / "homework-assets-low-priority.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    if not TEACHER.exists():
        raise SystemExit("Missing files-from-teacher submodule")
    write_source_index()
    write_homework_assets()
    print("generated review/source-index.md")
    print("generated review/homework-assets-low-priority.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
