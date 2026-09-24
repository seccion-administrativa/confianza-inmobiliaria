@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion
cd /d "%~dp0"

echo.
echo ╔════════════════════════════════════════════════╗
echo ║   CONFIANZA TUTORIALES - SETUP GITHUB          ║
echo ╚════════════════════════════════════════════════╝
echo.
echo Este script abre GitHub para que crees el repo.
echo.
echo INSTRUCCIONES:
echo 1. Se abrirá GitHub en tu navegador
echo 2. Completa el formulario:
echo    - Repository name: confianza-tutoriales
echo    - Description: Centro de tutoriales para ejecutivos de Confianza Inmobiliaria
echo    - Public (checkbox)
echo    - Desactiva "Add a README file"
echo 3. Click en "Create repository"
echo 4. Vuelve aquí y presiona ENTER
echo 5. Se hará push automático
echo.
pause

REM Abrir GitHub
echo Abriendo GitHub...
start https://github.com/new

echo.
echo Espera a que se abra tu navegador...
timeout /t 3 >nul

echo.
echo Una vez que hayas creado el repo en GitHub, presiona ENTER aquí...
pause

REM Hacer push
echo.
echo [1/3] Configurando git...
git config --local user.name "Eduardo Perez"
git config --local user.email "eduardoperez.contacto@gmail.com"
echo ✓ Configurado

echo [2/3] Agregando remote origin...
git remote remove origin >nul 2>&1
git remote add origin https://github.com/cotizadora/confianza-tutoriales.git
echo ✓ Remote agregado

echo [3/3] Haciendo push a GitHub...
echo.
git push -u origin main

if errorlevel 1 (
    echo.
    echo ⚠️  Posible error. GitHub te pedirá login/autenticación.
    echo Completa el login en el navegador si es necesario.
    echo.
) else (
    echo.
    echo ✅ ¡PUSH COMPLETADO!
)

echo.
echo ════════════════════════════════════════════════
echo La app estará en vivo en:
echo https://cotizadora.github.io/confianza-tutoriales/
echo.
echo Espera 2-3 minutos para que GitHub active Pages.
echo ════════════════════════════════════════════════
echo.
pause
