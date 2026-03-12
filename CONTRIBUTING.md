# 🤝 Katkıda Bulunma Rehberi

PHARMA-GUARD AI projesine katkıda bulunmak istediğiniz için teşekkür ederiz!

## 📋 Katkı Türleri

### 🐛 Hata Bildirimi
- GitHub Issues kullanarak hata bildirin
- Hatayı detaylı açıklayın
- Adım adım tekrarlama yöntemi ekleyin
- Sistem bilgilerinizi paylaşın

### ✨ Özellik Önerisi
- Yeni özellik fikirlerinizi paylaşın
- Kullanım senaryoları ekleyin
- Mümkünse mockup/tasarım ekleyin

### 📝 Dokümantasyon
- Dokümantasyon hatalarını düzeltin
- Yeni örnekler ekleyin
- Çeviri katkısı yapın

### 💻 Kod Katkısı
- Bug fix
- Yeni özellikler
- Performans iyileştirmeleri
- Test coverage artırma

## 🚀 Başlangıç

### 1. Repository'yi Fork Edin
```bash
# GitHub'da Fork butonuna tıklayın
```

### 2. Clone Edin
```bash
git clone https://github.com/YOUR_USERNAME/pharma-guard-ai.git
cd pharma-guard-ai
```

### 3. Branch Oluşturun
```bash
git checkout -b feature/amazing-feature
```

### 4. Geliştirme Ortamını Kurun
```bash
pip install -r requirements.txt
```

## 📝 Kod Standartları

### Python Stil Rehberi
- PEP 8 standartlarına uyun
- Anlamlı değişken isimleri kullanın
- Fonksiyonlara docstring ekleyin
- Type hints kullanın (mümkünse)

### Örnek:
```python
def analyze_drug(image_path: str, drug_name: str) -> Dict[str, Any]:
    """
    İlaç görselini analiz eder.
    
    Args:
        image_path: Görsel dosya yolu
        drug_name: İlaç adı
        
    Returns:
        Analiz sonuçları dictionary
    """
    # Kod buraya
    pass
```

### Commit Mesajları
```
feat: Yeni özellik ekle
fix: Hata düzelt
docs: Dokümantasyon güncelle
style: Kod formatı düzenle
refactor: Kod yeniden yapılandır
test: Test ekle/güncelle
chore: Bakım işleri
```

## 🧪 Test

### Testleri Çalıştırın
```bash
python -m pytest tests/
```

### Yeni Test Ekleyin
```python
def test_drug_analysis():
    """İlaç analizi testleri"""
    # Test kodu
    pass
```

## 📤 Pull Request Süreci

### 1. Değişikliklerinizi Commit Edin
```bash
git add .
git commit -m "feat: Yeni özellik ekle"
```

### 2. Push Edin
```bash
git push origin feature/amazing-feature
```

### 3. Pull Request Açın
- GitHub'da Pull Request açın
- Değişikliklerinizi detaylı açıklayın
- İlgili issue'ları referans gösterin
- Screenshot ekleyin (UI değişiklikleri için)

### 4. Code Review
- Geri bildirimlere yanıt verin
- Gerekli değişiklikleri yapın
- Merge onayını bekleyin

## 🎯 Öncelikli Alanlar

### Yüksek Öncelik
- [ ] Gerçek prospektüs verilerini TİTCK'dan çekme
- [ ] Vector database entegrasyonu
- [ ] PDF rapor desteği
- [ ] Test coverage artırma

### Orta Öncelik
- [ ] Çoklu dil desteği
- [ ] Barkod okuma iyileştirmesi
- [ ] İlaç geçmişi takibi
- [ ] Performans optimizasyonları

### Düşük Öncelik
- [ ] UI/UX iyileştirmeleri
- [ ] Dokümantasyon genişletme
- [ ] Örnek kullanım senaryoları

## 📞 İletişim

Sorularınız için:
- GitHub Issues
- Email: support@pharma-guard-ai.com

## 🙏 Teşekkürler

Katkılarınız için teşekkür ederiz! Her katkı, projeyi daha iyi hale getirir.
