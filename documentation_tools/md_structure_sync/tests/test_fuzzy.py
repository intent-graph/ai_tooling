"""Tests for fuzzy anchor matching."""

import pytest

from md_structure_sync.fuzzy import (
    anchor_similarity,
    find_best_match,
    normalize_anchor,
)


class TestAnchorSimilarity:
    """Tests for anchor_similarity function."""

    def test_exact_match(self):
        score = anchor_similarity("section-one", "section-one")
        assert score == 1.0

    def test_case_insensitive(self):
        score = anchor_similarity("Section-One", "section-one")
        assert score == 1.0

    def test_similar_anchors(self):
        # Typo: "sectoin" vs "section"
        score = anchor_similarity("sectoin-one", "section-one")
        assert score > 0.8

    def test_different_anchors(self):
        score = anchor_similarity("introduction", "conclusion")
        assert score < 0.5

    def test_empty_anchor(self):
        assert anchor_similarity("", "section") == 0.0
        assert anchor_similarity("section", "") == 0.0
        assert anchor_similarity("", "") == 0.0

    def test_strip_hyphens(self):
        # Leading/trailing hyphens should be stripped
        score = anchor_similarity("-section-", "section")
        assert score == 1.0


class TestFindBestMatch:
    """Tests for find_best_match function."""

    def test_exact_match(self):
        available = ["intro", "section-one", "conclusion"]
        match, score = find_best_match("section-one", available)

        assert match == "section-one"
        assert score == 1.0

    def test_fuzzy_match_above_threshold(self):
        available = ["introduction", "section-one", "conclusion"]
        # Typo in search
        match, score = find_best_match("secton-one", available)

        assert match == "section-one"
        assert score >= 0.8

    def test_no_match_below_threshold(self):
        available = ["introduction", "conclusion"]
        match, score = find_best_match("completely-different", available)

        assert match is None
        assert score < 0.8

    def test_custom_threshold(self):
        available = ["section"]
        # "sectin" is close but not super close
        match, score = find_best_match("sectin", available, threshold=0.95)

        assert match is None  # Below 0.95 threshold

        match2, score2 = find_best_match("sectin", available, threshold=0.7)
        assert match2 == "section"  # Above 0.7 threshold

    def test_empty_available(self):
        match, score = find_best_match("section", [])
        assert match is None
        assert score == 0.0

    def test_empty_target(self):
        match, score = find_best_match("", ["section", "intro"])
        assert match is None
        assert score == 0.0

    def test_best_among_multiple(self):
        available = ["section-1", "section-2", "section-one"]
        match, score = find_best_match("section-one", available)

        assert match == "section-one"
        assert score == 1.0


class TestNormalizeAnchor:
    """Tests for normalize_anchor function."""

    def test_lowercase(self):
        assert normalize_anchor("Section-One") == "section-one"

    def test_url_decode_space(self):
        assert normalize_anchor("section%20one") == "section-one"

    def test_collapse_hyphens(self):
        assert normalize_anchor("section--one") == "section-one"
        assert normalize_anchor("a---b") == "a-b"

    def test_strip_hyphens(self):
        assert normalize_anchor("-section-") == "section"
        assert normalize_anchor("--intro--") == "intro"

    def test_empty(self):
        assert normalize_anchor("") == ""

    def test_combined(self):
        assert normalize_anchor("--Section%20One--") == "section-one"
