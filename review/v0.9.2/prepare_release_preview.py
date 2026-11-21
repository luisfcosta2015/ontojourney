"""Prepare an unpublished, checksummed target-version archive in CI, not in production.
No raw logs, proprietary Manager code or Case 01 data are copied.
The archive is a review artifact; release authorization and date are separate.
"""
import hashlib, json, shutil, subprocess, sys, zipfile
from pathlib import Path
from rdflib import Graph, URIRef, Literal
from rdflib.namespace import OWL,DCTERMS
from rdflib.compare import isomorphic

ROOT=Path(__file__).resolve().parent
BASE=ROOT.parents[1]/"ontology"
INPUT=ROOT/"candidate-output"
OUT=ROOT/"release-preview"
DEST=OUT/"ontojourney-core-v0.9.2"
if OUT.exists(): shutil.rmtree(OUT)
DEST.mkdir(parents=True)
R=DEST/"reproducible"
G=R/"generated"
V=DEST/"validation"
for d in (G,R/"src",R/"scripts",R/"shacl",R/"evaluation/queries",DEST/"article",V): d.mkdir(parents=True,exist_ok=True)
meta=json.loads((ROOT/"release-metadata.json").read_text())
assert meta["status"]=="draft" and meta["doiStatus"]=="reserved-unpublished"
def write(p,s): p.write_text(s,encoding="utf-8")
def cp(a,b): shutil.copyfile(a,b)
def dump(p,o): write(p,json.dumps(o,indent=2,ensure_ascii=False)+"\n")
def script(p): subprocess.run([sys.executable,str(p)],check=True)
for name in ("LICENSE","CONSTRAINTS.md"): cp(BASE/name,DEST/name)
for name in ("core.tonto","OntoJourneyCore.json","ontojourney-core.shacl.ttl"): cp(INPUT/name,DEST/name)
cp(DEST/"core.tonto",R/"src/core.tonto")
cp(DEST/"OntoJourneyCore.json",G/"OntoJourneyCore.json")
cp(DEST/"ontojourney-core.shacl.ttl",R/"shacl/ontojourney-core-v0.9.2.shacl.ttl")
cp(INPUT/"structural-completeness-experimental.ttl",R/"shacl/structural-completeness-experimental.ttl")
cp(BASE/"reproducible/requirements-validation.txt",R/"requirements-validation.txt")
# Target version and reserved DOI, but no assertion that DOI is registered or published.
t=json.loads((INPUT/"tonto.json").read_text());t.update(version="0.9.2",description="OntoJourney Core v0.9.2: descriptive stages and planned HLJ stages.")
dump(DEST/"tonto.json",t);cp(DEST/"tonto.json",R/"tonto.json")
g=Graph().parse(INPUT/"ontojourney-core.ttl",format="turtle")
iri=URIRef(meta["ontologyIRI"])
g.set((iri,OWL.versionIRI,URIRef(meta["versionIRI"])))
g.set((iri,OWL.versionInfo,Literal(meta["targetVersion"])))
g.set((iri,DCTERMS.identifier,Literal(meta["doi"])))
g.remove((iri,DCTERMS.issued,None))
for ext,fmt in [("ttl","turtle"),("rdf","xml"),("nt","nt"),("jsonld","json-ld")]:
    f=DEST/("ontojourney-core."+ext);g.serialize(f,format=fmt)
    assert isomorphic(g,Graph().parse(f,format=fmt))
cp(DEST/"ontojourney-core.ttl",G/"OntoJourneyCore.ttl")
# Baseline PlantUML manually adapted to the validated exact edge delta.
p=(BASE/"OntoJourneyCore.puml").read_text()
assert p.count("PlanDescription <|-- StageSpecification")==1
p=p.replace("PlanDescription <|-- StageSpecification","Description <|-- StageSpecification").replace("StageSpecification <|-- HLJStageSpecification","StageSpecification <|-- HLJStageSpecification\nPlanDescription <|-- HLJStageSpecification")
write(DEST/"OntoJourneyCore.puml",p)
(G/"plantuml").mkdir();cp(DEST/"OntoJourneyCore.puml",G/"plantuml/OntoJourneyCore.puml")
# Preserve old test data, adapt only version-dependent assertions.
shutil.copytree(BASE/"reproducible/tests",R/"tests",ignore=shutil.ignore_patterns("__pycache__"))
a=R/"tests/audit_generated_json.py";s=a.read_text().replace('("StageSpecification", "PlanDescription"),','("StageSpecification", "Description"),\n    ("HLJStageSpecification", "PlanDescription"),').replace("len(generalizations) == 33","len(generalizations) == 34").replace("33 generalizations","34 generalizations").replace("v0.9.1 identity assertions","v0.9.2 identity assertions");write(a,s)
a=R/"tests/run_shacl_tests.py";write(a,a.read_text().replace("ontojourney-core-v0.9.1.shacl.ttl","ontojourney-core-v0.9.2.shacl.ttl"))
generator=R/"scripts/generate_class_documentation.py"
write(generator,(BASE/"reproducible/scripts/generate_class_documentation.py").read_text().replace("v0.9.1","v0.9.2"))
script(generator)
m=json.loads((BASE/"codemeta.json").read_text());m.pop("datePublished",None);m.update(version="0.9.2",url=meta["versionIRI"],identifier="https://doi.org/"+meta["doi"],developmentStatus="Unpublished release preparation")
dump(DEST/"codemeta.json",m)
s=(BASE/"CITATION.cff").read_text().replace("0.9.1","0.9.2").replace("date-released: 2026-08-21","doi: "+meta["doi"]).replace("If you use OntoJourney, please cite the ontology release below.","Reserved DOI for release preparation; cite only after publication.")
write(DEST/"CITATION.cff",s)
dump(DEST/"RELEASE_STATUS.json",meta)
for q in sorted((ROOT/"queries").glob("*.rq")): cp(q,R/"evaluation/queries"/q.name)
cp(ROOT/"synthetic-completion.ttl",R/"evaluation/synthetic-completion.ttl")
for f in ("candidate-verify.json","candidate-transformed.ttl","ci-validation.log"): cp(INPUT/f,V/f)
# Public evaluation runner: no dependency on the live repository or nonpublic graphs.
write(R/"evaluation/run_evaluation.py",'''from pathlib import Path
from rdflib import Graph,Namespace
from pyshacl import validate
R=Path(__file__).resolve().parents[1]
def load(p): return Graph().parse(p,format="turtle")
ont=load(R/"generated/OntoJourneyCore.ttl")
core=load(R/"shacl/ontojourney-core-v0.9.2.shacl.ttl")
strict=core+load(R/"shacl/structural-completeness-experimental.ttl")
original=load(R/"tests/data/positive.ttl")
complete=original+load(R/"evaluation/synthetic-completion.ttl")
for label,g,expected in [("original",original,[1,0,2,2,1,1,1,2,3]),("complete",complete,[1,1,2,2,1,1,1,2,3])]:
    counts=[len(list((ont+g).query((R/"evaluation/queries"/f"CQ{i}.rq").read_text()))) for i in range(1,10)]
    assert counts==expected,(label,counts)
    print(label,"CQ1-CQ9",counts)
def check(label,g,expected):
    actual,_,report=validate(g,shacl_graph=strict,ont_graph=ont,inference="rdfs",advanced=True,meta_shacl=True)
    assert bool(actual)==expected,(label,report)
    print(label,"PASS",actual)
check("original/strict",original,False)
check("complete/strict",complete,True)
EX=Namespace("https://example.org/test#"); OJ=Namespace("https://w3id.org/ontojourney/core#")
for name,s,p in [("narrative",EX.model,OJ.hasNarrative),("purpose",EX.model,OJ.hasEducationalPurpose),("framing",EX.stage1,OJ.hasNarrativeFraming),("mission",EX.stage1,OJ.hasMission),("assistance",EX.stage2,OJ.hasAssistance)]:
    m=Graph(); m+=complete; m.remove((s,p,None)); check("missing "+name,m,False)
''')
# Full cross-format definition consistency, with explicit unpublished metadata.
a=R/"tests/audit_release_consistency.py";s=a.read_text().replace("0.9.1","0.9.2").replace("assert len(graph) == 368, (path.name, len(graph))","assert len(graph) == "+str(len(g))+", (path.name, len(graph))")
s=s.replace('assert (\n            ONTOLOGY_IRI,\n            DCTERMS.issued,\n            Literal("2026-08-21", datatype=XSD.date),\n        ) in graph','assert not list(graph.objects(ONTOLOGY_IRI, DCTERMS.issued))').replace('Literal("2026-08-21", datatype=XSD.date)','Literal("2026-11-21", datatype=XSD.date)').replace('assert codemeta["datePublished"] == "2026-08-21"','assert "datePublished" not in codemeta').replace('assert "developmentStatus" not in codemeta','assert codemeta["developmentStatus"] == "Unpublished release preparation"')
write(a,s)
write(DEST/"README.md",'''# OntoJourney Core v0.9.2 — release preparation
UNPUBLISHED. DOI 10.5281/zenodo.24420185 is reserved, not registered. Target version IRI is not activated.

40 classes, 27 relations, 34 generalizations. StageSpecification now specialises Description; HLJStageSpecification also specialises PlanDescription. Public identifiers, stereotypes and association multiplicities are unchanged. Generic-stage entailments change. Core SHACL is unchanged; optional structural-completeness-experimental.ttl must be combined with Core.

Use Python dependencies in reproducible/requirements-validation.txt. Run reproducible/tests/audit_generated_json.py, audit_release_consistency.py, run_shacl_tests.py, and reproducible/evaluation/run_evaluation.py. The original positive graph is incomplete under the experimental overlay; the completed synthetic example is not learner data. Case 01 material and raw local logs are excluded pending redistribution review. The PlantUML view is manually aligned to the verified taxonomic delta. The JSON was regenerated in CI; nonsemantic IDs may differ from the locally generated input. See validation/ for CI output and the PR for original evidence provenance. No independent expert review or pedagogical effectiveness is established.

Promotion requires author review, final publication metadata/date, exact byte freeze, and the same archive in GitHub, Pages and Zenodo. Do not publish this review ZIP.
''')
write(DEST/"PUBLICATION.md","Stable ontology IRI: "+meta["ontologyIRI"]+"\n\nNamespace: "+meta["namespace"]+"\n\nTarget version IRI: "+meta["versionIRI"]+"\n\nReserved DOI: "+meta["doi"]+"\n\nPrior version and all historical artifacts remain unchanged. W3ID version routes are activated only after versioned hosting is verified.\n")
write(DEST/"CHANGELOG.md","# v0.9.2 — pending publication\n\n- Generalize StageSpecification to Description; preserve planned HLJ stage typing.\n- Keep Core SHACL unchanged; add opt-in experimental completeness and synthetic CQ tests.\n- Preserve identifiers; generic-stage entailments change.\n\n"+(BASE/"CHANGELOG.md").read_text())
write(DEST/"VALIDATION_REPORT.md","CI-generated review artifact. See validation/ci-validation.log for transformation and tests. The author separately executed HermiT on the locally transformed candidate with 356 input axioms and 414 output axioms; this CI archive is a regenerated serialization with the same checked logical delta. Formal checks do not replace domain expert evaluation. Publication pending.\n")
for name in ("audit_generated_json.py","audit_release_consistency.py","run_shacl_tests.py"):
    script(R/"tests"/name)
script(R/"evaluation/run_evaluation.py")
files=sorted(p for p in DEST.rglob("*") if p.is_file() and "__pycache__" not in p.parts)
write(DEST/"SHA256SUMS","".join(hashlib.sha256(p.read_bytes()).hexdigest()+"  "+p.relative_to(DEST).as_posix()+"\n" for p in files))
zip_path=OUT/"ontojourney-core-v0.9.2-PREVIEW.zip"
with zipfile.ZipFile(zip_path,"w",compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in sorted(files+[DEST/"SHA256SUMS"]):
        info=zipfile.ZipInfo(DEST.name+"/"+p.relative_to(DEST).as_posix(),date_time=(2026,11,21,0,0,0));info.create_system=3;info.external_attr=0o100644<<16
        z.writestr(info,p.read_bytes(),compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
with zipfile.ZipFile(zip_path) as z:
    assert z.testzip() is None
    for p in files+[DEST/"SHA256SUMS"]: assert z.read(DEST.name+"/"+p.relative_to(DEST).as_posix())==p.read_bytes()
write(OUT/"SHA256SUMS",hashlib.sha256(zip_path.read_bytes()).hexdigest()+"  "+zip_path.name+"\n")
print("PASS: unpublished preview archive",len(files),"files; RDF triples",len(g))
