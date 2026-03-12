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
    gemini_key = None
    
    try:
        # 1. Streamlit secrets
        if hasattr(st, 'secrets'):
            groq_key = st.secrets.get('GROQ_API_KEY')
            gemini_key = st.secrets.get('GEMINI_API_KEY') or st.secrets.get('GOOGLE_API_KEY')
    except:
        pass
    
    # 2. Environment
    if not groq_key or not gemini_key:
        load_dotenv()
        groq_key = groq_key or os.getenv("GROQ_API_KEY")
        gemini_key = gemini_key or os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    
    return groq_key, gemini_key


def main():
    """Ana uygulama"""
    
    # Başlık
    st.markdown('<h1 class="main-header">💊 PHARMA-GUARD AI</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #666;">Yapay Zeka Destekli Akıllı İlaç Denetçisi</p>', unsafe_allow_html=True)
    
    # API anahtarlarını yükle
    groq_key, gemini_key = load_api_keys()
    
    # Sidebar
    with st.sidebar:
        st.title("💊 Sistem Bilgileri")
        
        if groq_key:
            st.success("✅ Groq API: Aktif")
        else:
            st.error("❌ Groq API: Yok")
        
        if gemini_key and gemini_key != "your_gemini_api_key_here":
            st.success("✅ Gemini API: Aktif")
        else:
            st.warning("⚠️ Gemini API: Yok")
        
        st.divider()
        st.info("""
        **Aktif Ajanlar:**
        - 🔍 Vision Scanner
        - 📚 RAG Specialist
        - ⚠️ Safety Auditor
        - 📊 Report Synthesizer
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
        GEMINI_API_KEY = "AIzaSyB9VMJ926k-yBaqPRQdMCYh4WYDmE2QR4A"
        ```
        
        3. Save → App yeniden başlayacak
        """)
        st.stop()
    
    # Ana içerik
    st.subheader("📸 İlaç Görsel Analizi")
    
    uploaded_file = st.file_uploader(
        "İlaç kutusunun fotoğrafını yükleyin",
        type=["jpg", "jpeg", "png"],
        help="Net, iyi aydınlatılmış bir fotoğraf yükleyin"
    )
    
    if uploaded_file:
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.image(uploaded_file, caption="Yüklenen Görsel", use_container_width=True)
        
        with col2:
            if st.button("🔬 Analizi Başlat", type="primary", use_container_width=True):
                
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
                        
                        # Dosyayı kaydet
                        st.info("💾 Görsel kaydediliyor...")
                        temp_path = os.path.join("uploads", uploaded_file.name)
                        with open(temp_path, "wb") as f:
                            f.write(uploaded_file.getbuffer())
                        st.success(f"✅ Kaydedildi: {temp_path}")
                        
                        # Doğrula
                        st.info("🔍 Görsel doğrulanıyor...")
                        if not validate_image(temp_path):
                            st.error("❌ Geçersiz görsel!")
                            st.stop()
                        st.success("✅ Görsel geçerli")
                        
                        # Boyutlandır
                        st.info("📐 Boyutlandırılıyor...")
                        resized_path = resize_image(temp_path)
                        st.success("✅ Boyutlandırıldı")
                        
                        # AI Sistemi
                        st.info("🤖 AI sistemi başlatılıyor...")
                        orchestrator = PharmaGuardOrchestrator(groq_key, gemini_key)
                        st.success("✅ AI sistemi hazır")
                        
                        # Analiz
                        st.info("🔬 Analiz yapılıyor... (30-60 saniye)")
                        results = orchestrator.analyze_drug(resized_path)
                        st.success("✅ Analiz tamamlandı!")
                        
                        # Temizle progress
                        progress_container.empty()
                        
                        # Hata kontrolü
                        vision_data = results.get("vision", {})
                        if "error" in vision_data:
                            st.warning(f"⚠️ Görsel analiz uyarısı: {vision_data.get('user_message', 'Bilinmeyen')}")
                        
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
