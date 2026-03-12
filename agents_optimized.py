"""
PHARMA-GUARD AI Agents - ULTRA OPTİMİZE EDİLMİŞ
Tek Groq İsteği ile Tüm Analiz
"""

import os
import json
from typing import Dict, List
from groq import Groq
import google.generativeai as genai

# Gemini yapılandırması
def configure_gemini(api_key: str):
    """Gemini'yi yapılandır"""
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-2.0-flash-exp')


class OptimizedPharmaGuard:
    """Optimize edilmiş tek-istek analiz sistemi"""
    
    def __init__(self, groq_key: str, gemini_key: str = None):
        self.groq_client = Groq(api_key=groq_key)
        self.gemini_model = configure_gemini(gemini_key) if gemini_key else None
    
    def analyze_drug(self, image_path: str) -> Dict:
        """TEK Groq isteği ile tam analiz"""
        
        # 1. Görsel Analiz (Gemini - Groq'a sayılmaz)
        if self.gemini_model:
            try:
                with open(image_path, 'rb') as f:
                    image_data = f.read()
                
                response = self.gemini_model.generate_content([
                    "Bu ilaç kutusunu analiz et. Sadece JSON formatında yanıt ver: {\"ticari_ad\": \"...\", \"etken_madde\": \"...\", \"dozaj\": \"...\", \"form\": \"...\"}",
                    {"mime_type": "image/jpeg", "data": image_data}
                ])
                
                result_text = response.text.strip()
                if "```json" in result_text:
                    result_text = result_text.split("```json")[1].split("```")[0].strip()
                
                vision_data = json.loads(result_text)
                vision_data["guven_puani"] = 8
                
            except Exception as e:
                vision_data = {
                    "ticari_ad": "Bilinmiyor",
                    "etken_madde": "Bilinmiyor",
                    "dozaj": "Bilinmiyor",
                    "form": "Bilinmiyor",
                    "guven_puani": 0,
                    "error": str(e)
                }
        else:
            vision_data = {
                "ticari_ad": "Demo İlaç",
                "etken_madde": "Bilinmiyor",
                "dozaj": "500mg",
                "form": "Tablet",
                "guven_puani": 3
            }
        
        # 2. Prospektüs Yükleme (Lokal - Groq'a sayılmaz)
        prospectus_content = self._load_prospectus(vision_data.get("ticari_ad", ""))
        
        # 3. TEK GROQ İSTEĞİ - Tüm analiz birlikte
        try:
            mega_prompt = f"""
Sen bir ilaç analiz uzmanısın. Aşağıdaki bilgileri kullanarak KAPSAMLI bir analiz raporu oluştur.

İLAÇ BİLGİLERİ:
- Ticari Ad: {vision_data.get('ticari_ad', 'Bilinmiyor')}
- Etken Madde: {vision_data.get('etken_madde', 'Bilinmiyor')}
- Dozaj: {vision_data.get('dozaj', 'Bilinmiyor')}
- Form: {vision_data.get('form', 'Bilinmiyor')}

PROSPEKTÜS BİLGİLERİ:
{prospectus_content[:3000]}

GÖREV:
1. İlaç kimlik özetini yaz
2. Kullanım amacını açıkla
3. Yan etkileri listele
4. İlaç etkileşimlerini belirt
5. Kullanım uyarılarını yaz
6. Güven puanı ver (0-10)

RAPOR FORMATI (Markdown, TÜRKÇE):

# İLAÇ ANALİZ RAPORU

## İlaç Kimlik Özeti
- **Ticari Ad:** {vision_data.get('ticari_ad', 'Bilinmiyor')}
- **Etken Madde:** {vision_data.get('etken_madde', 'Bilinmiyor')}
- **Dozaj:** {vision_data.get('dozaj', 'Bilinmiyor')}
- **Form:** {vision_data.get('form', 'Bilinmiyor')}
- **Güven Puanı:** .../10

## Kullanım Amacı
(Prospektüs bilgilerinden özetle, yoksa genel bilgi ver)

## Kritik Uyarılar ve Yan Etkiler

### Yan Etkiler:
- ...
- ...

### İlaç Etkileşimleri:
- ...
- ...

### Kullanım Uyarıları:
- ...
- ...

## Etken Madde Detayları
(Bilinen bilgileri yaz)

---

⚠️ **UYARI:** Bu sistem eğitim amaçlıdır. Tıbbi kararlar için mutlaka sağlık profesyoneline danışın!

ÖNEMLİ: TAMAMEN TÜRKÇE yaz!
"""
            
            # TEK GROQ İSTEĞİ
            response = self.groq_client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": mega_prompt}],
                temperature=0.3,
                max_tokens=2048
            )
            
            report = response.choices[0].message.content
            
            # Güven puanını rapordan çıkar
            confidence = vision_data.get("guven_puani", 5)
            
            return {
                "vision": vision_data,
                "report": report,
                "confidence": confidence,
                "groq_requests": 1  # Sadece 1 istek!
            }
            
        except Exception as e:
            error_msg = str(e)
            
            if "429" in error_msg:
                return {
                    "vision": vision_data,
                    "report": f"""# ⏱️ API LİMİTİ AŞILDI

## Sorun
Groq API dakikalık limit aşıldı (30 istek/dakika).

## Çözüm
**Lütfen 60 saniye bekleyin ve tekrar deneyin.**

## Kısmi Bilgiler
- **İlaç:** {vision_data.get('ticari_ad', 'Bilinmiyor')}
- **Etken Madde:** {vision_data.get('etken_madde', 'Bilinmiyor')}
- **Dozaj:** {vision_data.get('dozaj', 'Bilinmiyor')}

---

⚠️ Detaylı analiz için lütfen 1 dakika bekleyin.
""",
                    "confidence": 0,
                    "groq_requests": 0,
                    "error": "RATE_LIMIT"
                }
            else:
                return {
                    "vision": vision_data,
                    "report": f"# Analiz Hatası\n\n{error_msg}",
                    "confidence": 0,
                    "groq_requests": 0,
                    "error": str(e)
                }
    
    def _load_prospectus(self, drug_name: str) -> str:
        """Prospektüs dosyalarını yükle (Lokal - API'ye sayılmaz)"""
        try:
            corpus_path = "data/corpus"
            if not os.path.exists(corpus_path):
                return "Prospektüs bilgisi bulunamadı."
            
            txt_files = [f for f in os.listdir(corpus_path) if f.endswith('.txt')]
            
            if not txt_files:
                return "Prospektüs bilgisi bulunamadı."
            
            # İlaç adına göre en yakın dosyayı bul
            drug_name_clean = drug_name.lower().replace(" ", "_")
            
            best_match = None
            for filename in txt_files:
                if drug_name_clean in filename.lower():
                    best_match = filename
                    break
            
            # Eşleşme yoksa ilk 3 dosyayı al
            if not best_match:
                best_match = txt_files[0]
            
            # Dosyayı oku
            with open(os.path.join(corpus_path, best_match), 'r', encoding='utf-8') as f:
                content = f.read()
            
            return f"[{best_match}]\n{content[:2000]}"
            
        except Exception as e:
            return f"Prospektüs yükleme hatası: {str(e)}"
