const checks = ["Tonto", "OntoUML API", "SHACL", "HermiT"];

export function ValidationStrip() {
  return (
    <aside className="validation-strip" aria-label="Validation status">
      <div className="site-container validation-strip__inner">
        <span className="validation-strip__label">Validated with</span>
        {checks.map((check) => (
          <span className="status-chip" key={check}>{check}</span>
        ))}
      </div>
    </aside>
  );
}
