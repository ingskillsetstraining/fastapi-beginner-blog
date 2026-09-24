# main.py

# 1. Ambil modul bawaan Python untuk membaca file JSON
import json
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# 2. Buat fungsi pembantu untuk membaca database file JSON kita
def ambil_semua_artikel():
    # Buka file posts.json yang berada di dalam folder src
    # 'r' berarti read (hanya membaca), encoding='utf-8' memastikan teks dibaca dengan aman
    with open("src/posts.json", "r", encoding="utf-8") as file:
        # Ubah teks mentah JSON menjadi List of Dictionaries di Python
        data_artikel = json.load(file)
    return data_artikel

# 3. Aturan rute halaman utama (masih menggunakan data simulasi lama untuk sementara)
@app.get("/")
def baca_utama(request: Request):
    data_kiriman = {
        "nama_pemilik": "Transformasi Anak Bangsa",
        "slogan": "Berbagai ilmu, pengetahuan, dan keterampilan tinggi bagi Genius Bangsa yang ingin bertumbuh.",
        "daftar_artikel": [
            {"judul": "Belajar FastAPI dari Nol", "ringkasan": "Panduan awal bagi pemula untuk memahami framework Python tercepat."},
            {"judul": "Mengenal Jinja2 Template", "ringkasan": "Cara cerdas membuat halaman HTML menjadi dinamis dengan Python."},
            {"judul": "Membangun Blog Statis", "ringkasan": "Langkah praktis menyusun arsitektur web static skala industri."}
        ]
    }

    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"data": data_kiriman}
    )
