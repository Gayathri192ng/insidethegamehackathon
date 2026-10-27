# MatchVerse AI — Submission Package

This folder contains everything needed to submit a **2-minute demo video** and a **professional PPT** for MatchVerse AI.

## Files & download locations
All files live in this `submission/` folder:
`c:\Users\nagarajang\Downloads\MatchVerseAI_Final_Full_Project\MatchVerseAI_Final_Project\submission\`

- **`MatchVerse_AI_Submission.pptx`** — 8-slide blue/white deck. **"Gayathri Nagarajan" appears bottom-right on every slide** (title, closing, and all content-slide footers). Double-click to open directly in PowerPoint — no extra download needed, it's already a native `.pptx` file in this folder.
- **`hero-banner.html`** — standalone hero banner page for the project (1600×500, blue/white gradient, logo, tagline, CTA buttons, key-stat cards). Open in a browser and use a screenshot tool (Win+Shift+S) to export as PNG if you need a static image.
- **`video-script.html`** — an auto-playing, exactly **120-second** timed slideshow (blue/white theme) with synced **English subtitles** (CC·EN badge, bottom-center subtitle bar). Screen-record it to produce your video file.
- **`DEMO_SCRIPT.md`** — the full narration/speaker script, timestamped to match the subtitles on screen.
- **`generate_pptx.py`** — the script that generated the pptx (re-run after edits with `py generate_pptx.py`).

## How to produce the video file (exact 2:00, with English subtitles)
1. Open `video-script.html` in a browser, maximized — it auto-scales to any window size.
2. Start your screen recorder (Windows: `Win+Alt+R` for Xbox Game Bar, or OBS) **right as you refresh the page** — it starts the 120s timeline automatically on load.
3. Let it run untouched; it stops exactly at 02:00 (progress bar + timer confirm this). English subtitles appear in a CC bar at the bottom of every scene automatically.
4. Stop the recording immediately at the 2:00 mark and trim if your recorder adds a second or two of lead-in.
5. Optional: narrate using `DEMO_SCRIPT.md` while recording, or dub the voiceover afterward — subtitles will already match your speech.

## Narration script (read aloud while recording, or use as voiceover track)

| Time | Scene | Narration |
|---|---|---|
| 0:00–0:10 | Title | "Welcome to MatchVerse AI — where every contested match decision gets a clear, data-backed story." |
| 0:10–0:23 | Problem | "Officiating decisions spark endless debate, but nobody shows fans what each alternative would have meant." |
| 0:23–0:39 | Solution | "MatchVerse AI models the observed call alongside realistic alternative outcomes, side by side." |
| 0:39–0:55 | Key Features | "Five connected modules take you from raw evidence to an audience-ready story." |
| 0:55–1:08 | How it works | "Each decision flows through five transparent stages — never a black box." |
| 1:08–1:22 | Tech Stack & How It's Built | "Today this runs as a scripted HTML/CSS/JS demo; the roadmap adds real computer-vision and ML models." |
| 1:22–1:38 | Live demo highlight | "Here's the live demo: a 97.4%-confidence offside call, with every alternative outcome modeled instantly." |
| 1:38–1:52 | Audience & Impact | "One engine adapts its story for casual fans, analysts, and broadcasters alike." |
| 1:52–2:00 | Closing | "Thank you — MatchVerse AI. Explain decisions, explore alternatives, understand impact." |

Total runtime: **exactly 2:00**. Full version with delivery tips: see `DEMO_SCRIPT.md`.

## Theme
Blue/white throughout (navy `#0B2E59`, blue `#1E5AC8`, accent `#3B82F6`, light background `#E8F1FD`) — matches the PPT, the video script, and the hero banner.
