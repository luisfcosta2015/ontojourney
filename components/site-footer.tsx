import Image from "next/image";
import Link from "next/link";

import { CANONICAL_IRI, REPOSITORY_URL, assetUrl } from "@/lib/site";

export function SiteFooter() {
  return (
    <footer className="site-footer">
      <div className="site-container">
        <div className="site-footer__grid">
          <div className="site-footer__about">
            <Link className="brand" href="/">
              <span className="brand-mark" aria-hidden="true" />
              OntoJourney
            </Link>
            <p>
              A public UFO-grounded OntoUML vocabulary with versioned source,
              serializations, constraints, validation evidence, and citation metadata.
            </p>
            <div className="initiative-mark">
              <span>A Heroic Journeys research initiative</span>
              <Image
                src={assetUrl("/brand/heroic-journeys-logo.png")}
                alt="Heroic Journeys"
                width={650}
                height={430}
                unoptimized
              />
            </div>
          </div>
          <div className="footer-links">
            <h2>Explore</h2>
            <ul>
              <li><Link href="/documentation/">Documentation</Link></li>
              <li><Link href="/model/">Model overview</Link></li>
              <li><Link href="/model/reference/">Term reference</Link></li>
              <li><Link href="/foundations/">Conceptual foundations</Link></li>
              <li><Link href="/validation/">Validation evidence</Link></li>
            </ul>
          </div>
          <div className="footer-links">
            <h2>Reuse</h2>
            <ul>
              <li><Link href="/resources/">Downloads and citation</Link></li>
              <li><a href={CANONICAL_IRI}>Persistent IRI</a></li>
              <li><a href={REPOSITORY_URL}>GitHub repository</a></li>
              <li><a href={`${REPOSITORY_URL}/issues`}>Report an issue</a></li>
              <li><a href={assetUrl("/ASSET-LICENSES.md")}>Asset licenses</a></li>
            </ul>
          </div>
        </div>
        <div className="footer-bottom">
          OntoJourney Core v0.9.0 · Ontology and documentation CC BY 4.0,
          except separately identified visual assets · Maintained by Luis Felipe Coimbra Costa
        </div>
      </div>
    </footer>
  );
}
