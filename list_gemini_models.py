"""
Gemini API'de mevcut modelleri listele
"""
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("❌ API anahtarı bulunamadı!")
    exit(1)

print(f"✅ API Key bulundu: {api_key[:20]}...")

genai.configure(api_key=api_key)

print("\n" + "="*60)
print("MEVCUT GEMİNİ MODELLERİ")
print("="*60)

try:
    models = genai.list_models()
    
    vision_models = []
    text_models = []
    
    for model in models:
        if 'generateContent' in model.supported_generation_methods:
            model_info = f"- {model.name}"
            
            # Vision desteği var mı?
            if hasattr(model, 'supported_generation_methods'):
                if 'vision' in model.name.lower() or 'pro' in model.name.lower() or 'flash' in model.name.lower():
                    vision_models.append(model_info)
                else:
                    text_models.append(model_info)
    
    print("\n📸 GÖRSEL ANALİZ DESTEKLİ MODELLER:")
    if vision_models:
        for m in vision_models:
            print(m)
    else:
        print("  (Bulunamadı)")
    
    print("\n📝 METIN MODELLER:")
    if text_models:
        for m in text_models[:5]:  # İlk 5'i göster
            print(m)
    else:
        print("  (Bulunamadı)")
    
    print("\n" + "="*60)
    print("ÖNERİLEN MODEL:")
    if vision_models:
        recommended = vision_models[0].replace("- ", "")
        print(f"  {recommended}")
        print(f"\nKullanım:")
        print(f"  self.model = genai.GenerativeModel('{recommended}')")
    else:
        print("  ⚠️ Görsel analiz destekli model bulunamadı!")
    
except Exception as e:
    print(f"\n❌ Hata: {e}")
    print("\nOlası nedenler:")
    print("1. API anahtarı geçersiz")
    print("2. İnternet bağlantısı yok")
    print("3. Gemini API erişimi yok")
