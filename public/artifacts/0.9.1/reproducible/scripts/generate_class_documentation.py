from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RELEASE_ROOT = ROOT.parent
MODEL_FILE = ROOT / "generated" / "OntoJourneyCore.json"
MARKDOWN_FILE = RELEASE_ROOT / "CLASS_DEFINITIONS.md"
LATEX_FILE = RELEASE_ROOT / "article" / "appendix_class_definitions.tex"

GROUPS = (
    (
        "Information objects and descriptions",
        (
            "InformationObject",
            "Description",
            "NarrativeContent",
            "NormativeDescription",
            "PlanDescription",
            "GoalDescription",
            "ConditionDescription",
        ),
    ),
    (
        "Journey models and model-level specifications",
        (
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
        ),
    ),
    (
        "Executions and internal events",
        (
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
        ),
    ),
    (
        "Situations and participants",
        (
            "RealizedTransformation",
            "ClosureSituation",
            "Person",
            "Protagonist",
            "Learner",
        ),
    ),
    (
        "HLJ stage specialization",
        ("HLJStageSpecification",),
    ),
)

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


def latex_escape(text: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(character, character) for character in text)


def break_identifier(identifier: str) -> str:
    parts = re.findall(r"[A-Z]+(?=[A-Z][a-z]|$)|[A-Z]?[a-z]+|\d+", identifier)
    return r"\allowbreak{}".join(parts) if parts else identifier


def load_classes() -> dict[str, dict[str, object]]:
    project = json.loads(MODEL_FILE.read_text(encoding="utf-8"))
    classes = {
        element["name"]: element
        for element in iter_elements(project)
        if element.get("type") == "Class"
        and isinstance(element.get("name"), str)
        and element["name"] not in PRIMITIVE_DATATYPES
    }
    expected_names = {name for _, names in GROUPS for name in names}
    if set(classes) != expected_names:
        missing = sorted(expected_names - set(classes))
        unexpected = sorted(set(classes) - expected_names)
        raise ValueError(f"Class grouping mismatch; missing={missing}, unexpected={unexpected}")
    for name, class_ in classes.items():
        if not english_text(class_.get("description")):
            raise ValueError(f"Missing English description for {name}")
    return classes


def generate_markdown(classes: dict[str, dict[str, object]]) -> str:
    lines = [
        "# OntoJourney Core v0.9.1 — class definitions",
        "",
        "This document is generated from the English `description` values in the canonical Tonto model. Do not edit it independently.",
        "",
    ]
    for title, names in GROUPS:
        lines.extend(
            [
                f"## {title}",
                "",
                "| Class | OntoUML stereotype | Definition |",
                "|---|---|---|",
            ]
        )
        for name in names:
            class_ = classes[name]
            description = english_text(class_.get("description"))
            lines.append(f"| `{name}` | `{class_.get('stereotype')}` | {description} |")
        lines.append("")
    return "\n".join(lines)


def generate_latex(classes: dict[str, dict[str, object]]) -> str:
    lines = [
        "% Generated from OntoJourneyCore.json; do not edit independently.",
        r"\begingroup",
        r"\small",
        r"\setlength{\LTleft}{0pt}",
        r"\setlength{\LTright}{0pt}",
        r"\setlength{\tabcolsep}{4pt}",
        r"\renewcommand{\arraystretch}{1.12}",
        r"\captionof{table}{Definitions of the 40 classes in OntoJourney Core v0.9.1.}",
        r"\label{tab:ontojourney-class-definitions}",
        r"\begin{longtable}{@{}>{\raggedright\arraybackslash}p{0.27\textwidth}>{\raggedright\arraybackslash}p{0.16\textwidth}>{\raggedright\arraybackslash}p{0.49\textwidth}@{}}",
        r"\toprule",
        r"\textbf{Class} & \textbf{Stereotype} & \textbf{Definition} \\",
        r"\midrule",
        r"\endfirsthead",
        r"\multicolumn{3}{@{}l}{\small\itshape Table~\ref{tab:ontojourney-class-definitions} continued}\\",
        r"\toprule",
        r"\textbf{Class} & \textbf{Stereotype} & \textbf{Definition} \\",
        r"\midrule",
        r"\endhead",
        r"\midrule",
        r"\multicolumn{3}{r@{}}{\small Continued on the next page}\\",
        r"\endfoot",
        r"\bottomrule",
        r"\endlastfoot",
    ]

    for title, names in GROUPS:
        lines.append(
            rf"\multicolumn{{3}}{{@{{}}l}}{{\textit{{{latex_escape(title)}}}}}\\*"
        )
        for name in names:
            class_ = classes[name]
            description = latex_escape(english_text(class_.get("description")))
            stereotype = break_identifier(latex_escape(str(class_.get("stereotype"))))
            identifier = break_identifier(name)
            lines.append(
                rf"\texttt{{{identifier}}} & \texttt{{{stereotype}}} & {description} \\"
            )
        lines.append(r"\addlinespace[2pt]")

    lines.extend([r"\end{longtable}", r"\endgroup", ""])
    return "\n".join(lines)


def main() -> None:
    classes = load_classes()
    MARKDOWN_FILE.write_text(generate_markdown(classes), encoding="utf-8")
    LATEX_FILE.write_text(generate_latex(classes), encoding="utf-8")
    print(f"Generated class documentation for {len(classes)} classes.")


if __name__ == "__main__":
    main()
