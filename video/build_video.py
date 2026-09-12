"""
build_video.py
Turns video/script.md into a narrated MP4 with subtitles.

Pipeline (one row of the script = one shot):
  1. parse script.md            -> scenes and rows (voice-over, on-screen text)
  2. edge-tts                   -> one MP3 of narration per row (neural voice)
  3. Pillow                     -> one 1920x1080 frame per row, designed like the report page
  4. ffmpeg                     -> one clip per row (still frame + narration), then concatenated
  5. write pyros_video.srt      -> subtitles with the real timings

Run from the project root:   python video/build_video.py
Needs: ffmpeg and ffprobe on PATH, Pillow, edge-tts (pip install edge-tts), internet for the voice.
Outputs (git-ignored except the .srt): video/build/ (working files), video/pyros_video.mp4, video/pyros_video.srt
"""
import asyncio, json, re, subprocess, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import edge_tts

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "video" / "script.md"
BUILD = ROOT / "video" / "build"
OUT_MP4 = ROOT / "video" / "pyros_video.mp4"
OUT_SRT = ROOT / "video" / "pyros_video.srt"
VOICE = "en-GB-RyanNeural"          # calm British male neural voice; change to taste
RATE = "-6%"                        # slightly slower than default for a calm pace
GAP = 0.7                           # seconds of silence after each line
W, H = 1920, 1080

# Palette, same as the report page (light theme)
PAPER = (244, 246, 248); INK = (22, 34, 46); MUTED = (91, 107, 120)
ACCENT = (184, 101, 27); RULE = (213, 220, 226); SLATE = (46, 90, 120)
FONTS = Path(r"C:\Windows\Fonts")
def font(name, size):
    return ImageFont.truetype(str(FONTS / name), size)
F_DISPLAY = lambda s: font("georgiab.ttf", s)
F_DISPLAY_I = lambda s: font("georgiai.ttf", s)
F_BODY = lambda s: font("segoeui.ttf", s)
F_BODY_L = lambda s: font("segoeuil.ttf", s)
F_MONO = lambda s: font("consola.ttf", s)

# ---------------------------------------------------------------- 1. parse
def parse_script(text):
    scenes = []
    cur = None
    for line in text.splitlines():
        m = re.match(r"^## Scene (\S+)\. (.+?) \(", line)
        if m:
            cur = {"num": m.group(1), "title": m.group(2), "rows": []}
            scenes.append(cur)
            continue
        if cur and line.startswith("| ") and not line.startswith("| Voice-over") and not line.startswith("|---"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 2:
                continue
            vo, screen = cells[0], cells[1]
            vo = re.sub(r"\*\((.*?)\)\*", "", vo)            # stage directions in italics
            vo = re.sub(r"\*\*\[.*?\]\*\*", "", vo)          # bracketed placeholders
            vo = re.sub(r"\[.*?\]", "", vo)
            vo = vo.replace("**", "").replace("*", "").strip()
            if not vo:
                continue
            bold = re.findall(r"\*\*(.+?)\*\*", screen)
            onscreen = " ".join(b for b in bold if not b.lower().startswith(("text:", "text label")))
            onscreen = re.sub(r"^(Text|Text label|Title card|Quote card):\s*", "", onscreen).strip()
            cur["rows"].append({"vo": vo, "onscreen": onscreen, "art": screen})
    return scenes

# ---------------------------------------------------------------- 2. speech
async def synth(text, path):
    await edge_tts.Communicate(text, VOICE, rate=RATE).save(str(path))

def duration(path):
    out = subprocess.run(["ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", str(path)],
                         capture_output=True, text=True).stdout
    return float(json.loads(out)["format"]["duration"])

# ---------------------------------------------------------------- 3. frames
def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur:
        lines.append(cur)
    return lines

def draw_frame(row, scene, idx, total, path):
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    margin = 140
    # eyebrow
    d.text((margin, 70), "PYROS  ·  THE DOCTOR WHO DRIVES A TAXI", font=F_MONO(26), fill=MUTED)
    lab = f"SCENE {scene['num']}  ·  {scene['title'].upper()}"
    d.text((W - margin - d.textlength(lab, font=F_MONO(26)), 70), lab, font=F_MONO(26), fill=MUTED)
    d.line([(margin, 120), (W - margin, 120)], fill=RULE, width=2)
    # accent mark
    d.rectangle([margin, 190, margin + 14, 190 + 120], fill=ACCENT)
    # main on-screen text
    text = row["onscreen"]
    is_quote = text.startswith(("\"", "“", "'"))
    if text:
        fnt = F_DISPLAY_I(78) if is_quote else F_DISPLAY(84)
        lines = wrap(d, text, fnt, W - 2 * margin - 60)
        while len(lines) > 4 and fnt.size > 48:
            fnt = F_DISPLAY_I(fnt.size - 8) if is_quote else F_DISPLAY(fnt.size - 8)
            lines = wrap(d, text, fnt, W - 2 * margin - 60)
        y = 180
        for ln in lines:
            d.text((margin + 50, y), ln, font=fnt, fill=INK)
            y += int(fnt.size * 1.18)
    else:
        # no headline phrase: show the scene title, quietly
        fnt = F_DISPLAY(64)
        d.text((margin + 50, 190), scene["title"], font=fnt, fill=SLATE)
    # subtitle band
    band_top = H - 300
    d.line([(margin, band_top - 30), (W - margin, band_top - 30)], fill=RULE, width=2)
    sub = F_BODY_L(40)
    for i, ln in enumerate(wrap(d, row["vo"], sub, W - 2 * margin)[:5]):
        d.text((margin, band_top + i * 52), ln, font=sub, fill=INK)
    # progress
    d.text((margin, H - 60), f"{idx + 1} / {total}", font=F_MONO(22), fill=MUTED)
    bar_w = W - 2 * margin
    d.rectangle([margin, H - 30, margin + bar_w, H - 26], fill=RULE)
    d.rectangle([margin, H - 30, margin + int(bar_w * (idx + 1) / total), H - 26], fill=ACCENT)
    img.save(path)

def end_card(path):
    img = Image.new("RGB", (W, H), INK)
    d = ImageDraw.Draw(img)
    d.text((140, 300), "The doctor who drives a taxi", font=F_DISPLAY(96), fill=PAPER)
    d.text((140, 440), "A rapid review by PYROS", font=F_BODY_L(48), fill=(200, 210, 218))
    d.text((140, 560), "Full report, data and code:", font=F_BODY(40), fill=(200, 210, 218))
    d.text((140, 620), "github.com/Odogwu90/PYROS_rapid_review", font=F_MONO(44), fill=(224, 146, 74))
    d.text((140, 760), "Reviewer: Dr. Okpara Onyedikachi Martins  ·  Narration: synthetic voice  ·  Version 1.0", font=F_MONO(26), fill=(150, 166, 178))
    img.save(path)

# ---------------------------------------------------------------- 4. assemble
def srt_time(t):
    h, rem = divmod(t, 3600); m, s = divmod(rem, 60)
    return f"{int(h):02d}:{int(m):02d}:{int(s):02d},{int(round((s % 1) * 1000)):03d}"

def main():
    BUILD.mkdir(exist_ok=True)
    scenes = parse_script(SCRIPT.read_text(encoding="utf-8"))
    rows = [(s, r) for s in scenes for r in s["rows"]]
    total = len(rows)
    print(f"{len(scenes)} scenes, {total} lines")
    # speech
    async def all_speech():
        for i, (s, r) in enumerate(rows):
            mp3 = BUILD / f"{i:03d}.mp3"
            if not mp3.exists():
                await synth(r["vo"], mp3)
                print(f"  voice {i + 1}/{total}", end="\r")
    asyncio.run(all_speech())
    # frames + clips
    concat, srt, t = [], [], 0.0
    for i, (s, r) in enumerate(rows):
        png, mp3, clip = BUILD / f"{i:03d}.png", BUILD / f"{i:03d}.mp3", BUILD / f"{i:03d}.mp4"
        draw_frame(r, s, i, total, png)
        dur = duration(mp3) + GAP
        if not clip.exists():
            subprocess.run(["ffmpeg", "-y", "-v", "error", "-loop", "1", "-framerate", "30", "-i", str(png),
                            "-i", str(mp3), "-t", f"{dur:.3f}", "-c:v", "libx264", "-tune", "stillimage",
                            "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-af", f"apad=pad_dur={GAP}",
                            "-shortest", str(clip)], check=True)
        concat.append(f"file '{clip.as_posix()}'")
        srt.append(f"{i + 1}\n{srt_time(t)} --> {srt_time(t + dur - GAP)}\n{r['vo']}\n")
        t += dur
        print(f"  clip {i + 1}/{total}  ({t/60:.1f} min)", end="\r")
    # end card, 6 s, silent
    png, clip = BUILD / "end.png", BUILD / "end.mp4"
    end_card(png)
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-loop", "1", "-framerate", "30", "-i", str(png),
                    "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono", "-t", "6", "-c:v", "libx264",
                    "-tune", "stillimage", "-pix_fmt", "yuv420p", "-c:a", "aac", "-shortest", str(clip)], check=True)
    concat.append(f"file '{clip.as_posix()}'")
    (BUILD / "concat.txt").write_text("\n".join(concat), encoding="utf-8")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(BUILD / "concat.txt"),
                    "-c", "copy", str(OUT_MP4)], check=True)
    OUT_SRT.write_text("\n".join(srt), encoding="utf-8")
    print(f"\nDone: {OUT_MP4}  length {t/60:.1f} min + 6 s end card;  subtitles: {OUT_SRT.name}")

if __name__ == "__main__":
    main()
