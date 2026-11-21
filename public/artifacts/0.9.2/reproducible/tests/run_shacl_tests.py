from pathlib import Path
import sys

from pyshacl import validate
from rdflib import Graph


ROOT = Path(__file__).resolve().parents[1]
SHAPES = ROOT / "shacl" / "ontojourney-core-v0.9.2.shacl.ttl"
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
            "must prescribe at least one Intended Learning Transformation",
            "must not directly precede itself",
            "must have exactly one Challenge Specification",
        ),
    ),
    (
        "negative_missing_learning_transformation.ttl",
        False,
        (
            "must prescribe at least one Intended Learning Transformation",
        ),
    ),
    (
        "negative_execution_model_types.ttl",
        False,
        (
            "must execute exactly one Narrative Journey Model",
            "must execute exactly one Heroic Narrative Journey Model",
            "must execute exactly one Learning Journey Model",
            "must execute exactly one Heroic Narrative Learning Journey Model",
        ),
    ),
    (
        "negative_model_stage_coherence.ttl",
        False,
        (
            "must execute a Stage Specification belonging to the executed Journey Model",
        ),
    ),
    (
        "negative_hlj_stage_type.ttl",
        False,
        (
            "must execute exactly one HLJ Stage Specification",
        ),
    ),
    (
        "negative_same_stage_encounter.ttl",
        False,
        (
            "must refer to a Challenge Specification of the same executed HLJ stage",
        ),
    ),
    (
        "negative_same_stage_performance.ttl",
        False,
        (
            "must address a Challenge Specification of the same executed HLJ stage",
        ),
    ),
    (
        "negative_same_stage_assistance.ttl",
        False,
        (
            "must realize the Assistance Specification of the same executed HLJ stage",
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
            meta_shacl=True,
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
