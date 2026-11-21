import type { Metadata } from "next";
import Link from "next/link";

import { PageHero } from "@/components/page-hero";
import { CANONICAL_IRI, ENTITY_NAMESPACE, VERSION_IRI } from "@/lib/site";

export const metadata: Metadata = {
  title: "Documentation",
  description:
    "Public scope, release structure, identifiers, and reuse guidance for OntoJourney Core v0.9.2.",
};

const toc = [
  ["purpose", "Purpose"],
  ["release", "Release structure"],
  ["representations", "Representations"],
  ["identifiers", "Identifiers"],
  ["reuse", "Reuse"],
];

export default function DocumentationPage() {
  return (
    <main id="main-content">
      <PageHero
        eyebrow="Documentation"
        title="A concise guide to the public ontology release."
        lead="This documentation describes the published artifact, its representations, persistent identifiers, and reuse path. The searchable reference remains the authoritative index of public terms."
      />
      <div className="site-container section prose-layout">
        <aside className="toc" aria-label="On this page">
          <h2>On this page</h2>
          <ol>
            {toc.map(([id, label]) => (
              <li key={id}><a href={`#${id}`}>{label}</a></li>
            ))}
          </ol>
        </aside>

        <article className="prose">
          <section id="purpose">
            <h2>Purpose</h2>
            <p>
              OntoJourney publishes a formally typed vocabulary for
              narrative-heroic learning journeys. The public core is intended
              for ontology inspection, data modeling, validation experiments,
              scholarly citation, and compatible extension work.
            </p>
            <p>
              The release is not a general ontology of every educational
              platform or every metaphorical use of the word “journey”. Reusers
              should inspect the public terms and declare any local extension
              separately.
            </p>
          </section>

          <section id="release">
            <h2>Release structure</h2>
            <div className="layer-stack">
              <div className="layer">
                <strong>Source</strong>
                <span>Tonto records the editable conceptual source.</span>
              </div>
              <div className="layer">
                <strong>Exchange</strong>
                <span>OntoUML JSON supports model interchange and the generated term reference.</span>
              </div>
              <div className="layer">
                <strong>Web data</strong>
                <span>RDF serializations publish the vocabulary for linked-data tooling.</span>
              </div>
              <div className="layer">
                <strong>Constraints</strong>
                <span>SHACL shapes and fixtures provide reproducible validation behavior.</span>
              </div>
            </div>
            <p>
              Checksums, citation metadata, validation records, and automated
              tests accompany these representations in the versioned archive.
            </p>
          </section>

          <section id="representations">
            <h2>Representations</h2>
            <p>
              Different files serve different tools. Tonto is the conceptual
              source; OntoUML JSON is the exchange representation; Turtle,
              RDF/XML, JSON-LD, and N-Triples are Web serializations; SHACL is
              the operational constraint graph.
            </p>
            <p>
              The project therefore publishes the representations together and
              identifies their version explicitly. A transformation between
              formats should not be treated as evidence that every modeling
              feature has identical expressivity in every language.
            </p>
          </section>

          <section id="identifiers">
            <h2>Identifiers</h2>
            <p><strong>Ontology IRI</strong><br /><code>{CANONICAL_IRI}</code></p>
            <p><strong>Entity namespace</strong><br /><code>{ENTITY_NAMESPACE}</code></p>
            <p><strong>Version IRI</strong><br /><code>{VERSION_IRI}</code></p>
            <div className="callout">
              <strong>Versioning rule.</strong> Public entity IRIs remain
              non-versioned across compatible releases. The version IRI
              identifies the release as a whole.
            </div>
            <p>
              The W3ID resolver is active and uses immutable version-specific
              routes. <code>/core/0.9</code> remains assigned to v0.9.0,
              <code>/core/0.9.1</code> remains assigned to v0.9.1, <code>/core/0.9.2</code> identifies this release, and the
              unversioned <code>/core</code> route is updated only after the
              corresponding GitHub Pages artifacts are available.
            </p>
          </section>

          <section id="reuse">
            <h2>Reuse</h2>
            <ol>
              <li>Browse the generated term reference and confirm the public scope.</li>
              <li>Download the representation required by the target workflow.</li>
              <li>Keep project-specific terms in a namespace controlled by the extending project.</li>
              <li>Run the published validation fixtures before adding local data.</li>
              <li>Cite the exact version used and record any local modifications.</li>
            </ol>
            <div className="button-row">
              <Link className="button button--primary" href="/model/reference/">
                Browse public terms <span aria-hidden="true">→</span>
              </Link>
              <Link className="button button--secondary" href="/resources/">
                Download and cite
              </Link>
            </div>
          </section>
        </article>
      </div>
    </main>
  );
}
