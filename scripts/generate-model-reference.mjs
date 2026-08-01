import { readFileSync, writeFileSync } from "node:fs";
import { resolve } from "node:path";

const root = resolve(import.meta.dirname, "..");
const sourcePath = resolve(root, "ontology/generated/OntoJourneyCore.json");
const outputPath = resolve(root, "lib/model-reference.json");
const project = JSON.parse(readFileSync(sourcePath, "utf8"));
const contents = project.model.contents.flatMap((pkg) => pkg.contents ?? []);
const byId = new Map(contents.filter((item) => item.id).map((item) => [item.id, item]));
const excludedDatatypes = new Set([
  "number",
  "string",
  "boolean",
  "date",
  "time",
  "datetime",
  "undefined",
]);

const parentNames = new Map();
for (const item of contents.filter((item) => item.type === "Generalization")) {
  const specific = byId.get(item.specific?.id)?.name;
  const general = byId.get(item.general?.id)?.name;
  if (!specific || !general) continue;
  parentNames.set(specific, [...(parentNames.get(specific) ?? []), general]);
}

const terms = [];
for (const item of contents) {
  if (item.type === "Class" && item.name && !excludedDatatypes.has(item.name)) {
    const parents = parentNames.get(item.name) ?? [];
    terms.push({
      name: item.name,
      kind: "class",
      stereotype: item.stereotype || "class",
      detail: parents.length
        ? `Specializes ${parents.join(" and ")}.`
        : "Top-level type in the OntoJourney domain model.",
      iri: `https://w3id.org/ontojourney/core#${item.name}`,
    });
  }

  if (item.type === "Relation" && item.name) {
    const ends = (item.properties ?? []).map((property) => ({
      name: byId.get(property.propertyType?.id)?.name ?? "Unknown",
      cardinality: property.cardinality ?? "",
    }));
    const [source, target] = ends;
    terms.push({
      name: item.name,
      kind: "relation",
      stereotype: item.stereotype || "relation",
      detail:
        source && target
          ? `${source.name} [${source.cardinality}] → ${target.name} [${target.cardinality}].`
          : "Relation in the OntoJourney domain model.",
      iri: `https://w3id.org/ontojourney/core#${item.name}`,
    });
  }
}

terms.sort((a, b) => a.name.localeCompare(b.name));
const output = `${JSON.stringify(terms, null, 2)}\n`;

if (process.argv.includes("--check")) {
  const current = readFileSync(outputPath, "utf8");
  if (current !== output) {
    console.error("lib/model-reference.json is out of date. Run npm run generate:model.");
    process.exit(1);
  }
  console.log(`Model reference is current (${terms.length} terms).`);
} else {
  writeFileSync(outputPath, output, "utf8");
  console.log(`Wrote ${terms.length} terms to lib/model-reference.json.`);
}
