"""
Build 15 new HTML pages for the Resonansi site and update demo drawers everywhere.
Run: python3 /Users/haimac/buzzer/site/_build_new_pages.py
"""
import os
import re

SITE_DIR = '/Users/haimac/buzzer/site'

# ============================================================
# DRAWER TEMPLATE
# ============================================================
def drawer_body(prefix, active_href=None):
    """Build drawer body. prefix is '' for root, '../' for client/ and advocate/.
    active_href should be the link href that's currently active (e.g. 'login.html').
    """
    def link(href, label):
        cls = "drawer-link active" if href == active_href else "drawer-link"
        full = prefix + href
        return f'      <a class="{cls}" href="{full}">{label}</a>'

    parts = []
    parts.append('<div class="demo-group">')
    parts.append('      <div class="demo-group-label">⚙ AUTH</div>')
    parts.append(link('login.html', 'Masuk (Login)'))
    parts.append(link('signup.html', 'Daftar (Sign Up)'))
    parts.append(link('forgot-password.html', 'Lupa Password'))
    parts.append(link('reset-password.html', 'Reset Password'))
    parts.append(link('email-verify.html', 'Verifikasi Email'))
    parts.append(link('welcome.html', 'Welcome / Tour'))
    parts.append('    </div>\n')

    parts.append('    <div class="demo-group">')
    parts.append('      <div class="demo-group-label">⚙ DESIGN SYSTEM</div>')
    parts.append(link('design-system.html', 'Design System Showcase'))
    parts.append('    </div>\n')

    parts.append('    <div class="demo-group">')
    parts.append('      <div class="demo-group-label">MARKETING</div>')
    parts.append(link('index.html', 'Homepage'))
    parts.append(link('how-it-works-client.html', 'How it Works — Client'))
    parts.append(link('how-it-works-advocate.html', 'How it Works — Advocate'))
    parts.append(link('solutions.html', 'Solutions per Industri'))
    parts.append(link('about.html', 'Tentang Resonansi'))
    parts.append(link('trust.html', 'Trust &amp; Safety'))
    parts.append(link('faq.html', 'FAQ / Pusat Bantuan'))
    parts.append(link('contact.html', 'Kontak / Demo Request'))
    parts.append('    </div>\n')

    parts.append('    <div class="demo-group">')
    parts.append('      <div class="demo-group-label">VERTIKAL</div>')
    parts.append(link('film.html', 'Halaman Film'))
    parts.append(link('politik.html', 'Halaman Politik'))
    parts.append(link('browse.html', 'Browse Advocates'))
    parts.append(link('pricing.html', 'Pricing'))
    parts.append('    </div>\n')

    parts.append('    <div class="demo-group">')
    parts.append('      <div class="demo-group-label">CLIENT (DASHBOARD)</div>')
    parts.append(link('client/dashboard.html', 'Dashboard Home'))
    parts.append(link('client/brief.html', 'Buat Brief (Wizard)'))
    parts.append(link('client/brief-detail.html', 'Brief Detail'))
    parts.append(link('client/campaigns.html', 'Kampanye (List)'))
    parts.append(link('client/shortlist.html', 'Shortlist Advocate'))
    parts.append(link('client/advocate-detail.html', 'Advocate Detail'))
    parts.append(link('client/approval.html', 'Content Approval'))
    parts.append(link('client/live-campaign.html', 'Live Campaign'))
    parts.append(link('client/library.html', 'Advocate Library'))
    parts.append(link('client/analytics.html', 'Analytics'))
    parts.append(link('client/billing.html', 'Billing &amp; Invoices'))
    parts.append(link('client/settings.html', 'Settings'))
    parts.append('    </div>\n')

    parts.append('    <div class="demo-group">')
    parts.append('      <div class="demo-group-label">ADVOCATE</div>')
    parts.append(link('advocate/onboarding.html', 'Onboarding (Mobile)'))
    parts.append(link('advocate/mobile.html', 'Mobile App'))
    parts.append(link('advocate/profile.html', 'Profile Editor'))
    parts.append(link('advocate/campaigns.html', 'My Campaigns'))
    parts.append(link('advocate/apply-brief.html', 'Apply ke Brief'))
    parts.append(link('advocate/inbox.html', 'Inbox / Chat'))
    parts.append(link('advocate/verification.html', 'Verification Center'))
    parts.append(link('advocate/tax-receipt.html', 'Bukti Potong PPh'))
    parts.append('    </div>\n')

    parts.append('    <div class="demo-group">')
    parts.append('      <div class="demo-group-label">PAGES TAMBAHAN</div>')
    parts.append(link('case-study-detail.html', 'Studi Kasus — Detail'))
    parts.append(link('blog-detail.html', 'Blog — Artikel'))
    parts.append(link('career.html', 'Karir'))
    parts.append(link('press.html', 'Press &amp; Media'))
    parts.append(link('trust-audit.html', 'Trust Audit Publik'))
    parts.append(link('dispute.html', 'Laporkan Sengketa'))
    parts.append(link('notifications.html', 'Notification Center'))
    parts.append(link('404.html', '404 — Not Found'))
    parts.append('    </div>')

    return '\n    '.join(parts)


# Total page count (existing 32 + 15 new = 47)
TOTAL_PAGES = 47


# ============================================================
# Standard sprite (full set, copied from about.html)
# ============================================================
SPRITE = '''<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <defs>
    <symbol id="i-home" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m3 10 9-7 9 7v10a2 2 0 0 1-2 2h-4v-7H9v7H5a2 2 0 0 1-2-2z"/></symbol>
    <symbol id="i-edit" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="m18.5 2.5 3 3L12 15l-4 1 1-4z"/></symbol>
    <symbol id="i-megaphone" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11v2l4 .5V10.5z"/><path d="m7 10.5 12-5v13l-12-5z"/><path d="M11 14v3a2 2 0 0 0 4 0v-1.5"/></symbol>
    <symbol id="i-bookmark" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 21V5a2 2 0 0 0-2-2H7a2 2 0 0 0-2 2v16l7-3z"/></symbol>
    <symbol id="i-chart" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v18h18"/><rect x="7" y="12" width="3" height="6" rx="1"/><rect x="12" y="8" width="3" height="10" rx="1"/><rect x="17" y="5" width="3" height="13" rx="1"/></symbol>
    <symbol id="i-card" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="5" width="20" height="14" rx="2"/><line x1="2" y1="10" x2="22" y2="10"/></symbol>
    <symbol id="i-users" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></symbol>
    <symbol id="i-settings" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M19 12.97a7.5 7.5 0 0 0 0-1.94l2-1.5-2-3.46-2.34.83a7.5 7.5 0 0 0-1.68-.97L14.5 3.5h-5l-.48 2.43a7.5 7.5 0 0 0-1.68.97L5 6.07 3 9.53l2 1.5a7.5 7.5 0 0 0 0 1.94l-2 1.5 2 3.46 2.34-.83a7.5 7.5 0 0 0 1.68.97L9.5 20.5h5l.48-2.43a7.5 7.5 0 0 0 1.68-.97l2.34.83 2-3.46z"/></symbol>
    <symbol id="i-zap" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 4 14 12 14 11 22 20 10 12 10 13 2"/></symbol>
    <symbol id="i-mail" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="5" width="20" height="14" rx="2"/><polyline points="2 7 12 13 22 7"/></symbol>
    <symbol id="i-wallet" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 7a2 2 0 0 1 2-2h14v4H5a2 2 0 0 1-2-2"/><path d="M3 7v11a2 2 0 0 0 2 2h15a1 1 0 0 0 1-1v-4"/><path d="M21 12v4h-4a2 2 0 0 1 0-4z"/></symbol>
    <symbol id="i-user" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"/><path d="M4 21v-1a6 6 0 0 1 6-6h4a6 6 0 0 1 6 6v1"/></symbol>
    <symbol id="i-shield" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><polyline points="9 12 11 14 15 10"/></symbol>
    <symbol id="i-search" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><line x1="21" y1="21" x2="16.5" y2="16.5"/></symbol>
    <symbol id="i-bell" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10 21a2 2 0 0 0 4 0"/></symbol>
    <symbol id="i-play" viewBox="0 0 24 24" fill="currentColor"><polygon points="6 4 20 12 6 20 6 4"/></symbol>
    <symbol id="i-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="4 12 10 18 20 6"/></symbol>
    <symbol id="i-film" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><line x1="7" y1="3" x2="7" y2="21"/><line x1="17" y1="3" x2="17" y2="21"/><line x1="3" y1="12" x2="21" y2="12"/></symbol>
    <symbol id="i-globe" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3a14 14 0 0 1 0 18"/><path d="M12 3a14 14 0 0 0 0 18"/></symbol>
    <symbol id="i-heart" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.6a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78L12 21.23l8.84-8.84a5.5 5.5 0 0 0 0-7.78z"/></symbol>
    <symbol id="i-instagram" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></symbol>
    <symbol id="i-tiktok" viewBox="0 0 24 24" fill="currentColor"><path d="M16 3v3.5a4.5 4.5 0 0 0 4.5 4.5V14a7.5 7.5 0 0 1-4.5-1.5V16a5.5 5.5 0 1 1-5.5-5.5v3a2.5 2.5 0 1 0 2.5 2.5V3z"/></symbol>
    <symbol id="i-youtube" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 7.2a2.8 2.8 0 0 0-2-2C17 5 12 5 12 5s-5 0-7 .2a2.8 2.8 0 0 0-2 2A29 29 0 0 0 3 12a29 29 0 0 0 0 4.8 2.8 2.8 0 0 0 2 2c2 .2 7 .2 7 .2s5 0 7-.2a2.8 2.8 0 0 0 2-2A29 29 0 0 0 21 12a29 29 0 0 0 0-4.8z"/><polygon points="10 9 16 12 10 15" fill="currentColor"/></symbol>
    <symbol id="i-x" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2H21l-6.51 7.444L22 22h-6.563l-5.14-6.72L4.4 22H1.642l6.96-7.95L1.5 2h6.7l4.65 6.139zm-2.298 18.4h1.534L7.07 3.46H5.42z"/></symbol>
    <symbol id="i-attach" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m21 11-8.5 8.5a5 5 0 1 1-7-7L14 4a3.5 3.5 0 0 1 5 5l-8.5 8.5a2 2 0 1 1-3-3l7.5-7.5"/></symbol>
    <symbol id="i-send" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m3 11 18-8-8 18-2-8z"/></symbol>
    <symbol id="i-calendar" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="16" rx="2"/><line x1="3" y1="10" x2="21" y2="10"/><line x1="8" y1="3" x2="8" y2="7"/><line x1="16" y1="3" x2="16" y2="7"/></symbol>
    <symbol id="i-camera" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 7h4l2-3h6l2 3h4a1 1 0 0 1 1 1v11a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V8a1 1 0 0 1 1-1z"/><circle cx="12" cy="13" r="4"/></symbol>
  </defs>
</svg>'''


STD_STYLE = '''<style>
    /* Multi-page overrides: every page renders a single .screen full-bleed */
    .screen { display: block !important; min-height: 100vh; padding: 0; max-width: none; }
    .screen.active { display: block !important; }
    .screen .screen-title, .screen .screen-meta { display: none; }
    .frame-label { display: none; }
    .frame { border: none; border-radius: 0; box-shadow: none; }
    /* Demo drawer uses <a> tags now */
    .demo-group a {
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
    }
    .demo-group a:hover { background: var(--grey-100); color: var(--ink); }
    .demo-group a.active { background: var(--accent-soft); color: var(--accent); font-weight: 600; }
    /* Make all clickable converted links inherit text style */
    .web-nav a.item { text-decoration: none; color: inherit; }
    a.logo { text-decoration: none; color: inherit; }
    a.nav-item { text-decoration: none; color: inherit; }
    .mega-footer ul li a { color: inherit; text-decoration: none; display: block; }
  </style>'''


STD_SCRIPT = '''<script>
  (function() {
    var drawer   = document.getElementById('demoDrawer');
    var backdrop = document.getElementById('demoBackdrop');
    var toggle   = document.getElementById('demoToggle');
    var closeBtn = document.getElementById('demoClose');
    if (!drawer || !backdrop || !toggle || !closeBtn) return;
    function openDrawer()  { drawer.classList.add('open');    backdrop.classList.add('open');    drawer.setAttribute('aria-hidden','false'); }
    function closeDrawer() { drawer.classList.remove('open'); backdrop.classList.remove('open'); drawer.setAttribute('aria-hidden','true'); }
    toggle.addEventListener('click', openDrawer);
    closeBtn.addEventListener('click', closeDrawer);
    backdrop.addEventListener('click', closeDrawer);
    document.addEventListener('keydown', function(e) { if (e.key === 'Escape') closeDrawer(); });
  })();
</script>'''


def chrome(title, prefix, active_href, extra_style=''):
    """Top of HTML doc with head + drawer + sprite. prefix='' or '../'."""
    css_path = prefix + 'assets/style.css'
    return f'''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap">
  <link rel="stylesheet" href="{css_path}">
  {STD_STYLE}
  {extra_style}
</head>
<body>

<button id="demoToggle" class="demo-toggle" title="Buka indeks halaman" aria-label="Buka indeks halaman demo">
  <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
  <span>Demo · {TOTAL_PAGES} halaman</span>
</button>
<div id="demoBackdrop" class="demo-backdrop"></div>
<aside id="demoDrawer" class="demo-drawer" aria-hidden="true">
  <div class="demo-drawer-head">
    <div>
      <strong>Resonansi · Demo Index</strong>
      <p class="small muted mb-0" style="margin-top:4px;">Klik halaman mana saja untuk berpindah. Header menu di setiap halaman juga aktif.</p>
    </div>
    <button class="demo-close" id="demoClose" aria-label="Tutup">×</button>
  </div>

  <div class="demo-drawer-body">
    {drawer_body(prefix, active_href)}
  </div>
</aside>

{SPRITE}

'''


def chrome_close():
    return f'''
{STD_SCRIPT}

</body>
</html>
'''


def write_page(rel_path, html):
    full = os.path.join(SITE_DIR, rel_path)
    os.makedirs(os.path.dirname(full), exist_ok=True) if os.path.dirname(full) else None
    with open(full, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'  wrote {rel_path}')


# Shared marketing header + footer
def web_header(prefix='', active=''):
    def cls(name): return 'item active' if name == active else 'item'
    return f'''<div class="web-header">
      <a class="logo" href="{prefix}index.html">RESONANSI</a>
      <div class="web-nav">
        <a class="{cls("how")}" href="{prefix}how-it-works-client.html">Cara Kerja</a>
        <a class="{cls("adv")}" href="{prefix}how-it-works-advocate.html">Untuk Advocate</a>
        <a class="{cls("sol")}" href="{prefix}solutions.html">Solusi</a>
        <a class="{cls("price")}" href="{prefix}pricing.html">Harga</a>
        <a class="{cls("about")}" href="{prefix}about.html">Tentang</a>
        <a class="{cls("contact")}" href="{prefix}contact.html">Kontak</a>
      </div>
      <div class="right row-tight">
        <a class="btn ghost" href="{prefix}login.html">Masuk</a>
        <a class="btn" href="{prefix}signup.html">Mulai Gratis</a>
      </div>
    </div>'''


def mega_footer(prefix=''):
    return f'''<div class="mega-footer">
      <div class="container">
        <div class="footer-brand">
          <a class="logo" href="{prefix}index.html">RESONANSI</a>
          <p>Suara Anda, dampak nyata.</p>
          <div class="social-icons">
            <a><svg width="16" height="16"><use href="#i-instagram"/></svg></a>
            <a><svg width="16" height="16"><use href="#i-x"/></svg></a>
            <a><svg width="16" height="16"><use href="#i-youtube"/></svg></a>
            <a><svg width="16" height="16"><use href="#i-tiktok"/></svg></a>
          </div>
        </div>
        <div><h4>Produk</h4><ul><li><a href="{prefix}how-it-works-client.html">Cara Kerja (Client)</a></li><li><a href="{prefix}how-it-works-advocate.html">Cara Kerja (Advocate)</a></li><li><a href="{prefix}solutions.html">Solusi</a></li><li><a href="{prefix}pricing.html">Harga</a></li></ul></div>
        <div><h4>Solusi</h4><ul><li><a href="{prefix}film.html">Film</a></li><li><a href="{prefix}politik.html">Politik</a></li><li><a href="{prefix}index.html">Brand</a></li><li><a href="{prefix}solutions.html">NGO</a></li></ul></div>
        <div><h4>Resources</h4><ul><li><a href="{prefix}case-study-detail.html">Studi Kasus</a></li><li><a href="{prefix}blog-detail.html">Blog</a></li><li><a href="{prefix}faq.html">FAQ</a></li></ul></div>
        <div><h4>Perusahaan</h4><ul><li><a href="{prefix}about.html">Tentang</a></li><li><a href="{prefix}career.html">Karir</a></li><li><a href="{prefix}press.html">Press</a></li><li><a href="{prefix}contact.html">Kontak</a></li></ul></div>
      </div>
      <div class="footer-bottom container">
        <span>© 2026 PT Resonansi Suara Indonesia</span>
      </div>
    </div>'''


# ============================================================
# 1. forgot-password.html
# ============================================================
AUTH_STYLE = '''<style>
    .screen { display: block !important; min-height: 100vh; }
    body { background: #fff; }
    a.btn { text-decoration: none; }
    .auth-layout { min-height: 100vh; display: grid; grid-template-columns: 1.05fr 0.95fr; }
    .auth-art {
      background:
        radial-gradient(circle at 25% 20%, rgba(255,180,0,0.18) 0%, transparent 50%),
        radial-gradient(circle at 75% 75%, rgba(11,95,224,0.35) 0%, transparent 55%),
        linear-gradient(135deg, #061F49 0%, #0B5FE0 50%, #093F94 100%);
      color: #fff;
      padding: 56px 60px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      position: relative;
      overflow: hidden;
    }
    .auth-art::after { content: ""; position: absolute; bottom: -200px; right: -200px; width: 500px; height: 500px; border-radius: 50%; background: radial-gradient(circle, rgba(255,180,0,0.25), transparent 70%); pointer-events: none; }
    .auth-art .logo { background: rgba(255,255,255,0.08); color: #fff; backdrop-filter: blur(4px); }
    .auth-art h1 { font-size: 44px; line-height: 1.1; letter-spacing: -0.025em; color: #fff; margin: 0 0 16px; }
    .auth-art p { font-size: 17px; opacity: 0.85; margin: 0; line-height: 1.55; max-width: 440px; }
    .trust-row { display: flex; align-items: center; gap: 14px; padding: 14px 0; }
    .trust-row .ico-circle { width: 44px; height: 44px; border-radius: 50%; background: rgba(255,255,255,0.1); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
    .trust-row strong { font-size: 14px; color: #fff; }
    .trust-row .small { font-size: 12.5px; opacity: 0.72; }
    .auth-form-side { padding: 64px 80px; display: flex; flex-direction: column; justify-content: center; max-width: 560px; margin: 0 auto; width: 100%; }
    .auth-form-side h2 { font-size: 32px; letter-spacing: -0.02em; margin: 0 0 8px; }
    .auth-form-side .form-sub { color: var(--muted); margin: 0 0 32px; font-size: 14.5px; }
    .auth-form-side .form-sub a { color: var(--accent); font-weight: 600; text-decoration: none; }
    .auth-form .form-group { margin-bottom: 16px; }
    .auth-form .form-group input { width: 100%; padding: 13px 16px; border-radius: 12px; border: 1px solid var(--line); font-family: var(--font-body); font-size: 14.5px; background: #fff; transition: border-color 0.15s, box-shadow 0.15s; color: var(--ink); }
    .auth-form .form-group input:focus { outline: none; border-color: var(--accent); box-shadow: 0 0 0 4px rgba(11,95,224,0.08); }
    @media (max-width: 900px) { .auth-layout { grid-template-columns: 1fr; } .auth-art { display: none; } .auth-form-side { padding: 40px 24px; } }
  </style>'''


def page_forgot_password():
    head = chrome('Lupa Password — Resonansi', '', 'forgot-password.html', AUTH_STYLE)
    body = '''<div class="auth-layout">

  <aside class="auth-art">
    <a class="logo" href="index.html">RESONANSI</a>

    <div style="position: relative; z-index: 1;">
      <h1>Lupa password?<br>Tidak masalah.</h1>
      <p>Kami akan kirim link reset password ke email kerja Anda. Link berlaku 30 menit untuk keamanan.</p>

      <div style="margin-top: 56px;">
        <div class="trust-row">
          <div class="ico-circle"><svg width="22" height="22"><use href="#i-shield"/></svg></div>
          <div>
            <strong>Link Aman & Berbatas Waktu</strong>
            <div class="small">Reset link hanya berlaku 30 menit</div>
          </div>
        </div>
        <div class="trust-row">
          <div class="ico-circle"><svg width="22" height="22"><use href="#i-mail"/></svg></div>
          <div>
            <strong>Cek Folder Spam Jika Perlu</strong>
            <div class="small">Email dikirim dari noreply@resonansi.id</div>
          </div>
        </div>
      </div>
    </div>

    <div class="small" style="opacity: 0.6; position: relative; z-index: 1;">
      © 2026 PT Resonansi Suara Indonesia · Terdaftar di Kominfo PSE
    </div>
  </aside>

  <main class="auth-form-side">
    <a class="btn ghost" href="login.html" style="align-self:flex-start; padding-left: 0; margin-bottom: 28px;">← Kembali ke Masuk</a>

    <h2>Reset password Anda</h2>
    <p class="form-sub">Masukkan email yang Anda gunakan untuk masuk. Kami akan kirim link untuk membuat password baru.</p>

    <form class="auth-form" onsubmit="event.preventDefault(); window.location.href='reset-password.html';">
      <div class="form-group">
        <label style="display:block; font-size:13px; font-weight:600; margin-bottom:6px;">Email Kerja</label>
        <input type="email" placeholder="nama@perusahaan.com" required autocomplete="email" value="marketing@falconpictures.id">
      </div>

      <button type="submit" class="btn lg" style="width:100%; justify-content:center; margin-top: 8px;">
        Kirim Link Reset →
      </button>
    </form>

    <div style="margin-top: 28px; padding: 18px 20px; background: var(--grey-50); border-radius: 12px;">
      <div style="font-size:13.5px; font-weight: 600; color: var(--ink); margin-bottom: 4px;">Belum dapat email?</div>
      <div class="small muted" style="line-height: 1.55;">
        Periksa folder Spam atau Promosi. Jika masih kosong setelah 5 menit, hubungi <a href="contact.html" style="color:var(--accent);">support@resonansi.id</a>.
      </div>
    </div>

    <p class="small muted" style="text-align:center; margin-top: 32px; line-height: 1.6;">
      Ingat password? <a href="login.html" style="color:var(--accent); font-weight:600;">Masuk →</a>
    </p>
  </main>
</div>'''
    return head + body + chrome_close()


# ============================================================
# 2. reset-password.html
# ============================================================
def page_reset_password():
    head = chrome('Reset Password — Resonansi', '', 'reset-password.html', AUTH_STYLE)
    body = '''<div class="auth-layout">

  <aside class="auth-art">
    <a class="logo" href="index.html">RESONANSI</a>

    <div style="position: relative; z-index: 1;">
      <h1>Buat password baru<br>yang kuat.</h1>
      <p>Minimal 8 karakter, kombinasi huruf besar, kecil, angka, dan simbol. Hindari password yang pernah digunakan.</p>

      <div style="margin-top: 56px;">
        <div class="trust-row">
          <div class="ico-circle"><svg width="22" height="22"><use href="#i-shield"/></svg></div>
          <div>
            <strong>Enkripsi End-to-End</strong>
            <div class="small">Password Anda di-hash dengan bcrypt</div>
          </div>
        </div>
        <div class="trust-row">
          <div class="ico-circle"><svg width="22" height="22"><use href="#i-check"/></svg></div>
          <div>
            <strong>Tidak Ada Yang Tahu</strong>
            <div class="small">Bahkan tim Resonansi tidak bisa melihat password Anda</div>
          </div>
        </div>
      </div>
    </div>

    <div class="small" style="opacity: 0.6; position: relative; z-index: 1;">
      © 2026 PT Resonansi Suara Indonesia · Terdaftar di Kominfo PSE
    </div>
  </aside>

  <main class="auth-form-side">
    <a class="btn ghost" href="login.html" style="align-self:flex-start; padding-left: 0; margin-bottom: 28px;">← Kembali ke Masuk</a>

    <h2>Buat password baru</h2>
    <p class="form-sub">Pilih password baru yang kuat. Anda akan otomatis dimasukkan ke akun Anda setelah selesai.</p>

    <form class="auth-form" onsubmit="event.preventDefault(); document.getElementById('successCard').style.display='block'; this.style.display='none';">
      <div class="form-group">
        <label style="display:block; font-size:13px; font-weight:600; margin-bottom:6px;">Password Baru</label>
        <input type="password" placeholder="••••••••" required autocomplete="new-password">
        <div class="small muted" style="margin-top:6px;">Minimal 8 karakter, huruf besar & kecil, angka, simbol.</div>
      </div>

      <div class="form-group">
        <label style="display:block; font-size:13px; font-weight:600; margin-bottom:6px;">Konfirmasi Password</label>
        <input type="password" placeholder="••••••••" required autocomplete="new-password">
      </div>

      <!-- Password strength meter -->
      <div style="margin: 16px 0 24px;">
        <div class="small" style="display:flex; justify-content:space-between; margin-bottom: 6px;">
          <span class="muted">Kekuatan password</span>
          <strong style="color: #16a34a;">Kuat</strong>
        </div>
        <div style="display:flex; gap:4px;">
          <div style="flex:1; height:4px; background:#16a34a; border-radius:2px;"></div>
          <div style="flex:1; height:4px; background:#16a34a; border-radius:2px;"></div>
          <div style="flex:1; height:4px; background:#16a34a; border-radius:2px;"></div>
          <div style="flex:1; height:4px; background:var(--grey-200); border-radius:2px;"></div>
        </div>
      </div>

      <button type="submit" class="btn lg" style="width:100%; justify-content:center;">
        Simpan Password Baru →
      </button>
    </form>

    <!-- Success state, hidden by default -->
    <div id="successCard" class="card" style="display:none; padding: 32px; text-align: center; border-color: #c8d8f7; background: var(--accent-soft);">
      <div style="width: 72px; height: 72px; border-radius: 50%; background: #16a34a; color: #fff; display: inline-flex; align-items: center; justify-content: center; margin-bottom: 16px;">
        <svg width="36" height="36"><use href="#i-check"/></svg>
      </div>
      <h3 style="margin: 0 0 8px; font-size: 22px; letter-spacing: -0.01em;">Password berhasil direset</h3>
      <p class="muted" style="margin: 0 0 24px;">Anda sekarang bisa masuk dengan password baru Anda.</p>
      <a href="login.html" class="btn lg" style="display:inline-block;">Masuk ke Akun →</a>
    </div>

    <p class="small muted" style="text-align:center; margin-top: 32px; line-height: 1.6;">
      Butuh bantuan? <a href="contact.html" style="color:var(--accent); font-weight:600;">Hubungi support →</a>
    </p>
  </main>
</div>'''
    return head + body + chrome_close()


# ============================================================
# 3. email-verify.html
# ============================================================
def page_email_verify():
    head = chrome('Verifikasi Email — Resonansi', '', 'email-verify.html', '''<style>
    body { background: linear-gradient(180deg, #f5f6f8 0%, #fff 100%); }
    .verify-wrap { min-height: 100vh; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 40px 24px; }
    .verify-card { max-width: 540px; width: 100%; background: #fff; border: 1px solid var(--line); border-radius: 20px; box-shadow: 0 8px 32px rgba(15,30,60,0.08); padding: 48px 40px; text-align: center; }
    .verify-icon { width: 96px; height: 96px; border-radius: 50%; background: var(--accent-soft); color: var(--accent); display: inline-flex; align-items: center; justify-content: center; margin-bottom: 24px; position: relative; }
    .verify-icon::after { content: ""; position: absolute; inset: -8px; border-radius: 50%; border: 2px solid var(--accent); opacity: 0.18; }
    .verify-card h1 { font-size: 30px; letter-spacing: -0.02em; margin: 0 0 12px; }
    .verify-card .lead { color: var(--muted); font-size: 15.5px; line-height: 1.6; margin: 0 0 28px; }
    .verify-card .email-badge { display: inline-flex; align-items: center; gap: 8px; padding: 8px 14px; background: var(--grey-50); border-radius: 999px; font-size: 13.5px; font-weight: 600; color: var(--ink); margin-bottom: 28px; }
  </style>''')
    body = '''<div class="verify-wrap">

  <a class="logo" href="index.html" style="margin-bottom: 32px;">RESONANSI</a>

  <div class="verify-card">
    <div class="verify-icon">
      <svg width="44" height="44"><use href="#i-mail"/></svg>
    </div>
    <h1>Periksa email Anda</h1>
    <p class="lead">Kami sudah kirim link verifikasi ke email Anda. Klik link di email untuk mengaktifkan akun.</p>

    <div class="email-badge">
      <svg width="14" height="14"><use href="#i-mail"/></svg>
      marketing@falconpictures.id
    </div>

    <div style="display: flex; flex-direction: column; gap: 10px; margin-bottom: 24px;">
      <a href="client/dashboard.html" class="btn lg" style="display:inline-flex; justify-content:center;">Sudah verifikasi? Lanjut ke Dashboard →</a>
      <button class="btn neutral" onclick="alert('Email verifikasi sudah dikirim ulang. Periksa kotak masuk Anda.');">Kirim Ulang Email</button>
    </div>

    <div style="padding: 18px 20px; background: var(--grey-50); border-radius: 12px; text-align: left;">
      <div style="font-size:13.5px; font-weight: 600; color: var(--ink); margin-bottom: 6px;">Tidak menerima email?</div>
      <ul style="margin: 0; padding-left: 20px; font-size: 13px; color: var(--muted); line-height: 1.7;">
        <li>Periksa folder <strong>Spam</strong> atau <strong>Promosi</strong></li>
        <li>Pastikan email <strong>marketing@falconpictures.id</strong> benar</li>
        <li>Tunggu 1–2 menit, email kadang delay</li>
        <li>Masih bermasalah? <a href="contact.html" style="color:var(--accent); font-weight:600;">Hubungi support</a></li>
      </ul>
    </div>
  </div>

  <p class="small muted" style="margin-top: 32px;">
    Salah email? <a href="signup.html" style="color: var(--accent); font-weight: 600;">Daftar ulang →</a>
  </p>
</div>'''
    return head + body + chrome_close()


# ============================================================
# 4. 404.html
# ============================================================
def page_404():
    head = chrome('Halaman Tidak Ditemukan — Resonansi', '', '404.html', '''<style>
    body { background: #fff; }
    .nf-wrap { min-height: 100vh; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 40px 24px; text-align: center; }
    .nf-illust { font-family: var(--font-display); font-size: 180px; font-weight: 800; line-height: 1; letter-spacing: -0.04em; background: linear-gradient(135deg, #0B5FE0 0%, #FFB400 100%); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 16px; }
    .nf-card { max-width: 720px; }
    .nf-card h1 { font-size: 36px; letter-spacing: -0.02em; margin: 0 0 12px; }
    .nf-card .lead { color: var(--muted); font-size: 17px; line-height: 1.6; margin: 0 0 32px; }
    .nf-links { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin-top: 40px; max-width: 720px; width: 100%; }
    .nf-link { padding: 20px; background: #fff; border: 1px solid var(--line); border-radius: 14px; text-decoration: none; color: var(--ink); transition: all 0.15s; }
    .nf-link:hover { border-color: var(--accent); box-shadow: 0 4px 12px rgba(11,95,224,0.08); transform: translateY(-2px); }
    .nf-link strong { display: block; font-size: 15px; margin-bottom: 4px; }
    .nf-link span { font-size: 13px; color: var(--muted); }
  </style>''')
    body = '''<div class="nf-wrap">

  <a class="logo" href="index.html" style="margin-bottom: 40px;">RESONANSI</a>

  <div class="nf-illust">404</div>

  <div class="nf-card">
    <h1>Hmm, halaman ini hilang dari peta.</h1>
    <p class="lead">URL yang Anda buka tidak ada atau sudah dipindahkan. Tidak masalah — banyak hal menarik di Resonansi.</p>

    <div class="row" style="justify-content: center; gap: 12px;">
      <a href="index.html" class="btn lg">← Kembali ke Beranda</a>
      <a href="contact.html" class="btn neutral lg">Hubungi Support</a>
    </div>
  </div>

  <div class="nf-links">
    <a href="index.html" class="nf-link">
      <strong>🏠 Homepage</strong>
      <span>Mulai dari halaman utama</span>
    </a>
    <a href="solutions.html" class="nf-link">
      <strong>💡 Solusi</strong>
      <span>Film, Politik, Brand, NGO</span>
    </a>
    <a href="contact.html" class="nf-link">
      <strong>✉ Kontak</strong>
      <span>Bicarakan project Anda</span>
    </a>
  </div>

  <p class="small muted" style="margin-top: 48px;">
    Kode error: 404 · Jika Anda yakin halaman ini seharusnya ada, <a href="contact.html" style="color: var(--accent); font-weight: 600;">beri tahu kami</a>.
  </p>
</div>'''
    return head + body + chrome_close()


# ============================================================
# 5. client/brief-detail.html
# ============================================================
def page_brief_detail():
    extra = '''<style>
    .brief-detail-grid { display: grid; grid-template-columns: 1fr 320px; gap: 24px; align-items: start; }
    .brief-section { background: #fff; border: 1px solid var(--line); border-radius: 14px; padding: 24px; margin-bottom: 16px; box-shadow: var(--shadow-1); }
    .brief-section h3 { font-family: var(--font-display); font-size: 16px; margin: 0 0 14px; letter-spacing: -0.01em; }
    .brief-meta-row { display: grid; grid-template-columns: repeat(4, 1fr); gap: 18px; padding: 18px 0; border-bottom: 1px solid var(--line); }
    .brief-meta-row:last-child { border: 0; padding-bottom: 0; }
    .brief-meta-cell .label { font-size: 11.5px; text-transform: uppercase; letter-spacing: 0.06em; color: var(--muted); margin-bottom: 4px; }
    .brief-meta-cell .value { font-size: 14px; font-weight: 600; color: var(--ink); }
    .deliv-row { display: flex; align-items: center; gap: 12px; padding: 12px 0; border-bottom: 1px solid var(--grey-100); }
    .deliv-row:last-child { border: 0; padding-bottom: 0; }
    .deliv-row .num { width: 28px; height: 28px; border-radius: 50%; background: var(--accent-soft); color: var(--accent); display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 12px; flex-shrink: 0; }
    .compliance-row { display: flex; align-items: center; gap: 10px; padding: 10px 0; font-size: 13.5px; }
    .compliance-row .ico { width: 22px; height: 22px; border-radius: 50%; background: #d8f0e3; color: #0a6a3a; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
    .sticky-rail { position: sticky; top: 24px; }
    .breadcrumb { font-size: 12.5px; color: var(--muted); margin-bottom: 8px; }
    .breadcrumb a { color: var(--muted); text-decoration: none; }
    .breadcrumb a:hover { color: var(--accent); }
  </style>'''
    head = chrome('Brief Detail — Resonansi', '../', 'client/brief-detail.html', extra)
    body = '''<section class="screen">
  <div class="frame">
    <div class="app-shell">
      <div class="app-sidebar">
        <a class="nav-item" href="../client/dashboard.html"><svg class="ico" width="18" height="18"><use href="#i-home"/></svg> Home</a>
        <a class="nav-item" href="../client/brief.html"><svg class="ico" width="18" height="18"><use href="#i-edit"/></svg> Buat Brief</a>
        <a class="nav-item active" href="../client/campaigns.html"><svg class="ico" width="18" height="18"><use href="#i-megaphone"/></svg> Kampanye</a>
        <a class="nav-item" href="../client/library.html"><svg class="ico" width="18" height="18"><use href="#i-bookmark"/></svg> Advocate Library</a>
        <a class="nav-item" href="../client/analytics.html"><svg class="ico" width="18" height="18"><use href="#i-chart"/></svg> Analytics</a>
        <a class="nav-item" href="../client/billing.html"><svg class="ico" width="18" height="18"><use href="#i-card"/></svg> Billing</a>
        <a class="nav-item" href="../client/settings.html"><svg class="ico" width="18" height="18"><use href="#i-users"/></svg> Team</a>
        <a class="nav-item" href="../client/settings.html"><svg class="ico" width="18" height="18"><use href="#i-settings"/></svg> Settings</a>
      </div>

      <div class="app-main">
        <div class="breadcrumb">
          <a href="../client/dashboard.html">Dashboard</a> · <a href="../client/campaigns.html">Kampanye</a> · <span style="color: var(--ink);">Film X — Opening Weekend</span>
        </div>

        <div class="row" style="align-items: flex-start; margin-bottom: 24px;">
          <div>
            <div class="row-tight" style="margin-bottom: 8px;">
              <span class="pill film">Film</span>
              <span class="pill" style="background:#d8f0e3; color:#0a6a3a; border-color:#a9d9bf;">● Live</span>
              <span class="small muted">Brief ID: BRF-2026-0421</span>
            </div>
            <h1 style="margin: 0; font-size: 28px; letter-spacing: -0.02em;">Film X — Opening Weekend Mobilization</h1>
            <p class="muted small mb-0" style="margin-top:6px;">Dipublikasi 14 Apr 2026 · Closing 20 Apr 2026 · 6 hari tersisa</p>
          </div>
          <div class="right row-tight">
            <a href="../client/brief.html" class="btn neutral">Edit Brief</a>
            <a href="../client/live-campaign.html" class="btn">View Live Campaign →</a>
          </div>
        </div>

        <div class="brief-detail-grid">
          <div>
            <!-- Metadata -->
            <div class="brief-section">
              <h3>Metadata Brief</h3>
              <div class="brief-meta-row">
                <div class="brief-meta-cell"><div class="label">Dibuat</div><div class="value">14 Apr 2026</div></div>
                <div class="brief-meta-cell"><div class="label">Vertikal</div><div class="value">Film · Hiburan</div></div>
                <div class="brief-meta-cell"><div class="label">Budget</div><div class="value">Rp 480.000.000</div></div>
                <div class="brief-meta-cell"><div class="label">Periode</div><div class="value">14–21 Apr 2026</div></div>
              </div>
              <div class="brief-meta-row">
                <div class="brief-meta-cell"><div class="label">Tujuan</div><div class="value">Maksimalkan okupansi opening weekend (+30%)</div></div>
                <div class="brief-meta-cell"><div class="label">Type</div><div class="value">Burst (7 hari)</div></div>
                <div class="brief-meta-cell"><div class="label">Estimated Reach</div><div class="value">5.5 M – 8 M</div></div>
                <div class="brief-meta-cell"><div class="label">Disclosure</div><div class="value">#KerjasamaResonansi (wajib)</div></div>
              </div>
            </div>

            <!-- Target Audiens -->
            <div class="brief-section">
              <h3>Target Audiens</h3>
              <div class="grid-2" style="gap: 20px;">
                <div>
                  <div class="field-label">Demografi</div>
                  <ul style="margin: 4px 0 0; padding-left: 20px; font-size: 13.5px; line-height: 1.8;">
                    <li>Umur 18–35 tahun</li>
                    <li>Pria & Wanita (60% W)</li>
                    <li>SES B–A, kelas mahasiswa & young professional</li>
                    <li>Aktif di TikTok, Instagram Reels</li>
                  </ul>
                </div>
                <div>
                  <div class="field-label">Geografi</div>
                  <ul style="margin: 4px 0 0; padding-left: 20px; font-size: 13.5px; line-height: 1.8;">
                    <li>Jabodetabek (40%)</li>
                    <li>Bandung, Surabaya, Medan (30%)</li>
                    <li>Yogya, Semarang, Makassar (20%)</li>
                    <li>Tier 3+ kota (10%)</li>
                  </ul>
                </div>
              </div>
            </div>

            <!-- Deliverables -->
            <div class="brief-section">
              <h3>Deliverables (per Advocate)</h3>
              <div class="deliv-row">
                <div class="num">1</div>
                <div style="flex:1;"><strong>1× TikTok Reaction Video</strong><br><span class="small muted">15–30 detik, vertical 9:16, original audio</span></div>
                <span class="pill" style="background: var(--accent-soft); color: var(--accent); border-color: #c8d8f7;">Wajib</span>
              </div>
              <div class="deliv-row">
                <div class="num">2</div>
                <div style="flex:1;"><strong>1× Instagram Reel</strong><br><span class="small muted">Bisa cross-post dari TikTok</span></div>
                <span class="pill" style="background: var(--accent-soft); color: var(--accent); border-color: #c8d8f7;">Wajib</span>
              </div>
              <div class="deliv-row">
                <div class="num">3</div>
                <div style="flex:1;"><strong>3× IG Story / day, 3 hari berturut</strong><br><span class="small muted">Behind-the-scene, reaction, sticker poll</span></div>
                <span class="pill" style="background: var(--accent-soft); color: var(--accent); border-color: #c8d8f7;">Wajib</span>
              </div>
              <div class="deliv-row">
                <div class="num">4</div>
                <div style="flex:1;"><strong>1× YouTube Short (opsional)</strong><br><span class="small muted">Untuk advocate dengan YouTube ≥ 10K subs</span></div>
                <span class="pill warn">Opsional</span>
              </div>
            </div>

            <!-- Timeline -->
            <div class="brief-section">
              <h3>Timeline</h3>
              <div style="display: grid; grid-template-columns: 100px 1fr; row-gap: 14px; font-size: 13.5px;">
                <div class="muted">14 Apr</div><div><strong>Brief publish.</strong> Open application untuk advocate Tier 1–4.</div>
                <div class="muted">15 Apr</div><div><strong>Shortlist 500 advocate</strong> dari ~1.200 aplikan. Review oleh tim Falcon Pictures.</div>
                <div class="muted">16 Apr</div><div><strong>Brief delivery</strong> + access ke screening private untuk Tier 1.</div>
                <div class="muted">17–18 Apr</div><div><strong>Content production</strong> dan upload draft ke approval queue.</div>
                <div class="muted">19 Apr</div><div><strong>Approval deadline 18:00.</strong> Konten live 20 Apr 00:00.</div>
                <div class="muted">20–21 Apr</div><div><strong>Opening weekend</strong> — peak window. Monitor sentiment & spike alerts.</div>
              </div>
            </div>

            <!-- Content Guideline -->
            <div class="brief-section">
              <h3>Content Guideline</h3>
              <p style="font-size: 13.5px; line-height: 1.7; margin: 0;">
                Reaction <strong>jujur dan autentik</strong> — bukan endorsement. Boleh disukai, boleh dikritisi (asal konstruktif). Wajib menyertakan: judul film, jam tayang/bioskop, hashtag <code style="background: var(--grey-100); padding: 2px 6px; border-radius: 4px;">#FilmX2026</code>, dan disclosure <code style="background: var(--grey-100); padding: 2px 6px; border-radius: 4px;">#KerjasamaResonansi</code>. <strong>Dilarang:</strong> spoiler di luar trailer, mention kompetitor, bahasa kasar/SARA.
              </p>
            </div>

            <!-- Compliance -->
            <div class="brief-section">
              <h3>Compliance Status</h3>
              <div class="compliance-row"><div class="ico"><svg width="12" height="12"><use href="#i-check"/></svg></div> Disclosure tag otomatis dilampirkan ke semua konten</div>
              <div class="compliance-row"><div class="ico"><svg width="12" height="12"><use href="#i-check"/></svg></div> KYC advocate sudah diverifikasi (387/387 advocate aktif)</div>
              <div class="compliance-row"><div class="ico"><svg width="12" height="12"><use href="#i-check"/></svg></div> Hashtag disclosure di-render saat upload</div>
              <div class="compliance-row"><div class="ico"><svg width="12" height="12"><use href="#i-check"/></svg></div> Audit trail otomatis tercatat (immutable log)</div>
            </div>
          </div>

          <!-- Sticky right rail -->
          <aside class="sticky-rail">
            <div class="brief-section" style="margin-bottom: 14px;">
              <h3 style="margin-bottom: 16px;">Aksi Cepat</h3>
              <div style="display: flex; flex-direction: column; gap: 10px;">
                <a href="../client/brief.html" class="btn neutral" style="justify-content: center;">✎ Edit Brief</a>
                <a href="../client/shortlist.html" class="btn neutral" style="justify-content: center;">View Shortlist (247)</a>
                <a href="../client/advocate-detail.html" class="btn neutral" style="justify-content: center;">View Advocate Detail</a>
                <a href="../client/live-campaign.html" class="btn" style="justify-content: center;">View Live Campaign →</a>
              </div>
            </div>

            <div class="brief-section">
              <h3 style="margin-bottom: 12px;">Performance So Far</h3>
              <div style="display: flex; flex-direction: column; gap: 12px;">
                <div>
                  <div class="small muted">Advocate Confirmed</div>
                  <div style="font-family: var(--font-display); font-size: 24px; font-weight: 700;">387 / 500</div>
                </div>
                <div>
                  <div class="small muted">Konten Published</div>
                  <div style="font-family: var(--font-display); font-size: 24px; font-weight: 700;">312</div>
                </div>
                <div>
                  <div class="small muted">Reach</div>
                  <div style="font-family: var(--font-display); font-size: 24px; font-weight: 700;">3.2 M</div>
                </div>
                <div>
                  <div class="small muted">Sentiment</div>
                  <div style="font-family: var(--font-display); font-size: 24px; font-weight: 700; color: #16a34a;">+0.71</div>
                </div>
              </div>
            </div>
          </aside>
        </div>

      </div>
    </div>
  </div>
</section>'''
    return head + body + chrome_close()


# ============================================================
# 6. advocate/apply-brief.html
# ============================================================
def page_apply_brief():
    extra = '''<style>
    .apply-wrap { max-width: 480px; margin: 0 auto; padding: 24px 20px 80px; }
    .apply-header { padding: 16px 0 20px; display: flex; align-items: center; justify-content: space-between; }
    .apply-card { background: #fff; border: 1px solid var(--line); border-radius: 14px; padding: 20px; margin-bottom: 16px; box-shadow: var(--shadow-1); }
    .apply-card h3 { font-family: var(--font-display); font-size: 15px; margin: 0 0 10px; }
    .apply-card .label { font-size: 11.5px; text-transform: uppercase; letter-spacing: 0.05em; color: var(--muted); margin-bottom: 4px; }
    .apply-card textarea { width: 100%; padding: 12px 14px; border: 1px solid var(--line); border-radius: 10px; font-family: var(--font-body); font-size: 14px; resize: vertical; min-height: 100px; background: #fff; }
    .apply-card textarea:focus { outline: none; border-color: var(--accent); box-shadow: 0 0 0 4px rgba(11,95,224,0.08); }
    .apply-card input[type="number"], .apply-card input[type="text"], .apply-card select { width: 100%; padding: 12px 14px; border: 1px solid var(--line); border-radius: 10px; font-family: var(--font-body); font-size: 14px; background: #fff; }
    .apply-card input:focus, .apply-card select:focus { outline: none; border-color: var(--accent); box-shadow: 0 0 0 4px rgba(11,95,224,0.08); }
    .range-row { display: flex; align-items: center; gap: 12px; font-size: 13px; }
    .range-row input[type="range"] { flex: 1; accent-color: var(--accent); }
    .fit-row { display: flex; align-items: center; gap: 10px; padding: 10px 12px; background: var(--accent-soft); border-radius: 10px; margin-bottom: 6px; font-size: 13px; }
    .fit-row .ico { width: 20px; height: 20px; border-radius: 50%; background: var(--accent); color: #fff; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
    .sticky-submit { position: sticky; bottom: 0; background: #fff; padding: 14px 20px; border-top: 1px solid var(--line); margin: 0 -20px -80px; box-shadow: 0 -4px 12px rgba(0,0,0,0.04); }
  </style>'''
    head = chrome('Apply Brief — Resonansi Advocate', '../', 'advocate/apply-brief.html', extra)
    body = '''<div class="apply-wrap">

  <div class="apply-header">
    <a href="../advocate/campaigns.html" class="btn ghost small" style="padding-left: 0;">← Kembali</a>
    <strong style="font-family: var(--font-display); font-size: 15px;">Apply ke Brief</strong>
    <div style="width: 60px;"></div>
  </div>

  <!-- Brief summary -->
  <div class="apply-card">
    <div class="row-tight" style="margin-bottom: 8px;">
      <span class="pill film">Film</span>
      <span class="small muted">BRF-2026-0421</span>
    </div>
    <h3 style="font-size: 17px; margin-bottom: 8px;">Film X — Opening Weekend</h3>
    <p class="small muted" style="margin: 0 0 14px; line-height: 1.55;">
      Reaction film, mobilisasi opening weekend. Closing 20 Apr 2026.
    </p>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; padding-top: 14px; border-top: 1px solid var(--grey-100);">
      <div><div class="label">Tarif Default</div><div style="font-weight: 700;">Rp 850.000</div></div>
      <div><div class="label">Deadline</div><div style="font-weight: 700;">19 Apr · 18:00</div></div>
      <div><div class="label">Periode</div><div style="font-weight: 700;">14–21 Apr</div></div>
      <div><div class="label">Slot Tersisa</div><div style="font-weight: 700;">113 / 500</div></div>
    </div>
  </div>

  <!-- Fit indicator -->
  <div class="apply-card" style="background: linear-gradient(135deg, #e8f0ff 0%, #fff 100%); border-color: #c8d8f7;">
    <h3>Mengapa Saya Cocok</h3>
    <div class="fit-row"><div class="ico"><svg width="11" height="11"><use href="#i-check"/></svg></div> Niche cinephile + audiens muda 18–28</div>
    <div class="fit-row"><div class="ico"><svg width="11" height="11"><use href="#i-check"/></svg></div> Score Match 87% · ER history 5.8%</div>
    <div class="fit-row"><div class="ico"><svg width="11" height="11"><use href="#i-check"/></svg></div> Lokasi Jakarta — pas dengan target Jabodetabek</div>
    <p class="small muted" style="margin: 12px 0 0; line-height: 1.55;">
      Sistem cocokkan profil Anda dengan kriteria brief. Klien akan lihat ini saat shortlisting.
    </p>
  </div>

  <!-- Deliverable expectations -->
  <div class="apply-card">
    <h3>Yang Diharapkan</h3>
    <ul style="margin: 0; padding-left: 20px; font-size: 13.5px; line-height: 1.8;">
      <li>1× TikTok Reaction (15–30s)</li>
      <li>1× Instagram Reel (bisa cross-post)</li>
      <li>3× IG Story / day selama 3 hari</li>
      <li>Tag wajib: <code style="background: var(--grey-100); padding: 1px 5px; border-radius: 4px;">#FilmX2026</code> + <code style="background: var(--grey-100); padding: 1px 5px; border-radius: 4px;">#KerjasamaResonansi</code></li>
    </ul>
  </div>

  <!-- Pesan -->
  <div class="apply-card">
    <h3>Pesan untuk Klien (Opsional)</h3>
    <textarea placeholder="Cerita singkat kenapa kamu cocok dan ide content angle-mu...">Saya punya audiens cinephile muda 18–28 yang aktif di TikTok. Sudah review 3 film dalam 30 hari terakhir dengan ER rata-rata 6%. Untuk Film X, saya rencana angle "reaction tanpa spoiler" + behind-the-scene experience nonton.</textarea>
    <div class="small muted" style="margin-top: 6px;">Maksimal 280 karakter. Klien punya 24 jam untuk respon.</div>
  </div>

  <!-- Custom tarif -->
  <div class="apply-card">
    <h3>Custom Tarif</h3>
    <div class="label" style="margin-bottom: 6px;">Tarif diajukan (default Rp 850.000)</div>
    <div class="range-row" style="margin-bottom: 10px;">
      <span class="muted">Rp 600k</span>
      <input type="range" min="600000" max="1500000" step="50000" value="900000" oninput="document.getElementById('rateVal').textContent='Rp ' + (this.value/1000).toLocaleString('id') + 'k';">
      <span class="muted">Rp 1.5jt</span>
    </div>
    <div style="text-align: center; font-family: var(--font-display); font-size: 22px; font-weight: 700; color: var(--accent);" id="rateVal">Rp 900k</div>
    <div class="small muted center" style="margin-top: 4px;">+6% di atas default. Klien lebih sering accept jika kamu di range ini.</div>
  </div>

  <!-- Turnaround -->
  <div class="apply-card">
    <h3>Turnaround Time</h3>
    <div class="label">Berapa lama kamu butuh untuk produksi konten?</div>
    <select style="margin-top: 6px;">
      <option>24 jam (rush — biasa untuk burst)</option>
      <option selected>48 jam (standar)</option>
      <option>72 jam (santai)</option>
      <option>Custom — lihat brief</option>
    </select>
  </div>

  <!-- Terms acknowledgement -->
  <div class="apply-card">
    <h3>Persetujuan</h3>
    <label style="display: flex; gap: 10px; font-size: 13px; cursor: pointer;">
      <input type="checkbox" checked style="accent-color: var(--accent); margin-top: 3px;">
      <span>Saya setuju <strong>compliance Resonansi</strong> — tag disclosure, no spoiler di luar trailer, no bahasa SARA.</span>
    </label>
    <label style="display: flex; gap: 10px; font-size: 13px; cursor: pointer; margin-top: 10px;">
      <input type="checkbox" checked style="accent-color: var(--accent); margin-top: 3px;">
      <span>Saya memahami pembayaran rilis <strong>setelah konten verified</strong> (max 7 hari setelah publish).</span>
    </label>
  </div>

  <div class="sticky-submit">
    <a href="../advocate/campaigns.html#applied" class="btn lg" style="width: 100%; justify-content: center; display: inline-flex;">
      Submit Aplikasi · Rp 900k →
    </a>
    <div class="small muted center" style="margin-top: 6px;">Klien biasanya respon dalam 24 jam.</div>
  </div>
</div>'''
    return head + body + chrome_close()


print('Module loaded. Run main() to write pages.')


# ============================================================
# WRITER
# ============================================================
def main():
    """Write the 15 pages. Drawer update is done separately."""
    pages = [
        ('forgot-password.html', page_forgot_password),
        ('reset-password.html', page_reset_password),
        ('email-verify.html', page_email_verify),
        ('404.html', page_404),
        ('client/brief-detail.html', page_brief_detail),
        ('advocate/apply-brief.html', page_apply_brief),
    ]
    for rel, fn in pages:
        write_page(rel, fn())
    print(f'\n  → wrote {len(pages)} pages (batch 1)')


if __name__ == '__main__':
    main()
