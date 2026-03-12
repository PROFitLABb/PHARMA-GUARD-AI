@echo off
chcp 65001 >nul
cls

echo ============================================================
echo    💊 PHARMA-GUARD AI - Demo Modu
echo ============================================================
echo.
echo 🎮 Demo modu başlatılıyor...
echo    (API anahtarı gerekmez)
echo.

cd ..
streamlit run app_demo.py

pause
