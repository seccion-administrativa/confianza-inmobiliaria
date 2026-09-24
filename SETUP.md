# Setup para GitHub Pages

## 1. Crear el repo en GitHub

1. Ve a https://github.com/new
2. **Repository name:** `confianza-tutoriales`
3. **Description:** Centro de tutoriales para ejecutivos de Confianza Inmobiliaria
4. **Public** (no marques privado)
5. Desactiva "Add a README file" (ya existe)
6. Crea el repo

## 2. Hacer push desde local

En PowerShell:
```powershell
cd C:\Users\eduardo.perez\Documents\confianza\tutoriales-web
git push -u origin main
```

Git te pedirá login (usa el navegador que aparecerá).

## 3. Activar Pages

1. Ve a https://github.com/seccion-administrativa/confianza-inmobiliaria
2. Settings → Pages
3. **Source:** Deploy from a branch
4. **Branch:** main / root
5. Espera ~2 min

Tu app estará en: **https://seccion-administrativa.github.io/confianza-inmobiliaria/**

## 4. Agregar tutoriales

Edita `data/tutoriales.json`:
```json
{
  "id": "tut-002",
  "slug": "nuevo-tutorial",
  "titulo": "Título del tutorial",
  "descripcion": "Breve descripción",
  "categoria": "id-categoria",
  "etiquetas": ["tag1", "tag2"],
  "video": {
    "proveedor": "drive",
    "id": "1dAL...EvT"
  },
  "estado": "publicado"
}
```

Luego:
```bash
git add data/tutoriales.json
git commit -m "Agregar tutorial: Título"
git push
```

¡Listo! La app se actualiza en ~1 min.

## 5. Generar thumbnails (opcional)

```bash
cd tools
python build.py
ffmpeg -ss 3 -i video.mp4 -frames:v 1 -vf scale=640:-2 ../thumbs/tut-NNN.webp
git add ../thumbs/
git commit -m "Agregar thumbnail"
git push
```

## 6. Cambiar proveedor (Drive → YouTube)

Solo edita `video.proveedor` en el JSON. No requiere cambios en código.

---

**¿Problemas?** Abre un issue en https://github.com/seccion-administrativa/confianza-inmobiliaria/issues
