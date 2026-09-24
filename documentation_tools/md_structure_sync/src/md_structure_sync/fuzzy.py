"""Fuzzy matching for anchor validation."""

from difflib import SequenceMatcher


def anchor_similarity(anchor1: str, anchor2: str) -> float:
    """Compute similarity score between two anchors.

    Uses SequenceMatcher ratio which gives a value between 0 and 1.

    Args:
        anchor1: First anchor string
        anchor2: Second anchor string

    Returns:
        Similarity score between 0.0 and 1.0
    """
    if not anchor1 or not anchor2:
        return 0.0

    # Normalize: lowercase, strip leading/trailing hyphens
    a1 = anchor1.lower().strip("-")
    a2 = anchor2.lower().strip("-")

    if a1 == a2:
        return 1.0

    return SequenceMatcher(None, a1, a2).ratio()


def find_best_match(
    target_anchor: str,
    available_anchors: list[str],
    threshold: float = 0.8,
) -> tuple[str | None, float]:
    """Find the best matching anchor from available options.

    Args:
        target_anchor: The anchor we're trying to match
        available_anchors: List of valid anchors in the target file
        threshold: Minimum similarity score to consider a match

    Returns:
        Tuple of (best_match_anchor, similarity_score)
        Returns (None, 0.0) if no match above threshold
    """
    if not target_anchor or not available_anchors:
        return None, 0.0

    best_anchor = None
    best_score = 0.0

    for anchor in available_anchors:
        score = anchor_similarity(target_anchor, anchor)
        if score > best_score:
            best_score = score
            best_anchor = anchor

    if best_score >= threshold:
        return best_anchor, best_score

    return None, best_score


def normalize_anchor(anchor: str) -> str:
    """Normalize an anchor for comparison.

    Handles common variations:
    - Case differences
    - Trailing numbers (section-1 vs section)
    - URL encoding

    Args:
        anchor: Raw anchor string

    Returns:
        Normalized anchor for comparison
    """
    if not anchor:
        return ""

    # Lowercase
    result = anchor.lower()

    # URL decode common sequences
    result = result.replace("%20", "-")
    result = result.replace("%2d", "-")

    # Collapse multiple hyphens
    while "--" in result:
        result = result.replace("--", "-")

    # Strip leading/trailing hyphens
    result = result.strip("-")

    return result
