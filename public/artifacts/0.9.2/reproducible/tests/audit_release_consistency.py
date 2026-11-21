from __future__ import annotations

import importlib.util
import json
import re
import sys
from pathlib import Path

from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.compare import isomorphic
from rdflib.namespace import DCTERMS, OWL, RDF, RDFS, XSD


sys.dont_write_bytecode = True


ROOT = Path(__file__).resolve().parents[1]
RELEASE_ROOT = ROOT.parent
ONTOLOGY_IRI = URIRef("https://w3id.org/ontojourney/core")
VERSION_IRI = URIRef("https://w3id.org/ontojourney/core/0.9.2")
CORE = Namespace("https://w3id.org/ontojourney/core#")

SOURCE_FILE = ROOT / "src" / "core.tonto"
GENERATED_JSON = ROOT / "generated" / "OntoJourneyCore.json"
GENERATED_TURTLE = ROOT / "generated" / "OntoJourneyCore.ttl"
SHACL_FILE = ROOT / "shacl" / "ontojourney-core-v0.9.2.shacl.ttl"

SERIALIZATIONS = (
    (RELEASE_ROOT / "ontojourney-core.ttl", "turtle"),
    (RELEASE_ROOT / "ontojourney-core.rdf", "xml"),
    (RELEASE_ROOT / "ontojourney-core.jsonld", "json-ld"),
    (RELEASE_ROOT / "ontojourney-core.nt", "nt"),
)


def iter_elements(value: object):
    if isinstance(value, dict):
        if value.get("type"):
            yield value
        for nested in value.values():
            yield from iter_elements(nested)
    elif isinstance(value, list):
        for nested in value:
            yield from iter_elements(nested)


def english_text(value: object) -> str:
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, dict):
        for language in ("en", "en-GB", "en-US"):
            text = value.get(language)
            if isinstance(text, str) and text.strip():
                return text.strip()
    return ""


def json_definitions() -> dict[str, str]:
    project = json.loads(GENERATED_JSON.read_text(encoding="utf-8"))
    definitions = {
        element["name"]: english_text(element.get("description"))
        for element in iter_elements(project)
        if element.get("type") == "Class"
        and isinstance(element.get("name"), str)
        and element["name"]
        not in {"number", "string", "boolean", "date", "time", "datetime", "undefined"}
    }
    assert len(definitions) == 40, len(definitions)
    assert all(definitions.values())
    return definitions


def tonto_definitions() -> dict[str, str]:
    text = SOURCE_FILE.read_text(encoding="utf-8")
    pattern = re.compile(
        r"(?ms)^\s*(?:kind|subkind|event|situation|historicalRole)\s+"
        r"(?P<name>[A-Za-z][A-Za-z0-9]*)[^\{]*\{\s*"
        r"description\s*\{\s*@en\s*\"(?P<definition>(?:[^\"\\]|\\.)*)\"\s*\}\s*\}"
    )
    definitions = {
        match.group("name"): json.loads(f'"{match.group("definition")}"')
        for match in pattern.finditer(text)
    }
    assert len(definitions) == 40, len(definitions)
    return definitions


def load_documentation_generator():
    path = ROOT / "scripts" / "generate_class_documentation.py"
    spec = importlib.util.spec_from_file_location("generate_class_documentation", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def assert_generated_documentation() -> None:
    generator = load_documentation_generator()
    classes = generator.load_classes()
    expected_markdown = generator.generate_markdown(classes)
    expected_latex = generator.generate_latex(classes)
    assert (RELEASE_ROOT / "CLASS_DEFINITIONS.md").read_text(
        encoding="utf-8"
    ) == expected_markdown
    assert (RELEASE_ROOT / "article" / "appendix_class_definitions.tex").read_text(
        encoding="utf-8"
    ) == expected_latex


def assert_rdf(definitions: dict[str, str]) -> None:
    graphs: list[Graph] = []
    for path, format_ in SERIALIZATIONS:
        graph = Graph().parse(path, format=format_)
        assert len(graph) == 370, (path.name, len(graph))
        assert (ONTOLOGY_IRI, OWL.versionIRI, VERSION_IRI) in graph
        assert (ONTOLOGY_IRI, OWL.versionInfo, Literal("0.9.2")) in graph
        assert (ONTOLOGY_IRI, DCTERMS.issued, Literal("2026-11-21", datatype=XSD.date)) in graph
        assert (
            ONTOLOGY_IRI,
            DCTERMS.modified,
            Literal("2026-11-21", datatype=XSD.date),
        ) in graph
        assert all((CORE[name], RDF.type, OWL.Class) in graph for name in definitions)
        rdf_definitions = {
            name: str(comment)
            for name in definitions
            for comment in graph.objects(CORE[name], RDFS.comment)
            if isinstance(comment, Literal) and comment.language == "en"
        }
        assert rdf_definitions == definitions, path.name
        graphs.append(graph)

    reference = graphs[0]
    for (path, _), graph in zip(SERIALIZATIONS[1:], graphs[1:]):
        assert isomorphic(reference, graph), path.name

    generated_graph = Graph().parse(GENERATED_TURTLE, format="turtle")
    assert isomorphic(reference, generated_graph)


def main() -> None:
    assert (RELEASE_ROOT / "core.tonto").read_bytes() == SOURCE_FILE.read_bytes()
    assert (RELEASE_ROOT / "OntoJourneyCore.json").read_bytes() == GENERATED_JSON.read_bytes()
    assert (RELEASE_ROOT / "ontojourney-core.ttl").read_bytes() == GENERATED_TURTLE.read_bytes()
    assert (RELEASE_ROOT / "ontojourney-core.shacl.ttl").read_bytes() == SHACL_FILE.read_bytes()
    assert (RELEASE_ROOT / "tonto.json").read_bytes() == (ROOT / "tonto.json").read_bytes()

    definitions = json_definitions()
    assert tonto_definitions() == definitions
    assert_generated_documentation()
    assert_rdf(definitions)

    codemeta = json.loads((RELEASE_ROOT / "codemeta.json").read_text(encoding="utf-8"))
    assert codemeta["version"] == "0.9.2"
    assert codemeta["datePublished"] == "2026-11-21"
    assert "developmentStatus" not in codemeta

    print(
        "Release consistency audit passed: canonical source copies match; "
        "40 definitions agree across Tonto, OntoUML JSON, four isomorphic RDF "
        "serializations, Markdown, and LaTeX; version metadata is 0.9.2."
    )


if __name__ == "__main__":
    main()
