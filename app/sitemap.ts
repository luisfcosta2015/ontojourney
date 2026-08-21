import type { MetadataRoute } from "next";

import { SITE_URL } from "@/lib/site";

export const dynamic = "force-static";

export default function sitemap(): MetadataRoute.Sitemap {
  const routes = [
    "",
    "documentation/",
    "model/",
    "model/reference/",
    "foundations/",
    "validation/",
    "resources/",
    "releases/0.9.0/",
    "releases/0.9.1/",
  ];

  return routes.map((route) => ({
    url: `${SITE_URL}${route}`,
    lastModified: new Date(route === "releases/0.9.0/" ? "2026-08-01" : "2026-08-21"),
    changeFrequency: route ? "monthly" : "weekly",
    priority: route ? 0.8 : 1,
  }));
}
