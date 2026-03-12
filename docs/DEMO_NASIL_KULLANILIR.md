# 🎮 PHARMA-GUARD Demo Modu

## Demo Modu Nedir?

API anahtarı olmadan sistemi test edebileceğiniz bir versiyondur.
- Gerçek AI analizi yapmaz
- Örnek sonuçlar gösterir
- Sistem mimarisini anlamanızı sağlar

## Demo Modunu Çalıştırma

```bash
streamlit run app_demo.py
```

Tarayıcınızda otomatik olarak açılacaktır: http://localhost:8501

## Demo Modunda Neler Yapabilirsiniz?

✅ İlaç fotoğrafı yükleyebilirsiniz  
✅ Arayüzü test edebilirsiniz  
✅ Örnek rapor görebilirsiniz  
✅ Sistem akışını anlayabilirsiniz  

❌ Gerçek AI analizi yapamaz  
❌ Farklı ilaçlar için farklı sonuçlar üretemez  
❌ PDF rapor oluşturamaz  

## Gerçek Sisteme Geçiş

Demo modunu test ettikten sonra gerçek sistemi kullanmak için:

### 1. Groq API Anahtarı Alın
https://console.groq.com
- Ücretsiz hesap oluşturun
- API Keys → Create API Key
- Anahtarı kopyalayın (gsk_ ile başlar)

### 2. Anahtarı Ekleyin

**PowerShell:**
```powershell
echo GROQ_API_KEY=gsk_ANAHTARINIZ | Out-File -FilePath .env -Encoding ASCII -NoNewline
```

**Veya manuel:**
- `.env` dosyasını Notepad ile açın
- `GROQ_API_KEY=gsk_ANAHTARINIZ` yazın
- Kaydedin

### 3. Gerçek Sistemi Başlatın
```bash
streamlit run app.py
```

## Karşılaştırma

| Özellik | Demo Modu | Gerçek Sistem |
|---------|-----------|---------------|
| API Anahtarı | ❌ Gerekli değil | ✅ Gerekli |
| Görsel Analiz | ❌ Örnek sonuç | ✅ Gerçek AI |
| Farklı İlaçlar | ❌ Aynı sonuç | ✅ Farklı sonuç |
| Güvenlik Analizi | ❌ Örnek | ✅ Gerçek |
| PDF Rapor | ❌ Yok | ✅ Var |
| Maliyet | 🆓 Ücretsiz | 🆓 Ücretsiz (limit dahilinde) |

## Sorun Giderme

### Demo modu açılmıyor
```bash
pip install streamlit pillow
streamlit run app_demo.py
```

### Gerçek sisteme geçemiyorum
1. `YENİ_API_ANAHTARI_EKLE.txt` dosyasını okuyun
2. `python test_groq_api.py` ile test edin
3. Başarılı olursa `streamlit run app.py`

## Destek

- Demo ile ilgili sorular: Proje README.md
- API anahtarı sorunları: `API_KONTROL.md`
- Genel hatalar: `HATA_COZUMLERI.md`

---

**İyi testler! 🚀**
