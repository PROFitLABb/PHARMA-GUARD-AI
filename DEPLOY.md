# 🚀 Deployment Rehberi

## GitHub'a Push

```bash
git add .
git commit -m "v2.1.0 - Proje temizlendi, API güncellemeleri"
git push origin main
```

## Streamlit Cloud Deployment

### 1. Streamlit Cloud'a Giriş
- https://share.streamlit.io/
- GitHub hesabınızla giriş yapın

### 2. Yeni Uygulama Deploy Et (İlk Kez)
- "New app" butonuna tıklayın
- Repository: `pharma-guard-ai`
- Branch: `main`
- Main file path: `app.py`
- "Deploy!" butonuna tıklayın

### 3. Secrets Yapılandırması (ÖNEMLİ!)
Deploy başladıktan sonra:

1. Uygulamanızı seçin
2. Sağ üstteki **⚙️ Settings** → **Secrets**
3. Aşağıdaki secrets'ı ekleyin:

```toml
GROQ_API_KEY = "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"
GEMINI_API_KEY = "AIzaSyCmvHFDdEMiEDgN14l298jZ0OVJ3-Du1tk"
GOOGLE_API_KEY = "AIzaSyCmvHFDdEMiEDgN14l298jZ0OVJ3-Du1tk"
```

4. **Save** butonuna basın
5. Uygulama otomatik olarak yeniden başlayacak (30-60 saniye)

### 4. Deployment Durumu
- ✅ **Running**: Uygulama çalışıyor
- 🔄 **Building**: Deploy ediliyor
- ❌ **Error**: Hata var, logları kontrol edin

### 5. Güncelleme (Sonraki Pushlar)
GitHub'a her push yaptığınızda Streamlit Cloud otomatik olarak yeniden deploy eder.

## Deployment Sonrası Kontroller

### ✅ Checklist
- [ ] Uygulama açılıyor mu?
- [ ] Groq API çalışıyor mu? (Sidebar'da ✅ Groq API: Aktif)
- [ ] Gemini API çalışıyor mu? (Sidebar'da ✅ Gemini API: Aktif)
- [ ] Görsel yükleme çalışıyor mu?
- [ ] Analiz butonu çalışıyor mu?
- [ ] Rapor oluşturuluyor mu?

### 🐛 Sorun Giderme

**1. API Anahtarı Hatası**
- Settings → Secrets'ı kontrol edin
- Anahtarların doğru kopyalandığından emin olun
- Tırnak işaretlerini kontrol edin

**2. Module Not Found Hatası**
- `requirements.txt` dosyasını kontrol edin
- Tüm bağımlılıklar listelenmiş mi?

**3. Prospektüs Bulunamadı**
- `data/corpus/` klasörü GitHub'da var mı?
- `.gitignore` içinde `data/` yok mu?

**4. Rate Limit Hatası**
- Normal! Groq ücretsiz tier limiti
- Yarın sabah sıfırlanır
- Kullanıcılara bilgi mesajı gösterilir

## Önemli Notlar

### 🔒 Güvenlik
- ✅ `.env` dosyası `.gitignore` içinde
- ✅ `secrets.toml` dosyası `.gitignore` içinde
- ✅ API anahtarları sadece Streamlit Cloud Secrets'ta
- ❌ API anahtarlarını asla GitHub'a push etmeyin

### 📊 Performans
- İlk yükleme: ~10 saniye (11,226 prospektüs)
- Analiz süresi: 30-60 saniye
- Groq limit: 30 istek/dakika, 100,000 token/gün
- Gemini limit: Genellikle yeterli (ücretsiz tier)

### 🔄 Güncelleme Süreci
1. Lokal değişiklik yap
2. Test et
3. `git add .`
4. `git commit -m "açıklama"`
5. `git push origin main`
6. Streamlit Cloud otomatik deploy eder

## Deployment URL
Deployment tamamlandığında URL şu formatta olacak:
```
https://pharma-guard-ai-[random].streamlit.app
```

Bu URL'yi README.md'ye ekleyebilirsiniz.

---

**Başarılar! 🎉**
