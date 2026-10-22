"""Generate the profile's SVG assets (light + dark) in a Cell-inspired palette.

Run from the repo root:  python3 scripts/build_assets.py
"""
from pathlib import Path
from xml.sax.saxutils import escape

from PIL import ImageFont

OUT = Path(__file__).resolve().parent.parent / "assets"
OUT.mkdir(exist_ok=True)

PALETTE = {
    "light": dict(ink="#1A2433", body="#2E3A4B", muted="#5B6B7F", accent="#1D4E89",
                  accent2="#C8691C", rule="#C9D3DF", card="#F4F7FA", chip_basic="#E3E9F0",
                  chip_basic_ink="#2E3A4B", chip_adv_ink="#FFFFFF", chip_adv="#1D4E89"),
    "dark": dict(ink="#E6EDF3", body="#C9D1D9", muted="#8B98A8", accent="#6FA8DC",
                 accent2="#F0A35E", rule="#30363D", card="#161B22", chip_basic="#2A3340",
                 chip_basic_ink="#C9D1D9", chip_adv_ink="#0D1117", chip_adv="#6FA8DC"),
}
SANS = "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
SERIF = "Georgia, 'Times New Roman', Times, serif"
WIDTH = 880

_FONTS = {}


def text_width(s, size, bold=False):
    key = (size, bold)
    if key not in _FONTS:
        _FONTS[key] = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", size, index=1 if bold else 0)
    # Arial/Segoe run a little wider than Helvetica — pad so chips never clip
    return _FONTS[key].getlength(s) * 1.08


def svg(w, h, label, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img" aria-label="{escape(label)}">\n{body}</svg>\n')


def write(name, mode, content):
    (OUT / f"{name}-{mode}.svg").write_text(content)


def header(c):
    body = f'''  <rect x="0" y="12" width="5" height="160" fill="{c['accent']}"/>
  <text x="28" y="38" font-family="{SANS}" font-size="13" font-weight="600" letter-spacing="2.4" fill="{c['accent2']}">INTEGRATED M.S./PH.D. STUDENT</text>
  <text x="26" y="92" font-family="{SERIF}" font-size="52" fill="{c['ink']}">Joonoh Park</text>
  <line x1="28" y1="112" x2="{WIDTH - 20}" y2="112" stroke="{c['rule']}" stroke-width="1"/>
  <text x="28" y="140" font-family="{SANS}" font-size="18" font-weight="600" fill="{c['ink']}">Department of Brain and Cognitive Sciences, Seoul National University</text>
  <text x="28" y="166" font-family="{SANS}" font-size="17" fill="{c['body']}">Cognitive and Systems Neuroscience Laboratory<tspan fill="{c['muted']}">  ·  </tspan>Advisor: Prof. Sang-Hun Lee</text>
'''
    return svg(WIDTH, 180, "Joonoh Park — Integrated M.S./Ph.D. Student, Department of Brain and Cognitive "
               "Sciences, Seoul National University; Cognitive and Systems Neuroscience Laboratory; "
               "advisor Prof. Sang-Hun Lee", body)


def section(c, title):
    body = f'''  <text x="0" y="22" font-family="{SANS}" font-size="15" font-weight="700" letter-spacing="2.2" fill="{c['accent']}">{escape(title.upper())}</text>
  <line x1="0" y1="34" x2="{WIDTH}" y2="34" stroke="{c['accent']}" stroke-width="1.5"/>
'''
    return svg(WIDTH, 40, title, body)


CARD_W, CARD_H = 430, 112

# 20x20 line icons
ICONS = {
    "microscope": '<path d="M3 19h14M6 19c0-4 2-6 6-6"/><rect x="8" y="1" width="4" height="9" rx="1" transform="rotate(-25 10 6)"/><path d="M12 13v-2M14 19v-3"/>',
    "briefcase": '<rect x="1.5" y="6" width="17" height="11" rx="2"/><path d="M7 6V4a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v2M1.5 11h17"/>',
    "chip": '<rect x="5" y="5" width="10" height="10" rx="1.5"/><path d="M8 2v3M12 2v3M8 15v3M12 15v3M2 8h3M2 12h3M15 8h3M15 12h3"/><path d="M8.2 12.2l1.8-4.4 1.8 4.4M8.9 10.6h2.2"/>',
    "grid": '<rect x="2" y="2" width="7" height="7" rx="1.5"/><rect x="11" y="2" width="7" height="7" rx="1.5"/><rect x="2" y="11" width="7" height="7" rx="1.5"/><rect x="11" y="11" width="7" height="7" rx="1.5"/>',
}


def card(c, icon, label, lines):
    body = f'''  <rect x="0.5" y="0.5" width="{CARD_W - 1}" height="{CARD_H - 1}" rx="10" fill="{c['card']}" stroke="{c['rule']}"/>
  <rect x="0.5" y="16" width="4" height="{CARD_H - 32}" fill="{c['accent']}"/>
  <g transform="translate(20 20)" fill="none" stroke="{c['accent']}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{ICONS[icon]}</g>
  <text x="50" y="36" font-family="{SANS}" font-size="16" font-weight="700" fill="{c['accent']}">{escape(label)}</text>
  <text x="{CARD_W - 20}" y="36" text-anchor="end" font-family="{SANS}" font-size="13" fill="{c['muted']}">browse ↗</text>
'''
    for i, line in enumerate(lines):
        body += (f'  <text x="22" y="{66 + i * 22}" font-family="{SANS}" font-size="15" '
                 f'fill="{c["body"]}">{escape(line)}</text>\n')
    return svg(CARD_W, CARD_H, f"{label}: {' '.join(lines)}", body)


CARDS = [
    ("research", "microscope", "personal-research", ["Experimental design, computational", "modeling, and analysis methods"]),
    ("lab", "briefcase", "lab-management", ["AI-powered lab management system", "for CSNL (private)"]),
    ("auto", "chip", "auto-research", ["AI-powered research automation system,", "built with @ysys143"]),
    ("apps", "grid", "personal-apps", ["Apps for productivity and an", "organized work environment"]),
]

TECH = [
    ("Languages", [("MATLAB", 1), ("Python", 0)]),
    ("Modeling", [("Bayesian Observer", 1), ("Efficient Coding", 1), ("CANN", 0), ("PyTorch", 0), ("CNN", 0)]),
    ("Analysis", [("Dimensionality Reduction", 1), ("Structural Equation Modeling", 1),
                  ("Hierarchical Bayesian Model Fitting", 1), ("fMRI", 0)]),
    ("Experiments", [("Psychtoolbox", 1), ("jsPsych", 0), ("Eye Tracking", 0), ("tES", 0)]),
    ("Automation", [("Claude Code", 0)]),
]


def chip(c, x, y, label, advanced, size=14):
    w = text_width(label, size, bold=advanced) + 22
    fill, ink = (c["chip_adv"], c["chip_adv_ink"]) if advanced else (c["chip_basic"], c["chip_basic_ink"])
    weight = ' font-weight="600"' if advanced else ""
    return w, (f'  <rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="28" rx="14" fill="{fill}"/>\n'
               f'  <text x="{x + w / 2:.1f}" y="{y + 19}" text-anchor="middle" font-family="{SANS}" '
               f'font-size="{size}"{weight} fill="{ink}">{escape(label)}</text>\n')


def techniques(c):
    body, y, label_w, gap = "", 8, 130, 8
    for name, items in TECH:
        body += (f'  <text x="0" y="{y + 19}" font-family="{SANS}" font-size="14" font-weight="700" '
                 f'fill="{c["ink"]}">{name}</text>\n')
        x = label_w
        for label, adv in items:
            w = text_width(label, 14, bold=bool(adv)) + 22
            if x + w > WIDTH:
                x, y = label_w, y + 36
            _, s = chip(c, x, y, label, adv)
            body += s
            x += w + gap
        y += 44
    # legend
    _, s1 = chip(c, 0, y + 6, "Advanced", 1, 12)
    w1 = text_width("Advanced", 12, True) + 22
    _, s2 = chip(c, w1 + 8, y + 6, "Basic", 0, 12)
    body += s1 + s2
    return svg(WIDTH, y + 40, "Techniques — advanced: MATLAB, Bayesian observer models, efficient coding, "
               "dimensionality reduction, structural equation modeling, hierarchical Bayesian model fitting, "
               "Psychtoolbox; basic: Python, CANN, PyTorch, CNN, fMRI, jsPsych, eye tracking, tES, Claude Code",
               body)


def button(fn, label, icon, fill, w):
    body = f'''  <rect x="0.5" y="0.5" width="{w - 1}" height="27" rx="13.5" fill="{fill}"/>
  {icon}
  <text x="32" y="18.5" font-family="{SANS}" font-size="13" font-weight="600" fill="#FFFFFF">{label}</text>
'''
    (OUT / fn).write_text(svg(w, 28, label.replace("&amp;", "and"), body))


SECTIONS = ["Repositories", "Education", "Research Interests", "Techniques", "Teaching",
            "Publications & Presentations"]

if __name__ == "__main__":
    for mode, c in PALETTE.items():
        write("header", mode, header(c))
        for t in SECTIONS:
            slug = t.lower().replace(" & ", "-").replace(" ", "-")
            write(f"h-{slug}", mode, section(c, t))
        for key, icon, label, lines in CARDS:
            write(f"card-{key}", mode, card(c, icon, label, lines))
        write("techniques", mode, techniques(c))
    poster = ('<g fill="none" stroke="#FFFFFF" stroke-width="1.3"><rect x="12" y="7" width="12" height="14" rx="1"/>'
              '<rect x="14" y="9" width="8" height="5" fill="#FFFFFF" stroke="none"/>'
              '<line x1="14" y1="16.2" x2="22" y2="16.2"/><line x1="14" y1="18.6" x2="19.5" y2="18.6"/></g>')
    code = ('<g fill="none" stroke="#FFFFFF" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">'
            '<polyline points="16,9 12,14 16,19"/><polyline points="20.5,9 24.5,14 20.5,19"/></g>')
    button("btn-poster.svg", "Poster ↗", poster, "#1D4E89", 104)
    button("btn-code.svg", "Data &amp; code ↗", code, "#2C7A7B", 146)
    print("\n".join(sorted(p.name for p in OUT.glob("*.svg"))))
