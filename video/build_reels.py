"""
build_reels.py
Cuts 12 vertical reels (1080x1920, under 60 s) for TikTok, Instagram Reels, Facebook Reels and YouTube Shorts
from the same footage (video/footage/) and narration (video/build/) as the main video.

Each reel = hook text over the first shot (first 3.5 s) + a themed run of script lines + a spoken call to action
to watch the full video on YouTube. Run after build_video_footage.py:   python video/build_reels.py
Outputs: video/reels/reel_NN.mp4, video/reels/captions.md (post text and hashtags per reel)
"""
import asyncio, subprocess
from pathlib import Path
from PIL import Image, ImageDraw
import edge_tts
import build_video as v1

ROOT = v1.ROOT
FOOT = ROOT / "video" / "footage"
OUT = ROOT / "video" / "reels"
WORK = OUT / "work"
W, H = 1080, 1920
GAP = 0.45                # shorter pause between lines than the long video
MAX_CONTENT = 54.5        # seconds of narration per reel; CTA adds about 4.5 s
CTA_TEXT = "Full story on YouTube. Search PYROS."

# Reels: hook shown on screen for the first seconds, then script lines (1-based row numbers) in order.
# Lines are added while the reel stays under MAX_CONTENT seconds; later lines are dropped if needed.
REELS = [
    ("Ten years to become a doctor. Then... a taxi.", [1, 2, 3, 4]),
    ("215 studies. Nobody asked this question.", [9, 10, 11, 12, 5]),
    ("Good news for migrant nurses", [17, 18, 19, 20, 21, 22]),
    ("Where does the pain live?", [23, 24, 25, 29]),
    ("Working below your level hurts", [26, 27, 28, 22]),
    ("He called 500 times. No answer.", [30, 31, 32, 34, 37]),
    ("A piece of cloth decided her future", [33, 35, 36, 37]),
    ("What helps: get back in the room", [38, 39, 40, 41]),
    ("Good colleagues. A real contract. Your own name.", [42, 43, 44]),
    ("Welcome is medicine", [45, 46, 51, 52]),
    ("How to read a study in 40 seconds", [13, 14, 15, 16, 8]),
    ("So, who suffers more?", [47, 48, 49, 50]),
]

def overlay(row, hook, path):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # darken top and bottom for legibility; keep the middle clean
    for y in range(0, 420):
        d.line([(0, y), (W, y)], fill=(10, 16, 22, int(190 * (1 - y / 420))))
    for y in range(H - 760, H):
        d.line([(0, y), (W, y)], fill=(10, 16, 22, int(215 * (y - (H - 760)) / 760)))
    m = 64
    d.text((m, 120), "PYROS", font=v1.F_MONO(30), fill=(235, 238, 240, 230))
    # hook (drawn on a separate layer, shown only for the first seconds)
    # on-screen phrase
    text = row["onscreen"]
    y_phrase_bottom = H - 720
    if text:
        is_quote = text.startswith(("\"", "“", "'"))
        fnt = v1.F_DISPLAY_I(62) if is_quote else v1.F_DISPLAY(66)
        lines = v1.wrap(d, text, fnt, W - 2 * m - 30)
        while len(lines) > 4 and fnt.size > 44:
            fnt = v1.F_DISPLAY_I(fnt.size - 6) if is_quote else v1.F_DISPLAY(fnt.size - 6)
            lines = v1.wrap(d, text, fnt, W - 2 * m - 30)
        lh = int(fnt.size * 1.2); block_h = len(lines) * lh + 36
        y0 = y_phrase_bottom - block_h
        d.rounded_rectangle([m - 18, y0, W - m + 18, y0 + block_h], radius=10, fill=(244, 246, 248, 228))
        d.rectangle([m - 18, y0, m - 6, y0 + block_h], fill=(184, 101, 27, 255))
        y = y0 + 16
        for ln in lines:
            d.text((m + 8, y), ln, font=fnt, fill=(22, 34, 46, 255)); y += lh
    # caption, above the platform UI zone (bottom ~330 px)
    sub = v1.F_BODY(46)
    cap = v1.wrap(d, row["vo"], sub, W - 2 * m)[:6]
    y = H - 360 - len(cap) * 58
    for ln in cap:
        d.text((m, y), ln, font=sub, fill=(245, 247, 248, 255)); y += 58
    img.save(path)

def hook_layer(hook, path):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    fnt = v1.F_DISPLAY(88)
    lines = v1.wrap(d, hook, fnt, W - 140)
    while len(lines) > 4 and fnt.size > 56:
        fnt = v1.F_DISPLAY(fnt.size - 6); lines = v1.wrap(d, hook, fnt, W - 140)
    lh = int(fnt.size * 1.15); y = 250
    d.rounded_rectangle([50, y - 30, W - 50, y + len(lines) * lh + 30], radius=14, fill=(184, 101, 27, 235))
    for ln in lines:
        d.text(((W - d.textlength(ln, font=fnt)) / 2, y), ln, font=fnt, fill=(255, 250, 244, 255)); y += lh
    img.save(path)

def cta_card(path):
    img = Image.new("RGB", (W, H), (22, 34, 46))
    d = ImageDraw.Draw(img)
    d.rectangle([64, 520, 78, 640], fill=(224, 146, 74))
    d.text((100, 520), "Watch the", font=v1.F_DISPLAY(80), fill=(244, 246, 248))
    d.text((100, 620), "full story", font=v1.F_DISPLAY(80), fill=(224, 146, 74))
    d.text((64, 800), "12 minutes on YouTube", font=v1.F_BODY(52), fill=(200, 210, 218))
    d.text((64, 900), "Search:", font=v1.F_BODY(44), fill=(150, 166, 178))
    d.text((64, 960), "PYROS", font=v1.F_MONO(64), fill=(244, 246, 248))
    d.text((64, 1050), "The doctor who drives a taxi", font=v1.F_DISPLAY_I(58), fill=(244, 246, 248))
    d.text((64, 1300), "Link in bio", font=v1.F_BODY(48), fill=(224, 146, 74))
    d.text((64, 1700), "github.com/Odogwu90/PYROS_rapid_review", font=v1.F_MONO(28), fill=(150, 166, 178))
    img.save(path)

def main():
    OUT.mkdir(exist_ok=True); WORK.mkdir(exist_ok=True)
    scenes = v1.parse_script(v1.SCRIPT.read_text(encoding="utf-8"))
    rows = [r for s in scenes for r in s["rows"]]
    cta_mp3 = WORK / "cta.mp3"
    if not cta_mp3.exists():
        asyncio.run(edge_tts.Communicate(CTA_TEXT, v1.VOICE, rate=v1.RATE).save(str(cta_mp3)))
    cta_png = WORK / "cta.png"; cta_card(cta_png)
    cta_dur = v1.duration(cta_mp3) + 0.6
    cta_clip = WORK / "cta.mp4"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-loop", "1", "-framerate", "30", "-i", str(cta_png), "-i", str(cta_mp3),
                    "-t", f"{cta_dur:.3f}", "-af", "apad=pad_dur=0.6", "-shortest", "-c:v", "libx264", "-tune", "stillimage",
                    "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", str(cta_clip)], check=True)
    captions = ["# Reel captions and hashtags\n",
                "Paste the caption, then the hashtag line. Put the YouTube link in the bio (Instagram, TikTok) or in the post (Facebook, YouTube Shorts).\n"]
    for n, (hook, wanted) in enumerate(REELS, 1):
        chosen, total = [], 0.0
        for rn in wanted:
            dur = v1.duration(v1.BUILD / f"{rn - 1:03d}.mp3") + GAP
            if total + dur > MAX_CONTENT:
                break
            chosen.append((rn, dur)); total += dur
        parts = []
        hk = WORK / f"r{n:02d}_hook.png"; hook_layer(hook, hk)
        for k, (rn, dur) in enumerate(chosen):
            i = rn - 1; row = rows[i]
            ov = WORK / f"r{n:02d}_{k}_ov.png"; overlay(row, hook, ov)
            out = WORK / f"r{n:02d}_{k}.mp4"
            src = FOOT / f"{i:03d}.mp4"
            vin = ["-stream_loop", "-1", "-i", str(src)] if src.exists() else ["-f", "lavfi", "-i", f"color=c=0x16222E:s={W}x{H}:r=30"]
            fc = (f"[0:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps=30,eq=brightness=-0.03:saturation=0.95[v0];"
                  f"[v0][1:v]overlay=0:0:format=auto[v1];")
            # input order: footage (0), overlay (1), then hook (2) on the first shot, and the narration mp3 last
            inputs = [*vin, "-i", str(ov)]
            if k == 0:
                inputs += ["-i", str(hk)]
                fc += "[v1][2:v]overlay=0:0:format=auto:enable='between(t,0,3.5)'[v]"
            else:
                fc += "[v1]null[v]"
            inputs += ["-i", str(v1.BUILD / f"{i:03d}.mp3")]
            mp3_idx = 3 if k == 0 else 2
            if not out.exists():
              subprocess.run(["ffmpeg", "-y", "-v", "error", *inputs, "-filter_complex", fc, "-map", "[v]", "-map", f"{mp3_idx}:a",
                            "-t", f"{dur:.3f}", "-af", f"apad=pad_dur={GAP}", "-shortest", "-c:v", "libx264", "-preset", "veryfast",
                            "-crf", "21", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-ar", "24000", str(out)], check=True)
            parts.append(out)
        concat = WORK / f"r{n:02d}_concat.txt"
        concat.write_text("\n".join(f"file '{p.as_posix()}'" for p in parts + [cta_clip]), encoding="utf-8")
        final = OUT / f"reel_{n:02d}.mp4"
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(concat), "-c", "copy", str(final)], check=True)
        length = total + cta_dur
        print(f"reel {n:02d}: {length:5.1f} s  lines {[rn for rn, _ in chosen]}  hook: {hook}")
        first_line = rows[chosen[0][0] - 1]["vo"]
        captions.append(f"\n## Reel {n:02d} ({length:.0f} s): {hook}\n\n{first_line} Full 12-minute video on YouTube: search PYROS, The doctor who drives a taxi.\n\n"
                        "#skilledmigrants #migration #mentalhealth #doctorsabroad #nursesabroad #globalhealth #brainwaste #PYROS #depressivesymptoms #immigrantlife\n")
    (OUT / "captions.md").write_text("".join(captions), encoding="utf-8")
    print("done:", OUT)

if __name__ == "__main__":
    main()
