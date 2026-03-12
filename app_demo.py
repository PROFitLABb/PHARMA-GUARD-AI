"""
PHARMA-GUARD Demo Modu
API anahtarı olmadan test edebilirsiniz
"""

import streamlit as st
import os
from utils import validate_image, resize_image, create_data_directories

# Sayfa yapılandırması
st.set_page_config(
    page_title="💊 PHARMA-GUARD AI (Demo)",
    page_icon="💊",
    layout="wide"
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
    .warning-box {
        background-color: #FFF3CD;
        border-left: 5px solid #FFC107;
        padding: 1rem;
        margin: 1rem 0;
    }
    .info-box {
        background-color: #D1ECF1;
        border-left: 5px solid #17A2B8;
        padding: 1rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.markdown('<h1 class="main-header">💊 PHARMA-GUARD AI (Demo Modu)</h1>', unsafe_allow_html=True)
    
    st.markdown('<div class="info-box">ℹ️ <b>Demo Modu:</b> Bu versiyon API anahtarı olmadan çalışır ve örnek sonuçlar gösterir.</div>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.title("Demo Bilgileri")
        st.info("""
        **Bu demo versiyonunda:**
        - Gerçek AI analizi yapılmaz
        - Örnek sonuçlar gösterilir
        - Sistem mimarisini test edebilirsiniz
        
        **Gerçek sistem için:**
        1. Groq API anahtarı alın
        2. `streamlit run app.py` çalıştırın
        """)
        
        st.divider()
        
        st.subheader("API Anahtarı Nasıl Alınır?")
        st.markdown("""
        1. https://console.groq.com
        2. Ücretsiz hesap oluştur
        3. API Keys → Create
        4. Anahtarı `.env` dosyasına ekle
        """)
    
    # Ana içerik
    tab1, tab2 = st.tabs(["📸 Demo Analiz", "ℹ️ Hakkında"])
    
    with tab1:
        st.subheader("İlaç Görsel Analizi (Demo)")
        
        uploaded_file = st.file_uploader(
            "İlaç kutusunun fotoğrafını yükleyin",
            type=["jpg", "jpeg", "png"],
            help="Demo modunda örnek sonuç gösterilecek"
        )
        
        if uploaded_file:
            col1, col2 = st.columns([1, 1])
            
            with col1:
                st.image(uploaded_file, caption="Yüklenen Görsel", use_column_width=True)
            
            with col2:
                if st.button("🔬 Demo Analizi Başlat", type="primary"):
                    with st.spinner("Demo analiz çalışıyor..."):
                        import time
                        time.sleep(2)  # Gerçekçi görünmesi için
                        
                        # Demo sonuçları
                        st.markdown('<div class="warning-box">⚠️ <b>DİKKAT:</b> Bu demo sonuçtur. Gerçek analiz için API anahtarı gereklidir.</div>', unsafe_allow_html=True)
                        
                        st.divider()
                        st.markdown("### 📋 Demo Analiz Raporu")
                        
                        demo_report = """
# İLAÇ KİMLİK ÖZETİ

**Ticari Ad:** PAROL 500 MG (Demo)  
**Etken Madde:** Parasetamol  
**Dozaj:** 500 mg  
**Form:** Tablet  
**Üretici:** Atabay İlaç (Demo)

---

## KULLANIM AMACI

Parol, ağrı kesici ve ateş düşürücü bir ilaçtır:
- Baş ağrısı
- Diş ağrısı
- Kas ağrıları
- Grip ve soğuk algınlığı

---

## KRİTİK UYARILAR VE YAN ETKİLER

### ⚠️ Önemli Uyarılar:
- Günlük maksimum doz: 4000 mg (8 tablet)
- Karaciğer hastalığı olanlarda dikkatli kullanılmalı
- Alkol ile birlikte kullanılmamalı

### Yan Etkiler:
- Nadir: Bulantı, kusma
- Aşırı dozda: Karaciğer hasarı riski

### İlaç Etkileşimleri:
- Warfarin (kan sulandırıcı) ile etkileşim
- Diğer parasetamol içeren ilaçlarla birlikte kullanılmamalı

---

## ETKEN MADDE VE ÜRETİCİ DETAYLARI

**Kimyasal Ad:** Parasetamol (Acetaminophen)  
**Üretici:** Atabay İlaç Sanayi A.Ş.  
**Menşe:** Türkiye  
**Sertifikalar:** TİTCK Onaylı

---

## KAYNAKÇA

Bu demo rapor örnek verilerle oluşturulmuştur.  
Gerçek analiz için Groq API anahtarı gereklidir.

---

**⚠️ UYARI:** Bu sistem eğitim amaçlıdır. Tıbbi kararlar için mutlaka sağlık profesyoneline danışın!
"""
                        st.markdown(demo_report)
                        
                        st.divider()
                        st.info("""
                        **Gerçek Sistem Özellikleri:**
                        - Groq Llama 3.2 Vision ile görsel analiz
                        - RAG tabanlı prospektüs arama
                        - Güvenlik risk değerlendirmesi
                        - PDF rapor oluşturma
                        
                        **Gerçek sistemi kullanmak için:**
                        1. Groq API anahtarı alın (ücretsiz)
                        2. `.env` dosyasına ekleyin
                        3. `streamlit run app.py` çalıştırın
                        """)
    
    with tab2:
        st.subheader("ℹ️ PHARMA-GUARD Hakkında")
        
        st.markdown("""
        ### 🎯 Proje Amacı
        
        Yapay zeka destekli, çoklu ajan mimarisine sahip akıllı ilaç denetleme sistemi.
        
        ### 🤖 Teknolojiler
        
        - **Groq Llama 3.2 Vision (90B):** Görsel analiz
        - **Groq Llama 3.1 (70B):** Güvenlik denetimi
        - **Streamlit:** Kullanıcı arayüzü
        
        ### 📊 Ajan Mimarisi
        
        1. **Vision Scanner:** Görsel analiz ve OCR
        2. **RAG Specialist:** Prospektüs veritabanı araması
        3. **Safety Auditor:** Güvenlik ve risk değerlendirmesi
        4. **Report Synthesizer:** Rapor oluşturma
        
        ### 🚀 Gerçek Sistemi Kullanmak İçin
        
        **Adım 1:** Groq API Anahtarı Alın
        ```
        https://console.groq.com
        → Ücretsiz hesap oluştur
        → API Keys → Create API Key
        ```
        
        **Adım 2:** Anahtarı Ekleyin
        ```
        .env dosyasına:
        GROQ_API_KEY=gsk_your_key_here
        ```
        
        **Adım 3:** Gerçek Uygulamayı Başlatın
        ```bash
        streamlit run app.py
        ```
        
        ### ⚠️ Önemli Not
        
        Bu sistem eğitim amaçlıdır. Tıbbi kararlar için mutlaka sağlık profesyoneline danışın!
        
        ---
        
        **Proje:** Yapay Zeka Uygulamaları ve Veri Bilimi  
        **Tema:** Sağlık Teknolojileri ve Yapay Zeka Etiği
        """)
        
        st.divider()
        
        st.success("""
        **✅ Demo Modu Başarıyla Çalışıyor!**
        
        Sistem mimarisini test ettiniz. Gerçek AI analizleri için:
        1. `YENİ_API_ANAHTARI_EKLE.txt` dosyasını okuyun
        2. Groq API anahtarı alın
        3. `streamlit run app.py` ile gerçek sistemi başlatın
        """)


if __name__ == "__main__":
    create_data_directories()
    main()
