from pathlib import Path
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
