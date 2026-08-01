from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import shutil
import zipfile

from rdflib import Graph


ROOT = Path(__file__).resolve().parents[1]
ONTOLOGY = ROOT / "ontology"
PUBLIC = ROOT / "public"
OUT = PUBLIC / "artifacts" / "0.9.0"
ARCHIVE_NAME = "ontojourney-core-v0.9.0.zip"


def copy(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def digest(path: Path) -> str:
    result = sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            result.update(chunk)
    return result.hexdigest()


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    graph = Graph().parse(ONTOLOGY / "generated" / "OntoJourneyCore.ttl", format="turtle")
    graph.serialize(OUT / "ontojourney-core.ttl", format="turtle")
    graph.serialize(OUT / "ontojourney-core.rdf", format="xml")
    graph.serialize(OUT / "ontojourney-core.jsonld", format="json-ld", indent=2)
    graph.serialize(OUT / "ontojourney-core.nt", format="nt")

    files = [
        (ONTOLOGY / "generated" / "OntoJourneyCore.json", OUT / "OntoJourneyCore.json"),
        (ONTOLOGY / "src" / "core.tonto", OUT / "core.tonto"),
        (ONTOLOGY / "tonto.json", OUT / "tonto.json"),
        (ONTOLOGY / "shacl" / "ontojourney-core-v0.9.shacl.ttl", OUT / "ontojourney-core.shacl.ttl"),
        (ONTOLOGY / "PUBLICATION.md", OUT / "PUBLICATION.md"),
        (ONTOLOGY / "CHANGELOG.md", OUT / "CHANGELOG.md"),
        (ONTOLOGY / "validation" / "VALIDATION_REPORT_V0.9.md", OUT / "VALIDATION_REPORT.md"),
        (ONTOLOGY / "validation" / "ONTOUML_API_VALIDATION_V0.9.md", OUT / "validation" / "ONTOUML_API_VALIDATION_V0.9.md"),
        (ONTOLOGY / "validation" / "ontouml-api-response-v0.9.json", OUT / "validation" / "ontouml-api-response-v0.9.json"),
        (ONTOLOGY / "validation" / "HERMIT_VALIDATION_V0.9.md", OUT / "validation" / "HERMIT_VALIDATION_V0.9.md"),
        (ROOT / "CITATION.cff", OUT / "CITATION.cff"),
        (ROOT / "codemeta.json", OUT / "codemeta.json"),
        (ROOT / "LICENSE", OUT / "LICENSE"),
        (ONTOLOGY / "generated" / "OntoJourneyCore.json", OUT / "reproducible" / "generated" / "OntoJourneyCore.json"),
        (ONTOLOGY / "src" / "core.tonto", OUT / "reproducible" / "src" / "core.tonto"),
        (ONTOLOGY / "tonto.json", OUT / "reproducible" / "tonto.json"),
        (ONTOLOGY / "shacl" / "ontojourney-core-v0.9.shacl.ttl", OUT / "reproducible" / "shacl" / "ontojourney-core-v0.9.shacl.ttl"),
        (ONTOLOGY / "tests" / "audit_generated_json.py", OUT / "reproducible" / "tests" / "audit_generated_json.py"),
        (ONTOLOGY / "tests" / "run_shacl_tests.py", OUT / "reproducible" / "tests" / "run_shacl_tests.py"),
        (ONTOLOGY / "tests" / "data" / "positive.ttl", OUT / "reproducible" / "tests" / "data" / "positive.ttl"),
        (ONTOLOGY / "tests" / "data" / "negative_focal_success.ttl", OUT / "reproducible" / "tests" / "data" / "negative_focal_success.ttl"),
        (ONTOLOGY / "tests" / "data" / "negative_model.ttl", OUT / "reproducible" / "tests" / "data" / "negative_model.ttl"),
        (ONTOLOGY / "requirements-validation.txt", OUT / "reproducible" / "requirements-validation.txt"),
    ]
    for source, destination in files:
        copy(source, destination)

    copy(OUT / "ontojourney-core.ttl", OUT / "reproducible" / "generated" / "OntoJourneyCore.ttl")

    readme = """# OntoJourney Core v0.9.0

This public release contains the OntoJourney formal source, exchange model,
RDF serializations, SHACL shapes, reproducibility fixtures, validation records,
checksums, and citation metadata.

Ontology IRI: `https://w3id.org/ontojourney/core`  
Entity namespace: `https://w3id.org/ontojourney/core#`  
Version IRI: `https://w3id.org/ontojourney/core/0.9`  
License: CC BY 4.0
"""
    (OUT / "README.md").write_text(readme, encoding="utf-8")

    archive = OUT / ARCHIVE_NAME
    sums_path = OUT / "SHA256SUMS"
    artifact_files = sorted(
        path for path in OUT.rglob("*") if path.is_file() and path.name not in {ARCHIVE_NAME, "SHA256SUMS"}
    )
    sums = [f"{digest(path)}  {path.relative_to(OUT).as_posix()}" for path in artifact_files]
    sums_path.write_text("\n".join(sums) + "\n", encoding="utf-8")

    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as bundle:
        for path in sorted(path for path in OUT.rglob("*") if path.is_file() and path != archive):
            bundle.write(path, Path("ontojourney-core-v0.9.0") / path.relative_to(OUT))

    with sums_path.open("a", encoding="utf-8") as stream:
        stream.write(f"{digest(archive)}  {ARCHIVE_NAME}\n")

    print(f"Published {len(graph)} RDF triples and {len(artifact_files)} release files.")
    print(f"Archive: {archive}")


if __name__ == "__main__":
    main()
