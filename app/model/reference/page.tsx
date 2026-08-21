import type { Metadata } from "next";
import Link from "next/link";

import { PageHero } from "@/components/page-hero";
import { TermExplorer } from "@/components/term-explorer";
import { ENTITY_NAMESPACE } from "@/lib/site";

export const metadata: Metadata = {
  title: "Term reference",
  description:
    "Search the 40 classes and 27 relations in OntoJourney Core v0.9.1, with class definitions, OntoUML stereotypes, generalizations, endpoints, cardinalities, and canonical IRIs.",
};

export default function ReferencePage() {
  return (
    <main id="main-content">
      <PageHero
        eyebrow="Model reference"
        title="Forty classes. Twenty-seven relations. One stable namespace."
        lead="This public reference is generated from the versioned OntoUML JSON. It exposes every domain class and relation, including the 40 canonical class definitions, without maintaining a separate hand-written index."
      />
      <section className="section">
        <div className="site-container">
          <div className="section-heading">
            <div>
              <p className="eyebrow">Term explorer</p>
              <h2 className="section-title">Search the core vocabulary.</h2>
            </div>
            <div>
              <p>
                Entity IRIs use <code>{ENTITY_NAMESPACE}</code>. Class cards
                show the canonical English definition, OntoUML stereotype, and
                immediate parent; relation cards identify endpoints and
                cardinalities.
              </p>
              <p>
                For release structure and reuse guidance, read the
                <Link href="/documentation/"> public documentation</Link>
                together with this generated reference.
              </p>
            </div>
          </div>
          <TermExplorer />
        </div>
      </section>
    </main>
  );
}
