from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]
MODEL_FILE = ROOT / "generated" / "OntoJourneyCore.json"


def main() -> None:
    model = json.loads(MODEL_FILE.read_text(encoding="utf-8"))["model"]
    elements = [
        element
        for package in model.get("contents", [])
        for element in package.get("contents", [])
    ]
    classes = [
        element
        for element in elements
        if element.get("type") == "Class"
        and element.get("name")
        not in {"number", "string", "boolean", "date", "time", "datetime", "undefined"}
    ]
    relations = [element for element in elements if element.get("type") == "Relation"]
    generalizations = [
        element for element in elements if element.get("type") == "Generalization"
    ]
    by_id = {element["id"]: element for element in elements if element.get("id")}
    by_name = {element.get("name"): element for element in elements if element.get("name")}

    assert len(classes) == 40
    assert len(relations) == 27
    assert len(generalizations) == 33
    relation_names = [relation["name"] for relation in relations]
    assert len(relation_names) == len(set(relation_names))

    mission = by_name["MissionSpecification"]
    mission_parents = {
        by_id[generalization["general"]["id"]]["name"]
        for generalization in generalizations
        if generalization["specific"]["id"] == mission["id"]
    }
    assert mission_parents == {"NormativeDescription"}

    expected_relations = {
        "participatesAsProtagonistIn": (
            ("Protagonist", "1..1"),
            ("HeroicNarrativeJourneyExecution", "1..*"),
        ),
        "isTransformationOf": (
            ("RealizedTransformation", "0..*"),
            ("Person", "1..1"),
        ),
        "hasChallenge": (
            ("StageSpecification", "1..1"),
            ("ChallengeSpecification", "0..*"),
        ),
    }

    for relation_name, expected_ends in expected_relations.items():
        relation = by_name[relation_name]
        actual_ends = tuple(
            (
                by_id[property_["propertyType"]["id"]]["name"],
                property_["cardinality"],
            )
            for property_ in relation["properties"]
        )
        assert actual_ends == expected_ends, (relation_name, actual_ends)

    print(
        "Generated JSON audit passed: "
        "40 domain classes, 27 relations, 33 generalizations, "
        "and all v0.9 delta assertions satisfied."
    )


if __name__ == "__main__":
    main()
