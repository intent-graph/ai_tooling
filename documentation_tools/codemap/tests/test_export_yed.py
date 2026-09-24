"""Tests for yEd GraphML export."""

from pathlib import Path
from xml.etree import ElementTree as ET

import pytest

from codemap.api import CodeMap
from codemap.export_yed import export_graphml

FIXTURES_DIR = Path(__file__).parent / "fixtures"
SAMPLE_PROJECT = FIXTURES_DIR / "sample_project"

# yEd GraphML namespaces
NS = {
    "g": "http://graphml.graphdrawing.org/xmlns",
    "y": "http://www.yworks.com/xml/graphml",
}


@pytest.fixture
def cm() -> CodeMap:
    return CodeMap.build(SAMPLE_PROJECT)


@pytest.fixture
def graphml_path(cm: CodeMap, tmp_path: Path) -> Path:
    out = tmp_path / "test.graphml"
    cm.export_yed(out)
    return out


# -- File creation -------------------------------------------------------------


class TestFileCreation:
    def test_creates_file(self, graphml_path: Path) -> None:
        assert graphml_path.exists()
        assert graphml_path.stat().st_size > 0

    def test_returns_path(self, cm: CodeMap, tmp_path: Path) -> None:
        out = tmp_path / "result.graphml"
        result = cm.export_yed(out)
        assert result == out

    def test_default_path(
        self, cm: CodeMap, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        # export_yed()'s default output path is tempfile.gettempdir(); redirect
        # it to a per-test tmp_path so the test never writes to a fixed
        # system-wide path (and needs no manual cleanup).
        monkeypatch.setattr("codemap.api.tempfile.gettempdir", lambda: str(tmp_path))
        result = cm.export_yed()
        assert result.exists()
        assert "sample_project" in result.name
        assert result.parent == tmp_path

    def test_standalone_function(self, cm: CodeMap, tmp_path: Path) -> None:
        out = tmp_path / "standalone.graphml"
        result = export_graphml(cm.graph, out)
        assert result == out
        assert out.exists()


# -- XML validity --------------------------------------------------------------


class TestXMLValidity:
    def test_parses_as_xml(self, graphml_path: Path) -> None:
        tree = ET.parse(graphml_path)
        assert tree.getroot() is not None

    def test_root_is_graphml(self, graphml_path: Path) -> None:
        tree = ET.parse(graphml_path)
        root = tree.getroot()
        assert root.tag == f"{{{NS['g']}}}graphml"

    def test_has_key_declarations(self, graphml_path: Path) -> None:
        tree = ET.parse(graphml_path)
        root = tree.getroot()
        keys = root.findall("g:key", NS)
        key_ids = {k.get("id") for k in keys}
        assert "d6" in key_ids, "Missing nodegraphics key"
        assert "d10" in key_ids, "Missing edgegraphics key"

    def test_has_graph_element(self, graphml_path: Path) -> None:
        tree = ET.parse(graphml_path)
        root = tree.getroot()
        graphs = root.findall("g:graph", NS)
        assert len(graphs) >= 1


# -- Node structure ------------------------------------------------------------


class TestNodes:
    def test_has_nodes(self, graphml_path: Path) -> None:
        tree = ET.parse(graphml_path)
        root = tree.getroot()
        # Nodes can be at any nesting level (groups contain nested graphs)
        nodes = root.findall(".//g:node", NS)
        assert len(nodes) > 0

    def test_every_node_has_visual_data(self, graphml_path: Path) -> None:
        tree = ET.parse(graphml_path)
        root = tree.getroot()
        for node in root.findall(".//g:node", NS):
            data_elems = node.findall("g:data", NS)
            data_keys = {d.get("key") for d in data_elems}
            assert "d6" in data_keys, f"Node {node.get('id')} missing visual data"

    def test_group_nodes_have_foldertype(self, graphml_path: Path) -> None:
        tree = ET.parse(graphml_path)
        root = tree.getroot()
        # Groups have nested <graph> children
        for node in root.findall(".//g:node", NS):
            nested = node.findall("g:graph", NS)
            if nested:
                assert node.get("yfiles.foldertype") == "group", (
                    f"Group node {node.get('id')} missing foldertype"
                )

    def test_duplicate_names_use_qualified_label(self, cm: CodeMap, tmp_path: Path) -> None:
        out = tmp_path / "flat.graphml"
        cm.export_yed(out, flat=True)

        tree = ET.parse(out)
        root = tree.getroot()

        name_counts: dict[str, int] = {}
        for node in cm.graph.nodes.values():
            name_counts[node.name] = name_counts.get(node.name, 0) + 1
        duplicate_qnames = {
            node.qualified_name
            for node in cm.graph.nodes.values()
            if name_counts[node.name] > 1
        }
        assert duplicate_qnames, "Fixture should contain duplicated short names"

        for xml_node in root.findall(".//g:node", NS):
            qname_data = next(
                (d for d in xml_node.findall("g:data", NS) if d.get("key") == "d_qname"),
                None,
            )
            if qname_data is None or qname_data.text is None:
                continue
            qname = qname_data.text

            label_elem = xml_node.find('.//y:NodeLabel', NS)
            if label_elem is None or label_elem.text is None:
                continue

            if qname in duplicate_qnames:
                assert label_elem.text == qname, (
                    f"Expected disambiguated label for duplicate name node: {qname}"
                )


# -- Edge structure ------------------------------------------------------------


class TestEdges:
    def test_has_edges(self, graphml_path: Path) -> None:
        tree = ET.parse(graphml_path)
        root = tree.getroot()
        edges = root.findall(".//g:edge", NS)
        assert len(edges) > 0

    def test_every_edge_has_visual_data(self, graphml_path: Path) -> None:
        tree = ET.parse(graphml_path)
        root = tree.getroot()
        for edge in root.findall(".//g:edge", NS):
            data_elems = edge.findall("g:data", NS)
            data_keys = {d.get("key") for d in data_elems}
            assert "d10" in data_keys, f"Edge {edge.get('id')} missing visual data"

    def test_no_contains_edges(self, cm: CodeMap, graphml_path: Path) -> None:
        """CONTAINS edges are expressed via group nesting, not edge elements."""
        # The contains edge style is not in our _EDGE_STYLE table,
        # so no edge should use a grey dashed style.
        # More directly: count edges in XML vs non-contains edges in graph.
        tree = ET.parse(graphml_path)
        root = tree.getroot()
        xml_edges = root.findall(".//g:edge", NS)
        graph_non_contains = [
            e for e in cm.graph.edges if e.kind.value != "contains"
        ]
        # XML edges should be <= non-contains (some may be filtered as dangling)
        assert len(xml_edges) <= len(graph_non_contains)

    def test_edge_sources_targets_exist(self, graphml_path: Path) -> None:
        tree = ET.parse(graphml_path)
        root = tree.getroot()
        # Collect all node IDs (at any nesting level)
        all_node_ids = {n.get("id") for n in root.findall(".//g:node", NS)}
        for edge in root.findall(".//g:edge", NS):
            src = edge.get("source")
            tgt = edge.get("target")
            assert src in all_node_ids, f"Edge source {src} not in node set"
            assert tgt in all_node_ids, f"Edge target {tgt} not in node set"
