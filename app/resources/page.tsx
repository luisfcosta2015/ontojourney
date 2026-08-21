import type { Metadata } from "next";
import Link from "next/link";

import { PageHero } from "@/components/page-hero";
import {
  CANONICAL_IRI,
  CONCEPT_DOI,
  ENTITY_NAMESPACE,
  REPOSITORY_URL,
  VERSION,
  VERSION_IRI,
  assetUrl,
} from "@/lib/site";

export const metadata: Metadata = {
  title: "Resources and citation",
  description:
    "Download OntoJourney Core v0.9.1 in Tonto, OntoUML JSON, RDF, and SHACL formats, with checksums and citation metadata.",
};

const downloads = [
  ["Complete release", "ZIP · source, serializations, tests, metadata, and validation", `ontojourney-core-v${VERSION}.zip`],
  ["Turtle", "RDF/Turtle · public Web ontology", "ontojourney-core.ttl"],
  ["RDF/XML", "RDF/XML · OWL-compatible serialization", "ontojourney-core.rdf"],
  ["JSON-LD", "JSON-LD · linked-data serialization", "ontojourney-core.jsonld"],
  ["N-Triples", "N-Triples · line-oriented RDF", "ontojourney-core.nt"],
  ["OntoUML JSON", "OntoUML model exchange project", "OntoJourneyCore.json"],
  ["Tonto source", "Canonical textual conceptual model", "core.tonto"],
  ["SHACL shapes", "Operational constraint graph", "ontojourney-core.shacl.ttl"],
  ["Checksums", "SHA-256 manifest for release files", "SHA256SUMS"],
];

export default function ResourcesPage() {
  const artifactRoot = `/artifacts/${VERSION}`;

  return (
    <main id="main-content">
      <PageHero
        eyebrow="Resources"
        title="Download and cite a versioned research artifact."
        lead="The public archive combines the conceptual source, exchange model, Web serializations, SHACL shapes, tests, validation records, checksums, and citation metadata."
      />

      <section className="section" aria-labelledby="downloads-title">
        <div className="site-container">
          <div className="section-heading">
            <div>
              <p className="eyebrow">{`Core v${VERSION}`}</p>
              <h2 className="section-title" id="downloads-title">Machine-readable artifacts.</h2>
            </div>
            <p>
              Use the complete archive for reproducibility or select an
              individual representation for a specific tool.
            </p>
          </div>
          <div className="download-grid">
            {downloads.map(([title, description, filename]) => (
              <a className="download-card" href={assetUrl(`${artifactRoot}/${filename}`)} key={filename} download>
                <span><strong>{title}</strong><span>{description}</span></span>
                <span className="download-card__arrow" aria-hidden="true">↓</span>
              </a>
            ))}
          </div>
        </div>
      </section>

      <section className="section section--tinted" aria-labelledby="iri-title">
        <div className="site-container split">
          <div>
            <p className="eyebrow">Persistent identification</p>
            <h2 className="section-title" id="iri-title">Stable identifiers, versioned releases.</h2>
          </div>
          <div>
            <p><strong>Ontology IRI</strong><br /><code>{CANONICAL_IRI}</code></p>
            <p><strong>Entity namespace</strong><br /><code>{ENTITY_NAMESPACE}</code></p>
            <p><strong>Version IRI</strong><br /><code>{VERSION_IRI}</code></p>
            <p>
              W3ID is the active persistent-identifier service. Its
              content-negotiation rules keep entity IRIs stable and route each
              version IRI to the corresponding documentation and RDF files.
            </p>
          </div>
        </div>
      </section>

      <section className="section" aria-labelledby="citation-title">
        <div className="site-container prose-layout">
          <aside className="toc">
            <h2>Citation formats</h2>
            <ol>
              <li><a href="#recommended-citation">Recommended citation</a></li>
              <li><a href="#bibtex">BibTeX</a></li>
              <li><a href="#metadata">Metadata files</a></li>
            </ol>
          </aside>
          <article className="prose">
            <section id="recommended-citation">
              <p className="eyebrow">Citation</p>
              <h2 id="citation-title">Credit the exact release used.</h2>
              <p>
                Costa, Luis Felipe Coimbra. 2026. <em>OntoJourney: An Ontology
                of Narrative-Heroic Learning Journeys</em>. OntoJourney Core
                {` v${VERSION}. `}<a href={VERSION_IRI}>{VERSION_IRI}</a>.
              </p>
              <p>
                The version IRI identifies this exact release. The
                <a href={CONCEPT_DOI}> Zenodo concept DOI</a> identifies the
                collection of OntoJourney versions; the v0.9.1 version DOI will
                be added after Zenodo creates the archive.
              </p>
            </section>
            <section id="bibtex">
              <h2>BibTeX</h2>
              <pre><code>{`@software{costa2026ontojourney,
  author  = {Costa, Luis Felipe Coimbra},
  title   = {OntoJourney: An Ontology of Narrative-Heroic Learning Journeys},
  year    = {2026},
  version = {${VERSION}},
  url     = {${VERSION_IRI}},
  license = {CC-BY-4.0}
}`}</code></pre>
            </section>
            <section id="metadata">
              <h2>Metadata files</h2>
              <p>
                <code>CITATION.cff</code>, <code>codemeta.json</code>, and the
                RDF metadata record the author, version, license, namespace,
                release date, and repository.
              </p>
            </section>
          </article>
        </div>
      </section>

      <section className="section section--tinted" aria-labelledby="assets-title">
        <div className="site-container split">
          <div>
            <p className="eyebrow">Published visual assets</p>
            <h2 className="section-title" id="assets-title">Separate provenance and licenses.</h2>
          </div>
          <div>
            <p className="lead">
              The Campbell, Murdock, and HLJ diagrams are previously published
              images reproduced unchanged under CC BY-NC-ND 4.0. The Heroic
              Journeys logo is used with permission and remains outside the
              repository&apos;s general license.
            </p>
            <div className="button-row">
              <Link className="button button--primary" href="/foundations/">View foundations <span aria-hidden="true">→</span></Link>
              <a className="button button--secondary" href={assetUrl("/ASSET-LICENSES.md")}>Asset licenses</a>
            </div>
          </div>
        </div>
      </section>

      <section className="section" id="contribute" aria-labelledby="contribute-title">
        <div className="site-container split">
          <div>
            <p className="eyebrow">Contribute</p>
            <h2 className="section-title" id="contribute-title">Propose corrections with traceability.</h2>
          </div>
          <div>
            <p className="lead">
              Structured issue templates are available for defects, questions,
              and term proposals. Each proposal should state its evidence,
              affected artifact, and compatibility impact.
            </p>
            <div className="button-row">
              <a className="button button--primary" href={`${REPOSITORY_URL}/issues/new/choose`}>Open an issue <span aria-hidden="true">↗</span></a>
              <a className="button button--secondary" href={`${REPOSITORY_URL}/blob/main/CONTRIBUTING.md`}>Contribution guide</a>
            </div>
          </div>
        </div>
      </section>
    </main>
  );
}
