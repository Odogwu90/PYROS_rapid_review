"""Make YouTube thumbnail options (1280x720) from frames of the film's own footage."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageEnhance

ROOT = Path(__file__).resolve().parents[1]
T = ROOT / "video" / "thumbnails"
W, H = 1280, 720
F = Path(r"C:\Windows\Fonts")
BLACK = lambda s: ImageFont.truetype(str(F / "seguibl.ttf"), s)   # Segoe UI Black
SERIF = lambda s: ImageFont.truetype(str(F / "georgiab.ttf"), s)
MONO = lambda s: ImageFont.truetype(str(F / "consola.ttf"), s)
INK = (22, 34, 46); PAPER = (244, 246, 248); ACCENT = (232, 140, 40); AMBER = (255, 196, 84)

def base(src, dark=0.55, blur=0):
    im = Image.open(src).convert("RGB")
    s = max(W / im.width, H / im.height)
    im = im.resize((int(im.width * s) + 1, int(im.height * s) + 1), Image.LANCZOS)
    im = im.crop(((im.width - W) // 2, (im.height - H) // 2, (im.width - W) // 2 + W, (im.height - H) // 2 + H))
    if blur:
        im = im.filter(ImageFilter.GaussianBlur(blur))
    im = ImageEnhance.Brightness(im).enhance(dark)
    return im

def outlined(d, xy, text, fnt, fill, outline=INK, w=6):
    x, y = xy
    for dx in range(-w, w + 1, 2):
        for dy in range(-w, w + 1, 2):
            d.text((x + dx, y + dy), text, font=fnt, fill=outline)
    d.text((x, y), text, font=fnt, fill=fill)

def tag(d, x, y):
    d.rounded_rectangle([x, y, x + 150, y + 44], radius=6, fill=PAPER)
    d.text((x + 16, y + 6), "PYROS", font=MONO(30), fill=INK)

# Option A: taxi at night, three-line punch
im = base(T / "src_taxi.png", dark=0.7)
d = ImageDraw.Draw(im)
outlined(d, (60, 70), "10 YEARS", BLACK(150), PAPER)
outlined(d, (60, 230), "TO BECOME", BLACK(96), PAPER)
outlined(d, (60, 335), "A DOCTOR.", BLACK(96), PAPER)
outlined(d, (60, 480), "THEN... A TAXI.", BLACK(120), AMBER)
tag(d, 1070, 640)
im.save(T / "thumb_A_taxi.jpg", quality=92)

# Option B: white coat, question format
im = base(T / "src_coat.png", dark=0.6, blur=1)
d = ImageDraw.Draw(im)
d.rectangle([0, 0, 560, H], fill=(22, 34, 46))
d.rectangle([560, 0, 574, H], fill=ACCENT)
d.text((50, 70), "WHO", font=BLACK(140), fill=PAPER)
d.text((50, 215), "SUFFERS", font=BLACK(110), fill=AMBER)
d.text((50, 335), "MORE?", font=BLACK(140), fill=PAPER)
d.text((50, 520), "The doctor who starts over,", font=SERIF(30), fill=(200, 210, 218))
d.text((50, 562), "or the graduate who", font=SERIF(30), fill=(200, 210, 218))
d.text((50, 604), "starts fresh?", font=SERIF(30), fill=(200, 210, 218))
tag(d, 1070, 640)
im.save(T / "thumb_B_question.jpg", quality=92)

# Option C: ladder into sky, the surprise
im = base(T / "src_ladder.png", dark=0.75)
d = ImageDraw.Draw(im)
outlined(d, (60, 60), "NOBODY", BLACK(160), PAPER)
outlined(d, (60, 230), "HAS STUDIED", BLACK(96), PAPER)
outlined(d, (60, 335), "THIS.", BLACK(160), AMBER)
d.rounded_rectangle([60, 560, 760, 640], radius=10, fill=PAPER)
d.text((80, 572), "Skilled migrants. 7 studies. 1 gap.", font=SERIF(40), fill=INK)
tag(d, 1070, 640)
im.save(T / "thumb_C_nobody.jpg", quality=92)

# Contact sheet
sheet = Image.new("RGB", (W + 40, 3 * (H // 2) + 80), PAPER)
for k, n in enumerate(["thumb_A_taxi.jpg", "thumb_B_question.jpg", "thumb_C_nobody.jpg"]):
    t = Image.open(T / n).resize((W // 2, H // 2))
    sheet.paste(t, (20 + (k % 2) * 0 + (20 if k == 1 else 0) + (0 if k != 1 else 0), 20 + k * (H // 2 + 20)))
sheet.save(T / "thumb_options.png")
print("done")
