"""Anchor generation and duplicate handling.

Implements GitHub's heading-slug algorithm (as used to render `#anchors` for
Markdown headings on github.com), not a generic slugify:

1. Strip inline markdown markup from the heading text so the anchor is
   computed from the *rendered* heading text, the way GitHub does:
   a. Extract code spans (`` `...` ``) first and hold their contents aside,
      literally — GFM code-span content is never touched by emphasis
      parsing, so backticks-only characters go, everything inside stays as-is
      (underscores, asterisks, etc. all survive).
   b. Reduce `[text](url)` links to `text`.
   c. Remove `*`/`**`/`***` and `~~` emphasis/strikethrough delimiters
      unconditionally (simplification: GFM only pairs them within non-code
      spans, which is the common case here).
   d. Remove `_`/`__`/`___` delimiters ONLY when they form a matched,
      non-intraword emphasis pair (see `_UNDERSCORE_EMPHASIS_PATTERN`).
      Intraword underscores (`line_profiler`, `STEP_IO_PROTOCOL`) and
      unpaired leading underscores (`_private`) are not emphasis in GFM and
      must stay.
   e. Splice the held-aside code-span contents back in.
2. Lowercase.
3. Remove every character that is not a Unicode letter/number, `-`, `_` or
   space. Python's `\\w` is Unicode-aware and already includes `_`, so
   `re.sub(r"[^\\w\\- ]", "", s)` keeps letters (accented or not), digits,
   underscores, hyphens and spaces, and drops everything else (`.`, `&`,
   `:`, …) *without* substituting a hyphen for it.
4. Replace each remaining space with `-`. Spaces are not collapsed first, so
   adjacent spaces (e.g. from removed punctuation) become adjacent hyphens:
   "Code & Examples" → "code--examples".

Duplicate headings get `-1`, `-2`, ... suffixes in document order
(`make_unique_anchors`), matching GitHub's behavior.
"""

import re

# Inline markdown to strip before slugifying, in GitHub's rendered-text sense:
# - Markdown links: [text](url) -> text
# - Emphasis / strong / strikethrough markers: *, ~ always; _ conditionally
#   (see _UNDERSCORE_EMPHASIS_PATTERN below)
# - Inline code backticks (content extracted separately, see _extract_code_spans)
_LINK_PATTERN = re.compile(r"\[([^\]]*)\]\([^)]*\)")
_CODE_SPAN_PATTERN = re.compile(r"`+(.+?)`+")
_STAR_TILDE_EMPHASIS_PATTERN = re.compile(r"(\*\*\*|\*\*|\*|~~)")

# `_`/`__`/`___` delimit emphasis only when NOT intraword (GFM rule): the
# opener must be preceded by start-of-string/whitespace/punctuation and
# followed by a non-space; the closer must be preceded by a non-space and
# followed by end-of-string/whitespace/punctuation. This leaves intraword
# underscores (line_profiler, STEP_IO_PROTOCOL, snake_case_name) and unpaired
# leading underscores (_private) untouched. Applied repeatedly (re.sub scans
# left-to-right and matches don't overlap, but a title can contain more than
# one emphasis span).
_UNDERSCORE_EMPHASIS_PATTERN = re.compile(r"(?<![\w])(_{1,3})(?=\S)(.+?)(?<=\S)\1(?![\w])")

# Placeholder used to hold code-span contents aside while other inline
# markdown is stripped, so their literal contents (underscores, asterisks,
# etc.) are immune to emphasis-stripping. Chosen to be extremely unlikely to
# collide with real heading text.
_CODE_SPAN_PLACEHOLDER = "\x00CODE{}\x00"

# GitHub keeps Unicode letters/numbers, '-', '_' and space; drops everything
# else without inserting a hyphen. Python's \w is Unicode-aware and includes
# '_', matching GitHub's own slugger.
_STRIP_PATTERN = re.compile(r"[^\w\- ]", re.UNICODE)


def _strip_inline_markdown(title: str) -> str:
    """Reduce inline markdown syntax to its rendered text, GitHub-style."""
    # 1. Extract code spans first: their content is literal in GFM, so hold
    #    it aside (immune to emphasis-stripping below) and splice it back in
    #    at the end.
    code_contents: list[str] = []

    def _hold_code_span(match: re.Match[str]) -> str:
        code_contents.append(match.group(1))
        return _CODE_SPAN_PLACEHOLDER.format(len(code_contents) - 1)

    s = _CODE_SPAN_PATTERN.sub(_hold_code_span, title)

    # 2. Links -> display text.
    s = _LINK_PATTERN.sub(r"\1", s)

    # 3. Star/tilde emphasis: always stripped.
    s = _STAR_TILDE_EMPHASIS_PATTERN.sub("", s)

    # 4. Underscore emphasis: stripped only when non-intraword and paired.
    while True:
        new_s = _UNDERSCORE_EMPHASIS_PATTERN.sub(r"\2", s)
        if new_s == s:
            break
        s = new_s

    # 5. Splice code-span contents back in, literally.
    for i, content in enumerate(code_contents):
        s = s.replace(_CODE_SPAN_PLACEHOLDER.format(i), content)

    return s


def slugify(title: str) -> str:
    """Convert a header title to GitHub's heading anchor slug.

    "My Section (v2)" → "my-section-v2"
    "Code & Examples" → "code--examples"
    "Hypothèse de départ" → "hypothèse-de-départ"
    """
    s = _strip_inline_markdown(title)
    s = s.strip().lower()
    s = _STRIP_PATTERN.sub("", s)
    s = s.replace(" ", "-")
    return s


def make_unique_anchors(titles: list[str]) -> list[str]:
    """Generate unique anchors for a list of titles.

    Handles duplicates by appending -1, -2, etc.
    """
    anchors: list[str] = []
    seen: dict[str, int] = {}

    for title in titles:
        base = slugify(title)
        if base in seen:
            seen[base] += 1
            anchor = f"{base}-{seen[base]}"
        else:
            seen[base] = 0
            anchor = base
        anchors.append(anchor)

    return anchors
