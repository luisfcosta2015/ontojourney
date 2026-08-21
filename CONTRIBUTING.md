# Contributing to OntoJourney

OntoJourney welcomes corrections, implementation reports, questions, and
carefully scoped extensions.

## Before proposing a model change

1. State the problem the current public model cannot address.
2. Identify the domain evidence supporting the proposal.
3. Explain why documentation, instance data, or an extension namespace is not sufficient.
4. Identify the affected representation: Tonto, OntoUML JSON, RDF/OWL, SHACL, or documentation.
5. Describe compatibility, validation, and migration effects.

## Choose the correct issue template

- **Defect report:** inconsistency, broken artifact, incorrect endpoint or cardinality, failed validation, or documentation error.
- **Question:** a required query or distinction that may reveal a justified gap.
- **Term proposal:** a class, relation, constraint, or definition supported by evidence.

Please keep unrelated requests in separate issues.

## Pull requests

Pull requests should be small and traceable. Include the related issue, changed
source files, regenerated artifacts when required, updated tests, and a concise
compatibility statement.

Run before opening a pull request:

```bash
python3 -m venv .venv
.venv/bin/pip install -r ontology/reproducible/requirements-validation.txt
.venv/bin/python ontology/reproducible/tests/audit_generated_json.py
.venv/bin/python ontology/reproducible/tests/audit_release_consistency.py
.venv/bin/python ontology/reproducible/tests/run_shacl_tests.py
python scripts/build_release.py
npm ci
npm run check:model
GITHUB_PAGES=true NEXT_PUBLIC_BASE_PATH=/ontojourney npm run build:pages
```

## Versioning

- Patch releases may add backward-compatible definitions or constraints and
  correct documentation, metadata, serializations, or tooling without changing
  term identity.
- Minor releases may add backward-compatible terms or constraints with documented evidence.
- A change in term identity or meaning requires explicit deprecation and a migration plan.

## Review criteria

The maintainer evaluates conceptual correctness, scope, traceability,
compatibility, validation evidence, and documentation quality.
