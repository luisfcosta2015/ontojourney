export const SITE_NAME = "OntoJourney";
export const SITE_URL = "https://luisfcosta2015.github.io/ontojourney/";
export const REPOSITORY_URL = "https://github.com/luisfcosta2015/ontojourney";
export const VERSION = "0.9.1";
export const RELEASE_LABEL = `Core v${VERSION}`;
export const CANONICAL_IRI = "https://w3id.org/ontojourney/core";
export const ENTITY_NAMESPACE = `${CANONICAL_IRI}#`;
export const VERSION_IRI = `${CANONICAL_IRI}/${VERSION}`;
export const VERSION_DOI = "https://doi.org/10.5281/zenodo.22043806";
export const CONCEPT_DOI = "https://doi.org/10.5281/zenodo.21802020";
export const SITE_DESCRIPTION =
  "OntoJourney is a public UFO-grounded OntoUML ontology for narrative-heroic learning journeys, published with versioned source, serializations, constraints, and validation evidence.";

export const BASE_PATH = process.env.NEXT_PUBLIC_BASE_PATH ?? "";

export function assetUrl(path: string): string {
  const normalized = path.startsWith("/") ? path : `/${path}`;
  return `${BASE_PATH}${normalized}`;
}
