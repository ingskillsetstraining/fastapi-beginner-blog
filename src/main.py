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

@app.get("/")
def baca_utama(request: Request):
    artikel_dari_json = ambil_semua_artikel()
    data_kiriman = {
        "nama_pemilik": "Transformasi Anak Bangsa",
        "slogan": "Berbagai ilmu, pengetahuan, dan keterampilan tinggi bagi Genius Bangsa yang ingin bertumbuh.",
        "daftar_artikel": artikel_dari_json
    }
    return templates.TemplateResponse(request=request, name="index.html", context={"data": data_kiriman})

# ==================== KODE BARU DI BAB 5 ====================

# 1. Buat rute baru dengan tanda kurung kurawal ganda {slug} pada alamatnya
@app.get("/blog/{slug}")
# 2. Tangkap variabel {slug} tersebut ke dalam parameter fungsi sebagai teks (str)
def baca_detail_artikel(request: Request, slug: str):
    # Untuk latihan awal, kita kembalikan data JSON sederhana dulu untuk melihat hasilnya
    return {
        "pesan": "Anda sedang mencoba membaca artikel",
        "slug_yang_diklik": slug
    }

