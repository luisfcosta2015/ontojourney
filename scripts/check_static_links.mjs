import { existsSync, readFileSync, readdirSync, statSync } from "node:fs";
import { dirname, join, resolve } from "node:path";

const root = resolve(import.meta.dirname, "../out");
const basePath = "/ontojourney";
const htmlFiles = [];

function walk(directory) {
  for (const name of readdirSync(directory)) {
    const path = join(directory, name);
    if (statSync(path).isDirectory()) walk(path);
    else if (path.endsWith(".html")) htmlFiles.push(path);
  }
}

function targetExists(value, source) {
  const clean = value.split("#")[0].split("?")[0];
  if (!clean || /^(https?:|mailto:|data:|tel:|javascript:)/.test(clean)) return true;
  let relative;
  if (clean.startsWith(basePath)) relative = clean.slice(basePath.length);
  else if (clean.startsWith("/")) return true;
  else relative = resolve(dirname(source), clean).slice(root.length);
  const normalized = relative.replace(/^\/+/, "");
  const direct = join(root, normalized);
  return (
    existsSync(direct) ||
    existsSync(`${direct}.html`) ||
    existsSync(join(direct, "index.html"))
  );
}

if (!existsSync(root)) throw new Error("Static export directory out/ does not exist.");
walk(root);
const failures = [];
const attributePattern = /(?:href|src)=["']([^"']+)["']/g;

for (const file of htmlFiles) {
  const html = readFileSync(file, "utf8");
  for (const match of html.matchAll(attributePattern)) {
    if (!targetExists(match[1], file)) {
      failures.push(`${file.slice(root.length + 1)} -> ${match[1]}`);
    }
  }
}

if (failures.length) {
  console.error("Broken internal links or assets:\n" + failures.join("\n"));
  process.exit(1);
}

console.log(`Checked ${htmlFiles.length} static HTML files; no broken internal links found.`);
