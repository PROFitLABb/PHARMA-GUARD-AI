# 💊 PHARMA-GUARD AI

<div align="center">

![Version](https://img.shields.io/badge/version-2.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-green.svg)
![License](https://img.shields.io/badge/license-Educational-orange.svg)
![Status](https://img.shields.io/badge/status-Active-success.svg)

**Yapay Zeka Destekli İlaç Analiz ve Güvenlik Sistemi**

[Özellikler](#-özellikler) • [Kurulum](#-kurulum) • [Kullanım](#-kullanım) • [Dokümantasyon](#-dokümantasyon) • [Lisans](#-lisans)

</div>

---

## 📋 İçindekiler

- [Genel Bakış](#-genel-bakış)
- [Özellikler](#-özellikler)
- [Teknoloji Stack](#-teknoloji-stack)
- [Kurulum](#-kurulum)
- [Kullanım](#-kullanım)
- [Veritabanı](#-veritabanı)
- [API Yapılandırması](#-api-yapılandırması)
- [Proje Yapısı](#-proje-yapısı)
- [Dokümantasyon](#-dokümantasyon)
- [Önemli Uyarılar](#-önemli-uyarılar)
- [Lisans](#-lisans)

---

## 🎯 Genel Bakış

PHARMA-GUARD AI, ilaç kutularının fotoğraflarını analiz ederek kapsamlı güvenlik ve kullanım bilgileri sunan yapay zeka destekli bir sistemdir. Sistem, görsel tanıma, doğal dil işleme ve 11,000+ ilaç prospektüsü içeren RAG (Retrieval-Augmented Generation) teknolojisini kullanır.

### 🎓 Eğitim Amaçlı Sistem

Bu sistem **eğitim ve bilgilendirme amaçlıdır**. Gerçek tıbbi kararlar için mutlaka sağlık profesyoneline danışın.

---

## ✨ Özellikler

### 🔍 Görsel Analiz
- **Tesseract OCR** ile metin çıkarma (ücretsiz, lokal)
- İlaç adı, etken madde, dozaj ve form tespiti
- Türkçe + İngilizce dil desteği
- Manuel giriş desteği (opsiyonel)

### 📚 Kapsamlı Veritabanı
- **11,226 ilaç** prospektüsü
- **21 farklı kategori** (Ağrı kesici, Antibiyotik, Kalp, vb.)
- Akıllı fuzzy matching algoritması
- Hızlı arama (<10 saniye)

### 🛡️ Güvenlik Analizi
- Yan etki tespiti
- İlaç etkileşimleri kontrolü
- Kullanım uyarıları
- Risk değerlendirmesi

### 📊 Detaylı Raporlama
- Kapsamlı analiz raporları
- Güven puanı sistemi
- Kaynak referansları
- TXT formatında rapor kaydetme

### 🌐 Kullanıcı Dostu Arayüz
- Streamlit tabanlı modern UI
- Türkçe dil desteği
- Sürükle-bırak dosya yükleme
- Responsive tasarım

---

## 🛠️ Teknoloji Stack

### AI & ML
- **Tesseract OCR** - Ücretsiz, lokal metin çıkarma
- **Groq Llama 3.3 70B** - Orkestratör, metin analizi ve RAG
- **RAG (Retrieval-Augmented Generation)** - 11,226 prospektüs arama

### Backend
- **Python 3.8+**
- **Streamlit** - Web framework
- **Pillow** - Görsel işleme
- **pytesseract** - OCR kütüphanesi
- **python-dotenv** - Ortam değişkenleri

### APIs
- Groq Cloud API (Text Analysis)

---

## 📦 Kurulum

### Gereksinimler

- Python 3.8 veya üzeri
- pip (Python paket yöneticisi)
- İnternet bağlantısı (API çağrıları için)

### Adım 1: Projeyi İndirin

```bash
git clone https://github.com/yourusername/pharma-guard-ai.git
cd pharma-guard-ai
```

### Adım 2: Bağımlılıkları Yükleyin

```bash
pip install -r requirements.txt
```

### Adım 3: API Anahtarlarını Yapılandırın

1. `.env.example` dosyasını `.env` olarak kopyalayın:
```bash
copy .env.example .env
```

2. `.env` dosyasını düzenleyin ve API anahtarınızı ekleyin:
```env
GROQ_API_KEY=your_groq_api_key_here
```

**API Anahtarı Nasıl Alınır?**
- **Groq API**: [console.groq.com](https://console.groq.com)

Detaylı talimatlar için `docs/API_ANAHTARI_NASIL_ALINIR.md` dosyasına bakın.

### Adım 4: Sistemi Başlatın

Veritabanı zaten 11,226 ilaç ile hazır. Hemen kullanmaya başlayabilirsiniz!

---

## 🚀 Kullanım

### Hızlı Başlangıç (Windows)

```bash
GERCEK_SISTEM_BASLAT.bat
```

### Manuel Başlatma

```bash
streamlit run app.py
```

### Kullanım Adımları

1. **Sistemi Başlatın**: Tarayıcınızda otomatik olarak açılacaktır
2. **İlaç Fotoğrafı Yükleyin**: "Browse files" butonuna tıklayın
3. **Analiz Edin**: "🔍 İlacı Analiz Et" butonuna basın
4. **Sonuçları İnceleyin**: Detaylı raporu görüntüleyin
5. **Rapor Kaydedin**: İsterseniz raporu TXT olarak kaydedin

### En İyi Sonuçlar İçin

- ✅ Net ve iyi ışıklandırılmış fotoğraflar çekin
- ✅ İlaç adının görünür olduğundan emin olun
- ✅ Kutuyu düz açıdan çekin
- ✅ Desteklenen formatlar: JPG, PNG, JPEG

---

## 📊 Veritabanı

### İstatistikler

- **Toplam İlaç**: 11,226
- **Toplam Dosya**: 11,280 prospektüs
- **Veritabanı Boyutu**: 10.03 MB
- **Kategoriler**: 21

### Kategori Dağılımı (Top 10)

| Kategori | İlaç Sayısı |
|----------|-------------|
| Ağrı Kesici | 5,733 |
| Antibiyotik | 1,400 |
| Mide | 756 |
| Kalp | 672 |
| Vitamin | 448 |
| Tansiyon | 440 |
| Diyabet | 256 |
| Astım | 252 |
| Antidepresan | 216 |
| Hormon | 216 |

### Veritabanı Yönetimi

Prospektüsler `data/corpus/` klasöründe TXT formatında saklanır. Veritabanı 11,226 ilaç ile hazır durumda.

---

## 🔑 API Yapılandırması

### Groq API (Görsel + Metin Analizi)

```python
GROQ_API_KEY=gsk_your_api_key_here
```

**Modeller**: 
- llama-3.3-70b-versatile (Metin analiz ve RAG)

**Not:** Vision modelleri Groq tarafından kullanımdan kaldırıldı. Manuel giriş kullanılıyor.

### Streamlit Secrets (Alternatif)

`.streamlit/secrets.toml` dosyasını da kullanabilirsiniz:

```toml
GROQ_API_KEY = "your_groq_key"
```

---

## 📁 Proje Yapısı

```
pharma-guard-ai/
├── 📄 app.py                          # Ana uygulama
├── 📄 agents.py                       # AI ajanları (Vision, RAG, Security)
├── 📄 utils.py                        # Yardımcı fonksiyonlar
├── 📄 requirements.txt                # Python bağımlılıkları
├── 📄 runtime.txt                     # Python versiyonu (Streamlit Cloud)
├── 📄 packages.txt                    # Sistem bağımlılıkları
├── 📄 .env.example                    # Örnek ortam değişkenleri
├── 📄 .gitignore                      # Git ignore kuralları
├── 📄 START.bat                       # Windows başlatma scripti
│
├── 📁 data/
│   └── 📁 corpus/                     # 11,226 ilaç prospektüsü
│
├── 📁 reports/                        # Analiz raporları
├── 📁 uploads/                        # Yüklenen görseller
│
├── 📁 .streamlit/
│   ├── 📄 config.toml                 # Streamlit yapılandırması
│   └── 📄 secrets.toml                # API anahtarları
│
├── 📁 docs/                           # Dokümantasyon
│   ├── 📄 KURULUM.md
│   ├── 📄 HATA_COZUMLERI.md
│   ├── 📄 HIZLI_BASLANGIC.md
│   ├── 📄 API_ANAHTARI_NASIL_ALINIR.md
│   └── 📄 STREAMLIT_CLOUD_DEPLOYMENT.md
│
└── 📁 scripts/                        # Yardımcı scriptler
    ├── 📄 GERCEK_SISTEM_BASLAT.bat
    └── 📄 TEMIZ_BASLATMA.bat
```
│
└── 📁 scripts/                        # Yardımcı scriptler
    ├── 📄 GERCEK_SISTEM_BASLAT.bat
    ├── 📄 DEMO_BASLAT.bat
    └── 📄 TEMIZ_BASLATMA.bat
```

---

## 📚 Dokümantasyon

### Kurulum ve Yapılandırma
- [KURULUM.md](docs/KURULUM.md) - Detaylı kurulum talimatları
- [API_ANAHTARI_NASIL_ALINIR.md](docs/API_ANAHTARI_NASIL_ALINIR.md) - Groq API anahtarı

### Kullanım Kılavuzları
- [HIZLI_BASLANGIC.md](docs/HIZLI_BASLANGIC.md) - Hızlı başlangıç rehberi
- [STREAMLIT_CLOUD_DEPLOYMENT.md](docs/STREAMLIT_CLOUD_DEPLOYMENT.md) - Cloud deployment

### Sorun Giderme
- [HATA_COZUMLERI.md](docs/HATA_COZUMLERI.md) - Yaygın hatalar ve çözümleri

---

## ⚠️ Önemli Uyarılar

### 🚨 Tıbbi Sorumluluk Reddi

- Bu sistem **eğitim ve bilgilendirme amaçlıdır**
- Gerçek tıbbi kararlar için **mutlaka doktora danışın**
- İlaç kullanımında **prospektüsü okuyun**
- Şüphe durumunda **eczacıya sorun**
- Sistem %100 doğru değildir

### 🔒 Güvenlik

- API anahtarlarınızı **asla paylaşmayın**
- `.env` dosyasını **Git'e eklemeyin**
- Üretim ortamında **güvenlik önlemleri alın**

### 📊 Sınırlamalar

- Sistem bazı ilaçları tanımayabilir
- Yeni ilaçlar veritabanında olmayabilir
- Güven puanı 8'in altındaysa dikkatli olun
- Görsel kalitesi düşük fotoğraflar hata verebilir

---

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Lütfen şu adımları izleyin:

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. Pull Request açın

---

## 🐛 Hata Bildirimi

Hata bulursanız lütfen [issue açın](https://github.com/yourusername/pharma-guard-ai/issues) ve şunları ekleyin:

- Hatanın detaylı açıklaması
- Hata mesajı (varsa)
- Adım adım tekrarlama yöntemi
- Sistem bilgileri (OS, Python versiyonu)

---

## 📝 Lisans

Bu proje **eğitim amaçlıdır** ve MIT Lisansı altında lisanslanmıştır.

```
MIT License

Copyright (c) 2026 PHARMA-GUARD AI

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 👥 Ekip

**PHARMA-GUARD AI Development Team**

- Görsel Analiz: Google Gemini Vision 2.5 Flash
- Metin Analizi: Groq Llama 3.3 70B
- RAG Sistemi: Custom Implementation
- UI/UX: Streamlit Framework

---

## 📞 İletişim

Sorularınız için:
- 📧 Email: support@pharma-guard-ai.com
- 🐛 Issues: [GitHub Issues](https://github.com/yourusername/pharma-guard-ai/issues)
- 📖 Docs: [Dokümantasyon](docs/)

---

## 🙏 Teşekkürler

- [Google Gemini](https://ai.google.dev/) - Görsel analiz API'si
- [Groq](https://groq.com/) - Hızlı LLM inference
- [Streamlit](https://streamlit.io/) - Web framework
- Tüm katkıda bulunanlara

---

## 📈 Versiyon Geçmişi

### v2.0 (2026-03-12)
- ✨ 11,000+ ilaç prospektüsü eklendi
- ⚡ RAG sistemi optimize edildi
- 🎨 UI iyileştirmeleri
- 🐛 Bug düzeltmeleri

### v1.0 (2026-03-10)
- 🎉 İlk sürüm
- 🔍 Görsel analiz
- 📚 49 ilaç prospektüsü
- 🛡️ Güvenlik analizi

---

<div align="center">

**⭐ Projeyi beğendiyseniz yıldız vermeyi unutmayın! ⭐**

Made with ❤️ by PHARMA-GUARD AI Team

[⬆ Başa Dön](#-pharma-guard-ai)

</div>
