@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion
cd /d "%~dp0"

echo.
echo ╔════════════════════════════════════════════════╗
echo ║   CONFIANZA TUTORIALES - PUSH A GITHUB         ║
echo ╚════════════════════════════════════════════════╝
echo.

REM Verificar que el repo existe en GitHub
echo [1/4] Verificando conexión a GitHub...
git ls-remote https://github.com/seccion-administrativa/confianza-inmobiliaria.git >nul 2>&1
if errorlevel 1 (
    echo.
    echo ❌ ERROR: El repo no existe en GitHub
    echo.
    echo Crea el repo PRIMERO:
    echo 1. Ve a https://github.com/new
    echo 2. Repository name: confianza-tutoriales
    echo 3. Descripción: Centro de tutoriales para ejecutivos de Confianza Inmobiliaria
    echo 4. Public (sin README)
    echo 5. Create repository
    echo.
    echo Luego vuelve a ejecutar este archivo.
    echo.
    pause
    exit /b 1
)

echo ✓ Repo encontrado

REM Agregar remote si no existe
echo [2/4] Configurando remote...
git remote get-url origin >nul 2>&1
if errorlevel 1 (
    git remote add origin https://github.com/seccion-administrativa/confianza-inmobiliaria.git
    echo ✓ Remote agregado
) else (
    echo ✓ Remote ya existe
)

REM Configurar git
echo [3/4] Verificando configuración git...
for /f "delims=" %%i in ('git config user.name') do set gitname=%%i
if "!gitname!"=="" (
    echo Usuario git no configurado. Configurando...
    git config --local user.name "Eduardo Perez"
    git config --local user.email "eduardoperez.contacto@gmail.com"
    echo ✓ Configurado
) else (
    echo ✓ Usuario: !gitname!
)

REM Push
echo [4/4] Haciendo push a GitHub...
echo.
git push -u origin main
if errorlevel 1 (
    echo.
    echo ❌ Error al hacer push
    echo.
    echo GitHub te pedirá login en el navegador.
    echo Usa "Authorize with GitHub" o ingresa tu password.
    echo.
    pause
    exit /b 1
)

echo.
echo ╔════════════════════════════════════════════════╗
echo ║  ✅ PUSH COMPLETADO                           ║
echo ║                                                ║
echo ║  La app estará en vivo en:                    ║
echo ║  https://seccion-administrativa.github.io/confianza-inmobiliaria     ║
echo ║  tutoriales/                                  ║
echo ║                                                ║
echo ║  (Espera 2-3 minutos para que GitHub         ║
echo ║   active GitHub Pages)                        ║
echo ╚════════════════════════════════════════════════╝
echo.
pause
