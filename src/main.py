import json
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
# 1. Impor modul router blog dari src/blog.py
from src import blog

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# 2. DAFTARKAN ROUTER BLOG KE APLIKASI UTAMA
app.include_router(blog.router)

# Rute inti halaman utama tetap berada di main.py sebagai pintu gerbang
@app.get("/")
def baca_utama(request: Request):
    # Panggil fungsi pembantu dari berkas blog.py
    artikel_dari_json = blog.ambil_semua_artikel()
    data_kiriman = {
        "nama_pemilik": "Transformasi Anak Bangsa",
        "slogan": "Berbagai ilmu, pengetahuan, dan keterampilan tinggi bagi Genius Bangsa yang ingin bertumbuh.",
        "daftar_artikel": artikel_dari_json
    }
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"data": data_kiriman}
    )

# Rute inti tentang saya tetap berada di main.py
@app.get("/about")
def baca_tentang(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="about.html",
        context={}
    )
