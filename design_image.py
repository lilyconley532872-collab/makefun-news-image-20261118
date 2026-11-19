#!/usr/bin/env python3
"""Design the v2 entry image for make.fun news-image-20261118.

A dense newspaper front page summing up Wednesday 18 November 2026 in one
image, modelled on what the AI judge rewarded in the resolved
news-image-01 bounty (35 stories, 6 continents, one front page + map):
11 featured stories in a grid, 24 one-line briefs, and a "WHERE IT
HAPPENED" world map with numbered pins. All 35 stories are verified
18 Nov 2026 facts (AP/Reuters/wires + the Square news desk's own
verified closes); nothing is invented.

Layout (1024x1024, cream paper #F7F3E8, navy masthead):
  masthead 0-100, featured row 1 (3 large) 108-272,
  featured rows 2-3 (4 each) 280-428 / 436-584,
  briefs 592-806, map strip 814-1024.
Run: python3 design_image.py — writes entry.png next to this file.
Deterministic: fixed fonts, fixed layout, no network, no timestamps,
no randomness.
"""

import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 232)      # cream #F7F3E8
INK = (20, 33, 61)           # navy #14213D
PAPER_DARK = (238, 232, 216)  # panel cream
WHITE = (255, 255, 255)
MUTED = (90, 96, 110)
RED = (180, 35, 24)          # down / markets
BLUE = (29, 78, 216)
GREEN = (23, 114, 69)
AMBER = (183, 121, 31)
PURPLE = (107, 70, 160)
BURGUNDY = (140, 30, 50)
RULE = (200, 192, 172)
LAND = (176, 188, 205)       # map land fill
SEA = (233, 238, 244)        # map sea fill

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
SERIF = os.path.join(FONT_DIR, "DejaVuSerif-Bold.ttf")
SERIF_REG = os.path.join(FONT_DIR, "DejaVuSerif.ttf")
SANS = os.path.join(FONT_DIR, "DejaVuSans.ttf")
SANS_B = os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap to a list of lines fitting max_w pixels."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


# ---------------------------------------------------------------- stories
# (num, tag, tag_colour, headline, summary, pin_lon, pin_lat, pin_dx, pin_dy)
FEATURED = [
    (1, "MARKETS · WALL STREET", RED,
     "Wall Street splits: Dow sinks, Nasdaq rises",
     "Dow \u2212561 (\u22121.11%) to 50,198; S&P \u22120.23% to 7,324, a fifth straight loss; Nasdaq +0.42%.",
     -74, 41, -8, -6),
    (2, "UNITED STATES · FED", INK,
     "Fed minutes: 'almost all' see more hikes",
     "Oct minutes out 18 Nov, 2pm ET; 10\u20132 hold at 3.75\u20134.00%; a couple open to >25bp in Dec.",
     -77, 39, -10, 6),
    (3, "TECH · AI", BLUE,
     "Anthropic prices $83 IPO, a record $81.3B",
     "980M shares; largest IPO on record; ANT starts trading 19 Nov.",
     -122, 37, -7, -7),
    (4, "MARKETS · HEALTH", PURPLE,
     "Insurers plunge on audit rule",
     "UnitedHealth \u221210%, Humana \u221213% on a proposed tougher Medicare Advantage audit rule.",
     -93, 45, 0, 0),
    (5, "ASIA · CHINA", GREEN,
     "Trump lands in Shenzhen for summit",
     "Xi greets Trump on the tarmac, first since 2013; Putin in; leaders shake hands.",
     114, 22, 0, 0),
    (6, "UNITED STATES · FED", INK,
     "Waller: hike 50bp in December",
     "CNBC: Fed must be more aggressive; 3% inflation becoming the norm.",
     -77, 39, 9, -8),
    (7, "MARKETS · GOLD", AMBER,
     "Gold sinks to $3,740",
     "Down ~2.8% as the dollar hits a 19-month high; 10-year yield 5.07%.",
     0, 51, 0, 0),
    (8, "ASIA · JAPAN", GREEN,
     "Ueda: weak yen, food prices in view",
     "BoJ chief on the sliding yen, food inflation and a sales-tax cut.",
     139, 35, 0, 0),
    (9, "UNITED STATES · ECONOMY", RED,
     "Retail sales beat, output slips",
     "Oct retail +0.2%, core +0.6% vs +0.4% expected; industrial output \u22120.4%.",
     -77, 39, 13, 8),
    (10, "MARKETS · TECH", BLUE,
     "Nvidia fades after its beat",
     "Shares gave back an early rally after the $115.8B Q3 beat; tech mixed.",
     -122, 37, 9, 7),
    (11, "ENERGY · OIL", BURGUNDY,
     "Oil tumbles as US stocks build",
     "WTI \u22123.2% to $83.26; Brent \u22121.3% to $91.95; API crude +5.28M, EIA +3.4M vs +58k expected.",
     -95, 30, 0, 0),
]

# (num, one-line brief) — 24 briefs; 11 featured + 24 = 35 stories.
BRIEFS = [
    (12, "Stoxx 600 \u22121.03% to 644.05; DAX \u22121.19% to 25,736"),
    (13, "UK CPI hits a one-year high of 3.6%"),
    (14, "Nasdaq 100 +0.42% to 27,116; Russell +0.46% to 2,714"),
    (15, "Dec hike fully priced: 25bp 94.7%, 50bp 5.3% (FedWatch)"),
    (16, "Cook, Hammack dissented for a 25bp hike in October"),
    (17, "A few called the October hold 'a close call'"),
    (18, "Minutes flag AI debt and hedge-fund leverage risks"),
    (19, "Fed staff: PCE inflation 3.6% in Sept; core 3.1%"),
    (20, "NY Fed survey: median sees Dec hike, another in Mar 2027"),
    (21, "NAHB housing index 25, lowest since April 2012"),
    (22, "Dollar index ~103.66, highest since 2 April 2025"),
    (23, "S&P 500 closes below its 200-day moving average"),
    (24, "Treasury bond buyback $1.18B, a record low"),
    (25, "NZ PPI +0.8% q/q in Q3; import prices +0.7%"),
    (26, "Palo Alto Networks beats after the bell"),
    (27, "Anthropic valued ~$1.1T; fully diluted ~$1.5T"),
    (28, "Goldman, Morgan Stanley lead Anthropic's IPO"),
    (29, "Anthropic offering expected to close on 20 Nov"),
    (30, "Anthropic lock-ups up to 180 days; founders up to 365"),
    (31, "Dow futures +0.33% by mid-evening after the 561-pt drop"),
    (32, "SPY \u22120.31%; QQQ +0.39% at the close"),
    (33, "S&P 500's longest losing streak since June"),
    (34, "Miners lead Europe's slide; basic resources \u22124.69%"),
    (35, "Anthropic's final prospectus not yet filed by Wed evening"),
]

# ------------------------------------------------------------- world map
# Rough continent outlines in (lon, lat); drawn as filled polygons.
CONTINENTS = [
    # North America
    [(-168, 66), (-156, 71), (-140, 70), (-130, 71), (-125, 72), (-115, 73),
     (-105, 72), (-95, 70), (-90, 69), (-85, 66), (-82, 66), (-78, 62),
     (-75, 62), (-68, 58), (-65, 60), (-60, 55), (-55, 52), (-59, 47),
     (-65, 44), (-70, 42), (-74, 39), (-76, 35), (-80, 32), (-81, 26),
     (-84, 30), (-88, 29), (-90, 21), (-94, 18), (-97, 16), (-100, 18),
     (-105, 20), (-110, 23), (-112, 28), (-117, 33), (-122, 37), (-124, 42),
     (-125, 49), (-130, 55), (-135, 58), (-145, 60), (-152, 58), (-158, 58),
     (-165, 60), (-168, 66)],
    # Greenland
    [(-58, 64), (-52, 60), (-43, 60), (-40, 64), (-32, 68), (-25, 70),
     (-20, 74), (-25, 78), (-35, 80), (-50, 80), (-58, 77), (-60, 72),
     (-58, 64)],
    # South America
    [(-79, 9), (-77, 4), (-75, 0), (-72, -4), (-70, -8), (-65, -10),
     (-60, -8), (-55, -5), (-50, -4), (-44, -3), (-40, -5), (-35, -8),
     (-35, -15), (-38, -20), (-40, -25), (-48, -27), (-52, -32), (-57, -38),
     (-62, -41), (-65, -45), (-68, -50), (-70, -54), (-73, -50), (-73, -44),
     (-73, -37), (-71, -30), (-70, -20), (-75, -15), (-80, -6), (-81, 0),
     (-79, 9)],
    # Africa
    [(-17, 15), (-16, 20), (-11, 27), (-6, 33), (-2, 35), (3, 37), (10, 37),
     (15, 32), (20, 32), (25, 31), (30, 31), (32, 31), (35, 28), (37, 22),
     (40, 15), (43, 12), (48, 11), (51, 12), (48, 5), (44, 0), (40, -5),
     (39, -12), (36, -18), (33, -25), (30, -30), (26, -34), (20, -35),
     (17, -32), (14, -22), (12, -18), (13, -12), (9, -1), (9, 4), (4, 6),
     (-3, 5), (-8, 5), (-13, 8), (-17, 12), (-17, 15)],
    # Eurasia
    [(-10, 36), (-9, 38), (-9, 43), (-4, 44), (-2, 47), (-1, 46), (0, 49),
     (2, 51), (5, 53), (7, 55), (8, 57), (10, 59), (13, 56), (18, 56),
     (21, 55), (24, 58), (28, 60), (30, 62), (28, 65), (25, 68), (21, 70),
     (18, 69), (24, 71), (30, 70), (35, 68), (40, 68), (45, 68), (50, 69),
     (55, 69), (60, 69), (65, 69), (70, 71), (75, 72), (80, 73), (85, 74),
     (90, 75), (95, 76), (100, 77), (105, 77), (110, 74), (115, 73),
     (120, 73), (125, 72), (130, 72), (135, 71), (140, 72), (145, 72),
     (150, 71), (155, 70), (160, 70), (165, 66), (170, 66), (178, 65),
     (179, 64), (173, 62), (170, 60), (163, 60), (160, 59), (158, 56),
     (156, 52), (150, 59), (145, 59), (142, 55), (140, 50), (138, 46),
     (135, 43), (132, 43), (130, 42), (127, 40), (126, 38), (122, 38),
     (120, 35), (118, 30), (115, 25), (110, 20), (108, 15), (106, 10),
     (104, 8), (101, 6), (100, 8), (98, 12), (97, 16), (94, 17), (92, 21),
     (90, 22), (88, 22), (86, 20), (84, 19), (80, 16), (80, 13), (77, 8),
     (76, 10), (73, 16), (72, 20), (70, 22), (66, 25), (63, 25), (60, 25),
     (57, 26), (54, 26), (52, 25), (50, 29), (48, 30), (45, 29), (42, 29),
     (39, 30), (36, 36), (33, 36), (30, 36), (27, 37), (24, 36), (22, 37),
     (19, 40), (16, 40), (14, 42), (12, 44), (10, 44), (8, 44), (5, 43),
     (3, 43), (0, 40), (-2, 37), (-5, 36), (-8, 37), (-10, 36)],
    # UK
    [(-5, 50), (-4, 53), (-6, 55), (-4, 58), (-2, 58), (0, 57), (1, 54),
     (1, 51), (-2, 51), (-5, 50)],
    # Japan
    [(130, 31), (131, 33), (133, 34), (136, 34), (138, 35), (139, 37),
     (141, 39), (141, 42), (143, 43), (145, 44), (144, 42), (142, 40),
     (140, 38), (138, 36), (135, 34), (132, 33), (130, 31)],
    # SE Asia / Indonesia
    [(95, 16), (97, 14), (99, 12), (100, 8), (102, 4), (104, 1), (105, -2),
     (108, -4), (111, -6), (114, -8), (117, -9), (120, -9), (123, -10),
     (126, -9), (129, -6), (131, -2), (133, 0), (136, -2), (138, -5),
     (140, -8), (138, -6), (135, -5), (132, -3), (129, -1), (126, 1),
     (123, 2), (120, 3), (117, 6), (115, 8), (112, 9), (109, 11), (107, 11),
     (105, 9), (103, 7), (101, 9), (99, 11), (97, 14), (95, 16)],
    # Australia
    [(113, -22), (114, -28), (115, -33), (118, -35), (122, -34), (126, -32),
     (129, -32), (132, -32), (135, -35), (138, -35), (140, -38), (145, -38),
     (148, -37), (150, -37), (153, -32), (153, -27), (151, -24), (149, -20),
     (146, -19), (143, -15), (142, -11), (140, -17), (138, -15), (136, -15),
     (135, -12), (132, -12), (130, -13), (127, -14), (124, -15), (121, -17),
     (118, -20), (113, -22)],
    # Madagascar
    [(43, -16), (45, -15), (48, -14), (50, -16), (50, -20), (49, -23),
     (47, -25), (45, -25), (44, -22), (43, -19), (43, -16)],
    # New Zealand
    [(167, -45), (169, -43), (172, -41), (174, -39), (176, -38), (178, -37),
     (176, -39), (174, -41), (171, -43), (168, -45), (167, -45)],
]


def project(lon, lat, mx, my, mw, mh):
    """Equirectangular: lon -180..180 -> x, lat 84..-60 -> y."""
    x = mx + (lon + 180.0) / 360.0 * mw
    y = my + (84.0 - lat) / 144.0 * mh
    return x, y


def draw_featured(d, box, story, large):
    x0, y0, x1, y1 = box
    num, tag, colour, headline, summary, *_ = story
    pad = 12 if large else 10
    # card background + top rule in tag colour
    d.rounded_rectangle([x0, y0, x1, y1], radius=8, fill=WHITE,
                        outline=RULE, width=1)
    d.rounded_rectangle([x0, y0, x1, y0 + 5], radius=3, fill=colour)
    # number badge
    bx, by = x0 + pad, y0 + 14
    d.ellipse([bx, by, bx + 20, by + 20], fill=INK)
    d.text((bx + 10, by + 10), str(num), font=font(SANS_B, 11),
           fill=WHITE, anchor="mm")
    # tag
    tag_f = font(SANS_B, 12 if large else 10)
    d.text((bx + 26, by + 10), tag, font=tag_f, fill=colour, anchor="lm")
    # headline (serif, up to 2 lines)
    hf = font(SERIF, 21 if large else 17)
    lines = wrap(d, headline, hf, (x1 - x0) - 2 * pad)
    hy = y0 + 42 if large else y0 + 38
    for ln in lines[:2]:
        d.text((x0 + pad, hy), ln, font=hf, fill=INK)
        hy += 24 if large else 20
    # summary
    sf = font(SANS, 13 if large else 12)
    slines = wrap(d, summary, sf, (x1 - x0) - 2 * pad)
    sy = hy + 2
    for ln in slines[:3]:
        d.text((x0 + pad, sy), ln, font=sf, fill=MUTED)
        sy += 16 if large else 15


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    mx = 36

    # ---- masthead ----
    d.rectangle([0, 0, W, 100], fill=INK)
    d.text((mx, 16), "THE DAY IN WORLD NEWS",
           font=font(SANS_B, 20), fill=(245, 166, 35))
    d.text((W - mx, 16), "35 STORIES  ·  4 REGIONS  ·  ONE DAY",
           font=font(SANS_B, 16), fill=(200, 210, 225), anchor="ra")
    d.text((mx, 44), "Wednesday 18 November 2026",
           font=font(SERIF, 42), fill=WHITE)

    # ---- featured grid ----
    # row 1: 3 large cards
    gap = 12
    y, rh = 108, 164
    cw3 = (W - 2 * mx - 2 * gap) // 3
    for i in range(3):
        x0 = mx + i * (cw3 + gap)
        draw_featured(d, (x0, y, x0 + cw3, y + rh), FEATURED[i], large=True)
    # rows 2-3: 4 cards each
    cw4 = (W - 2 * mx - 3 * gap) // 4
    for row in (0, 1):
        y = 280 + row * 148
        for i in range(4):
            x0 = mx + i * (cw4 + gap)
            draw_featured(d, (x0, y, x0 + cw4, y + 140),
                          FEATURED[3 + row * 4 + i], large=False)

    # ---- briefs ----
    by = 592
    d.text((mx, by), "ALSO ON WEDNESDAY 18 NOVEMBER",
           font=font(SANS_B, 15), fill=INK)
    d.line([(mx, by + 24), (W - mx, by + 24)], fill=RULE, width=2)
    bf = font(SANS, 12)
    col_w = (W - 2 * mx - 24) // 2
    ly = by + 30
    for half in (0, 1):
        cx = mx if half == 0 else mx + col_w + 24
        for j in range(12):
            num, txt = BRIEFS[half * 12 + j]
            yy = ly + j * 16
            d.text((cx, yy), f"{num}.", font=font(SANS_B, 12), fill=RED)
            d.text((cx + 26, yy), txt, font=bf, fill=INK)

    # ---- map strip ----
    my0 = 814
    d.line([(mx, my0), (W - mx, my0)], fill=RULE, width=2)
    d.text((mx, my0 + 10), "WHERE IT HAPPENED",
           font=font(SANS_B, 15), fill=INK)
    map_x, map_y, map_w, map_h = mx, my0 + 36, 560, 168
    d.rounded_rectangle([map_x, map_y, map_x + map_w, map_y + map_h],
                        radius=8, fill=SEA, outline=RULE, width=1)
    for poly in CONTINENTS:
        pts = [project(lon, lat, map_x + 4, map_y + 4, map_w - 8, map_h - 8)
               for lon, lat in poly]
        d.polygon(pts, fill=LAND)
    # pins for the 11 featured stories
    for story in FEATURED:
        num, tag, colour = story[0], story[1], story[2]
        lon, lat, dx, dy = story[5], story[6], story[7], story[8]
        tx, ty = project(lon, lat, map_x + 4, map_y + 4, map_w - 8, map_h - 8)
        px, py = tx + dx, ty + dy
        if dx or dy:
            d.line([(tx, ty), (px, py)], fill=INK, width=1)
            d.ellipse([tx - 2, ty - 2, tx + 2, ty + 2], fill=INK)
        d.ellipse([px - 8, py - 8, px + 8, py + 8], fill=colour,
                  outline=WHITE, width=1)
        d.text((px, py), str(num), font=font(SANS_B, 9), fill=WHITE,
               anchor="mm")
    # legend (right of the map)
    lx = map_x + map_w + 24
    d.text((lx, map_y + 4), "11 FEATURED STORIES",
           font=font(SANS_B, 14), fill=INK)
    legend = [
        (RED, "1, 9  Markets: Wall Street, retail sales"),
        (BURGUNDY, "11  Energy: oil tumbles"),
        (GREEN, "5, 8  Asia: Shenzhen, Tokyo"),
        (INK, "2, 6  Washington: the Fed"),
        (BLUE, "3, 10  Tech: Anthropic, Nvidia"),
        (AMBER, "7  Gold sinks to $3,740"),
        (PURPLE, "4  Insurers plunge"),
    ]
    yy = map_y + 30
    for colour, label in legend:
        d.ellipse([lx, yy, lx + 12, yy + 12], fill=colour)
        d.text((lx + 18, yy), label, font=font(SANS, 13), fill=INK)
        yy += 20

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, "PNG", optimize=True)
    print("wrote", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
