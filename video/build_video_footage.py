"""
build_video_footage.py
Version 2 of the video: real stock footage under the narration.

For each line of video/script.md:
  1. take the narration MP3 already made by build_video.py (video/build/NNN.mp3)
  2. search Pexels Videos for the query in video/shotlist.csv, download the best HD clip
     (cached in video/footage/NNN.mp4; delete a file there to force a new pick)
  3. loop or trim the clip to the narration length, fit to 1920x1080
  4. overlay a transparent PNG drawn with Pillow: on-screen phrase, caption band, scene label
  5. mux with the narration; then concatenate all shots and the end card

Pexels key: put it in video/.pexels_key (one line, git-ignored) or the PEXELS_API_KEY variable.
Run from the project root after build_video.py has run once:  python video/build_video_footage.py
Output: video/pyros_video_v2.mp4, video/footage_credits.csv (Pexels author and link for every clip).
"""
import csv, json, os, subprocess, sys, time
from pathlib import Path
import requests
from PIL import Image, ImageDraw
import build_video as v1   # reuse the parser, fonts, palette, end card and timing helpers

ROOT = v1.ROOT
FOOT = ROOT / "video" / "footage"
BUILD2 = ROOT / "video" / "build2"
OUT_MP4 = ROOT / "video" / "pyros_video_v2.mp4"
CREDITS = ROOT / "video" / "footage_credits.csv"
W, H = v1.W, v1.H

def api_key():
    k = os.environ.get("PEXELS_API_KEY")
    f = ROOT / "video" / ".pexels_key"
    if not k and f.exists():
        k = f.read_text(encoding="utf-8").strip()
    if not k:
        sys.exit("No Pexels key. Put it in video/.pexels_key or set PEXELS_API_KEY.")
    return k

def pexels_search(query, key, per_page=8):
    r = requests.get("https://api.pexels.com/videos/search",
                     headers={"Authorization": key},
                     params={"query": query, "per_page": per_page, "orientation": "landscape", "size": "medium"},
                     timeout=30)
    r.raise_for_status()
    return r.json().get("videos", [])

def best_file(video):
    files = [f for f in video.get("video_files", []) if f.get("width") and 1280 <= f["width"] <= 1920 and f.get("file_type") == "video/mp4"]
    if not files:
        return None
    return sorted(files, key=lambda f: -f["width"])[0]

def fetch_clip(i, row, key, credits):
    dst = FOOT / f"{i:03d}.mp4"
    meta = FOOT / f"{i:03d}.json"
    if dst.exists() and meta.exists():
        credits.append(json.loads(meta.read_text(encoding="utf-8")))
        return dst
    for q in (row["search_query"], row["fallback_query"]):
        try:
            vids = pexels_search(q, key)
        except requests.HTTPError as e:
            print(f"\n  search failed for '{q}': {e}")
            vids = []
        for v in vids:
            f = best_file(v)
            if not f:
                continue
            data = requests.get(f["link"], timeout=120).content
            dst.write_bytes(data)
            info = {"row": i, "query": q, "pexels_url": v["url"], "author": v["user"]["name"],
                    "author_url": v["user"]["url"], "duration_s": v.get("duration")}
            meta.write_text(json.dumps(info), encoding="utf-8")
            credits.append(info)
            time.sleep(0.3)
            return dst
    return None

def overlay_png(row, scene, idx, total, path):
    """Transparent layer: dark gradient at the bottom, caption text, on-screen phrase, scene label."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # bottom gradient for caption legibility
    for y in range(H - 420, H):
        a = int(210 * (y - (H - 420)) / 420)
        d.line([(0, y), (W, y)], fill=(10, 16, 22, a))
    # top strip for labels
    for y in range(0, 140):
        a = int(140 * (1 - y / 140))
        d.line([(0, y), (W, y)], fill=(10, 16, 22, a))
    margin = 120
    d.text((margin, 46), "PYROS  ·  THE DOCTOR WHO DRIVES A TAXI", font=v1.F_MONO(24), fill=(235, 238, 240, 230))
    lab = f"SCENE {scene['num']}"
    d.text((W - margin - d.textlength(lab, font=v1.F_MONO(24)), 46), lab, font=v1.F_MONO(24), fill=(235, 238, 240, 230))
    # on-screen phrase (only when the script gives one)
    text = row["onscreen"]
    if text:
        is_quote = text.startswith(("\"", "“", "'"))
        fnt = v1.F_DISPLAY_I(70) if is_quote else v1.F_DISPLAY(74)
        lines = v1.wrap(d, text, fnt, W - 2 * margin - 40)
        while len(lines) > 3 and fnt.size > 44:
            fnt = v1.F_DISPLAY_I(fnt.size - 6) if is_quote else v1.F_DISPLAY(fnt.size - 6)
            lines = v1.wrap(d, text, fnt, W - 2 * margin - 40)
        block_h = len(lines) * int(fnt.size * 1.18) + 40
        y0 = H - 420 - block_h - 10
        # soft plate behind the phrase
        d.rounded_rectangle([margin - 24, y0 - 6, margin + max(d.textlength(l, font=fnt) for l in lines) + 44, y0 + block_h - 20],
                            radius=8, fill=(244, 246, 248, 225))
        d.rectangle([margin - 24, y0 - 6, margin - 12, y0 + block_h - 20], fill=(184, 101, 27, 255))
        y = y0 + 12
        for ln in lines:
            d.text((margin + 6, y), ln, font=fnt, fill=(22, 34, 46, 255))
            y += int(fnt.size * 1.18)
    # caption
    sub = v1.F_BODY(40)
    for k, ln in enumerate(v1.wrap(d, row["vo"], sub, W - 2 * margin)[:4]):
        d.text((margin, H - 250 + k * 50), ln, font=sub, fill=(245, 247, 248, 255))
    # progress
    bar_w = W - 2 * margin
    d.rectangle([margin, H - 26, margin + bar_w, H - 22], fill=(255, 255, 255, 90))
    d.rectangle([margin, H - 26, margin + int(bar_w * (idx + 1) / total), H - 22], fill=(224, 146, 74, 255))
    img.save(path)

def main():
    key = api_key()
    FOOT.mkdir(exist_ok=True); BUILD2.mkdir(exist_ok=True)
    scenes = v1.parse_script(v1.SCRIPT.read_text(encoding="utf-8"))
    rows = [(s, r) for s in scenes for r in s["rows"]]
    total = len(rows)
    shots = {int(r["row"]) - 1: r for r in csv.DictReader(open(ROOT / "video" / "shotlist.csv", encoding="utf-8"))}
    assert len(shots) == total, f"shotlist has {len(shots)} rows, script has {total}"
    credits, concat, srt, t = [], [], [], 0.0
    for i, (s, r) in enumerate(rows):
        mp3 = v1.BUILD / f"{i:03d}.mp3"
        if not mp3.exists():
            sys.exit("Run build_video.py first to create the narration.")
        dur = v1.duration(mp3) + v1.GAP
        clip = fetch_clip(i, shots[i], key, credits)
        ov = BUILD2 / f"{i:03d}_overlay.png"
        overlay_png(r, s, i, total, ov)
        out = BUILD2 / f"{i:03d}.mp4"
        if not out.exists():
            if clip is None:
                # no footage found: fall back to the typographic frame from version 1
                v1.draw_frame(r, s, i, total, BUILD2 / f"{i:03d}_still.png")
                vin = ["-loop", "1", "-framerate", "30", "-i", str(BUILD2 / f"{i:03d}_still.png")]
                vf = "[0:v]"
            else:
                vin = ["-stream_loop", "-1", "-i", str(clip)]
                vf = "[0:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=30,eq=brightness=-0.03:saturation=0.95[v0];[v0]"
            filt = vf + "[1:v]overlay=0:0:format=auto[v]" if clip else "[0:v][1:v]overlay=0:0:format=auto[v]"
            subprocess.run(["ffmpeg", "-y", "-v", "error", *vin, "-i", str(ov), "-i", str(mp3),
                            "-filter_complex", filt, "-map", "[v]", "-map", "2:a",
                            "-t", f"{dur:.3f}", "-af", f"apad=pad_dur={v1.GAP}", "-shortest",
                            "-c:v", "libx264", "-preset", "veryfast", "-crf", "21", "-pix_fmt", "yuv420p",
                            "-c:a", "aac", "-b:a", "160k", str(out)], check=True)
        concat.append(f"file '{out.as_posix()}'")
        srt.append(f"{i + 1}\n{v1.srt_time(t)} --> {v1.srt_time(t + dur - v1.GAP)}\n{r['vo']}\n")
        t += dur
        print(f"  shot {i + 1}/{total}  ({t/60:.1f} min)  {'footage' if clip else 'still'}", end="\r")
    end_png, end_clip = BUILD2 / "end.png", BUILD2 / "end.mp4"
    v1.end_card(end_png)
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-loop", "1", "-framerate", "30", "-i", str(end_png),
                    "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono", "-t", "6", "-c:v", "libx264",
                    "-tune", "stillimage", "-pix_fmt", "yuv420p", "-c:a", "aac", "-shortest", str(end_clip)], check=True)
    concat.append(f"file '{end_clip.as_posix()}'")
    (BUILD2 / "concat.txt").write_text("\n".join(concat), encoding="utf-8")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(BUILD2 / "concat.txt"),
                    "-c", "copy", str(OUT_MP4)], check=True)
    (ROOT / "video" / "pyros_video_v2.srt").write_text("\n".join(srt), encoding="utf-8")
    with open(CREDITS, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["row", "query", "pexels_url", "author", "author_url", "duration_s"])
        w.writeheader(); w.writerows(sorted(credits, key=lambda c: c["row"]))
    print(f"\nDone: {OUT_MP4}  length {t/60:.1f} min + 6 s end card; credits in {CREDITS.name}")

if __name__ == "__main__":
    main()
