from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]
MODEL_FILE = ROOT / "generated" / "OntoJourneyCore.json"

EXPECTED_CLASS_NAMES = {
    "InformationObject",
    "Description",
    "NarrativeContent",
    "NormativeDescription",
    "PlanDescription",
    "GoalDescription",
    "ConditionDescription",
    "JourneyModel",
    "NarrativeJourneyModel",
    "HeroicNarrativeJourneyModel",
    "LearningJourneyModel",
    "HeroicNarrativeLearningJourneyModel",
    "StageSpecification",
    "JourneyNarrative",
    "NarrativeFraming",
    "IntendedTransformation",
    "IntendedLearningTransformation",
    "EducationalPurpose",
    "MissionSpecification",
    "ClosureSpecification",
    "ChallengeSpecification",
    "AssistanceSpecification",
    "JourneyExecution",
    "NarrativeJourneyExecution",
    "HeroicNarrativeJourneyExecution",
    "LearningJourneyExecution",
    "HeroicNarrativeLearningJourneyExecution",
    "SuccessfulHeroicNarrativeLearningJourneyExecution",
    "StageExecution",
    "HLJStageExecution",
    "TransformationEvent",
    "ChallengeEncounter",
    "ChallengePerformance",
    "AssistanceProvision",
    "RealizedTransformation",
    "ClosureSituation",
    "Person",
    "Protagonist",
    "Learner",
    "HLJStageSpecification",
}

EXPECTED_RELATION_NAMES = {
    "hasStage",
    "directlyPrecedesStage",
    "hasNarrative",
    "prescribesTransformation",
    "hasEducationalPurpose",
    "definesClosure",
    "isExecutionOfJourneyModel",
    "hasStageExecution",
    "isExecutionOfStageSpecification",
    "participatesAsProtagonistIn",
    "participatesAsLearnerIn",
    "hasTransformationEvent",
    "producesTransformation",
    "satisfiesIntendedTransformation",
    "isTransformationOf",
    "producesClosure",
    "satisfiesClosureSpecification",
    "hasNarrativeFraming",
    "hasMission",
    "hasAssistance",
    "hasChallenge",
    "hasChallengeEncounter",
    "hasChallengePerformance",
    "hasAssistanceProvision",
    "isEncounterOf",
    "addressesChallenge",
    "realizesAssistance",
}

EXPECTED_GENERALIZATIONS = {
    ("Description", "InformationObject"),
    ("NarrativeContent", "InformationObject"),
    ("NormativeDescription", "Description"),
    ("PlanDescription", "NormativeDescription"),
    ("GoalDescription", "NormativeDescription"),
    ("ConditionDescription", "NormativeDescription"),
    ("JourneyModel", "Description"),
    ("NarrativeJourneyModel", "JourneyModel"),
    ("HeroicNarrativeJourneyModel", "NarrativeJourneyModel"),
    ("LearningJourneyModel", "JourneyModel"),
    ("LearningJourneyModel", "PlanDescription"),
    ("HeroicNarrativeLearningJourneyModel", "HeroicNarrativeJourneyModel"),
    ("HeroicNarrativeLearningJourneyModel", "LearningJourneyModel"),
    ("StageSpecification", "PlanDescription"),
    ("JourneyNarrative", "NarrativeContent"),
    ("NarrativeFraming", "NarrativeContent"),
    ("IntendedTransformation", "GoalDescription"),
    ("IntendedLearningTransformation", "IntendedTransformation"),
    ("EducationalPurpose", "GoalDescription"),
    ("MissionSpecification", "NormativeDescription"),
    ("ClosureSpecification", "ConditionDescription"),
    ("ChallengeSpecification", "NormativeDescription"),
    ("AssistanceSpecification", "NormativeDescription"),
    ("NarrativeJourneyExecution", "JourneyExecution"),
    ("HeroicNarrativeJourneyExecution", "NarrativeJourneyExecution"),
    ("LearningJourneyExecution", "JourneyExecution"),
    ("HeroicNarrativeLearningJourneyExecution", "HeroicNarrativeJourneyExecution"),
    ("HeroicNarrativeLearningJourneyExecution", "LearningJourneyExecution"),
    ("SuccessfulHeroicNarrativeLearningJourneyExecution", "HeroicNarrativeLearningJourneyExecution"),
    ("HLJStageExecution", "StageExecution"),
    ("Protagonist", "Person"),
    ("Learner", "Person"),
    ("HLJStageSpecification", "StageSpecification"),
}


def has_english_description(value: object) -> bool:
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, dict):
        return any(
            isinstance(text, str) and text.strip()
            for language, text in value.items()
            if language.lower() in {"en", "en-gb", "en-us"}
        )
    return False


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
    class_names = {class_["name"] for class_ in classes}
    relation_names = {relation["name"] for relation in relations}
    actual_generalizations = {
        (
            by_id[generalization["specific"]["id"]]["name"],
            by_id[generalization["general"]["id"]]["name"],
        )
        for generalization in generalizations
    }
    assert class_names == EXPECTED_CLASS_NAMES
    assert relation_names == EXPECTED_RELATION_NAMES
    assert actual_generalizations == EXPECTED_GENERALIZATIONS
    missing_descriptions = sorted(
        class_["name"]
        for class_ in classes
        if not has_english_description(class_.get("description"))
    )
    assert not missing_descriptions, missing_descriptions

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
        "40 English class descriptions, and all v0.9.1 identity assertions satisfied."
    )


if __name__ == "__main__":
    main()
