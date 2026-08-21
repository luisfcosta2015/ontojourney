# OntoJourney Core v0.9.1

This release contains the OntoJourney formal source, exchange model, RDF
serializations, SHACL shapes, class definitions, reproducibility fixtures,
validation records, checksums, and citation metadata. It preserves the 40
classes, 27 relations, and 33 generalizations of v0.9.0 while tightening the
constraints required by the manuscript.

- Ontology IRI: `https://w3id.org/ontojourney/core`
- Entity namespace: `https://w3id.org/ontojourney/core#`
- Version IRI: `https://w3id.org/ontojourney/core/0.9.1`
- Release date: 21 August 2026
- License: CC BY 4.0

The canonical definitions are the English `description` blocks in
`core.tonto`. `CLASS_DEFINITIONS.md` and the appendix source are generated from
the OntoUML JSON; the RDF serializations expose the same text as
`rdfs:comment` annotations. `CONSTRAINTS.md` explains the division of work
between Tonto, OWL/gUFO, and SHACL.

## Local validation

With Tonto CLI and the Python packages pinned in
`reproducible/requirements-validation.txt`, run:

```text
tonto-cli validate reproducible
python reproducible/tests/audit_generated_json.py
python reproducible/tests/audit_release_consistency.py
python reproducible/tests/run_shacl_tests.py
```

The remote OntoUML API and HermiT results are recorded in `validation/`.

`reproducible/scripts/finalize_release_artifacts.py` adds the version metadata
and canonical class comments after the gUFO transformation.
`reproducible/scripts/generate_class_documentation.py` regenerates the Markdown
glossary and LaTeX appendix from the OntoUML JSON. The checksum manifest must be
regenerated last with `reproducible/scripts/update_checksums.py`.
