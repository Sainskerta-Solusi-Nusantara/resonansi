"""Wire mega-footer links across all HTML files to point to new pages."""
import os
import re

SITE_DIR = '/Users/haimac/buzzer/site'

# Replacements applied only inside mega-footer block
ROOT_REPLACEMENTS = [
    # Studi Kasus → case-study-detail
    (r'<li><a href="solutions\.html">Studi Kasus</a></li>',
     '<li><a href="case-study-detail.html">Studi Kasus</a></li>'),
    # Blog → blog-detail
    (r'<li><a href="faq\.html">Blog</a></li>',
     '<li><a href="blog-detail.html">Blog</a></li>'),
    # Karir → career
    (r'<li><a href="index\.html">Karir</a></li>',
     '<li><a href="career.html">Karir</a></li>'),
    # Press / Press Kit → press
    (r'<li><a href="index\.html">Press( Kit)?</a></li>',
     '<li><a href="press.html">Press</a></li>'),
]

# For subfolder (client/, advocate/) — paths start with ../
SUB_REPLACEMENTS = [
    (r'<li><a href="\.\./solutions\.html">Studi Kasus</a></li>',
     '<li><a href="../case-study-detail.html">Studi Kasus</a></li>'),
    (r'<li><a href="\.\./faq\.html">Blog</a></li>',
     '<li><a href="../blog-detail.html">Blog</a></li>'),
    (r'<li><a href="\.\./index\.html">Karir</a></li>',
     '<li><a href="../career.html">Karir</a></li>'),
    (r'<li><a href="\.\./index\.html">Press( Kit)?</a></li>',
     '<li><a href="../press.html">Press</a></li>'),
]


def process_file(path):
    rel = os.path.relpath(path, SITE_DIR)
    depth = rel.count(os.sep)
    repls = SUB_REPLACEMENTS if depth > 0 else ROOT_REPLACEMENTS

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    total = 0
    for pat, rep in repls:
        content, n = re.subn(pat, rep, content)
        total += n
    if content != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'  ✓ {rel:<45} {total} link(s) rewired')
    return content != original


def main():
    for root, _, files in os.walk(SITE_DIR):
        for fn in files:
            if not fn.endswith('.html'):
                continue
            process_file(os.path.join(root, fn))


if __name__ == '__main__':
    main()
