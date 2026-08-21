# OntoJourney Core v0.9.1 — OntoUML API validation

## Execution record

The remote verification was executed on 21 August 2026 after explicit
authorization to transmit OntoJourney Core v0.9.1 to `api.ontouml.org`.

Canonical input:

```text
file: OntoJourneyCore.json
source: reproducible/src/core.tonto
Tonto CLI version: 0.4.13
file size: 94,484 bytes
SHA-256: 2465501b7152b50e5c6c01197d47dbc45df591010757b4ecc2453d5761b8436d
```

Request:

```text
method: POST
endpoint: http://api.ontouml.org/v1/verify
content type: application/json
options: null
canonical request SHA-256:
7a34fb18082ba6b909683e6c98ceece538a6026052348d4e4d6012f2a60f3863
```

The request format and endpoint follow the public documentation of the
[OntoUML Server](https://github.com/OntoUML/ontouml-server).

Response:

```text
HTTP status: 200
content type: application/json; charset=utf-8
server date: Fri, 21 Aug 2026 08:22:48 GMT
response SHA-256:
ff1434e1a4afd84247c3f0475e98240a613c4f97c22f4afc7af1a014af57a627
```

```json
{
  "result": []
}
```

## Interpretation

The OntoUML verification service accepted the serialized v0.9.1 project and
reported no violations. This result concerns the verification rules
implemented by that service. It does not establish domain completeness,
validate the cross-path constraints implemented in SHACL, or replace OWL
classification with a description-logic reasoner.

HermiT classification is recorded in `HERMIT_VALIDATION_V0.9.1.md`.
