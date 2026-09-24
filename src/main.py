# main.py

import json
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

def ambil_semua_artikel():
    with open("src/posts.json", "r", encoding="utf-8") as file:
        data_artikel = json.load(file)
    return data_artikel

# Aturan rute halaman utama yang baru dan bersih
@app.get("/")
def baca_utama(request: Request):
    # 1. Panggil fungsi pembantu untuk mengambil data dari posts.json
    artikel_dari_json = ambil_semua_artikel()

    # 2. Susun data kiriman, ambil daftar artikel langsung dari variabel di atas
    data_kiriman = {
        "nama_pemilik": "Transformasi Anak Bangsa",
        "slogan": "Berbagai ilmu, pengetahuan, dan keterampilan tinggi bagi Genius Bangsa yang ingin bertumbuh.",
        "daftar_artikel": artikel_dari_json  # <-- Hubungkan ke data asli JSON
    }

    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"data": data_kiriman}
    )

