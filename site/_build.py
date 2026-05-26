#!/usr/bin/env python3
"""
Split wireframes.html (SPA) into a multi-page static site.

Reads:   /Users/haimac/buzzer/wireframes.html
Writes:  /Users/haimac/buzzer/site/*.html + assets/ + client/ + advocate/
"""

from __future__ import annotations

import os
import re
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
ROOT = Path("/Users/haimac/buzzer")
SRC = ROOT / "wireframes.html"
OUT = ROOT / "site"
ASSETS = OUT / "assets"
CLIENT = OUT / "client"
ADVOCATE = OUT / "advocate"

for d in (OUT, ASSETS, CLIENT, ADVOCATE):
    d.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# Screen → output file path mapping
# ---------------------------------------------------------------------------
SCREEN_MAP = {
    "s-home":             ("index.html",                       "Homepage"),
    "s-howto-client":     ("how-it-works-client.html",         "How it Works — Client"),
    "s-howto-advocate":   ("how-it-works-advocate.html",       "How it Works — Advocate"),
    "s-solutions":        ("solutions.html",                   "Solusi per Industri"),
    "s-about":            ("about.html",                       "Tentang"),
    "s-trust":            ("trust.html",                       "Trust & Safety"),
    "s-faq":              ("faq.html",                         "FAQ / Pusat Bantuan"),
    "s-contact":          ("contact.html",                     "Kontak / Demo"),
    "s-pricing":          ("pricing.html",                     "Harga"),
    "s-film":             ("film.html",                        "Film"),
    "s-politik":          ("politik.html",                     "Politik"),
    "s-browse":           ("browse.html",                      "Browse Advocates"),
    "s-design-system":    ("design-system.html",               "Design System"),
    "s-client-home":      ("client/dashboard.html",            "Dashboard"),
    "s-brief":            ("client/brief.html",                "Buat Brief"),
    "s-campaigns-list":   ("client/campaigns.html",            "Kampanye"),
    "s-shortlist":        ("client/shortlist.html",            "Shortlist Advocate"),
    "s-advocate-detail":  ("client/advocate-detail.html",      "Advocate Detail"),
    "s-approval":         ("client/approval.html",             "Content Approval"),
    "s-dashboard":        ("client/live-campaign.html",        "Live Campaign"),
    "s-library":          ("client/library.html",              "Advocate Library"),
    "s-analytics":        ("client/analytics.html",            "Analytics"),
    "s-billing":          ("client/billing.html",              "Billing & Invoices"),
    "s-settings":         ("client/settings.html",             "Settings"),
    "s-onboard":          ("advocate/onboarding.html",         "Advocate Onboarding"),
    "s-mobile":           ("advocate/mobile.html",             "Advocate Mobile"),
    "s-adv-profile":      ("advocate/profile.html",            "Profil Advocate"),
    "s-adv-campaigns":    ("advocate/campaigns.html",          "Kampanye Saya"),
    "s-adv-inbox":        ("advocate/inbox.html",              "Inbox"),
    "s-adv-verification": ("advocate/verification.html",       "Verifikasi"),
}

# Web-nav item text → target file name (root-relative)
NAV_ROUTES = {
    "Cara Kerja":     "how-it-works-client.html",
    "Untuk Advocate": "how-it-works-advocate.html",
    "Untuk Client":   "how-it-works-client.html",
    "Solusi":         "solutions.html",
    "Harga":          "pricing.html",
    "Tentang":        "about.html",
    "Trust & Safety": "trust.html",
    "Bantuan":        "faq.html",
    "FAQ":            "faq.html",
    "Kontak":         "contact.html",
    "Film":           "film.html",
    "Politik":        "politik.html",
    "Brand":          "solutions.html",
    "NGO":            "solutions.html",
    "Studi Kasus":    "solutions.html",
}

# Footer text → target file (root-relative)
FOOTER_ROUTES = {
    "Cara Kerja (Client)":   "how-it-works-client.html",
    "Cara Kerja (Advocate)": "how-it-works-advocate.html",
    "Solusi per Industri":   "solutions.html",
    "Solusi":                "solutions.html",
    "Harga":                 "pricing.html",
    "Trust & Safety":        "trust.html",
    "FAQ":                   "faq.html",
    "Pusat Bantuan":         "faq.html",
    "Studi Kasus":           "solutions.html",
    "Tentang Kami":          "about.html",
    "Tentang":               "about.html",
    "Kontak / Demo":         "contact.html",
    "Kontak":                "contact.html",
    "Film & Hiburan":        "film.html",
    "Film":                  "film.html",
    "Komunikasi Politik":    "politik.html",
    "Politik":               "politik.html",
    "Brand & FMCG":          "solutions.html",
    "NGO & Lembaga":         "solutions.html",
    "NGO":                   "solutions.html",
    "Kementerian/Pemda":     "solutions.html",
    "Pemerintah":            "solutions.html",
    "Pelatihan Advocate":    "advocate/onboarding.html",
    "Blog Insight":          "faq.html",
    "Blog":                  "faq.html",
}

# Sidebar nav-item text (client dashboard) → root-relative path
CLIENT_SIDEBAR_ROUTES = {
    "Home":             "client/dashboard.html",
    "Buat Brief":       "client/brief.html",
    "Kampanye":         "client/campaigns.html",
    "Advocate Library": "client/library.html",
    "Analytics":        "client/analytics.html",
    "Billing":          "client/billing.html",
    "Team":             "client/settings.html",
    "Settings":         "client/settings.html",
}

# Sidebar nav-item text (advocate dashboard) → root-relative path
ADVOCATE_SIDEBAR_ROUTES = {
    "Peluang":        "advocate/mobile.html",
    "Kampanye Saya":  "advocate/campaigns.html",
    "Inbox":          "advocate/inbox.html",
    "Earning":        "advocate/mobile.html",
    "Profil":         "advocate/profile.html",
    "Verifikasi":     "advocate/verification.html",
}

# Which web-nav item text indicates "current page" — keyed by output page (root-relative)
PAGE_ACTIVE_NAV = {
    "film.html":                   "Film",
    "politik.html":                "Politik",
    "pricing.html":                "Harga",
    "how-it-works-client.html":    "Cara Kerja",
    "how-it-works-advocate.html":  "Untuk Advocate",
    "solutions.html":              "Solusi",
    "about.html":                  "Tentang",
    "trust.html":                  "Trust & Safety",
    "faq.html":                    "Bantuan",
    "contact.html":                "Kontak",
}

# ---------------------------------------------------------------------------
# Parse the source file
# ---------------------------------------------------------------------------
print(f"Reading {SRC}…")
src = SRC.read_text(encoding="utf-8")

# Extract <style>…</style>
m = re.search(r"<style>(.*?)</style>", src, re.DOTALL)
if not m:
    raise SystemExit("No <style> block found")
css_inner = m.group(1)

# Extract the SVG sprite (the inline <svg width="0" height="0" …>…</svg>)
sprite_m = re.search(
    r'(<svg width="0" height="0"[^>]*>.*?</svg>)',
    src,
    re.DOTALL,
)
if not sprite_m:
    raise SystemExit("No SVG sprite found")
sprite_html = sprite_m.group(1)

# Extract demoToggle, demoBackdrop, demoDrawer blocks (verbatim)
toggle_m = re.search(
    r'(<button id="demoToggle".*?</button>)',
    src,
    re.DOTALL,
)
backdrop_m = re.search(
    r'(<div id="demoBackdrop"[^>]*></div>)',
    src,
)
drawer_m = re.search(
    r'(<aside id="demoDrawer".*?</aside>)',
    src,
    re.DOTALL,
)
if not (toggle_m and backdrop_m and drawer_m):
    raise SystemExit("Demo drawer markup not found")
demo_toggle_html = toggle_m.group(1)
demo_backdrop_html = backdrop_m.group(1)
demo_drawer_html_raw = drawer_m.group(1)

# Extract screens.  Iterate by start positions to handle non-greedy correctly.
section_starts = [
    (m.start(), m.group(1))
    for m in re.finditer(r'<section id="(s-[^"]+)" class="screen[^"]*">', src)
]
# Each section ends at the next "^</section>" line after its start.
close_positions = [m.start() for m in re.finditer(r"\n</section>", src)]
screens: dict[str, str] = {}
for i, (start, sid) in enumerate(section_starts):
    # next close after start
    close = next((c for c in close_positions if c > start), None)
    if close is None:
        raise SystemExit(f"No closing </section> for {sid}")
    end = close + len("\n</section>")
    block = src[start:end]
    screens[sid] = block

print(f"Found {len(screens)} screens.")

missing = [k for k in SCREEN_MAP if k not in screens]
if missing:
    raise SystemExit(f"Missing expected screens: {missing}")

# ---------------------------------------------------------------------------
# Write shared assets
# ---------------------------------------------------------------------------
(ASSETS / "style.css").write_text(css_inner.lstrip("\n"), encoding="utf-8")

# Standalone icons.svg (with viewBox stripped width/height? Keep <defs>)
# Use the same sprite contents but as a top-level <svg> with no width/height.
stand_alone_sprite = re.sub(
    r'^<svg width="0" height="0"[^>]*>',
    '<svg xmlns="http://www.w3.org/2000/svg" style="display:none">',
    sprite_html,
    count=1,
)
(ASSETS / "icons.svg").write_text(stand_alone_sprite, encoding="utf-8")

# ---------------------------------------------------------------------------
# Helpers for transforming a screen
# ---------------------------------------------------------------------------

def relpath_to(from_file: str, target_root_rel: str) -> str:
    """Compute a relative href from a generated page back to a target file."""
    if "/" not in from_file:
        return target_root_rel
    # from_file lives in subfolder; need to step up
    depth = from_file.count("/")
    return ("../" * depth) + target_root_rel


def transform_web_nav(html: str, active_label: str | None, current_page_rel: str) -> str:
    """Convert <span class="item …">Label</span> inside .web-nav to <a> links."""

    def replace_block(block_m: re.Match) -> str:
        block = block_m.group(0)

        def replace_span(span_m: re.Match) -> str:
            cls = span_m.group(1) or ""
            label_html = span_m.group(2)
            # Convert &amp; back for matching, then preserve original label text in output
            label_plain = (
                label_html
                .replace("&amp;", "&")
                .strip()
            )
            target = NAV_ROUTES.get(label_plain, "index.html")
            href = relpath_to(current_page_rel, target)
            classes = ["item"]
            # detect existing "active" presence in the cls attribute
            had_active = "active" in cls
            should_active = active_label and label_plain == active_label
            if had_active or should_active:
                classes.append("active")
            return (
                f'<a class="{" ".join(classes)}" href="{href}">{label_html}</a>'
            )

        return re.sub(
            r'<span class="(item[^"]*)">([^<]+)</span>',
            replace_span,
            block,
        )

    return re.sub(
        r'<div class="web-nav">(?:[\s\S]*?)</div>',
        replace_block,
        html,
        count=0,
    )


def transform_logo(html: str, current_page_rel: str) -> str:
    href = relpath_to(current_page_rel, "index.html")
    return re.sub(
        r'<div class="logo">RESONANSI</div>',
        f'<a class="logo" href="{href}">RESONANSI</a>',
        html,
    )


def transform_sidebar(html: str, current_page_rel: str) -> str:
    """Convert <div class="nav-item ..."> Icon Text </div> into <a> links.

    Detects label (last text in the div) and chooses route based on client
    vs advocate context (decided by whether the label appears in either map).
    """

    def replace(m: re.Match) -> str:
        cls = m.group(1) or ""
        inner = m.group(2)
        # Strip tags from inner to get the label
        text = re.sub(r"<[^>]+>", "", inner).strip()
        # Find last meaningful word group (e.g. "Buat Brief")
        # The "label" is everything after the SVG; in practice it's the trailing text node.
        label = text  # full visible text
        # Try advocate routes first if it looks advocate-y (icon hints handled elsewhere)
        target = None
        if label in CLIENT_SIDEBAR_ROUTES:
            target = CLIENT_SIDEBAR_ROUTES[label]
        elif label in ADVOCATE_SIDEBAR_ROUTES:
            target = ADVOCATE_SIDEBAR_ROUTES[label]
        if target is None:
            return m.group(0)  # leave it alone
        href = relpath_to(current_page_rel, target)
        return f'<a class="{cls}" href="{href}">{inner}</a>'

    return re.sub(
        r'<div class="(nav-item[^"]*)">([\s\S]*?)</div>',
        replace,
        html,
    )


def transform_footer(html: str, current_page_rel: str) -> str:
    """Convert footer <li>Label</li> to <li><a href=…>Label</a></li>."""

    # Only transform <li>…</li> inside the .mega-footer block (we approximate by
    # looking for <li>X</li> with simple inline text only).
    def replace(m: re.Match) -> str:
        inner = m.group(1)
        # only transform if it's a plain text label (no nested tags)
        if "<" in inner:
            return m.group(0)
        plain = inner.replace("&amp;", "&").strip()
        target = FOOTER_ROUTES.get(plain, "index.html")
        href = relpath_to(current_page_rel, target)
        return f'<li><a href="{href}">{inner}</a></li>'

    # Limit replacement to inside <div class="mega-footer">…</div>
    def in_footer(footer_m: re.Match) -> str:
        return re.sub(r"<li>([^<]+)</li>", replace, footer_m.group(0))

    return re.sub(
        r'<div class="mega-footer">[\s\S]*?</div>\s*</div>\s*</div>',
        in_footer,
        html,
    )


def build_drawer(current_page_rel: str, current_screen_id: str) -> str:
    """Rewrite demo drawer so each <button data-target="..."> becomes an <a>."""
    drawer = demo_drawer_html_raw

    def replace_button(m: re.Match) -> str:
        target_id = m.group(1)
        label = m.group(2)
        mapping = SCREEN_MAP.get(target_id)
        if not mapping:
            return m.group(0)
        target_file = mapping[0]
        href = relpath_to(current_page_rel, target_file)
        active = " active" if target_id == current_screen_id else ""
        cls = f"drawer-link{active}".strip()
        return f'<a class="{cls}" href="{href}">{label}</a>'

    return re.sub(
        r'<button data-target="([^"]+)">([\s\S]*?)</button>',
        replace_button,
        drawer,
    )


def transform_screen(screen_html: str, current_page_rel: str, screen_id: str) -> str:
    """Strip the screen's <h2 class="screen-title"> + meta and rewrite nav/footer/sidebar."""
    html = screen_html
    # Remove the screen-title and screen-meta paragraphs (CSS hides them but
    # let's strip to keep the document clean).
    html = re.sub(r'<h2 class="screen-title">[\s\S]*?</h2>\s*', '', html, count=1)
    html = re.sub(r'<p class="screen-meta">[\s\S]*?</p>\s*', '', html, count=1)
    # Strip "active" from the section opening tag so we don't get stale state
    html = re.sub(
        r'^<section id="(s-[^"]+)" class="screen active">',
        r'<section id="\1" class="screen">',
        html,
        count=1,
    )

    active_label = PAGE_ACTIVE_NAV.get(current_page_rel)
    html = transform_web_nav(html, active_label, current_page_rel)
    html = transform_logo(html, current_page_rel)
    html = transform_sidebar(html, current_page_rel)
    html = transform_footer(html, current_page_rel)
    return html


# ---------------------------------------------------------------------------
# Per-page HTML template
# ---------------------------------------------------------------------------

PAGE_TPL = """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — Resonansi</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap">
  <link rel="stylesheet" href="{assets_prefix}style.css">
  <style>
    /* Multi-page overrides: every page renders a single .screen full-bleed */
    .screen {{ display: block !important; min-height: 100vh; padding: 0; max-width: none; }}
    .screen.active {{ display: block !important; }}
    .screen .screen-title, .screen .screen-meta {{ display: none; }}
    .frame-label {{ display: none; }}
    .frame {{ border: none; border-radius: 0; box-shadow: none; }}
    /* Demo drawer uses <a> tags now */
    .demo-group a {{
      display: block;
      width: 100%;
      text-align: left;
      background: transparent;
      border: none;
      padding: 9px 12px;
      border-radius: 8px;
      font-family: var(--font-body);
      font-size: 13.5px;
      color: var(--grey-700);
      font-weight: 500;
      cursor: pointer;
      text-decoration: none;
      transition: all 0.15s;
    }}
    .demo-group a:hover {{ background: var(--grey-100); color: var(--ink); }}
    .demo-group a.active {{ background: var(--accent-soft); color: var(--accent); font-weight: 600; }}
    /* Make all clickable converted links inherit text style */
    .web-nav a.item {{ text-decoration: none; color: inherit; }}
    a.logo {{ text-decoration: none; color: inherit; }}
    a.nav-item {{ text-decoration: none; color: inherit; }}
    .mega-footer ul li a {{ color: inherit; text-decoration: none; display: block; }}
  </style>
</head>
<body>

{demo_toggle}
{demo_backdrop}
{demo_drawer}

{sprite}

{screen}

<script>
  (function() {{
    var drawer   = document.getElementById('demoDrawer');
    var backdrop = document.getElementById('demoBackdrop');
    var toggle   = document.getElementById('demoToggle');
    var closeBtn = document.getElementById('demoClose');
    if (!drawer || !backdrop || !toggle || !closeBtn) return;
    function openDrawer()  {{ drawer.classList.add('open');    backdrop.classList.add('open');    drawer.setAttribute('aria-hidden','false'); }}
    function closeDrawer() {{ drawer.classList.remove('open'); backdrop.classList.remove('open'); drawer.setAttribute('aria-hidden','true'); }}
    toggle.addEventListener('click', openDrawer);
    closeBtn.addEventListener('click', closeDrawer);
    backdrop.addEventListener('click', closeDrawer);
    document.addEventListener('keydown', function(e) {{ if (e.key === 'Escape') closeDrawer(); }});
  }})();
</script>

</body>
</html>
"""

# ---------------------------------------------------------------------------
# Generate each page
# ---------------------------------------------------------------------------
created: list[str] = []
for screen_id, (rel_path, title) in SCREEN_MAP.items():
    screen_block = screens[screen_id]
    transformed = transform_screen(screen_block, rel_path, screen_id)
    drawer_html = build_drawer(rel_path, screen_id)
    assets_prefix = "../" * rel_path.count("/") + "assets/"
    page_html = PAGE_TPL.format(
        title=title,
        assets_prefix=assets_prefix,
        demo_toggle=demo_toggle_html,
        demo_backdrop=demo_backdrop_html,
        demo_drawer=drawer_html,
        sprite=sprite_html,
        screen=transformed,
    )
    out_path = OUT / rel_path
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(page_html, encoding="utf-8")
    created.append(str(out_path.relative_to(OUT)))

print(f"\nGenerated {len(created)} HTML pages under {OUT}/")
for p in created:
    print(f"  {p}")
