# OntoJourney publication and persistent IRI policy

## Canonical identifiers

```text
Ontology IRI:    https://w3id.org/ontojourney/core
Entity namespace: https://w3id.org/ontojourney/core#
Version IRI:     https://w3id.org/ontojourney/core/0.9.1
```

Entity IRIs remain non-versioned. For example:

```text
https://w3id.org/ontojourney/core#JourneyModel
```

Version IRIs identify releases, not replacement identities for every class.

## Hosting and negotiation

The W3ID resolver is active. Its rules redirect requests according to their
`Accept` header:

| Requested representation | Published resource |
|---|---|
| `text/html` | human-readable model or release documentation |
| `text/turtle` | Turtle |
| `application/rdf+xml` | RDF/XML |
| `application/ld+json` | JSON-LD |
| `application/n-triples` | N-Triples |

Version-specific routes are immutable: `/core/0.9` continues to identify
v0.9.0, while publication of this release adds `/core/0.9.1`. The coordinated
publication sequence first makes the versioned artifacts and documentation
available on GitHub Pages and then updates the unversioned `/core` negotiation
targets to v0.9.1. This sequence retains the ontology IRI and all entity IRIs.

## Compatibility rule

Compatible releases retain entity IRIs. A breaking change that changes the
identity of a term requires an explicit deprecation and migration decision; it
must not be implemented by silently reusing an IRI for a different referent.

The v0.9.1 release adds annotations and stricter validation constraints. It
does not rename a class or relation, change the class taxonomy, or reuse an IRI
for a different referent.
