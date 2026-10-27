"""Generates MatchVerse_AI_Submission.pptx — a blue/white professional deck."""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn

NAVY = RGBColor(0x0B, 0x2E, 0x59)
BLUE = RGBColor(0x1E, 0x5A, 0xC8)
LIGHT_BLUE = RGBColor(0xE8, 0xF1, 0xFD)
ACCENT = RGBColor(0x3B, 0x82, 0xF6)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
GRAY = RGBColor(0x4B, 0x55, 0x63)
PRESENTER = "Gayathri Nagarajan"

SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)

prs = Presentation()
prs.slide_width = SLIDE_W
prs.slide_height = SLIDE_H
blank = prs.slide_layouts[6]


def add_slide():
    return prs.slides.add_slide(blank)


def set_background(slide, color=WHITE):
    bg = slide.background
    bg.fill.solid()
    bg.fill.fore_color.rgb = color


def add_rect(slide, x, y, w, h, color, line=False):
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    if line:
        shape.line.color.rgb = color
    else:
        shape.line.fill.background()
    shape.shadow.inherit = False
    return shape


def add_text(slide, x, y, w, h, text, size=18, color=GRAY, bold=False,
             align=PP_ALIGN.LEFT, font="Segoe UI", anchor=MSO_ANCHOR.TOP, italic=False):
    box = slide.shapes.add_textbox(x, y, w, h)
    tf = box.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = Pt(size)
    run.font.color.rgb = color
    run.font.bold = bold
    run.font.italic = italic
    run.font.name = font
    return box


def add_bullets(slide, x, y, w, h, items, size=16, color=GRAY, font="Segoe UI", space_after=10):
    box = slide.shapes.add_textbox(x, y, w, h)
    tf = box.text_frame
    tf.word_wrap = True
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(space_after)
        run = p.add_run()
        run.text = f"●  {item}"
        run.font.size = Pt(size)
        run.font.color.rgb = color
        run.font.name = font
    return box


def add_header(slide, kicker, title):
    add_rect(slide, Inches(0), Inches(0), Inches(13.333), Inches(1.3), NAVY)
    add_text(slide, Inches(0.6), Inches(0.12), Inches(10), Inches(0.4), kicker,
              size=13, color=ACCENT, bold=True)
    add_text(slide, Inches(0.6), Inches(0.45), Inches(12), Inches(0.75), title,
              size=28, color=WHITE, bold=True)


def add_footer(slide, page):
    add_text(slide, Inches(0.6), Inches(7.12), Inches(8), Inches(0.3),
              "MatchVerse AI · RefSight Decision Intelligence", size=10, color=RGBColor(0x8A, 0x97, 0xA8))
    add_text(slide, Inches(12.3), Inches(7.12), Inches(0.7), Inches(0.3), str(page),
              size=10, color=RGBColor(0x8A, 0x97, 0xA8), align=PP_ALIGN.RIGHT)


# ---------- Slide 1: Title ----------
s = add_slide()
set_background(s, WHITE)
add_rect(s, Inches(0), Inches(0), Inches(13.333), Inches(7.5), WHITE)
add_rect(s, Inches(0), Inches(0), Inches(0.25), Inches(7.5), BLUE)
add_rect(s, Inches(0), Inches(5.6), Inches(13.333), Inches(1.9), LIGHT_BLUE)

add_text(s, Inches(1.0), Inches(1.6), Inches(4), Inches(0.6), "🧠  MATCHVERSE AI", size=22, color=BLUE, bold=True)
add_text(s, Inches(1.0), Inches(2.3), Inches(11), Inches(1.6),
          "Every Match Has Multiple Realities", size=46, color=NAVY, bold=True)
add_text(s, Inches(1.0), Inches(3.75), Inches(10.5), Inches(1.0),
          "Explain the decision. Explore the alternative. Measure the impact.",
          size=20, color=GRAY, italic=True)
add_text(s, Inches(1.0), Inches(5.9), Inches(11), Inches(0.5),
          "Powered by RefSight Decision Intelligence", size=16, color=BLUE, bold=True)
add_text(s, Inches(1.0), Inches(6.4), Inches(11), Inches(0.5),
          "Project Submission  ·  MatchVerse AI Demo Deck", size=13, color=GRAY)
add_text(s, Inches(9.3), Inches(6.9), Inches(3.2), Inches(0.4), f"Done by {PRESENTER}",
          size=14, color=NAVY, bold=True, align=PP_ALIGN.RIGHT)

# ---------- Slide 2: Problem ----------
s = add_slide()
set_background(s)
add_header(s, "THE PROBLEM", "One Decision. A Thousand Opinions.")
add_bullets(s, Inches(0.8), Inches(2.0), Inches(7.0), Inches(4.5), [
    "Contested officiating decisions dominate post-match conversation, with no shared source of truth.",
    "Fans, analysts, and broadcasters all ask \"what if?\" — but rarely get a data-backed answer.",
    "Existing review systems explain the rule, but not the ripple effect on the match outcome.",
    "Trust in officiating erodes when decisions feel opaque, even when they are correct.",
], size=18)
box = add_rect(s, Inches(8.2), Inches(2.1), Inches(4.3), Inches(4.2), LIGHT_BLUE)
add_text(s, Inches(8.5), Inches(2.35), Inches(3.7), Inches(0.4), "WHY IT MATTERS", size=13, color=BLUE, bold=True)
add_text(s, Inches(8.5), Inches(2.85), Inches(3.7), Inches(3.2),
          "A single offside call can swing a match from a draw to a win — "
          "yet audiences never see that probability shift explained clearly.",
          size=16, color=NAVY)
add_footer(s, 2)

# ---------- Slide 3: Solution ----------
s = add_slide()
set_background(s)
add_header(s, "THE SOLUTION", "MatchVerse AI — Decision Intelligence for Every Match")
add_text(s, Inches(0.8), Inches(1.7), Inches(11.5), Inches(0.8),
          "A web experience that turns every contested decision into a clear, data-grounded story.",
          size=18, color=GRAY, italic=True)
cards = [
    ("Observed Outcome", "What actually happened — the real decision, confidence score, and evidence margin."),
    ("Alternative Outcome", "What would have happened if the call had gone the other way, modeled with win/draw probabilities."),
    ("Tactical Alternative", "How a different in-match decision (e.g. a substitution) could have reshaped the result."),
]
x = Inches(0.8)
for title, desc in cards:
    add_rect(s, x, Inches(2.7), Inches(3.75), Inches(3.4), LIGHT_BLUE)
    add_rect(s, x, Inches(2.7), Inches(3.75), Inches(0.08), BLUE)
    add_text(s, x + Inches(0.3), Inches(3.0), Inches(3.2), Inches(0.6), title, size=18, color=NAVY, bold=True)
    add_text(s, x + Inches(0.3), Inches(3.65), Inches(3.2), Inches(2.3), desc, size=14, color=GRAY)
    x += Inches(4.05)
add_footer(s, 3)

# ---------- Slide 4: Key Features ----------
s = add_slide()
set_background(s)
add_header(s, "KEY FEATURES", "Four Modules, One Decision Intelligence Flow")
features = [
    ("MatchVerse", "Live key-moment timeline with goal, penalty, card and validation reviews."),
    ("Decision Intelligence", "RefSight evidence breakdown: confidence score, positional margin, match state."),
    ("Reality Compare", "Side-by-side scenario modeling of observed vs. alternative match outcomes."),
    ("Match Story", "Audience- and language-aware narrative generation for fans, analysts, broadcasters."),
    ("Integrity", "Evidence-tamper simulation and baseline restore to demonstrate auditability."),
]
y = Inches(1.9)
for i, (title, desc) in enumerate(features):
    add_rect(s, Inches(0.8), y, Inches(0.55), Inches(0.9), BLUE)
    add_text(s, Inches(0.8), y + Inches(0.18), Inches(0.55), Inches(0.5), str(i + 1), size=22, color=WHITE,
              bold=True, align=PP_ALIGN.CENTER)
    add_text(s, Inches(1.6), y + Inches(0.02), Inches(3.0), Inches(0.5), title, size=18, color=NAVY, bold=True)
    add_text(s, Inches(4.8), y + Inches(0.05), Inches(7.7), Inches(0.8), desc, size=14, color=GRAY)
    y += Inches(1.02)
add_footer(s, 4)

# ---------- Slide 5: How it works ----------
s = add_slide()
set_background(s)
add_header(s, "HOW IT WORKS", "From Raw Evidence to Audience-Ready Insight")
steps = ["Select Key Moment", "RefSight Evidence", "Model Alternatives", "Measure Impact", "Tell the Story"]
x = Inches(0.6)
w = Inches(2.3)
for i, step in enumerate(steps):
    add_rect(s, x, Inches(3.0), w, Inches(1.3), BLUE if i % 2 == 0 else NAVY)
    add_text(s, x, Inches(3.4), w, Inches(0.6), step, size=14, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
    if i < len(steps) - 1:
        add_text(s, x + w, Inches(3.15), Inches(0.35), Inches(1.0), "➜", size=22, color=BLUE, align=PP_ALIGN.CENTER)
    x += w + Inches(0.35)
add_text(s, Inches(0.8), Inches(4.8), Inches(11.5), Inches(1.5),
          "Each stage is transparent and explainable — decisions are never a black box. "
          "Probability changes are modelled estimates for decision exploration; human review remains authoritative.",
          size=16, color=GRAY, italic=True)
add_footer(s, 5)

# ---------- Slide 6: Tech Stack & How It's Built ----------
s = add_slide()
set_background(s)
add_header(s, "TECH STACK & HOW IT'S BUILT", "Today's Demo vs. the Production Roadmap")
cols = [
    ("TODAY — DEMO BUILD", [
        "Pure HTML5, CSS3 and vanilla JavaScript — zero frameworks, runs in any browser.",
        "No backend/server: served as static files (e.g. a local Python http.server).",
        "Decisions, confidence scores and outcome probabilities are scripted demo data, "
        "illustrating the product experience end to end.",
        "MatchVerse Copilot answers are pre-written text, not a live model call.",
    ]),
    ("ROADMAP — PRODUCTION AI", [
        "Computer-vision event detection on broadcast video (offside lines, contact, ball tracking).",
        "Probabilistic / ML win-draw-loss models trained on historical match data.",
        "NLG service to generate the audience-specific Match Story narratives.",
        "API + data layer connecting live match feeds to the existing front-end UI.",
    ]),
]
x = Inches(0.8)
for title, items in cols:
    add_rect(s, x, Inches(1.9), Inches(5.75), Inches(4.4), LIGHT_BLUE)
    add_rect(s, x, Inches(1.9), Inches(5.75), Inches(0.08), BLUE)
    add_text(s, x + Inches(0.3), Inches(2.15), Inches(5.2), Inches(0.5), title, size=16, color=NAVY, bold=True)
    bullets = slide_shapes_textbox = s.shapes.add_textbox(x + Inches(0.3), Inches(2.7), Inches(5.2), Inches(3.4))
    tf = bullets.text_frame
    tf.word_wrap = True
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(10)
        run = p.add_run()
        run.text = f"●  {item}"
        run.font.size = Pt(13)
        run.font.color.rgb = GRAY
        run.font.name = "Segoe UI"
    x += Inches(6.0)
add_text(s, Inches(0.8), Inches(6.45), Inches(11.5), Inches(0.5),
          "Transparency note: today's build is a UX/product demo — the AI behavior shown is simulated to illustrate the intended experience.",
          size=12, color=BLUE, italic=True, bold=True)
add_footer(s, 6)

# ---------- Slide 7: Demo highlight ----------
s = add_slide()
set_background(s)
add_header(s, "LIVE DEMO HIGHLIGHT", "78:14 · Goal Review — North City 1 : 1 Red Borough")
add_rect(s, Inches(0.8), Inches(1.9), Inches(11.73), Inches(0.85), NAVY)
add_text(s, Inches(1.1), Inches(2.05), Inches(3.5), Inches(0.55), "DECISION: OFFSIDE", size=16, color=WHITE, bold=True)
add_text(s, Inches(5.0), Inches(2.05), Inches(3.5), Inches(0.55), "CONFIDENCE: 97.4%", size=16, color=ACCENT, bold=True)
add_text(s, Inches(8.8), Inches(2.05), Inches(3.5), Inches(0.55), "MARGIN: 12 cm", size=16, color=WHITE, bold=True)

outcomes = [
    ("OBSERVED", "Goal disallowed", "1 – 1", "Draw probability 41%"),
    ("ALTERNATIVE", "Goal awarded", "2 – 1", "Home-win probability 62%"),
    ("TACTICAL ALT.", "Earlier substitution", "3 – 1", "Home-win probability 71%"),
]
x = Inches(0.8)
for tag, title, score, prob in outcomes:
    add_rect(s, x, Inches(3.1), Inches(3.75), Inches(3.0), LIGHT_BLUE)
    add_text(s, x + Inches(0.25), Inches(3.3), Inches(3.3), Inches(0.4), tag, size=12, color=BLUE, bold=True)
    add_text(s, x + Inches(0.25), Inches(3.75), Inches(3.3), Inches(0.5), title, size=18, color=NAVY, bold=True)
    add_text(s, x + Inches(0.25), Inches(4.3), Inches(3.3), Inches(0.7), score, size=30, color=BLUE, bold=True)
    add_text(s, x + Inches(0.25), Inches(5.1), Inches(3.3), Inches(0.7), prob, size=13, color=GRAY)
    x += Inches(4.05)
add_footer(s, 7)

# ---------- Slide 8: Audience & Impact ----------
s = add_slide()
set_background(s)
add_header(s, "AUDIENCE & IMPACT", "One Engine, Every Audience")
auds = [
    ("Casual Fan", "Simple, story-driven explanations of what the decision meant for the match."),
    ("Analyst", "Deeper statistical breakdowns, confidence scores, and scenario probabilities."),
    ("Broadcaster", "Ready-to-air narrative framing, multi-language support for global audiences."),
]
x = Inches(0.8)
for title, desc in auds:
    add_rect(s, x, Inches(2.0), Inches(3.75), Inches(2.3), LIGHT_BLUE)
    add_text(s, x + Inches(0.3), Inches(2.25), Inches(3.2), Inches(0.5), title, size=18, color=NAVY, bold=True)
    add_text(s, x + Inches(0.3), Inches(2.8), Inches(3.2), Inches(1.4), desc, size=13, color=GRAY)
    x += Inches(4.05)
add_bullets(s, Inches(0.8), Inches(4.6), Inches(11.5), Inches(2.2), [
    "Builds trust through transparency — every call is explainable, not just enforced.",
    "Increases fan engagement with interactive, data-backed storytelling.",
    "Strengthens officiating integrity with tamper-evident evidence auditing.",
], size=16)
add_footer(s, 8)

# ---------- Slide 9: Closing ----------
s = add_slide()
set_background(s, NAVY)
add_rect(s, Inches(0), Inches(0), Inches(13.333), Inches(7.5), NAVY)
add_text(s, Inches(1.0), Inches(2.4), Inches(11), Inches(1.0), "MATCHVERSE AI", size=38, color=WHITE, bold=True)
add_text(s, Inches(1.0), Inches(3.3), Inches(11), Inches(0.8),
          "Explain decisions · Explore alternatives · Understand impact", size=20, color=ACCENT, bold=True)
add_text(s, Inches(1.0), Inches(4.3), Inches(11), Inches(0.8),
          "Thank you — questions welcome.", size=16, color=WHITE)
add_text(s, Inches(1.0), Inches(6.6), Inches(11), Inches(0.5),
          "Probability changes are modelled estimates for decision exploration. Human review remains authoritative.",
          size=11, color=RGBColor(0xB9, 0xC6, 0xDA), italic=True)

prs.save("MatchVerse_AI_Submission.pptx")
print("Saved MatchVerse_AI_Submission.pptx")
