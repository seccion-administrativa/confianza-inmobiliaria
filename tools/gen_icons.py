"""Genera íconos PWA desde logo.png (símbolo sobre navy)."""
import os
from PIL import Image

HERE = os.path.dirname(os.path.dirname(__file__))
NAVY = (13, 27, 62, 255)  # #0d1b3e

logo = Image.open(os.path.join(HERE, "logo.png")).convert("RGBA")
# El símbolo está a la izquierda; recortar y quitar transparencia sobrante
sym = logo.crop((0, 0, 300, logo.height))
bbox = sym.getbbox()
if bbox:
    sym = sym.crop(bbox)


def make(size, pad_ratio, out):
    canvas = Image.new("RGBA", (size, size), NAVY)
    maxw = int(size * (1 - 2 * pad_ratio))
    w, h = sym.size
    scale = min(maxw / w, maxw / h)
    nw, nh = max(1, int(w * scale)), max(1, int(h * scale))
    s = sym.resize((nw, nh), Image.LANCZOS)
    canvas.paste(s, ((size - nw) // 2, (size - nh) // 2), s)
    canvas.save(os.path.join(HERE, out))


make(192, 0.14, "icon-192.png")
make(512, 0.14, "icon-512.png")
make(512, 0.24, "icon-512-maskable.png")
print("✓ Íconos generados")
