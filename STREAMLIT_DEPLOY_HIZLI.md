# 🚀 Streamlit Cloud'a Hızlı Deploy

## 1️⃣ GitHub'a Yükle

```bash
# Eğer henüz git init yapmadıysan
git init
git add .
git commit -m "PHARMA-GUARD AI - OCR Vision System"
git branch -M main

# GitHub'da yeni repo oluştur: pharma-guard-ai
# Sonra:
git remote add origin https://github.com/KULLANICI_ADIN/pharma-guard-ai.git
git push -u origin main
```

## 2️⃣ Streamlit Cloud'da Deploy

1. **https://share.streamlit.io** → Giriş yap (GitHub ile)

2. **"New app"** butonuna tıkla

3. **Ayarlar:**
   - Repository: `KULLANICI_ADIN/pharma-guard-ai`
   - Branch: `main`
   - Main file: `app.py`

4. **Advanced settings → Secrets:**
   ```toml
   GROQ_API_KEY = "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"
   ```

5. **Deploy!** → 2-5 dakika bekle

## ✅ Sistem Özellikleri

- ✅ **Tesseract OCR** - Streamlit Cloud'da otomatik yüklenir
- ✅ **11,226 ilaç** prospektüsü dahil
- ✅ **Sadece Groq API** gerekli (ücretsiz tier yeterli)
- ✅ **Türkçe + İngilizce** OCR desteği

## 🔍 Test Et

Deploy sonrası test için:
1. İlaç kutusu fotoğrafı yükle
2. OCR'ın metni okuduğunu kontrol et
3. Groq'un analiz yaptığını kontrol et
4. Rapor oluşturulduğunu kontrol et

## ⚠️ Önemli Notlar

- `.env` ve `secrets.toml` GitHub'a yüklenmez (`.gitignore`'da)
- Prospektüs dosyaları (`data/corpus/`) GitHub'a yüklenir
- OCR için ek API gerekmez (lokal çalışır)
- Groq ücretsiz tier: 30 istek/dakika, 14,400 istek/gün

## 🐛 Sorun Çıkarsa

**OCR çalışmıyor:**
- `packages.txt` dosyasının olduğundan emin ol
- Streamlit Cloud logs'u kontrol et

**Groq API hatası:**
- Secrets'ı kontrol et
- API key'in geçerli olduğundan emin ol

**Memory hatası:**
- Prospektüs sayısını azalt (agents.py'de limit ekle)

## 📱 Canlı URL

Deploy sonrası URL'in:
```
https://KULLANICI_ADIN-pharma-guard-ai-RANDOM.streamlit.app
```

Bu URL'i paylaşabilirsin!

---

**Başarılar!** 🎉
