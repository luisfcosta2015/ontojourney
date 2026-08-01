# OntoJourney Core v0.9.0 - Validation report

**Release date:** 1 August 2026  
**Status:** passed all planned technical gates

## Results

| Check | Result | Evidence |
|---|---|---|
| Tonto CLI validation | Passed | Canonical `src/core.tonto` accepted |
| OntoUML JSON audit | Passed | 40 domain classes together with 27 relations and 33 generalizations |
| gUFO/RDF parse | Passed | 326 triples; 40 classes and 27 object properties preserved |
| SHACL suite | Passed | Conforming fixture accepted; two invalid fixtures rejected as expected |
| OntoUML API | Passed | HTTP 200 and `{"result":[]}` |
| Protégé/HermiT | Passed | gUFO import resolved; no OntoJourney class observed under `owl:Nothing` |

## OntoUML API input

```text
SHA-256: 7830fc94d0741517bbb415094ed3ff08204a166419b92627b4aa300192f6e18a
date: 31 July 2026
response: HTTP 200, {"result":[]}
```

The API returned an empty violation list for the supplied OntoUML JSON. This
does not establish domain completeness.

## SHACL behavior

The conforming fixture passes. Both deliberately invalid fixtures fail with the
expected validation messages. The test suite demonstrates the behavior of the
published shapes against these fixtures; it is not an exhaustive proof for
every possible data graph.

## Limits

Technical validation supports reproducibility and consistency for the tested
release. It does not replace independent domain review or establish the
suitability of every future extension.
