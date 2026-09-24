# main.py

# 1. Ambil kelas utama, alat file statis, dan alat cetak Jinja2
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# 2. Buat objek aplikasi web utama
app = FastAPI()

# 3. Hubungkan folder aset statis (CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# 4. Beri tahu FastAPI di mana kita menyimpan folder cetakan HTML (templates)
templates = Jinja2Templates(directory="templates")

# 5. Aturan rute halaman utama
@app.get("/")
def baca_utama(request: Request):
    # 6. Cetak file index.html menggunakan Jinja2 dan kirim ke browser
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={}
    )
