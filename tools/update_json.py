#!/usr/bin/env python3
"""Actualiza tutoriales.json: videos a proveedor local con duración y miniatura."""
import json, os

HERE = os.path.dirname(os.path.dirname(__file__))
meta = {}
mpath = os.path.join(HERE, "tools", "_meta.txt")
if os.path.exists(mpath):
    for line in open(mpath, encoding="utf-8"):
        line = line.strip()
        if not line or "|" not in line:
            continue
        parts = line.split("|")
        vid = parts[0]
        dur = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else None
        meta[vid] = dur

jpath = os.path.join(HERE, "data", "tutoriales.json")
data = json.load(open(jpath, encoding="utf-8"))

for t in data["tutoriales"]:
    if t.get("tipo") == "documento":
        continue
    vid = t["id"]
    localmp4 = os.path.join(HERE, "videos", vid + ".mp4")
    if os.path.exists(localmp4):
        t["video"] = {"proveedor": "local", "src": "videos/" + vid + ".mp4"}
        t["thumbnail"] = "thumbs/" + vid + ".webp"
        if meta.get(vid):
            t["duracion_seg"] = meta[vid]
    # si no existe el mp4 local, se deja como estaba (drive)

data["version"] = 3
json.dump(data, open(jpath, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("JSON actualizado. Videos locales:",
      sum(1 for t in data["tutoriales"] if t.get("video", {}).get("proveedor") == "local"))
for t in data["tutoriales"]:
    v = t.get("video", {})
    print(f"  {t['id']}: {v.get('proveedor')} dur={t.get('duracion_seg')}")
