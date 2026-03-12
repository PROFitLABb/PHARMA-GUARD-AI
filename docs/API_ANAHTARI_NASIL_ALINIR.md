# 🔑 Groq API Anahtarı Nasıl Alınır?

## Adım 1: Groq Console'a Gidin
https://console.groq.com

## Adım 2: Hesap Oluşturun
- "Sign Up" butonuna tıklayın
- Google, GitHub veya email ile kayıt olun
- Ücretsiz hesap yeterli!

## Adım 3: API Key Oluşturun
1. Sol menüden "API Keys" sekmesine tıklayın
2. "Create API Key" butonuna tıklayın
3. Anahtara bir isim verin (örn: "pharma-guard")
4. "Submit" butonuna tıklayın

## Adım 4: Anahtarı Kopyalayın
- Oluşturulan anahtar `gsk_` ile başlar
- **ÖNEMLİ:** Bu anahtarı sadece bir kez görebilirsiniz!
- Hemen kopyalayın ve güvenli bir yere kaydedin

## Adım 5: Projeye Ekleyin

### Yöntem 1: .env dosyası (Önerilen)
`.env` dosyasını açın ve anahtarınızı yapıştırın:
```
GROQ_API_KEY=gsk_BURAYA_GERÇEK_ANAHTARINIZI_YAPIŞTIRIN
```

### Yöntem 2: Streamlit Secrets
`.streamlit/secrets.toml` dosyasını açın:
```toml
GROQ_API_KEY = "gsk_BURAYA_GERÇEK_ANAHTARINIZI_YAPIŞTIRIN"
```

## Adım 6: Streamlit'i Yeniden Başlatın
```bash
# Terminal'de Ctrl+C ile durdurun
# Sonra tekrar çalıştırın:
streamlit run app.py
```

## 🎁 Ücretsiz Limitler
- **Llama 3.2 Vision (90B):** 30 istek/dakika
- **Llama 3.1 (70B):** 30 istek/dakika
- **Günlük limit:** 14,400 istek

Bu limitler proje için fazlasıyla yeterli!

## ⚠️ Güvenlik Notları
- API anahtarınızı asla GitHub'a yüklemeyin
- `.env` ve `.streamlit/secrets.toml` dosyaları `.gitignore`'da
- Anahtarı kimseyle paylaşmayın

## 🆘 Sorun mu Yaşıyorsunuz?
- Anahtarın `gsk_` ile başladığından emin olun
- Boşluk veya satır sonu karakteri olmadığını kontrol edin
- Anahtarı yeniden oluşturmayı deneyin
- Groq Console'da "Usage" bölümünden limitinizi kontrol edin

## 📚 Daha Fazla Bilgi
https://console.groq.com/docs/quickstart
