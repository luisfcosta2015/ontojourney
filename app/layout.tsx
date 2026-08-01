import type { Metadata } from "next";
import "@fontsource-variable/inter";
import "@fontsource/cormorant-garamond/500.css";
import "@fontsource/cormorant-garamond/600.css";
import "./globals.css";

import { SiteFooter } from "@/components/site-footer";
import { SiteHeader } from "@/components/site-header";
import { SITE_DESCRIPTION, SITE_NAME, SITE_URL, assetUrl } from "@/lib/site";

export const metadata: Metadata = {
  metadataBase: new URL(SITE_URL),
  title: {
    default: `${SITE_NAME} | Ontology of narrative-heroic learning journeys`,
    template: `%s | ${SITE_NAME}`,
  },
  description: SITE_DESCRIPTION,
  authors: [{ name: "Luis Felipe Coimbra Costa" }],
  creator: "Luis Felipe Coimbra Costa",
  publisher: "OntoJourney Project",
  keywords: [
    "ontology",
    "OntoUML",
    "UFO",
    "learning journey",
    "heroic narrative",
    "Heroine's Learning Journey",
    "Heroic Journeys",
    "SHACL",
  ],
  alternates: { canonical: SITE_URL },
  openGraph: {
    type: "website",
    locale: "en_US",
    url: SITE_URL,
    siteName: SITE_NAME,
    title: `${SITE_NAME}: an ontology for narrative-heroic learning journeys`,
    description: SITE_DESCRIPTION,
    images: [
      {
        url: assetUrl("/images/social-card.png"),
        width: 1440,
        height: 900,
        alt: "OntoJourney abstract journey map",
      },
    ],
  },
  icons: {
    icon: assetUrl("/favicon.svg"),
    shortcut: assetUrl("/favicon.svg"),
  },
  manifest: assetUrl("/site.webmanifest"),
};

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en">
      <body>
        <a className="skip-link" href="#main-content">
          Skip to content
        </a>
        <SiteHeader />
        {children}
        <SiteFooter />
      </body>
    </html>
  );
}
