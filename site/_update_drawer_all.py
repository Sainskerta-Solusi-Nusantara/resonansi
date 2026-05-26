"""
Update the demo drawer body and the demo-toggle page count
across every HTML file in the site.

Run: python3 /Users/haimac/buzzer/site/_update_drawer_all.py
"""
import os
import re
import sys

sys.path.insert(0, '/Users/haimac/buzzer/site')
from _build_new_pages import drawer_body, TOTAL_PAGES

SITE_DIR = '/Users/haimac/buzzer/site'


def get_active_href(rel_path):
    """Given a relative path like 'client/dashboard.html', return the href that
    matches what drawer_body uses to mark active."""
    # drawer_body uses paths like 'login.html' or 'client/dashboard.html'
    return rel_path.replace(os.sep, '/')


def update_file(path):
    rel = os.path.relpath(path, SITE_DIR)
    depth = rel.count(os.sep)
    prefix = '../' * depth
    active = get_active_href(rel)

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1) Replace drawer body content
    # Pattern: <div class="demo-drawer-body"> ... </div>\s*</aside>
    new_body = drawer_body(prefix, active)
    new_drawer = f'<div class="demo-drawer-body">\n    {new_body}\n  </div>\n</aside>'

    pattern = re.compile(
        r'<div class="demo-drawer-body">.*?</div>\s*</aside>',
        re.DOTALL
    )
    content, n_drawer = pattern.subn(new_drawer, content, count=1)

    # 2) Update page count: "Demo · NN halaman"
    content, n_count = re.subn(
        r'Demo · \d+ halaman',
        f'Demo · {TOTAL_PAGES} halaman',
        content
    )

    if content != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'  ✓ {rel:<45} drawer={n_drawer} count={n_count}')
        return True
    return False


def main():
    total = 0
    for root, _, files in os.walk(SITE_DIR):
        # Skip non-source dirs
        if any(x in root for x in ('node_modules', '.git')):
            continue
        for fn in files:
            if not fn.endswith('.html'):
                continue
            path = os.path.join(root, fn)
            if update_file(path):
                total += 1
    print(f'\nDone. Updated drawer in {total} files.')


if __name__ == '__main__':
    main()
