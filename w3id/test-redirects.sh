#!/usr/bin/env bash
set -euo pipefail

base="https://w3id.org/ontojourney/core"

curl -fsSI -H "Accept: text/html" "$base"
curl -fsSI -H "Accept: text/turtle" "$base"
curl -fsSI -H "Accept: application/rdf+xml" "$base"
curl -fsSI -H "Accept: application/ld+json" "$base"
curl -fsSI -H "Accept: application/n-triples" "$base"
curl -fsSI -H "Accept: text/html" "$base/0.9"
