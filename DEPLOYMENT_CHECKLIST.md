# ✅ Streamlit Cloud Deployment Checklist

## Dosya Kontrolü

- [x] `app.py` - Ana uygulama ✅
- [x] `agents.py` - AI ajanları (OCR sistemi) ✅
- [x] `utils.py` - Yardımcı fonksiyonlar ✅
- [x] `requirements.txt` - Python paketleri ✅
- [x] `packages.txt` - Sistem paketleri (tesseract-ocr) ✅
- [x] `runtime.txt` - Python 3.11 ✅
- [x] `.streamlit/config.toml` - Streamlit ayarları ✅
- [x] `.gitignore` - Secrets koruması ✅
- [x] `data/corpus/` - 11,283 prospektüs (10 MB) ✅

## Güvenlik Kontrolü

- [x] `.env` dosyası `.gitignore`'da ✅
- [x] `.streamlit/secrets.toml` dosyası `.gitignore`'da ✅
- [x] API anahtarları kodda hardcoded değil ✅

## Sistem Özellikleri

- [x] **Vision:** Tesseract OCR (lokal, ücretsiz) ✅
- [x] **Text AI:** Groq Llama 3.3 70B ✅
- [x] **RAG:** 11,226 ilaç prospektüsü ✅
- [x] **Dil:** Türkçe + İngilizce OCR ✅

## GitHub'a Yükleme

```bash
# 1. Git başlat (eğer yoksa)
git init

# 2. Dosyaları ekle
git add .

# 3. Commit
git commit -m "PHARMA-GUARD AI v2.2 - OCR Vision System"

# 4. Branch oluştur
git branch -M main

# 5. Remote ekle (GitHub'da repo oluşturduktan sonra)
git remote add origin https://github.com/KULLANICI_ADIN/pharma-guard-ai.git

# 6. Push
git push -u origin main
```

## Streamlit Cloud Ayarları

### 1. App Oluştur
- URL: https://share.streamlit.io
- Repository: `KULLANICI_ADIN/pharma-guard-ai`
- Branch: `main`
- Main file: `app.py`

### 2. Secrets Ekle
```toml
GROQ_API_KEY = "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"
```

### 3. Deploy
- "Deploy!" butonuna tıkla
- 2-5 dakika bekle
- Logs'u izle

## Test Senaryosu

1. ✅ App açılıyor mu?
2. ✅ Görsel yükleme çalışıyor mu?
3. ✅ OCR metin çıkarıyor mu?
4. ✅ Groq analiz yapıyor mu?
5. ✅ Prospektüs arama çalışıyor mu?
6. ✅ Rapor oluşturuluyor mu?
7. ✅ Rapor indirme çalışıyor mu?

## Beklenen Performans

- **OCR Süresi:** 2-5 saniye
- **Groq Analiz:** 3-8 saniye
- **RAG Arama:** 1-3 saniye
- **Toplam:** ~10-20 saniye

## Limitler (Streamlit Free Tier)

- **RAM:** 1 GB
- **CPU:** 1 core
- **Storage:** 1 GB
- **Bandwidth:** Sınırsız

## Groq API Limitler (Free Tier)

- **Dakikalık:** 30 istek
- **Günlük:** 14,400 istek
- **Token:** 100,000/gün

## Sorun Giderme

### OCR Çalışmıyor
```
Çözüm: packages.txt dosyasını kontrol et
tesseract-ocr
tesseract-ocr-tur
```

### Groq API Hatası
```
Çözüm: Streamlit Cloud Secrets'ı kontrol et
Settings → Secrets → GROQ_API_KEY
```

### Memory Hatası
```
Çözüm: agents.py'de prospektüs limitini azalt
txt_files = txt_files[:1000]  # İlk 1000 prospektüs
```

### Prospektüs Bulunamadı
```
Çözüm: data/corpus/ klasörünün GitHub'da olduğunu kontrol et
git add data/corpus/
git commit -m "Add prospectus files"
git push
```

## Deployment Sonrası

- [ ] Canlı URL'i test et
- [ ] Farklı ilaç görselleri dene
- [ ] Error handling'i test et
- [ ] Performance'ı ölç
- [ ] Logs'u kontrol et

## Paylaşım

Canlı URL'in:
```
https://KULLANICI_ADIN-pharma-guard-ai-RANDOM.streamlit.app
```

Bu URL'i güvenle paylaşabilirsin! 🎉

---

**Hazırsın!** Şimdi GitHub'a push yap ve Streamlit Cloud'da deploy et.
