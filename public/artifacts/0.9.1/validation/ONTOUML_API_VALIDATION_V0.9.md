# OntoJourney Core v0.9 — OntoUML API validation

## Execution record

The remote verification was executed on 31 July 2026 after explicit
authorization to transmit OntoJourney Core v0.9 to `api.ontouml.org`.

Canonical input:

```text
file: generated/OntoJourneyCore.json
source: src/core.tonto
Tonto CLI version: 0.4.13
SHA-256: 7830fc94d0741517bbb415094ed3ff08204a166419b92627b4aa300192f6e18a
```

Request:

```text
method: POST
endpoint: http://api.ontouml.org/v1/verify
content type: application/json
options: null
```

The request format and endpoint follow the public documentation of the
[OntoUML Server](https://github.com/OntoUML/ontouml-server).

Response:

```text
HTTP status: 200
content type: application/json; charset=utf-8
elapsed request time: 6.217493 seconds
```

```json
{
  "result": []
}
```

## Interpretation

The OntoUML verification service accepted the serialized v0.9 project and
reported no violations. This result concerns the verification rules
implemented by that service. It does not establish domain completeness,
validate the cross-path constraints implemented in SHACL, or replace OWL
classification with a description-logic reasoner.

Protégé/HermiT classification was completed on 1 August 2026 and is recorded in
`HERMIT_VALIDATION_V0.9.md`.
