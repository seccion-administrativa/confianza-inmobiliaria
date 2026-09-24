#!/bin/bash
# Recomprime los videos descargados, genera miniaturas y calcula duración.
SRC="/c/Users/eduardo.perez/Downloads"
DST="/c/Users/eduardo.perez/Documents/confianza/tutoriales-web"
mkdir -p "$DST/videos" "$DST/thumbs"
META="$DST/tools/_meta.txt"
: > "$META"

# eliminar duplicado de postular si existe
rm -f "$SRC/como postular a un depto  (1).mp4"

for in in "$SRC"/*.mp4; do
  base=$(basename "$in")
  case "$base" in
    *"creo el lead"*) id="tut-lead";;
    *"promocionar"*) id="tut-promocionar";;
    *"cotizaci"*|*"g"*"nero la cotiz"*) id="tut-cotizacion";;
    *"agendo"*) id="tut-visita";;
    *"candado"*) id="tut-candado";;
    *"postular"*) id="tut-postular";;
    *"evaluar a un cliente"*) id="tut-evaluar";;
    *"aval y link"*) id="tut-aval";;
    *"aprobaci"*) id="tut-aprobacion";;
    *"boletas"*) id="tut-boletas";;
    *) continue;;
  esac
  # ya procesado?
  if [ -f "$DST/videos/$id.mp4" ]; then echo "skip $id"; continue; fi
  echo ">>> procesando $id desde: $base"
  ffmpeg -y -i "$in" \
    -vf "scale='min(1280,iw)':-2:force_original_aspect_ratio=decrease" \
    -c:v libx264 -crf 28 -preset veryfast -c:a aac -b:a 112k -movflags +faststart \
    "$DST/videos/$id.mp4" 2>/dev/null
  ffmpeg -y -ss 2 -i "$in" -frames:v 1 -vf "scale=640:-2" -q:v 80 "$DST/thumbs/$id.webp" 2>/dev/null
  dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$in" 2>/dev/null | cut -d. -f1)
  sz=$(stat -c%s "$DST/videos/$id.mp4" 2>/dev/null)
  echo "$id|$dur|$sz" >> "$META"
  echo "    -> $id.mp4 ($((sz/1024/1024)) MB, ${dur}s)"
done
echo "=== LISTO ==="
cat "$META"
