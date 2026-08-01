# OntoJourney Core v0.9.0

This directory contains the public formal artifacts for OntoJourney Core
v0.9.0.

## Contents

```text
src/core.tonto                         conceptual source
generated/OntoJourneyCore.json         OntoUML exchange model
generated/OntoJourneyCore.ttl          gUFO-aligned Turtle serialization
shacl/ontojourney-core-v0.9.shacl.ttl  SHACL constraint graph
tests/                                  structural and SHACL fixtures
validation/                             public technical records
PUBLICATION.md                          IRI and version policy
CHANGELOG.md                            public release history
```

## Validation

Version 0.9.0 passed local source validation, OntoUML JSON structural auditing,
RDF parsing, SHACL fixture tests, remote OntoUML API verification, and
Protégé/HermiT classification.

Run the reproducible local checks from this directory:

```bash
python3 -m pip install -r requirements-validation.txt
python3 tests/audit_generated_json.py
python3 tests/run_shacl_tests.py
```

The OntoUML API record, raw response, and HermiT record are available under
`validation/`.

## Public identifiers

```text
Ontology IRI:     https://w3id.org/ontojourney/core
Entity namespace: https://w3id.org/ontojourney/core#
Version IRI:      https://w3id.org/ontojourney/core/0.9
```
