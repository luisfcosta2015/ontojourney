# HermiT validation — OntoJourney Core v0.9.1

## Result

OntoJourney Core v0.9.1 was classified with HermiT 1.4.5.456 through
ROBOT 1.9.10 on 21 August 2026. The gUFO import was resolved with a local XML
catalog, the reasoner completed successfully, and no inconsistent ontology,
unsatisfiable class, or unsatisfiable object property was reported.

```text
result: passed
reasoner: HermiT 1.4.5.456
runner: ROBOT 1.9.10
input axioms: 355
output axioms after reasoning: 413
gUFO import: resolved by local catalog
unsatisfiable classes: none detected
unsatisfiable object properties: none detected
exit code: 0
```

## Input identity

```text
OntoJourney Turtle:
SHA-256 04376eeaad49188ea74549ef8421e4d7e7f3bc6ad26ee4167c0eeebcc8db3921

gUFO source commit:
f4122544133544eb4c6c467ba316302ab20b754a

gUFO Turtle:
SHA-256 0eb67c085a9ebf3bd559b1f19ca32cc9be1f4fd2d7f604eb7dfd92843f8dcc66

ROBOT JAR:
SHA-256 16a73c074f3df359a7338a84b4e0788785fe06117f931bb9796e9619ea776105
```

The ROBOT JAR digest agrees with the digest published for the official
v1.9.10 release asset.

## Command

```text
java -Xmx2G -jar robot.jar -vv reason \
  --input ontojourney-core.ttl \
  --catalog catalog-v001.xml \
  --reasoner HermiT \
  --equivalent-classes-allowed all \
  --output ontojourney-core-v0.9.1-reasoned.ttl
```

The catalog maps `http://purl.org/nemo/gufo#` to the pinned local copy of
`gufo.ttl`.

## Interpretation

This result supports logical consistency and coherence of the classified OWL
import closure. It does not establish completeness of the domain commitments,
validate closed-world cardinalities, or replace the SHACL suite for
cross-path constraints.
