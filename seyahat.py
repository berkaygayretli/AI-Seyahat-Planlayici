# -*- coding: utf-8 -*-
import google.generativeai as genai
import json

# 1. API Ayarları
# NOT: API anahtarını güvenliğin için bir .env dosyasında tutmanı öneririm
API_KEY = "AIzaSyDddMI7EH5Tx_w6koClmeYBTphM2B5cVuo" 
genai.configure(api_key=API_KEY)

# 2. Sistem Talimatı (AI'nın kişiliğini ve kurallarını burada belirliyoruz)
SYSTEM_INSTRUCTION = """
Sen uzman bir seyahat planlayıcısısın. Kullanıcının bütçesine, süresine ve ilgi alanlarına göre 
en mantıklı, coğrafi olarak birbirine yakın mekanlardan oluşan bir rota oluşturursun.
Cevaplarını sadece JSON formatında verirsin. Asla JSON dışında bir metin yazmazsın.Türkçe cevap ver.
"""

def generate_travel_plan(city, days, budget, interests):
    # Modeli yapılandır (1.5 Flash hem hızlı hem de işimizi fazlasıyla görür)
    model = genai.GenerativeModel(
        model_name="gemini-3-flash-preview",
        system_instruction=SYSTEM_INSTRUCTION
    )

    # Kullanıcıdan gelen ham veriyi prompt haline getiriyoruz
    user_prompt = f"""
    Şehir: {city}
    Süre: {days} Gün
    Bütçe Seviyesi: {budget}
    İlgi Alanları: {interests}

    Lütfen bu geziyi JSON formatında planla. Yapı şu şekilde olsun:
    {{
      "trip_name": "Şehir Gezisi",
      "total_days": {days},
      "itinerary": [
        {{
          "day": 1,
          "activities": [
            {{"time": "09:00", "title": "...", "location": "...", "description": "...", "estimated_cost": "..."}}
          ]
        }}
      ]
    }}
    """

    # Gemini'den yanıtı alırken JSON modunu aktif ediyoruz
    response = model.generate_content(
        user_prompt,
        generation_config={"response_mime_type": "application/json"}
    )

    # Gelen string'i Python sözlüğüne (dict) çeviriyoruz
    try:
        plan_data = json.loads(response.text)
        return plan_data
    except Exception as e:
        return {"error": f"JSON parse hatası: {str(e)}", "raw_response": response.text}

# --- TEST ETME ---
if __name__ == "__main__":
    test_plan = generate_travel_plan("İstanbul", 2, "Orta", "Tarihi yerler ve kahve dükkanları")
    print(json.dumps(test_plan, indent=2, ensure_ascii=False))