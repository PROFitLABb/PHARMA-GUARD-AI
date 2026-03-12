"""
PHARMA-GUARD Streamlit Arayüzü
Yapay Zeka Destekli Akıllı İlaç Denetçisi
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


def initialize_system():
    """Sistemi başlatır"""
    create_data_directories()
    
    groq_key = None
    gemini_key = None
    
    # 1. Önce Streamlit secrets'tan dene (en güvenilir)
    try:
        if hasattr(st, 'secrets'):
            if 'GROQ_API_KEY' in st.secrets:
                groq_key = st.secrets['GROQ_API_KEY']
            if 'GOOGLE_API_KEY' in st.secrets:
                gemini_key = st.secrets['GOOGLE_API_KEY']
    except Exception as e:
        pass
    
    # 2. .streamlit/secrets.toml dosyasından doğrudan oku
    if not groq_key or not gemini_key:
        try:
            with open('.streamlit/secrets.toml', 'r', encoding='utf-8') as f:
                for line in f:
                    if 'GROQ_API_KEY' in line and '=' in line and not groq_key:
                        groq_key = line.split('=')[1].strip().strip('"').strip("'")
                    if 'GOOGLE_API_KEY' in line and '=' in line and not gemini_key:
                        gemini_key = line.split('=')[1].strip().strip('"').strip("'")
        except Exception as e:
            pass
    
    # 3. .env dosyasından dene
    if not groq_key or not gemini_key:
        try:
            load_dotenv(override=True)
            if not groq_key:
                groq_key = os.getenv("GROQ_API_KEY")
            if not gemini_key:
                gemini_key = os.getenv("GOOGLE_API_KEY")
        except Exception as e:
            pass
    
    # 4. .env dosyasından doğrudan oku
    if not groq_key or not gemini_key:
        try:
            with open('.env', 'r', encoding='utf-8') as f:
                for line in f:
                    if line.startswith('GROQ_API_KEY=') and not groq_key:
                        groq_key = line.split('=', 1)[1].strip()
                    if line.startswith('GOOGLE_API_KEY=') and not gemini_key:
                        gemini_key = line.split('=', 1)[1].strip()
        except Exception as e:
            pass
    
    # Hata kontrolü
    if not groq_key:
        st.error("⚠️ GROQ_API_KEY bulunamadı!")
        st.stop()
    
    # Gemini opsiyonel
    if not gemini_key or gemini_key == "your_gemini_api_key_here":
        st.sidebar.warning("⚠️ Gemini API anahtarı yok - Görsel analizi simüle edilecek")
        gemini_key = None
    else:
        st.sidebar.success("✅ Gemini Vision aktif")
    
    return PharmaGuardOrchestrator(groq_key, gemini_key)


def main():
    """Ana uygulama"""
    
    # Başlık
    st.markdown('<h1 class="main-header">💊 PHARMA-GUARD AI</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #666;">Yapay Zeka Destekli Akıllı İlaç Denetçisi</p>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.image("https://img.icons8.com/fluency/96/000000/pill.png", width=80)
        st.title("Sistem Bilgileri")
        st.info("""
        **Aktif Ajanlar (Groq-Only):**
        - 🔍 Vision Scanner (Llama 3.2 Vision)
        - 📚 RAG Specialist (Llama 3.1)
        - ⚠️ Safety Auditor (Llama 3.1)
        - 📊 Report Synthesizer (Llama 3.1)
        """)
        
        st.divider()
        
        st.subheader("Kullanım Kılavuzu")
        st.markdown("""
        1. İlaç kutusunun net fotoğrafını yükleyin
        2. Analiz butonuna tıklayın
        3. Raporu inceleyin ve indirin
        
        **Not:** İyi aydınlatma ve net görüntü önemlidir!
        """)
    
    # Ana içerik
    tab1, tab2, tab3 = st.tabs(["📸 Analiz", "📚 Prospektüs Yönetimi", "ℹ️ Hakkında"])
    
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
                st.image(uploaded_file, caption="Yüklenen Görsel", use_column_width=True)
            
            with col2:
                if st.button("🔬 Analizi Başlat", type="primary"):
                    with st.spinner("Çoklu ajan sistemi çalışıyor..."):
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
                        
                        # Sistemi başlat ve analiz et
                        orchestrator = initialize_system()
                        
                        try:
                            results = orchestrator.analyze_drug(resized_path)
                            
                            # Hata kontrolü - Vision
                            vision_data = results.get("vision", {})
                            if "error" in vision_data:
                                if vision_data.get("error") == "API_KEY_INVALID":
                                    st.error("🔑 API Anahtarı Geçersiz!")
                                    st.info(vision_data.get("error_detail", ""))
                                    st.info("""
                                    **Hızlı Çözüm:**
                                    1. https://console.groq.com → API Keys
                                    2. Yeni anahtar oluştur
                                    3. `.env` veya `.streamlit/secrets.toml` dosyasını güncelle
                                    4. Streamlit'i yeniden başlat (Ctrl+C sonra tekrar çalıştır)
                                    """)
                                    return
                                elif vision_data.get("error") == "RATE_LIMIT":
                                    st.warning("⏱️ API Limit Aşıldı!")
                                    st.info(vision_data.get("error_detail", ""))
                                    return
                                else:
                                    st.error(f"❌ {vision_data.get('error_detail', 'Bilinmeyen hata')}")
                            
                            # Güven puanı hesapla
                            confidence = calculate_confidence_score(results)
                            
                            # Uyarı göster
                            if confidence < 8:
                                st.markdown(f'<div class="warning-box">⚠️ <b>DİKKAT:</b> Güven puanı düşük ({confidence:.1f}/10). Bilgiler %100 doğrulanamadı, profesyonel yardım alın!</div>', unsafe_allow_html=True)
                            else:
                                st.markdown(f'<div class="success-box">✅ Analiz tamamlandı. Güven puanı: {confidence:.1f}/10</div>', unsafe_allow_html=True)
                            
                            # Raporu göster
                            st.divider()
                            st.markdown("### 📋 Analiz Raporu")
                            st.markdown(results["report"])
                            
                            # Rapor dosyası oluştur
                            st.divider()
                            pdf_gen = PDFReportGenerator()
                            report_path = pdf_gen.generate_report(results, "reports/rapor.txt")
                            
                            if report_path:
                                with open(report_path, "r", encoding="utf-8") as report_file:
                                    st.download_button(
                                        label="📥 Raporu TXT Olarak İndir",
                                        data=report_file.read(),
                                        file_name=f"pharma_guard_rapor_{uploaded_file.name}.txt",
                                        mime="text/plain"
                                    )
                            
                        except Exception as e:
                            st.error(f"❌ Analiz sırasında hata oluştu: {str(e)}")
    
    with tab2:
        st.subheader("📚 Prospektüs Veritabanı Yönetimi")
        
        st.info("""
        Prospektüs bilgilerini `data/corpus/` klasörüne .txt dosyası olarak ekleyin.
        Sistem Groq ile semantik arama yapacaktır.
        
        **Örnek format:** ilac_adi.txt (düz metin olarak prospektüs içeriği)
        """)
        
        corpus_path = "data/corpus"
        if os.path.exists(corpus_path):
            txt_files = [f for f in os.listdir(corpus_path) if f.endswith('.txt')]
            
            if txt_files:
                st.success(f"✅ {len(txt_files)} adet prospektüs bulundu:")
                for txt in txt_files:
                    st.text(f"📄 {txt}")
            else:
                st.warning("⚠️ Henüz prospektüs eklenmemiş. Lütfen .txt dosyalarını data/corpus/ klasörüne ekleyin.")
        
        st.divider()
        
        if st.button("🔄 Prospektüsleri Yükle"):
            with st.spinner("Prospektüsler yükleniyor..."):
                orchestrator = initialize_system()
                success = orchestrator.rag_agent.initialize_db()
                
                if success:
                    st.success("✅ Prospektüsler başarıyla yüklendi!")
                else:
                    st.error("❌ Prospektüsler yüklenemedi. Lütfen .txt dosyalarını kontrol edin.")
    
    with tab3:
        st.subheader("ℹ️ Proje Hakkında")
        
        st.markdown("""
        ### 🎯 PHARMA-GUARD AI Nedir?
        
        Yapay zeka destekli, çoklu ajan mimarisine sahip akıllı ilaç denetleme sistemidir.
        
        ### 🤖 Kullanılan Teknolojiler
        
        - **Groq (Llama 3.2 Vision):** Görsel analiz ve OCR
        - **Groq (Llama 3.1 70B):** Güvenlik denetimi ve rapor sentezi
        - **Streamlit:** Kullanıcı arayüzü
        
        ### ⚡ Neden Sadece Groq?
        
        - Çok hızlı inference (saniyeler içinde)
        - Ücretsiz tier cömert (günlük limit yüksek)
        - Vision + Text modelleri tek platformda
        - Kurulum basit, bağımlılık az
        
        ### 👥 Ajan Mimarisi
        
        1. **Vision Scanner:** Görsel analiz ve OCR
        2. **RAG Specialist:** Prospektüs veritabanı araması
        3. **Safety Auditor:** Güvenlik ve risk değerlendirmesi
        4. **Report Synthesizer:** Rapor oluşturma
        
        ### ⚠️ Önemli Uyarı
        
        Bu sistem eğitim amaçlıdır. Tıbbi kararlar için mutlaka sağlık profesyoneline danışın!
        
        ---
        
        **Proje:** Yapay Zeka Uygulamaları ve Veri Bilimi  
        **Tema:** Sağlık Teknolojileri ve Yapay Zeka Etiği
        """)


if __name__ == "__main__":
    main()
