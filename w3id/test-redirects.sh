#!/usr/bin/env bash
set -euo pipefail

base="${ONTOJOURNEY_W3ID_BASE:-https://w3id.org/ontojourney/core}"
site="https://luisfcosta2015.github.io/ontojourney"

assert_redirect() {
  local accept="$1"
  local url="$2"
  local expected="$3"
  local location

  location="$({ curl -fsSI -H "Accept: ${accept}" "${url}" || true; } \
    | awk 'BEGIN { IGNORECASE=1 } /^location:/ { sub(/^[^:]+:[[:space:]]*/, ""); sub(/\r$/, ""); print; exit }')"
  if [[ "${location}" != "${expected}" ]]; then
    echo "Unexpected redirect for ${url} (${accept})" >&2
    echo "Expected: ${expected}" >&2
    echo "Found:    ${location:-<none>}" >&2
    exit 1
  fi
}

# Current unversioned route and v0.9.1 route.
for suffix in "" "/0.9.1"; do
  if [[ -n "${suffix}" ]]; then
    expected_html="${site}/releases/0.9.1/"
  else
    expected_html="${site}/model/"
  fi
  assert_redirect "text/html" "${base}${suffix}" "${expected_html}"
  assert_redirect "text/turtle" "${base}${suffix}" "${site}/artifacts/0.9.1/ontojourney-core.ttl"
  assert_redirect "application/rdf+xml" "${base}${suffix}" "${site}/artifacts/0.9.1/ontojourney-core.rdf"
  assert_redirect "application/ld+json" "${base}${suffix}" "${site}/artifacts/0.9.1/ontojourney-core.jsonld"
  assert_redirect "application/n-triples" "${base}${suffix}" "${site}/artifacts/0.9.1/ontojourney-core.nt"
done

# Historical v0.9 remains immutable.
assert_redirect "text/html" "${base}/0.9" "${site}/releases/0.9.0/"
assert_redirect "text/turtle" "${base}/0.9" "${site}/artifacts/0.9.0/ontojourney-core.ttl"

echo "OntoJourney W3ID redirects match the v0.9.1 publication policy."
