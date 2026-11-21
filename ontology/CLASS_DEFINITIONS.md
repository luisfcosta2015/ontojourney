# OntoJourney Core v0.9.2 — class definitions

This document is generated from the English `description` values in the canonical Tonto model. Do not edit it independently.

## Information objects and descriptions

| Class | OntoUML stereotype | Definition |
|---|---|---|
| `InformationObject` | `kind` | An entity whose identity is determined by its informational content and that may be expressed through different physical or digital carriers. |
| `Description` | `subkind` | An Information Object that expresses a conceptualization of entities or configurations and provides criteria for interpreting or assessing them. |
| `NarrativeContent` | `subkind` | An Information Object that organises characters, events, or themes as narrative content, independently of the medium through which it is expressed. |
| `NormativeDescription` | `subkind` | A Description that prescribes, permits, or evaluates possible actions or situations instead of merely characterising them. |
| `PlanDescription` | `subkind` | A Normative Description that prescribes or organises intended actions and events towards a purpose. |
| `GoalDescription` | `subkind` | A Normative Description whose propositional content describes a situation intended to be attained. |
| `ConditionDescription` | `subkind` | A Normative Description that specifies a condition against which a situation can be assessed. |

## Journey models and model-level specifications

| Class | OntoUML stereotype | Definition |
|---|---|---|
| `JourneyModel` | `subkind` | A Description that characterises a reusable journey pattern through one or more Stage Specifications and one Closure Specification, and may prescribe Intended Transformations. |
| `NarrativeJourneyModel` | `subkind` | A Journey Model whose overall progression is organised by exactly one Journey Narrative. |
| `HeroicNarrativeJourneyModel` | `subkind` | A Narrative Journey Model that frames a meaningful progression through demanding stages towards transformation and closure as a heroic trajectory. |
| `LearningJourneyModel` | `subkind` | A Journey Model and Plan Description that intentionally organises an educational experience and has at least one Educational Purpose. |
| `HeroicNarrativeLearningJourneyModel` | `subkind` | A Heroic Narrative Journey Model and Learning Journey Model whose identity includes one Journey Narrative, at least two connected Stage Specifications, at least one challenged stage, at least one Educational Purpose, at least one Intended Learning Transformation, and one Closure Specification. |
| `StageSpecification` | `subkind` | A Description that characterises a model-specific stage of a Journey Model, whether as a descriptive pattern or as a prescribed part of a plan, and may be linked to other Stage Specifications through directlyPrecedesStage. |
| `JourneyNarrative` | `subkind` | Narrative Content that organises the narrative progression of a Narrative Journey Model as a whole. |
| `NarrativeFraming` | `subkind` | Narrative Content that gives one HLJ Stage Specification its local narrative context and connects it to the wider journey. |
| `IntendedTransformation` | `subkind` | A Goal Description prescribed by a Journey Model that specifies a transformation the model is intended to bring about. |
| `IntendedLearningTransformation` | `subkind` | An Intended Transformation that specifies a learning-related change to be pursued through a learning journey. |
| `EducationalPurpose` | `subkind` | A Goal Description that states an educational aim of a Learning Journey Model. |
| `MissionSpecification` | `subkind` | A Normative Description that states what the Learner is invited or expected to pursue within an HLJ stage and may combine a desired result with directions for action. |
| `ClosureSpecification` | `subkind` | A Condition Description defined by a Journey Model that states the condition under which an execution of the model counts as having reached closure. |
| `ChallengeSpecification` | `subkind` | A Normative Description assigned to a Stage Specification that describes a demand, obstacle, problem, task, or condition that makes progression demanding. |
| `AssistanceSpecification` | `subkind` | A Normative Description of support intended to be made available within an HLJ Stage Specification. |

## Executions and internal events

| Class | OntoUML stereotype | Definition |
|---|---|---|
| `JourneyExecution` | `event` | A complex event in which one Journey Model is enacted in a particular context through one or more Stage Executions. |
| `NarrativeJourneyExecution` | `event` | A Journey Execution of a Narrative Journey Model in which the performed stages enact a narratively organised journey. |
| `HeroicNarrativeJourneyExecution` | `event` | A Narrative Journey Execution of a Heroic Narrative Journey Model that constitutes one focal heroic trajectory with exactly one Protagonist. |
| `LearningJourneyExecution` | `event` | A Journey Execution of a Learning Journey Model in which at least one Person participates as Learner. |
| `HeroicNarrativeLearningJourneyExecution` | `event` | A Heroic Narrative Journey Execution and Learning Journey Execution of one Heroic Narrative Learning Journey Model, with exactly one focal Person participating as both Protagonist and Learner. |
| `SuccessfulHeroicNarrativeLearningJourneyExecution` | `event` | A Heroic Narrative Learning Journey Execution that produces a Closure Situation satisfying the executed model's Closure Specification and at least one Realized Transformation of the focal Person satisfying an Intended Learning Transformation prescribed by that model. |
| `StageExecution` | `event` | An event within a Journey Execution that enacts one Stage Specification belonging to the executed Journey Model. |
| `HLJStageExecution` | `event` | A Stage Execution of an HLJ Stage Specification that may include Challenge Encounters, Challenge Performances, and Assistance Provisions connected to specifications of that same stage. |
| `TransformationEvent` | `event` | An event within a Journey Execution that brings about one Realized Transformation. |
| `ChallengeEncounter` | `event` | An event within an HLJ Stage Execution in which the specified challenge of that stage is faced, whether or not it is successfully addressed. |
| `ChallengePerformance` | `event` | An event within an HLJ Stage Execution in which action is directed towards the specified challenge of that stage; its occurrence does not by itself imply success. |
| `AssistanceProvision` | `event` | An event within an HLJ Stage Execution in which assistance specified for that stage is provided. |

## Situations and participants

| Class | OntoUML stereotype | Definition |
|---|---|---|
| `RealizedTransformation` | `situation` | A situation brought about by one or more Transformation Events that represents an actual change concerning exactly one Person and satisfies one Intended Transformation. |
| `ClosureSituation` | `situation` | A situation brought about by a Journey Execution that satisfies a Closure Specification; in a successful execution, that specification is defined by the executed model. |
| `Person` | `kind` | A human individual who may participate in Journey Executions and whose identity is preserved across the historical roles Protagonist and Learner. |
| `Protagonist` | `historicalRole` | A historical role instantiated by a Person through participation as the focal subject of a Heroic Narrative Journey Execution. |
| `Learner` | `historicalRole` | A historical role instantiated by a Person through participation in a Learning Journey Execution. |

## HLJ stage specialization

| Class | OntoUML stereotype | Definition |
|---|---|---|
| `HLJStageSpecification` | `subkind` | A Stage Specification and Plan Description in the Heroine's Learning Journey anatomy that contains exactly one Narrative Framing, Mission Specification, Challenge Specification, and Assistance Specification. |
