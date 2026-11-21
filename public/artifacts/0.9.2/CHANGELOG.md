# v0.9.2 - 2026-11-21

- Generalize StageSpecification to Description; preserve planned HLJ stage typing.
- Keep Core SHACL unchanged; add opt-in experimental completeness and synthetic CQ tests.
- Preserve identifiers; generic-stage entailments change.

# Public changelog

## v0.9.1 - 21 August 2026

- Added English genus--differentia definitions for all 40 domain classes to
  the canonical Tonto source, the OntoUML JSON, the RDF serializations, and the
  generated class glossary.
- Required every `HeroicNarrativeLearningJourneyModel` to prescribe at least
  one `IntendedLearningTransformation`.
- Required each narrative, heroic narrative, learning, and heroic narrative
  learning execution subtype to execute the corresponding model subtype.
- Added model--stage coherence, the `HLJStageExecution` type constraint, and
  same-stage constraints for challenge encounters, challenge performances, and
  assistance provisions.
- Expanded the SHACL suite from one conforming and two invalid graphs to one
  conforming and nine deliberately invalid graphs.
- Preserved all 40 class IRIs, 27 relation IRIs, and 33 generalizations from
  v0.9.0.
- Recorded HTTP 200 with an empty violation list from the OntoUML API for the
  exact v0.9.1 JSON.
- Classified the OWL import closure with HermiT 1.4.5.456, with no
  inconsistency or unsatisfiable class or object property reported.

## v0.9.0 - 1 August 2026

- Published the canonical Tonto source and OntoUML JSON exchange model.
- Published 40 domain classes together with 27 relations and 33 generalizations.
- Published Turtle, RDF/XML, JSON-LD, and N-Triples serializations under the
  `https://w3id.org/ontojourney/core#` namespace.
- Published the SHACL graph, one conforming fixture, and two deliberately
  invalid fixtures.
- Recorded local source validation, structural auditing, RDF parsing, remote
  OntoUML API verification, and Protégé/HermiT classification.
- Added versioned checksums, citation metadata, release automation, and static
  documentation.

Earlier development snapshots were internal working versions and are not part
of the public release history.
