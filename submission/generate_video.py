"""Generates MatchVerse_AI_Demo.mp4 — rendered slides + offline narration, muxed with ffmpeg."""
import os
import subprocess
import wave
import contextlib
from PIL import Image, ImageDraw, ImageFont
import pyttsx3

W, H = 1280, 720
NAVY = (11, 46, 89)
BLUE = (30, 90, 200)
ACCENT = (59, 130, 246)
LIGHT = (232, 241, 253)
WHITE = (255, 255, 255)
GRAY = (75, 85, 99)
GREEN = (34, 197, 94)

FONT_DIR = r"C:\Windows\Fonts"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


F_TITLE = font("segoeuib.ttf", 46)
F_H1 = font("segoeuib.ttf", 30)
F_KICKER = font("segoeuib.ttf", 15)
F_BODY = font("segoeui.ttf", 20)
F_BODY_B = font("segoeuib.ttf", 20)
F_SMALL = font("segoeui.ttf", 14)
F_SCORE = font("segoeuib.ttf", 34)

OUT_DIR = os.path.join(os.path.dirname(__file__), "_render")
os.makedirs(OUT_DIR, exist_ok=True)

FFMPEG = r"C:\Users\nagarajang\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0.2-full_build\bin\ffmpeg.exe"
if not os.path.exists(FFMPEG):
    FFMPEG = "ffmpeg"


def wrap(draw, text, fnt, max_width):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        test = (cur + " " + w).strip()
        if draw.textlength(test, font=fnt) <= max_width:
            cur = test
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def header(draw, kicker, title):
    draw.rectangle([0, 0, W, 90], fill=NAVY)
    draw.text((40, 14), kicker, font=F_KICKER, fill=ACCENT)
    draw.text((40, 38), title, font=F_H1, fill=WHITE)


def footer(draw):
    draw.text((40, H - 34), "MatchVerse AI · RefSight Decision Intelligence", font=F_SMALL, fill=GRAY)


def bullets(draw, x, y, items, max_width=1150, gap=14, line_gap=6):
    for item in items:
        lines = wrap(draw, item, F_BODY, max_width - 30)
        draw.ellipse([x, y + 8, x + 8, y + 16], fill=BLUE)
        for i, line in enumerate(lines):
            draw.text((x + 22, y + i * 26), line, font=F_BODY, fill=GRAY)
        y += len(lines) * 26 + gap
    return y


def card(draw, x, y, w, h, title, body, color):
    draw.rectangle([x, y, x + w, y + h], fill=LIGHT)
    draw.rectangle([x, y, x + 6, y + h], fill=color)
    draw.text((x + 24, y + 20), title, font=F_BODY_B, fill=NAVY)
    lines = wrap(draw, body, F_BODY, w - 48)
    for i, line in enumerate(lines):
        draw.text((x + 24, y + 56 + i * 24), line, font=F_BODY, fill=GRAY)


def scene_title(img, draw):
    draw.rectangle([0, 0, 14, H], fill=BLUE)
    draw.rectangle([0, H - 170, W, H], fill=LIGHT)
    draw.text((70, 150), "🧠  MATCHVERSE AI", font=F_BODY_B, fill=BLUE)
    draw.text((70, 200), "Every Match Has", font=F_TITLE, fill=NAVY)
    draw.text((70, 255), "Multiple Realities", font=F_TITLE, fill=NAVY)
    draw.text((70, 330), "Explain the decision. Explore the alternative. Measure the impact.", font=F_BODY, fill=GRAY)
    draw.text((70, H - 130), "Powered by RefSight Decision Intelligence", font=F_BODY_B, fill=BLUE)


def scene_problem(img, draw):
    header(draw, "THE PROBLEM", "One Decision. A Thousand Opinions.")
    y = bullets(draw, 60, 140, [
        "Contested officiating decisions dominate the conversation — with no shared source of truth.",
        "Fans, analysts, and broadcasters all ask \u201cwhat if?\u201d, but rarely get a data-backed answer.",
        "Existing systems explain the rule, not the ripple effect on the result.",
    ])
    card(draw, 60, y + 20, 1150, 150, "Why it matters",
         "A single offside call can swing a match from a draw to a win — yet audiences never see that probability shift explained clearly.",
         BLUE)
    footer(draw)


def scene_solution(img, draw):
    header(draw, "THE SOLUTION", "MatchVerse AI — Decision Intelligence for Every Match")
    cards = [
        ("Observed Outcome", "What actually happened — the real decision, confidence score, and evidence margin.", GREEN),
        ("Alternative Outcome", "What would have happened if the call went the other way — modeled probabilities.", BLUE),
        ("Tactical Alternative", "How a different in-match decision could have reshaped the final result.", ACCENT),
    ]
    x = 60
    cw = 370
    for title, body, color in cards:
        card(draw, x, 150, cw, 260, title, body, color)
        x += cw + 20
    footer(draw)


def scene_features(img, draw):
    header(draw, "KEY FEATURES", "Four Modules, One Decision Intelligence Flow")
    y = bullets(draw, 60, 140, [
        "MatchVerse — live key-moment timeline: goal, penalty, card, validation reviews.",
        "Decision Intelligence — RefSight evidence breakdown with confidence and margin.",
        "Reality Compare — side-by-side scenario modeling of outcomes.",
        "Match Story — audience- and language-aware narrative generation.",
        "Integrity — evidence-tamper simulation and baseline restore.",
    ], gap=20)
    footer(draw)


def scene_flow(img, draw):
    header(draw, "HOW IT WORKS", "From Raw Evidence to Audience-Ready Insight")
    steps = ["Select Key\nMoment", "RefSight\nEvidence", "Model\nAlternatives", "Measure\nImpact", "Tell the\nStory"]
    x = 60
    w = 210
    for i, step in enumerate(steps):
        color = BLUE if i % 2 == 0 else NAVY
        draw.rectangle([x, 220, x + w, 320], fill=color)
        lines = step.split("\n")
        for li, line in enumerate(lines):
            tw = draw.textlength(line, font=F_BODY_B)
            draw.text((x + w / 2 - tw / 2, 250 + li * 26), line, font=F_BODY_B, fill=WHITE)
        x += w + 20
        if i < len(steps) - 1:
            draw.text((x - 10, 255), "➜", font=F_H1, fill=BLUE)
            x += 10
    draw.text((60, 400), "Every stage stays transparent and explainable — never a black box.", font=F_BODY, fill=GRAY)
    footer(draw)


def scene_techstack(img, draw):
    header(draw, "TECH STACK & HOW IT'S BUILT", "Today's Demo vs. the Production Roadmap")
    card(draw, 60, 140, 560, 340, "Today — Demo Build",
         "Pure HTML5, CSS3, vanilla JavaScript — zero frameworks, served as static files. "
         "Decisions, confidence scores and outcomes are scripted demo data illustrating the product experience.",
         BLUE)
    card(draw, 650, 140, 560, 340, "Roadmap — Production AI",
         "Computer-vision event detection, ML win-probability models, and an NLG service for Match Story — "
         "connected via a real API layer.",
         ACCENT)
    footer(draw)


def scene_demo(img, draw):
    header(draw, "LIVE DEMO HIGHLIGHT", "78:14 · Goal Review — North City 1 : 1 Red Borough")
    draw.rectangle([60, 130, 1210, 200], fill=NAVY)
    draw.text((90, 150), "DECISION: OFFSIDE", font=F_BODY_B, fill=WHITE)
    draw.text((470, 150), "CONFIDENCE: 97.4%", font=F_BODY_B, fill=ACCENT)
    draw.text((850, 150), "MARGIN: 12 cm", font=F_BODY_B, fill=WHITE)
    outcomes = [
        ("OBSERVED", "Goal disallowed", "1 – 1", "Draw probability 41%", GREEN),
        ("ALTERNATIVE", "Goal awarded", "2 – 1", "Home-win probability 62%", BLUE),
        ("TACTICAL ALT.", "Earlier substitution", "3 – 1", "Home-win probability 71%", ACCENT),
    ]
    x = 60
    cw = 370
    for tag, title, score, prob, color in outcomes:
        draw.rectangle([x, 230, x + cw, 230 + 240], fill=LIGHT)
        draw.text((x + 20, 250), tag, font=F_SMALL, fill=BLUE)
        draw.text((x + 20, 280), title, font=F_BODY_B, fill=NAVY)
        draw.text((x + 20, 330), score, font=F_SCORE, fill=color)
        draw.text((x + 20, 390), prob, font=F_SMALL, fill=GRAY)
        x += cw + 20
    footer(draw)


def scene_audience(img, draw):
    header(draw, "AUDIENCE & IMPACT", "One Engine, Every Audience")
    cards = [
        ("Casual Fan", "Simple, story-driven explanations of what the decision meant.", GREEN),
        ("Analyst", "Deeper statistics, confidence scores, and scenario probabilities.", BLUE),
        ("Broadcaster", "Ready-to-air narrative framing, multi-language support.", ACCENT),
    ]
    x = 60
    cw = 370
    for title, body, color in cards:
        card(draw, x, 140, cw, 150, title, body, color)
        x += cw + 20
    bullets(draw, 60, 320, [
        "Builds trust through transparency, not just enforcement.",
        "Increases engagement with interactive, data-backed storytelling.",
    ], gap=18)
    footer(draw)


def scene_closing(img, draw):
    draw.rectangle([0, 0, W, H], fill=NAVY)
    draw.text((70, 260), "MATCHVERSE AI", font=F_TITLE, fill=WHITE)
    draw.text((70, 330), "Explain decisions · Explore alternatives · Understand impact", font=F_BODY_B, fill=ACCENT)
    draw.text((70, 600), "Probability changes are modelled estimates for decision exploration.", font=F_SMALL, fill=(185, 198, 218))
    draw.text((70, 622), "Human review remains authoritative.", font=F_SMALL, fill=(185, 198, 218))


SCENES = [
    ("title", scene_title, True,
     "Welcome to MatchVerse AI, where every contested match decision gets a clear, data backed story."),
    ("problem", scene_problem, False,
     "Officiating decisions spark endless debate, but nobody shows fans what each alternative would have meant."),
    ("solution", scene_solution, False,
     "MatchVerse AI models the observed call alongside realistic alternative outcomes, side by side."),
    ("features", scene_features, False,
     "Five connected modules take you from raw evidence to an audience ready story: MatchVerse, Decision Intelligence, Reality Compare, Match Story, and Integrity."),
    ("flow", scene_flow, False,
     "Each decision flows through five transparent stages, select the moment, review the evidence, model alternatives, measure impact, and tell the story. Never a black box."),
    ("techstack", scene_techstack, False,
     "Today this runs as a lightweight HTML, CSS and JavaScript demo. The decision data and AI outcomes are scripted for this walkthrough, with real computer vision and probability models on the roadmap."),
    ("demo", scene_demo, False,
     "Here's the live demo: a ninety seven point four percent confidence offside call. Observed outcome, goal disallowed, one one. Alternative, goal awarded, two one. Tactical alternative, an earlier substitution leading to three one."),
    ("audience", scene_audience, False,
     "One engine adapts its story for casual fans, analysts, and broadcasters alike, building trust through transparency and driving deeper engagement."),
    ("closing", scene_closing, True,
     "Thank you. MatchVerse AI. Explain decisions, explore alternatives, understand impact."),
]


def render_images():
    for i, (name, fn, is_full, _) in enumerate(SCENES):
        img = Image.new("RGB", (W, H), WHITE)
        draw = ImageDraw.Draw(img)
        fn(img, draw)
        path = os.path.join(OUT_DIR, f"{i:02d}_{name}.png")
        img.save(path)
        print("rendered", path)


def synth_audio():
    durations = []
    for i, (name, fn, is_full, narration) in enumerate(SCENES):
        wav_path = os.path.join(OUT_DIR, f"{i:02d}_{name}.wav")
        if not os.path.exists(wav_path):
            engine = pyttsx3.init()
            engine.setProperty("rate", 165)
            engine.save_to_file(narration, wav_path)
            engine.runAndWait()
            try:
                engine.stop()
            except Exception:
                pass
            del engine
        with contextlib.closing(wave.open(wav_path, "r")) as wf:
            frames = wf.getnframes()
            rate = wf.getframerate()
            dur = frames / float(rate)
        durations.append(max(dur + 0.8, 3.0))
        print(name, "audio duration:", round(dur, 2))
    return durations


def assemble(durations):
    # Build concat list for images (each image shown for its scene duration)
    concat_path = os.path.join(OUT_DIR, "images.txt")
    with open(concat_path, "w") as f:
        for i, (name, fn, is_full, _) in enumerate(SCENES):
            png = os.path.join(OUT_DIR, f"{i:02d}_{name}.png").replace("\\", "/")
            f.write(f"file '{png}'\nduration {durations[i]:.2f}\n")
        # repeat last frame per ffmpeg concat quirk
        last_png = os.path.join(OUT_DIR, f"{len(SCENES)-1:02d}_{SCENES[-1][0]}.png").replace("\\", "/")
        f.write(f"file '{last_png}'\n")

    silent_video = os.path.join(OUT_DIR, "silent.mp4")
    subprocess.run([
        FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", concat_path,
        "-fps_mode", "vfr", "-pix_fmt", "yuv420p", silent_video
    ], check=True)

    # Concat all narration wavs into one audio track with silence gaps matching duration
    audio_concat_path = os.path.join(OUT_DIR, "audio.txt")
    padded_wavs = []
    for i, (name, fn, is_full, _) in enumerate(SCENES):
        src = os.path.join(OUT_DIR, f"{i:02d}_{name}.wav")
        padded = os.path.join(OUT_DIR, f"{i:02d}_{name}_padded.wav")
        subprocess.run([
            FFMPEG, "-y", "-i", src, "-af",
            f"apad=whole_dur={durations[i]:.2f}", padded
        ], check=True)
        padded_wavs.append(padded)
    with open(audio_concat_path, "w") as f:
        for p in padded_wavs:
            f.write(f"file '{p.replace(chr(92), '/')}'\n")
    full_audio = os.path.join(OUT_DIR, "full_audio.wav")
    subprocess.run([
        FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", audio_concat_path, full_audio
    ], check=True)

    out_path = os.path.join(os.path.dirname(__file__), "MatchVerse_AI_Demo.mp4")
    subprocess.run([
        FFMPEG, "-y", "-i", silent_video, "-i", full_audio,
        "-c:v", "libx264", "-c:a", "aac", "-shortest", out_path
    ], check=True)
    print("DONE:", out_path)


if __name__ == "__main__":
    render_images()
    durations = synth_audio()
    assemble(durations)
