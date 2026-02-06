# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv
from google import genai
import json

# .env dosyasındaki GEMINI_API_KEY'i yükle
load_dotenv()

# Anahtarı gizli kasadan al
API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

# Gemini 3 için talimatlar
SYSTEM_INSTRUCTION = """
Sen profesyonel bir seyahat planlayıcısısın. 
SADECE aşağıdaki JSON formatında cevap ver. Türkçe karakterleri düzgün kullan.
Her aktivite için 'transport_info' alanına bir önceki yerden buraya ulaşım bilgisini yaz.
"""

def generate_travel_plan(city, days, budget):
    query = f"Şehir: {city}, Süre: {days} gün, Bütçe: {budget} TL. Ulaşım bilgileri dahil bir seyahat rotası oluştur."
    
    try:
        # BURASI SENİN DOKUNMAMIZI İSTEMEDİĞİN KRİTİK MODEL
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=query,
            config={
                'system_instruction': SYSTEM_INSTRUCTION,
                'response_mime_type': 'application/json',
            }
        )
        return json.loads(response.text)
    except Exception as e:
        return {"error": f"AI Hatası: {str(e)}"}