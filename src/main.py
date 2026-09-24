# main.py

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
def baca_utama(request: Request):
    # 1. Tambahkan daftar artikel (list of dictionaries) ke dalam data_kiriman
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
