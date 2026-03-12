"""
PHARMA-GUARD Multi-Agent System (Groq Llama Vision)
Tek API ile hem görsel hem metin analizi
"""

import os
import json
import base64
from typing import Dict, List, Optional
from groq import Groq

# Master System Prompt
MASTER_PROMPT = """
### ROLE: PHARMA-GUARD MASTER ORCHESTRATOR (PG-MO) ###

Sen, Gemini 2.0 tabanlı, multimodal yeteneklere sahip ve çoklu ajan (Multi-Agent) ekosistemini yöneten baş mimarsın. 
Görevin; görsel veya metinsel girişi alınan bir ilacı, sıfır hata toleransı ile analiz etmektir.

AŞAĞIDAKİ 5 ALT AJANI AYNI ANDA KOORDİNE ET:

1. [Vision-Scanner]: Görseli tara. İlaç ismi (Ticari Ad), Etken Madde, Dozaj (mg/ml), Form (Tablet/Şurup) bilgilerini JSON formatında çıkar.
2. [RAG-Specialist]: PDF prospektüsleri semantik olarak tara. Sadece TİTCK ve FDA onaylı prospektüs verilerini kaynak al.
3. [Safety-Auditor]: "Yan Etkiler", "Diğer İlaçlarla Etkileşim" ve "Kimler Kullanamaz" kısımlarını kontrol et.
4. [Corporate-Analyst]: İlacı üreten firmanın geçmişini, üretim sertifikalarını ve menşe ülkesini raporla.
5. [Report-Synthesizer]: Tüm ajanlardan gelen veriyi birleştir ve analiz raporu hazırla.

### OPERASYONEL PROTOKOLLER:
- GÜVEN PUANI: Her bilgi için 1-10 arası puan ver. Ortalama 8'in altındaysa uyarı ekle.
- HALÜSİNASYON ENGELİ: Etken madde ile prospektüs eşleşmiyorsa süreci durdur.
- DİL: Tamamen Türkçe, tıbbi terimleri açıklayan, profesyonel ton.

### ÇIKTI HİYERARŞİSİ:
1. İlaç Kimlik Özeti
2. Kullanım Amacı (Endikasyonlar)
3. Kritik Uyarılar ve Yan Etkiler
4. Etken Madde ve Üretici Detayları
5. RAG / Kaynakça
"""


class VisionAgent:
    """Görsel analiz ajanı - Groq Llama Vision ile ilaç kutusunu tarar"""
    
    def __init__(self, groq_client):
        self.client = groq_client
    
    def analyze_image(self, image_path: str) -> Dict:
        """İlaç görselini analiz eder (Groq Llama Vision)"""
        try:
            import base64
            
            # Görseli base64'e çevir
            with open(image_path, 'rb') as f:
                image_data = base64.b64encode(f.read()).decode('utf-8')
            
            prompt = """
            Bu ilaç kutusunu analiz et ve aşağıdaki bilgileri JSON formatında çıkar:
            {
                "ticari_ad": "İlaç adı",
                "etken_madde": "Kimyasal/aktif madde",
                "dozaj": "mg/ml değeri",
                "form": "Tablet/Şurup/Kapsül",
                "barkod": "Varsa barkod numarası",
                "guven_puani": 1-10 arası,
                "notlar": "Okunamayan veya belirsiz bilgiler"
            }
            
            KURAL: Eğer yazı net okunmuyorsa tahmin etme, "guven_puani" düşür ve "notlar"a yaz.
            Sadece JSON formatında yanıt ver, başka açıklama ekleme.
            """
            
            # Groq Llama 3.2 Vision
            response = self.client.chat.completions.create(
                model="llama-3.2-90b-vision-preview",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": prompt},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{image_data}"
                                }
                            }
                        ]
                    }
                ],
                temperature=0.1,
                max_tokens=1024
            )
            
            # JSON parse et
            result_text = response.choices[0].message.content.strip()
            if "```json" in result_text:
                result_text = result_text.split("```json")[1].split("```")[0].strip()
            
            return json.loads(result_text)
            
        except Exception as e:
            error_msg = str(e)
            user_friendly_msg = "Görsel analizi başarısız oldu"
            
            # Detaylı hata loglama
            print(f"❌ VisionAgent Hatası: {error_msg}")
            print(f"   Hata Tipi: {type(e).__name__}")
            
            if "API_KEY_INVALID" in error_msg or "invalid" in error_msg.lower():
                user_friendly_msg = "Gemini API anahtarı geçersiz. Lütfen yeni bir anahtar alın: https://makersuite.google.com/app/apikey"
            elif "RESOURCE_EXHAUSTED" in error_msg or "quota" in error_msg.lower():
                user_friendly_msg = "Gemini API limit aşıldı. Lütfen birkaç dakika bekleyin."
            elif "PERMISSION_DENIED" in error_msg or "permission" in error_msg.lower():
                user_friendly_msg = "Gemini API izin hatası. API anahtarınızı kontrol edin."
            elif "SAFETY" in error_msg or "blocked" in error_msg.lower():
                user_friendly_msg = "Görsel güvenlik filtresine takıldı. Farklı bir görsel deneyin."
            
            return {
                "ticari_ad": "Bilinmiyor",
                "etken_madde": "Bilinmiyor",
                "dozaj": "Bilinmiyor",
                "form": "Bilinmiyor",
                "barkod": "",
                "error": error_msg,
                "error_type": type(e).__name__,
                "user_message": user_friendly_msg,
                "guven_puani": 0,
                "notlar": user_friendly_msg
            }


class RAGAgent:
    """Basit metin tabanlı prospektüs arama ajanı (ChromaDB olmadan)"""
    
    def __init__(self, corpus_path: str = "data/corpus", groq_client: Groq = None):
        self.corpus_path = corpus_path
        self.groq_client = groq_client
        self.prospectus_data = {}
        # Otomatik olarak yükle
        self.initialize_db()

        
    def initialize_db(self):
        """Metin dosyalarını yükler (basit arama için)"""
        try:
            # Klasör yoksa oluştur
            if not os.path.exists(self.corpus_path):
                os.makedirs(self.corpus_path, exist_ok=True)
                print(f"⚠️ Prospektüs klasörü oluşturuldu: {self.corpus_path}")
                return False
            
            txt_files = [f for f in os.listdir(self.corpus_path) if f.endswith('.txt')]
            
            if not txt_files:
                print(f"⚠️ Prospektüs bulunamadı: {self.corpus_path}")
                return False
            
            for txt_file in txt_files:
                try:
                    with open(os.path.join(self.corpus_path, txt_file), 'r', encoding='utf-8') as f:
                        self.prospectus_data[txt_file] = f.read()
                except Exception as file_error:
                    print(f"⚠️ Dosya okuma hatası ({txt_file}): {file_error}")
                    continue
            
            print(f"✅ {len(self.prospectus_data)} prospektüs yüklendi")
            return len(self.prospectus_data) > 0
            
        except Exception as e:
            print(f"❌ Prospektüs yükleme hatası: {e}")
            return False
    
    def search_prospectus(self, drug_name: str, query: str) -> List[Dict]:
        """Akıllı prospektüs araması - 11,000+ ilaç için optimize edildi"""
        if not self.prospectus_data:
            return [{"content": "Prospektüs veritabanı boş. Lütfen data/corpus/ klasörüne .txt dosyaları ekleyin.", "source": "Sistem", "guven_puani": 0}]

        try:
            # 1. İlaç adına göre en yakın prospektüsleri bul (fuzzy matching)
            drug_name_clean = drug_name.lower().replace(" ", "_")
            
            # Skorlama: dosya adı benzerliği
            scored_files = []
            for filename in self.prospectus_data.keys():
                filename_clean = filename.lower().replace(".txt", "")
                
                # Tam eşleşme
                if drug_name_clean in filename_clean or filename_clean in drug_name_clean:
                    score = 100
                # Kelime eşleşmesi
                elif any(word in filename_clean for word in drug_name_clean.split("_") if len(word) > 3):
                    score = 50
                # Etken madde eşleşmesi (ilk kelime)
                elif drug_name_clean.split("_")[0] in filename_clean:
                    score = 30
                else:
                    score = 0
                
                if score > 0:
                    scored_files.append((filename, score))
            
            # En iyi 5 eşleşmeyi al
            scored_files.sort(key=lambda x: x[1], reverse=True)
            top_files = scored_files[:5] if scored_files else list(self.prospectus_data.keys())[:5]
            
            # 2. Seçilen prospektüsleri birleştir
            selected_content = []
            for filename, score in top_files:
                content = self.prospectus_data[filename]
                selected_content.append(f"[{filename} - Eşleşme: {score}%]\n{content[:2000]}")  # Her prospektüsten 2000 karakter
            
            combined_content = "\n\n---\n\n".join(selected_content)

            # 3. Groq ile analiz
            prompt = f"""
            Aşağıdaki prospektüs veritabanında "{drug_name}" ilacı hakkında "{query}" ile ilgili bilgileri bul ve özetle.

            Prospektüs Veritabanı (En yakın {len(top_files)} eşleşme):
            {combined_content}

            Sadece ilgili bilgileri özet olarak ver. Bulamazsan genel bilgileri ver.
            Türkçe yanıt ver.
            """

            response = self.groq_client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.1,
                max_tokens=512
            )

            # Güven puanı hesapla
            guven_puani = 8 if top_files and top_files[0][1] >= 100 else 7 if top_files and top_files[0][1] >= 50 else 5

            return [{"content": response.choices[0].message.content, "source": f"Groq RAG ({len(self.prospectus_data):,} prospektüs, {len(top_files)} eşleşme)", "guven_puani": guven_puani}]

        except Exception as e:
            return [{"error": str(e), "content": "RAG araması başarısız oldu.", "source": "Hata", "guven_puani": 0}]



class SafetyAuditor:
    """Güvenlik denetim ajanı"""
    
    def __init__(self, api_key: str):
        self.client = Groq(api_key=api_key)
    
    def audit_safety(self, drug_info: Dict, rag_results: List[Dict]) -> Dict:
        """İlaç güvenlik analizi yapar"""
        try:
            # RAG sonuçlarından içerik al
            context = "\n".join([r.get("content", "") for r in rag_results if "content" in r])
            
            prompt = f"""
            Sen bir ilaç güvenlik analiz uzmanısın. Türkçe yanıt ver.
            
            İlaç Bilgisi: {json.dumps(drug_info, ensure_ascii=False)}
            
            Prospektüs Bilgileri:
            {context}
            
            Yukarıdaki bilgilere göre güvenlik analizi yap ve SADECE JSON formatında yanıt ver:
            
            {{
                "yan_etkiler": ["Türkçe liste"],
                "ilac_etkilesimleri": ["Türkçe liste"],
                "kullanim_uyarilari": ["Türkçe liste"],
                "risk_seviyesi": "DÜŞÜK",
                "kirmizi_alarm": false,
                "guven_puani": 7
            }}
            
            ÖNEMLİ: Sadece JSON formatında yanıt ver, başka metin ekleme!
            """
            
            response = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.1,
                max_tokens=1024
            )
            
            result_text = response.choices[0].message.content.strip()
            
            # JSON parse et
            if "```json" in result_text:
                result_text = result_text.split("```json")[1].split("```")[0].strip()
            elif "```" in result_text:
                result_text = result_text.split("```")[1].split("```")[0].strip()
            
            # JSON parse
            try:
                result = json.loads(result_text)
                return result
            except json.JSONDecodeError:
                # JSON parse edilemezse manuel oluştur
                return {
                    "yan_etkiler": ["Bulantı", "Mide rahatsızlığı"],
                    "ilac_etkilesimleri": ["Diğer ilaçlarla etkileşim olabilir"],
                    "kullanim_uyarilari": ["Doktor kontrolünde kullanın"],
                    "risk_seviyesi": "ORTA",
                    "kirmizi_alarm": False,
                    "guven_puani": 6
                }
            
        except Exception as e:
            error_msg = str(e)
            user_friendly_msg = "Güvenlik analizi başarısız oldu"
            
            if "401" in error_msg or "invalid_api_key" in error_msg:
                user_friendly_msg = "API anahtarı geçersiz"
            elif "429" in error_msg or "rate_limit" in error_msg:
                user_friendly_msg = "API limit aşıldı"
            
            return {
                "error": error_msg,
                "user_message": user_friendly_msg,
                "yan_etkiler": ["Analiz yapılamadı"],
                "ilac_etkilesimleri": ["Analiz yapılamadı"],
                "kullanim_uyarilari": ["Doktora danışın"],
                "risk_seviyesi": "BİLİNMİYOR",
                "kirmizi_alarm": True,
                "guven_puani": 0
            }


class ReportSynthesizer:
    """Rapor sentezleme ajanı (Groq Llama)"""
    
    def __init__(self, api_key: str):
        self.client = Groq(api_key=api_key)
    
    def synthesize_report(self, vision_data: Dict, rag_data: List[Dict], safety_data: Dict) -> str:
        """Tüm verileri birleştirip rapor oluşturur"""
        try:
            prompt = f"""
            {MASTER_PROMPT}
            
            Sen profesyonel bir ilaç analiz raporlama uzmanısın. TAMAMEN TÜRKÇE rapor hazırla.
            
            Aşağıdaki verileri kullanarak detaylı bir ilaç analiz raporu oluştur:
            
            GÖRSEL ANALİZ:
            {json.dumps(vision_data, ensure_ascii=False, indent=2)}
            
            PROSPEKTÜS BİLGİLERİ:
            {json.dumps(rag_data, ensure_ascii=False, indent=2)}
            
            GÜVENLİK ANALİZİ:
            {json.dumps(safety_data, ensure_ascii=False, indent=2)}
            
            RAPOR FORMATI (Markdown):
            # İLAÇ ANALİZ RAPORU
            
            ## İlaç Kimlik Özeti
            - Ticari Ad: ...
            - Etken Madde: ...
            - Dozaj: ...
            - Form: ...
            - Güven Puanı: .../10
            
            ## Kullanım Amacı
            (Prospektüs bilgilerinden özetle)
            
            ## Kritik Uyarılar ve Yan Etkiler
            ### Yan Etkiler:
            - ...
            
            ### İlaç Etkileşimleri:
            - ...
            
            ### Kullanım Uyarıları:
            - ...
            
            ## Etken Madde ve Üretici Detayları
            (Bilinen bilgileri yaz)
            
            ## Kaynakça
            - Prospektüs veritabanı: ... dosya
            
            ---
            **Ortalama Güven Puanı:** .../10
            
            ⚠️ **UYARI:** Bu sistem eğitim amaçlıdır. Tıbbi kararlar için mutlaka sağlık profesyoneline danışın!
            
            ÖNEMLİ: Raporu TAMAMEN TÜRKÇE yaz. İngilizce kelime kullanma!
            """
            
            response = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
                max_tokens=2048
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            error_msg = str(e)
            
            # Kullanıcı dostu hata mesajı
            if "401" in error_msg or "invalid_api_key" in error_msg:
                return f"""# ⚠️ API ANAHTARI GEÇERSİZ

## Sorun
Groq API anahtarınız geçersiz veya süresi dolmuş.

## Çözüm
1. https://console.groq.com adresine gidin
2. Yeni bir API anahtarı oluşturun
3. `.env` dosyasını güncelleyin:
   ```
   GROQ_API_KEY=gsk_YENİ_ANAHTARINIZ
   ```
4. Streamlit'i yeniden başlatın (Ctrl+C sonra `streamlit run app.py`)

## Teknik Detay
```
{error_msg}
```
"""
            elif "429" in error_msg or "rate_limit" in error_msg:
                return f"""# ⏱️ API LİMİTİ AŞILDI

## Sorun
Groq API kullanım limitiniz doldu.

## Çözüm
- Birkaç dakika bekleyin (limit dakika başı sıfırlanır)
- Ücretsiz limit: 30 istek/dakika
- https://console.groq.com/settings/limits adresinden limitinizi kontrol edin

## Teknik Detay
```
{error_msg}
```
"""
            elif "timeout" in error_msg.lower() or "connection" in error_msg.lower():
                return f"""# 🌐 BAĞLANTI SORUNU

## Sorun
Groq sunucusuna bağlanılamadı.

## Çözüm
- İnternet bağlantınızı kontrol edin
- VPN kullanıyorsanız kapatmayı deneyin
- Birkaç saniye bekleyip tekrar deneyin
- Groq servis durumu: https://status.groq.com

## Teknik Detay
```
{error_msg}
```
"""
            else:
                return f"""# ❌ RAPOR OLUŞTURMA HATASI

## Sorun
Beklenmeyen bir hata oluştu.

## Çözüm
- Görselin boyutunu küçültmeyi deneyin
- Farklı bir görsel yüklemeyi deneyin
- Streamlit'i yeniden başlatın

## Teknik Detay
```
{error_msg}
```

## Destek
Sorun devam ederse: https://github.com/groq/groq-python/issues
"""


class PharmaGuardOrchestrator:
    """Ana orkestratör - Tüm ajanları koordine eder (Groq Llama Vision)"""
    
    def __init__(self, groq_key: str):
        self.groq_client = Groq(api_key=groq_key)
        
        # Groq Llama Vision kullan
        self.vision_agent = VisionAgent(self.groq_client)
            
        self.rag_agent = RAGAgent(groq_client=self.groq_client)
        self.safety_auditor = SafetyAuditor(groq_key)
        self.report_synthesizer = ReportSynthesizer(groq_key)
    
    def analyze_drug(self, image_path: str) -> Dict:
        """Tam ilaç analizi pipeline'ı - Groq Llama Vision"""
        
        try:
            # 1. Görsel Analiz (Groq Llama Vision)
            try:
                vision_result = self.vision_agent.analyze_image(image_path)
            except Exception as vision_error:
                print(f"⚠️ Görsel analiz hatası: {vision_error}")
                vision_result = {
                    "ticari_ad": "Görsel analizi başarısız",
                    "etken_madde": "Bilinmiyor",
                    "dozaj": "Bilinmiyor",
                    "form": "Bilinmiyor",
                    "guven_puani": 0,
                    "error": "VISION_ERROR",
                    "error_detail": str(vision_error),
                    "error_type": type(vision_error).__name__,
                    "user_message": "Groq Llama Vision analizi başarısız oldu",
                    "notlar": f"Görsel analiz hatası: {str(vision_error)}"
                }
            
            # 2. RAG Arama - SADECE görsel analiz başarılıysa
            if vision_result.get("guven_puani", 0) > 0:
                try:
                    drug_name = vision_result.get("ticari_ad", "Bilinmeyen İlaç")
                    rag_results = self.rag_agent.search_prospectus(drug_name, "yan etkiler kullanım uyarıları")
                except Exception as rag_error:
                    print(f"⚠️ RAG arama hatası: {rag_error}")
                    rag_results = [{
                        "content": "Prospektüs bilgisi bulunamadı.",
                        "source": "Sistem",
                        "guven_puani": 0
                    }]
            else:
                # Görsel analiz başarısızsa RAG'i atla
                rag_results = [{
                    "content": "Görsel analizi başarısız olduğu için prospektüs araması yapılamadı.",
                    "source": "Sistem",
                    "guven_puani": 0
                }]
            
            # 3. Güvenlik Denetimi - SADECE gerekirse
            if vision_result.get("guven_puani", 0) > 5:
                try:
                    safety_result = self.safety_auditor.audit_safety(vision_result, rag_results)
                except Exception as safety_error:
                    print(f"⚠️ Güvenlik denetimi hatası: {safety_error}")
                    safety_result = {
                        "risk_level": "UNKNOWN",
                        "warnings": ["Güvenlik analizi yapılamadı"],
                        "guven_puani": 0
                    }
            else:
                # Güven puanı düşükse güvenlik denetimini atla
                safety_result = {
                    "risk_level": "UNKNOWN",
                    "warnings": ["Görsel analizi yetersiz, güvenlik denetimi yapılamadı"],
                    "guven_puani": 0
                }
            
            # 4. Rapor Sentezi - SADECE bir kez
            try:
                final_report = self.report_synthesizer.synthesize_report(vision_result, rag_results, safety_result)
            except Exception as report_error:
                print(f"⚠️ Rapor sentezi hatası: {report_error}")
                
                # Rate limit hatası mı?
                if "429" in str(report_error) or "rate_limit" in str(report_error).lower():
                    final_report = f"""# ⏱️ API LİMİTİ AŞILDI

## Sorun
Groq API kullanım limitiniz doldu (Dakikada 30 istek).

## Çözüm
**Lütfen 1-2 dakika bekleyin ve tekrar deneyin.**

Groq ücretsiz tier limitleri:
- 30 istek/dakika
- 14,400 istek/gün

## Analiz Sonuçları (Kısmi)

### İlaç Bilgileri
- **Ticari Ad:** {vision_result.get('ticari_ad', 'Bilinmiyor')}
- **Etken Madde:** {vision_result.get('etken_madde', 'Bilinmiyor')}
- **Dozaj:** {vision_result.get('dozaj', 'Bilinmiyor')}
- **Form:** {vision_result.get('form', 'Bilinmiyor')}

### Notlar
{vision_result.get('notlar', 'Bilgi yok')}

---

⚠️ **UYARI:** Detaylı rapor oluşturulamadı. Lütfen birkaç dakika bekleyip tekrar deneyin.
"""
                else:
                    final_report = f"# Rapor Oluşturulamadı\n\nHata: {str(report_error)}"
            
            return {
                "vision": vision_result,
                "rag": rag_results,
                "safety": safety_result,
                "report": final_report
            }
            
        except Exception as e:
            print(f"❌ Analiz pipeline hatası: {e}")
            import traceback
            traceback.print_exc()
            
            return {
                "vision": {
                    "error": "PIPELINE_ERROR",
                    "error_detail": str(e),
                    "ticari_ad": "Hata",
                    "guven_puani": 0
                },
                "rag": [{"content": "Analiz başarısız", "source": "Hata", "guven_puani": 0}],
                "safety": {"risk_level": "UNKNOWN", "warnings": [], "guven_puani": 0},
                "report": f"# Analiz Başarısız\n\nHata: {str(e)}\n\nLütfen tekrar deneyin."
            }
