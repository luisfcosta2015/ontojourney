import type { Metadata } from "next";
import Link from "next/link";

import { PageHero } from "@/components/page-hero";
import { assetUrl } from "@/lib/site";

export const metadata: Metadata = {
  title: "Release 0.9.0",
  description:
    "Public release notes, validation status, identifiers, and downloads for OntoJourney Core v0.9.0.",
};

const VERSION_DOI = "https://doi.org/10.5281/zenodo.21802021";
const CONCEPT_DOI = "https://doi.org/10.5281/zenodo.21802020";
const VERSION_IRI = "https://w3id.org/ontojourney/core/0.9";

const contents = [
  "Canonical Tonto source and OntoUML JSON exchange model.",
  "Turtle, RDF/XML, JSON-LD, and N-Triples serializations.",
  "SHACL shapes with one conforming and two invalid test fixtures.",
  "Technical validation records and the raw OntoUML API response.",
  "Checksums, citation metadata, licensing, and reproducibility scripts.",
];

export default function ReleasePage() {
  return (
    <main id="main-content">
      <PageHero
        eyebrow="Release · 1 August 2026"
        title="OntoJourney Core v0.9.0"
        lead="The first public preview release packages the ontology's source, exchange model, Web serializations, constraints, tests, validation evidence, and citation metadata under stable identifiers."
      />

      <section className="section">
        <div className="site-container prose-layout">
          <aside className="toc">
            <h2>Release contents</h2>
            <ol>
              <li><a href="#contents">Contents</a></li>
              <li><a href="#validation">Validation</a></li>
              <li><a href="#identifiers">Identifiers</a></li>
              <li><a href="#download">Download</a></li>
            </ol>
          </aside>
          <article className="prose">
            <section id="contents">
              <h2>Contents</h2>
              <ul>{contents.map((item) => <li key={item}>{item}</li>)}</ul>
              <p>
                The archive deliberately contains only public ontology
                artifacts and technical documentation for this release.
              </p>
            </section>

            <section id="validation">
              <h2>Validation</h2>
              <p>
                Version 0.9.0 passed local Tonto validation, OntoUML JSON
                structural auditing, RDF parsing, SHACL fixture tests, remote
                OntoUML verification, and Protégé/HermiT classification.
              </p>
              <p>
                OntoUML API input hash:
                <code>7830fc94d0741517bbb415094ed3ff08204a166419b92627b4aa300192f6e18a</code>.
              </p>
              <Link className="button button--secondary" href="/validation/">Inspect validation evidence</Link>
            </section>

            <section id="identifiers">
              <h2>Identifiers</h2>
              <p>Version IRI: <a href={VERSION_IRI}>{VERSION_IRI}</a></p>
              <p>Version DOI: <a href={VERSION_DOI}>{VERSION_DOI}</a></p>
              <p>Concept DOI for all versions: <a href={CONCEPT_DOI}>{CONCEPT_DOI}</a></p>
              <p>
                Entity identifiers use the stable non-versioned namespace
                <code>https://w3id.org/ontojourney/core#</code>.
              </p>
            </section>

            <section id="download">
              <h2>Download</h2>
              <p>
                Zenodo preserves the citable archive for version 0.9.0. The
                repository also provides the corresponding public release
                artifacts and validation records.
              </p>
              <div className="button-row">
                <a className="button button--primary" href={VERSION_DOI}>
                  Open archived release <span aria-hidden="true">↗</span>
                </a>
                <a className="button button--secondary" href={assetUrl("/artifacts/0.9.0/ontojourney-core-v0.9.0.zip")} download>
                  Download repository copy <span aria-hidden="true">↓</span>
                </a>
                <Link className="button button--secondary" href="/resources/">Select individual files</Link>
              </div>
            </section>
          </article>
        </div>
      </section>
    </main>
  );
}
