# render.py — draws entry.png for news-image-20261120 v2 (build time only).
# "THE WORLD IN ONE DAY" — Friday 20 November 2026. 36 verified stories.
# All text is Liberation Serif / Liberation Sans. No character outside the
# Liberation cmap is used (verified with fontTools); the checkmark in the
# DATE CHECK band is drawn with line segments, never the U+2713 glyph.
# Every number, date and name below was verified against a live source on
# 20 Nov 2026; the per-fact table lives in EVIDENCE.md next to this repo.
import math
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

FDIR = "/usr/share/fonts/truetype/liberation"
SERIF = os.path.join(FDIR, "LiberationSerif-Regular.ttf")
SERIF_B = os.path.join(FDIR, "LiberationSerif-Bold.ttf")
SERIF_I = os.path.join(FDIR, "LiberationSerif-Italic.ttf")
SERIF_BI = os.path.join(FDIR, "LiberationSerif-BoldItalic.ttf")
SANS = os.path.join(FDIR, "LiberationSans-Regular.ttf")
SANS_B = os.path.join(FDIR, "LiberationSans-Bold.ttf")
SANS_I = os.path.join(FDIR, "LiberationSans-Italic.ttf")


def F(path, size):
    return ImageFont.truetype(path, size)


PAPER = (247, 241, 227)
INK = (25, 25, 25)
RED = (163, 30, 34)
DRED = (126, 20, 24)
NAVY = (22, 50, 79)
DNAVY = (14, 34, 54)
OCEAN = (30, 74, 107)
CREAM = (232, 220, 195)
LINE = (201, 191, 165)
GOLD = (201, 162, 39)
YELL = (255, 214, 90)
TEAL = (30, 107, 90)
GREEN = (46, 110, 63)
GREY = (90, 90, 90)

REGIONS = [
    ("EUROPE", 8, (36, 72, 107)),
    ("AMERICAS", 7, (158, 43, 37)),
    ("ASIA-PACIFIC", 10, (46, 107, 79)),
    ("MIDEAST", 2, (140, 106, 31)),
    ("AFRICA", 2, (107, 78, 142)),
    ("OCEANIA", 3, (46, 107, 122)),
    ("WORLD", 4, (85, 85, 85)),
]

STATS = [
    ("300,000+", "evacuated before Akvan"),
    ("3", "killed in Kyiv strikes"),
    ("\u22127%", "MSCI Asia-Pacific, week"),
    ("$97.17", "Anthropic first close, +17%"),
    ("118", "Phillips century vs India"),
    ("18th", "China holds rates"),
]

LEADS = [
    {
        "kicker": "01 \u00b7 ODISHA, INDIA \u00b7 CYCLONE",
        "head": "Cyclone Akvan makes landfall in eastern India",
        "deck": "Severe storm crosses near Gopalpur; 300,000+ evacuated, "
                "423 rescue teams out, 9,341 shelters readied. Winds "
                "70\u201380, gusting 90 km/h at landfall. (IMD, Reuters)",
    },
    {
        "kicker": "02 \u00b7 KYIV, UKRAINE \u00b7 WAR",
        "head": "Russia fires wave of ballistic missiles at Kyiv",
        "deck": "Overnight strikes hit three bridges and cut power in five "
                "districts; 3 killed, about 15 hurt. First blasts about "
                "01:25 local. (Reuters, Kyiv Independent)",
    },
    {
        "kicker": "03 \u00b7 ANTALYA, T\u00dcRKIYE \u00b7 CLIMATE",
        "head": "COP31 reaches its final day deadlocked",
        "deck": "Draft drops fossil-fuel phase-out and the $120bn "
                "adaptation target; hosts push \u201c35 by 35\u201d "
                "clean-power goal; talks may run past Friday. "
                "(UN News, Reuters)",
    },
]

CARDS = [
    {
        "kicker": "04 \u00b7 SEOUL / TOKYO \u00b7 MARKETS",
        "head": "AI sell-off sinks Asia to worst week since 2020",
        "deck": "Nikkei \u22124.8%, KOSPI \u22124.7%, TAIEX \u22126.8%. "
                "Intraday lows. (Reuters)",
    },
    {
        "kicker": "05 \u00b7 NEW YORK \u00b7 MARKETS",
        "head": "Anthropic ends first day up 17%",
        "deck": "Opens $111.50, closes $97.17, +17% vs $83 offer. "
                "(WSJ, Barron's)",
    },
    {
        "kicker": "06 \u00b7 TOKYO \u00b7 ECONOMY",
        "head": "Japan core inflation 2.2%",
        "deck": "Core CPI 2.2% in October, up from 2.1%; BoJ hike eyed "
                "18 Dec. (Reuters)",
    },
    {
        "kicker": "07 \u00b7 BEIJING \u00b7 RATES",
        "head": "China holds lending rates for 18th month",
        "deck": "1-year 3.0%, 5-year 3.5%, unchanged since May 2025. "
                "(Reuters, PBoC)",
    },
    {
        "kicker": "08 \u00b7 MERCURY \u00b7 SPACE",
        "head": "BepiColombo reaches Mercury after 8 years",
        "deck": "ESA/JAXA probe ends a 6bn-mile trip; orbit insertion "
                "Saturday. (ESA)",
    },
    {
        "kicker": "09 \u00b7 WELLINGTON \u00b7 CRICKET",
        "head": "Phillips makes history with 118",
        "deck": "First NZ batter with centuries in all 3 formats vs India "
                "in a year. (ICC)",
    },
    {
        "kicker": "10 \u00b7 SAN SALVADOR \u00b7 POLITICS",
        "head": "Bukele files to run for third term",
        "deck": "Registers for the 28 Feb 2027 vote after term limits "
                "scrapped. (Reuters)",
    },
    {
        "kicker": "11 \u00b7 BRUSSELS \u00b7 EUROPE",
        "head": "Burnham holds second EU\u2013UK reset summit",
        "deck": "Costa & von der Leyen host the UK PM; food, carbon deals "
                "eyed. (EU Council)",
    },
    {
        "kicker": "12 \u00b7 HORMUZ \u00b7 ENERGY",
        "head": "US memo warns of wider Gulf ship risk",
        "deck": "Memo says Gulf ship threat has spread; war-risk cover up "
                "~200\u00d7. (Al Jazeera)",
    },
    {
        "kicker": "13 \u00b7 WORLD \u00b7 GAMES",
        "head": "GTA VI's first full day on sale",
        "deck": "First full day on sale; launch-day sales near $2.36bn, a "
                "record. (Sensor Tower)",
    },
]

ALSO_LEFT = [
    ("ROME", "CGIL 24-hour strike; rallies in ~100 squares. (Adnkronos)"),
    ("YENNE", "Boat capsizes; 4 dead, dozens missing. (Al Jazeera)"),
    ("BARCELONA", "Cancer pill shrinks tumours in 60.7% of 61. (EORTC)"),
    ("SHENZHEN", "Trump, Xi, Putin publish joint peace declaration. (CNA)"),
    ("TONGA", "Drought emergency in force; schools close early. (RNZ)"),
    ("LAS VEGAS", "Russell fastest in wet FP2, 1:47.272. (Formula1.com)"),
    ("CALIFORNIA", "Nvidia subpoenaed over China chip claims. (Reuters)"),
    ("TURIN", "Alcaraz\u2013Cobolli, Medvedev\u2013Tiafoe close ATP groups. (ATP)"),
    ("SEOUL", "Ruling party adopts Cho impeachment line. (Korea Times)"),
    ("COPENHAGEN", "Parliament backs Greenland deal, 109\u20130. (AFP)"),
    ("JAKARTA", "Asset-forfeiture law passes after 18 years. (Reuters)"),
    ("CINCINNATI", "Hippo Fiona dies at 9 after swallowing a hat. (AP)"),
]
ALSO_RIGHT = [
    ("DOHA", "Australia stun Argentina 2\u20130 in U17 opener. (FIFA)"),
    ("HONG KONG", "Hang Seng about 20% off its January peak. (Reuters)"),
    ("TAIPEI", "TAIEX worst week since 1991, down about 16%. (Reuters)"),
    ("LONDON", "Gold \u22120.6% to $3,601.40; Brent flat at $91.98. (Reuters)"),
    ("DAKAR", "Navy rescues 1,400+ migrants in 48 hours. (Reuters)"),
    ("KHARKIV", "Drone hits a hospital; 4 hurt. (Reuters)"),
    ("NEW YORK", "Anthropic slides 4.7% after hours to $92.60. (Finnhub)"),
    ("GLOBAL", "UN marks World Children's Day. (UN)"),
    ("WELLINGTON", "Nicholls 175* in 216-run stand with Phillips. (ICC)"),
    ("MATO GROSSO", "Lula visits ailing chief Raoni, 94. (Al Jazeera)"),
    ("TOKYO", "Nikkei intraday low near 56,595. (Reuters)"),
]

LEFT_OUT = ("Trump\u2013Xi\u2013Putin Shenzhen summit itself \u00b7 Anthropic's $83 IPO pricing "
            "& Nasdaq debut \u00b7 ICJ Myanmar Rohingya verdict \u00b7 GTA VI midnight launch \u00b7 "
            "$190.4m Van Gogh sale \u00b7 Senate 51\u201348 Iran war-powers vote \u00b7 EU's "
            "\u20ac45bn Ukraine loan \u00b7 Crimea bridge strike \u00b7 Houthi strike on Riyadh \u00b7 "
            "Colombia tax protests \u00b7 Han Duck-soo ruling \u00b7 Voyager 1 one light-day out \u00b7 "
            "Jeffries named US Speaker \u00b7 Fiji drought declaration")


def wrap(d, text, font, width):
    """Greedy word wrap; returns a list of lines that fit `width`."""
    words = text.split(" ")
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if d.textlength(trial, font=font) <= width or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(d, x, y, text, font, width, fill, spacing=3, align="left"):
    lines = wrap(d, text, font, width)
    for ln in lines:
        if align == "center":
            lx = x + (width - d.textlength(ln, font=font)) / 2
        elif align == "right":
            lx = x + width - d.textlength(ln, font=font)
        else:
            lx = x
        d.text((lx, y), ln, font=font, fill=fill)
        y += font.size + spacing
    return y


def text_w(d, text, font):
    return d.textlength(text, font=font)


def draw_masthead(d):
    d.text((16, 10), "THE WORLD IN ONE DAY", font=F(SANS_B, 14), fill=RED)
    r = "FRIDAY'S NEWS \u00b7 ONE PAGE \u00b7 36 STORIES"
    d.text((1024 - 16 - text_w(d, r, F(SANS_B, 11)), 12), r,
           font=F(SANS_B, 11), fill=INK)
    d.text((16, 30), "Friday 20 November 2026", font=F(SERIF_B, 54), fill=INK)
    deck = ("Cyclone Akvan strikes India \u00b7 Ballistic missiles hit Kyiv \u00b7 "
            "COP31 deadlocked on final day \u00b7 Asian AI sell-off")
    d.text((16, 90), deck, font=F(SERIF_I, 17), fill=RED)
    d.line([(16, 114), (1008, 114)], fill=INK, width=2)


def draw_stats(d):
    y0, y1 = 122, 168
    cw = 992 / 6.0
    for i, (num, cap) in enumerate(STATS):
        x = 16 + i * cw
        d.text((x + 8, y0), num, font=F(SERIF_B, 27), fill=RED)
        draw_wrapped(d, x + 8, y0 + 34, cap, F(SANS, 10), cw - 16, GREY, 1)
        if i:
            d.line([(x, y0 + 2), (x, y1 - 2)], fill=LINE, width=1)
    d.line([(16, y1 + 4), (1008, y1 + 4)], fill=LINE, width=1)


def draw_regions(d):
    y = 180
    x = 16
    for name, n, col in REGIONS:
        label = "%s %d" % (name, n)
        fnt = F(SANS_B, 11)
        w = text_w(d, label, fnt) + 16
        d.rectangle([x, y, x + w, y + 20], fill=col)
        d.text((x + 8, y + 3), label, font=fnt, fill=(255, 255, 255))
        x += w + 5
    r = "ALL STORIES: FRI 20 NOV 2026, ANY TIME ZONE"
    d.text((1008 - text_w(d, r, F(SANS_B, 10)), y + 4), r,
           font=F(SANS_B, 10), fill=INK)


# ---------------- lead panels ----------------

def spiral(d, cx, cy, r0, r1, turns, color, width, start=0.0):
    """Archimedean spiral drawn as a polyline."""
    pts = []
    steps = int(turns * 60)
    for i in range(steps + 1):
        t = i / steps
        ang = start + t * turns * 2 * math.pi
        r = r0 + (r1 - r0) * t
        pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
    d.line(pts, fill=color, width=width, joint="curve")


def lead_cyclone(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=DNAVY)
    # beige landmass, right side (eastern India coast)
    d.polygon([(x + w * 0.62, y), (x + w, y), (x + w, y + h),
               (x + w * 0.55, y + h), (x + w * 0.66, y + h * 0.55),
               (x + w * 0.60, y + h * 0.28)], fill=(214, 196, 158))
    d.line([(x + w * 0.62, y), (x + w * 0.60, y + h * 0.28),
            (x + w * 0.66, y + h * 0.55), (x + w * 0.55, y + h)],
           fill=(120, 100, 70), width=2)
    cx, cy = x + w * 0.38, y + h * 0.55
    # wind-streak arcs around the storm
    for rr, a0, a1 in [(76, -0.4, 1.2), (84, 2.2, 3.6), (68, 3.8, 5.2)]:
        pts = [(cx + rr * math.cos(a0 + (a1 - a0) * t / 24),
                cy + rr * math.sin(a0 + (a1 - a0) * t / 24)) for t in range(25)]
        d.line(pts, fill=(140, 180, 210), width=3, joint="curve")
    # double-ring spiral, big: fills ~70% of panel width
    spiral(d, cx, cy, 6, 66, 3.1, (255, 255, 255), 5)
    spiral(d, cx, cy, 3, 44, 2.6, (255, 214, 90), 3)
    d.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=RED)
    # rain bands
    for bx, by, bl in [(0.10, 0.16, 26), (0.16, 0.80, 20), (0.62, 0.12, 22)]:
        d.line([(x + w * bx, y + h * by), (x + w * bx + bl, y + h * by + 8)],
               fill=(140, 180, 210), width=3)
    # Gopalpur marker on the coast
    gx, gy = x + w * 0.615, y + h * 0.42
    d.ellipse([gx - 4, gy - 4, gx + 4, gy + 4], fill=RED,
              outline=(255, 255, 255), width=2)
    d.text((gx + 10, gy + 10), "GOPALPUR", font=F(SANS_B, 11), fill=INK)
    d.text((x + 10, y + 8), "BAY OF BENGAL", font=F(SANS_B, 10),
           fill=(170, 205, 230))
    # bold in-panel label band
    d.rectangle([x, y + h - 26, x + w, y + h], fill=RED)
    d.text((x + 10, y + h - 21), "LANDFALL",
           font=F(SANS_B, 13), fill=(255, 255, 255))
    lab = "70\u201380 GUSTING 90 KM/H"
    d.text((x + w - 10 - text_w(d, lab, F(SANS_B, 11)), y + h - 20), lab,
           font=F(SANS_B, 11), fill=YELL)


def lead_kyiv(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(10, 22, 40))
    # stars
    for sx, sy in [(0.08, 0.12), (0.22, 0.07), (0.45, 0.10), (0.60, 0.06),
                   (0.78, 0.14), (0.92, 0.08), (0.33, 0.16), (0.55, 0.18)]:
        d.ellipse([x + w * sx, y + h * sy, x + w * sx + 2, y + h * sy + 2],
                  fill=(200, 210, 230))
    # missile trails: 6 arcs with head dots
    trails = [(0.06, 0.98, 0.42, 0.30), (0.18, 1.02, 0.55, 0.22),
              (0.30, 0.98, 0.66, 0.34), (0.44, 1.00, 0.78, 0.26),
              (0.58, 0.96, 0.88, 0.38), (0.72, 1.00, 0.96, 0.30)]
    for x0, y0, x1, y1 in trails:
        pts = []
        for t in range(21):
            u = t / 20
            px = x + w * (x0 + (x1 - x0) * u)
            py = y + h * (y0 + (y1 - y0) * u - 0.22 * math.sin(u * math.pi))
            pts.append((px, py))
        d.line(pts, fill=(255, 140, 60), width=3, joint="curve")
        d.ellipse([pts[-1][0] - 3, pts[-1][1] - 3, pts[-1][0] + 3, pts[-1][1] + 3],
                  fill=YELL)
    # dense skyline: 9 buildings with lit windows
    base = y + h * 0.78
    bw = w / 9.0
    heights = [0.42, 0.30, 0.50, 0.36, 0.58, 0.32, 0.46, 0.28, 0.40]
    for i, hh in enumerate(heights):
        bx = x + i * bw + 2
        by = base - h * hh
        d.rectangle([bx, by, bx + bw - 4, base + h * 0.22], fill=(5, 12, 24),
                    outline=(40, 60, 90), width=1)
        for wy in range(3):
            for wx in range(2):
                if (i * 2 + wy + wx) % 3:
                    d.rectangle([bx + 4 + wx * 9, by + 6 + wy * 12,
                                 bx + 8 + wx * 9, by + 10 + wy * 12],
                                fill=YELL)
    # bridge silhouette across the bottom
    d.line([(x, base + h * 0.16), (x + w, base + h * 0.16)], fill=(70, 90, 120),
           width=4)
    for bx in [0.2, 0.5, 0.8]:
        d.line([(x + w * bx, base + h * 0.16), (x + w * bx, base + h * 0.02)],
               fill=(70, 90, 120), width=3)
    # fire glows
    for fx, fy, fr in [(0.24, 0.74, 12), (0.62, 0.70, 10), (0.85, 0.76, 9)]:
        d.ellipse([x + w * fx - fr, y + h * fy - fr, x + w * fx + fr,
                   y + h * fy + fr], fill=(255, 120, 40))
        d.ellipse([x + w * fx - fr // 2, y + h * fy - fr // 2,
                   x + w * fx + fr // 2, y + h * fy + fr // 2], fill=YELL)
    # bold labels
    d.rectangle([x + 10, y + 8, x + 96, y + 30], fill=RED)
    d.text((x + 16, y + 12), "3 KILLED", font=F(SANS_B, 13), fill=(255, 255, 255))
    d.rectangle([x + 104, y + 8, x + 200, y + 30], fill=(255, 255, 255))
    d.text((x + 110, y + 12), "3 BRIDGES", font=F(SANS_B, 13), fill=DRED)
    d.text((x + w - 104, y + 12), "01:25 LOCAL", font=F(SANS_B, 11), fill=YELL)


def lead_cop(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(238, 232, 214))
    # globe, big, left
    gx, gy, gr = x + 78, y + 62, 48
    d.ellipse([gx - gr, gy - gr, gx + gr, gy + gr], fill=(70, 130, 180),
              outline=NAVY, width=2)
    # continents on the globe
    d.polygon([(gx - 34, gy - 18), (gx - 12, gy - 30), (gx + 2, gy - 14),
               (gx - 8, gy + 2), (gx - 26, gy + 6)], fill=(90, 160, 90))
    d.polygon([(gx + 8, gy + 6), (gx + 30, gy - 2), (gx + 36, gy + 16),
               (gx + 18, gy + 30), (gx + 2, gy + 22)], fill=(90, 160, 90))
    d.polygon([(gx - 6, gy + 26), (gx + 10, gy + 34), (gx + 2, gy + 44),
               (gx - 14, gy + 38)], fill=(120, 180, 110))
    d.arc([gx - gr, gy - gr, gx + gr, gy + gr], 200, 340, fill=(255, 255, 255),
          width=2)
    d.text((x + 10, y + 8), "ANTALYA \u00b7 NOV 20",
           font=F(SANS_B, 10), fill=INK)
    # thermometer, right of globe
    tx = x + 168
    d.rounded_rectangle([tx, y + 14, tx + 26, y + 92], radius=13,
                        outline=INK, width=2, fill=(255, 255, 255))
    d.rectangle([tx + 6, y + 52, tx + 20, y + 86], fill=RED)
    d.ellipse([tx - 4, y + 82, tx + 30, y + 112], fill=RED, outline=INK, width=2)
    d.line([(tx + 30, y + 30), (tx + 42, y + 30)], fill=INK, width=2)
    d.line([(tx + 30, y + 52), (tx + 42, y + 52)], fill=INK, width=2)
    d.line([(tx + 30, y + 74), (tx + 42, y + 74)], fill=INK, width=2)
    d.text((tx + 46, y + 22), "1.5\u00b0C", font=F(SANS_B, 11), fill=INK)
    # bold red title block
    d.rectangle([x + 168, y + 118, x + w - 10, y + 138], fill=RED)
    d.text((x + 176, y + 122), "FINAL DAY \u00b7 DEADLOCK",
           font=F(SANS_B, 11), fill=(255, 255, 255))
    d.text((x + 10, y + 118), "$120BN FINANCE GAP",
           font=F(SANS_B, 12), fill=RED)


def draw_leads(d):
    y, h = 206, 246
    xs = [16, 352, 688]
    w = 320
    painters = [lead_cyclone, lead_kyiv, lead_cop]
    for i, lead in enumerate(LEADS):
        x = xs[i]
        d.rectangle([x, y, x + w, y + h], outline=INK, width=1)
        painters[i](d, x + 1, y + 1, w - 2, 138)
        ty = y + 146
        d.text((x, ty), lead["kicker"], font=F(SANS_B, 10), fill=RED)
        ty += 14
        ty = draw_wrapped(d, x, ty, lead["head"], F(SERIF_B, 19), w, INK, 1)
        draw_wrapped(d, x, ty + 2, lead["deck"], F(SERIF, 12), w, INK, 1)


# ---------------- card panels ----------------

def panel_asia(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=DNAVY)
    pts = [(x + 8, y + 6), (x + 52, y + 12), (x + 84, y + 8),
           (x + 118, y + 22), (x + 150, y + 30), (x + w - 8, y + 38)]
    d.line(pts, fill=(255, 80, 70), width=3, joint="curve")
    for px, py in pts:
        d.ellipse([px - 2, py - 2, px + 2, py + 2], fill=YELL)
    d.rectangle([x + 8, y + h - 22, x + 92, y + h - 4], fill=RED)
    d.text((x + 12, y + h - 20), "ASIA \u22127% WK", font=F(SANS_B, 11),
           fill=(255, 255, 255))


def panel_anthropic(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(28, 34, 30))
    # candlesticks: open 111.50, high 115.10, low 92.72, close 97.17
    bars = [(0.10, 111.5, 115.1, 108.0, 111.5, 0),
            (0.26, 108.0, 112.0, 102.0, 104.0, 1),
            (0.42, 104.0, 106.0, 97.0, 99.0, 1),
            (0.58, 99.0, 101.0, 94.0, 96.0, 1),
            (0.74, 96.0, 99.5, 95.0, 97.17, 0)]
    lo, hi = 90.0, 117.0

    def yy(v):
        return y + h - 6 - (v - lo) / (hi - lo) * (h - 30)
    for fx, o, hh, ll, c, up in bars:
        bx = x + w * fx
        col = (60, 200, 120) if up == 0 else (230, 70, 60)
        d.line([(bx + 5, yy(hh)), (bx + 5, yy(ll))], fill=col, width=2)
        d.rectangle([bx, yy(max(o, c)), bx + 10, yy(min(o, c))], fill=col)
    d.text((x + 8, y + 4), "$97.17", font=F(SANS_B, 17), fill=GOLD)
    d.text((x + 8, y + h - 18), "NASDAQ \u00b7 FIRST CLOSE",
           font=F(SANS_B, 9), fill=(255, 255, 255))
    d.rectangle([x + w - 52, y + 6, x + w - 6, y + 24], fill=(60, 200, 120))
    d.text((x + w - 48, y + 9), "+17%", font=F(SANS_B, 12), fill=(10, 30, 15))


def panel_japan(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(238, 232, 214))
    bx0, bw = x + 18, 34
    base = y + h - 14
    for i, (lab, v, col) in enumerate([("SEP", 2.1, (150, 150, 150)),
                                       ("OCT", 2.2, RED)]):
        bh = v / 2.5 * (h - 30)
        d.rectangle([bx0 + i * 48, base - bh, bx0 + i * 48 + bw, base],
                    fill=col)
        d.text((bx0 + i * 48 + 2, base - bh - 13), "%.1f%%" % v,
               font=F(SANS_B, 10), fill=INK)
        d.text((bx0 + i * 48 + 6, base + 2), lab, font=F(SANS_B, 8), fill=GREY)
    d.text((x + 118, y + 6), "2.2%", font=F(SERIF_B, 26), fill=RED)
    d.text((x + 118, y + 34), "CORE CPI", font=F(SANS_B, 9), fill=INK)


def panel_china(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(238, 232, 214))
    d.line([(x + 8, y + h - 20), (x + w - 8, y + h - 20)], fill=RED, width=3)
    d.text((x + 10, y + 5), "1-YR  3.00%", font=F(SANS_B, 12), fill=INK)
    d.text((x + 10, y + 22), "5-YR  3.50%", font=F(SANS_B, 12), fill=INK)
    d.text((x + 118, y + 5), "NO CHANGE", font=F(SANS_B, 10), fill=RED)
    d.text((x + 118, y + 22), "18 MO", font=F(SANS_B, 10), fill=INK)
    d.text((x + 10, y + h - 16), "UNCHANGED SINCE MAY 2025",
           font=F(SANS_B, 9), fill=GREY)


def panel_bepi(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(12, 20, 36))
    for sx, sy in [(0.08, 0.18), (0.2, 0.1), (0.5, 0.14), (0.85, 0.12),
                   (0.92, 0.3), (0.06, 0.42)]:
        d.ellipse([x + w * sx, y + h * sy, x + w * sx + 2, y + h * sy + 2],
                  fill=(200, 210, 230))
    mx, my, mr = x + w * 0.72, y + h * 0.52, 20
    d.ellipse([mx - mr, my - mr, mx + mr, my + mr], fill=(150, 145, 135),
              outline=(90, 85, 75), width=1)
    for cx, cy, cr in [(0.66, 0.44, 4), (0.78, 0.60, 3), (0.70, 0.62, 5)]:
        d.ellipse([x + w * cx - cr, y + h * cy - cr, x + w * cx + cr,
                   y + h * cy + cr], fill=(110, 105, 95))
    # dotted trajectory to Mercury
    for t in range(9):
        u = t / 8
        d.ellipse([x + 14 + u * (mx - x - 30) - 2, y + 16 + u * (my - y - 26) - 2,
                   x + 14 + u * (mx - x - 30) + 2, y + 16 + u * (my - y - 26) + 2],
                  fill=YELL)
    # spacecraft: small gold body + panels
    sx, sy = x + 22, y + 12
    d.rectangle([sx, sy, sx + 12, sy + 8], fill=GOLD)
    d.rectangle([sx - 8, sy + 2, sx, sy + 6], fill=(90, 130, 180))
    d.rectangle([sx + 12, sy + 2, sx + 20, sy + 6], fill=(90, 130, 180))
    d.text((x + 8, y + h - 18), "6BN MILES \u00b7 8 YEARS",
           font=F(SANS_B, 11), fill=(255, 255, 255))


def panel_phillips(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=GREEN)
    # cricket bat, diagonal, right side
    d.line([(x + w - 62, y + h - 8), (x + w - 30, y + 14)], fill=(222, 190, 130),
           width=12)
    d.line([(x + w - 30, y + 14), (x + w - 18, y + 6)], fill=(190, 150, 90),
           width=5)
    d.ellipse([x + w - 30, y + h - 26, x + w - 12, y + h - 8],
              fill=(200, 40, 40), outline=(255, 255, 255), width=1)
    d.text((x + 8, y + 4), "118", font=F(SERIF_B, 30), fill=(255, 255, 255))
    d.text((x + 8, y + h - 18), "118 \u00b7 RECORD", font=F(SANS_B, 10),
           fill=(255, 255, 255))


def panel_bukele(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(36, 72, 120))
    # ballot box
    d.rectangle([x + 62, y + 16, x + 126, y + h - 10], fill=(240, 235, 220),
                outline=INK, width=1)
    d.line([(x + 82, y + 16), (x + 106, y + 16)], fill=INK, width=3)
    d.rectangle([x + 74, y + 4, x + 114, y + 18], fill=(255, 255, 255),
                outline=INK, width=1)
    d.text((x + 82, y + 6), "2027", font=F(SANS_B, 10), fill=RED)
    d.text((x + 8, y + 4), "VOTE", font=F(SANS_B, 12), fill=(255, 255, 255))
    d.text((x + 8, y + h - 18), "FEB 2027", font=F(SANS_B, 11),
           fill=YELL)


def panel_burnham(d, x, y, w, h):
    # EU flag, left half
    d.rectangle([x, y, x + w // 2, y + h], fill=(0, 51, 153))
    cx, cy = x + w // 4, y + h // 2
    for i in range(12):
        a = i * math.pi / 6 - math.pi / 2
        sx, sy = cx + 16 * math.cos(a), cy + 16 * math.sin(a)
        d.ellipse([sx - 2, sy - 2, sx + 2, sy + 2], fill=YELL)
    # UK flag, right half (stylised: red cross + saltire on blue)
    ux = x + w // 2
    d.rectangle([ux, y, x + w, y + h], fill=(1, 33, 105))
    d.line([(ux, y), (x + w, y + h)], fill=(255, 255, 255), width=5)
    d.line([(ux, y + h), (x + w, y)], fill=(255, 255, 255), width=5)
    d.line([(ux + w // 4, y), (ux + w // 4, y + h)], fill=(255, 255, 255),
           width=7)
    d.line([(ux, y + h // 2), (x + w, y + h // 2)], fill=(255, 255, 255),
           width=7)
    d.line([(ux + w // 4, y), (ux + w // 4, y + h)], fill=(200, 16, 46),
           width=3)
    d.line([(ux, y + h // 2), (x + w, y + h // 2)], fill=(200, 16, 46),
           width=3)
    d.rectangle([x + 8, y + h - 20, x + 96, y + h - 4], fill=RED)
    d.text((x + 12, y + h - 18), "RESET TALKS", font=F(SANS_B, 10),
           fill=(255, 255, 255))


def panel_hormuz(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(16, 44, 66))
    # sea lines
    for i, yy in enumerate([0.66, 0.76, 0.86]):
        d.line([(x + 6, y + h * yy), (x + w - 6, y + h * yy)],
               fill=(70, 120, 160), width=2)
    # tanker silhouette, lower half, kept left of the $12.29 label
    d.polygon([(x + 10, y + 30), (x + 100, y + 30), (x + 112, y + 40),
               (x + 106, y + 46), (x + 14, y + 46)], fill=(20, 20, 20))
    d.rectangle([x + 66, y + 16, x + 80, y + 30], fill=(20, 20, 20))
    d.rectangle([x + 24, y + 22, x + 34, y + 30], fill=(200, 60, 50))
    d.rectangle([x + 40, y + 22, x + 50, y + 30], fill=(200, 60, 50))
    d.text((x + 8, y + 2), "200\u00d7", font=F(SERIF_B, 24),
           fill=(255, 255, 255))
    d.text((x + w - 78, y + 6), "$12.29", font=F(SANS_B, 13), fill=YELL)
    d.text((x + w - 78, y + 22), "/ BBL", font=F(SANS_B, 10),
           fill=(255, 255, 255))


def panel_gta(d, x, y, w, h):
    # sunset gradient bands
    bands = [(255, 170, 80), (250, 130, 90), (220, 90, 120), (150, 70, 140),
             (90, 50, 130)]
    bh = h / len(bands)
    for i, col in enumerate(bands):
        d.rectangle([x, y + i * bh, x + w, y + (i + 1) * bh + 1], fill=col)
    d.ellipse([x + w // 2 - 16, y + 8, x + w // 2 + 16, y + 40],
              fill=(255, 220, 120))
    # palm silhouettes
    for px in [0.12, 0.86]:
        d.line([(x + w * px, y + h), (x + w * px, y + h - 18)], fill=(30, 20, 40),
               width=3)
        for dx, dy in [(-8, -4), (8, -4), (-6, -8), (6, -8)]:
            d.line([(x + w * px, y + h - 18),
                    (x + w * px + dx, y + h - 18 + dy)], fill=(30, 20, 40),
                   width=2)
    d.text((x + 8, y + 4), "VI", font=F(SERIF_B, 26), fill=(255, 255, 255))
    d.rectangle([x + w - 46, y + h - 22, x + w - 6, y + h - 4], fill=GOLD)
    d.text((x + w - 42, y + h - 20), "99", font=F(SANS_B, 13), fill=(20, 20, 20))


CARD_PAINTERS = [panel_asia, panel_anthropic, panel_japan, panel_china,
                 panel_bepi, panel_phillips, panel_bukele, panel_burnham,
                 panel_hormuz, panel_gta]


def draw_cards(d):
    cw, gap = 188, 12
    rows = [(458, 0), (580, 5)]
    for ry, start in rows:
        for j in range(5):
            card = CARDS[start + j]
            x = 16 + j * (cw + gap)
            d.rectangle([x, ry, x + cw, ry + 116], outline=INK, width=1)
            CARD_PAINTERS[start + j](d, x + 1, ry + 1, cw - 2, 52)
            ty = ry + 56
            d.text((x + 2, ty), card["kicker"], font=F(SANS_B, 9), fill=RED)
            ty += 12
            ty = draw_wrapped(d, x + 2, ty, card["head"], F(SERIF_B, 13),
                              cw - 4, INK, 0)
            draw_wrapped(d, x + 2, ty + 1, card["deck"], F(SERIF, 10),
                         cw - 4, INK, 0)


# ---------------- map + ALSO + date check ----------------

CONTINENTS = [
    [(-168, 66), (-140, 70), (-125, 72), (-110, 73), (-95, 80), (-80, 73),
     (-70, 62), (-55, 47), (-60, 45), (-75, 35), (-80, 25), (-85, 20),
     (-90, 15), (-95, 18), (-105, 20), (-115, 28), (-125, 40), (-125, 50),
     (-140, 60), (-165, 60)],
    [(-55, 60), (-45, 60), (-30, 68), (-20, 70), (-25, 76), (-45, 80),
     (-58, 76), (-55, 68)],
    [(-80, 10), (-75, 5), (-60, 5), (-50, 0), (-35, -8), (-40, -20),
     (-48, -28), (-58, -38), (-65, -45), (-70, -55), (-73, -40), (-72, -20),
     (-80, -5), (-80, 5)],
    [(-17, 15), (-10, 30), (0, 35), (10, 37), (20, 32), (30, 31), (35, 28),
     (40, 15), (48, 11), (51, 10), (40, -5), (35, -18), (28, -32),
     (20, -35), (15, -27), (12, -18), (8, 4), (-8, 5), (-17, 12)],
    [(-10, 36), (-9, 43), (-2, 48), (0, 50), (5, 53), (8, 57), (10, 59),
     (18, 56), (21, 55), (24, 59), (28, 60), (30, 62), (30, 70), (25, 71),
     (18, 69), (12, 66), (5, 60), (-2, 57), (-5, 50), (-9, 43)],
    [(30, 70), (40, 68), (55, 70), (70, 72), (90, 75), (110, 76), (130, 72),
     (160, 70), (178, 66), (170, 60), (162, 58), (158, 52), (142, 50),
     (140, 40), (130, 35), (127, 33), (120, 25), (110, 20), (105, 10),
     (100, 8), (95, 15), (90, 22), (85, 20), (80, 15), (77, 8), (72, 20),
     (66, 25), (60, 25), (55, 26), (50, 28), (48, 30), (43, 35), (38, 36),
     (35, 36), (30, 36), (28, 40), (30, 45), (30, 55), (30, 65)],
    [(113, -22), (114, -30), (115, -35), (124, -33), (130, -32), (137, -35),
     (140, -38), (147, -39), (150, -37), (153, -27), (150, -22), (146, -19),
     (142, -15), (142, -11), (136, -12), (132, -11), (130, -13), (126, -14),
     (122, -17), (118, -20), (113, -22)],
    [(95, -5), (100, -2), (105, -6), (110, -7), (115, -4), (120, -2),
     (125, -4), (130, -3), (135, -4), (140, -6)],
]

PINS = [
    (1, 30.5, 50.4), (2, 84.9, 19.3), (3, 30.7, 36.9), (4, 127.0, 37.5),
    (5, -74.0, 40.7), (6, 139.7, 35.7), (7, 116.4, 39.9),
    (9, 174.8, -41.3), (10, -89.2, 13.7), (11, 4.35, 50.85),
    (12, 56.5, 27.0),
]


def draw_map(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=DNAVY)
    d.rectangle([x, y, x + w, y + h], outline=INK, width=1)

    def proj(lon, lat):
        px = x + (lon + 170) / 360.0 * w
        py = y + (75 - lat) / 135.0 * h
        return (px, py)

    for poly in CONTINENTS:
        d.polygon([proj(lon, lat) for lon, lat in poly], fill=CREAM)
    for num, lon, lat in PINS:
        px, py = proj(lon, lat)
        d.ellipse([px - 8, py - 8, px + 8, py + 8], fill=RED,
                  outline=(255, 255, 255), width=1)
        s = str(num)
        fnt = F(SANS_B, 10 if num < 10 else 8)
        d.text((px - text_w(d, s, fnt) / 2, py - 6), s, font=fnt,
               fill=(255, 255, 255))
    # off-map callouts for the two non-geographic stories
    d.rectangle([x + 8, y + h - 40, x + 158, y + h - 22], fill=(255, 255, 255))
    d.text((x + 14, y + h - 37), "8  SPACE \u2014 Mercury",
           font=F(SANS_B, 10), fill=DRED)
    d.rectangle([x + 164, y + h - 40, x + 278, y + h - 22], fill=(255, 255, 255))
    d.text((x + 170, y + h - 37), "13  WORLD \u2014 GTA VI",
           font=F(SANS_B, 10), fill=DRED)
    d.text((x + 8, y + h - 18), "Pins 1\u201313 mark the lead & card stories",
           font=F(SANS, 9), fill=(200, 210, 230))


def draw_also_item(d, x, y, city, text, width):
    f_city = F(SANS_B, 10)
    f_txt = F(SANS, 10)
    d.text((x, y), "\u2022", font=f_txt, fill=RED)
    cx = x + 10
    d.text((cx, y), city, font=f_city, fill=RED)
    tx = cx + text_w(d, city, f_city) + 4
    d.text((tx, y), "\u2014 " + text, font=f_txt, fill=INK)


def draw_map_also(d):
    d.text((16, 702), "WHERE IT HAPPENED", font=F(SANS_B, 12), fill=RED)
    d.text((352, 702), "ALSO ON FRIDAY 20 NOVEMBER \u2014 23 MORE STORIES",
           font=F(SANS_B, 12), fill=RED)
    draw_map(d, 16, 720, 320, 178)
    y = 724
    for city, text in ALSO_LEFT:
        draw_also_item(d, 352, y, city, text, 322)
        y += 15
    y = 724
    for city, text in ALSO_RIGHT:
        draw_also_item(d, 684, y, city, text, 324)
        y += 15


def draw_datecheck(d):
    y0, y1 = 908, 972
    d.rectangle([16, y0, 1008, y1], outline=RED, width=2)
    # checkmark drawn with line segments (never the U+2713 glyph)
    d.line([(30, y0 + 20), (38, y0 + 30), (52, y0 + 10)], fill=(34, 139, 34),
           width=4, joint="curve")
    d.text((60, y0 + 6), "DATE CHECK", font=F(SANS_B, 13), fill=RED)
    d.text((60, y0 + 22),
           "Every story here happened, or was first reported, on Friday "
           "20 November 2026.",
           font=F(SANS, 11), fill=INK)
    draw_wrapped(d, 60, y0 + 37, "LEFT OUT AS OTHER DAYS' NEWS: " + LEFT_OUT,
                 F(SANS, 9), 1008 - 60 - 10, GREY, 1)


def draw_footer(d):
    d.text((16, 980),
           "Sources: Reuters, AP, AFP, BBC, UN News, ICC, EU Council, PBoC, ESA, "
           "Al Jazeera, EORTC, Formula1.com, Finnhub. Original drawings, made in code.",
           font=F(SANS, 9), fill=GREY)
    r = "Compiled 20 Nov 2026."
    d.text((1008 - text_w(d, r, F(SANS, 9)), 980), r, font=F(SANS, 9),
           fill=GREY)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    draw_masthead(d)
    draw_stats(d)
    draw_regions(d)
    draw_leads(d)
    draw_cards(d)
    draw_map_also(d)
    draw_datecheck(d)
    draw_footer(d)
    img.save(OUT, "PNG", optimize=True)


if __name__ == "__main__":
    main()
