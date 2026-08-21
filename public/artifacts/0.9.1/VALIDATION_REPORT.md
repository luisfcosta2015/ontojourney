# OntoJourney Core v0.9.1 - validation report

**Release build date:** 21 August 2026  
**Status:** all structural, serialization, SHACL, OntoUML API, and HermiT
release gates passed

## Results

| Check | Result | Evidence |
|---|---|---|
| Tonto CLI validation | Passed | Canonical root source and the byte-identical `reproducible/src/core.tonto` accepted locally |
| OntoUML JSON audit | Passed | 40 classes, 27 relations, 33 generalizations, and 40 English definitions; exact identifier sets preserved |
| Cross-format definition audit | Passed | The 40 definitions agree across Tonto, OntoUML JSON, Markdown, LaTeX, and all four RDF serializations |
| gUFO/RDF parse | Passed | 368 triples in each serialization; 40 class comments and version 0.9.1 preserved |
| SHACL suite | Passed | Meta-SHACL enabled; one conforming fixture accepted and nine invalid fixtures rejected with the expected messages |
| OntoUML API | Passed | HTTP 200 and an empty `result` list for the exact v0.9.1 JSON; evidence and response archived in `validation/` |
| HermiT | Passed | HermiT 1.4.5.456 through ROBOT 1.9.10; gUFO import resolved; no inconsistency or unsatisfiable class or object property reported |

## OntoUML API evidence

```text
input SHA-256: 2465501b7152b50e5c6c01197d47dbc45df591010757b4ecc2453d5761b8436d
date: 21 August 2026
response: HTTP 200, {"result":[]}
```

The API returned an empty violation list for the exact v0.9.1 OntoUML JSON.
The execution record is in `validation/ONTOUML_API_VALIDATION_V0.9.1.md`.

## HermiT evidence

HermiT 1.4.5.456 classified the v0.9.1 OWL import closure through ROBOT 1.9.10.
The gUFO import was resolved by a local catalog. The reasoner reported no
inconsistency, unsatisfiable class, or unsatisfiable object property. The
execution record is in `validation/HERMIT_VALIDATION_V0.9.1.md`.

## SHACL behavior

The conforming fixture passes. All nine deliberately invalid fixtures fail with
the expected validation messages. The new cases isolate the intended learning
transformation, execution--model typing, model--stage coherence, HLJ stage type,
and same-stage challenge and assistance paths. The test suite demonstrates the
behavior of the release shapes against these fixtures; it is not an
exhaustive proof for every possible data graph.

## Limits

Technical validation supports reproducibility and consistency for the tested
release. It does not replace independent domain review or establish the
suitability of every future extension.
