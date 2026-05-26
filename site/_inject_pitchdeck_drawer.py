"""
_inject_pitchdeck_drawer.py
Injects a "📊 PITCH" group (with a link to pitchdeck.html) at the TOP of every
existing page's demo drawer.

Idempotent: skips a file if the PITCH group is already present.

For nested pages (client/, advocate/), the link uses "../pitchdeck.html".

Also updates the "Demo · N halaman" counter on the toggle button.
"""
import os
import re
import sys

SITE_DIR = os.path.dirname(os.path.abspath(__file__))
SKIP = {"pitchdeck.html"}

PITCH_GROUP_TEMPLATE = '''    <div class="demo-group">
      <div class="demo-group-label">📊 PITCH</div>
      <a class="drawer-link" href="{href}">Pitch Deck (16 Slides)</a>
    </div>

'''

# Marker we look for at top of <div class="demo-drawer-body">
BODY_OPEN_RE = re.compile(r'(<div\s+class="demo-drawer-body">\s*\n)')
# Toggle counter span — match "Demo · N halaman"
COUNTER_RE = re.compile(r'(<span>Demo · )\d+(\s*halaman</span>)')

def relpath_to_pitch(html_path: str) -> str:
    rel_dir = os.path.relpath(os.path.dirname(html_path), SITE_DIR)
    if rel_dir == "." or rel_dir == "":
        return "pitchdeck.html"
    # one level deep (client/ or advocate/)
    depth = rel_dir.count(os.sep) + 1
    return ("../" * depth) + "pitchdeck.html"


def process_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    name = os.path.relpath(path, SITE_DIR)

    if "📊 PITCH" in content:
        return f"skip (already injected): {name}"

    if 'class="demo-drawer-body"' not in content:
        return f"skip (no drawer): {name}"

    href = relpath_to_pitch(path)
    pitch_block = PITCH_GROUP_TEMPLATE.format(href=href)

    new_content, count = BODY_OPEN_RE.subn(
        lambda m: m.group(1) + pitch_block,
        content,
        count=1,
    )
    if count == 0:
        return f"skip (regex no match): {name}"

    # Update counter (best-effort: pages currently say "32 halaman" → bump to 33)
    new_content, cc = COUNTER_RE.subn(r"\g<1>33\g<2>", new_content, count=1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    return f"updated: {name} (href={href}, counter={'updated' if cc else 'unchanged'})"


def main():
    files = []
    for root, _, fnames in os.walk(SITE_DIR):
        for fn in fnames:
            if not fn.endswith(".html"):
                continue
            if fn in SKIP:
                continue
            files.append(os.path.join(root, fn))

    files.sort()
    print(f"Scanning {len(files)} HTML files...")
    for p in files:
        print(process_file(p))


if __name__ == "__main__":
    main()
