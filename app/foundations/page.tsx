import type { Metadata } from "next";
import Image from "next/image";

import { PageHero } from "@/components/page-hero";
import { assetUrl } from "@/lib/site";

export const metadata: Metadata = {
  title: "Conceptual foundations",
  description:
    "Visual lineage of OntoJourney through previously published diagrams by Campbell, Murdock, and the HLJ project.",
};

const sourceTitle =
  "Heroine's Learning Journey: Motivating Women in STEM Online Courses Through the Power of a Narrative";

export default function FoundationsPage() {
  return (
    <main id="main-content">
      <PageHero
        eyebrow="Conceptual foundations"
        title="Three published journey structures, shown in sequence."
        lead="These diagrams situate the educational lineage of the project. They were previously published in the 2024 HLJ article and are reproduced unchanged here; they are not formal diagrams of OntoJourney Core."
      />

      <section className="section" aria-labelledby="campbell-title">
        <div className="site-container foundation-section">
          <div className="foundation-copy">
            <p className="eyebrow">Narrative foundation</p>
            <h2 className="section-title" id="campbell-title">Campbell&apos;s Hero&apos;s Journey</h2>
            <p>
              The diagram presents seventeen stages organized across departure,
              initiation, and return. It is included as a previously published
              historical foundation for comparison.
            </p>
          </div>
          <figure className="foundation-figure">
            <Image
              src={assetUrl("/foundations/campbell-hero-journey.jpg")}
              alt="Campbell's seventeen-stage Hero's Journey arranged in three acts"
              width={1196}
              height={812}
              unoptimized
              sizes="(max-width: 1280px) 100vw, 1100px"
            />
            <figcaption>
              Campbell&apos;s Hero&apos;s Journey. Previously published in Costa et al. (2024), Fig. 1(a).
            </figcaption>
          </figure>
        </div>
      </section>

      <section className="section section--tinted" aria-labelledby="murdock-title">
        <div className="site-container foundation-section">
          <div className="foundation-copy">
            <p className="eyebrow">Gender-aware foundation</p>
            <h2 className="section-title" id="murdock-title">Murdock&apos;s Heroine&apos;s Journey</h2>
            <p>
              The circular diagram presents ten stages and foregrounds a
              distinct account of development, healing, and integration.
            </p>
          </div>
          <figure className="foundation-figure">
            <Image
              src={assetUrl("/foundations/murdock-heroine-journey.jpg")}
              alt="Murdock's ten-stage Heroine's Journey arranged as a cycle"
              width={1196}
              height={812}
              unoptimized
              sizes="(max-width: 1280px) 100vw, 1100px"
            />
            <figcaption>
              Murdock&apos;s Heroine&apos;s Journey. Previously published in Costa et al. (2024), Fig. 1(b).
            </figcaption>
          </figure>
        </div>
      </section>

      <section className="section" aria-labelledby="hlj-title">
        <div className="site-container foundation-section">
          <div className="foundation-copy">
            <p className="eyebrow">Educational specialization</p>
            <h2 className="section-title" id="hlj-title">Heroine&apos;s Learning Journey</h2>
            <p>
              The HLJ diagram organizes twelve stages in three educational acts:
              empowerment, growth, and return.
            </p>
          </div>
          <figure className="foundation-figure">
            <Image
              src={assetUrl("/foundations/heroines-learning-journey.jpg")}
              alt="The twelve-stage Heroine's Learning Journey arranged in three educational acts"
              width={1073}
              height={788}
              unoptimized
              sizes="(max-width: 1280px) 100vw, 1100px"
            />
            <figcaption>
              Heroine&apos;s Learning Journey. Previously published in Costa et al. (2024), Fig. 2.
            </figcaption>
          </figure>
        </div>
      </section>

      <section className="section section--tinted" aria-labelledby="source-title">
        <div className="site-container split">
          <div>
            <p className="eyebrow">Source and license</p>
            <h2 className="section-title" id="source-title">Reproduced unchanged with attribution.</h2>
          </div>
          <div>
            <p>
              Costa, L. F. C. et al. (2024). <em>{sourceTitle}</em>. IEEE Access,
              12, 20103-20124. <a href="https://doi.org/10.1109/ACCESS.2024.3360376">https://doi.org/10.1109/ACCESS.2024.3360376</a>.
            </p>
            <p>
              The three image files are reproduced unchanged under
              <a href="https://creativecommons.org/licenses/by-nc-nd/4.0/"> CC BY-NC-ND 4.0</a>
              and are excluded from the repository&apos;s general CC BY 4.0 license.
              See <a href={assetUrl("/ASSET-LICENSES.md")}>asset licensing details</a>.
            </p>
          </div>
        </div>
      </section>
    </main>
  );
}
