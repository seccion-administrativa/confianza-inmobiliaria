# Confianza · Centro de Tutoriales

Plataforma de tutoriales en video para capacitar ejecutivos y vendedores de arriendo de Confianza Inmobiliaria.

## 🚀 Quick Start

1. **Agregar un tutorial:** edita `data/tutoriales.json` con esta estructura:

```json
{
  "id": "tut-NNN",
  "slug": "titulo-en-slug",
  "titulo": "Título del Tutorial",
  "descripcion": "Breve resumen",
  "categoria": "id-categoria",
  "etiquetas": ["tag1", "tag2"],
  "palabras_clave": ["palabra", "clave"],
  "video": {
    "proveedor": "drive",
    "id": "1dALtjISFgqa2..."
  },
  "duracion_seg": 120,
  "fecha": "2026-09-24",
  "estado": "publicado"
}
```

2. **Subir video:**
   - Google Drive: compartir con "Cualquiera con el enlace" (Lector)
   - YouTube: crear no listado y copiar ID de embed

3. **Cambiar proveedor:** edita `video.proveedor` — no requiere cambios en el código.

4. **Generar thumbnail:** (opcional)
   ```bash
   ffmpeg -ss 3 -i video.mp4 -frames:v 1 -vf scale=640:-2 thumbs/tut-NNN.webp
   ```

5. **Commit y push:**
   ```bash
   git add data/tutoriales.json thumbs/
   git commit -m "Agregar tutorial: Título"
   git push
   ```

## 🎨 Configuración

- **Tema:** oscuro/claro (preferencia en `localStorage`)
- **Acento:** dorado/verde/azul (selector en ⚙️)
- **Buscador:** normalización, stemming ligero, sinónimos desde `data/sinonimos.json`

## 📱 Mobile-first

- <480px: single column
- ≥900px: sidebar + grid

## 🔒 Privacidad

- Público con `noindex` (herramienta interna)
- Verificar que videos no expongan datos personales
- Control de acceso real (futuro): Cloudflare Access

## 📚 Stack

HTML + CSS + JavaScript vanilla (sin dependencias).  
Hosting: GitHub Pages (`cotizadora.github.io/confianza-tutoriales/`)

---

**Creada por Eduardo Pérez**  
[Soporte WhatsApp](https://wa.me/56927690949?text=Soporte%20app%20tutoriales)
