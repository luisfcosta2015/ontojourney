import Image from "next/image";
import Link from "next/link";

import { ValidationStrip } from "@/components/validation-strip";
import { CONCEPT_DOI, RELEASE_LABEL, VERSION_DOI, assetUrl } from "@/lib/site";

const entryPoints = [
  {
    number: "01",
    title: "Browse the vocabulary",
    text: "Search every public class and relation generated from the OntoUML exchange model.",
    href: "/model/reference/",
    label: "Open the term reference",
  },
  {
    number: "02",
    title: "Trace the foundations",
    text: "View the three previously published journey diagrams that situate the educational lineage of the project.",
    href: "/foundations/",
    label: "View conceptual foundations",
  },
  {
    number: "03",
    title: "Reuse the release",
    text: "Download Tonto, OntoUML JSON, RDF serializations, SHACL shapes, tests, checksums, and citation metadata.",
    href: "/resources/",
    label: "Open resources",
  },
];

export default function Home() {
  return (
    <main id="main-content">
      <section className="hero">
        <div className="site-container hero__grid">
          <div className="hero__copy">
            <p className="eyebrow">OntoJourney {RELEASE_LABEL}</p>
            <h1 className="display-title">
              A public ontology for narrative-heroic learning journeys.
            </h1>
            <p className="lead">
              Explore a UFO-grounded OntoUML vocabulary, inspect its technical
              validation, and reuse versioned machine-readable artifacts.
            </p>
            <div className="button-row">
              <Link className="button button--primary" href="/model/reference/">
                Explore 67 terms <span aria-hidden="true">→</span>
              </Link>
              <a
                className="button button--secondary"
                href={VERSION_DOI}
              >
                Open citation record <span aria-hidden="true">↗</span>
              </a>
              <a
                className="button button--secondary"
                href={assetUrl("/artifacts/0.9.2/ontojourney-core-v0.9.2.zip")}
                download
              >
                Download v0.9.2 <span aria-hidden="true">↓</span>
              </a>
            </div>
          </div>
          <div className="hero__art" aria-hidden="true">
            <Image
              className="hero__image"
              src={assetUrl("/images/journey-spiral-transparent.webp")}
              alt=""
              width={1800}
              height={1600}
              priority
              unoptimized
              sizes="(max-width: 900px) 100vw, 50vw"
            />
          </div>
        </div>
        <ValidationStrip />
      </section>

      <section className="section" aria-labelledby="entry-title">
        <div className="site-container">
          <div className="section-heading">
            <div>
              <p className="eyebrow">Start here</p>
              <h2 className="section-title" id="entry-title">
                Documentation, provenance, and reusable data.
              </h2>
            </div>
            <p className="lead">
              The public release keeps its conceptual source, exchange model,
              Web serializations, validation records, and documentation under
              explicit version and licensing policies.
            </p>
          </div>
          <div className="card-grid">
            {entryPoints.map((item) => (
              <article className="card" key={item.number}>
                <span className="card__number">{item.number}</span>
                <h3 className="card-title">{item.title}</h3>
                <p>{item.text}</p>
                <Link className="card__link" href={item.href}>
                  {item.label} <span aria-hidden="true">→</span>
                </Link>
              </article>
            ))}
          </div>
        </div>
      </section>

      <section className="section section--tinted" aria-labelledby="lineage-title">
        <div className="site-container split">
          <div className="foundation-preview">
            <Image
              src={assetUrl("/foundations/heroines-learning-journey.jpg")}
              alt="The twelve-stage Heroine's Learning Journey diagram"
              width={1073}
              height={788}
              unoptimized
              sizes="(max-width: 900px) 100vw, 50vw"
            />
          </div>
          <div>
            <p className="eyebrow">Published lineage</p>
            <h2 className="section-title" id="lineage-title">
              From heroic patterns to an educational journey.
            </h2>
            <p className="lead">
              Campbell, Murdock, and the Heroine&apos;s Learning Journey are
              presented as previously published conceptual foundations. Their
              diagrams are contextual illustrations, not formal OntoJourney
              model diagrams.
            </p>
            <Link className="button button--primary" href="/foundations/">
              Compare the three journeys <span aria-hidden="true">→</span>
            </Link>
          </div>
        </div>
      </section>

      <section className="stat-grid" aria-label="OntoJourney Core v0.9.2 statistics">
        <div className="stat"><strong>40</strong><span>Domain classes</span></div>
        <div className="stat"><strong>27</strong><span>Relations</span></div>
        <div className="stat"><strong>34</strong><span>Generalizations</span></div>
        <div className="stat"><strong>370</strong><span>Published RDF triples</span></div>
      </section>

      <section className="section" aria-labelledby="release-title">
        <div className="site-container split">
          <div>
            <p className="eyebrow">Current public release</p>
            <h2 className="section-title" id="release-title">
              OntoJourney Core v0.9.2
            </h2>
          </div>
          <div>
            <p className="lead">
              The release passed the planned source, structural, RDF, SHACL,
              local OntoUML verification, and HermiT checks. The version DOI identifies the
              exact archived package, while the Zenodo concept DOI identifies
              the project collection.
            </p>
            <div className="button-row">
              <Link className="button button--primary" href="/validation/">
                Review validation <span aria-hidden="true">→</span>
              </Link>
              <Link className="button button--secondary" href="/releases/0.9.2/">
                Release notes
              </Link>
              <a className="button button--secondary" href={CONCEPT_DOI}>
                Open Zenodo collection <span aria-hidden="true">↗</span>
              </a>
            </div>
          </div>
        </div>
      </section>
    </main>
  );
}
