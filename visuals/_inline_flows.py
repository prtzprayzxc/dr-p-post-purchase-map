"""
One-shot inliner: builds a fully self-contained drp-all-flows-simple.html
by embedding each sub-flow HTML as a <script type="text/html"> template.
The loader then sets iframe.srcdoc from those templates, so no file:// cross-
origin iframe blocks occur.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WRAPPER = ROOT / "visuals" / "drp-all-flows-simple.html"
OUT = WRAPPER  # overwrite in place

SUBS = {
    "uha":       ROOT / "services" / "uha"       / "visuals" / "uha-flow-simple.html",
    "challenge": ROOT / "services" / "challenge" / "visuals" / "challenge-flow-simple.html",
    "mem":       ROOT / "services" / "mem"       / "visuals" / "mem-flow-simple.html",
    "hwn":       ROOT / "services" / "hwn"       / "visuals" / "hwn-flow-simple.html",
}

def escape_for_template(html: str) -> str:
    # Prevent inner </script> from closing the outer <script type="text/html">.
    # HTML5 spec: any "</" followed by letters breaks the script tokenizer.
    # Breaking </script with a backslash keeps the text intact and the outer tag open.
    return re.sub(r"</(script)", r"<\\/\1", html, flags=re.IGNORECASE)

wrapper = WRAPPER.read_text(encoding="utf-8")

# Build the template blocks
tmpl_blocks = []
for key, path in SUBS.items():
    content = path.read_text(encoding="utf-8")
    escaped = escape_for_template(content)
    tmpl_blocks.append(
        f'<script type="text/html" id="tmpl-{key}">\n{escaped}\n</script>'
    )
templates_html = "\n".join(tmpl_blocks)

# Replace the iframe elements: drop data-src (we no longer fetch by URL)
# and leave them empty; the loader populates srcdoc from the template.
iframe_pattern = re.compile(
    r'<iframe\s+([^>]*?)data-src="[^"]*"([^>]*)></iframe>',
    flags=re.DOTALL,
)
def strip_data_src(m):
    before = m.group(1).strip()
    after = m.group(2).strip()
    attrs = " ".join(p for p in [before, after] if p)
    return f"<iframe {attrs}></iframe>"
new_wrapper = iframe_pattern.sub(strip_data_src, wrapper)

# Replace the loader script's source-loading lines
new_loader_js = r'''
    // Load a frame's HTML from its inline template (no network, no cross-origin).
    // NOTE: avoid any literal close-script tokens in this source — they would
    // prematurely terminate this outer script block during HTML parsing.
    function loadFrame(frame) {
      if (!frame || loaded.has(frame.id)) return;
      const key = frame.id.replace(/^frame-/, '');
      const tmpl = document.getElementById('tmpl-' + key);
      if (!tmpl) return;
      // Templates escape close-script as "<BS/script" where BS=backslash (one char).
      // Avoid embedding that sequence literally in JS source to dodge escape confusion.
      const BS           = String.fromCharCode(92); // backslash char
      const escapedClose = '<' + BS + '/script';    // the escaped form used in templates
      const realClose    = '<' + '/script';         // the real close tag we restore
      const html = tmpl.textContent.split(escapedClose).join(realClose);
      frame.srcdoc = html;
      loaded.add(frame.id);
    }

    // Eager-load the first active frame — deferred until DOM is parsed so the
    // inline templates below this script block are already in the document.
    function eagerLoadActive() {
      frames.forEach(f => {
        if (f.classList.contains('active')) loadFrame(f);
      });
    }
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', eagerLoadActive);
    } else {
      eagerLoadActive();
    }
'''

# Swap the old eager-load block
old_eager = re.compile(
    r'// Eager-load the first active frame\s*\n\s*frames\.forEach\(f => \{\s*\n\s*if \(f\.classList\.contains\(\'active\'\) && f\.dataset\.src\) \{\s*\n\s*f\.src = f\.dataset\.src;\s*\n\s*loaded\.add\(f\.id\);\s*\n\s*\}\s*\n\s*\}\);',
    flags=re.MULTILINE,
)
if not old_eager.search(new_wrapper):
    raise SystemExit("Could not locate old eager-load block.")
new_wrapper = old_eager.sub(new_loader_js.strip(), new_wrapper)

# Swap the activate()'s lazy-loader block
old_activate = re.compile(
    r'if \(on && !loaded\.has\(f\.id\) && f\.dataset\.src\) \{\s*\n\s*f\.src = f\.dataset\.src;\s*\n\s*loaded\.add\(f\.id\);\s*\n\s*\}',
    flags=re.MULTILINE,
)
if not old_activate.search(new_wrapper):
    raise SystemExit("Could not locate old activate-lazy-load block.")
new_wrapper = old_activate.sub("if (on) loadFrame(f);", new_wrapper)

# Insert the templates right before </body>
if "</body>" not in new_wrapper:
    raise SystemExit("Wrapper missing </body>")
new_wrapper = new_wrapper.replace("</body>", templates_html + "\n\n</body>")

OUT.write_text(new_wrapper, encoding="utf-8")
print(f"Wrote {OUT} ({len(new_wrapper):,} chars, {new_wrapper.count(chr(10)):,} lines)")
