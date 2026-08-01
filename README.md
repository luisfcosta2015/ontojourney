# OntoJourney

[![Pages](https://github.com/luisfcosta2015/ontojourney/actions/workflows/pages.yml/badge.svg)](https://github.com/luisfcosta2015/ontojourney/actions/workflows/pages.yml)
[![Validation](https://github.com/luisfcosta2015/ontojourney/actions/workflows/validate.yml/badge.svg)](https://github.com/luisfcosta2015/ontojourney/actions/workflows/validate.yml)
[![License: CC BY 4.0](https://img.shields.io/badge/ontology%20%26%20docs-CC%20BY%204.0-8d4e32.svg)](LICENSE)
[![Version: 0.9.0](https://img.shields.io/badge/core-v0.9.0-462542.svg)](https://w3id.org/ontojourney/core/0.9)

**OntoJourney is a public ontology for narrative-heroic learning journeys. Its
OntoUML representation uses UFO as a foundational basis.**

Core v0.9.0 publishes 40 domain classes together with 27 relations,
33 generalizations, and 326 RDF triples. The repository combines the conceptual source, OntoUML
exchange model, Web serializations, SHACL shapes, test fixtures, validation
records, checksums, and citation metadata.

## Public documentation

- Website: <https://luisfcosta2015.github.io/ontojourney/>
- Ontology IRI: <https://w3id.org/ontojourney/core>
- Entity namespace: `https://w3id.org/ontojourney/core#`
- Version IRI: <https://w3id.org/ontojourney/core/0.9>
- Release: [Core v0.9.0](https://github.com/luisfcosta2015/ontojourney/releases/tag/v0.9.0)

## Validation status

Version 0.9.0 passed:

- local Tonto source validation;
- OntoUML JSON structural auditing;
- gUFO-aligned RDF parsing and structural checks;
- SHACL positive and deliberately invalid fixture tests;
- remote OntoUML API verification with no reported violations; and
- Protégé/HermiT classification with no unsatisfiable OntoJourney classes.

The OntoUML API result is tied to SHA-256
`7830fc94d0741517bbb415094ed3ff08204a166419b92627b4aa300192f6e18a`.
See [`ontology/validation`](ontology/validation/) for the public technical
records and the limits of each check.

## Repository structure

```text
app/                  Static documentation website
components/           Shared interface components
ontology/             Source, JSON, RDF, SHACL, tests, and validation records
public/artifacts/      Versioned release files and archive
public/foundations/    Three unchanged images previously published in the HLJ article
public/brand/          Heroic Journeys identity asset
scripts/               Reference and release generation
templates/             Issue and extension templates
w3id/                  Prepared persistent-identifier redirect configuration
.github/               Validation, Pages, issue, and release automation
```

## Reproduce the ontology checks

```bash
python3 -m venv .venv
.venv/bin/pip install -r ontology/requirements-validation.txt
.venv/bin/python ontology/tests/audit_generated_json.py
.venv/bin/python ontology/tests/run_shacl_tests.py
```

The deliberately invalid SHACL fixtures must report `conforms=False`; their
rejection is the expected passing result.

## Build the documentation

Requires Node.js 22 or newer.

```bash
npm ci
npm run generate:model
npm run dev
```

The GitHub Pages workflow performs a static export with the repository base
path and deploys it from `main`.

## Cite

> Costa, Luis Felipe Coimbra. 2026. *OntoJourney: An Ontology of
> Narrative-Heroic Learning Journeys*. OntoJourney Core v0.9.0.
> <https://w3id.org/ontojourney/core/0.9>.

Machine-readable citation metadata is available in [`CITATION.cff`](CITATION.cff)
and [`codemeta.json`](codemeta.json).

## Licenses

The ontology and original documentation are licensed under
[CC BY 4.0](LICENSE). Website source code and automation scripts are licensed
under the [MIT License](LICENSE-CODE).

The three previously published journey images and the Heroic Journeys logo are
excluded from those general grants. Their provenance and terms are stated in
[`ASSET-LICENSES.md`](ASSET-LICENSES.md).

## Contribute

Read [`CONTRIBUTING.md`](CONTRIBUTING.md) before proposing a correction or
extension. Structured issue templates are provided for defects, questions, and
term proposals.
