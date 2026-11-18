import math
from PIL import Image, ImageDraw, ImageFilter

SRC = '/home/hatch/workspace/goals/paid-note-article-preparation/maru-spec/maru-normal.png'
OUT = '/home/hatch/workspace/goals/paid-note-article-preparation/maru-motion-test/frames'
W = H = 1080
FPS = 30
DUR = 3.0
N = int(FPS * DUR)
BG = (246, 241, 231, 255)
SIZE = 620  # maru display size

maru0 = Image.open(SRC).convert('RGBA').resize((SIZE, SIZE), Image.LANCZOS)
GROUND_Y = 880  # bottom of maru at rest
CX = W // 2

def ease_out(p): return 1 - (1 - p) ** 3

for i in range(N):
    t = i / FPS
    # --- motion timeline (whole-sphere transforms only: translate + rotate) ---
    if t < 0.9:            # idle bob
        lift = 5 * (1 - math.cos(2 * math.pi * t / 0.9)) / 2
        roll = 1.5 * math.sin(2 * math.pi * t / 0.9)
        shadow_s = 1.0
    elif t < 1.5:          # big hop
        p = (t - 0.9) / 0.6
        lift = 130 * math.sin(math.pi * p)
        roll = 6 * math.sin(math.pi * p)
        shadow_s = 1 - 0.35 * math.sin(math.pi * p)
    elif t < 2.1:          # happy double bounce
        p = ((t - 1.5) % 0.3) / 0.3
        lift = 34 * math.sin(math.pi * p)
        roll = 3 * math.sin(2 * math.pi * (t - 1.5) / 0.6)
        shadow_s = 1 - 0.12 * math.sin(math.pi * p)
    else:                  # settle
        p = (t - 2.1) / 0.9
        lift = (1 - ease_out(p)) * 6 + 3 * (1 - math.cos(2 * math.pi * (t - 2.1) / 0.9)) / 2 * ease_out(p)
        roll = (1 - ease_out(p)) * 2 * math.sin(2 * math.pi * (t - 2.1) / 0.45)
        shadow_s = 1.0

    frame = Image.new('RGBA', (W, H), BG)
    # shadow
    sh_w = int(430 * shadow_s); sh_h = int(56 * shadow_s)
    shadow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(shadow)
    d.ellipse([CX - sh_w // 2, GROUND_Y + 18 - sh_h // 2, CX + sh_w // 2, GROUND_Y + 18 + sh_h // 2],
              fill=(90, 70, 50, int(70 * shadow_s)))
    shadow = shadow.filter(ImageFilter.GaussianBlur(10))
    frame = Image.alpha_composite(frame, shadow)
    # maru (rotate whole sphere, then translate)
    m = maru0.rotate(-roll, resample=Image.BICUBIC, center=(SIZE // 2, SIZE // 2))
    x = CX - SIZE // 2
    y = int(GROUND_Y - SIZE - lift)
    frame.alpha_composite(m, (x, y))
    frame.convert('RGB').save(f'{OUT}/{i:03d}.png')
print('frames done', N)
