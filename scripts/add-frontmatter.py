#!/usr/bin/env python3
"""
Automatically add/update Hugo YAML frontmatter for .md files under content/post/.

Usage:
    python scripts/add-frontmatter.py              # Process all files
    python scripts/add-frontmatter.py --dry-run    # Show what would change
    python scripts/add-frontmatter.py --force      # Regenerate all frontmatter
    python scripts/add-frontmatter.py --path content/post/理论/数学  # Specific path
"""

import argparse
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# ── Repository root (relative to this script) ──────────────────────────
REPO_ROOT = Path(__file__).resolve().parent.parent
POST_DIR = REPO_ROOT / "content" / "post"

# ── Known topic directories used for tag derivation ────────────────────
# When walking up from a file, the FIRST directory matching this set
# becomes the tag. Add new topics here as the blog grows.
KNOWN_TOPICS = {
    # 数学
    "微积分", "线性代数", "集合论", "概率论", "数理逻辑",
    # 物理
    "大学物理", "电磁场", "数字电路",
    # 控制
    "信号与系统", "计算机控制",
    # 政治
    "毛中特", "形势与政策",
    # 哲学
    "人生", "社会",
    # 通信
    "移动通信",
    # 计算机 - 语言 & 基础
    "编程语言", "C语言", "IDE", "汇编", "Python",
    "数据结构", "Web", "机器人", "单片机",
    # 计算机 - AI
    "人工智能", "机器学习", "深度学习", "LLM", "Deepfake", "视觉生成",
}

# ── Category derivation from path prefix ───────────────────────────────
# Maps path prefixes (relative to content/post/) to categories.
# Ordered: first match wins. "Default" entries match any remaining path.
CATEGORY_PREFIXES = [
    ("理论/数学",   ["数学"]),
    ("理论/物理",   ["物理"]),
    ("理论/控制",   ["控制"]),
    ("理论/政治",   ["政治"]),
    ("理论/哲学",   ["哲学"]),
    ("实践/计算机", ["计算机"]),
    ("实践/通信",   ["通信"]),
]

DEFAULT_CATEGORY = ["技术博客"]

# ── Required frontmatter fields for completeness check ─────────────────
REQUIRED_FIELDS = {"title", "description", "slug", "date", "categories", "tags"}

# ── Helpers ────────────────────────────────────────────────────────────

def strip_numeric_prefix(name: str) -> str:
    """Strip leading numeric/chapter prefixes from a filename.

    Handles: '1. ', '01. ', '1.', '一、', '0.', '5.1.v1 ' etc.
    """
    name = name.strip()
    # Chinese number + delimiter: 一、二、三...
    name = re.sub(r'^[一二三四五六七八九十]+[、，]\s*', '', name)
    # Numeric prefix with optional dot/space: '1. ', '01.', '5.1.v1 '
    name = re.sub(r'^\d+(?:\.\d+)*[.v]?\s*', '', name)
    return name.strip()


def title_from_filename(filepath: Path) -> str:
    """Extract a human-readable title from a filename."""
    name = filepath.stem  # filename without .md
    name = strip_numeric_prefix(name)
    # Also clean up trailing markers like _CSDN博客
    name = re.sub(r'[-_]\s*(CSDN博客|知乎|博客园)$', '', name)
    name = name.strip()
    return name if name else filepath.stem


def slug_from_filename(filepath: Path) -> str:
    """Generate a slug from filename. Chinese characters are preserved."""
    name = filepath.stem
    name = strip_numeric_prefix(name)
    # Replace spaces with hyphens for pure-ASCII slugs
    if name.isascii():
        name = re.sub(r'\s+', '-', name)
    name = name.strip()
    return name if name else filepath.stem


def derive_tag(filepath: Path) -> str:
    """Walk up from the file's parent directory to find the first known topic."""
    rel = filepath.parent.relative_to(POST_DIR)
    parts = list(rel.parts)

    # Walk from deepest to shallowest
    for i in range(len(parts) - 1, -1, -1):
        if parts[i] in KNOWN_TOPICS:
            return parts[i]

    # Fallback: use the immediate parent directory
    return parts[-1] if parts else "未分类"


def derive_category(filepath: Path) -> list:
    """Derive categories from the path prefix under content/post/."""
    try:
        rel = filepath.parent.relative_to(POST_DIR).as_posix()
    except ValueError:
        return DEFAULT_CATEGORY

    for prefix, cat in CATEGORY_PREFIXES:
        if rel == prefix or rel.startswith(prefix + "/") or rel == prefix:
            return cat

    # For top-level directories directly under post/ (e.g., 机器学习/)
    first_dir = rel.split("/")[0]
    if first_dir and first_dir != ".":
        return [first_dir]

    return DEFAULT_CATEGORY


def get_git_date(filepath: Path) -> str | None:
    """Get the last commit date for a file from git, in YYYY-MM-DD format."""
    try:
        result = subprocess.run(
            ["git", "log", "--follow", "--format=%ad", "--date=short", "-1", "--",
             str(filepath.name)],
            cwd=str(filepath.parent),
            capture_output=True, text=True, timeout=10,
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
    except (subprocess.TimeoutExpired, FileNotFoundError, OSError):
        pass

    # Fallback: try from repo root
    try:
        rel_path = filepath.relative_to(REPO_ROOT)
        result = subprocess.run(
            ["git", "log", "--follow", "--format=%ad", "--date=short", "-1", "--",
             str(rel_path)],
            cwd=str(REPO_ROOT),
            capture_output=True, text=True, timeout=10,
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
    except (subprocess.TimeoutExpired, FileNotFoundError, OSError, ValueError):
        pass

    return None


def get_file_date(filepath: Path) -> str:
    """Get the best available date for a file (git → filesystem → today)."""
    git_date = get_git_date(filepath)
    if git_date:
        return git_date

    # Filesystem modification time
    mtime = os.path.getmtime(str(filepath))
    return datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")


def format_frontmatter(title: str, slug: str, date: str,
                       categories: list, tags: list) -> str:
    """Format a complete Hugo YAML frontmatter block."""
    lines = ["---"]
    lines.append(f"title: {_quote_yaml(title)}")
    lines.append("description: ")
    lines.append(f"slug: {_quote_yaml(slug)}")
    lines.append(f"date: {date} 00:00:00+0000")
    lines.append("categories:")
    for c in categories:
        lines.append(f"    - {c}")
    lines.append("tags:")
    for t in tags:
        lines.append(f"    - {t}")
    lines.append("weight: 1")
    lines.append("---")
    return "\n".join(lines) + "\n"


def _quote_yaml(value: str) -> str:
    """Quote a YAML string value if it contains special characters."""
    # If the value needs quoting (contains :, #, &, *, !, etc.)
    special = re.search(r'[:#&*!{}\[\]|>%@`"\']', value)
    # If it looks like a number or boolean
    looks_scalar = re.match(r'^(yes|no|true|false|null|~|\d+\.?\d*)$',
                            value, re.IGNORECASE)
    if special or looks_scalar or not value.strip():
        return f'"{value}"'
    return value


def parse_frontmatter(content: str) -> tuple[dict | None, str]:
    """Parse YAML frontmatter from content.

    Returns (frontmatter_dict_or_None, body_content).
    """
    if not content.startswith("---"):
        return None, content

    # Find closing ---
    end = content.find("---", 3)
    if end == -1:
        return None, content

    fm_text = content[3:end].strip()
    body = content[end + 3:]

    # Parse simple YAML key: value pairs (one level deep, no nesting beyond lists)
    fm = {}
    current_key = None
    current_list = None

    for line in fm_text.split("\n"):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        # List item: "    - value"
        list_match = re.match(r'^\s+-\s+(.+)$', line)
        if list_match and current_key:
            val = list_match.group(1).strip()
            val = val.strip('"').strip("'")
            # Ensure the value is a list (convert empty string or scalar)
            existing = fm.get(current_key)
            if not isinstance(existing, list):
                if existing and existing != "":
                    fm[current_key] = [existing, val]
                else:
                    fm[current_key] = [val]
            else:
                fm[current_key].append(val)
            continue

        # Key: value
        kv_match = re.match(r'^(\w[\w_-]*)\s*:\s*(.*)', line)
        if kv_match:
            current_key = kv_match.group(1)
            val = kv_match.group(2).strip()
            val = val.strip('"').strip("'")
            if val:
                fm[current_key] = val
            else:
                fm[current_key] = ""  # empty value
            continue

    # Normalize: ensure list fields are lists, string fields are strings
    for key in ("categories", "tags"):
        if key in fm:
            if isinstance(fm[key], str):
                fm[key] = [fm[key]] if fm[key] else []
            if not isinstance(fm[key], list):
                fm[key] = [fm[key]]

    return fm, body


def is_complete(fm: dict | None) -> bool:
    """Check if frontmatter has all required fields."""
    if fm is None:
        return False
    return REQUIRED_FIELDS.issubset(fm.keys())


def merge_frontmatter(existing: dict | None, generated: dict) -> dict:
    """Merge generated frontmatter into existing, preserving user-set values.

    For list fields (categories, tags), keep existing if non-empty.
    For scalar fields, keep existing if present and non-empty.
    """
    if existing is None:
        return generated

    result = dict(generated)

    # Preserve existing non-empty values
    for key in ("title", "slug", "date", "description"):
        if existing.get(key):
            result[key] = existing[key]

    # Preserve existing non-empty lists
    for key in ("categories", "tags"):
        if existing.get(key):
            result[key] = existing[key]

    return result


def process_file(filepath: Path, force: bool = False, dry_run: bool = False) -> str | None:
    """Process a single .md file. Returns 'updated', 'skipped', or 'error'."""
    relative = filepath.relative_to(REPO_ROOT)

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except (OSError, UnicodeDecodeError) as e:
        print(f"  ERROR reading {relative}: {e}")
        return "error"

    existing_fm, body = parse_frontmatter(content)

    if is_complete(existing_fm) and not force:
        return "skipped"

    # Generate fresh frontmatter
    title = title_from_filename(filepath)
    slug = slug_from_filename(filepath)
    date = get_file_date(filepath)
    categories = derive_category(filepath)
    tag = derive_tag(filepath)
    tags = [tag]

    generated_fm = {
        "title": title,
        "description": "",
        "slug": slug,
        "date": date,
        "categories": categories,
        "tags": tags,
        "weight": 1,
    }

    # Merge with existing (preserve user-set values)
    final_fm = merge_frontmatter(existing_fm, generated_fm)

    # Build output
    new_fm_text = format_frontmatter(
        title=str(final_fm["title"]),
        slug=str(final_fm["slug"]),
        date=str(final_fm["date"]),
        categories=final_fm["categories"] if isinstance(final_fm["categories"], list) else [final_fm["categories"]],
        tags=final_fm["tags"] if isinstance(final_fm["tags"], list) else [final_fm["tags"]],
    )

    new_content = new_fm_text + "\n" + body

    if dry_run:
        action = "REGENERATE" if force and is_complete(existing_fm) else "UPDATE"
        print(f"  [{action}] {relative}")
        print(f"    title: {final_fm['title']}")
        print(f"    categories: {final_fm['categories']}  tags: {final_fm['tags']}")
        return "updated"

    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        return "updated"
    except OSError as e:
        print(f"  ERROR writing {relative}: {e}")
        return "error"


def main():
    parser = argparse.ArgumentParser(
        description="Add/update Hugo YAML frontmatter for content/post/ .md files."
    )
    parser.add_argument(
        "--force", action="store_true",
        help="Regenerate frontmatter even for files that already have complete frontmatter"
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Show what would change without actually writing files"
    )
    parser.add_argument(
        "--path", type=str, default=None,
        help="Specific file or directory to process (default: content/post/)"
    )
    args = parser.parse_args()

    target = REPO_ROOT / args.path if args.path else POST_DIR
    if not target.exists():
        print(f"Error: path not found: {target}")
        sys.exit(1)

    # Collect files
    if target.is_file():
        files = [target]
    else:
        files = sorted(target.rglob("*.md"))

    files = [f for f in files if f.suffix == ".md"]

    if not files:
        print(f"No .md files found in {target.relative_to(REPO_ROOT)}")
        sys.exit(0)

    print(f"{'[DRY RUN] ' if args.dry_run else ''}Processing {len(files)} file(s)...")
    print()

    updated = 0
    skipped = 0
    errors = 0

    for filepath in files:
        result = process_file(filepath, force=args.force, dry_run=args.dry_run)
        if result == "updated":
            updated += 1
        elif result == "skipped":
            skipped += 1
        else:
            errors += 1

    print()
    print(f"Done. Updated: {updated}, Skipped: {skipped}, Errors: {errors}")


if __name__ == "__main__":
    main()
