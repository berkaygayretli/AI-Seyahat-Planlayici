# -*- coding: utf-8 -*-
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from google import genai
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = "AIzaSyC2K_riIGDFyS1myREipN6PJUvBBYDGIzU"
client = genai.Client(api_key=API_KEY)

# Gemini 3 için talimatlar (Sadece rota ve ulaşım)
SYSTEM_INSTRUCTION = """
Sen profesyonel bir seyahat planlayıcısısın. 
SADECE aşağıdaki JSON formatında cevap ver. Türkçe karakterleri düzgün kullan.
Her aktivite için 'transport_info' alanına bir önceki yerden buraya ulaşım bilgisini yaz.

{
  "itinerary": [
    {
      "day": 1,
      "activities": [
        {
          "time": "09:00",
          "title": "Yer Adı",
          "location": "Bölge",
          "description": "Açıklama",
          "estimated_cost": "100 TL",
          "transport_info": "Yürüyerek 10 dk",
          "map_url": "http://google.com/maps"
        }
      ]
    }
  ]
}
"""

@app.get("/", response_class=HTMLResponse)
def home():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.get("/planla")
def get_travel_plan(sehir: str, gun: int, butce: int):
    query = f"Şehir: {sehir}, Süre: {gun} gün, Bütçe: {butce} TL. Ulaşım bilgileri dahil bir seyahat rotası oluştur."
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=query,
        config={
            'system_instruction': SYSTEM_INSTRUCTION,
            'response_mime_type': 'application/json',
        }
    )
    return json.loads(response.text)