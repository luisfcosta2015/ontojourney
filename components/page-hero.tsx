type PageHeroProps = {
  eyebrow: string;
  title: string;
  lead: string;
};

export function PageHero({ eyebrow, title, lead }: PageHeroProps) {
  return (
    <header className="page-hero">
      <div className="site-container page-hero__grid">
        <div>
          <p className="eyebrow">{eyebrow}</p>
          <h1 className="page-title">{title}</h1>
        </div>
        <p className="lead">{lead}</p>
      </div>
    </header>
  );
}
