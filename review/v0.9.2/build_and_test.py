"""Build and test an unpublished candidate without changing production."""
import json, shutil, runpy
from pathlib import Path
from rdflib import Graph, Namespace, Literal, URIRef, RDF, RDFS, OWL, BNode
from rdflib.namespace import DCTERMS, XSD
from rdflib.compare import isomorphic
from pyshacl import validate

ROOT=Path(__file__).resolve().parent
BASE=ROOT.parents[1]/"ontology"
OUT=ROOT/"candidate-output"
OUT.mkdir(exist_ok=True)
OJ=Namespace("https://w3id.org/ontojourney/core#")
SH=Namespace("http://www.w3.org/ns/shacl#")
AUD=Namespace("https://example.org/ontojourney/audit#")
IRI=URIRef("https://w3id.org/ontojourney/core")
def load(p): return Graph().parse(p,format="turtle")
def elements(p):
    es=[e for pkg in json.loads(p.read_text())["model"]["contents"] for e in pkg["contents"]]
    ids={e["id"]:e["name"] for e in es if e.get("name")}
    classes={e["name"]:(e["stereotype"],e["description"]) for e in es if e["type"]=="Class" and e["stereotype"]!="datatype"}
    rels={e["name"]:(e.get("stereotype"),tuple((ids[x["propertyType"]["id"]],x["cardinality"],x["aggregationKind"]) for x in e["properties"])) for e in es if e["type"]=="Relation"}
    gens={(ids[e["specific"]["id"]],ids[e["general"]["id"]]) for e in es if e["type"]=="Generalization"}
    return classes,rels,gens
bc,br,bg=elements(BASE/"OntoJourneyCore.json")
cc,cr,cg=elements(ROOT/"tonto-project/generated/OntoJourneyCore.json")
assert (len(cc),len(cr),len(cg))==(40,27,34)
assert set(bc)==set(cc) and br==cr and {k:v[0] for k,v in bc.items()}=={k:v[0] for k,v in cc.items()}
assert {k for k in cc if cc[k][1]!=bc[k][1]}=={"StageSpecification","HLJStageSpecification"}
assert bg-cg=={("StageSpecification","PlanDescription")}
assert cg-bg=={("StageSpecification","Description"),("HLJStageSpecification","PlanDescription")}
print("PASS: JSON exact semantic delta")
baseline=load(BASE/"ontojourney-core.ttl")
actual=load(OUT/"candidate-transformed.ttl")
g=Graph();g+=baseline
g.remove((OJ.StageSpecification,RDFS.subClassOf,OJ.PlanDescription))
g.add((OJ.StageSpecification,RDFS.subClassOf,OJ.Description))
g.add((OJ.HLJStageSpecification,RDFS.subClassOf,OJ.PlanDescription))
def axioms(graph):
    a=Graph(); onts=set(graph.subjects(RDF.type,OWL.Ontology))
    for s,p,o in graph:
        if p not in {RDFS.label,RDFS.comment,OWL.versionIRI,OWL.versionInfo,OWL.priorVersion} and (s not in onts or p==OWL.imports): a.add((s,p,o))
    return a
assert isomorphic(axioms(actual),axioms(g)), "Unexpected transformed axiom delta"
print("PASS: transformed OWL exact axiom delta")
g.set((IRI,OWL.versionIRI,URIRef(str(IRI)+"/0.9.2-rc.1")))
g.set((IRI,OWL.versionInfo,Literal("0.9.2-rc.1")))
g.set((IRI,OWL.priorVersion,URIRef(str(IRI)+"/0.9.1")))
g.remove((IRI,DCTERMS.issued,None))
g.set((IRI,DCTERMS.modified,Literal("2026-11-21",datatype=XSD.date)))
for name,(_,desc) in cc.items():
    if isinstance(desc,dict): desc=desc.get("en") or desc.get("en-GB") or desc.get("en-US")
    assert isinstance(desc,str) and desc.strip(),name
    g.set((OJ[name],RDFS.comment,Literal(desc,lang="en")))
for ext,fmt in [("ttl","turtle"),("rdf","xml"),("nt","nt"),("jsonld","json-ld")]:
    p=OUT/("ontojourney-core."+ext);g.serialize(p,format=fmt)
    assert isomorphic(g,Graph().parse(p,format=fmt))
assert isomorphic(axioms(g),axioms(actual))
print("PASS: four RDF serializations and axioms aligned")
tests=BASE/"reproducible/tests"
core=load(BASE/"ontojourney-core.shacl.ttl")
shutil.copyfile(BASE/"ontojourney-core.shacl.ttl",OUT/"ontojourney-core.shacl.ttl")
def check(name,data,shapes,expected,messages=()):
    ok,_,report=validate(data_graph=data,shacl_graph=shapes,ont_graph=g,inference="rdfs",advanced=True,meta_shacl=True,abort_on_first=False)
    assert bool(ok)==expected,(name,report)
    assert all(m in report for m in messages),(name,report)
    print(name,"PASS",ok)
for name,expected,messages in runpy.run_path(str(tests/"run_shacl_tests.py"))["CASES"]:
    check(name,load(tests/"data"/name),core,expected,messages)
overlay=Graph()
for name,(_,ends) in cr.items():
    for direction,src,dst in [("Forward",ends[0],ends[1]),("Inverse",ends[1],ends[0])]:
        node=AUD[name+direction+"Shape"]; prop=BNode()
        overlay.add((node,RDF.type,SH.NodeShape));overlay.add((node,SH.targetClass,OJ[src[0]]));overlay.add((node,SH.property,prop))
        path=OJ[name]
        if direction=="Inverse":
            path=BNode();overlay.add((path,SH.inversePath,OJ[name]))
        overlay.add((prop,SH.path,path));overlay.add((prop,SH["class"],OJ[dst[0]]))
        low,high=dst[1].split("..")
        if int(low):overlay.add((prop,SH.minCount,Literal(int(low))))
        if high!="*":overlay.add((prop,SH.maxCount,Literal(int(high))))
assert len(set(overlay.subjects(RDF.type,SH.NodeShape)))==54
overlay.serialize(OUT/"structural-completeness-experimental.ttl",format="turtle")
strict=core+overlay
original=load(tests/"data/positive.ttl")
complete=original+load(ROOT/"synthetic-completion.ttl")
check("original/strict",original,strict,False)
check("completed/strict",complete,strict,True)
EX=Namespace("https://example.org/test#")
for name,s,p in [("narrative",EX.model,OJ.hasNarrative),("purpose",EX.model,OJ.hasEducationalPurpose),("framing",EX.stage1,OJ.hasNarrativeFraming),("mission",EX.stage1,OJ.hasMission),("assistance",EX.stage2,OJ.hasAssistance)]:
    mutated=Graph();mutated+=complete;mutated.remove((s,p,None));check("missing "+name,mutated,strict,False)
for label,data,counts in [("original",original,[1,0,2,2,1,1,1,2,3]),("completed",complete,[1,1,2,2,1,1,1,2,3])]:
    for i,count in enumerate(counts,1):
        q=(ROOT/"queries"/f"CQ{i}.rq").read_text()
        b=sorted(tuple(str(v) if v is not None else "" for v in row) for row in (baseline+data).query(q))
        c=sorted(tuple(str(v) if v is not None else "" for v in row) for row in (g+data).query(q))
        assert b==c and len(c)==count,(label,i,b,c)
        print(label,"CQ"+str(i),"PASS",count)
for src,dst in [(ROOT/"tonto-project/src/core.tonto","core.tonto"),(ROOT/"tonto-project/tonto.json","tonto.json"),(ROOT/"tonto-project/generated/OntoJourneyCore.json","OntoJourneyCore.json"),(BASE/"LICENSE","LICENSE")]:
    shutil.copyfile(src,OUT/dst)
print("PASS: candidate build and synthetic regression suite")
