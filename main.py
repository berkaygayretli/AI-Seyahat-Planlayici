# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import seyahat # seyahat.py dosyasını buraya bağladık
import json

# .env dosyasındaki verileri (API_KEY vb.) sisteme yükle
load_dotenv()

app = FastAPI()

# Frontend erişim izinleri (CORS) - Render'da sorun yaşamaman için kritik
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
def home():
    # index.html dosyasını okuyup arayüzü sunar
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.get("/planla")
def get_plan(sehir: str, gun: int, butce: int):
    # seyahat.py içindeki generate_travel_plan fonksiyonunu tetikler
    # Gemini 3 Preview modelini seyahat.py üzerinden ateşler
    plan = seyahat.generate_travel_plan(sehir, gun, butce)
    return plan