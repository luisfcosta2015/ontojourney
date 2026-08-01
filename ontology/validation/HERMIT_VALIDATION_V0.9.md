# Protégé/HermiT validation — OntoJourney Core v0.9

## Result

OntoJourney Core v0.9 was classified in Protégé with HermiT on 1 August 2026.
The gUFO import resolved, the reasoner completed, and the inferred class
hierarchy contained no OntoJourney class under `owl:Nothing`.

```text
result: passed
reasoner: HermiT
view inspected: inferred class hierarchy
gUFO import: resolved
unsatisfiable OntoJourney classes: none observed
```

## Interpretation

This result supports logical consistency of the classified OWL graph. It does
not establish completeness of the domain commitments, validate closed-world
cardinalities, or replace the SHACL tests for cross-path constraints.

## Publication namespace

The publication artifact replaces the provisional namespace with
`https://w3id.org/ontojourney/core#`. This migration is a uniform IRI rename
and does not alter class axioms, property axioms, or imports. The repository
tests verify the published graph and its SHACL data after the migration.
