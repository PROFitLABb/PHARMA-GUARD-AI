# 🔧 PHARMA-GUARD Hata Çözümleri

## ❌ Yaygın Hatalar ve Çözümleri

### 1. API Anahtarı Geçersiz (401 Error)

**Hata Mesajı:**
```
Hata kodu: 401 - {'error': {'message': 'Geçersiz API Anahtarı'}}
```

**Neden Oluşur:**
- API anahtarı yanlış girilmiş
- API anahtarının süresi dolmuş
- API anahtarı iptal edilmiş

**Çözüm:**
1. https://console.groq.com → API Keys
2. Eski anahtarı sil
3. "Create API Key" ile yeni anahtar oluştur
4. Anahtarı kopyala (gsk_ ile başlar)
5. `.env` dosyasını güncelle:
   ```
   GROQ_API_KEY=gsk_YENİ_ANAHTARINIZ
   ```
6. Streamlit'i yeniden başlat:
   - Terminal'de `Ctrl+C`
   - `streamlit run app.py`

---

### 2. API Limit Aşıldı (429 Error)

**Hata Mesajı:**
```
Hata kodu: 429 - Rate limit exceeded
```

**Neden Oluşur:**
- Dakikada 30 istek limitini aştınız
- Günlük 14,400 istek limitini aştınız

**Çözüm:**
- 1-2 dakika bekleyin (limit dakika başı sıfırlanır)
- https://console.groq.com/settings/limits → Limitinizi kontrol edin
- Ücretsiz hesapsa, Pro hesaba geçmeyi düşünün

---

### 3. Bağlantı Hatası (Connection Error)

**Hata Mesajı:**
```
Connection timeout / Connection refused
```

**Neden Oluşur:**
- İnternet bağlantısı yok
- Groq sunucuları erişilemiyor
- Firewall/VPN engelliyor

**Çözüm:**
- İnternet bağlantınızı kontrol edin
- VPN kullanıyorsanız kapatın
- Groq servis durumu: https://status.groq.com
- Firewall ayarlarını kontrol edin

---

### 4. Model Hatası (Model Not Available)

**Hata Mesajı:**
```
Model 'llama-3.2-90b-vision-preview' not available
```

**Neden Oluşur:**
- Model geçici olarak kullanılamıyor
- Model adı değişmiş

**Çözüm:**
- Birkaç dakika bekleyin
- https://console.groq.com/docs/models → Mevcut modelleri kontrol edin
- Alternatif model kullanın (agents.py'de model adını değiştirin)

---

### 5. Görsel Yüklenemedi

**Hata Mesajı:**
```
Geçersiz görsel dosyası
```

**Neden Oluşur:**
- Dosya bozuk
- Desteklenmeyen format
- Dosya çok büyük

**Çözüm:**
- JPG, JPEG veya PNG formatı kullanın
- Görsel boyutunu küçültün (max 5MB)
- Farklı bir görsel deneyin

---

### 6. Prospektüs Bulunamadı

**Hata Mesajı:**
```
Prospektüs veritabanı boş
```

**Neden Oluşur:**
- `data/corpus/` klasörü boş
- Dosya formatı yanlış

**Çözüm:**
- `data/corpus/` klasörüne .txt dosyaları ekleyin
- Dosya adı: `ilac_adi.txt`
- İçerik: Düz metin olarak prospektüs bilgileri

---

### 7. PDF Oluşturulamadı

**Hata Mesajı:**
```
PDF oluşturma hatası
```

**Neden Oluşur:**
- fpdf2 kütüphanesi yüklü değil
- Yazma izni yok

**Çözüm:**
```bash
pip install fpdf2
```
- `reports/` klasörünün yazma iznini kontrol edin

---

### 8. Streamlit Başlamıyor

**Hata Mesajı:**
```
ModuleNotFoundError / ImportError
```

**Neden Oluşur:**
- Gerekli kütüphaneler yüklü değil

**Çözüm:**
```bash
pip install -r requirements.txt --upgrade
```

---

### 9. .env Dosyası Okunamıyor

**Hata Mesajı:**
```
UnicodeDecodeError / GROQ_API_KEY bulunamadı
```

**Neden Oluşur:**
- Dosya encoding hatası
- Dosya yanlış konumda

**Çözüm:**
1. `.env` dosyasını sil
2. Yeniden oluştur (UTF-8 encoding ile):
   ```
   GROQ_API_KEY=gsk_your_key_here
   ```
3. Dosyanın proje kök dizininde olduğundan emin ol

---

### 10. Güven Puanı 0

**Hata Mesajı:**
```
Güven puanı düşük (0.0/10)
```

**Neden Oluşur:**
- API hatası oluştu
- Görsel analizi başarısız
- Model yanıt veremedi

**Çözüm:**
- Yukarıdaki hataları kontrol edin
- Daha net bir görsel yükleyin
- API anahtarını kontrol edin

---

## 🆘 Hala Sorun mu Yaşıyorsunuz?

1. **Logları Kontrol Edin:**
   - Terminal'deki hata mesajlarını okuyun
   - Streamlit arayüzündeki detaylı hata mesajlarını inceleyin

2. **Temiz Başlangıç:**
   ```bash
   # Tüm cache'i temizle
   streamlit cache clear
   
   # Kütüphaneleri yeniden yükle
   pip uninstall groq httpx -y
   pip install groq httpx --upgrade
   
   # Yeniden başlat
   streamlit run app.py
   ```

3. **Destek Kaynakları:**
   - Groq Docs: https://console.groq.com/docs
   - Groq Discord: https://discord.gg/groq
   - GitHub Issues: https://github.com/groq/groq-python/issues

---

## ✅ Sistem Sağlık Kontrolü

Sisteminizin düzgün çalıştığını kontrol etmek için:

```bash
# Python versiyonu (3.8+)
python --version

# Kütüphaneler yüklü mü?
pip list | grep groq
pip list | grep streamlit

# .env dosyası var mı?
cat .env  # veya Windows'ta: type .env

# Klasörler oluşturulmuş mu?
ls -la data/corpus uploads reports
```

Tüm kontroller başarılıysa sistem hazır!
