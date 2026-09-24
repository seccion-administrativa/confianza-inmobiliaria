#!/usr/bin/env python3
"""Valida tutoriales.json y genera thumbnails (opcional)."""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent.parent

# Validar JSON
with open(HERE / "data" / "tutoriales.json") as f:
    data = json.load(f)

print(f"✓ JSON válido ({len(data['tutoriales'])} tutoriales)")

# Validaciones
for t in data["tutoriales"]:
    assert t.get("id"), f"Falta 'id' en {t.get('titulo', '?')}"
    assert t.get("slug"), f"Falta 'slug' en {t['id']}"
    assert t.get("titulo"), f"Falta 'titulo' en {t['id']}"
    assert t.get("estado") in ["publicado", "borrador", "oculto"], f"Estado inválido: {t['id']}"

    if t.get("video"):
        v = t["video"]
        assert v.get("proveedor") in ["drive", "youtube", "mp4"], f"Proveedor inválido: {t['id']}"
        assert v.get("id"), f"Falta video.id: {t['id']}"
        # Validar ID según proveedor
        if v["proveedor"] == "drive":
            assert re.match(r'^[A-Za-z0-9_-]{10,}$', v["id"]), f"Drive ID inválido: {t['id']}"
        elif v["proveedor"] == "youtube":
            assert re.match(r'^[A-Za-z0-9_-]{11}$', v["id"]), f"YouTube ID debe ser 11 caracteres: {t['id']}"

print(f"✓ Validación completada ({len([t for t in data['tutoriales'] if t['estado'] == 'publicado'])} publicados)")

# Generar thumbnails (opcional)
if "--gen-thumbs" in sys.argv and (HERE / "tools" / "gen_icons.py").exists():
    print("\nGenerando thumbnails con ffmpeg...")
    for t in data["tutoriales"]:
        if t.get("video") and t["video"].get("proveedor") == "mp4":
            # Aquí iría ffmpeg -ss 3 -i <file> -frames:v 1 thumbs/<id>.webp
            pass
    print("(ffmpeg no configurado en esta fase)")

print("\n✅ Listo para commit y push")
