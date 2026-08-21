"use client";

import { useMemo, useState } from "react";

import terms from "@/lib/model-reference.json";

type Filter = "all" | "class" | "relation";

export function TermExplorer() {
  const [query, setQuery] = useState("");
  const [filter, setFilter] = useState<Filter>("all");

  const visible = useMemo(() => {
    const normalized = query.trim().toLowerCase();
    return terms.filter((term) => {
      const matchesFilter = filter === "all" || term.kind === filter;
      const matchesQuery =
        !normalized ||
        term.name.toLowerCase().includes(normalized) ||
        term.stereotype.toLowerCase().includes(normalized) ||
        term.definition.toLowerCase().includes(normalized) ||
        term.detail.toLowerCase().includes(normalized);
      return matchesFilter && matchesQuery;
    });
  }, [filter, query]);

  return (
    <div className="term-explorer">
      <div className="term-controls">
        <label className="sr-only" htmlFor="term-search">Search ontology terms</label>
        <input
          className="search-input"
          id="term-search"
          onChange={(event) => setQuery(event.target.value)}
          placeholder="Search by term, definition, stereotype, or endpoint…"
          type="search"
          value={query}
        />
        {(["all", "class", "relation"] as Filter[]).map((option) => (
          <button
            aria-pressed={filter === option}
            className="filter-button"
            key={option}
            onClick={() => setFilter(option)}
            type="button"
          >
            {option === "all" ? "All terms" : option === "class" ? "Classes" : "Relations"}
          </button>
        ))}
      </div>
      <p className="term-count" role="status">
        Showing {visible.length} of {terms.length} terms
      </p>
      <div className="term-grid">
        {visible.map((term) => (
          <article className="term-card" key={term.name}>
            <div className="term-card__top">
              <h3>{term.name}</h3>
              <span className="term-type">{term.stereotype}</span>
            </div>
            {term.definition ? <p className="term-definition">{term.definition}</p> : null}
            <p className="term-detail">{term.detail}</p>
            <a className="card__link" href={term.iri}>
              Canonical IRI <span aria-hidden="true">↗</span>
            </a>
          </article>
        ))}
      </div>
      {visible.length === 0 ? (
        <div className="callout" role="status">
          No ontology term matches this search.
        </div>
      ) : null}
    </div>
  );
}
