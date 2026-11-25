#!/usr/bin/env python3
"""Draw the 24 November 2026 world-news image (1024 x 1024 PNG).

A newspaper front page: a masthead naming the day, one lead story, and
six more stories from six regions. Every story below was reported on
24 November 2026 (Daily Summary Of, Reuters, SCMP, AP).
Run: python3 draw.py  ->  entry.png (1024 x 1024, under 1 MiB)
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (250, 247, 238)
NAVY = (15, 42, 68)
RED = (178, 34, 34)
INK = (20, 20, 20)
GREY = (90, 90, 90)
RULE = (180, 175, 165)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, max_w, leading, color=INK):
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=color)
        y += leading
    return y


STORIES = [
    ("COURTS", "Huawei found guilty",
     "A US jury finds Huawei guilty of trade-secret theft and "
     "bank fraud, acquitting it of racketeering."),
    ("TURKIYE", "Helicopter crash kills five",
     "A Turkish Air Force helicopter crashes after takeoff in "
     "western Turkiye, killing five crew members."),
    ("COLOMBIA", "Hostages in Cartagena",
     "Armed men hold 25 hostages in a supermarket in Cartagena, "
     "one of Colombia\u2019s top tourist cities."),
    ("YEMEN", "Houthis close on Aden",
     "Houthi fighters are 60 km from Aden and ready to attack. "
     "Riyadh\u2019s tallest tower is hit, 11 wounded."),
    ("UKRAINE", "Strikes spread at sea",
     "Ukraine hits Russian ships in the Gulf of Finland and off "
     "Libya. Kyiv calls the strikes self-defence."),
    ("SPACE & SPORT", "Shenzhou-24 launches",
     "China launches Shenzhou-24 with Pakistan\u2019s first "
     "astronaut. Senegal regain the Africa Cup title."),
]


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Masthead
    d.rectangle([0, 0, W, 168], fill=NAVY)
    d.text((36, 22), "WORLD NEWS", font=font(BOLD, 78), fill=(255, 255, 255))
    d.text((36, 118), "TUESDAY  24  NOVEMBER  2026",
           font=font(BOLD, 30), fill=(255, 210, 90))
    d.text((36, 182), "One day in the world  \u2014  seven stories, six regions",
           font=font(REG, 26), fill=GREY)

    # Lead story
    y = 224
    d.rectangle([36, y, 988, y + 4], fill=RED)
    y += 16
    d.text((36, y), "LEAD  \u00b7  STRAIT OF HORMUZ", font=font(BOLD, 24), fill=RED)
    y += 34
    y = para(d, 36, y, "Four tankers hit mines",
             font(SERIF_B, 42), 952, 50)
    y += 4
    y = para(d, 36, y,
             "Iran\u2019s Revolutionary Guards said four oil tankers hit "
             "naval mines in the Strait of Hormuz and caught fire. "
             "A container ship was also targeted in the strait.",
             font(SERIF, 25), 952, 34)
    y += 12
    d.line([36, y, 988, y], fill=RULE, width=2)

    # Six stories, two columns
    y += 18
    col_w, col_h = 462, 158
    for i, (tag, head, body) in enumerate(STORIES):
        x = 36 + (i % 2) * 490
        yy = y + (i // 2) * (col_h + 14)
        d.text((x, yy), tag, font=font(BOLD, 21), fill=RED)
        yy += 30
        yy = para(d, x, yy, head, font(SERIF_B, 27), col_w, 34)
        yy += 2
        para(d, x, yy, body, font(REG, 21), col_w, 28)

    # Footer
    fy = 996
    d.line([36, fy - 12, 988, fy - 12], fill=RULE, width=2)
    d.text((36, fy), "24 November 2026  \u00b7  Sources: Daily Summary Of, Reuters, SCMP, AP",
           font=font(REG, 19), fill=GREY)

    img.save("entry.png", format="PNG", optimize=True)
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
