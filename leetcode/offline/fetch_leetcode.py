#!/usr/bin/env python3
"""Scaffold offline LeetCode solution files from a list of problem URLs.

Reads a text file with one LeetCode URL (or bare slug) per line, downloads
each problem once from the public LeetCode GraphQL endpoint, sorts it into
an easy/, medium/ or hard/ subfolder, and writes a self-contained Python
unittest file containing:

  * the full problem description as header comments,
  * the official Python3 ``Solution`` stub,
  * unit tests derived from the official examples (where the example data
    is plain Python data; complex inputs get TODO placeholder tests).

Everything needed to work on a problem afterwards lives in the generated
file, so no internet access is required while solving. Standard library
only.

Usage:
    uv run fetch_leetcode.py problems.txt
    uv run fetch_leetcode.py problems.txt --force
    uv run fetch_leetcode.py problems.txt --output-dir ./out
"""

from __future__ import annotations

import argparse
import ast
import json
import re
import sys
import textwrap
import time
import typing
import urllib.error
import urllib.request
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path

GRAPHQL_URL = "https://leetcode.com/graphql"
REQUEST_DELAY_S = 0.3
DEFAULT_TIMEOUT_S = 20.0
WRAP_WIDTH = 76

DIFFICULTY_DIRS = {"Easy": "easy", "Medium": "medium", "Hard": "hard"}

QUESTION_QUERY = """
query getQuestion($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionFrontendId
    title
    titleSlug
    difficulty
    isPaidOnly
    content
    codeSnippets { lang langSlug code }
    exampleTestcaseList
  }
}
"""

HELPER_DEFINITIONS = {
    "ListNode": [
        "# Definition for singly-linked list.",
        "# class ListNode:",
        "#     def __init__(self, val=0, next=None):",
        "#         self.val = val",
        "#         self.next = next",
    ],
    "TreeNode": [
        "# Definition for a binary tree node.",
        "# class TreeNode:",
        "#     def __init__(self, val=0, left=None, right=None):",
        "#         self.val = val",
        "#         self.left = left",
        "#         self.right = right",
    ],
}

BLOCK_TAGS = {"p", "div", "h1", "h2", "h3", "h4", "h5", "h6", "ul", "ol", "table", "hr"}


class FetchError(Exception):
    """Raised when a problem cannot be downloaded or is not usable."""


class StubError(Exception):
    """Raised when the official code snippet cannot be parsed."""


# ---------------------------------------------------------------------------
# Downloading
# ---------------------------------------------------------------------------


def extract_slug(line: str) -> str | None:
    token = line.strip()
    match = re.search(r"/problems/([^/?#\s]+)", token)
    if match:
        return match.group(1)
    candidate = token.split("/")[0].split("?")[0].strip()
    if re.fullmatch(r"[a-z0-9-]+", candidate):
        return candidate
    return None


def fetch_question(slug: str, timeout: float) -> dict:
    payload = json.dumps(
        {"query": QUESTION_QUERY, "variables": {"titleSlug": slug}}
    ).encode()
    request = urllib.request.Request(
        GRAPHQL_URL,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Referer": f"https://leetcode.com/problems/{slug}/",
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
            ),
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            data = json.load(response)
    except urllib.error.HTTPError as exc:
        raise FetchError(f"HTTP {exc.code} from LeetCode") from exc
    except urllib.error.URLError as exc:
        raise FetchError(f"network error: {exc.reason}") from exc
    except json.JSONDecodeError as exc:
        raise FetchError("LeetCode returned invalid JSON") from exc

    question = (data.get("data") or {}).get("question")
    if question is None:
        raise FetchError("problem not found (check the slug)")
    if question.get("isPaidOnly"):
        raise FetchError("premium-only problem, skipped")
    if not question.get("content"):
        raise FetchError("problem has no description content")
    return question


# ---------------------------------------------------------------------------
# Description parsing (HTML -> comment lines)
# ---------------------------------------------------------------------------


class _DescriptionParser(HTMLParser):
    """Convert a LeetCode problem HTML body into ordered text blocks."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.blocks: list[tuple[str, str]] = []
        self._buf: list[str] = []
        self._in_pre = False
        self._list_stack: list[int] = []

    # -- helpers ----------------------------------------------------------

    def _flush_text(self) -> None:
        text = "".join(self._buf)
        self._buf = []
        text = re.sub(r"\s+", " ", text.replace("\xa0", " ")).strip()
        if text:
            self.blocks.append(("p", text))

    def _flush_code(self) -> None:
        code = "".join(self._buf).replace("\xa0", " ").strip("\n")
        self._buf = []
        self._in_pre = False
        if code.strip():
            self.blocks.append(("code", code))

    # -- parser hooks -----------------------------------------------------

    def handle_starttag(self, tag: str, attrs) -> None:
        if self._in_pre:
            return
        if tag == "pre":
            self._flush_text()
            self._in_pre = True
        elif tag in ("ul", "ol"):
            self._flush_text()
            self._list_stack.append(0)
        elif tag == "li":
            self._flush_text()
            if self._list_stack:
                self._list_stack[-1] += 1
                marker = f"{self._list_stack[-1]}. "
            else:
                marker = "- "
            self._buf.append(marker)
        elif tag in BLOCK_TAGS:
            self._flush_text()
        elif tag == "code":
            self._buf.append("`")
        elif tag == "sup":
            self._buf.append("^")
        elif tag == "sub":
            self._buf.append("_")

    def handle_endtag(self, tag: str) -> None:
        if self._in_pre:
            if tag == "pre":
                self._flush_code()
            return
        if tag == "li":
            self._flush_text()
        elif tag in ("ul", "ol"):
            self._flush_text()
            if self._list_stack:
                self._list_stack.pop()
        elif tag == "code":
            self._buf.append("`")
        elif tag in BLOCK_TAGS:
            self._flush_text()

    def handle_data(self, data: str) -> None:
        self._buf.append(data)

    def close(self) -> None:
        super().close()
        if self._in_pre:
            self._flush_code()
        self._flush_text()


def parse_description(html: str) -> list[tuple[str, str]]:
    parser = _DescriptionParser()
    parser.feed(html)
    parser.close()
    return parser.blocks


def render_description(blocks: list[tuple[str, str]]) -> list[str]:
    lines: list[str] = []
    for kind, text in blocks:
        if lines:
            lines.append("#")
        if kind == "code":
            for src in text.splitlines():
                lines.append(f"#     {src.rstrip()}" if src.strip() else "#")
        else:
            bullet = re.match(r"^((?:\d+\.|-)\s+)", text)
            hang = " " * len(bullet.group(1)) if bullet else ""
            wrapped = textwrap.wrap(
                text,
                width=WRAP_WIDTH,
                subsequent_indent=hang,
                break_long_words=False,
                break_on_hyphens=False,
            )
            for chunk in wrapped or [""]:
                lines.append(f"# {chunk}" if chunk else "#")
    return lines


# ---------------------------------------------------------------------------
# Example extraction and literal conversion
# ---------------------------------------------------------------------------

_EXAMPLE_RE = re.compile(
    r"Input:[ \t]*(?P<input>.*?)"
    r"Output:[ \t]*(?P<output>[^\n]*)",
    re.S,
)


def _one_line(text: str) -> str:
    return " ".join(text.split())


def extract_examples(blocks: list[tuple[str, str]]) -> list[tuple[str, str]]:
    """Find ordered ``Input``/``Output`` pairs across all description blocks.

    Older problems keep each example in one ``<pre>`` block; newer ones split
    them across several paragraphs. Scanning the joined text handles both.
    """
    if not blocks:
        return []
    combined = "\n".join(text for _, text in blocks)
    return [
        (match.group("input").strip(), match.group("output").strip())
        for match in _EXAMPLE_RE.finditer(combined)
    ]


def lc_literal_to_py(text: str) -> tuple[str, bool] | None:
    """Return ``(python_literal_source, contained_null)`` or ``None``."""
    source = text.strip().replace("\xa0", " ")
    if not source:
        return None
    had_null = bool(re.search(r"\bnull\b", source))
    source = re.sub(r"\bnull\b", "None", source)
    source = re.sub(r"\btrue\b", "True", source)
    source = re.sub(r"\bfalse\b", "False", source)
    try:
        ast.literal_eval(source)
    except (ValueError, SyntaxError, MemoryError, RecursionError):
        return None
    return source, had_null


def scan_split(text: str, sep: str) -> list[str]:
    """Split on *sep* at bracket depth zero, honouring quotes and escapes."""
    parts: list[str] = []
    buf: list[str] = []
    depth = 0
    quote: str | None = None
    i = 0
    while i < len(text):
        ch = text[i]
        if quote:
            buf.append(ch)
            if ch == "\\" and i + 1 < len(text):
                buf.append(text[i + 1])
                i += 2
                continue
            if ch == quote:
                quote = None
        elif ch in "\"'":
            quote = ch
            buf.append(ch)
        elif ch in "[({":
            depth += 1
            buf.append(ch)
        elif ch in "])}":
            depth -= 1
            buf.append(ch)
        elif ch == sep and depth == 0:
            parts.append("".join(buf))
            buf = []
        else:
            buf.append(ch)
        i += 1
    parts.append("".join(buf))
    return [part.strip() for part in parts]


def parse_input_assignments(input_text: str) -> dict[str, tuple[str, bool]] | None:
    """Parse ``name = literal`` pairs; ``None`` when the format is exotic."""
    flat = re.sub(r"\s*\n\s*", ", ", input_text.strip())
    assignments: dict[str, tuple[str, bool]] = {}
    for part in scan_split(flat, ","):
        pieces = scan_split(part, "=")
        if len(pieces) < 2:
            return None
        name = pieces[0].strip()
        value = "=".join(pieces[1:]).strip()
        if not re.fullmatch(r"[A-Za-z_]\w*", name):
            return None
        converted = lc_literal_to_py(value)
        if converted is None:
            return None
        assignments[name] = converted
    return assignments or None


# ---------------------------------------------------------------------------
# Solution stub parsing
# ---------------------------------------------------------------------------


@dataclass
class Method:
    name: str
    params: list[tuple[str, str]]  # (name, annotation source)
    returns: str

    @property
    def param_names(self) -> list[str]:
        return [name for name, _ in self.params]


_DEF_RE = re.compile(r"^([ \t]*)def\s+(\w+)\(", re.M)


def _annotation_identifiers(annotation: str) -> set[str]:
    return set(re.findall(r"\b[A-Za-z_]\w*\b", annotation))


def parse_solution_stub(code: str) -> list[Method]:
    methods: list[Method] = []
    for match in _DEF_RE.finditer(code):
        name = match.group(2)
        i = match.end()  # just after "("
        depth = 1
        while i < len(code) and depth:
            ch = code[i]
            if ch == "(":
                depth += 1
            elif ch == ")":
                depth -= 1
            i += 1
        params_src = code[match.end() : i - 1]
        rest = code[i:]
        colon = rest.find(":")
        if colon < 0:
            raise StubError(f"cannot find signature end for method '{name}'")
        returns = ""
        arrow = re.match(r"\s*->\s*(.+)", rest[:colon].strip())
        if arrow:
            returns = arrow.group(1).strip()

        params: list[tuple[str, str]] = []
        for part in scan_split(params_src, ","):
            if not part:
                continue
            pieces = scan_split(part, "=")[0]
            pieces2 = scan_split(pieces, ":")
            pname = pieces2[0].strip()
            annotation = ":".join(pieces2[1:]).strip() if len(pieces2) > 1 else ""
            if pname == "self":
                continue
            if not re.fullmatch(r"\*{0,2}[A-Za-z_]\w*", pname) or not annotation:
                raise StubError(f"unsupported parameter '{part}' in method '{name}'")
            params.append((pname.lstrip("*"), annotation))
        methods.append(Method(name=name, params=params, returns=returns))

    if not methods:
        raise StubError("no method definitions found in code snippet")
    return methods


def python_snippet(question: dict) -> str:
    snippets = question.get("codeSnippets") or []
    for snippet in snippets:
        if snippet.get("langSlug") == "python3":
            return snippet["code"]
    raise StubError("snippet list contains no python3 entry")


def typing_imports(methods: list[Method]) -> list[str]:
    names: set[str] = set()
    for method in methods:
        for _, annotation in method.params:
            names |= _annotation_identifiers(annotation)
        names |= _annotation_identifiers(method.returns)
    usable = sorted(
        name
        for name in names
        if not name.startswith("_")
        and name[0:1].isupper()
        and hasattr(typing, name)
    )
    return usable


def helper_types_needed(methods: list[Method]) -> list[str]:
    names: set[str] = set()
    for method in methods:
        for _, annotation in method.params:
            names |= _annotation_identifiers(annotation)
        names |= _annotation_identifiers(method.returns)
    return [helper for helper in HELPER_DEFINITIONS if helper in names]


# ---------------------------------------------------------------------------
# Generated file assembly
# ---------------------------------------------------------------------------


def pascal_case(title: str) -> str:
    words = re.split(r"[^A-Za-z0-9]+", title)
    return "".join(word.capitalize() for word in words if word)


def build_solution_class(methods: list[Method]) -> list[str]:
    lines = ["class Solution:"]
    for method in methods:
        rendered_params = ["self"]
        for pname, annotation in method.params:
            rendered_params.append(f"{pname}: {annotation}")
        returns = f" -> {method.returns}" if method.returns else ""
        lines.append(f"    def {method.name}({', '.join(rendered_params)}){returns}:")
        lines.append("        pass  # TODO: implement")
    return lines


def build_test_case(
    methods: list[Method],
    test_name: str,
    examples: list[tuple[str, str]],
) -> list[str]:
    lines = [f"class {test_name}(unittest.TestCase):"]

    single_plain_method = (
        len(methods) == 1
        and methods[0].name != "__init__"
        and methods[0].returns.strip() not in ("", "None")
        and not helper_types_needed(methods)
    )

    for index, (input_text, output_text) in enumerate(examples, start=1):
        assignments = parse_input_assignments(input_text)
        converted_output = lc_literal_to_py(output_text)

        usable = (
            single_plain_method
            and assignments is not None
            and converted_output is not None
            and set(assignments) == set(methods[0].param_names)
            and not any(had_null for _, had_null in assignments.values())
            and not converted_output[1]
        )

        if usable:
            call_kwargs = ", ".join(
                f"{name}={assignments[name][0]}" for name in methods[0].param_names
            )
            lines.extend(
                [
                    f"    def test_example_{index}(self) -> None:",
                    f"        self.assertEqual("
                    f"Solution().{methods[0].name}({call_kwargs}), "
                    f"{converted_output[0]})",
                    "",
                ]
            )
        else:
            lines.extend(
                [
                    f"    def test_example_{index}(self) -> None:",
                    f"        # Input: {_one_line(input_text)}",
                    f"        # Output: {_one_line(output_text)}",
                    "        pass  "
                    "# TODO translate this example into an assertion by hand.",
                    "",
                ]
            )

    if not examples:
        lines.extend(
            [
                "    def test_example_1(self) -> None:",
                "        pass  # No machine-readable examples were provided.",
                "",
            ]
        )

    lines.extend(
        [
            "    def test_edgecase(self) -> None:",
            "        pass  # TODO add your own edge cases.",
        ]
    )
    return lines


def build_module(question: dict) -> str:
    slug = question["titleSlug"]
    url = f"https://leetcode.com/problems/{slug}/"
    title = question.get("title") or slug
    difficulty = question.get("difficulty") or "Unknown"

    blocks = parse_description(question["content"])
    description_lines = render_description(blocks)
    examples = extract_examples(blocks)

    methods = parse_solution_stub(python_snippet(question))
    needs_helpers = helper_types_needed(methods)
    typing_names = typing_imports(methods)

    header_lines = [
        f"# {url}",
        "#",
        f"# Title: {question.get('questionFrontendId', '?')}. {title}",
        f"# Difficulty: {difficulty}",
        "#",
    ]

    import_lines = ["from __future__ import annotations", ""]
    if typing_names:
        import_lines.append(f"from typing import {', '.join(typing_names)}")
    import_lines.append("")
    import_lines.append("import unittest")

    solution_lines = build_solution_class(methods)

    helper_lines: list[str] = []
    if needs_helpers:
        for helper in needs_helpers:
            if helper_lines:
                helper_lines.append("#")
            helper_lines.extend(HELPER_DEFINITIONS[helper])

    test_name = "Test" + (pascal_case(title) or "Problem")
    test_lines = build_test_case(methods, test_name, examples)

    sections = [
        *header_lines,
        *description_lines,
        "",
        "",
        *import_lines,
        "",
        "",
        *solution_lines,
    ]
    if helper_lines:
        sections += ["", "", *helper_lines]
    sections += ["", "", *test_lines, "", "", 'if __name__ == "__main__":', "    unittest.main()", ""]

    return "\n".join(sections)


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------


def find_existing(output_root: Path, slug: str) -> Path | None:
    for directory in DIFFICULTY_DIRS.values():
        candidate = output_root / directory / f"{slug}.py"
        if candidate.exists():
            return candidate
    return None


def process_slug(slug: str, args: argparse.Namespace) -> tuple[str, str]:
    existing = find_existing(args.output_dir, slug)
    if existing and not args.force:
        return "SKIPPED", f"{existing.relative_to(args.output_dir)} already exists"

    question = fetch_question(slug, args.timeout)

    difficulty_dir = DIFFICULTY_DIRS.get(question.get("difficulty"))
    if difficulty_dir is None:
        return "FAILED", f"unknown difficulty '{question.get('difficulty')}'"

    module_source = build_module(question)
    target = args.output_dir / difficulty_dir / f"{slug}.py"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(module_source, encoding="utf-8")
    verb = "OVERWROTE" if existing else "CREATED"
    return verb, str(target.relative_to(args.output_dir))


def read_slug_file(path: Path) -> list[tuple[int, str | None]]:
    entries: list[tuple[int, str | None]] = []
    seen: set[str] = set()
    text = path.read_text(encoding="utf-8")
    for lineno, raw_line in enumerate(text.splitlines(), start=1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        slug = extract_slug(line)
        if slug is None:
            entries.append((lineno, None))
        elif slug in seen:
            continue
        else:
            seen.add(slug)
            entries.append((lineno, slug))
    return entries


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Generate offline LeetCode unittest scaffolds from a URL list.",
    )
    parser.add_argument("urls_file", type=Path, help="text file with one URL per line")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parent,
        help="root folder for easy/, medium/, hard/ (default: next to this script)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="re-download and overwrite existing files",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=DEFAULT_TIMEOUT_S,
        help=f"per-request timeout in seconds (default: {DEFAULT_TIMEOUT_S:g})",
    )
    args = parser.parse_args(argv)

    if not args.urls_file.is_file():
        parser.error(f"urls file not found: {args.urls_file}")

    entries = read_slug_file(args.urls_file)
    if not entries:
        print(f"No URLs found in {args.urls_file}", file=sys.stderr)
        return 1

    counts = {"CREATED": 0, "OVERWROTE": 0, "SKIPPED": 0, "FAILED": 0}
    failures: list[str] = []

    for lineno, slug in entries:
        label = slug if slug else f"line {lineno} (unrecognised)"
        try:
            if slug is None:
                raise FetchError("not a LeetCode URL or slug")
            status, detail = process_slug(slug, args)
        except FetchError as exc:
            status, detail = "FAILED", str(exc)
        except (StubError, KeyError, OSError) as exc:
            status, detail = "FAILED", f"{type(exc).__name__}: {exc}"
        counts[status] += 1
        marker = "!" if status == "FAILED" else " "
        print(f"{marker} {status:<9} {label:<60} {detail}")
        if status == "FAILED":
            failures.append(label)
        time.sleep(REQUEST_DELAY_S)

    print(
        f"\nDone: {counts['CREATED']} created, {counts['OVERWROTE']} overwritten,"
        f" {counts['SKIPPED']} skipped, {counts['FAILED']} failed"
        f" (of {len(entries)} entries)."
    )
    if counts["FAILED"]:
        print(f"Failures: {', '.join(failures)}", file=sys.stderr)
    return 1 if counts["FAILED"] == len(entries) else 0


if __name__ == "__main__":
    sys.exit(main())
