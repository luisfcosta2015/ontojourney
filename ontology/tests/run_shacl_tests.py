from pathlib import Path
import sys

from pyshacl import validate
from rdflib import Graph


ROOT = Path(__file__).resolve().parents[1]
SHAPES = ROOT / "shacl" / "ontojourney-core-v0.9.shacl.ttl"
ONTOLOGY = ROOT / "generated" / "OntoJourneyCore.ttl"

CASES = (
    ("positive.ttl", True, ()),
    (
        "negative_focal_success.ttl",
        False,
        (
            "must be the same Person",
            "must concern its focal participant",
            "must realize an intended learning transformation",
        ),
    ),
    (
        "negative_model.ttl",
        False,
        (
            "two or more StageSpecification members",
            "hasChallenge path through one of its stages",
            "must not directly precede itself",
            "must have exactly one Challenge Specification",
        ),
    ),
)


def load(path: Path) -> Graph:
    graph = Graph()
    graph.parse(path, format="turtle")
    return graph


def main() -> int:
    shapes = load(SHAPES)
    ontology = load(ONTOLOGY)
    failed = False

    for filename, expected, expected_messages in CASES:
        conforms, _, report = validate(
            data_graph=load(ROOT / "tests" / "data" / filename),
            shacl_graph=shapes,
            ont_graph=ontology,
            inference="rdfs",
            advanced=True,
            abort_on_first=False,
        )
        print(f"{filename}: conforms={conforms}, expected={expected}")
        if conforms != expected:
            failed = True
            print(report)
            continue

        for message in expected_messages:
            if message not in report:
                failed = True
                print(f"Missing expected violation message: {message}")
                print(report)

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
