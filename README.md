# OntoJourney

[![Pages](https://github.com/luisfcosta2015/ontojourney/actions/workflows/pages.yml/badge.svg)](https://github.com/luisfcosta2015/ontojourney/actions/workflows/pages.yml)
[![Validation](https://github.com/luisfcosta2015/ontojourney/actions/workflows/validate.yml/badge.svg)](https://github.com/luisfcosta2015/ontojourney/actions/workflows/validate.yml)
[![License: CC BY 4.0](https://img.shields.io/badge/ontology%20%26%20docs-CC%20BY%204.0-8d4e32.svg)](LICENSE)
[![Version: 0.9.2](https://img.shields.io/badge/core-v0.9.2-462542.svg)](https://w3id.org/ontojourney/core/0.9.2)
[![Concept DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21802020.svg)](https://doi.org/10.5281/zenodo.21802020)

**OntoJourney is a public ontology for narrative-heroic learning journeys. Its
OntoUML representation uses UFO as a foundational basis.**

Core v0.9.2 publishes 40 domain classes, 27 relations, 34 generalizations, and
370 RDF triples. This update distinguishes descriptive stage patterns from planned HLJ stages. It preserves all class and relation IRIs but changes generic-stage entailments. Core SHACL is unchanged; an optional completeness profile is included. The repository combines
the conceptual source, OntoUML exchange model, Web serializations, SHACL shapes,
test fixtures, validation records, checksums, and citation metadata.

## Public documentation

- Website: <https://luisfcosta2015.github.io/ontojourney/>
- Ontology IRI: <https://w3id.org/ontojourney/core>
- Entity namespace: `https://w3id.org/ontojourney/core#`
- Version IRI: <https://w3id.org/ontojourney/core/0.9.2>
- Version DOI: <https://doi.org/10.5281/zenodo.24420185>
- Concept DOI for all versions: <https://doi.org/10.5281/zenodo.21802020>
- Release: [Core v0.9.2](https://github.com/luisfcosta2015/ontojourney/releases/tag/v0.9.2)

The version DOI identifies the archived v0.9.2 package. The concept DOI
represents all OntoJourney versions and resolves to the latest record.

## Validation status

Version 0.9.2 passed:

- local Tonto source validation;
- OntoUML JSON structural auditing, including all 40 class definitions;
- cross-format definition and release-consistency checks;
- gUFO-aligned RDF parsing and isomorphism checks across four serializations;
- one conforming and nine deliberately invalid SHACL fixtures;
- local OntoUML verification and transformation with no reported violations; and
- HermiT 1.4.5.456 classification through ROBOT 1.9.10, with no reported
  inconsistency or unsatisfiable OntoJourney class or object property.

The HermiT transformation input is tied to SHA-256
`f3b12bad9bb39d78d59e6a5d413a9885dd6e3c888ca7086f7c0ba132c63834e8`.
See [`ontology/validation`](ontology/validation/) for the public technical
records and the limits of each check.

## Repository structure

```text
app/                  Static documentation website
components/           Shared interface components
ontology/             Complete current ontology release package
public/artifacts/      Immutable versioned release files and archives
public/foundations/    Three unchanged images previously published in the HLJ article
public/brand/          Heroic Journeys identity asset
scripts/               Reference and deterministic release generation
templates/             Issue and extension templates
w3id/                  Persistent-identifier policy, rules, and verification script
.github/               Validation, Pages, issue, and release automation
```

The unpublished article is not stored in this public repository. The
`ontology/article/` directory contains only the generated class-definition
appendix distributed as part of the ontology release.

## Reproduce the ontology checks

```bash
python3 -m venv .venv
.venv/bin/pip install -r ontology/reproducible/requirements-validation.txt
.venv/bin/python ontology/reproducible/tests/audit_generated_json.py
.venv/bin/python ontology/reproducible/tests/audit_release_consistency.py
.venv/bin/python ontology/reproducible/tests/run_shacl_tests.py
.venv/bin/python ontology/reproducible/evaluation/run_evaluation.py
```

The deliberately invalid SHACL fixtures must report `conforms=False`; their
rejection is the expected passing result.

## Build the release and documentation

Requires Python 3.12 and Node.js 22 or newer.

```bash
python scripts/build_release.py
npm ci
npm run generate:model
GITHUB_PAGES=true NEXT_PUBLIC_BASE_PATH=/ontojourney npm run build:pages
```

The release builder verifies the source manifest, copies the package to the
versioned public directory, and creates a deterministic ZIP archive. The GitHub
Pages workflow performs a static export with the repository base path and
deploys it from `main`.

## Cite

> Costa, Luis Felipe Coimbra. 2026. *OntoJourney: An Ontology of
> Narrative-Heroic Learning Journeys*. OntoJourney Core v0.9.2.
> Zenodo. <https://doi.org/10.5281/zenodo.24420185>.

Use the version DOI to cite the exact archived package. The version IRI
<https://w3id.org/ontojourney/core/0.9.2> identifies the corresponding
ontology release through W3ID. The concept DOI
<https://doi.org/10.5281/zenodo.21802020> represents the collection of all
OntoJourney versions.

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
