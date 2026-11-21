import type { Metadata } from "next";
import Link from "next/link";
import { PageHero } from "@/components/page-hero";
import { ENTITY_NAMESPACE, assetUrl } from "@/lib/site";

export const metadata: Metadata = {
  title: "Release 0.9.2",
  description: "OntoJourney Core v0.9.2 release notes and downloads.",
};

export default function ReleasePage() {
  return (
    <main id="main-content">
      <PageHero eyebrow="Release · 21 November 2026"
        title="OntoJourney Core v0.9.2"
        lead="A reviewed taxonomic correction distinguishing descriptive stage patterns from planned HLJ stages." />
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
              <p>The Core SHACL graph is unchanged. An optional experimental completeness profile is included to check association bounds and target types. It is not a replacement for Core SHACL.</p>
            </section>
            <section id="validation">
              <h2>Technical evidence</h2>
              <p>Local Tonto, OntoUML verification and gUFO transformation, HermiT classification, Core SHACL, and SPARQL regression tests passed on the examined candidate. CI reproduced the transformation, four RDF serializations and synthetic graph tests. Domain review, execution evidence and educational effectiveness are not established by these checks.</p>
              <p>See the archived technical validation report for evidence and limitations.</p>
            </section>
            <section id="identifiers">
              <h2>Persistent identifiers</h2>
              <p>Entity namespace: <code>{ENTITY_NAMESPACE}</code></p>
              <p>Target version IRI: <code>https://w3id.org/ontojourney/core/0.9.2</code>.</p>
              <p>Version DOI: <a href="https://doi.org/10.5281/zenodo.24420185">10.5281/zenodo.24420185</a>.</p>
              <p>Cite the version-specific DOI for the exact archive.</p>
              <div className="button-row">
                <Link className="button button--secondary" href="/releases/0.9.1/">Previous release</Link>
                <a className="button button--primary" href={assetUrl("/artifacts/0.9.2/ontojourney-core-v0.9.2.zip")} download>Download v0.9.2</a>
              </div>
            </section>
          </article>
        </div>
      </section>
    </main>
  );
}
