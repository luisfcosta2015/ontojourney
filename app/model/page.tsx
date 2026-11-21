import type { Metadata } from "next";
import Link from "next/link";

import { PageHero } from "@/components/page-hero";
import { ENTITY_NAMESPACE, VERSION, assetUrl } from "@/lib/site";

export const metadata: Metadata = {
  title: "Model overview",
  description:
    "Public OntoJourney Core v0.9.2 statistics, representations, namespace, and generated term reference.",
};

const layers = [
  ["Conceptual source", "core.tonto", "Editable Tonto source for the OntoUML model."],
  ["Exchange model", "OntoJourneyCore.json", "OntoUML JSON used to generate the searchable reference."],
  ["Web ontology", "ontojourney-core.ttl", "gUFO-aligned RDF vocabulary in Turtle and equivalent serializations."],
  ["Constraint graph", "ontojourney-core.shacl.ttl", "SHACL shapes accompanied by positive and negative fixtures."],
];

export default function ModelPage() {
  return (
    <main id="main-content">
      <PageHero
        eyebrow="Model overview"
        title="Inspect the public model from its generated vocabulary."
        lead={`OntoJourney Core v${VERSION} publishes 40 domain classes, 27 relation records, and 34 generalization records. Its term explorer is generated from the versioned OntoUML JSON rather than maintained as a second model.`}
      />

      <section className="stat-grid" aria-label="Public model statistics">
        <div className="stat"><strong>40</strong><span>Domain classes</span></div>
        <div className="stat"><strong>27</strong><span>Relations</span></div>
        <div className="stat"><strong>34</strong><span>Generalizations</span></div>
        <div className="stat"><strong>1</strong><span>Stable entity namespace</span></div>
      </section>

      <section className="section" aria-labelledby="representations-title">
        <div className="site-container">
          <div className="section-heading">
            <div>
              <p className="eyebrow">Representations</p>
              <h2 className="section-title" id="representations-title">
                One release, four complementary layers.
              </h2>
            </div>
            <p>
              Each artifact is published with a specific role. The release
              archive keeps them together with checksums and validation records.
            </p>
          </div>
          <div className="data-table-wrap">
            <table className="data-table">
              <thead><tr><th>Layer</th><th>Primary file</th><th>Role</th></tr></thead>
              <tbody>
                {layers.map(([layer, file, role]) => (
                  <tr key={layer}><td><strong>{layer}</strong></td><td><code>{file}</code></td><td>{role}</td></tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </section>

      <section className="section section--tinted" aria-labelledby="namespace-title">
        <div className="site-container split">
          <div>
            <p className="eyebrow">Identity</p>
            <h2 className="section-title" id="namespace-title">
              Stable public term IRIs.
            </h2>
          </div>
          <div>
            <p className="lead">
              Every public class and relation is identified under
              <code>{ENTITY_NAMESPACE}</code>. Compatible releases retain these
              identifiers while the release itself receives a version IRI.
            </p>
            <Link className="button button--primary" href="/model/reference/">
              Search all public terms <span aria-hidden="true">→</span>
            </Link>
          </div>
        </div>
      </section>

      <section className="section" aria-labelledby="download-title">
        <div className="site-container split">
          <div>
            <p className="eyebrow">Direct access</p>
            <h2 className="section-title" id="download-title">
              Use the format your tooling expects.
            </h2>
          </div>
          <div className="button-row">
            <a className="button button--primary" href={assetUrl(`/artifacts/${VERSION}/OntoJourneyCore.json`)} download>
              OntoUML JSON <span aria-hidden="true">↓</span>
            </a>
            <a className="button button--secondary" href={assetUrl(`/artifacts/${VERSION}/ontojourney-core.ttl`)} download>
              Turtle <span aria-hidden="true">↓</span>
            </a>
            <Link className="button button--secondary" href="/resources/">
              All resources
            </Link>
          </div>
        </div>
      </section>
    </main>
  );
}
