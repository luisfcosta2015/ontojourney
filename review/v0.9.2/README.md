# OntoJourney Core v0.9.2 — draft review

**Not a published release. Do not merge this preparatory PR as a release.**

Review baseline: main daa7a991d54798d96acd9ae1d3609d5de901e45a; published release 0.9.1 remains immutable. Candidate source `tonto-project/src/core.tonto` is byte-identical to the source validated by the author on 2026-11-21 (SHA-256 264f7bda66374f36d2cffd2d6227931b771ea0d5463848c44f4d9d74d567ab6c).

## Semantic change
- StageSpecification specializes Description rather than PlanDescription.
- HLJStageSpecification specializes both StageSpecification and PlanDescription.
- Two definitions updated. 40 classes, 27 relations and 34 generalizations. Identifiers, stereotypes and association multiplicities unchanged.
- The generic stage no longer entails PlanDescription or NormativeDescription; HLJ stages retain those entailments. This is not unconditional semantic backward compatibility.

## Existing evidence (author's independent local run, not a CI claim)
Tonto CLI 0.4.13 local validation and JSON structural audit passed. ontouml-js 0.4.1 verified and transformed baseline and candidate locally. Transformed axioms match the prototype after excluding annotations and release metadata (zero differing triples). HermiT via ROBOT 1.9.10 passed on the candidate transformation (356 input / 414 output axioms). Nine CQ queries on three graphs returned the same bindings in the candidate and baseline. Original 10 SHACL tests and ten comparative candidate/profile scenarios returned expected results. Case 01 remains model-only. No empirical or independent domain-expert validation is claimed. The original positive fixture is incomplete for seven multiplicities; optional structural completeness overlay detects those gaps.

## Promotion gates
- [ ] Review remaining semantic questions with ontology specialists; do not equate tool validation with domain adequacy.
- [ ] Transfer the reviewed release candidate artefacts, sanitized evidence and reproducibility scripts into this branch; verify public redistribution rights for Case 01 material. No private Manager code or raw personal/local logs.
- [ ] Reserve a new version-specific DOI on Zenodo (new version of record 22043806, not a new independent record); retain existing concept DOI and historic identifiers. No fabricated DOI or publication date.
- [ ] Finalize version IRI /core/0.9.2, provenance, metadata, checksums, source/JSON/four RDF formats, generated glossary and appendix. Rerun release audits, Core SHACL tests, CQ tests and optional completeness overlay. Core SHACL unchanged; overlay opt-in.
- [ ] Update build_release.py, validate.yml, release.yml (manual release gate), root citation and README metadata, lib/site.ts, model reference, site content and release page /releases/0.9.2/. Verify site build and old artifacts unchanged.
- [ ] Review figures and manuscript; confirm final scope and version/citation.
- [ ] Approve merge only after final CI and DOI reservation; publish GitHub assets and Pages, then publish Zenodo version with the exact same archive.
- [ ] After verifying live destinations, prepare separate PR to perma-id/w3id.org. Preserve old version routes, keep entity namespace /core#, update unversioned route only when safe. Verify current upstream redirect rules first.
- [ ] Verify new and historical content negotiation plus download checksums before announcing.

The extended review workflow regenerates JSON, verifies and transforms it locally, compares exact axiom changes, builds four RDF serializations, reruns Core SHACL, generates an opt-in overlay and tests nine queries on two synthetic graphs. Candidate outputs become an unpublished CI artifact. IDs may differ from the original generated JSON. Case 01 data and raw logs are not included pending redistribution checks. Production files and redirects remain unchanged. Final promotion remains gated.
