"""
PHARMA-GUARD AI - Streamlit Arayüzü
Yapay Zeka Destekli Akıllı İlaç Denetçisi
v2.2 - Tam Hata Yakalama
"""

import streamlit as st
import os
import traceback
from dotenv import load_dotenv

# Sayfa yapılandırması
st.set_page_config(
    page_title="💊 PHARMA-GUARD AI",
    page_icon="💊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)


def load_api_keys():
    """API anahtarlarını yükler"""
    groq_key = None
    
    try:
        # 1. Streamlit secrets
        if hasattr(st, 'secrets'):
            groq_key = st.secrets.get('GROQ_API_KEY')
    except:
        pass
    
    # 2. Environment
    if not groq_key:
        load_dotenv()
        groq_key = os.getenv("GROQ_API_KEY")
    
    return groq_key


def main():
    """Ana uygulama"""
    
    # Başlık
    st.markdown('<h1 class="main-header">💊 PHARMA-GUARD AI</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #666;">Yapay Zeka Destekli Akıllı İlaç Denetçisi</p>', unsafe_allow_html=True)
    
    # API anahtarlarını yükle
    groq_key = load_api_keys()
    
    # Sidebar
    with st.sidebar:
        st.title("💊 Sistem Bilgileri")
        
        if groq_key:
            st.success("✅ Groq API: Aktif")
            st.info("🔍 Groq Llama Vision kullanılıyor")
        else:
            st.error("❌ Groq API: Yok")
        
        st.divider()
        st.info("""
        **Aktif Ajanlar:**
        - � Manuel Giriş
        - 📚 RAG Specialist (11,226 ilaç)
        - ⚠️ Safety Auditor
        - 📊 Report Synthesizer
        
        **Not:** Vision modelleri deprecated
        """)
    
    # API key kontrolü
    if not groq_key:
        st.error("⚠️ GROQ_API_KEY bulunamadı!")
        st.info("""
        **Streamlit Cloud için:**
        
        1. Sağ üstteki ⚙️ Settings → Secrets
        2. Şunu ekleyin:
        
        ```
        GROQ_API_KEY = "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"
        ```
        
        3. Save → App yeniden başlayacak
        """)
        st.stop()
    
    # Ana içerik
    st.subheader("📸 İlaç Analizi")
    
    st.info("""
    ℹ️ **Önemli:** Groq vision modelleri kullanımdan kaldırıldı. 
    Lütfen ilaç adını manuel olarak girin.
    """)
    
    # Manuel ilaç adı girişi
    manual_drug_name = st.text_input(
        "İlaç Adı",
        placeholder="Örn: Parol, Aspirin, Majezik",
        help="İlaç kutusunda yazan ticari adı girin"
    )
    
    uploaded_file = st.file_uploader(
        "İlaç kutusunun fotoğrafını yükleyin (opsiyonel)",
        type=["jpg", "jpeg", "png"],
        help="Referans için görsel yükleyebilirsiniz"
    )
    
    if manual_drug_name or uploaded_file:
        col1, col2 = st.columns([1, 1])
        
        with col1:
            if uploaded_file:
                st.image(uploaded_file, caption="Yüklenen Görsel", use_container_width=True)
            else:
                st.info("📝 Manuel giriş modu")
        
        with col2:
            if st.button("🔬 Analizi Başlat", type="primary", use_container_width=True, disabled=not manual_drug_name):
                
                if not manual_drug_name:
                    st.error("❌ Lütfen ilaç adını girin!")
                    return
                
                # Progress container
                progress_container = st.container()
                
                with progress_container:
                    try:
                        # Import burada (lazy loading)
                        st.info("📦 Modüller yükleniyor...")
                        from agents import PharmaGuardOrchestrator
                        from utils import validate_image, resize_image, PDFReportGenerator, calculate_confidence_score, create_data_directories
                        st.success("✅ Modüller yüklendi")
                        
                        # Klasörler
                        st.info("📁 Klasörler hazırlanıyor...")
                        create_data_directories()
                        st.success("✅ Klasörler hazır")
                        
                        # Dosyayı kaydet (varsa)
                        if uploaded_file:
                            st.info("💾 Görsel kaydediliyor...")
                            temp_path = os.path.join("uploads", uploaded_file.name)
                            with open(temp_path, "wb") as f:
                                f.write(uploaded_file.getbuffer())
                            st.success(f"✅ Kaydedildi: {temp_path}")
                            
                            # Doğrula
                            st.info("🔍 Görsel doğrulanıyor...")
                            if not validate_image(temp_path):
                                st.error("❌ Geçersiz görsel!")
                                return
                            st.success("✅ Görsel geçerli")
                            
                            # Boyutlandır
                            st.info("📐 Boyutlandırılıyor...")
                            resized_path = resize_image(temp_path)
                            st.success("✅ Boyutlandırıldı")
                        else:
                            # Görsel yoksa dummy path
                            resized_path = "dummy.jpg"
                        
                        # AI Sistemi
                        st.info("🤖 AI sistemi başlatılıyor...")
                        orchestrator = PharmaGuardOrchestrator(groq_key)
                        st.success("✅ AI sistemi hazır")
                        
                        # Analiz (manuel ilaç adı ile)
                        st.info(f"🔬 '{manual_drug_name}' analiz ediliyor... (30-60 saniye)")
                        results = orchestrator.analyze_drug(resized_path, manual_drug_name)
                        st.success("✅ Analiz tamamlandı!")
                        
                        # Temizle progress
                        progress_container.empty()
                        
                        # Hata kontrolü
                        vision_data = results.get("vision", {})
                        if "error" in vision_data:
                            error_type = vision_data.get('error_type', 'Unknown')
                            user_msg = vision_data.get('user_message', 'Bilinmeyen hata')
                            
                            # Hata tipine göre uyarı seviyesi
                            if error_type in ["FileNotFoundError", "ValueError"]:
                                st.error(f"❌ {user_msg}")
                            elif "rate_limit" in vision_data.get('error', '').lower():
                                st.warning(f"⏱️ {user_msg}")
                            else:
                                st.warning(f"⚠️ Görsel analiz uyarısı: {user_msg}")
                            
                            # Detaylı hata bilgisi
                            with st.expander("🔍 Teknik Detaylar (Geliştiriciler için)"):
                                st.code(f"Hata Tipi: {error_type}")
                                st.code(f"Hata Mesajı: {vision_data.get('error', 'Unknown')}")
                                
                                # Çözüm önerileri
                                if "rate_limit" in vision_data.get('error', '').lower():
                                    if "tokens per day" in vision_data.get('error', '').lower():
                                        st.info("""
                                        **Çözüm:**
                                        - Groq günlük token limiti (100,000) doldu
                                        - Yarın sabah otomatik sıfırlanır
                                        - Acil kullanım için Groq Pro'ya geçin: https://console.groq.com/settings/billing
                                        """)
                                    else:
                                        st.info("""
                                        **Çözüm:**
                                        - Dakikalık limit (30 istek) aşıldı
                                        - 1-2 dakika bekleyin ve tekrar deneyin
                                        """)
                                elif "401" in vision_data.get('error', ''):
                                    st.info("""
                                    **Çözüm:**
                                    - API anahtarınız geçersiz
                                    - Yeni anahtar alın: https://console.groq.com
                                    - Streamlit Cloud Secrets'ı güncelleyin
                                    """)
                                elif "timeout" in vision_data.get('error', '').lower():
                                    st.info("""
                                    **Çözüm:**
                                    - İstek zaman aşımına uğradı
                                    - Daha küçük bir görsel deneyin
                                    - İnternet bağlantınızı kontrol edin
                                    """)
                                elif "model_decommissioned" in vision_data.get('error', '').lower():
                                    st.error("""
                                    **Kritik:**
                                    - Kullanılan AI modeli kullanımdan kaldırıldı
                                    - Sistem güncellemesi gerekiyor
                                    - Lütfen geliştiriciyle iletişime geçin
                                    """)
                                else:
                                    st.info("Sorun devam ederse lütfen farklı bir görsel deneyin.")
                        
                        # Güven puanı
                        confidence = calculate_confidence_score(results)
                        
                        if confidence < 8:
                            st.warning(f"⚠️ Güven puanı: {confidence:.1f}/10 - Bilgiler tam doğrulanamadı!")
                        else:
                            st.success(f"✅ Güven puanı: {confidence:.1f}/10")
                        
                        # Rapor
                        st.divider()
                        st.markdown("### 📋 Analiz Raporu")
                        st.markdown(results["report"])
                        
                        # İndirme
                        st.divider()
                        pdf_gen = PDFReportGenerator()
                        report_path = pdf_gen.generate_report(results, "reports/rapor.txt")
                        
                        if report_path and os.path.exists(report_path):
                            with open(report_path, "r", encoding="utf-8") as f:
                                st.download_button(
                                    label="📥 Raporu İndir (TXT)",
                                    data=f.read(),
                                    file_name=f"pharma_guard_{uploaded_file.name}.txt",
                                    mime="text/plain",
                                    use_container_width=True
                                )
                        
                    except Exception as e:
                        st.error(f"❌ Hata oluştu: {str(e)}")
                        
                        # Rate limit kontrolü
                        if "429" in str(e) or "rate_limit" in str(e).lower():
                            if "tokens per day" in str(e).lower() or "tpd" in str(e).lower():
                                st.warning("""
                                ### ⏱️ GÜNLÜK TOKEN LİMİTİ DOLDU
                                
                                **Sorun:** Groq ücretsiz hesabınızın günlük token limiti (100,000) doldu.
                                
                                **Çözümler:**
                                
                                1. **Yarın Sabah Deneyin** (Önerilen)
                                   - Limit her gün sıfırlanır
                                   - Ücretsiz ve kolay
                                
                                2. **Groq Pro'ya Geçin** (Hemen kullanmak için)
                                   - https://console.groq.com/settings/billing
                                   - Ücretli ama limitsiz
                                """)
                            else:
                                st.warning("""
                                ### ⏱️ DAKİKALIK LİMİT AŞILDI
                                
                                **Sorun:** Dakikada 30 istek limiti aşıldı.
                                
                                **Çözüm:** 1-2 dakika bekleyin ve tekrar deneyin.
                                """)
                        
                        with st.expander("🔍 Detaylı Hata Bilgisi (Geliştiriciler için)"):
                            st.code(f"Hata Tipi: {type(e).__name__}")
                            st.code(f"Hata Mesajı: {str(e)}")
                            st.code("Stack Trace:")
                            st.code(traceback.format_exc())
                            
                        st.info("""
                        **Olası Çözümler:**
                        
                        1. **API Key Sorunu:** Secrets'ı kontrol edin
                        2. **Görsel Sorunu:** Daha küçük/farklı görsel deneyin
                        3. **Timeout:** Birkaç saniye bekleyip tekrar deneyin
                        4. **Prospektüs Yok:** Normal, sistem yine çalışır
                        
                        **Destek:** https://github.com/yourusername/pharma-guard-ai/issues
                        """)


if __name__ == "__main__":
    main()
