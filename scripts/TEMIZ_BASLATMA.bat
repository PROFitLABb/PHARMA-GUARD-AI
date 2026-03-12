@echo off
chcp 65001 >nul
cls

echo ============================================================
echo    💊 PHARMA-GUARD AI - Temiz Başlatma
echo ============================================================
echo.
echo 🧹 Cache temizleniyor...

cd ..
rmdir /s /q __pycache__ 2>nul
rmdir /s /q .streamlit\cache 2>nul

echo ✅ Cache temizlendi
echo.
echo 🚀 Sistem başlatılıyor...
echo.

streamlit run app.py

pause
