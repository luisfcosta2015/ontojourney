import type { Metadata } from "next";
import Link from "next/link";
import { PageHero } from "@/components/page-hero";
import { ENTITY_NAMESPACE, assetUrl } from "@/lib/site";

export const metadata: Metadata = {
  title: "Release review 0.9.2",
  description: "Unpublished OntoJourney Core v0.9.2 release preparation.",
  robots: { index: false, follow: false },
};

export default function ReleasePage() {
  return (
    <main id="main-content">
      <PageHero eyebrow="Release preparation · unpublished"
        title="OntoJourney Core v0.9.2"
        lead="A reviewed taxonomic correction distinguishing descriptive stage patterns from planned HLJ stages. This page is a draft; the currently published release remains v0.9.1." />
      <section className="section">
        <div className="site-container prose-layout">
          <aside className="toc">
            <h2>Release review</h2>
            <ol><li><a href="#changes">Changes</a></li><li><a href="#validation">Validation</a></li><li><a href="#identifiers">Identifiers</a></li></ol>
          </aside>
          <article className="prose">
            <section id="changes">
              <h2>Taxonomic correction</h2>
              <p><code>StageSpecification</code> specialises <code>Description</code> rather than <code>PlanDescription</code>. <code>HLJStageSpecification</code> specialises both <code>StageSpecification</code> and <code>PlanDescription</code>.</p>
              <p>40 classes, 27 relations, 34 generalizations. All public term IRIs, relation multiplicities and stereotypes are unchanged. Generic stages no longer entail PlanDescription or NormativeDescription; existing HLJ stages retain those entailments. Semantic backward compatibility is therefore not unconditional.</p>
              <p>The Core SHACL graph is unchanged. An optional experimental completeness profile is being prepared to check association bounds and target types. It is not a replacement for Core SHACL.</p>
            </section>
            <section id="validation">
              <h2>Technical evidence</h2>
              <p>Local Tonto, OntoUML verification and gUFO transformation, HermiT classification, Core SHACL, and SPARQL regression tests passed on the examined candidate. CI reproduced the transformation, four RDF serializations and synthetic graph tests. Domain review, execution evidence and educational effectiveness are not established by these checks.</p>
              <p>Final release packaging and publication checks remain pending.</p>
            </section>
            <section id="identifiers">
              <h2>Reserved identifiers</h2>
              <p>Entity namespace: <code>{ENTITY_NAMESPACE}</code></p>
              <p>Target version IRI: <code>https://w3id.org/ontojourney/core/0.9.2</code> (not activated).</p>
              <p>Reserved Zenodo DOI: <code>10.5281/zenodo.24420185</code> (not yet registered or published).</p>
              <p>Until publication, cite and download the official v0.9.1 release.</p>
              <div className="button-row">
                <Link className="button button--secondary" href="/releases/0.9.1/">Previous release</Link>
                <a className="button button--primary" href={assetUrl("/artifacts/0.9.1/ontojourney-core-v0.9.1.zip")} download>Download published v0.9.1</a>
              </div>
            </section>
          </article>
        </div>
      </section>
    </main>
  );
}
