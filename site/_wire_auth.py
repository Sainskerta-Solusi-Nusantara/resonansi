"""
Wire up auth CTAs across all marketing pages:
- "Masuk" buttons       → login.html
- "Mulai Gratis", "Daftar Gratis", "Daftar Sebagai Advocate",
  "Daftar Sekarang", "Coba Pro 14 Hari" → signup.html
- "Mulai Sekarang", "Coba Gratis" → signup.html

Converts `<button class="btn ...">Label</button>` into
`<a class="btn ..." href="signup.html">Label</a>` so navigation works.

Run: python3 /Users/haimac/buzzer/site/_wire_auth.py
"""
import os
import re

SITE_DIR = '/Users/haimac/buzzer/site'

# (label_pattern, target) pairs
# label_pattern is a regex (case-insensitive substring match on inner text)
ROUTES = [
    (r'^Masuk$',                                   'login.html'),
    (r'^Masuk →$',                                 'login.html'),
    (r'^Mulai Gratis →?$',                         'signup.html'),
    (r'^Mulai Brief Gratis →?$',                   'signup.html'),
    (r'^Daftar Gratis( →?| \(8 menit\) →?)?$',     'signup.html'),
    (r'^Daftar Sebagai Advocate →?$',              'signup.html'),
    (r'^Daftar Sekarang →?$',                      'signup.html'),
    (r'^Coba Pro 14 Hari$',                        'signup.html'),
    (r'^Mulai Sekarang$',                          'signup.html'),
    (r'^Buat Brief Pertamamu$',                    'signup.html'),
    (r'^\+ Buat Brief$',                           'signup.html'),
    (r'^\+ Buat Brief Kampanye$',                  'signup.html'),
]

# Pattern: <button class="btn ANY"...>LABEL</button>
# Captures: class attribute value, inner label text
BTN_PATTERN = re.compile(
    r'<button\s+class="([^"]*?\bbtn\b[^"]*)"([^>]*)>([^<]+?)</button>',
    re.DOTALL
)

def get_target(label):
    label_clean = label.strip()
    for pattern, target in ROUTES:
        if re.match(pattern, label_clean, re.IGNORECASE):
            return target
    return None


def resolve_href(target, depth):
    """Add ../ for subfolder pages."""
    prefix = '../' * depth
    return prefix + target


def transform(match, depth):
    cls = match.group(1)
    extra_attrs = match.group(2)
    label = match.group(3)
    target = get_target(label)
    if not target:
        return match.group(0)  # unchanged
    href = resolve_href(target, depth)
    # Strip onclick from extra attrs (don't want both onclick and href)
    extra_attrs = re.sub(r'\s*onclick="[^"]*"', '', extra_attrs)
    return f'<a class="{cls}" href="{href}"{extra_attrs}>{label}</a>'


def process_file(path):
    rel = os.path.relpath(path, SITE_DIR)
    depth = rel.count(os.sep)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    replaced = 0
    def _sub(m):
        nonlocal replaced
        result = transform(m, depth)
        if result != m.group(0):
            replaced += 1
        return result

    new_content = BTN_PATTERN.sub(_sub, content)

    if replaced > 0:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
    return replaced


def main():
    total_files = 0
    total_wired = 0
    for root, _, files in os.walk(SITE_DIR):
        for fn in files:
            if not fn.endswith('.html'):
                continue
            # Skip auth pages themselves
            if fn in ('login.html', 'signup.html'):
                continue
            path = os.path.join(root, fn)
            count = process_file(path)
            total_files += 1
            total_wired += count
            if count > 0:
                print(f'  {os.path.relpath(path, SITE_DIR):<48} → wired {count} CTA(s)')
    print(f'\nDone. Scanned {total_files} files, wired {total_wired} CTA(s).')


if __name__ == '__main__':
    main()
