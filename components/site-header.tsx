import Link from "next/link";

const navigation = [
  { href: "/documentation/", label: "Documentation" },
  { href: "/model/", label: "Model" },
  { href: "/foundations/", label: "Foundations" },
  { href: "/validation/", label: "Validation" },
  { href: "/resources/", label: "Resources" },
];

export function SiteHeader() {
  return (
    <header className="site-header">
      <div className="site-container site-header__inner">
        <Link className="brand" href="/" aria-label="OntoJourney home">
          <span className="brand-mark" aria-hidden="true" />
          OntoJourney
        </Link>
        <nav className="desktop-nav" aria-label="Primary navigation">
          {navigation.map((item) => (
            <Link key={item.href} href={item.href}>
              {item.label}
            </Link>
          ))}
        </nav>
        <details className="mobile-menu">
          <summary>Menu</summary>
          <nav className="mobile-nav" aria-label="Mobile navigation">
            {navigation.map((item) => (
              <Link key={item.href} href={item.href}>
                {item.label}
              </Link>
            ))}
          </nav>
        </details>
      </div>
    </header>
  );
}
