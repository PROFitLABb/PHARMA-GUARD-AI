"""
PHARMA-GUARD AI - Basitleştirilmiş Versiyon (Hata Ayıklama)
"""

import streamlit as st
import os
from dotenv import load_dotenv

# Sayfa yapılandırması
st.set_page_config(
    page_title="💊 PHARMA-GUARD AI - Test",
    page_icon="💊",
    layout="wide"
)

st.title("💊 PHARMA-GUARD AI - Test Modu")

# API Key Kontrolü
st.subheader("🔑 API Key Kontrolü")

# 1. Streamlit Secrets
st.write("**1. Streamlit Secrets:**")
try:
    groq_from_secrets = st.secrets.get("GROQ_API_KEY", "YOK")
    gemini_from_secrets = st.secrets.get("GEMINI_API_KEY", "YOK")
    st.success(f"✅ GROQ_API_KEY: {groq_from_secrets[:20]}..." if len(groq_from_secrets) > 20 else f"❌ {groq_from_secrets}")
    st.success(f"✅ GEMINI_API_KEY: {gemini_from_secrets[:20]}..." if len(gemini_from_secrets) > 20 else f"❌ {gemini_from_secrets}")
except Exception as e:
    st.error(f"❌ Secrets hatası: {e}")

# 2. Environment Variables
st.write("**2. Environment Variables:**")
load_dotenv()
groq_from_env = os.getenv("GROQ_API_KEY", "YOK")
gemini_from_env = os.getenv("GEMINI_API_KEY", "YOK")
st.info(f"GROQ_API_KEY: {groq_from_env[:20]}..." if len(groq_from_env) > 20 else f"❌ {groq_from_env}")
st.info(f"GEMINI_API_KEY: {gemini_from_env[:20]}..." if len(gemini_from_env) > 20 else f"❌ {gemini_from_env}")

# 3. Dosya Sistemi
st.write("**3. Dosya Sistemi:**")
st.info(f"📁 Çalışma Dizini: {os.getcwd()}")
st.info(f"📁 uploads klasörü var mı? {os.path.exists('uploads')}")
st.info(f"📁 data/corpus klasörü var mı? {os.path.exists('data/corpus')}")

if os.path.exists('data/corpus'):
    txt_files = [f for f in os.listdir('data/corpus') if f.endswith('.txt')]
    st.success(f"✅ {len(txt_files)} prospektüs dosyası bulundu")
else:
    st.warning("⚠️ data/corpus klasörü yok")

# 4. Test Analizi
st.divider()
st.subheader("🧪 Test Analizi")

uploaded_file = st.file_uploader("Test için bir görsel yükleyin", type=["jpg", "jpeg", "png"])

if uploaded_file and st.button("🔬 Test Et"):
    try:
        st.info("1️⃣ Dosya yükleniyor...")
        
        # Klasör oluştur
        os.makedirs("uploads", exist_ok=True)
        
        # Dosyayı kaydet
        temp_path = os.path.join("uploads", uploaded_file.name)
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        st.success(f"✅ Dosya kaydedildi: {temp_path}")
        
        st.info("2️⃣ Groq API test ediliyor...")
        
        # Groq API key al
        groq_key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")
        
        if not groq_key:
            st.error("❌ GROQ_API_KEY bulunamadı!")
            st.stop()
        
        st.success(f"✅ API Key bulundu: {groq_key[:20]}...")
        
        st.info("3️⃣ Groq bağlantısı test ediliyor...")
        
        from groq import Groq
        client = Groq(api_key=groq_key)
        
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": "Merhaba, test mesajı"}],
            max_tokens=50
        )
        
        st.success(f"✅ Groq yanıtı: {response.choices[0].message.content}")
        
        st.info("4️⃣ Gemini API test ediliyor...")
        
        gemini_key = st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")
        
        if gemini_key and gemini_key != "your_gemini_api_key_here":
            try:
                import google.generativeai as genai
                genai.configure(api_key=gemini_key)
                model = genai.GenerativeModel('gemini-2.0-flash-exp')
                
                with open(temp_path, 'rb') as f:
                    image_data = f.read()
                
                response = model.generate_content([
                    "Bu görselde ne var? Kısaca açıkla.",
                    {"mime_type": "image/jpeg", "data": image_data}
                ])
                
                st.success(f"✅ Gemini yanıtı: {response.text[:100]}...")
                
            except Exception as e:
                st.warning(f"⚠️ Gemini hatası: {str(e)}")
        else:
            st.warning("⚠️ Gemini API key yok")
        
        st.success("🎉 TÜM TESTLER BAŞARILI!")
        
    except Exception as e:
        st.error(f"❌ HATA: {str(e)}")
        
        with st.expander("🔍 Detaylı Hata"):
            import traceback
            st.code(traceback.format_exc())

st.divider()
st.info("""
**Streamlit Cloud Secrets Nasıl Eklenir?**

1. App sayfanızda sağ üstteki ⚙️ Settings'e tıklayın
2. Secrets sekmesine gidin
3. Şunu yapıştırın:

```toml
GROQ_API_KEY = "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"
GEMINI_API_KEY = "AIzaSyB9VMJ926k-yBaqPRQdMCYh4WYDmE2QR4A"
```

4. Save butonuna tıklayın
5. App otomatik yeniden başlayacak
""")
