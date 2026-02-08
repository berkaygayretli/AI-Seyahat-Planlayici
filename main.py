# -*- coding: utf-8 -*-
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import seyahat # seyahat.py'yi buraya bağladık

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
def home():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.get("/planla")
def get_plan(sehir: str, gun: int, butce: int):
    # seyahat.py içindeki fonksiyonu çağırır
    plan = seyahat.generate_travel_plan(sehir, gun, butce)
    return plan