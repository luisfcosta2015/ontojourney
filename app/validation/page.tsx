import type { Metadata } from "next";

import { PageHero } from "@/components/page-hero";
import { assetUrl } from "@/lib/site";

export const metadata: Metadata = {
  title: "Validation",
  description:
    "Technical validation records for OntoJourney Core v0.9.0 across source, structure, RDF, SHACL, the OntoUML API, and HermiT.",
};

const checks = [
  ["Tonto source", "Local CLI validation", "Passed", "31 Jul 2026"],
  ["OntoUML JSON", "Structural audit: 40 classes, 27 relations, 33 generalizations", "Passed", "31 Jul 2026"],
  ["gUFO / RDF", "Turtle parse and structural audit: 326 triples", "Passed", "1 Aug 2026"],
  ["SHACL", "One conforming fixture and two deliberately invalid fixtures", "Passed", "31 Jul 2026"],
  ["OntoUML API", "HTTP 200; no reported violations", "Passed", "31 Jul 2026"],
  ["Protégé / HermiT", "Classification completed; no unsatisfiable OntoJourney classes", "Passed", "1 Aug 2026"],
];

const evidence = [
  ["Source validation", "Confirms that the canonical Tonto source is accepted by the local validation tool."],
  ["Structural audit", "Confirms expected counts, references, endpoints, and generation integrity in the OntoUML JSON."],
  ["RDF parsing", "Confirms that the public Turtle serialization parses and exposes the expected graph structure."],
  ["SHACL fixtures", "Confirms that the published shapes accept the conforming fixture and reject the intended invalid fixtures."],
  ["Remote verification", "Records the official OntoUML API response for the submitted model hash."],
  ["Logical classification", "Records the Protégé/HermiT result for the imported gUFO-aligned ontology."],
];

export default function ValidationPage() {
  return (
    <main id="main-content">
      <PageHero
        eyebrow="Validation"
        title="Six checks, with evidence and explicit limits."
        lead="The release separates source validation, structural auditing, RDF parsing, constraint behavior, remote model verification, and logical classification. Each check addresses a different technical question."
      />

      <section className="section" aria-labelledby="status-title">
        <div className="site-container">
          <div className="section-heading">
            <div>
              <p className="eyebrow">Release status</p>
              <h2 className="section-title" id="status-title">
                All planned v0.9.0 technical gates passed.
              </h2>
            </div>
            <p>
              The OntoUML API record is tied to SHA-256
              <code>7830fc94d0741517bbb415094ed3ff08204a166419b92627b4aa300192f6e18a</code>
              of the submitted OntoUML JSON.
            </p>
          </div>
          <div className="data-table-wrap">
            <table className="data-table">
              <thead><tr><th>Layer</th><th>Evidence</th><th>Result</th><th>Date</th></tr></thead>
              <tbody>
                {checks.map(([layer, detail, result, date]) => (
                  <tr key={layer}>
                    <td><strong>{layer}</strong></td>
                    <td>{detail}</td>
                    <td className="result-pass">{result}</td>
                    <td>{date}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          <div className="button-row" style={{ marginTop: "1.5rem" }}>
            <a className="button button--primary" href={assetUrl("/artifacts/0.9.0/VALIDATION_REPORT.md")}>Open validation report <span aria-hidden="true">→</span></a>
            <a className="button button--secondary" href={assetUrl("/artifacts/0.9.0/validation/ontouml-api-response-v0.9.json")}>Raw API response</a>
          </div>
        </div>
      </section>

      <section className="section section--tinted" aria-labelledby="meaning-title">
        <div className="site-container">
          <div className="section-heading">
            <div>
              <p className="eyebrow">Interpretation</p>
              <h2 className="section-title" id="meaning-title">
                What the evidence establishes.
              </h2>
            </div>
            <p>
              Passing these checks establishes reproducible technical behavior
              for this release. It does not replace domain review or guarantee
              that every future extension will remain compatible.
            </p>
          </div>
          <div className="card-grid">
            {evidence.map(([title, text], index) => (
              <article className="card" key={title}>
                <span className="card__number">{String(index + 1).padStart(2, "0")}</span>
                <h3 className="card-title">{title}</h3>
                <p>{text}</p>
              </article>
            ))}
          </div>
        </div>
      </section>

      <section className="section" aria-labelledby="reproduce-title">
        <div className="site-container split">
          <div>
            <p className="eyebrow">Reproducibility</p>
            <h2 className="section-title" id="reproduce-title">Run the packaged checks locally.</h2>
          </div>
          <div className="prose">
            <pre><code>{`python3 -m venv .venv
.venv/bin/pip install -r ontology/requirements-validation.txt
.venv/bin/python ontology/tests/audit_generated_json.py
.venv/bin/python ontology/tests/run_shacl_tests.py`}</code></pre>
            <p>
              The two invalid SHACL fixtures are expected to report
              <code>conforms=False</code>; rejection is their passing outcome.
            </p>
          </div>
        </div>
      </section>
    </main>
  );
}
