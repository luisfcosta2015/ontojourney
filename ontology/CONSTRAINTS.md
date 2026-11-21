# OntoJourney Core v0.9.2 — constraint policy

OntoJourney uses three complementary representations. The Tonto source records the conceptual taxonomy, relation stereotypes, and multiplicities. The gUFO-aligned RDF serializations expose the taxonomy and relation domains and ranges under open-world semantics. The SHACL graph operationalizes selected cardinality and cross-path requirements that must reject incomplete or incoherent instance data.

The SHACL graph is therefore part of the normative release. Conformance to the OWL graph alone does not establish conformance to the full OntoJourney model.

## Focal participation and transformation

- Every `HeroicNarrativeJourneyExecution` has exactly one focal `Protagonist`.
- Every `HeroicNarrativeLearningJourneyExecution` has exactly one focal `Learner`, and the same `Person` participates as both `Protagonist` and `Learner`.
- Every `RealizedTransformation` concerns exactly one `Person`.
- Every transformation produced within a heroic narrative learning execution concerns its focal participant.

## Model identity and execution typing

- Every `HeroicNarrativeLearningJourneyModel` has at least two `StageSpecification` members, contains at least one challenged stage, and has two distinct stages connected by `directlyPrecedesStage`.
- Every `HeroicNarrativeLearningJourneyModel` prescribes at least one `IntendedLearningTransformation`.
- `NarrativeJourneyExecution`, `HeroicNarrativeJourneyExecution`, `LearningJourneyExecution`, and `HeroicNarrativeLearningJourneyExecution` execute exactly one model of their corresponding model subtype.

## Stage progression and execution coherence

- A `StageSpecification` does not directly precede itself.
- Directly related stage specifications share at least one `JourneyModel`.
- Every `StageExecution` aggregated by a `JourneyExecution` executes a `StageSpecification` belonging to the model executed by that journey execution.
- Every `HLJStageExecution` executes exactly one `HLJStageSpecification`.

## HLJ stage anatomy and same-stage links

- Every `HLJStageSpecification` has exactly one `ChallengeSpecification`. The Tonto source also assigns exactly one `NarrativeFraming`, `MissionSpecification`, and `AssistanceSpecification`.
- A `ChallengeEncounter` in an `HLJStageExecution` refers to a challenge of the same executed stage.
- A `ChallengePerformance` in an `HLJStageExecution` addresses a challenge of the same executed stage.
- An `AssistanceProvision` in an `HLJStageExecution` realizes the assistance specified for the same executed stage.

## Successful realization

A `SuccessfulHeroicNarrativeLearningJourneyExecution`:

1. executes exactly one `HeroicNarrativeLearningJourneyModel`;
2. produces exactly one `ClosureSituation` satisfying the `ClosureSpecification` defined by that model; and
3. realizes at least one `IntendedLearningTransformation` prescribed by that model, through a `RealizedTransformation` concerning the focal `Person`.

## Validation fixtures

The v0.9.1 suite contains one conforming graph and nine deliberately invalid graphs. The invalid fixtures isolate focal identity and successful realization, model structure, the intended-learning-transformation requirement, execution–model typing, model–stage coherence, the HLJ stage type, and the three same-stage paths. Passing these fixtures demonstrates the implemented behavior of the shapes; it is not an exhaustive proof for every possible RDF graph.


## Optional experimental completeness overlay
The additional graph at `reproducible/shacl/structural-completeness-experimental.ttl` checks 54 association ends for type and multiplicity. Combine it with Core SHACL when complete structural data are required. It is not normative Core SHACL. The original positive fixture conforms to Core but omits seven required links detected by the overlay.
