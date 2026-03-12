# 📝 Değişiklik Günlüğü

Tüm önemli değişiklikler bu dosyada belgelenecektir.

## [2.1.0] - 2026-03-12

### ✨ Eklenenler
- Rate limit optimizasyonları (koşullu RAG ve Safety audit)
- Detaylı hata mesajları ve kullanıcı dostu uyarılar
- Günlük token limiti kontrolü ve bilgilendirme

### 🔧 İyileştirmeler
- Hata yakalama mekanizması iyileştirildi
- API limit aşımı durumunda kısmi rapor gösterimi
- Görsel analiz başarısızsa RAG atlanıyor (token tasarrufu)
- Güven puanı düşükse güvenlik denetimi atlanıyor

### 🗑️ Kaldırılanlar
- Demo modu referansları ana uygulamadan çıkarıldı
- Gereksiz test dosyaları ve görseller silindi
- Kullanılmayan dokümantasyon dosyaları (RATE_LIMIT_FIX.md, FINAL_FIX.md, vb.)
- agents_optimized.py (henüz entegre edilmemiş)
- prospektus_olusturucu.py (veritabanı zaten hazır)
- app_simple.py (kullanılmıyor)

### 📦 Proje Temizliği
- 15 gereksiz dosya silindi
- Proje yapısı sadeleştirildi
- README güncellendigereksiz referanslar kaldırıldı

---

## [2.0.0] - 2026-03-12

### ✨ Eklenenler
- 11,226 ilaç prospektüsü (49'dan artırıldı)
- 21 farklı ilaç kategorisi
- Akıllı fuzzy matching algoritması
- RAG sistemi optimizasyonu
- Güven puanı sistemi (0-10)
- Detaylı kategori dağılımı
- Performans testleri
- Kapsamlı dokümantasyon
- LICENSE dosyası
- CONTRIBUTING.md rehberi
- Profesyonel README.md

### 🔧 İyileştirmeler
- RAG arama hızı optimize edildi (~1 saniye yükleme)
- Görsel analiz doğruluğu artırıldı (8-9/10)
- UI/UX iyileştirmeleri
- Hata mesajları daha açıklayıcı
- API key yönetimi iyileştirildi

### 🐛 Düzeltmeler
- Duplicate initialize_db() çağrısı düzeltildi
- Token limit aşımı sorunu çözüldü
- Encoding hataları düzeltildi
- Gemini model adı güncellendi (gemini-2.5-flash)

### 📁 Proje Yapısı
- `docs/` klasörü eklendi (dokümantasyon)
- `scripts/` klasörü eklendi (batch dosyaları)
- `.gitignore` güncellendi
- `.gitkeep` dosyaları eklendi

### 🗑️ Kaldırılanlar
- Gereksiz test dosyaları silindi
- Geçici dokümantasyon dosyaları temizlendi
- Eski API kontrol dosyaları kaldırıldı

---

## [1.0.0] - 2026-03-10

### 🎉 İlk Sürüm
- Görsel analiz (Google Gemini Vision)
- Metin analizi (Groq Llama 3.3)
- RAG sistemi (49 prospektüs)
- Güvenlik analizi
- Rapor oluşturma (TXT)
- Streamlit UI
- Türkçe dil desteği
- Demo modu
- API key yapılandırması

### 📚 Dokümantasyon
- KURULUM.md
- HATA_COZUMLERI.md
- API_ANAHTARI_NASIL_ALINIR.md
- GEMINI_API_NASIL_ALINIR.txt

### 🚀 Özellikler
- Multi-agent sistem
- Vision Agent (görsel analiz)
- RAG Agent (prospektüs arama)
- Security Agent (güvenlik analizi)
- PDF Report Generator (TXT formatı)

---

## Versiyon Formatı

Format: [MAJOR.MINOR.PATCH]

- **MAJOR**: Uyumsuz API değişiklikleri
- **MINOR**: Geriye uyumlu yeni özellikler
- **PATCH**: Geriye uyumlu hata düzeltmeleri

---

## Gelecek Sürümler

### [2.1.0] - Planlanan
- [ ] Vector database entegrasyonu (ChromaDB)
- [ ] Gerçek prospektüs verilerini TİTCK'dan çekme
- [ ] PDF rapor desteği
- [ ] Çoklu dil desteği (İngilizce)

### [2.2.0] - Planlanan
- [ ] Barkod okuma iyileştirmesi
- [ ] İlaç geçmişi takibi
- [ ] Kullanıcı hesapları
- [ ] Favoriler sistemi

### [3.0.0] - Uzun Vadeli
- [ ] Mobil uygulama
- [ ] Offline mod
- [ ] Sesli asistan
- [ ] AR (Augmented Reality) desteği

---

**Not**: Bu proje aktif olarak geliştirilmektedir. Katkılarınızı bekliyoruz!
