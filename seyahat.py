# -*- coding: utf-8 -*-
import os
import json
from google import genai
from dotenv import load_dotenv

# .env dosyasındaki değişkenleri (API_KEY gibi) sisteme yükler
load_dotenv()

# API anahtarını gizli dosyadan çekiyoruz
API_KEY = os.getenv("GEMINI_API_KEY")

# Gemini istemcisini başlat
client = genai.Client(api_key=API_KEY)

# AI'nın nasıl davranacağını belirleyen talimatlar
SYSTEM_INSTRUCTION = """
Sen profesyonel bir seyahat planlayıcısısın. 
SADECE aşağıdaki JSON formatında cevap ver. Türkçe karakterleri düzgün kullan.
JSON şemasında 'itinerary' altında 'day' ve 'activities' olsun. 
Her aktivitede 'time', 'title', 'description', 'transport_info', 'estimated_cost' ve 'map_url' alanları bulunmalı.
"""

def generate_travel_plan(city, days, budget):
    """
    Kullanıcıdan alınan bilgilere göre Gemini AI kullanarak 
    JSON formatında bir seyahat rotası oluşturur.
    """
    query = f"Şehir: {city}, Süre: {days} gün, Bütçe: {budget} TL. Ulaşım bilgileri dahil bir seyahat rotası oluştur."
    
    try:
        # Gemini modelini çağır
        response = client.models.generate_content(
            model="gemini-3-flash-preview", # Not: Kullandığın kütüphane sürümüne göre model adını kontrol et kanka
            contents=query,
            config={
                'system_instruction': SYSTEM_INSTRUCTION,
                'response_mime_type': 'application/json',
            }
        )
        
        # Gelen metni JSON objesine dönüştür
        return json.loads(response.text)
        
    except Exception as e:
        # Hata durumunda frontend'in anlayacağı bir hata mesajı döndür
        return {"error": f"AI Hatası: {str(e)}"}

# Test etmek istersen burayı kullanabilirsin (main.py'den çağırırken çalışmaz)
if __name__ == "__main__":
    test_plan = generate_travel_plan("İstanbul", 1, 1000)
    print(json.dumps(test_plan, indent=4, ensure_ascii=False))