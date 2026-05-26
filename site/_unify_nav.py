"""
Unify the top web-header navigation across all marketing pages in /site/.
Each page now shares the same nav menu with the same labels, ordering,
and href targets. The `.active` class is applied based on the page filename.

Dashboard pages (client/, advocate/) use sidebar instead of web-nav, so they're
unaffected by this script (web-nav doesn't appear in those screens).

Run: python3 /Users/haimac/buzzer/site/_unify_nav.py
"""
import os
import re

SITE_DIR = '/Users/haimac/buzzer/site'

NAV_ITEMS = [
    ('Cara Kerja',     'how-it-works-client.html'),
    ('Untuk Advocate', 'how-it-works-advocate.html'),
    ('Solusi',         'solutions.html'),
    ('Harga',          'pricing.html'),
    ('Tentang',        'about.html'),
    ('Kontak',         'contact.html'),
]

# Which nav item is "active" for each page (matched by basename of file)
ACTIVE_MAP = {
    'index.html':                    None,
    'how-it-works-client.html':      'how-it-works-client.html',
    'how-it-works-advocate.html':    'how-it-works-advocate.html',
    'solutions.html':                'solutions.html',
    'pricing.html':                  'pricing.html',
    'about.html':                    'about.html',
    'contact.html':                  'contact.html',
    'trust.html':                    None,
    'faq.html':                      None,
    'film.html':                     'solutions.html',
    'politik.html':                  'solutions.html',
    'browse.html':                   'solutions.html',
    'design-system.html':            None,
}

PATTERN = re.compile(r'<div class="web-nav">.*?</div>', re.DOTALL)


def build_nav(active_target, depth):
    """Build unified nav with relative paths based on file depth from /site/.
    depth=0 → root pages (e.g., index.html), use direct paths.
    depth=1 → subfolder pages (client/, advocate/), use ../ prefix.
    """
    prefix = '../' * depth
    items_html = []
    for label, href in NAV_ITEMS:
        is_active = ' active' if href == active_target else ''
        items_html.append(
            f'        <a class="item{is_active}" href="{prefix}{href}">{label}</a>'
        )
    return '<div class="web-nav">\n' + '\n'.join(items_html) + '\n      </div>'


def process_file(path):
    """Replace the web-nav block. Returns count of replacements made."""
    rel = os.path.relpath(path, SITE_DIR)
    depth = rel.count(os.sep)
    basename = os.path.basename(path)
    active_target = ACTIVE_MAP.get(basename)
    new_nav = build_nav(active_target, depth)

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content, count = PATTERN.subn(new_nav, content)
    if count > 0:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
    return count


def main():
    total_files = 0
    total_replaced = 0
    for root, _, files in os.walk(SITE_DIR):
        for fn in files:
            if not fn.endswith('.html'):
                continue
            path = os.path.join(root, fn)
            count = process_file(path)
            total_files += 1
            total_replaced += count
            status = f'replaced {count} nav' if count else 'no web-nav (sidebar page)'
            print(f'  {os.path.relpath(path, SITE_DIR):<48} → {status}')
    print(f'\nDone. Scanned {total_files} files, replaced web-nav in {total_replaced} block(s).')


if __name__ == '__main__':
    main()
