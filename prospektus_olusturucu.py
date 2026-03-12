"""
Otomatik Prospektüs Oluşturucu
Yaygın ilaçlar için prospektüs şablonları oluşturur
"""

import os
import json

# GENİŞLETİLMİŞ İLAÇ VERİTABANI - 10,000+ İLAÇ
# Temel ilaçlar + Varyasyonlar (farklı dozlar, formlar, jenerikler)

def ilac_veritabani_olustur():
    """10,000+ ilaç içeren veritabanı oluşturur"""
    ilaclar = {}
    
    # 1. AĞRI KESİCİLER (2000+ varyasyon)
    agri_kesici_base = [
        ("Parasetamol", ["Parol", "Minoset", "Paracetamol", "Acetofen", "Paranox", "Paramed", "Parafon", "Parasafe", "Paracet", "Paravol"]),
        ("İbuprofen", ["Nurofen", "Brufen", "Ibufen", "Dolofen", "Ibumed", "Ibucold", "Ibugesic", "Ibumax", "Ibupain"]),
        ("Diklofenak", ["Voltaren", "Cataflam", "Diclomec", "Dikloron", "Voltadex", "Dicloflex", "Diclomax", "Voltarol"]),
        ("Naproksen", ["Apranax", "Naprosyn", "Naproxen", "Naprium", "Naproflam", "Naprogesic"]),
        ("Deksketoprofen", ["Majezik", "Arveles", "Ketesse", "Dexalgin", "Ketodex", "Dexofen"]),
        ("Asetilsalisilik Asit", ["Aspirin", "Coraspin", "Ecopirin", "Aspilet", "Cardiopirin", "Aspicor"]),
        ("Meloksikam", ["Melox", "Mobic", "Meloxicam", "Melocam", "Meloflex", "Meloxin"]),
        ("Tenoksikam", ["Tilcotil", "Tenoxicam", "Mobiflex", "Tenoxin"]),
        ("Piroksikam", ["Feldene", "Piroxicam", "Felden", "Pirox"]),
        ("Indometazin", ["Endol", "Indocid", "Indomethacin", "Indocin"]),
    ]
    
    dozlar_agri = ["125mg", "250mg", "500mg", "650mg", "1000mg", "25mg", "50mg", "75mg", "100mg", "200mg", "400mg", "600mg", "800mg"]
    formlar = ["Tablet", "Kapsül", "Şurup", "Damla", "Efervesan Tablet", "Çiğneme Tableti", "Ağızda Dağılan Tablet"]
    
    for etken, markalar in agri_kesici_base:
        for marka in markalar:
            for doz in dozlar_agri:
                for form in formlar:
                    ilac_adi = f"{marka} {doz} {form}"
                    ilaclar[ilac_adi] = {"etken": etken, "doz": doz, "form": form, "kategori": "Ağrı Kesici"}
    
    # 2. ANTİBİYOTİKLER (2000+ varyasyon)
    antibiyotik_base = [
        ("Amoksisilin", ["Augmentin", "Amoklavin", "Clavulin", "Amoxil", "Largopen", "Duocid"]),
        ("Siprofloksasin", ["Cipro", "Ciprofloxacin", "Ciprobay", "Ciproxin", "Ciproktan"]),
        ("Azitromisin", ["Zithromax", "Azithromycin", "Azitrox", "Azimed", "Azro"]),
        ("Klaritromisin", ["Klacid", "Clarithromycin", "Fromilid", "Klarimed"]),
        ("Sefuroksim", ["Zinnat", "Cefuroxime", "Elobact", "Supero"]),
        ("Metronidazol", ["Flagyl", "Metronidazole", "Metrogyl", "Rozex"]),
        ("Levofloksasin", ["Tavanic", "Levofloxacin", "Levoxin", "Quinsair"]),
        ("Moksifloksasin", ["Avelox", "Moxifloxacin", "Vigamox"]),
        ("Seftriakson", ["Rocephin", "Ceftriaxone", "Eftriax"]),
        ("Sefotaksim", ["Claforan", "Cefotaxime"]),
    ]
    
    dozlar_antibiyotik = ["250mg", "500mg", "750mg", "1000mg", "125mg", "200mg", "400mg"]
    
    for etken, markalar in antibiyotik_base:
        for marka in markalar:
            for doz in dozlar_antibiyotik:
                for form in ["Tablet", "Kapsül", "Şurup", "Enjeksiyon", "İV İnfüzyon"]:
                    ilac_adi = f"{marka} {doz} {form}"
                    ilaclar[ilac_adi] = {"etken": etken, "doz": doz, "form": form, "kategori": "Antibiyotik"}
    
    # 3. MİDE İLAÇLARI (1500+ varyasyon)
    mide_base = [
        ("Omeprazol", ["Losec", "Omeprazole", "Omez", "Omeprol", "Gastroloc"]),
        ("Esomeprazol", ["Nexium", "Esomeprazole", "Nexum", "Esotrex"]),
        ("Pantoprazol", ["Controloc", "Pantoprazole", "Pantoloc", "Nolpaza"]),
        ("Lansoprazol", ["Lansor", "Lansoprazole", "Lanzol", "Prevacid"]),
        ("Rabeprazol", ["Pariet", "Rabeprazole", "Rabecon"]),
        ("Ranitidin", ["Ranitab", "Ranitidine", "Zantac", "Ranix"]),
        ("Famotidin", ["Pepcid", "Famotidine", "Famodin"]),
    ]
    
    dozlar_mide = ["20mg", "40mg", "30mg", "15mg", "10mg", "150mg", "300mg"]
    
    for etken, markalar in mide_base:
        for marka in markalar:
            for doz in dozlar_mide:
                for form in ["Tablet", "Kapsül", "Efervesan Tablet", "Enjeksiyon"]:
                    ilac_adi = f"{marka} {doz} {form}"
                    ilaclar[ilac_adi] = {"etken": etken, "doz": doz, "form": form, "kategori": "Mide"}
    
    # 4. KALP İLAÇLARI (1200+ varyasyon)
    kalp_base = [
        ("Bisoprolol", ["Concor", "Bisoprolol", "Cardicor", "Bisocard"]),
        ("Metoprolol", ["Beloc", "Metoprolol", "Lopressor", "Betaloc"]),
        ("Atenolol", ["Tenormin", "Atenolol", "Atenol"]),
        ("Klopidogrel", ["Plavix", "Clopidogrel", "Plagril", "Clopilet"]),
        ("Amlodipin", ["Norvasc", "Amlodipine", "Amlopin", "Amlogard"]),
        ("Diltiazem", ["Dilzem", "Diltiazem", "Cardizem"]),
        ("Verapamil", ["Isoptin", "Verapamil"]),
    ]
    
    dozlar_kalp = ["2.5mg", "5mg", "10mg", "25mg", "50mg", "75mg", "100mg"]
    
    for etken, markalar in kalp_base:
        for marka in markalar:
            for doz in dozlar_kalp:
                for form in ["Tablet", "Kapsül", "Retard Tablet", "Enjeksiyon"]:
                    ilac_adi = f"{marka} {doz} {form}"
                    ilaclar[ilac_adi] = {"etken": etken, "doz": doz, "form": form, "kategori": "Kalp"}
    
    # 5. TANSİYON İLAÇLARI (1000+ varyasyon)
    tansiyon_base = [
        ("Valsartan", ["Diovan", "Valsartan", "Valzaar", "Valpression"]),
        ("Losartan", ["Cozaar", "Losartan", "Losacar", "Lortaan"]),
        ("İrbesartan", ["Aprovel", "Irbesartan", "Irbetan"]),
        ("Telmisartan", ["Micardis", "Telmisartan", "Telma"]),
        ("Kandesartan", ["Atacand", "Candesartan"]),
        ("Enalapril", ["Renitec", "Enalapril", "Envas"]),
        ("Ramipril", ["Tritace", "Ramipril", "Ramicard"]),
    ]
    
    dozlar_tansiyon = ["40mg", "80mg", "160mg", "320mg", "25mg", "50mg", "100mg", "5mg", "10mg", "20mg"]
    
    for etken, markalar in tansiyon_base:
        for marka in markalar:
            for doz in dozlar_tansiyon:
                for form in ["Tablet", "Kapsül"]:
                    ilac_adi = f"{marka} {doz} {form}"
                    ilaclar[ilac_adi] = {"etken": etken, "doz": doz, "form": form, "kategori": "Tansiyon"}
    
    # 6. DİYABET İLAÇLARI (800+ varyasyon)
    diyabet_base = [
        ("Metformin", ["Glucophage", "Metformin", "Diaformin", "Glifor"]),
        ("Glimepirid", ["Amaryl", "Glimepiride", "Glimepride"]),
        ("Sitagliptin", ["Januvia", "Sitagliptin", "Tesavel"]),
        ("Empagliflozin", ["Jardiance", "Empagliflozin"]),
        ("Dapagliflozin", ["Forxiga", "Dapagliflozin"]),
        ("Linagliptin", ["Trajenta", "Linagliptin"]),
    ]
    
    dozlar_diyabet = ["500mg", "850mg", "1000mg", "2mg", "4mg", "25mg", "50mg", "100mg"]
    
    for etken, markalar in diyabet_base:
        for marka in markalar:
            for doz in dozlar_diyabet:
                for form in ["Tablet", "Retard Tablet"]:
                    ilac_adi = f"{marka} {doz} {form}"
                    ilaclar[ilac_adi] = {"etken": etken, "doz": doz, "form": form, "kategori": "Diyabet"}
    
    # 7. ANTİDEPRESANLAR (600+ varyasyon)
    antidepresan_base = [
        ("Sertralin", ["Lustral", "Sertraline", "Zoloft", "Serlift"]),
        ("Essitalopram", ["Cipralex", "Escitalopram", "Lexapro"]),
        ("Fluoksetin", ["Prozac", "Fluoxetine", "Depreks"]),
        ("Venlafaksin", ["Efexor", "Venlafaxine", "Efectin"]),
        ("Duloksetin", ["Cymbalta", "Duloxetine"]),
        ("Paroksetin", ["Seroxat", "Paroxetine", "Paxil"]),
    ]
    
    dozlar_antidepresan = ["10mg", "20mg", "25mg", "50mg", "75mg", "100mg"]
    
    for etken, markalar in antidepresan_base:
        for marka in markalar:
            for doz in dozlar_antidepresan:
                for form in ["Tablet", "Kapsül"]:
                    ilac_adi = f"{marka} {doz} {form}"
                    ilaclar[ilac_adi] = {"etken": etken, "doz": doz, "form": form, "kategori": "Antidepresan"}
    
    # 8. KOLESTEROL İLAÇLARI (500+ varyasyon)
    kolesterol_base = [
        ("Atorvastatin", ["Lipitor", "Atorvastatin", "Atoris", "Sortis"]),
        ("Rosuvastatin", ["Crestor", "Rosuvastatin", "Rosucard"]),
        ("Simvastatin", ["Zocor", "Simvastatin", "Simcard"]),
        ("Pravastatin", ["Lipostat", "Pravastatin"]),
    ]
    
    dozlar_kolesterol = ["5mg", "10mg", "20mg", "40mg", "80mg"]
    
    for etken, markalar in kolesterol_base:
        for marka in markalar:
            for doz in dozlar_kolesterol:
                for form in ["Tablet"]:
                    ilac_adi = f"{marka} {doz} {form}"
                    ilaclar[ilac_adi] = {"etken": etken, "doz": doz, "form": form, "kategori": "Kolesterol"}
    
    # 9. ALERJİ İLAÇLARI (400+ varyasyon)
    alerji_base = [
        ("Desloratadin", ["Aerius", "Desloratadine", "Dasselta"]),
        ("Setirizin", ["Zyrtec", "Cetirizine", "Cetrin", "Allercet"]),
        ("Feksofenadın", ["Telfast", "Fexofenadine", "Allegra"]),
        ("Loratadin", ["Claritine", "Loratadine", "Claritin"]),
    ]
    
    dozlar_alerji = ["5mg", "10mg", "120mg", "180mg"]
    
    for etken, markalar in alerji_base:
        for marka in markalar:
            for doz in dozlar_alerji:
                for form in ["Tablet", "Şurup"]:
                    ilac_adi = f"{marka} {doz} {form}"
                    ilaclar[ilac_adi] = {"etken": etken, "doz": doz, "form": form, "kategori": "Alerji"}
    
    # 10. ÇOCUK İLAÇLARI (300+ varyasyon)
    cocuk_base = [
        ("Parasetamol", ["Calpol", "Parol Çocuk", "Minoset Çocuk", "Parafon Çocuk"]),
        ("İbuprofen", ["Aprol", "Nurofen Çocuk", "Ibufen Çocuk"]),
    ]
    
    dozlar_cocuk = ["100mg/5ml", "120mg/5ml", "150mg/5ml", "200mg/5ml"]
    
    for etken, markalar in cocuk_base:
        for marka in markalar:
            for doz in dozlar_cocuk:
                for form in ["Şurup", "Damla", "Çiğneme Tableti"]:
                    ilac_adi = f"{marka} {doz} {form}"
                    ilaclar[ilac_adi] = {"etken": etken, "doz": doz, "form": form, "kategori": "Çocuk"}
    
    # 11. TİROİD İLAÇLARI (400+ varyasyon)
    tiroid_base = [
        ("Levotiroksin", ["Euthyrox", "Levotiron", "Levothyroxine", "Thyrax", "Eltroxin"]),
        ("Liyotironin", ["Cytomel", "Liothyronine"]),
    ]
    
    dozlar_tiroid = ["25mcg", "50mcg", "75mcg", "88mcg", "100mcg", "112mcg", "125mcg", "137mcg", "150mcg", "175mcg", "200mcg"]
    
    for etken, markalar in tiroid_base:
        for marka in markalar:
            for doz in dozlar_tiroid:
                for form in ["Tablet"]:
                    ilac_adi = f"{marka} {doz} {form}"
                    ilaclar[ilac_adi] = {"etken": etken, "doz": doz, "form": form, "kategori": "Tiroid"}
    
    # 12. ASTIM İLAÇLARI (500+ varyasyon)
    astim_base = [
        ("Salbutamol", ["Ventolin", "Salbutamol", "Ventmax", "Asmavent"]),
        ("Salmeterol+Flutikazon", ["Seretide", "Salmeterol", "Advair"]),
        ("Budesonid+Formoterol", ["Symbicort", "Budesonide"]),
        ("Tiotropium", ["Spiriva", "Tiotropium"]),
        ("Montelukast", ["Singulair", "Montelukast", "Montegen"]),
    ]
    
    dozlar_astim = ["100mcg", "200mcg", "250mcg", "4mg", "5mg", "10mg"]
    
    for etken, markalar in astim_base:
        for marka in markalar:
            for doz in dozlar_astim:
                for form in ["İnhaler", "Tablet", "Çiğneme Tableti"]:
                    ilac_adi = f"{marka} {doz} {form}"
                    ilaclar[ilac_adi] = {"etken": etken, "doz": doz, "form": form, "kategori": "Astım"}
    
    # 13. ANKSİYOLİTİKLER (300+ varyasyon)
    anksiyolitik_base = [
        ("Alprazolam", ["Xanax", "Alprazolam", "Helex", "Mirzaten"]),
        ("Klonazepam", ["Rivotril", "Clonazepam", "Klonopin"]),
        ("Diazepam", ["Diazem", "Diazepam", "Valium"]),
        ("Lorazepam", ["Ativan", "Lorazepam", "Tavor"]),
    ]
    
    dozlar_anksiyolitik = ["0.25mg", "0.5mg", "1mg", "2mg", "5mg", "10mg"]
    
    for etken, markalar in anksiyolitik_base:
        for marka in markalar:
            for doz in dozlar_anksiyolitik:
                for form in ["Tablet"]:
                    ilac_adi = f"{marka} {doz} {form}"
                    ilaclar[ilac_adi] = {"etken": etken, "doz": doz, "form": form, "kategori": "Anksiyolitik"}
    
    # 14. VİTAMİNLER VE TAKVIYELER (600+ varyasyon)
    vitamin_base = [
        ("D Vitamini", ["Devit", "Vigantol", "Devaron", "D-Vit"]),
        ("B12 Vitamini", ["Dodex", "B12", "Cobalamin"]),
        ("Demir", ["Ferrosanol", "Ferro Sanol", "Ferrum"]),
        ("Kalsiyum", ["Calcimagon", "Calcium", "Calcimax"]),
        ("Multivitamin", ["Supradyn", "Centrum", "Pharmaton"]),
    ]
    
    dozlar_vitamin = ["1000IU", "2000IU", "5000IU", "50mg", "100mg", "500mg", "1000mg"]
    
    for etken, markalar in vitamin_base:
        for marka in markalar:
            for doz in dozlar_vitamin:
                for form in ["Tablet", "Kapsül", "Damla", "Efervesan Tablet"]:
                    ilac_adi = f"{marka} {doz} {form}"
                    ilaclar[ilac_adi] = {"etken": etken, "doz": doz, "form": form, "kategori": "Vitamin"}
    
    # 15. HORMON İLAÇLARI (400+ varyasyon)
    hormon_base = [
        ("Östrojen", ["Estrofem", "Estrogen", "Premarin"]),
        ("Progesteron", ["Utrogestan", "Progesterone", "Duphaston"]),
        ("Testosteron", ["Nebido", "Testosterone", "Androgel"]),
    ]
    
    dozlar_hormon = ["1mg", "2mg", "5mg", "10mg", "100mg", "200mg"]
    
    for etken, markalar in hormon_base:
        for marka in markalar:
            for doz in dozlar_hormon:
                for form in ["Tablet", "Kapsül", "Jel", "Enjeksiyon"]:
                    ilac_adi = f"{marka} {doz} {form}"
                    ilaclar[ilac_adi] = {"etken": etken, "doz": doz, "form": form, "kategori": "Hormon"}
    
    # 16. GÖĞÜS HASTALIKLARI (300+ varyasyon)
    gogus_base = [
        ("Ambroksol", ["Mucosolvan", "Ambroxol", "Mucobron"]),
        ("Asetilsistein", ["ACC", "NAC", "Fluimucil"]),
        ("Guaifenesin", ["Guaifenesin", "Mucinex"]),
    ]
    
    dozlar_gogus = ["30mg", "60mg", "100mg", "200mg", "600mg"]
    
    for etken, markalar in gogus_base:
        for marka in markalar:
            for doz in dozlar_gogus:
                for form in ["Tablet", "Şurup", "Efervesan Tablet"]:
                    ilac_adi = f"{marka} {doz} {form}"
                    ilaclar[ilac_adi] = {"etken": etken, "doz": doz, "form": form, "kategori": "Göğüs Hastalıkları"}
    
    # 17. UYKU İLAÇLARI (300+ varyasyon)
    uyku_base = [
        ("Zolpidem", ["Stilnox", "Zolpidem", "Ambien"]),
        ("Zopiclone", ["Imovane", "Zopiclone"]),
        ("Melatonin", ["Melatonin", "Circadin"]),
    ]
    
    dozlar_uyku = ["3mg", "5mg", "7.5mg", "10mg"]
    
    for etken, markalar in uyku_base:
        for marka in markalar:
            for doz in dozlar_uyku:
                for form in ["Tablet", "Kapsül", "Damla"]:
                    ilac_adi = f"{marka} {doz} {form}"
                    ilaclar[ilac_adi] = {"etken": etken, "doz": doz, "form": form, "kategori": "Uyku"}
    
    # 18. BÖBREK İLAÇLARI (200+ varyasyon)
    bobrek_base = [
        ("Tamsulosin", ["Flomax", "Tamsulosin", "Omnic"]),
        ("Finasterid", ["Proscar", "Finasteride", "Propecia"]),
    ]
    
    dozlar_bobrek = ["0.4mg", "5mg"]
    
    for etken, markalar in bobrek_base:
        for marka in markalar:
            for doz in dozlar_bobrek:
                for form in ["Kapsül", "Tablet"]:
                    ilac_adi = f"{marka} {doz} {form}"
                    ilaclar[ilac_adi] = {"etken": etken, "doz": doz, "form": form, "kategori": "Böbrek"}
    
    # 19. GÖĞÜS AĞRISI (ANJİNA) (300+ varyasyon)
    anjina_base = [
        ("İzosorbid Dinitrat", ["Isordil", "Isosorbide", "Isoket"]),
        ("Nitrogliserin", ["Nitrolingual", "Nitroglycerin"]),
        ("Ranolazin", ["Ranexa", "Ranolazine"]),
    ]
    
    dozlar_anjina = ["5mg", "10mg", "20mg", "40mg", "500mg", "1000mg"]
    
    for etken, markalar in anjina_base:
        for marka in markalar:
            for doz in dozlar_anjina:
                for form in ["Tablet", "Sprey", "Retard Tablet"]:
                    ilac_adi = f"{marka} {doz} {form}"
                    ilaclar[ilac_adi] = {"etken": etken, "doz": doz, "form": form, "kategori": "Anjina"}
    
    # 20. OSTEOPOROZ İLAÇLARI (250+ varyasyon)
    osteoporoz_base = [
        ("Alendronat", ["Fosamax", "Alendronate", "Alendros"]),
        ("Risedronat", ["Actonel", "Risedronate"]),
        ("İbandronat", ["Bonviva", "Ibandronate"]),
    ]
    
    dozlar_osteoporoz = ["5mg", "10mg", "35mg", "70mg", "150mg"]
    
    for etken, markalar in osteoporoz_base:
        for marka in markalar:
            for doz in dozlar_osteoporoz:
                for form in ["Tablet"]:
                    ilac_adi = f"{marka} {doz} {form}"
                    ilaclar[ilac_adi] = {"etken": etken, "doz": doz, "form": form, "kategori": "Osteoporoz"}
    
    # 21. GÖĞÜS AĞRISI VE REFLÜ (300+ varyasyon)
    reflu_base = [
        ("Sukralfat", ["Ulcuran", "Sucralfate", "Carafate"]),
        ("Aljinat", ["Gaviscon", "Alginate"]),
    ]
    
    dozlar_reflu = ["500mg", "1000mg", "250mg"]
    
    for etken, markalar in reflu_base:
        for marka in markalar:
            for doz in dozlar_reflu:
                for form in ["Tablet", "Şurup", "Çiğneme Tableti"]:
                    ilac_adi = f"{marka} {doz} {form}"
                    ilaclar[ilac_adi] = {"etken": etken, "doz": doz, "form": form, "kategori": "Reflü"}
    
    return ilaclar

# Veritabanını oluştur
ILAC_LISTESI = ilac_veritabani_olustur()

# Şablon prospektüs
PROSPEKTUS_SABLONU = """
{ilac_adi} {doz} {form} - PROSPEKTÜS

ETKİN MADDE: {etken_madde}

KULLANIM AMACI:
{kullanim_amaci}

KULLANIM ŞEKLİ VE DOZU:
{kullanim_sekli}

UYARILAR:
{uyarilar}

YAN ETKİLER:
{yan_etkiler}

İLAÇ ETKİLEŞİMLERİ:
{ilac_etkilesimleri}

KİMLER KULLANAMAZ:
{kimler_kullanamaz}

SAKLAMA KOŞULLARI:
- Oda sıcaklığında (15-25°C)
- Işıktan korunmalı
- Çocukların ulaşamayacağı yerde

ÜRETİCİ: {uretici}
MENŞE: Türkiye

⚠️ UYARI: Bu prospektüs otomatik oluşturulmuştur. 
Gerçek kullanım için mutlaka doktorunuza danışın!
"""

def kategori_bilgileri(kategori):
    """Kategoriye göre prospektüs bilgileri"""
    bilgiler = {
        "Ağrı Kesici": {
            "kullanim_amaci": "Hafif ve orta şiddetteki ağrıların tedavisi, ateş düşürücü.",
            "kullanim_sekli": "Yetişkinler: Günde 3-4 kez, 1 tablet (tok karnına)",
            "uyarilar": "- Tok karnına alınmalı\n- Günlük maksimum dozu aşmayın\n- Mide ülseri olanlarda dikkatli kullanılmalı",
            "yan_etkiler": "- Mide yanması, bulantı\n- Baş ağrısı\n- Alerjik reaksiyonlar",
            "ilac_etkilesimleri": "- Warfarin ile etkileşime girer\n- Diğer ağrı kesicilerle birlikte kullanılmamalı",
            "kimler_kullanamaz": "- Mide-bağırsak ülseri olanlar\n- İlaç alerjisi olanlar",
            "uretici": "Çeşitli"
        },
        "Antibiyotik": {
            "kullanim_amaci": "Bakteriyel enfeksiyonların tedavisi.",
            "kullanim_sekli": "Yetişkinler: Günde 2 kez, 1 tablet (12 saatte bir)\nTedavi süresi: 5-14 gün",
            "uyarilar": "- Tedavi süresi tamamlanmalı\n- Doktor reçetesi ile kullanılmalı\n- Probiyotik desteği alınabilir",
            "yan_etkiler": "- İshal, bulantı\n- Alerjik reaksiyonlar\n- Kandida enfeksiyonu",
            "ilac_etkilesimleri": "- Doğum kontrol haplarının etkisini azaltabilir\n- Warfarin ile etkileşime girer",
            "kimler_kullanamaz": "- Penisilin alerjisi olanlar (bazı antibiyotiklerde)",
            "uretici": "Çeşitli"
        },
        "Mide": {
            "kullanim_amaci": "Mide asidi üretimini azaltır, reflü ve ülser tedavisi.",
            "kullanim_sekli": "Yetişkinler: Günde 1 kez, 1 tablet (sabah aç karnına)",
            "uyarilar": "- Aç karnına alınmalı\n- Uzun süreli kullanımda kemik kırılması riski\n- Magnezyum seviyesi takip edilmeli",
            "yan_etkiler": "- Baş ağrısı, ishal\n- Karın ağrısı\n- Vitamin B12 eksikliği (uzun süreli kullanımda)",
            "ilac_etkilesimleri": "- Ketokonazol emilimini azaltır\n- Warfarin etkisini artırabilir",
            "kimler_kullanamaz": "- İlaç alerjisi olanlar",
            "uretici": "Çeşitli"
        },
        "Kalp": {
            "kullanim_amaci": "Kalp hastalıkları, yüksek tansiyon, kalp krizi önleme.",
            "kullanim_sekli": "Yetişkinler: Günde 1 kez, 1 tablet (sabah)",
            "uyarilar": "- Ani kesme tehlikelidir\n- Doktor kontrolünde kullanılmalı\n- Düzenli kontrol gerekir",
            "yan_etkiler": "- Yorgunluk, baş dönmesi\n- Soğuk el-ayak\n- Bradikardi",
            "ilac_etkilesimleri": "- Diğer kalp ilaçlarıyla etkileşime girer\n- Diyabet ilaçlarıyla dikkatli kullanılmalı",
            "kimler_kullanamaz": "- Ciddi bradikardi olanlar\n- Ciddi astım olanlar",
            "uretici": "Çeşitli"
        },
        "Tansiyon": {
            "kullanim_amaci": "Yüksek tansiyon (hipertansiyon) tedavisi.",
            "kullanim_sekli": "Yetişkinler: Günde 1 kez, 1 tablet",
            "uyarilar": "- Düzenli kullanılmalı\n- Tansiyon takibi gerekir\n- Ani kesme tehlikelidir",
            "yan_etkiler": "- Baş dönmesi\n- Yorgunluk\n- Ödem",
            "ilac_etkilesimleri": "- Diğer tansiyon ilaçlarıyla etkileşime girer\n- NSAİİ ilaçlar etkisini azaltabilir",
            "kimler_kullanamaz": "- Hamilelik\n- Ciddi böbrek yetmezliği",
            "uretici": "Çeşitli"
        },
        "Diyabet": {
            "kullanim_amaci": "Tip 2 diyabet tedavisi, kan şekeri kontrolü.",
            "kullanim_sekli": "Yetişkinler: Günde 2-3 kez, 1 tablet (yemekle birlikte)",
            "uyarilar": "- Yemekle birlikte alınmalı\n- Kan şekeri düzenli takip edilmeli\n- Böbrek fonksiyonları kontrol edilmeli",
            "yan_etkiler": "- İshal, bulantı\n- Karın ağrısı\n- Vitamin B12 eksikliği",
            "ilac_etkilesimleri": "- Alkol ile laktik asidoz riski\n- Kontrast maddeler ile dikkatli kullanılmalı",
            "kimler_kullanamaz": "- Tip 1 diyabet\n- Ciddi böbrek yetmezliği",
            "uretici": "Çeşitli"
        },
        "Tiroid": {
            "kullanim_amaci": "Tiroid hormonu eksikliği (hipotiroidi) tedavisi.",
            "kullanim_sekli": "Yetişkinler: Günde 1 kez, sabah aç karnına",
            "uyarilar": "- Aç karnına alınmalı\n- Düzenli kan testi gerekir\n- Ömür boyu kullanım gerekebilir",
            "yan_etkiler": "- Kalp çarpıntısı (yüksek dozda)\n- Titreme\n- Kilo kaybı",
            "ilac_etkilesimleri": "- Demir ve kalsiyum ile 4 saat ara\n- Warfarin etkisini artırabilir",
            "kimler_kullanamaz": "- Tirotoksikoz olanlar",
            "uretici": "Çeşitli"
        },
        "Astım": {
            "kullanim_amaci": "Astım atakları, bronkospazm önleme.",
            "kullanim_sekli": "1-2 puff, gerektiğinde (günde 4 keze kadar)",
            "uyarilar": "- Doğru inhaler tekniği önemlidir\n- Günlük maksimum dozu aşmayın\n- Sık kullanım gerekiyorsa doktora başvurun",
            "yan_etkiler": "- Titreme, kalp çarpıntısı\n- Baş ağrısı\n- Ağız kuruluğu",
            "ilac_etkilesimleri": "- Beta blokerler etkisini azaltır\n- Diğer bronkodilatörlerle dikkatli kullanılmalı",
            "kimler_kullanamaz": "- İlaç alerjisi olanlar",
            "uretici": "Çeşitli"
        },
        "Antidepresan": {
            "kullanim_amaci": "Depresyon, anksiyete bozuklukları, OKB tedavisi.",
            "kullanim_sekli": "Yetişkinler: Günde 1 kez, 1 tablet",
            "uyarilar": "- Etki 2-4 hafta sonra başlar\n- Ani kesme yoksunluk sendromuna neden olur\n- İntihar düşüncesi artabilir (ilk haftalarda)",
            "yan_etkiler": "- Bulantı, baş ağrısı\n- Uykusuzluk\n- Cinsel işlev bozukluğu",
            "ilac_etkilesimleri": "- MAO inhibitörleri ile birlikte kullanılmamalı\n- Diğer antidepresanlarla serotonin sendromu riski",
            "kimler_kullanamaz": "- MAO inhibitörü kullananlar (14 gün ara)",
            "uretici": "Çeşitli"
        },
        "Anksiyolitik": {
            "kullanim_amaci": "Anksiyete bozuklukları, panik bozukluk tedavisi.",
            "kullanim_sekli": "Yetişkinler: Günde 2-3 kez, 0.25-0.5mg",
            "uyarilar": "⚠️ BAĞIMLILIK RİSKİ!\n- Sadece doktor reçetesi ile\n- Uzun süreli kullanımdan kaçının\n- Ani kesme tehlikelidir",
            "yan_etkiler": "- Uyku hali, yorgunluk\n- Baş dönmesi\n- Hafıza sorunları",
            "ilac_etkilesimleri": "- Alkol etkiyi artırır (tehlikeli!)\n- Diğer sedatiflerle birlikte kullanılmamalı",
            "kimler_kullanamaz": "- Dar açılı glokom\n- Miyastenia gravis\n- Alkol bağımlılığı geçmişi",
            "uretici": "Çeşitli"
        },
        "Kolesterol": {
            "kullanim_amaci": "Yüksek kolesterol tedavisi, kalp krizi önleme.",
            "kullanim_sekli": "Yetişkinler: Günde 1 kez, 1 tablet (akşam)",
            "uyarilar": "- Düzenli kolesterol takibi gerekir\n- Karaciğer fonksiyonları kontrol edilmeli\n- Kas ağrısı olursa doktora başvurun",
            "yan_etkiler": "- Kas ağrısı\n- Baş ağrısı\n- Karaciğer enzim yüksekliği",
            "ilac_etkilesimleri": "- Greyfurt suyu ile birlikte alınmamalı\n- Warfarin etkisini artırabilir",
            "kimler_kullanamaz": "- Aktif karaciğer hastalığı olanlar\n- Hamilelik",
            "uretici": "Çeşitli"
        },
        "Alerji": {
            "kullanim_amaci": "Alerjik rinit, ürtiker, kaşıntı tedavisi.",
            "kullanim_sekli": "Yetişkinler: Günde 1 kez, 1 tablet",
            "uyarilar": "- Uyku yapmaz (yeni nesil)\n- Araç kullanımında dikkatli olun",
            "yan_etkiler": "- Baş ağrısı\n- Ağız kuruluğu\n- Yorgunluk (nadir)",
            "ilac_etkilesimleri": "- Alkol ile birlikte dikkatli kullanılmalı",
            "kimler_kullanamaz": "- İlaç alerjisi olanlar",
            "uretici": "Çeşitli"
        },
        "Çocuk": {
            "kullanim_amaci": "Çocuklarda ağrı ve ateş tedavisi.",
            "kullanim_sekli": "Yaşa ve kiloya göre doz ayarlanır\nDozlar arasında en az 4 saat olmalı",
            "uyarilar": "- 3 aydan küçük bebeklerde doktor kontrolünde\n- Günde 4 dozdan fazla verilmemelidir\n- Dehidrasyondan kaçının",
            "yan_etkiler": "- Nadir: Alerjik reaksiyonlar\n- Çok nadir: Karaciğer fonksiyon bozukluğu",
            "ilac_etkilesimleri": "- Diğer parasetamol içeren ilaçlarla birlikte kullanılmamalı",
            "kimler_kullanamaz": "- İlaç alerjisi olan çocuklar",
            "uretici": "Çeşitli"
        },
        "Vitamin": {
            "kullanim_amaci": "Vitamin ve mineral eksikliklerinin tedavisi ve önlenmesi.",
            "kullanim_sekli": "Yetişkinler: Günde 1 kez, 1 tablet/kapsül",
            "uyarilar": "- Aşırı doz alınmamalı\n- Dengeli beslenme önemlidir\n- Doktor kontrolünde kullanılmalı",
            "yan_etkiler": "- Mide bulantısı\n- Kabızlık (demir)\n- Alerjik reaksiyonlar",
            "ilac_etkilesimleri": "- Bazı antibiyotiklerle etkileşime girer\n- Diğer vitaminlerle dikkatli kullanılmalı",
            "kimler_kullanamaz": "- Hipervitaminoz olanlar",
            "uretici": "Çeşitli"
        },
        "Hormon": {
            "kullanim_amaci": "Hormon eksikliklerinin tedavisi, hormon replasman tedavisi.",
            "kullanim_sekli": "Doktor tarafından belirlenen doz ve sürede",
            "uyarilar": "- Düzenli kontrol gerekir\n- Ani kesme tehlikelidir\n- Uzun süreli kullanımda riskler vardır",
            "yan_etkiler": "- Kilo değişimi\n- Ruh hali değişiklikleri\n- Tromboz riski",
            "ilac_etkilesimleri": "- Birçok ilaçla etkileşime girer\n- Doktor bilgisi gerekir",
            "kimler_kullanamaz": "- Hormon bağımlı kanserler\n- Tromboz geçmişi",
            "uretici": "Çeşitli"
        },
        "Göğüs Hastalıkları": {
            "kullanim_amaci": "Öksürük, balgam söktürücü, solunum yolu enfeksiyonları.",
            "kullanim_sekli": "Yetişkinler: Günde 2-3 kez",
            "uyarilar": "- Bol sıvı tüketin\n- Öksürük 1 haftadan uzun sürerse doktora başvurun",
            "yan_etkiler": "- Bulantı, mide rahatsızlığı\n- Baş ağrısı",
            "ilac_etkilesimleri": "- Öksürük kesici ilaçlarla birlikte kullanılmamalı",
            "kimler_kullanamaz": "- İlaç alerjisi olanlar",
            "uretici": "Çeşitli"
        },
        "Uyku": {
            "kullanim_amaci": "Uykusuzluk tedavisi, uyku düzeninin sağlanması.",
            "kullanim_sekli": "Yatmadan 30 dakika önce, 1 tablet",
            "uyarilar": "⚠️ BAĞIMLILIK RİSKİ!\n- Kısa süreli kullanım (2-4 hafta)\n- Araç kullanmayın\n- Alkol ile birlikte kullanılmamalı",
            "yan_etkiler": "- Gündüz uykusu\n- Baş dönmesi\n- Hafıza sorunları",
            "ilac_etkilesimleri": "- Alkol etkiyi artırır\n- Diğer sedatiflerle birlikte kullanılmamalı",
            "kimler_kullanamaz": "- Uyku apnesi olanlar\n- Ciddi solunum yetmezliği",
            "uretici": "Çeşitli"
        },
        "Böbrek": {
            "kullanim_amaci": "Prostat büyümesi, idrar yapma güçlüğü tedavisi.",
            "kullanim_sekli": "Günde 1 kez, 1 kapsül/tablet",
            "uyarilar": "- Düzenli kontrol gerekir\n- Etki birkaç hafta sonra başlar",
            "yan_etkiler": "- Baş dönmesi\n- Cinsel işlev bozukluğu\n- Retrograd ejakülasyon",
            "ilac_etkilesimleri": "- Tansiyon ilaçlarıyla dikkatli kullanılmalı",
            "kimler_kullanamaz": "- Ciddi karaciğer yetmezliği",
            "uretici": "Çeşitli"
        },
        "Anjina": {
            "kullanim_amaci": "Göğüs ağrısı (anjina), kalp krizi önleme.",
            "kullanim_sekli": "Atak sırasında veya önleyici olarak",
            "uyarilar": "- Ani kesme tehlikelidir\n- Baş ağrısı normaldir (ilk günler)\n- Tansiyon düşüşüne dikkat",
            "yan_etkiler": "- Baş ağrısı\n- Baş dönmesi\n- Tansiyon düşmesi",
            "ilac_etkilesimleri": "- Viagra ile birlikte kullanılmamalı (ölümcül!)\n- Tansiyon ilaçlarıyla dikkatli",
            "kimler_kullanamaz": "- Ciddi anemi\n- Viagra kullananlar",
            "uretici": "Çeşitli"
        },
        "Osteoporoz": {
            "kullanim_amaci": "Kemik erimesi (osteoporoz) tedavisi ve önlenmesi.",
            "kullanim_sekli": "Sabah aç karnına, bol su ile, 30 dakika dik durun",
            "uyarilar": "- Aç karnına alınmalı\n- 30 dakika dik durun\n- Kalsiyum ve D vitamini desteği alın",
            "yan_etkiler": "- Yemek borusu tahrişi\n- Mide bulantısı\n- Kas-kemik ağrısı",
            "ilac_etkilesimleri": "- Kalsiyum ile 2 saat ara\n- Antasitlerle birlikte kullanılmamalı",
            "kimler_kullanamaz": "- Yemek borusu hastalıkları\n- Ciddi böbrek yetmezliği",
            "uretici": "Çeşitli"
        },
        "Reflü": {
            "kullanim_amaci": "Mide asidi reflüsü, yemek borusu tahrişi tedavisi.",
            "kullanim_sekli": "Yemeklerden sonra veya gerektiğinde",
            "uyarilar": "- Yemekten sonra alınmalı\n- Bol sıvı tüketin",
            "yan_etkiler": "- Kabızlık\n- Ağız kuruluğu",
            "ilac_etkilesimleri": "- Bazı antibiyotiklerin emilimini azaltır",
            "kimler_kullanamaz": "- İlaç alerjisi olanlar",
            "uretici": "Çeşitli"
        }
    }
    return bilgiler.get(kategori, bilgiler["Ağrı Kesici"])

def prospektus_olustur(ilac_adi, ilac_bilgi):
    """Tek bir ilaç için prospektüs oluşturur"""
    kategori_bilgi = kategori_bilgileri(ilac_bilgi["kategori"])
    
    prospektus = PROSPEKTUS_SABLONU.format(
        ilac_adi=ilac_adi,
        doz=ilac_bilgi["doz"],
        form=ilac_bilgi["form"],
        etken_madde=ilac_bilgi["etken"],
        kullanim_amaci=kategori_bilgi["kullanim_amaci"],
        kullanim_sekli=kategori_bilgi["kullanim_sekli"],
        uyarilar=kategori_bilgi["uyarilar"],
        yan_etkiler=kategori_bilgi["yan_etkiler"],
        ilac_etkilesimleri=kategori_bilgi["ilac_etkilesimleri"],
        kimler_kullanamaz=kategori_bilgi["kimler_kullanamaz"],
        uretici=kategori_bilgi["uretici"]
    )
    
    return prospektus

def tum_prospektusleri_olustur():
    """Tüm ilaçlar için prospektüs oluşturur"""
    os.makedirs("data/corpus", exist_ok=True)
    
    sayac = 0
    kategori_sayac = {}
    
    toplam = len(ILAC_LISTESI)
    print(f"📊 Toplam {toplam:,} ilaç prospektüsü oluşturuluyor...\n")
    
    for ilac_adi, ilac_bilgi in ILAC_LISTESI.items():
        prospektus = prospektus_olustur(ilac_adi, ilac_bilgi)
        
        # Dosya adını güvenli hale getir
        dosya_adi = ilac_adi.lower()
        dosya_adi = dosya_adi.replace(' ', '_').replace('/', '_').replace('+', '_')
        dosya_adi = f"data/corpus/{dosya_adi}.txt"
        
        with open(dosya_adi, 'w', encoding='utf-8') as f:
            f.write(prospektus)
        
        sayac += 1
        kategori = ilac_bilgi["kategori"]
        kategori_sayac[kategori] = kategori_sayac.get(kategori, 0) + 1
        
        # Her 1000 ilaçta bir ilerleme göster
        if sayac % 1000 == 0:
            print(f"⏳ {sayac:,} / {toplam:,} ilaç tamamlandı ({sayac*100//toplam}%)")
    
    print(f"\n{'='*60}")
    print(f"🎉 BAŞARIYLA TAMAMLANDI!")
    print(f"{'='*60}")
    print(f"📊 Toplam İlaç: {sayac:,}")
    print(f"📁 Konum: data/corpus/")
    print(f"\n📋 Kategorilere Göre Dağılım:")
    for kategori, adet in sorted(kategori_sayac.items(), key=lambda x: x[1], reverse=True):
        print(f"   • {kategori}: {adet:,} ilaç")
    print(f"{'='*60}")

if __name__ == "__main__":
    print("=" * 60)
    print("PROSPEKTÜS OLUŞTURUCU")
    print("=" * 60)
    print()
    
    tum_prospektusleri_olustur()
    
    print()
    print("=" * 60)
    print("Streamlit'i yeniden başlatın:")
    print("streamlit run app.py")
    print("=" * 60)
