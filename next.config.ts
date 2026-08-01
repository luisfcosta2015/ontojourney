import type { NextConfig } from "next";

const isGitHubPages = process.env.GITHUB_PAGES === "true";
const basePath = isGitHubPages ? "/ontojourney" : "";

const nextConfig: NextConfig = {
  ...(isGitHubPages ? { output: "export" } : {}),
  ...(isGitHubPages ? { typescript: { tsconfigPath: "tsconfig.pages.json" } } : {}),
  basePath,
  assetPrefix: basePath || undefined,
  trailingSlash: true,
  images: { unoptimized: true },
};

export default nextConfig;
