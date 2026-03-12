# 🚀 Streamlit Cloud Deployment Rehberi

## 📋 Ön Hazırlık

### 1. GitHub Repository Hazırlığı

Projenizin GitHub'da olması gerekiyor:

```bash
git init
git add .
git commit -m "Initial commit: PHARMA-GUARD AI v2.1"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/pharma-guard-ai.git
git push -u origin main
```

### 2. Gerekli Dosyalar

✅ Aşağıdaki dosyaların repository'de olduğundan emin olun:

- `app.py` - Ana uygulama
- `requirements.txt` - Python bağımlılıkları
- `packages.txt` - Sistem bağımlılıkları
- `runtime.txt` - Python versiyonu
- `.streamlit/config.toml` - Streamlit yapılandırması
- `agents.py`, `utils.py` - Yardımcı modüller

⚠️ **ÖNEMLİ:** `.env` ve `.streamlit/secrets.toml` dosyalarını GitHub'a YÜKLEMEYIN!

## 🌐 Streamlit Cloud'a Deploy

### Adım 1: Streamlit Cloud'a Giriş

1. https://share.streamlit.io adresine gidin
2. GitHub hesabınızla giriş yapın
3. "New app" butonuna tıklayın

### Adım 2: Repository Seçimi

1. **Repository:** `YOUR_USERNAME/pharma-guard-ai`
2. **Branch:** `main`
3. **Main file path:** `app.py`

### Adım 3: Secrets Yapılandırması

"Advanced settings" → "Secrets" bölümüne gidin ve şunu ekleyin:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

**API Anahtarınızı Buraya Girin:**
- Groq: https://console.groq.com

**NOT:** Artık sadece Groq API gerekiyor! Tesseract OCR lokal olarak çalışır.

### Adım 4: Deploy

"Deploy!" butonuna tıklayın ve bekleyin (2-5 dakika).

## 🔧 Sorun Giderme

### Pillow Hatası

**Hata:** `KeyError: '__version__'` (Pillow build hatası)

**Çözüm:** `requirements.txt` dosyasında:
```
pillow>=10.4.0  # Eski: pillow==10.2.0
```

### Python Versiyonu Hatası

**Hata:** Python 3.14 uyumsuzluğu

**Çözüm:** `runtime.txt` dosyası oluşturun:
```
python-3.11
```

### Prospektüs Dosyaları Yüklenmiyor

**Sorun:** `data/corpus/` klasörü çok büyük (11,000+ dosya)

**Çözüm 1:** Git LFS kullanın
```bash
git lfs install
git lfs track "data/corpus/*.txt"
git add .gitattributes
git add data/corpus/
git commit -m "Add prospectus files with LFS"
git push
```

**Çözüm 2:** Prospektüsleri harici depolama kullanın
- Google Drive
- AWS S3
- GitHub Releases

**Çözüm 3:** Prospektüs sayısını azaltın (demo için)
```bash
# İlk 100 prospektüsü tut
cd data/corpus
ls *.txt | head -100 > keep.txt
ls *.txt | grep -v -f keep.txt | xargs rm
```

### Memory Hatası

**Hata:** Out of memory

**Çözüm:** RAG agent'ı optimize edin - tüm prospektüsleri yüklemeyin:

```python
# agents.py içinde
def initialize_db(self):
    # Sadece ilk 1000 prospektüsü yükle
    txt_files = [f for f in os.listdir(self.corpus_path) if f.endswith('.txt')][:1000]
```

### API Key Bulunamadı

**Hata:** `GROQ_API_KEY bulunamadı!`

**Çözüm:** Streamlit Cloud Secrets'ı kontrol edin:
1. App settings → Secrets
2. API anahtarlarını ekleyin
3. App'i yeniden başlatın

## 📊 Deployment Checklist

- [ ] GitHub repository oluşturuldu
- [ ] Tüm dosyalar commit edildi
- [ ] `.env` ve `secrets.toml` .gitignore'da
- [ ] `requirements.txt` güncellendi (pillow>=10.4.0)
- [ ] `runtime.txt` oluşturuldu (python-3.11)
- [ ] `packages.txt` oluşturuldu
- [ ] `.streamlit/config.toml` oluşturuldu
- [ ] Streamlit Cloud'da app oluşturuldu
- [ ] Secrets yapılandırıldı (GROQ_API_KEY)
- [ ] Deploy tamamlandı
- [ ] App test edildi
- [ ] OCR çalışıyor mu test edildi

## 🎯 Optimizasyon İpuçları

### 1. Prospektüs Veritabanını Küçült

Demo için 100-500 prospektüs yeterli:

```bash
cd data/corpus
# En yaygın ilaçları tut
ls parol* aspirin* augmentin* nexium* lustral* | head -100 > keep.txt
```

### 2. Lazy Loading

Prospektüsleri ihtiyaç anında yükle:

```python
@st.cache_resource
def load_rag_agent():
    return RAGAgent(groq_client=client)
```

### 3. Caching

Streamlit caching kullan:

```python
@st.cache_data
def analyze_drug(image_path):
    # Analiz kodu
    pass
```

## 🔗 Faydalı Linkler

- **Streamlit Cloud Docs:** https://docs.streamlit.io/streamlit-community-cloud
- **Deployment Guide:** https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app
- **Secrets Management:** https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app/secrets-management
- **Git LFS:** https://git-lfs.github.com/

## 💡 Pro Tips

1. **Free Tier Limits:**
   - 1 GB RAM
   - 1 CPU core
   - 1 GB storage
   - Unlimited apps (public)

2. **Performance:**
   - Prospektüs sayısını sınırlayın
   - Caching kullanın
   - Lazy loading uygulayın

3. **Security:**
   - API anahtarlarını asla commit etmeyin
   - Secrets kullanın
   - `.gitignore` kontrol edin

4. **Monitoring:**
   - Streamlit Cloud logs'u izleyin
   - Error tracking ekleyin
   - Usage metrics takip edin

---

**Başarılı deployment!** 🎉

Sorularınız için: https://discuss.streamlit.io
