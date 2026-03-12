"""
PHARMA-GUARD AI - Streamlit Arayüzü
Yapay Zeka Destekli Akıllı İlaç Denetçisi
DOM Hatası Düzeltildi - v2.1
"""

import streamlit as st
import os
from dotenv import load_dotenv
from agents import PharmaGuardOrchestrator
from utils import validate_image, resize_image, PDFReportGenerator, calculate_confidence_score, create_data_directories

# Ortam değişkenlerini yükle
load_dotenv(override=True)

# Sayfa yapılandırması
st.set_page_config(
    page_title="💊 PHARMA-GUARD AI",
    page_icon="💊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS Stil
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 1rem;
    }
    .warning-box {
        background-color: #FFF3CD;
        border-left: 5px solid #FFC107;
        padding: 1rem;
        margin: 1rem 0;
    }
    .success-box {
        background-color: #D4EDDA;
        border-left: 5px solid #28A745;
        padding: 1rem;
        margin: 1rem 0;
    }
    .danger-box {
        background-color: #F8D7DA;
        border-left: 5px solid #DC3545;
        padding: 1rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)


def load_api_keys():
    """API anahtarlarını yükler"""
    groq_key = None
    gemini_key = None
    
    # 1. Streamlit secrets
    try:
        if hasattr(st, 'secrets'):
            groq_key = st.secrets.get('GROQ_API_KEY')
            gemini_key = st.secrets.get('GOOGLE_API_KEY') or st.secrets.get('GEMINI_API_KEY')
    except Exception:
        pass
    
    # 2. .streamlit/secrets.toml
    if not groq_key or not gemini_key:
        try:
            with open('.streamlit/secrets.toml', 'r', encoding='utf-8') as f:
                for line in f:
                    if 'GROQ_API_KEY' in line and '=' in line and not groq_key:
                        groq_key = line.split('=')[1].strip().strip('"').strip("'")
                    if ('GOOGLE_API_KEY' in line or 'GEMINI_API_KEY' in line) and '=' in line and not gemini_key:
                        gemini_key = line.split('=')[1].strip().strip('"').strip("'")
        except Exception:
            pass
    
    # 3. .env dosyası
    if not groq_key or not gemini_key:
        try:
            load_dotenv(override=True)
            groq_key = groq_key or os.getenv("GROQ_API_KEY")
            gemini_key = gemini_key or os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
        except Exception:
            pass
    
    # 4. .env dosyasından doğrudan
    if not groq_key or not gemini_key:
        try:
            with open('.env', 'r', encoding='utf-8') as f:
                for line in f:
                    if line.startswith('GROQ_API_KEY=') and not groq_key:
                        groq_key = line.split('=', 1)[1].strip()
                    if (line.startswith('GOOGLE_API_KEY=') or line.startswith('GEMINI_API_KEY=')) and not gemini_key:
                        gemini_key = line.split('=', 1)[1].strip()
        except Exception:
            pass
    
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
        
        # API durumu
        if groq_key:
            st.success("✅ Groq API: Aktif")
        else:
            st.error("❌ Groq API: Bulunamadı")
            st.info("Lütfen `.env` veya `.streamlit/secrets.toml` dosyasına GROQ_API_KEY ekleyin")
        
        if gemini_key and gemini_key != "your_gemini_api_key_here":
            st.success("✅ Gemini API: Aktif")
        else:
            st.warning("⚠️ Gemini API: Yok (Simülasyon modu)")
        
        st.divider()
        
        st.info("""
        **Aktif Ajanlar:**
        - 🔍 Vision Scanner
        - 📚 RAG Specialist (11,000+ ilaç)
        - ⚠️ Safety Auditor
        - 📊 Report Synthesizer
        """)
        
        st.divider()
        
        st.subheader("📖 Kullanım Kılavuzu")
        st.markdown("""
        1. İlaç kutusunun net fotoğrafını yükleyin
        2. Analiz butonuna tıklayın
        3. Raporu inceleyin ve indirin
        
        **İpucu:** İyi aydınlatma ve net görüntü önemlidir!
        """)
    
    # API key kontrolü
    if not groq_key:
        st.error("⚠️ GROQ_API_KEY bulunamadı! Lütfen API anahtarınızı yapılandırın.")
        st.info("""
        **Hızlı Çözüm:**
        1. https://console.groq.com → API Keys
        2. Yeni anahtar oluştur
        3. `.env` veya `.streamlit/secrets.toml` dosyasına ekle
        4. Sayfayı yenile
        """)
        return
    
    # Sistemi başlat
    create_data_directories()
    
    # Ana içerik
    tab1, tab2, tab3 = st.tabs(["� Analiz", "📚 Prospektüs", "ℹ️ Hakkında"])
    
    with tab1:
        st.subheader("İlaç Görsel Analizi")
        
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
                    with st.spinner("Çoklu ajan sistemi çalışıyor..."):
                        try:
                            # Dosyayı kaydet
                            temp_path = os.path.join("uploads", uploaded_file.name)
                            with open(temp_path, "wb") as f:
                                f.write(uploaded_file.getbuffer())
                            
                            # Görsel doğrulama
                            if not validate_image(temp_path):
                                st.error("❌ Geçersiz görsel dosyası!")
                                return
                            
                            # Boyutlandır
                            resized_path = resize_image(temp_path)
                            
                            # Orchestrator oluştur
                            orchestrator = PharmaGuardOrchestrator(groq_key, gemini_key)
                            
                            # Analiz et
                            results = orchestrator.analyze_drug(resized_path)
                            
                            # Hata kontrolü
                            vision_data = results.get("vision", {})
                            if "error" in vision_data:
                                if vision_data.get("error") == "API_KEY_INVALID":
                                    st.error("🔑 API Anahtarı Geçersiz!")
                                    st.info(vision_data.get("error_detail", ""))
                                    return
                                elif vision_data.get("error") == "RATE_LIMIT":
                                    st.warning("⏱️ API Limit Aşıldı!")
                                    st.info(vision_data.get("error_detail", ""))
                                    return
                                else:
                                    st.error(f"❌ {vision_data.get('error_detail', 'Bilinmeyen hata')}")
                                    return
                            
                            # Güven puanı
                            confidence = calculate_confidence_score(results)
                            
                            # Sonuçları göster
                            st.divider()
                            
                            if confidence < 8:
                                st.warning(f"⚠️ Güven puanı: {confidence:.1f}/10 - Bilgiler %100 doğrulanamadı!")
                            else:
                                st.success(f"✅ Analiz tamamlandı! Güven puanı: {confidence:.1f}/10")
                            
                            # Rapor
                            st.markdown("### 📋 Analiz Raporu")
                            st.markdown(results["report"])
                            
                            # Rapor indirme
                            st.divider()
                            pdf_gen = PDFReportGenerator()
                            report_path = pdf_gen.generate_report(results, "reports/rapor.txt")
                            
                            if report_path:
                                with open(report_path, "r", encoding="utf-8") as report_file:
                                    st.download_button(
                                        label="📥 Raporu TXT Olarak İndir",
                                        data=report_file.read(),
                                        file_name=f"pharma_guard_rapor_{uploaded_file.name}.txt",
                                        mime="text/plain",
                                        use_container_width=True
                                    )
                            
                        except Exception as e:
                            st.error(f"❌ Analiz sırasında hata oluştu: {str(e)}")
                            
                            # Detaylı hata bilgisi
                            with st.expander("🔍 Detaylı Hata Bilgisi"):
                                st.code(f"Hata Tipi: {type(e).__name__}")
                                st.code(f"Hata Mesajı: {str(e)}")
                                import traceback
                                st.code(traceback.format_exc())
    
    with tab2:
        st.subheader("� Prospektüs Veritabanı")
        
        st.info("""
        Prospektüs bilgilerini `data/corpus/` klasörüne .txt dosyası olarak ekleyin.
        Sistem akıllı arama yapacaktır.
        """)
        
        corpus_path = "data/corpus"
        if os.path.exists(corpus_path):
            txt_files = [f for f in os.listdir(corpus_path) if f.endswith('.txt')]
            
            if txt_files:
                st.success(f"✅ {len(txt_files):,} adet prospektüs bulundu")
                
                with st.expander("📄 Prospektüs Listesi (İlk 20)"):
                    for txt in txt_files[:20]:
                        st.text(f"• {txt}")
                    if len(txt_files) > 20:
                        st.text(f"... ve {len(txt_files) - 20:,} dosya daha")
            else:
                st.warning("⚠️ Henüz prospektüs eklenmemiş.")
        
        st.divider()
        
        if st.button("🔄 Prospektüsleri Yeniden Yükle", use_container_width=True):
            with st.spinner("Prospektüsler yükleniyor..."):
                try:
                    orchestrator = PharmaGuardOrchestrator(groq_key, gemini_key)
                    success = orchestrator.rag_agent.initialize_db()
                    
                    if success:
                        st.success("✅ Prospektüsler başarıyla yüklendi!")
                    else:
                        st.error("❌ Prospektüsler yüklenemedi.")
                except Exception as e:
                    st.error(f"❌ Hata: {str(e)}")
    
    with tab3:
        st.subheader("ℹ️ Proje Hakkında")
        
        st.markdown("""
        ### 🎯 PHARMA-GUARD AI Nedir?
        
        Yapay zeka destekli, çoklu ajan mimarisine sahip akıllı ilaç denetleme sistemidir.
        
        ### 🤖 Kullanılan Teknolojiler
        
        - **Google Gemini Vision 2.5 Flash:** Görsel analiz
        - **Groq Llama 3.3 70B:** Metin analizi ve RAG
        - **Streamlit:** Kullanıcı arayüzü
        - **11,226 İlaç Prospektüsü:** Kapsamlı veritabanı
        
        ### 👥 Ajan Mimarisi
        
        1. **Vision Scanner:** Görsel analiz ve OCR
        2. **RAG Specialist:** Prospektüs veritabanı araması
        3. **Safety Auditor:** Güvenlik ve risk değerlendirmesi
        4. **Report Synthesizer:** Rapor oluşturma
        
        ### ⚠️ Önemli Uyarı
        
        Bu sistem **eğitim amaçlıdır**. Tıbbi kararlar için mutlaka sağlık profesyoneline danışın!
        
        ### 📊 İstatistikler
        
        - **Toplam İlaç:** 11,226
        - **Kategoriler:** 21
        - **Veritabanı Boyutu:** 10.03 MB
        - **Güven Puanı:** 8-9/10
        
        ---
        
        **Versiyon:** 2.1 (DOM Hatası Düzeltildi)  
        **Lisans:** MIT (Eğitim Amaçlı)
        """)


if __name__ == "__main__":
    main()
