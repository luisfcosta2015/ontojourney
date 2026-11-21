from __future__ import annotations

import json
import shutil
from pathlib import Path

from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import DCTERMS, OWL, RDF, RDFS, XSD


ROOT = Path(__file__).resolve().parents[1]
RELEASE_ROOT = ROOT.parent
JSON_FILE = ROOT / "generated" / "OntoJourneyCore.json"
TURTLE_FILE = ROOT / "generated" / "OntoJourneyCore.ttl"

ONTOLOGY_IRI = URIRef("https://w3id.org/ontojourney/core")
ENTITY_NAMESPACE = Namespace("https://w3id.org/ontojourney/core#")
VERSION_IRI = URIRef("https://w3id.org/ontojourney/core/0.9.2")
PRIOR_VERSION_IRI = URIRef("https://w3id.org/ontojourney/core/0.9.1")
VERSION_INFO = "0.9.2"
ISSUED = Literal("2026-11-21", datatype=XSD.date)
PRIMITIVE_DATATYPES = {
    "number",
    "string",
    "boolean",
    "date",
    "time",
    "datetime",
    "undefined",
}


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


def load_class_definitions() -> dict[str, str]:
    project = json.loads(JSON_FILE.read_text(encoding="utf-8"))
    definitions: dict[str, str] = {}
    for element in iter_elements(project):
        if (
            element.get("type") == "Class"
            and isinstance(element.get("name"), str)
            and element["name"] not in PRIMITIVE_DATATYPES
        ):
            description = english_text(element.get("description"))
            if not description:
                raise ValueError(f"Missing English description for {element['name']}")
            definitions[element["name"]] = description

    if len(definitions) != 40:
        raise ValueError(f"Expected 40 class definitions, found {len(definitions)}")
    return definitions


def main() -> None:
    definitions = load_class_definitions()
    graph = Graph().parse(TURTLE_FILE, format="turtle")

    graph.set((ONTOLOGY_IRI, DCTERMS.identifier, Literal("10.5281/zenodo.24420185")))
    graph.set((ONTOLOGY_IRI, OWL.versionIRI, VERSION_IRI))
    graph.set((ONTOLOGY_IRI, OWL.versionInfo, Literal(VERSION_INFO)))
    graph.set((ONTOLOGY_IRI, OWL.priorVersion, PRIOR_VERSION_IRI))
    graph.remove((ONTOLOGY_IRI, DCTERMS.issued, None))
    graph.set((ONTOLOGY_IRI, DCTERMS.modified, ISSUED))

    for name, definition in definitions.items():
        class_iri = ENTITY_NAMESPACE[name]
        if (class_iri, RDF.type, OWL.Class) not in graph:
            raise ValueError(f"Class IRI not found in transformed graph: {class_iri}")
        graph.remove((class_iri, RDFS.comment, None))
        graph.add((class_iri, RDFS.comment, Literal(definition, lang="en")))

    comment_count = sum(
        1
        for name in definitions
        if any(graph.objects(ENTITY_NAMESPACE[name], RDFS.comment))
    )
    if comment_count != 40:
        raise ValueError(f"Expected 40 class comments, found {comment_count}")

    graph.serialize(destination=TURTLE_FILE, format="turtle")
    shutil.copyfile(TURTLE_FILE, RELEASE_ROOT / "ontojourney-core.ttl")
    shutil.copyfile(JSON_FILE, RELEASE_ROOT / "OntoJourneyCore.json")
    graph.serialize(destination=RELEASE_ROOT / "ontojourney-core.rdf", format="xml")
    graph.serialize(destination=RELEASE_ROOT / "ontojourney-core.nt", format="nt")
    graph.serialize(
        destination=RELEASE_ROOT / "ontojourney-core.jsonld",
        format="json-ld",
        auto_compact=True,
    )

    print(
        "Release artifacts finalized: version 0.9.2, "
        "40 English class definitions, and four RDF serializations."
    )


if __name__ == "__main__":
    main()
