# 🚀 PHARMA-GUARD AI Kurulum Rehberi

## 1. Gereksinimler
- Python 3.8 veya üzeri
- Groq API anahtarı (ücretsiz: https://console.groq.com)

## 2. Adım Adım Kurulum

### Adım 1: Kütüphaneleri Yükleyin
```bash
pip install -r requirements.txt
```

**Not:** Eğer `googletrans` uyarısı alırsanız görmezden gelebilirsiniz (kullanmıyoruz).

### Adım 2: Groq API Anahtarı Alın
1. https://console.groq.com adresine gidin
2. Ücretsiz hesap oluşturun
3. API Keys bölümünden yeni anahtar oluşturun
4. Anahtarı kopyalayın (gsk_ ile başlar)

### Adım 3: .env Dosyası Oluşturun
`.env` dosyasını düzenleyin ve API anahtarınızı ekleyin:
```
GROQ_API_KEY=gsk_your_actual_key_here
```

### Adım 4: Prospektüs Ekleyin (Opsiyonel)
`data/corpus/` klasörüne ilaç prospektüslerini .txt formatında ekleyin.

Örnek: `data/corpus/aspirin.txt`
```
ASPİRİN 500 MG TABLET

ETKİN MADDE: Asetilsalisilik asit 500 mg
KULLANIM AMACI: Ağrı kesici, ateş düşürücü
...
```

### Adım 5: Uygulamayı Başlatın
```bash
streamlit run app.py
```

Tarayıcınızda otomatik olarak açılacaktır: http://localhost:8501

## 3. Kullanım

1. İlaç kutusunun net fotoğrafını yükleyin
2. "Analizi Başlat" butonuna tıklayın
3. Raporu inceleyin ve PDF olarak indirin

## 4. Sorun Giderme

### Hata: "GROQ_API_KEY bulunamadı"
- `.env` dosyasının proje klasöründe olduğundan emin olun
- API anahtarının doğru kopyalandığını kontrol edin

### Hata: "httpx import hatası"
```bash
pip install --upgrade httpx groq
```

### Hata: "Prospektüs bulunamadı"
- `data/corpus/` klasörüne .txt dosyaları ekleyin
- Dosya uzantısının .txt olduğundan emin olun

## 5. Test

Örnek prospektüs dosyası eklenmiştir: `data/corpus/parol_ornek.txt`

Sistemi test etmek için herhangi bir ilaç kutusu fotoğrafı yükleyebilirsiniz.

## 6. Önemli Notlar

⚠️ Bu sistem eğitim amaçlıdır. Tıbbi kararlar için mutlaka sağlık profesyoneline danışın!

📊 Groq Limitleri:
- Ücretsiz tier: Günlük 14,400 istek
- Llama 3.2 Vision: Dakikada 30 istek
- Llama 3.1 70B: Dakikada 30 istek

Sorularınız için: https://console.groq.com/docs
