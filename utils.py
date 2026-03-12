"""
Yardımcı fonksiyonlar - Görüntü işleme ve raporlama
"""

import os
from PIL import Image
from datetime import datetime


def validate_image(image_path: str) -> bool:
    """Görsel dosyasını doğrular"""
    try:
        img = Image.open(image_path)
        img.verify()
        return True
    except Exception:
        return False


def resize_image(image_path: str, max_size: tuple = (1024, 1024)) -> str:
    """Görseli yeniden boyutlandırır"""
    try:
        img = Image.open(image_path)
        img.thumbnail(max_size, Image.Resampling.LANCZOS)
        
        output_path = image_path.replace(".", "_resized.")
        img.save(output_path, quality=85)
        return output_path
    except Exception as e:
        print(f"Görsel boyutlandırma hatası: {e}")
        return image_path


class PDFReportGenerator:
    """Basit metin tabanlı rapor oluşturucu (PDF yerine TXT)"""
    
    def __init__(self):
        pass
    
    def generate_report(self, report_data: dict, output_path: str = "rapor.txt"):
        """Markdown raporunu TXT dosyasına kaydeder"""
        try:
            # PDF yerine TXT uzantısı kullan
            output_path = output_path.replace('.pdf', '.txt')
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write("=" * 60 + "\n")
                f.write("PHARMA-GUARD İLAÇ ANALİZ RAPORU\n")
                f.write("=" * 60 + "\n\n")
                f.write(f"Tarih: {datetime.now().strftime('%d.%m.%Y %H:%M')}\n\n")
                f.write("-" * 60 + "\n\n")
                
                # Rapor içeriğini ekle
                report_text = report_data.get("report", "Rapor oluşturulamadı")
                f.write(report_text)
                
                f.write("\n\n" + "=" * 60 + "\n")
                f.write("Bu rapor PHARMA-GUARD AI tarafından oluşturulmuştur.\n")
                f.write("Eğitim amaçlıdır. Tıbbi kararlar için doktora danışın.\n")
                f.write("=" * 60 + "\n")
            
            return output_path
            
        except Exception as e:
            print(f"Rapor oluşturma hatası: {e}")
            return None


def calculate_confidence_score(data: dict) -> float:
    """Genel güven puanını hesaplar"""
    scores = []
    
    if "vision" in data and "guven_puani" in data["vision"]:
        try:
            score = float(data["vision"]["guven_puani"])
            scores.append(score)
        except (ValueError, TypeError):
            pass
    
    if "safety" in data and "guven_puani" in data["safety"]:
        try:
            score = float(data["safety"]["guven_puani"])
            scores.append(score)
        except (ValueError, TypeError):
            pass
    
    return sum(scores) / len(scores) if scores else 0.0


def create_data_directories():
    """Gerekli klasörleri oluşturur"""
    os.makedirs("data/corpus", exist_ok=True)
    os.makedirs("uploads", exist_ok=True)
    os.makedirs("reports", exist_ok=True)
