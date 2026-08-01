# W3ID submission checklist

The publication files are prepared, but the canonical redirects become active
only after a pull request is accepted in `perma-id/w3id.org`.

1. Confirm that GitHub Pages is live and every target in `w3id/.htaccess`
   returns HTTP 200.
2. Fork <https://github.com/perma-id/w3id.org>.
3. Copy the local `w3id/` directory to `ontojourney/` in that fork. Include
   `.htaccess` and `README.md`; the local test script may remain in the project
   repository rather than the W3ID pull request.
4. Open a pull request titled `Add OntoJourney persistent identifiers`.
5. In the pull request, identify Luis Felipe Coimbra Costa as maintainer and
   link the ontology repository and documentation site.
6. After approval, run `w3id/test-redirects.sh` and record the result in the
   release notes.

The `ontojourney` directory name was not present in the W3ID repository when
the publication package was prepared on 1 August 2026. Availability is not a
reservation; it must be checked again immediately before opening the pull
request.
