# main.py

import json
# Tambahkan alat bernama Path dari modul fastapi
from fastapi import FastAPI, Request, Path
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

# ==================== PENGAMAN VALIDASI URL DENGAN REGEX ====================

@app.get("/blog/{slug}")
# Batasi input slug menggunakan fungsi Path() dan rumus REGEX di parameter 'pattern'
def baca_detail_artikel(
   request: Request, 
   slug: str = Path(..., min_length=3, max_length=50, pattern="^[a-z0-9-]+$")
):
   return {
       "pesan": "URL Anda aman dan lolos validasi!",
       "slug_yang_diklik": slug
   }

