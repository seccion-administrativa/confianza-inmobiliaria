#!/usr/bin/env python3
"""Genera og-image.png (1200x630) para la preview de WhatsApp/redes."""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.dirname(__file__))
W, H = 1200, 630

# Fondo grafito (gradiente vertical sutil bg2 -> page)
base = Image.new("RGB", (W, H), (11, 13, 16))
top = (24, 28, 33)      # #181c21
bot = (11, 13, 16)      # #0b0d10
for y in range(H):
    t = y / H
    r = int(top[0]*(1-t) + bot[0]*t)
    g = int(top[1]*(1-t) + bot[1]*t)
    b = int(top[2]*(1-t) + bot[2]*t)
    for x in range(0, W, W):
        pass
    ImageDraw.Draw(base).line([(0, y), (W, y)], fill=(r, g, b))

# Glow dorado detrás del logo
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
gd.ellipse([W//2 - 340, -220, W//2 + 340, 340], fill=(245, 158, 11, 70))
glow = glow.filter(ImageFilter.GaussianBlur(130))
base.paste(glow, (0, 0), glow)

# Logo dorado centrado (parte superior)
logo = Image.open(os.path.join(HERE, "logo.png")).convert("RGBA")
lw = 640
lh = int(logo.height * lw / logo.width)
logo = logo.resize((lw, lh), Image.LANCZOS)
base.paste(logo, ((W - lw)//2, 128), logo)

draw = ImageDraw.Draw(base)
font_title = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 66)
font_sub = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 32)

def centered(text, y, font, fill):
    b = draw.textbbox((0, 0), text, font=font)
    w = b[2] - b[0]
    draw.text(((W - w)//2, y), text, font=font, fill=fill)

# Línea de acento dorada
draw.rounded_rectangle([W//2 - 44, 372, W//2 + 44, 378], radius=3, fill=(245, 158, 11))

centered("Centro de Tutoriales", 400, font_title, (255, 255, 255))
centered("Capacitación para ejecutivos · Confianza Inmobiliaria", 492, font_sub, (154, 163, 173))

base.save(os.path.join(HERE, "og-image.png"), quality=92)
# También una versión cuadrada 600x600 para apple-touch/preview alterno (opcional)
print("OK og-image.png", base.size)
