"""
Inject the AUTH group (Login + Sign Up) at the top of every page's demo drawer,
so users can reach those pages from anywhere in the demo.

Run: python3 /Users/haimac/buzzer/site/_inject_auth_drawer.py
"""
import os
import re

SITE_DIR = '/Users/haimac/buzzer/site'

# Find the first <div class="demo-group"> after <div class="demo-drawer-body">
# and insert our AUTH group before it (if not already present).

PATTERN = re.compile(
    r'(<div class="demo-drawer-body">\s*)(<div class="demo-group">)',
    re.DOTALL
)

def build_auth_group(depth):
    prefix = '../' * depth
    return (
        '<div class="demo-group">\n'
        '      <div class="demo-group-label">⚙ AUTH</div>\n'
        f'      <a class="drawer-link" href="{prefix}login.html">Masuk (Login)</a>\n'
        f'      <a class="drawer-link" href="{prefix}signup.html">Daftar (Sign Up)</a>\n'
        '    </div>\n\n    '
    )

def process_file(path):
    rel = os.path.relpath(path, SITE_DIR)
    depth = rel.count(os.sep)

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already has AUTH group
    if 'demo-group-label">⚙ AUTH<' in content or 'AUTH</div>' in content:
        return 0

    auth_group = build_auth_group(depth)
    new_content, n = PATTERN.subn(
        lambda m: m.group(1) + auth_group + m.group(2),
        content,
        count=1
    )
    if n > 0:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
    return n


def main():
    total = 0
    for root, _, files in os.walk(SITE_DIR):
        for fn in files:
            if not fn.endswith('.html'):
                continue
            # Skip auth pages (already have it inline)
            if fn in ('login.html', 'signup.html'):
                continue
            path = os.path.join(root, fn)
            n = process_file(path)
            total += n
            if n > 0:
                print(f'  {os.path.relpath(path, SITE_DIR):<48} → injected AUTH group')
    print(f'\nDone. Injected AUTH group into {total} files.')


if __name__ == '__main__':
    main()
