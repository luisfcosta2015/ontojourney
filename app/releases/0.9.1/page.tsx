import type { Metadata } from "next";
import Link from "next/link";

import { PageHero } from "@/components/page-hero";
import {
  CONCEPT_DOI,
  REPOSITORY_URL,
  VERSION,
  VERSION_DOI,
  VERSION_IRI,
  assetUrl,
} from "@/lib/site";

export const metadata: Metadata = {
  title: "Release 0.9.1",
  description:
    "Release notes, validation status, identifiers, and downloads for OntoJourney Core v0.9.1.",
};

const contents = [
  "Canonical English definitions for all 40 domain classes in Tonto, OntoUML JSON, Markdown, LaTeX, and RDF.",
  "Turtle, RDF/XML, JSON-LD, and N-Triples serializations with 368 isomorphic triples.",
  "Stricter SHACL constraints with one conforming and nine deliberately invalid fixtures.",
  "Technical validation records and the raw response for the exact OntoUML JSON submitted to the OntoUML API.",
  "Checksums, citation metadata, licensing, and reproducibility scripts.",
];

export default function ReleasePage() {
  return (
    <main id="main-content">
      <PageHero
        eyebrow="Release · 21 August 2026"
        title="OntoJourney Core v0.9.1"
        lead="This compatible preview update adds canonical class definitions and stricter validation constraints while preserving every public class IRI, relation IRI, and generalization from v0.9.0."
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
                The archive contains public ontology artifacts and technical
                documentation; it does not contain the full unpublished
                article.
              </p>
            </section>

            <section id="validation">
              <h2>Validation</h2>
              <p>
                Version {VERSION} passed local Tonto validation, OntoUML JSON
                structural auditing, cross-format definition checks, RDF
                parsing and isomorphism checks, SHACL fixture tests, remote
                OntoUML verification, and HermiT classification through ROBOT.
              </p>
              <p>
                OntoUML API input hash:
                <code>2465501b7152b50e5c6c01197d47dbc45df591010757b4ecc2453d5761b8436d</code>.
              </p>
              <Link className="button button--secondary" href="/validation/">Inspect validation evidence</Link>
            </section>

            <section id="identifiers">
              <h2>Identifiers</h2>
              <p>Version IRI: <a href={VERSION_IRI}>{VERSION_IRI}</a></p>
              <p>Version DOI: <a href={VERSION_DOI}>{VERSION_DOI}</a></p>
              <p>Concept DOI for all versions: <a href={CONCEPT_DOI}>{CONCEPT_DOI}</a></p>
              <p>
                Entity identifiers retain the stable non-versioned namespace
                <code>https://w3id.org/ontojourney/core#</code>.
              </p>
            </section>

            <section id="download">
              <h2>Download</h2>
              <p>
                The repository provides the complete release archive and each
                machine-readable representation separately. The GitHub release
                is the source used for subsequent Zenodo archival.
              </p>
              <div className="button-row">
                <a className="button button--primary" href={assetUrl(`/artifacts/${VERSION}/ontojourney-core-v${VERSION}.zip`)} download>
                  Download repository copy <span aria-hidden="true">↓</span>
                </a>
                <a className="button button--secondary" href={`${REPOSITORY_URL}/releases/tag/v${VERSION}`}>
                  Open GitHub release <span aria-hidden="true">↗</span>
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
