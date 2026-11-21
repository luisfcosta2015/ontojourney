const fs=require('fs'),path=require('path');
const {serializationUtils,OntoumlVerification,Ontouml2Gufo}=require('ontouml-js');
const root=__dirname,out=path.join(root,'candidate-output');fs.mkdirSync(out,{recursive:true});
const raw=fs.readFileSync(path.join(root,'tonto-project/generated/OntoJourneyCore.json'),'utf8');
const project=()=>serializationUtils.parse(raw,true);
(async()=>{
 const v=await new OntoumlVerification(project(),null).run();
 fs.writeFileSync(path.join(out,'candidate-verify.json'),JSON.stringify(v,null,2)+'\n');
 if(!Array.isArray(v.result)||v.result.length||(v.issues&&v.issues.length))throw Error('verification failed');
 const t=await new Ontouml2Gufo(project(),{format:'turtle',baseIri:'https://w3id.org/ontojourney/core',basePrefix:'oj',uriFormatBy:'name',createObjectProperty:true,createInverses:false,prefixPackages:false}).run();
 if(typeof t.result!=='string'||!t.result.trim()||(t.issues&&t.issues.length))throw Error('transformation failed');
 fs.writeFileSync(path.join(out,'candidate-transformed.ttl'),t.result);
 console.log('PASS: local OntoUML verification and transformation');
})().catch(e=>{console.error(e);process.exitCode=1});
