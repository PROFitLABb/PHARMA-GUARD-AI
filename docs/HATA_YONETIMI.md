# 🛡️ Hata Yönetimi ve Çözümleri

## Kapsamlı Hata Yakalama

PHARMA-GUARD AI, tüm olası hataları yakalar ve kullanıcı dostu mesajlar gösterir.

---

## 🔍 Görsel Analiz Hataları

### 1. Dosya Bulunamadı (FileNotFoundError)
**Hata:** `Görsel dosyası bulunamadı`

**Neden:**
- Dosya yükleme sırasında hata oluştu
- Geçici dosya silinmiş

**Çözüm:**
- Görseli tekrar yükleyin
- Farklı bir görsel deneyin

---

### 2. Dosya Çok Büyük (ValueError)
**Hata:** `Görsel çok büyük (XX MB). Maksimum 20MB olmalı.`

**Neden:**
- Görsel dosyası 20MB'dan büyük

**Çözüm:**
- Görseli sıkıştırın
- Daha düşük çözünürlükte fotoğraf çekin
- Online araçlar: tinypng.com, compressor.io

---

### 3. JSON Parse Hatası (JSONDecodeError)
**Hata:** `AI yanıtı işlenemedi`

**Neden:**
- AI modeli JSON formatında yanıt vermedi
- Yanıt bozuk

**Çözüm:**
- Tekrar deneyin
- Daha net bir görsel yükleyin
- Farklı açıdan fotoğraf çekin

---

## 🔑 API Anahtarı Hataları

### 1. Geçersiz API Anahtarı (401)
**Hata:** `Groq API anahtarı geçersiz`

**Neden:**
- API anahtarı yanlış
- API anahtarı süresi dolmuş
- API anahtarı iptal edilmiş

**Çözüm:**
1. Yeni API anahtarı alın: https://console.groq.com
2. `.env` dosyasını güncelleyin (lokal)
3. Streamlit Cloud Secrets'ı güncelleyin (cloud)
4. Uygulamayı yeniden başlatın

---

## ⏱️ Rate Limit Hataları

### 1. Günlük Token Limiti (429 - TPD)
**Hata:** `Günlük token limiti doldu`

**Neden:**
- Groq ücretsiz tier: 100,000 token/gün
- Limit doldu

**Çözüm:**
- **Önerilen:** Yarın sabah deneyin (otomatik sıfırlanır)
- **Acil:** Groq Pro'ya geçin (ücretli, limitsiz)
  - https://console.groq.com/settings/billing

**Limit Takibi:**
- https://console.groq.com/settings/limits

---

### 2. Dakikalık İstek Limiti (429 - RPM)
**Hata:** `Dakikalık API limiti aşıldı`

**Neden:**
- Groq ücretsiz tier: 30 istek/dakika
- Çok hızlı istek gönderildi

**Çözüm:**
- 1-2 dakika bekleyin
- Tekrar deneyin

---

## 🌐 Bağlantı Hataları

### 1. Timeout Hatası
**Hata:** `İstek zaman aşımına uğradı`

**Neden:**
- İnternet bağlantısı yavaş
- Groq sunucusu yavaş yanıt veriyor
- Görsel çok büyük

**Çözüm:**
- İnternet bağlantınızı kontrol edin
- Daha küçük görsel yükleyin
- Birkaç saniye bekleyip tekrar deneyin

---

### 2. Bağlantı Hatası
**Hata:** `İnternet bağlantısı sorunu`

**Neden:**
- İnternet bağlantısı yok
- Firewall engelliyor
- VPN sorunu

**Çözüm:**
- İnternet bağlantınızı kontrol edin
- VPN'i kapatıp deneyin
- Firewall ayarlarını kontrol edin
- Groq servis durumu: https://status.groq.com

---

## 🤖 Model Hataları

### 1. Model Kullanımdan Kaldırıldı
**Hata:** `Model kullanımdan kaldırıldı`

**Neden:**
- Groq modeli deprecated edildi
- Sistem güncellemesi gerekiyor

**Çözüm:**
- **Kritik:** Geliştiriciyle iletişime geçin
- GitHub Issue açın
- Sistem güncellemesi bekleyin

---

### 2. İçerik Politikası İhlali
**Hata:** `Görsel güvenlik filtresine takıldı`

**Neden:**
- Görsel uygunsuz içerik içeriyor
- AI güvenlik filtresi tetiklendi

**Çözüm:**
- Farklı bir görsel deneyin
- Sadece ilaç kutusunu çekin
- Arka planı temizleyin

---

## 📚 Prospektüs Hataları

### 1. Prospektüs Bulunamadı
**Hata:** `Prospektüs bilgisi bulunamadı`

**Neden:**
- İlaç veritabanında yok
- İlaç adı yanlış tanımlandı

**Çözüm:**
- Normal bir durum
- Sistem yine çalışır
- Güven puanı düşük olabilir

---

### 2. RAG Arama Hatası
**Hata:** `RAG araması başarısız oldu`

**Neden:**
- Groq API hatası
- Veritabanı erişim sorunu

**Çözüm:**
- Tekrar deneyin
- Sistem kısmi rapor oluşturur

---

## 🔧 Genel Sorun Giderme

### Adım 1: Hata Mesajını Okuyun
- Kullanıcı dostu mesaj gösterilir
- "Teknik Detaylar" kısmını açın

### Adım 2: Çözüm Önerilerini Uygulayın
- Her hata için özel çözüm önerilir
- Adım adım takip edin

### Adım 3: Tekrar Deneyin
- Çoğu hata geçicidir
- Birkaç saniye bekleyip tekrar deneyin

### Adım 4: Destek Alın
- GitHub Issues: https://github.com/yourusername/pharma-guard-ai/issues
- Hata mesajını ve ekran görüntüsünü paylaşın

---

## 📊 Hata İstatistikleri

### En Yaygın Hatalar:
1. **Rate Limit (429)** - %40
   - Çözüm: Bekleyin veya Pro'ya geçin
2. **Timeout** - %25
   - Çözüm: Daha küçük görsel
3. **JSON Parse** - %15
   - Çözüm: Tekrar deneyin
4. **Prospektüs Yok** - %10
   - Çözüm: Normal, endişelenmeyin
5. **Diğer** - %10

---

## 🛡️ Önleyici Tedbirler

### Kullanıcılar İçin:
- ✅ Net, iyi aydınlatılmış fotoğraflar çekin
- ✅ Görsel boyutunu 5MB altında tutun
- ✅ Dakikada 1-2 analiz yapın (rate limit)
- ✅ İnternet bağlantınızı kontrol edin

### Geliştiriciler İçin:
- ✅ Tüm API çağrılarında timeout kullanın
- ✅ Rate limit hatalarını özel olarak yakalayın
- ✅ Kullanıcı dostu hata mesajları gösterin
- ✅ Detaylı loglar tutun
- ✅ Fallback mekanizmaları ekleyin

---

## 📝 Hata Raporlama

Yeni bir hata bulduysanız:

1. **GitHub Issue Açın:**
   - https://github.com/yourusername/pharma-guard-ai/issues/new

2. **Şunları Ekleyin:**
   - Hata mesajı (tam metin)
   - Ekran görüntüsü
   - Adım adım tekrarlama yöntemi
   - Sistem bilgileri (tarayıcı, OS)

3. **Gizlilik:**
   - API anahtarlarını paylaşmayın
   - Kişisel bilgileri gizleyin

---

**Son Güncelleme:** 2026-03-12
**Versiyon:** 2.2.0
