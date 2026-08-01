# OntoJourney publication and persistent IRI policy

## Canonical identifiers

```text
Ontology IRI:    https://w3id.org/ontojourney/core
Entity namespace: https://w3id.org/ontojourney/core#
Version IRI:     https://w3id.org/ontojourney/core/0.9
```

Entity IRIs remain non-versioned. For example:

```text
https://w3id.org/ontojourney/core#JourneyModel
```

Version IRIs identify releases, not replacement identities for every class.

## Hosting and negotiation

The GitHub Pages publication contains HTML documentation and RDF
serializations. The prepared W3ID rules redirect requests according to their
`Accept` header:

| Requested representation | Published resource |
|---|---|
| `text/html` | human-readable model or release documentation |
| `text/turtle` | Turtle |
| `application/rdf+xml` | RDF/XML |
| `application/ld+json` | JSON-LD |
| `application/n-triples` | N-Triples |

The `w3id/` directory at the repository root contains the files to submit to
the W3ID repository. Until that pull request is approved, the W3ID IRIs are the
chosen canonical identifiers but their public redirects are not yet active.

## Compatibility rule

Compatible releases retain entity IRIs. A breaking change that changes the
identity of a term requires an explicit deprecation and migration decision; it
must not be implemented by silently reusing an IRI for a different referent.
